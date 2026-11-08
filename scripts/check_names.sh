#!/usr/bin/env bash
# Every cb- name must be defined in only one library. lib/cb_book.ps loads
# them all, so a second definition silently replaces the first one for every
# book (cb-glow in cb_marsh.ps once broke Ten Boats Home's lamps this way).
set -euo pipefail
cd "$(dirname "$0")/.."
dups="$(grep -ho '^/cb-[A-Za-z0-9-]*' lib/cb_*.ps | sort | uniq -d)"
if [ -n "$dups" ]; then
  for n in $dups; do echo "check_names: $n is defined in: $(grep -l "^$n[ {]" lib/cb_*.ps | tr '\n' ' ')" >&2; done
  exit 1
fi
echo "check_names: ok"
