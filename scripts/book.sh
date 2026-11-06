#!/usr/bin/env bash
# Bind every page in book/ into one PDF, in file-name order.
#
#   scripts/book.sh                    # -> renders/moss-goes-to-the-sea.pdf
#   scripts/book.sh out.pdf            # somewhere else
#
# Each page runs inside its own save ... restore, so one page's options,
# seeds and definitions never leak into the next. The run is strictly linted
# and must produce exactly one PDF page per book/*.ps file.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

out="${CB_RENDERS:-renders}"
pdf="${1:-$out/moss-goes-to-the-sea.pdf}"
mkdir -p "$(dirname "$pdf")"

command -v pscat >/dev/null 2>&1 || { echo "book: pscat not found on PATH; see README.md" >&2; exit 2; }

tmp="$(mktemp -d "${TMPDIR:-/tmp}/cb-book.XXXXXX")"
trap 'rm -rf "$tmp"' EXIT

pages=(book/*.ps)
{
  echo "%!PS-Adobe-3.0"
  echo "%%Title: Moss Goes to the Sea"
  echo "%%Pages: ${#pages[@]}"
  for p in "${pages[@]}"; do echo "save ($p) run restore"; done
} > "$tmp/book.ps"

start=$(date +%s)
pscat --page 612x612 --lint-strict --pdf "$pdf" "$tmp/book.ps"
secs=$(( $(date +%s) - start ))

# one PDF page per page file (counts /Type /Page objects, not /Pages)
n="$(LC_ALL=C grep -a -o '/Type */Page[^s]' "$pdf" | wc -l | tr -d ' ')"
if [ "$n" != "${#pages[@]}" ]; then
  echo "book: expected ${#pages[@]} pages, $pdf has $n" >&2
  exit 1
fi
echo "book: ${#pages[@]} pages in ${secs}s -> $pdf ($(du -h "$pdf" | cut -f1))"
