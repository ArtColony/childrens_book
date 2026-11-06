# Making a picture book: the stages and their checkpoints

This repo is an experiment in making a long creative artifact, a 32-page-style
picture book, out of many small programs. A long artifact fails differently
from a short one. Each page can be fine on its own while the whole is wrong:
the words on page 12 describe a picture that is on page 13, a refrain drifts,
the hero faces the wrong way halfway through. The fix is the one long-form
makers have always used: work in stages, from cheap to expensive, and don't
pay for the expensive stage until the cheap one has passed a checkpoint.

```
 1 Ideation ──▶ 2 Manuscript ──▶ 3 Storyboard ──▶ 4 Book ──▶ 5 Reflection
 concepts,      words, page      grey thumbnails    painted     what the book
 the heart,     plan             with real type     pages,      actually says,
 hero sheet                                         bound PDF   read cold
 (minutes)      (an hour)        (an hour)          (hours)     (an hour)
```

### The heart: a thread through every stage

A picture book is read aloud by an adult to a child, many times. It works on
two levels at once. The child takes away a **feeling** (it's safe to be
small, the dark has friends in it). The adult takes away an **idea**, usually
unstated, that makes the hundredth reading bearable. The process names this
*heart* at the start and checks it at every stage:

| Stage | What happens to the heart |
|---|---|
| 1 Ideation | Write it down: one sentence for the adult, one feeling for the child, and the **question** the story asks (not the answer). |
| 2 Manuscript | The hero **acts** it: the heart is shown through a choice the hero makes under pressure. At most one character may say it, in their own words. The narrator never states a moral. |
| 3 Storyboard | The moment of choice gets the book's strongest page: the widest shot, or the page-turn reveal. |
| 4 Book | The painting serves it: palette, light and scale move with the arc. |
| 5 Reflection | Read the finished book cold. What does it *actually* say, including what we didn't intend? Compare that with stage 1. |

A story built *from* a lesson tends to preach; a story whose heart was never
named tends to say something by accident. Naming the heart early and then
hiding it in action avoids both.

Every stage leaves a file in `books/<slug>/`, and every checkpoint is logged
in `books/<slug>/checkpoints.md`. The log records pass or fail, what failed
and what changed, so the history of the book can be audited. A checkpoint is
a list of questions with yes/no answers. "Reads well" is not a checkpoint;
"every page's text names only things visible in its picture" is.

A stage can send work back. A storyboard that shows a page with nothing to
draw sends that line back to the manuscript. That is cheap at stage 3 and
expensive at stage 4.

---

## 1. Ideation: `01-ideation.md` and `01-hero/hero_sheet.ps`

