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

## Checkpoint 3: Storyboard

*Artifacts: [03-storyboard.md](03-storyboard.md) and the
[contact sheet](storyboard_sheet.png). Reviews:
[artist](reviews/03-storyboard-artist.md) (Sonnet, all 19 images),
[educator](reviews/03-storyboard-educator.md) (Sonnet, counted every boat),
[child](reviews/03-storyboard-child.md) (Haiku, the pictures only).*

**The panel's verdict on round 1 was "revise before painting".** The
storyboard caught the book's biggest remaining problems, every one of them
invisible in the manuscript:

| # | Point (reviewer) | Decision | What changed in round 2 |
|---|---|---|---|
| 33 | **"Eleven" has nothing to count** ("Who is the eleven?") (child; educator: "about 8 boats") | **Adopt, in the art** | p17 lays the count out for a finger: ten boats in one row (the nine and the little blue one), and at the end of the row, at the same height, Ana's lamp is the eleventh thing. The text stays as it is |
| 34 | **"Not little" has no visual meaning:** Grandpa's boat was never smaller than the others (educator) | **Adopt** | The nine are bigger (s 20/26) and Grandpa's is smaller (s 13–15) wherever they share a page, including in its empty mooring |
| 35 | Teal reads as blue, so "not blue" is shaky (educator) | **Adopt** | The sixth sail is lime |
| 36 | **Mama missing** on pp. 2, 7, 9, 14, 17, and only a hand on 16 (all three) | **Adopt** | Mama is in frame on every page. On p9 her hand is on Ana's shoulder |
| 37 | **Ana holds the lamp in one hand** (artist, safety) | **Adopt** | `cb-ana` draws the far arm whenever she carries the lamp, so it is always in both hands |
| 38 | **p8: the fog reads as a moon** and hides the pink boat; a child counts 8 (educator, artist) | **Adopt** | A soft bank of overlapping washes stands on the tenth mooring, which moved right (x 572) so no boat is covered. The nine fade behind a thinner fog |
| 39 | **p13 is the weakest key page** (artist) | **Adopt** | The camera pushes in (Ana 130 → 200 pt). A new pose, `cb-arm /top`, has both arms straight up on tiptoe, and the glow is the largest in the book |
| 40 | **Light only reads against dark:** the fog-night pages were pale grey, so the gold was beige and white text illegible (artist, child) | **Adopt** | A `/fognight` light (cool blue-grey, L about 35%) and a darker fog colour for pp. 12–14 |
| 41 | p7 is a copy of p6; the gulls are specks that could be counted as boats (artist, educator) | **Adopt** | p7 turns the camera to the open sea: Ana small, alone at the rail, three large gulls on the posts, and Mama behind |
| 42 | Rows cut by the rail, boats hidden by posts and figures (educator) | **Adopt** | The moorings are raised above the rail and placed clear of the lamp post and the figures |
| 43 | Nets read as a basket (educator, artist) | **Adopt** | A wider net draped over the rail, with a diamond mesh |
| 44 | p14: the boat is fully visible, so nothing "blinks" (artist) | **Adopt** | The boat is a faded shape behind the fog, and only its lamp is sharp: a spark answering Ana's |
| 45 | p16: Ana floats, and the ten boats are absent (artist, educator) | **Adopt** | She sits on Grandpa's lifted arm (`cb-gparm /lift`), with ten boats behind |
| 46 | p17: no grin (artist) | **Adopt** | `cb-grin` |
| 47 | Cover subtitle "painted in PostScript" is a production note (artist) | **Adopt** | "a counting book" |
| 48 | p18 has no words, so "there's nothing to ask for" (child) | **Decline** | The editor asked for a wordless end page. On the last page, a child looking for the blue boat in its mooring and the lamp back on its hook *is* the asking |
| 49 | pp. 3–8 are six wide shots in a row, breaking the shot-variety rule (author's own check) | **Adapt** | p7 now breaks the run (a new camera). The counting pages keep one camera deliberately, so each returning boat is found in the same place: continuity outranks variety for a counting book |

**Checkpoint 3 passed** after round 2 (the stop rule: two rounds). The
round-2 sheet was checked against every row above. **Unlocks painting.**

## Checkpoint 4: Book

*Reviews of the first painted pass, all fresh readers given the pages
rasterized from the print PDF:
[editor](reviews/04-book-writer.md) (Opus),
[artist](reviews/04-book-artist.md) (Sonnet),
[parent](reviews/04-book-parent.md) (Sonnet),
[child](reviews/04-book-child.md) (Haiku). Then the advisor.*

**Mechanical checks, which passed:** every page renders under strict lint; one
PDF page per file (19); 0.6 MB a page (budget 1 MB); it binds in about 13 s;
binding twice gives the same bytes.

**Value check.** Rough mode predicted positions but not values. Painted, the
p8 fog bank became a hard white cloud, p14's blue boat fogged to grey, and
p16's glow crowded the text. All three were fixed before the panel saw the
book, and rough mode was then calibrated to the paint's real opacity (see
`docs/process.md`).

