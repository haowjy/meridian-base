#!/bin/bash
# Deny generic Agent(subagent_type: "claude") spawns.
# Named agents (design-lead, tech-lead, etc.) are allowed.
# Forces use of meridian spawn for codebase work.

if [ "$CLAUDE_TOOL_NAME" != "Agent" ]; then
  exit 0
fi

subagent_type=$(echo "$CLAUDE_TOOL_INPUT" | jq -r '.subagent_type // ""')

if [ "$subagent_type" = "claude" ] || [ -z "$subagent_type" ]; then
  echo "Blocked: generic Agent(claude) spawn. Use a named agent or meridian spawn instead." >&2
  exit 2
fi

exit 0
