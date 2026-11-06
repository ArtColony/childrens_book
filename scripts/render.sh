#!/usr/bin/env bash
# Render book pages to PNG with pscat, lint each one, and record how long it took.
#
#   scripts/render.sh                          # every book/*.ps
#   scripts/render.sh book/01_home.ps          # just these
#   DPI=144 scripts/render.sh                  # higher resolution (default 72)
#   scripts/render.sh -D Seed=4 book/01_home.ps
#                                              # predefine /Seed 4 (pages opt in
#                                              # with `/Name where { pop } {...} ifelse`)
#   scripts/render.sh --sweep-seed 1:9 book/01_home.ps
#                                              # seed sweep: frames plus a contact
#                                              # sheet, <name>-sweep.png
#
# Output goes to $CB_RENDERS (default renders/, git-ignored) as <name>.png, and
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
[ "$have" = "$want" ] || echo "render: warning: pscat $have, but .pscat-version pins $want" >&2

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
    *) files+=("$1"); shift ;;
  esac
done
[ ${#files[@]} -gt 0 ] || files=(book/*.ps)

tmp="$(mktemp -d "${TMPDIR:-/tmp}/cb-render.XXXXXX")"
trap 'rm -rf "$tmp"' EXIT

status=0
for page in "${files[@]}"; do
  name="$(basename "$page" .ps)"
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
      echo "($page) run"
    } > "$prelude"
  fi
  if [ ${#sweep[@]} -gt 0 ]; then
    target="$out/$name-sweep.png"
    args=("${sweep[@]}" --png "$out/$name-frame.png" --contact-sheet "$target")
  else
    target="$out/$name.png"
    args=(--lint-strict --png "$target")
  fi
  start=$(date +%s)
  if pscat --page "$size" --dpi "$dpi" "${args[@]}" "$prelude"; then
    secs=$(( $(date +%s) - start ))
    printf '%s\t%s\t%s\t%ss\t%s\n' "$(date -u +%FT%TZ)" "$name" "$dpi" "$secs" "${defs[*]-}" >> "$out/timings.tsv"
    echo "render: $name ${secs}s -> $target"
  else
    echo "render: $name FAILED" >&2
    status=1
  fi
done
exit $status
}

main "$@"
