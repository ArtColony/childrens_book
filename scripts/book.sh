#!/usr/bin/env bash
# Bind a directory of page programs into one PDF, in file-name order.
#
#   scripts/book.sh books/moss-goes-to-the-sea            # -> renders/moss-goes-to-the-sea.pdf
#   scripts/book.sh books/moss-goes-to-the-sea --commit   # -> books/<slug>/<slug>.pdf (the committed copy)
#   scripts/book.sh books/lamp-for-the-dark/03-storyboard out.pdf
#                                                         # any directory of pages
#   scripts/book.sh                                       # every book, into renders/
#
# A book directory means its pages/ subdirectory. Each page runs inside its
# own save ... restore, so one page's options, seeds and definitions never
# leak into the next. The run is strictly linted and must produce exactly one
# PDF page per .ps file.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
out="${CB_RENDERS:-renders}"
command -v pscat >/dev/null 2>&1 || { echo "book: pscat not found on PATH; see README.md" >&2; exit 2; }

bind() { # dir pdf
  local dir="$1" pdf="$2" tmp n start secs
  local pages=("$dir"/*.ps)
  mkdir -p "$(dirname "$pdf")"
  tmp="$(mktemp -d "${TMPDIR:-/tmp}/cb-book.XXXXXX")"
  # the PDF's title: the first page's %%Title, up to its first comma
  local title
  title="$(awk -F': ' '/^%%Title:/ { sub(/,.*/, "", $2); print $2; exit }' "${pages[0]}")"
  {
    echo "%!PS-Adobe-3.0"
    [ -n "$title" ] && echo "%%Title: $title"
    echo "%%Pages: ${#pages[@]}"
    for p in "${pages[@]}"; do echo "save ($p) run restore"; done
  } > "$tmp/book.ps"
  start=$(date +%s)
  pscat --page 612x612 --lint-strict --pdf "$pdf" "$tmp/book.ps"
  secs=$(( $(date +%s) - start ))
  rm -rf "$tmp"
  # one PDF page per page file (counts /Type /Page objects, not /Pages)
  n="$(LC_ALL=C grep -a -o '/Type */Page[^s]' "$pdf" | wc -l | tr -d ' ')"
  if [ "$n" != "${#pages[@]}" ]; then
    echo "book: expected ${#pages[@]} pages, $pdf has $n" >&2
    return 1
  fi
  echo "book: ${#pages[@]} pages in ${secs}s -> $pdf ($(du -h "$pdf" | cut -f1))"
}

if [ $# -eq 0 ]; then
  for b in books/*/; do b="${b%/}"; bind "$b/pages" "$out/$(basename "$b").pdf"; done
  exit 0
fi

dir="${1%/}"; shift
if [ -d "$dir/pages" ]; then
  slug="$(basename "$dir")"
  pdf="$out/$slug.pdf"
  [ "${1-}" = "--commit" ] && pdf="$dir/$slug.pdf"
  dir="$dir/pages"
else
  pdf="$out/$(basename "$(dirname "$dir")")-$(basename "$dir").pdf"
fi
[ $# -gt 0 ] && [ "$1" != "--commit" ] && pdf="$1"
bind "$dir" "$pdf"
