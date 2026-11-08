# The Ugly Duckling: checkpoint log

## Checkpoint 1: interpretation, style and hero sheet

- [x] **Source:** a public-domain edition was identified (Stickney, Ginn
  1886/1914; Gutenberg #32571). Its translator is unnamed, and that is
  stated.
- [x] **Tale chosen by what the medium paints well:** birds, water, reeds,
  four seasons, and almost no people.
- [x] **Interpretation:** Andersen's "born of a swan's egg" line is
  dropped, because it says worth comes from birth. The message is
  explicit: *you are not wrong for being different; you are still
  growing.*
- [x] **Style studies:** three looks of one scene. **B, painted**, was
  picked by the art director and agreed by the advisor. The studies were
  sent to the reader.
- [x] **Hero sheet, advisor test 1:** the growth row reads as one bird
  (fresh child agent: "the same bird, getting bigger"). This needed a
  second pass. The first sheet swapped a grey chick for a white chick that
  never appears in the story. The advisor caught it, and `cb-dkgrow` fixed
  it.
- [x] **Hero sheet, advisor test 2:** the hen and the cat hold up as flat
  lit shapes, so the cottage stays.
- [x] **Seasons** are one table (`cb-season`) and read as palette swaps.
- Duckling fixes from the first sheet:
  - The neck was too long and he read as a goose: now a chick, with a big
    head, a short thick neck and a tuft.
  - A gap at the neck joint showed the background: the neck is now a
    stroke in the body colour.
  - The rim light on the fluff read as orange spots: it is now half-mixed
    with the lit colour.
  - The swan's black beak knob was too big.
- **Advisor gates:** called at the opening plan, at the style pick and hero
  sheet (above), and next at the retelling and the finished book.

## Checkpoint 2: the retelling

Panel on draft 1 (465 words): child, parent, and editor (6/10).
**Lesson gate on draft 1:**

- **Child:** "…keep going until you find friends who think you're
  wonderful, and then you turn out to be a swan!"
- **Parent:** "…you were never ugly, only different and still growing."

The child's last clause is the trap the parent named: the transformation
reads as the reward.

| # | Point | Decision |
|---|---|---|
| 1 | Parent: "still growing" is the "you'll be beautiful later" trap; use "a swan all along". Editor: "still growing" is the real lesson; "a swan all along" leans back toward Andersen's birth line | **The editor's line, the parent's ending.** "You were different. And you were still growing." keeps growth, not birth. The last words became an invitation, "Come, swim with us", so the reward is belonging, not beauty (the parent's point) |
| 2 | Editor: the swans speak unprompted; let him speak first, and don't end on "the ugly duckling" | **Accepted.** His whisper (adapted from Andersen's last line) comes first, and theirs is the answer |
| 3 | Editor: drop "only" | **Accepted** |
| 4 | Editor: cut the old woman (a person), make p7 wordless, fold the setting into p8 | **Accepted.** Three wordless pages now (7, 13, 18) |
| 5 | Editor: cut what the art shows (p1 list, p10 leaves, p14's five beats, p16's caption) | **Accepted.** p16 is now "And there in the water was a swan." |
| 6 | Editor: p14 gives the reveal away ("strong" wings, a white bird flying) | **Accepted,** in text and art: he stays a grey shape in flight against the light |
| 7 | Parent: "not a clumsy grey bird any more" agrees with the bullies | **Cut** (also by the editor) |
| 8 | Parent: no adult fixes the bullying; let the mother's "look how well he swims" come back | **Accepted:** p12 ends "His mother had always said he swam well." He saves himself with the gift she named |
| 9 | Parent: use "ugly" only in the bullies' mouths | **Mostly.** It appears on pp. 4 and 6 (the bullies), and in p17 his own whisper, which the swans answer at once |
| 10 | Child: burdock, marsh, nonsense | "Burdock" is cut. "Marsh" is shown on p5. "Nonsense" is kept: the hen's voice carries it |
| 11 | Editor: aim for 280–320 words | **Partly: 376.** The cottage comedy and the winter line about his mother were kept on purpose |

**Lesson gate on draft 2 (fresh readers, text only): passed.**

- **Child:** "Even when you look different, you can still be lovely, and you
  might be growing into something really wonderful."
- **Adult:** "Being different isn't being worthless; what looks ugly may
  simply be unfinished, and you grow into who you truly are." Asked what
  the reward is: "belonging plus self-recognition and growth, more than
  beauty alone."

The draft 1 trap ("and then you turn out to be a swan!") is gone. The
adult's remaining hesitations (the pecking, the all-night swim, the cold
wild ducks) are the tale's own stakes, and they are kept, each to one line.

## Checkpoint 4: the finished book

Panel on the 19 painted pages: artist (Sonnet), a cold child (Haiku) and a
cold adult (Sonnet), page images only. **Codex was unavailable**, so its
review of the code was done by a Claude code reviewer (Opus), given the
code and CLAUDE.md but none of our notes ([process](../../docs/process.md)).
A Codex pass can still be run later.

**Lesson gate on the finished book (images only): passed.**

- **Child:** "Even when you are different and other people are mean, you
  can keep going and grow up to be wonderful."
- **Adult:** "Being different isn't the same as being bad, and you'll find
  where you belong while you're still growing."

Artist score: **7/10.** The strongest pages are p13, p14 and p7, all of
them nearly wordless.