**The panel's verdict on the first painted pass:** the editor gave **6.5/10**,
"the text is about 7.5; the pictures pull it down". The child counted every
boat correctly through ten, then asked again **"Why is it eleven?"**

| # | Point (reviewer) | Decision | What changed |
|---|---|---|---|
| 50 | **"Eleven" is still ambiguous**: the lamp sat *above* the row, not in it (child, parent, editor) | **Adopt, in the art** | p17 is rebuilt: ten boats in one row, and in the *same* row, at the same spacing, the lamp stands on the last mooring post. The family is whole on the pier, Ana grinning and pointing along the row. The words stay. The parent's "if you count my lamp" is declined: explaining a joke kills it |
| 51 | **The payoff is the weakest version of the refrain** (editor); "And this one is Grandpa's" reads as ten *plus* Grandpa's (parent) | **Adopt** | p15: "*Ten!* Little. Blue. *Grandpa's.*" It inverts "Not little. Not blue. Not Grandpa's." word for word, and fixes the arithmetic |
| 52 | **The reunion is staged at a distance:** a speck of a boat, no Grandpa (editor, artist) | **Adopt** | p15 is close and low: a big blue boat with Grandpa waving, two lamps answering each other |
| 53 | **Two lamps at once:** the old lamp still on its hook while Ana holds it (artist, editor) | **Adopt** | A real continuity bug: p15 drew the harbour's hook lamp. The hook is empty from p10 until the end page |
| 54 | **The fear is never drawn:** the same placid face at "Where is Grandpa?" (editor, artist) | **Adopt** | `cb-worry` gives a raised, slanted brow and a small open mouth, used on p9 |
| 55 | **Ana reads as holding the lamp in one hand** (artist): the far arm was hidden behind her coat | **Adopt** | The far arm crosses the front of the coat, a second sleeve and hand on the handle |
| 56 | **The glow is muddy khaki**, built from hard concentric bands (artist) | **Adopt** | Seven faint rings in a pale warm gold, plus a two-step core. It reads as light, lighter than the fog around it |
| 57 | **Mama's hand never touches Ana** at the pier's end (parent) | **Adopt** | `cb-mamahand` aims her hand at Ana's shoulder on pp. 12–15 and the cover, and she is drawn over the glow so she isn't faded |
| 58 | **The middle sags:** three pages of instructions; "Then Ana thinks of Grandpa's lamp" tells a thought (editor) | **Adopt** | p10: "Ana looks up at the old lamp." p11: "Mama lights it. *Click!* And out they go, into the fog." |
| 59 | p2's "She waits for one most of all" clashes with the next page's "One!" (parent); the sentence is long (child) | **Adopt** | "Most of all, she waits for Grandpa's boat. It is little. It is blue. And it carries a lamp, just like the old lamp on the pier." |
| 60 | **Representation:** everyone has the same peach skin (parent) | **Adopt** | The family has warm brown skin and dark hair; the hero sheet is re-rendered |
| 61 | The cover shows Grandpa's boat, which spoils the reveal (parent) | **Adopt** | The cover shows Ana and Mama with the lit lamp, and no boat |
| 62 | p7's boats vanish, which reads as a continuity break (editor); the gulls read as petals (artist) | **Adopt** | p7 returns to the harbour view with the nine moored. The gulls have folded grey wings, dark tips and beaks |
| 63 | p8's fog bank is a ball (artist) | **Adopt** | Low, wide, flat banks of mist that thicken toward the empty mooring |
| 64 | Foreground boats sit under the page number; dark text on mid-violet (artist) | **Adopt** | Boats raised; p5's text is cream |
| 65 | p17's sky is lighter than the night before it (artist) | **Adopt** | The night pages use a dark night fog; p17 is a clear deep night |
| 66 | Grandpa's boat reads grey in the fog (artist) | **Adopt** | It is blue all over, hull and sail (`cb-hullc`) |
| 67 | "swallows" will wake a 4-year-old (parent) | **Decline** | The child reviewers loved the suspense, and it resolves within four pages. The fog's soft drawing keeps it gentle |
| 68 | "Light it, quick!" is panicky (parent) | **Decline** | It is the one moment of urgency, and the editor kept it. Mama's calm *Click!* answers it |
| 69 | Add "Ten boats. One lamp. Goodnight." to the end page (parent) | **Decline** | The editor's and artist's case for a wordless coda stands: the child finds the blue boat in its mooring and the lamp on its hook |
| 70 | Mama is carer, Grandpa is captain (parent) | **Noted** | Mama mends nets (she fishes too) and does the one dangerous job, the match. A fuller fix is a stage 1 cast question, logged for the reflection |

