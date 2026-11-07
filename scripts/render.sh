#!/usr/bin/env bash
# Render book pages to PNG with pscat, lint each one, and record how long it took.
#
#   scripts/render.sh                          # every page of every book
#   scripts/render.sh books/moss-goes-to-the-sea/pages      # one book's pages
#   scripts/render.sh books/ten-boats-home/03-storyboard # its storyboard
#   scripts/render.sh books/moss-goes-to-the-sea/pages/01_home.ps   # one page
#   DPI=144 scripts/render.sh                  # higher resolution (default 72)
#   scripts/render.sh -D Seed=4 books/.../pages/01_home.ps
#                                              # predefine /Seed 4 (pages opt in
#                                              # with `/Name where { pop } {...} ifelse`)
#   scripts/render.sh --sweep-seed 1:9 books/.../pages/01_home.ps
#                                              # seed sweep: frames plus a contact
#                                              # sheet, <name>-sweep.png
#
# Output goes to $CB_RENDERS (default renders/, git-ignored) as
# <book>/<stage>/<name>.png (books/<book>/<stage>/<name>.ps), and
# timings are appended to timings.tsv there. The page size comes from the
# page's %%BoundingBox (612x612, an 8.5 in square). Lint is strict: a stack or
# gsave leak fails the run. Exits nonzero on any error.
# For the whole book as one PDF, use scripts/book.sh.
set -euo pipefail

main() {
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"   # pages load (lib/...) relative to the repo root

dpi="${DPI:-72}"
out="${CB_RENDERS:-renders}"
mkdir -p "$out"

if ! command -v pscat >/dev/null 2>&1; then
  echo "render: pscat not found on PATH; see README.md" >&2
  exit 2
fi
want="$(cat .pscat-version)"
have="$(pscat --version | awk '{print $2}')"
if [ "$have" != "$want" ]; then
  # the pin is what makes the committed PDFs reproducible: refuse, unless told
  echo "render: pscat $have, but .pscat-version pins $want (CB_ALLOW_PSCAT=1 to override)" >&2
  [ "${CB_ALLOW_PSCAT:-}" = 1 ] || exit 2
fi

# a repo lib/ file named like a built-in would shadow pscat's own
for f in lib/*.ps; do
  case "$(basename "$f")" in
    cb_*) ;;
    *) echo "render: $f: repo libraries must be named lib/cb_*.ps" >&2; exit 2 ;;
  esac
done

defs=() sweep=() files=()
while [ $# -gt 0 ]; do
  case "$1" in
    -D) defs+=("$2"); shift 2 ;;
    --sweep-seed) sweep=(--sweep-seed "$2"); shift 2 ;;
    -*) echo "render: unknown option $1" >&2; exit 2 ;;
    *) if [ -d "$1" ]; then files+=("${1%/}"/*.ps); else files+=("$1"); fi; shift ;;
  esac
done
if [ ${#files[@]} -eq 0 ]; then
  shopt -s nullglob
  files=(books/*/pages/*.ps)
  shopt -u nullglob
fi

tmp="$(mktemp -d "${TMPDIR:-/tmp}/cb-render.XXXXXX")"
trap 'rm -rf "$tmp"' EXIT

status=0
for page in "${files[@]}"; do
  name="$(basename "$page" .ps)"
  stage="$(basename "$(dirname "$page")")"
  book="$(basename "$(dirname "$(dirname "$page")")")"
  dest="$out/$book/$stage"
  mkdir -p "$dest"
  size="$(awk '/^%%BoundingBox:/ { print $4-$2 "x" $5-$3; exit }' "$page")"
  size="${size:-612x612}"
  # -D values go in a prelude that then runs the page; without them the page
  # runs directly, so error reports give its own line numbers
  prelude="$page"
  if [ ${#defs[@]} -gt 0 ]; then
    prelude="$tmp/$name.ps"
    {
      echo "%!PS-Adobe-3.0"
      for d in "${defs[@]}"; do echo "/${d%%=*} ${d#*=} def"; done
      printf '(%s) run\n' "$(printf '%s' "$page" | sed 's/[\\()]/\\&/g')"
    } > "$prelude"
  fi
  if [ ${#sweep[@]} -gt 0 ]; then
    target="$dest/$name-sweep.png"
    args=("${sweep[@]}" --lint-strict --png "$dest/$name-frame.png" --contact-sheet "$target")
  else
    target="$dest/$name.png"
    args=(--lint-strict --png "$target")
  fi
  start=$(date +%s)
  if pscat --page "$size" --dpi "$dpi" "${args[@]}" "$prelude"; then
    secs=$(( $(date +%s) - start ))
    printf '%s\t%s\t%s\t%ss\t%s\n' "$(date -u +%FT%TZ)" "$book/$stage/$name" "$dpi" "$secs" "${defs[*]-}" >> "$out/timings.tsv"
    echo "render: $name ${secs}s -> $target"
  else
    echo "render: $name FAILED" >&2
    status=1
  fi
done
exit $status
}

main "$@"