| # | Point | Decision |
|---|---|---|
| 1 | All three: text collides with art on p8 (the cat's ear), p15 (a tree trunk), p16 (the mirrored line through the swan), p18 (the credits on the reeds) | **Fixed.** p16's mirrored line is cut: it was the page's one type move, and it fought the reflection, which is the point of the page |
| 2 | Artist and adult: "all alone." on p6 is tiny and lost in the reeds; the grey "No." lines on p8 are faint | **Fixed:** larger, darker, set in open water |
| 3 | Artist: on p11 the duckling is bigger than on p12 (growth reads backwards), the line touches his head, and the swans are specks | **Fixed:** duckling 280 → 210, swans about twice the size, the line lifted |
| 4 | Artist: "Crack!" is dark on dark leaves; the cover title is at the trim | **Fixed:** cream, set by the nest; the title is lowered |
| 5 | Code review: ice cracks (p12) and snow fall into the text | **Fixed:** `cb-icelo` keeps the cracks low; the snow stops at y 500 |
| 6 | Code review: **the 21 MB PDF is `cb-pmist`**, about 1 MB of vector spray per call, from `pkwet` | **Fixed:** a soft wash band under a plain spray. **13 MB** now; the horizon looks the same |
| 7 | Code review: the reed path went base → tip → middle, so every reed was a hooked double stroke | **Fixed** (point order). The reeds now taper to the tip |
| 8 | Code review: `cb-swan-wingshape` wrote into the current dict; dead code in `cb-ptree` | **Fixed** |
| 9 | Code review: Palatino on every page, not the house NewCenturySchlbk | **Kept**: the painted style is a different book voice (see the [style note](01-style.md)). Recorded here as a per-book choice |
| 10 | Artist: p16 should show the *grey* duckling bowing above and the swan only in the water | **Declined.** The retelling's order is welcome first (p15, still grey), then recognition (p16). The white bird above and below is the reveal |
| 11 | Artist: p5 bird too small, p9 doorway reads as a wall, p17 swans cropped, the sparkly horizon repeats, ear tufts read as cat ears | **Deferred** to a second painting pass (listed in the reflection) |
| 12 | Adult: wordless p7 and p13 leave the parent to narrate; the cruelty ("ugly", "no use at all") | **Kept.** The wordless pages were the artist's strongest. The cruelty is the tale's stakes, each one line, and the swans answer it |
| 13 | Child: p13 unclear ("night or snow?") | **Kept** for now: p12 sets it up on the facing page. Noted for the second pass |

## Checkpoint 5: the second painting pass

The art items deferred at checkpoint 4, painted:

| Page | Was | Now |
|---|---|---|
| all | two-pointed head tufts read as a cat's ears | one soft wisp of down, which fades as he grows |
| 5 | a small dot standing mid-lawn | a bigger bird running out from under the hedge, toward the water; the words lifted clear of the hedge |
| 6 | the same mid-page horizon as five other pages | a high horizon: a wide marsh, and a small bird in it |
| 9 | a brown slab that read as a wall | the lamp-lit wall, the door frame, the open door with its latch, and a doorstep in the spilled light |
| 17 | four equal swans, two cropped | the young swan in front and largest; nobody cropped; the trees clear of the text |

Kept: p13 (the child's "night or snow?"). p12 sets it up on the page before.
Moss, Ten Boats Home and Puff still rebind byte-identical.

## Checkpoint 6: review round 2

The review loop ([process](../../docs/process.md)) replaces the Codex pass.
Fresh agents saw only the page images (and, for the artist, the page plan),
with no earlier notes. **Lesson gate: passed again.**

- **Child:** "Being different from others does not make you bad or ugly, and if you keep going and stay kind to yourself, you may grow into something beautiful."
- **Adult (7.5/10):** "Being different isn't being bad; you can be unloved where you are and still be growing into something beautiful, and you belong with those who welcome you."

**Artist: 6.5/10** (a fresh reviewer; round 1 gave 7). The biggest lift it named: the duckling has one neutral face, and the emotional pages are too small or pale.

| # | Point | Decision |
|---|---|---|
| 1 | Artist: he is an expressionless lump | **New `cb-dkmood /sad`**: a worried brow rising toward the beak, on pp 4 (with his head down), 6, 7, 8 and 15 |
| 2 | Artist, adult: p7 duckling invisible, window speckle "looks like a glitch" | **Fixed:** he is at the door at 1.7x, in a pool of window light. The speckle (a spray) is replaced by a new `cb-glow` (soft rings), also on p8 (the cat's "smudges") |
| 3 | Both children (rounds 1 and 2): p13 "night, or space?" | **Fixed:** a moonlit ice tint instead of the navy wash, frozen reeds at the edges, and ripples round the open water. It stays wordless |
| 4 | Artist: p16 swan lost on the pale band | **Fixed:** a green treeline behind, a larger swan, a deeper reflection |
| 5 | Artist: p5 he doesn't run; p9 the step and the floating bird; p14 the bird over the sun; p18 the card | **Fixed:** p5 larger, clear of the hedge; p9 a solid step and a shadow; p14 the sun moved and the bird larger; p18 a soft wash, not a card |
| 6 | Code: the tuft punched a hole in his head on every page | **Fixed** |
| 7 | Code: PDF 13.5 MB (sky strokes, paper grain, mist) | **Fixed: 6.5 MB**, with no visible change |
| 8 | Code: p2 Crack!, p9 folio, p17 overlap | **Fixed** |
| 9 | Artist: p4 hen tilt and pecking ducks; p1 bigger nest and farm details; p17 text weight; sky bands | **Deferred** to round 3, to see if a fresh artist names them again |
| 10 | Adult: split sentences on pp 5, 6, 11, 12 | **Kept:** the one type move per page is the house rule. Only p6 was hard to see, and that was fixed in round 1 |
| 11 | Adult: wordless p7 and p13 | **Kept**, now drawn to read without words (pp 7 and 13 above) |