**Draft 4:** 192 words.

### Finished book, round 2

*Fresh reviews of the revised book: [editor](reviews/04-book-r2-writer.md)
(Opus), [child](reviews/04-book-r2-child.md) (Haiku); a Codex review was also
run.*

The editor's score rose from **6.5 to 7/10**: "the structure, the refrain and
its flip, the 'Ten is fog' turn and the light-and-sky art are all at a
professional level". The child matched every count from one to ten, and
then found a real bug on the last count.

| # | Point (reviewer) | Decision | What changed |
|---|---|---|---|
| 71 | **p17: "I count eight boats and one lamp. That's nine."** Two boats in the row were hidden behind the grown-ups' heads (child) | **Adopt** | The row is raised clear of everyone's heads: ten boats and the lamp, eleven things in one line, and nothing in front of them |
| 72 | **The joke is explained before Ana makes it:** "and one little light" (editor) | **Adopt** | p16: "Grandpa lifts Ana up. 'I saw your light,' he says. 'Ten boats home.'" Grandpa credits the light; Ana finds the eleven herself. The "lamp and all" description is cut |
| 73 | **The reveal is spent a page early:** the blue boat clearly drawn on the blink page (editor) | **Adopt in the art, keep the words** | On p14 the boat is now a ghost in thicker fog, and only its light is sharp; its colour and Grandpa arrive on the turn. The words stay: "A little light. A little boat. A little *blue* boat." is the line three readers named as the book's music, and it narrows like the fog thinning |
| 74 | Slow the count; merge the middle pages (editor) | **Decline for this edition** | That would restructure the book around one reader's preference. Two counting pages are deliberately quick, a speeding count while the sun goes down, and earlier panels found the middle pages earned by the lamp |
| 75 | Stiff figures; the face doesn't act fear and joy (editor, three panels) | **Logged as the book's ceiling** | This is the house style's limit: profile figures built from simple shapes. The next book should prove expressive faces and bodies on its hero sheet *before* writing (a stage 1 lesson; see the reflection) |
| 76 | Mama's hand on Ana in nearly every frame dilutes "I can, though I'm small" (editor) | **Keep** | This is the parent's safety requirement and the editor's heart requirement pulling against each other. Safety wins in a book for 3–6s; Ana still makes every choice |

**Checkpoint 4 passed.** Strict lint, 19 pages, a reproducible bind, and
every panel point adopted or declined with a reason.

### Codex review of the finished book

*[Codex](reviews/04-book-codex.md), a different model family, run read-only.
It reviewed the first revised book.* It scored the book **6.5/10** and
independently found the p17 counting bug (fixed in round 2, #71). Its code
findings were all fixed, and both books still rebuild byte-identical:

| # | Finding | Fix |
|---|---|---|
| 77 | **High:** the site builder deleted its output directory without checking, so `build_site.py .` would destroy the repo | It refuses the repo, its ancestors and source directories, and deletes only a directory it built (one marked by `.nojekyll`) |
| 78 | Markdown could inject HTML attributes, and unsafe URL schemes passed through | Attribute values are escaped; only http, https and mailto pass |
| 79 | The generated review index linked to `reviews/reviews/…` | Links are relative to the index's own location |
| 80 | Links to unpublished files (e.g. `hero_sheet.ps`) were made local | Local links come from the same rule as the asset copier; anything else goes to GitHub |
| 81 | Nested-list continuation text moved into the parent item | A nested list keeps its own continuation lines |
| 82 | Helpers overwrote the caller's options (`cb-lit`, `cb-hullc`, `cb-face`) | They restore what they found |
| 83 | A failed bind could replace the committed PDF | It builds to `*.part.pdf` and moves into place only after the page check |
| 84 | Table cells split on `|` inside code spans | **Known, not fixed:** no document uses one |

## Checkpoint 5: Reflection

*Artifact: [05-reflection.md](05-reflection.md).*

- [x] Section 1 was written from the pages before re-reading the ideation.
- [x] Unintended readings are named and judged: the structural *rescue*
      reading (kept, explained), "Ten is fog" taken literally (kept), and
      gender roles (logged).
- [x] Every "what we'd change" item is either done or logged as a decision
      not to.

**Done.**