**Input.** The brief: audience, trim size, rough length, medium, and
anything to avoid (here: repeating an earlier book's shape).

**Work.**
1. Write at least **three concepts**. Each gets a one-sentence logline, the
   hero, the emotional arc (want → obstacle → change), the **structural shape**
   (journey, cumulative, problem–solution, counting, there-and-back, call
   and response), the refrain if any, and what makes it **drawable in this
   medium** (here: PostScript washes and ink, which are good at light, pattern
   and repetition and weak at crowds and complex anatomy).
2. **Score** them against criteria stated *before* scoring: emotional payoff,
   page-turn potential, visual variety across pages, feasibility in the
   medium, distinctness from earlier books. Pick one and record why it won.
3. For the chosen concept, write **the heart**:
   - *For the adult:* the idea, in one sentence.
   - *For the child:* the feeling they should leave with.
   - *The question* the story asks, which the hero's choice answers.
   - *What it is not:* the nearby message we must not slide into. For
     example, "be brave" is not "fear is silly".
4. Write a **world note**: setting, palette (one accent colour), time of day
   across the book, and a short cast list.
5. Draw the **hero sheet**: the hero as a library procedure (`lib/cb_<hero>.ps`)
   in every pose and scale the story will need, rendered on one page.

**Checkpoint 1.**
- [ ] Three or more concepts, each with logline, arc, shape and feasibility.
- [ ] Scoring criteria written down before the scores.
- [ ] The chosen concept's ending answers its opening want.
- [ ] The heart is written down: adult idea, child feeling, question, and
      what it is not.
- [ ] The heart comes out of the hero's want and choice, not out of a
      narrator; it could be guessed from the logline.
- [ ] Its shape differs from the earlier books' shapes.
- [ ] The hero sheet renders cleanly (strict lint), and the hero reads at
      the smallest scale the story needs (look at it at that size).
- [ ] The palette is named, with one accent colour.

**Unlocks:** writing.

## 2. Manuscript: `02-manuscript.md`

**Input.** The chosen concept and world note.

**Work.**
1. Write the text straight through, read-aloud first: rhythm, a refrain
   if the shape wants one, words a 4-year-old knows or can enjoy guessing.
2. Break it into pages in a **page plan table**: page number, the exact text,
   and **the one drawable moment** that page shows. A line that can't name
   its picture is either cut or merged.
3. Mark the **page turns**: what a reader is waiting to see when they turn,
   and where a turn reveals it.

**Checkpoint 2.**
- [ ] Word count in range (ages 3–6: about 300–600; record it).
- [ ] Every page has exactly one drawable moment, and the text names nothing
      the picture can't show (the "what does this page *show*?" test).
- [ ] No page holds more than about 45 words (it must fit the text band).
- [ ] The refrain, if any, appears at least three times and changes at
      the end.
- [ ] The last page pays off the first: name the setup and the payoff.
- [ ] **The heart is acted, not told.** Name the page where the hero makes
      the choice that carries it. No narrator line states a moral, and at
      most one character line says the idea aloud.
- [ ] **The obstacle really tests the heart.** If the hero could succeed
      without the quality the story is about, the story doesn't prove it.
- [ ] Read aloud end to end once. Note any line that trips.

**Unlocks:** storyboard.

## 3. Storyboard: `03-storyboard/NN_*.ps` and a contact sheet

**Input.** The page plan.

**Work.** For every page, a **thumbnail at full trim size**: flat grey
masses for ground, sky and big shapes, the hero (the real procedure) at the
right size, pose and facing, and the **real manuscript text set with
`cb-text`**. Text fit, line breaks and widows are then real now, not
guesses. Render the whole board onto one contact sheet and look at the book
as a sequence:

```sh
scripts/render.sh books/<slug>/03-storyboard
scripts/sheet.py renders/<slug>/03-storyboard renders/<slug>-storyboard.png
```

**Checkpoint 3.**
- [ ] **Text and picture agree** on every page (re-run the manuscript test
      against the drawing, not the plan).
- [ ] **The text band is clear**: no mark crosses it on any page, and no
      line ends on a single short word (a widow).
- [ ] **Shot distance varies**: label each page close / mid / wide; there are
      no more than three of the same in a row.
- [ ] **Continuity**: direction of travel is consistent (left-to-right
      reads as "onward"), the time of day only moves forward, and props
      persist (anything carried stays carried).
- [ ] **Page turns land**: the reveal is on the right-hand turn, not
      spoiled by the page before.
- [ ] The hero is recognisable on every thumbnail at contact-sheet size.
- [ ] The page carrying the heart's choice has the book's strongest visual
      beat (widest shot, biggest turn, or the change in light).

**Unlocks:** painting. The painted page is the storyboard page with the
grey masses replaced by paint. Keep the composition.

## 4. Book: `pages/NN_*.ps` and `<slug>.pdf`

**Input.** The approved storyboard.

**Work.** Paint each page from its thumbnail: same composition, same text
position, house style (`cb-wash`, `cb-bigwash`, `cb-line`, `cb-text`). Then
bind with `scripts/book.sh books/<slug> --commit`.

**Checkpoint 4.**
- [ ] Every page renders under strict lint (no error, no stack or gsave leak).
- [ ] The PDF has one page per page file (`book.sh` checks).
- [ ] **Look at the rasterized PDF itself**, not just the PNGs: a full grid
      plus 300 dpi crops of a face, a text block and a busy texture.
- [ ] Each painted page matches its thumbnail; any drift is deliberate and
      logged.
- [ ] Checkpoint 3's text-band and continuity checks still hold after
      painting (paint spreads; grass grows).
- [ ] Size budget: under 1 MB a page.
- [ ] Builds are reproducible: binding twice gives the same bytes.

**Unlocks:** reflection.

## 5. Reflection: `05-reflection.md`

**Input.** The finished PDF, read cold, start to finish, as a parent would
read it aloud, ideally a day later or by a reader who hasn't seen stages 1–3.

**Work.** A short meta-analysis:
1. **What the book says**, to the child and to the adult, written from the
   pages alone, before re-reading `01-ideation.md`.
2. **Intent versus result.** Compare it with the stage 1 heart. Where do they
   match, where did the story drift, and was the drift an improvement?
3. **Other readings.** What a child, a worried parent or a critic might take
   from it that we didn't mean, including any we'd want to prevent.
4. **The lessons**, stated plainly here so they never need stating in the
   book.
5. **What we'd change**, and whether it is worth a revision.

**Checkpoint 5.**
- [ ] Section 1 was written before re-reading the ideation notes.
- [ ] At least one unintended reading is named and judged (keep, or fix).
- [ ] Every "what we'd change" item is either done or logged as a decision
      not to.

**Done:** commit the PDF, previews and reflection, and update the README.

---

## Retrospective: what *Moss Goes to the Sea* skipped

Moss was made before this process existed. Its ideation was a single
concept, never weighed against others, and it had **no storyboard**: the
pages were painted straight from the text. It worked, but every defect was
found at stage 4, the most expensive place to find it:

| Defect, found in the final PDF | The checkpoint that would have caught it |
|---|---|
| Page 12's text said Moss curled into her shell; the picture showed her outside it. The tucked shell was on page 13. | 2 / 3: text and picture agree |
| The meadow grass on page 6 grew through *Slowly, slowly.* | 3: text band is clear |
| Page 12's sentence left *heavy.* alone on the last line. | 3: no widows (real type in thumbnails) |
| Stars sat on top of words on the night pages. | 3: text band is clear |
| The folio on page 9 was invisible on the dark hill. | 3: text band (and the folio) is legible |
| Grass showed through Moss's translucent shell. | 1: the hero sheet, if drawn over a busy ground |

Each fix meant repainting and re-binding. Moss also never had a named
heart. Its message emerged during writing, and its strengths and weaknesses
show it. See [its reflection](../books/moss-goes-to-the-sea/05-reflection.md).

The second book, [*Ten Boats Home*](../books/ten-boats-home/), runs every
stage in order, and its `checkpoints.md` records what each checkpoint caught.

## Applying this to other long artifacts

The pattern does not depend on picture books:

0. **Name the heart before the form**: what the work should leave its
   audience with, and the question it asks. Then make every stage carry it
   and a final reading check it.
1. **Diverge before converging.** Write several concepts, with the criteria
   fixed before the scoring.
2. **Prove the hardest element first.** The hero sheet stands in for any
   component that, if it fails, sinks the whole: a voice, a core mechanic, a
   recurring diagram style.
3. **Plan in units that each name their deliverable** (page → drawable
   moment; chapter → scene goal; slide → single claim).
4. **Rough the whole sequence at full size with real content** before
   finishing any unit, then judge it *as a sequence*: pacing, variety,
   continuity.
5. **Finish from the rough**, check the finished whole the way a reader
   will meet it, and log any drift.
6. **Keep the checkpoint log**. It is the cheapest record of why the
   artifact looks the way it does.
