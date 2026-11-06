# Ten Boats Home: checkpoint log

Each stage's checkpoint from [the process](../../docs/process.md), with what it
caught and what changed as a result. Ticked items passed; anything that failed
first records the fix.

## Checkpoint 1: Ideation

*Artifacts: [01-ideation.md](01-ideation.md), the
[hero sheet](hero_sheet.png) drawn by `lib/cb_ana.ps`.*

- [x] Three or more concepts, each with logline, arc, shape and feasibility:
      A *Tink's Light*, B *Ten Boats Home*, C *Bear Can't Find the Quiet*.
- [x] Scoring criteria written down before the scores (payoff, page turns,
      variety, feasibility, distinctness). B won 23 to 19 and 18.
- [x] The ending answers the opening want: Ana wants Grandpa home, and he
      comes home by her light.
- [x] The heart is written down: adult idea, child feeling, question, and
      what it is not.
- [x] The heart comes from the hero's choice (carrying the lamp out), not a
      narrator. It can be guessed from the logline.
- [x] Its shape (counting, then problem and solution) differs from Moss's
      journey.
- [x] The palette is named, with one accent colour (lamp gold).
- [x] The hero sheet renders under strict lint, and Ana reads at 40 pt,
      her smallest size (wide harbour shots).

**What the hero sheet caught**, the first time it was rendered:

| Problem | Fix |
|---|---|
| The lamp glow was a huge opaque yellow disc, judged on paper instead of the night it will be seen on | Glow alpha cut from 0.16 to 0.07 a ring; the sheet now has a night swatch, and lit things are judged only on it |
| With the lamp held up, it hung over Ana's face | Raised hand moved forward (0.16 → 0.27 of her height) so the lamp hangs in front of her |
| The glow was placed by hand and missed the lantern | `cb-ana` draws its own glow, centred on the lantern's glass (`cb-glowr` sets the size) |
| Coat buttons blotted into ink smudges (a wash on a tiny circle) | Buttons are plain fills |
| Grandpa in his boat was too small to recognise | His bust is drawn at 1.5× the boat's half-length |
| `cb-lamp` named both an option and a procedure, so a call silently did the wrong thing | The procedure is now `cb-lantern` |
| Labels took whatever colour the last wash left | Every label sets ink first (a page-level rule for text too) |

**Passed.** Unlocks the manuscript.
