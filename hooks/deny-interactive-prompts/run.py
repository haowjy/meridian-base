#!/usr/bin/env python3
"""Deny Codex shell commands likely to block on interactive auth prompts."""

from __future__ import annotations

import json
import os
import re
import shlex
import sys
from pathlib import PurePath

PG_COMMANDS = {"createdb", "dropdb", "psql", "pg_dump", "pg_restore"}
SSH_COMMANDS = {"ssh", "scp", "sftp"}
GIT_NETWORK_COMMANDS = {"clone", "fetch", "pull", "push"}
SHELL_TOOLS = {
    "",
    "Bash",
    "Shell",
    "bash",
    "shell",
    "exec_command",
    "unified_exec",
    "commandExecution",
}
SEPARATORS = {";", "&", "&&", "|", "||", "\n", "(", ")"}
CONTROL_WORDS = {"if", "then", "do", "else", "elif", "while", "until", "for", "case"}
REDIRECTS = {"<", ">", "<<", ">>", "<<<", "<>", ">&", "<&", "2>", "2>>"}
SUDO_OPTIONS_WITH_ARG = {
    "-A",
    "-a",
    "-b",
    "-C",
    "-c",
    "-D",
    "-g",
    "-h",
    "-p",
    "-R",
    "-r",
    "-T",
    "-t",
    "-U",
    "-u",
}
GIT_OPTIONS_WITH_ARG = {
    "-C",
    "-c",
    "--config-env",
    "--git-dir",
    "--work-tree",
    "--namespace",
    "--exec-path",
}


def deny(reason: str) -> None:
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        },
        sys.stdout,
    )
    sys.stdout.write("\n")


def payload_command(payload: object) -> tuple[str, str]:
    if not isinstance(payload, dict):
        return "", ""

    tool_name = str(payload.get("tool_name") or payload.get("toolName") or "")
    for input_key in ("tool_input", "toolInput"):
        tool_input = payload.get(input_key)
        if isinstance(tool_input, dict):
            command = tool_input.get("command") or tool_input.get("cmd")
            if isinstance(command, str):
                return tool_name, command
    for command_key in ("command", "cmd"):
        command = payload.get(command_key)
        if isinstance(command, str):
            return tool_name, command
    return tool_name, ""


def tokens_for(command: str) -> list[str]:
    lexer = shlex.shlex(command, posix=True, punctuation_chars=";&|()<>\n")
    lexer.whitespace_split = True
    lexer.commenters = ""
    try:
        return list(lexer)
    except ValueError:
        # Incomplete quotes are invalid shell anyway; fail open here so Codex
        # reports the real shell syntax error instead of a hook parse error.
        return []


def basename(token: str) -> str:
    return PurePath(token).name


def is_assignment(token: str) -> bool:
    return re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", token) is not None


def command_spans(tokens: list[str]) -> list[list[str]]:
    spans: list[list[str]] = []
    current: list[str] = []
    expect_command = True
    skip_redirect_target = False

    for token in tokens:
        if token in SEPARATORS:
            if current:
                spans.append(current)
                current = []
            expect_command = True
            skip_redirect_target = False
            continue

        if token in REDIRECTS or re.match(r"^\d*(<<|<<<|>>|>|<|<>|>&|<&)$", token):
            skip_redirect_target = True
            continue

        if skip_redirect_target:
            skip_redirect_target = False
            continue

        if expect_command and token in CONTROL_WORDS:
            continue

        current.append(token)
        if not (expect_command and is_assignment(token)):
            expect_command = False

    if current:
        spans.append(current)
    return spans


def split_env_assignments(span: list[str]) -> tuple[dict[str, str], list[str]]:
    assignments: dict[str, str] = {}
    i = 0
    while i < len(span) and is_assignment(span[i]):
        key, value = span[i].split("=", 1)
        assignments[key] = value
        i += 1
    return assignments, span[i:]


def span_text(span: list[str]) -> str:
    return " ".join(shlex.quote(token) for token in span)


def has_pg_failfast(assignments: dict[str, str], argv: list[str]) -> bool:
    return bool(
        os.environ.get("PGPASSWORD")
        or os.environ.get("PGPASSFILE")
        or assignments.get("PGPASSWORD")
        or assignments.get("PGPASSFILE")
        or "--no-password" in argv
        or "-w" in argv
        or any(re.search(r"postgres(?:ql)?://[^\s@]+:[^\s@]+@", token) for token in argv)
    )


