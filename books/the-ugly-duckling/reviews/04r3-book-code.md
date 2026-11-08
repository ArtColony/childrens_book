# Review round 3: code (Opus; the round 2 commit only)

1. **Blocker: the new `cb-glow` in `cb_marsh.ps` replaced `cb_ana.ps`'s 3-operand `cb-glow`** for every book. Ten Boats Home's lamp pages failed with `stackunderflow`. *Fixed:* renamed to `cb-pglow`. A new `scripts/check_names.sh` (now in CI) fails on any `cb-` name defined in two libraries. (Our own "byte-identical" check had missed it: the failed bind left the old PDF in place. The check now deletes the PDF first.)
2. **p7:** `cb-glow` washed inside a squashed `cb-local` frame, which gave stepped bands. *Fixed:* `cb-pglowsq` builds the path squashed and washes at page scale.
3. **The `/sad` brow stuck out above the head** on grown ducklings (fixed offsets, shrinking head). *Fixed:* scaled by the head radius.
4. **The brow leaked `setlinecap` and `setlinewidth`.** *Fixed:* `gsave`/`grestore`.
5. **p14:** the sun's spray reached the text band. *Fixed:* a smaller nozzle.

**Checked clean:** `cb-grain` (the other books are unaffected), the option resets, the wisp winding, and the dict sizes.
