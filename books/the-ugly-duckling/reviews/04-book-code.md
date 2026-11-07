# Stage 4 book: code review (Claude Opus, standing in for Codex)

Codex was unavailable, so this review was done by a Claude reviewer given
the code and CLAUDE.md but none of our notes. All 19 pages pass strict
lint, and `cb_book.ps` leaves the stack empty. No operator shadowing,
balanced gsave/grestore and clips, every rand seeded.

1. **The 21 MB PDF is `cb-pmist`** (`lib/cb_marsh.ps`): about 1 MB of
   vector spray per call, from `pkwet`. 10 pages call it. A plain spray
   costs about 170 KB. *Fixed: 13 MB.*
2. **p12: snow falls into the text band** (`cb-psnow` up to y 600, text
   from 590). *Fixed.*
3. **Reed path points in the wrong order** (`cb-preeds`): base → tip →
   middle, a hooked double stroke with the taper on the middle. *Fixed.*
4. **The committed PDF was stale.** *Rebound.*
5. **Palatino, not the house NewCenturySchlbk** (low). *Kept as a per-book
   choice, recorded in checkpoint 4.*
6. **`cb-swan-wingshape` wrote into the current dict** (low). *Fixed.*
7. **Dead code in `cb-ptree`** (cosmetic). *Removed.*
8. `build_site.py` STAGES: no defect. The stage labels "1 · Interpretation"
   and "1b · Style" are uneven (a nit).
