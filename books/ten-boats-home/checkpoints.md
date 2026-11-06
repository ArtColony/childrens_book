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

## Checkpoint 2: Manuscript

### Draft 1 → panel

*Reviews: [child](reviews/02-manuscript-child.md) (Haiku, text only),
[parent](reviews/02-manuscript-parent.md) (Sonnet),
[educator](reviews/02-manuscript-educator.md) (Sonnet),
[editor](reviews/02-manuscript-writer.md) (Opus), then the advisor.*

Draft 1's own checklist passed: 244 words, one drawable moment per page, the
refrain changes at the end, the heart acted. **The panel found what the
checklist couldn't.** The editor scored it **5/10** against award-quality
picture books. The child loved the count and the reveal, but wriggled
through the long fog sentences.

### Reconciliation: every point, adopted, adapted or declined

| # | Point (reviewer) | Decision | What changed |
|---|---|---|---|
| 1 | Continuity: Ana "at the end of the pier" on p1, yet she can't see the end on p7 and carries the lamp "to the end" on p10 (parent, editor) | **Adopt** | Ana is at the *start* of the pier, by the lamp's hook. A continuity ledger is added to the page plan |
| 2 | Mama appears from nowhere on p9 (parent, educator, editor) | **Adopt** | Mama is on page 1, mending nets by the lamp, and in frame on every page through the end |
| 3 | The count is folded up too fast: 3–5 and 6–9 share pages (editor) | **Adopt** | One page for each beat. The count stalls at "Ana waits for ten" |
| 4 | Break the count *on the number*: "But ten is not a boat. Ten is fog." (editor) | **Adopt** | Used as written. It is the book's central turn and can't be bettered |
| 5 | The climax costs nothing: add a beat of failure (editor) | **Adopt, adapted** | "Nothing. Only grey." / (turn) / "So she holds it higher." The editor's two sentences become two pages, so the turn is the cost |
| 6 | Grandpa's "your light made it feel very close" reads as the brief explained (editor) | **Adopt, adapted** | "I always know the way home. But tonight, I could see it." It still says the light was a gift, not a rescue |
| 7 | Reverse the refrain at the end (editor) | **Adopt** | "And this one," he says, "is mine." Ana, who counted every boat, is the one who gets counted |
| 8 | "With a red sail", "the sky turns purple" and similar words repeat the picture (editor) | **Adopt** | "Red sail. *One!*" The sky, the sun and the masts are left to the art |
| 9 | Clichés: "sun slips down", "step by careful step", "to light the way" (editor) | **Adopt** | All cut. New concrete lines: "The gulls go quiet", "shuts its little glass door" |
| 10 | Long comma-chained sentences on the fog and lamp pages (child) | **Adopt** | Every sentence on pp. 8–13 is 13 words or fewer |
| 11 | Unknown words: *mast*, *wick*, *harbour* (child) | **Adopt / adapt** | *Mast* and *wick* are gone. *Pier*, *harbour* and *nets* stay, and the art glossary says where each is first shown clearly |
| 12 | "How will he find the harbour" is an adult construction and the scariest line (parent) | **Adopt** | "How will he find us in all this grey?" |
| 13 | Fire safety: "Mama lights the wick" reads as an open flame (parent) | **Adapt** | The text gives one concrete detail, "shuts its little glass door" and "in both hands", not instructions. The art carries the rest: a glass lantern, a rail, Mama in frame. The editor's "cut what the picture shows" and the parent's "say it in words" conflict; the ruling is to say it once, concretely, and let the picture do the rest |
| 14 | The lamp is in two places at the end, and a child carries fire home (parent) | **Adopt** | The walk-home line is cut. The wordless end page hangs the lamp back on its hook, lit |
| 15 | Mama has no beat after p10 (parent) | **Adopt** | She catches Grandpa's rope on p15 (art) and is in frame on p17 |
| 16 | A child must be able to count all ten together (educator) | **Adopt** | p15 and the end page show all ten. The ledger column "boats seen" makes it checkable |
| 17 | Boats on pp. 5–6 must be pointable, not "a forest of masts" (educator) | **Adopt** (storyboard) | p6 shows two rows, 4 + 5, with gaps and distinct sails |
| 18 | No boat on pp. 3–8 may be blue or as small as Grandpa's (educator) | **Adopt** (art rule) | Added to the storyboard checklist |
| 19 | Keep the fog cosy, not menacing (parent) | **Adopt** (art rule) | Soft, warm-grey fog, with Mama always in frame |
| 20 | The premise is familiar: *The Storm Whale*, *Hello Lighthouse*, *Harbor* (editor) | **Decline, with reasons** | The distinction is structural. It is a counting book whose count *breaks* into the problem, and the missing tenth *is* the fog. The child acts; no lighthouse keeper does it for her. The editor itself called the frame "the reason to publish it". Draft 2 now spends that frame properly instead of folding it up |
| 21 | The adult layer is thin (parent) | **Adopt** (via #7) | The refrain reversal turns "what Grandpa has" into "whom Grandpa loves", a second reading for the twentieth time through |

**Stop rule** (set before re-review, at the advisor's suggestion): a
**fresh** editor (not the one whose ideas were adopted) scores draft 2. At
8/10 or more, or after two manuscript rounds, the book moves on to the
storyboard. A fresh child reader also reads it cold.

### Draft 2 → fresh panel (round 2)

*Reviews: [fresh child](reviews/02-manuscript-draft2-child.md) (Haiku),
[fresh editor](reviews/02-manuscript-draft2-writer.md) (Opus). Both were new
agents that had not seen draft 1 or any earlier review.*

The editor's score rose from **5 to 6.5/10**, and the editor called the 7→8
turn the line "that would get the book acquired". The child now wanted to
turn every page, and said "wait, what?" at "Ten is fog".

| # | Point (reviewer) | Decision | What changed in draft 3 |
|---|---|---|---|
| 22 | The text never establishes *ten* (editor) | **Adopt** | p1: "Ten boats sail out in the morning." The picture shows all ten leaving, the blue one last |
| 23 | The lamp idea is handed to Ana, not seeded (editor) | **Adopt** | p2: Grandpa's boat "carries a lamp just like the old lamp on the pier". p10: "Then Ana thinks of Grandpa's lamp." A light can call a light |
| 24 | Open with Ana and her want, not Mama (editor) | **Adopt** | Ana is the subject of p1. Mama stays in the same sentence ("while Mama mends the nets") |
| 25 | The count rushes through the middle; the refrain is mechanical (editor) | **Adopt, adapted** | "*Three! Four! Five!* Not one of them is Grandpa's." / "*Six. Seven. Eight.* … *Nine.* Not little. Not blue. Not Grandpa's." The refrain now tightens instead of repeating |
| 26 | "How will he find us in all this grey?" states the problem as the author's set-up (editor) | **Adopt** | Cut. "The fog swallows the boats. It swallows the pier. 'Where is Grandpa?'" The sound-play the editor missed is now in the fog page |
| 27 | "Grey" three times in five pages (editor) | **Adopt** | "Grey" is gone. "Fog" is the word, and the picture carries the colour |
| 28 | The adult does every physical act (editor) | **Adopt** | Ana lifts the lamp off its hook herself. Mama only strikes the match (safety) and catches the rope |
| 29 | "I always know the way home…" reads as a disclaimer; "this one is mine" waters down the first reversal (editor) | **Adopt** | Both are cut. Grandpa: "Ten boats home, and one little light." Ana: "*Eleven*." The count goes past the title, and the book ends on the child's voice |
| 30 | "Ten is fog" will confuse a literal listener (fresh child) | **Keep the line, fix it in the art** | The confusion *is* the hook ("wait, what?"). The picture must make the metaphor literal: fog standing exactly where the tenth boat should be. Added to the storyboard checklist |
| 31 | p1 and the lamp page are long, wiggly sentences (fresh child) | **Adopt** | p1 is now two short sentences. The lamp page is "Mama lights it. *Click* goes the little glass door. And out they go, into the fog." |
| 32 | *Pier*, *nets* unfamiliar (fresh child) | **Art** | They are shown plainly on p1 (the glossary for the art) |

**Draft 3:** 206 words, longest page 25 words, fog-to-lamp sentences at most
11 words.

**Checkpoint 2 passed by the stop rule** (two manuscript rounds). Draft 3
was not re-scored; the editor's own estimate was that A–C make it "an 8".
What remains is music on every page, and that is best judged again at the
storyboard, when words and pictures can be read together. **Unlocks the
storyboard.**