def sudo_has_failfast(span: list[str]) -> bool:
    # Only accept sudo flags before the sudo command operand. `sudo apt -n` is
    # not safe because `-n` belongs to apt, not sudo.
    i = 1
    while i < len(span):
        token = span[i]
        if token == "--":
            return False
        if token in {"-n", "--non-interactive"}:
            return True
        if token.startswith("--"):
            if token in {"--user", "--group", "--host", "--prompt", "--chdir", "--chroot"}:
                i += 2
            else:
                i += 1
            continue
        if token.startswith("-") and token != "-":
            chars = token[1:]
            j = 0
            while j < len(chars):
                ch = chars[j]
                if ch == "n":
                    return True
                if f"-{ch}" in SUDO_OPTIONS_WITH_ARG:
                    # The rest of this token, or the next token, is this
                    # option's argument. Do not scan attached arguments for n.
                    i += 1 if j + 1 < len(chars) else 2
                    break
                j += 1
            else:
                i += 1
            continue
        return False
    return False


def has_ssh_failfast(span: list[str]) -> bool:
    text = span_text(span)
    return bool(re.search(r"BatchMode\s*=\s*yes", text) or basename(span[0]) == "sshpass")


def has_git_failfast(assignments: dict[str, str]) -> bool:
    return bool(
        os.environ.get("GIT_TERMINAL_PROMPT") == "0"
        or assignments.get("GIT_TERMINAL_PROMPT") == "0"
    )


def has_git_ssh_failfast(assignments: dict[str, str], span: list[str]) -> bool:
    return bool(
        has_ssh_failfast(span)
        or re.search(r"BatchMode\s*=\s*yes", assignments.get("GIT_SSH_COMMAND", ""))
    )


def git_subcommand(span: list[str]) -> str:
    i = 1
    while i < len(span):
        token = span[i]
        if token == "--":
            i += 1
            break
        if token in GIT_OPTIONS_WITH_ARG:
            i += 2
            continue
        if any(
            token.startswith(f"{option}=")
            for option in GIT_OPTIONS_WITH_ARG
            if option.startswith("--")
        ):
            i += 1
            continue
        if token.startswith("-"):
            i += 1
            continue
        break
    return span[i] if i < len(span) else ""


def git_uses_ssh(span: list[str]) -> bool:
    return bool(re.search(r"(git@|ssh://|[A-Za-z0-9_.-]+@[A-Za-z0-9_.-]+:)", span_text(span)))


def rsync_uses_remote(span: list[str]) -> bool:
    return any(":" in token and not token.startswith("--") for token in span[1:]) or any("ssh" in token for token in span[1:])


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    tool_name, command = payload_command(payload)
    if not command or tool_name not in SHELL_TOOLS:
        return 0

    spans = command_spans(tokens_for(command))
    for span in spans:
        if not span:
            continue
        assignments, argv = split_env_assignments(span)
        if not argv:
            continue
        executable = basename(argv[0])

        if executable in PG_COMMANDS and not has_pg_failfast(assignments, argv):
            deny("Blocked: PostgreSQL CLI may prompt for a password. Add PGPASSWORD/PGPASSFILE or -w/--no-password so it fails fast instead of hanging Codex.")
            return 0

        if executable == "sudo" and not sudo_has_failfast(argv):
            deny("Blocked: sudo may prompt for a password. Use sudo -n/--non-interactive before the command or avoid sudo in Codex commands.")
            return 0

        if executable in {"su", "passwd"}:
            deny("Blocked: command is likely to require an interactive password prompt. Use a noninteractive/fail-fast alternative.")
            return 0

        if executable in SSH_COMMANDS and not has_ssh_failfast(argv):
            deny("Blocked: SSH-family command may prompt for auth. Add BatchMode=yes or another noninteractive auth mechanism.")
            return 0

        if executable == "rsync" and rsync_uses_remote(argv) and not has_ssh_failfast(argv):
            deny("Blocked: rsync over SSH may prompt for auth. Add BatchMode=yes or another noninteractive auth mechanism.")
            return 0

        if executable == "git" and git_subcommand(argv) in GIT_NETWORK_COMMANDS:
            if not has_git_failfast(assignments):
                deny("Blocked: git network command may prompt for credentials. Add GIT_TERMINAL_PROMPT=0 or use configured noninteractive auth.")
                return 0
            if git_uses_ssh(argv) and not has_git_ssh_failfast(assignments, argv):
                deny("Blocked: git over SSH may prompt for auth. Add GIT_SSH_COMMAND with BatchMode=yes or another noninteractive auth mechanism.")
                return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
