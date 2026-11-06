#!/usr/bin/env bash
# Blocks the push if any secret value appears in today's changes.
# Usage: secret-guard.sh <start-sha>
set -euo pipefail
START_SHA="$1"
DIFF="$(git diff "$START_SHA" -- . ; git log --format=%B "$START_SHA"..HEAD)"
found=0
for name in ANTHROPIC_API_KEY CLAUDE_CODE_OAUTH_TOKEN OPENAI_API_KEY GEMINI_API_KEY \
            XAI_API_KEY STRIPE_SECRET_KEY CLOUDFLARE_API_TOKEN; do
  value="${!name:-}"
  if [ -n "$value" ] && [ "${#value}" -ge 12 ] && grep -qF -- "$value" <<<"$DIFF"; then
    echo "::error::Secret $name found in today's changes. Push blocked."
    found=1
  fi
done
# Generic patterns for keys the workflow doesn't know about
if grep -qE '(sk_live_[0-9A-Za-z]{24,}|rk_live_[0-9A-Za-z]{24,}|sk-ant-[0-9A-Za-z_-]{20,}|sk-proj-[0-9A-Za-z_-]{20,}|xai-[0-9A-Za-z]{20,}|AIza[0-9A-Za-z_-]{30,})' <<<"$DIFF"; then
  echo "::error::Something that looks like an API key is in today's changes. Push blocked."
  found=1
fi
exit $found
