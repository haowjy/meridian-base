#!/bin/bash
# Shell wrapper because Mars executes hook scripts with bash.
set -euo pipefail

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)

if ! command -v python3 >/dev/null 2>&1; then
  cat <<'JSON'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Blocked: python3 is required to evaluate the interactive prompt guard safely."}}
JSON
  exit 0
fi

exec python3 "$script_dir/run.py"
