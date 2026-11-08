# Review round 2: code (Opus; the diff of PRs #4 and #5 only)

1. **The new tuft punched a hole in the duckling's head** (`cb-duckling`). The wisp ran clockwise and the head counter-clockwise, so nonzero fill cancelled where they overlapped. This was on every page with the duckling. *Fixed* (the wisp is reversed).
2. **p2:** the second "Crack!" fell between the leaves, cream on pale sky. *Fixed* (moved onto the leaf).
3. **p9:** the folio sat on the dark doorstep. *Fixed* (paper-coloured folio).
4. **p17:** the front swan's head touched a neck. *Fixed* (nudged left).

**Checked clean:** the reed fix, the wing dict, `cb-pmist`, `cb-icelo`, the p12 snow, and no leaks between pages.

**PDF size, measured** (13.46 MB):

| Cost | Fix | Saving | Visual |
|---|---|---|---|
| Sky strokes 5.4 MB | `/Pitch 8` on `pkbroad` | 2.2 MB | mean diff 0.19/255 |
| Paper grain 3.7 MB | `/Grain 0` (paint covers it) | 3.7 MB | pixel-identical |
| Mist spray 1.8 MB | `/Density 90` | 0.7 MB | mean diff 0.06/255 |

*All three applied: 6.5 MB.* Grain is a new `cb-grain` option (default 0.55), set to 0 only in this book, so the other books are byte-identical.
