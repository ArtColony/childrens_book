# The Golden Pig: checkpoint log

Issue: [#7](https://github.com/ArtColony/childrens_book/issues/7). Branch:
`book/golden-pig`.

## Setup: Korean type

- [x] pscat's `cjk-thai` pack is installed (23 MB, on external storage,
  symlinked into pscat's font folder). Faces: `NotoSansKR-Regular` and
  `NanumBrushScript-Regular`. There is no Korean serif.
- [x] `lib/cb_ko.ps`: `cb-textko` and `cb-brushko`. Each checks its face on
  use and stops rather than set Hangul in Helvetica.
- [x] `render.sh` and `book.sh` fail on pscat's font-fallback warning. CI
  installs the pack, and `CLAUDE.md` allows it.
- [x] A bilingual test page renders. Korean wraps at its word spaces, and
  Hangul comes out as outlines in the PDF, like the Latin text.
- [x] The other four books bind byte-identical to their committed PDFs.
- pscat bug found: `resourcestatus` reports no Font, even for installed
  faces ([PSCatLabs/pscat#1214](https://github.com/PSCatLabs/pscat/issues/1214)).

## Checkpoint 1: interpretation, style and hero sheet

- [x] **Source** identified: *Choe Goun jeon* (최고운전). Research is in
  [research.md](research.md): the beats, the variants, the earliest records,
  and content notes for 6–9. No English translation exists, and the
  retelling is our own wording.
- [x] **The reader's choices** are recorded: the whole novel condensed, the
  father left a mystery, the wife kills the pig, sunflowers as hope.
- [x] **Interpretation** written. The editor
  ([review](reviews/01-interpretation-writer.md)) scored the first draft
  5/10: "the heart is laid on top", with no choice by the boy.
- [x] **Style studies:** three figure treatments of one scene. The art
  director picked a hybrid built on C, flat minhwa figures
  ([review](reviews/01-style-artist.md)).
- [x] Second study pass: minhwa crags, sangseo-un, a flat moon, a lighter
  indigo, a hillside, and the figure redrawn (two-wing putou, gaze, lean,
  the thread at his hand).
- [x] **Text budget measured** (an advisor point): 3 Korean lines at 20 pt and
  4 English lines at 19 pt. About 30 English words a page, 38 at most,
  about 850 in all. The first plan's 50 a page didn't fit.
- [x] CI installs the `cjk-thai` pack on Linux (draft PR #8, green).
- [x] **The reader signed off** (2026-11-14), after seeing the before and
  after sheet:
  - **Sunflowers** are on every page, closed or bowed until kindness opens
    them and turns them toward him.
  - **The father's line** at the end is kept, as our stated addition.
  - **The cuts** are approved, except that the river woman's **talismans and
    the poisoned meal are restored** (one more page, 29 story pages).
- [ ] Hero sheet: the people, the pig, the boy at each age ("the same boy,
  getting older").
- [x] Advisor gate on the interpretation and style. Its points: measure the
  text budget, rebuild the mountains rather than reshape them, draw the pig
  first, ask the reader about the changes to their choices, and open a
  draft PR early for CI.

### The editor's review: what changed

| # | Point | Decision |
|---|---|---|
| 1 | The boy makes no choice; the box riddle should be the climax, not a detour | **Done.** The box is page 20, the widest spread. The boy's four acts from the source carry the heart: he refuses to come home, names the pavilion, names himself, and answers the box. |
| 2 | Sunflowers that follow him mark him as special from birth | **Partly.** The reader chose "bloom where he is protected or loved, turn to follow him". They now answer *kindness to him* (the maidens, his mother, Unyeong, the old woman), not his presence. That stays inside the reader's choice. |
| 3 | Heavenly teachers swap pig-birth for heaven-birth | **Done.** He teaches himself letters from birds' tracks (English Wikipedia: self-taught). The maidens only nurse him. |
| 4 | The pig takes 8 of 28 pages; China becomes a list | **Done.** The pig takes 6 pages. Cut: the Tang scholars, the exam, the talismans and the poisoned meal. Exile is kept, because slander is the whisper again. |
| 5 | The refrain drops 이래's hearsay | **Done.** "The golden pig's child, they say." The Tang court hears it because the scholars carried it home. |
| 6 | The boy's answer to the whisper is blank | **Done.** "My name is Chiwon." |
| 7 | The father's lesson comes too early, and it says "are", not "become" | **Done.** He only apologises at the pavilion ("I was afraid of a story. Come home."). The lesson is on the next-to-last page: "I should have watched what you did." Our addition: the father lives to the end. |
| 8 | The last line should turn the refrain | **Done.** "Once they said: the golden pig's child. Now they say: he became an immortal." |
| 9 | Shoes by a stream read as drowning | **Done.** Now a hat on a pine and a path into cloud. |
| 10 | "Marry the minister's daughter" as a reward, in a book of stolen wives | **Done.** Unyeong chooses him, judging him by his work in the garden. |
| 11 | Cut the blue lion | **Declined.** It is one page of wonder, very minhwa, and a source beat the reader asked us to follow. |

### The art director's review: what changed

| # | Point | Decision |
|---|---|---|
| 1 | The landscape is generic, not minhwa: gumdrop peaks, puff clouds, a glowing moon, a navy field | **Accepted** as the style rules in [01-style.md](01-style.md), and the first job of the second pass |
| 2 | The figure: the putou hat is wrong, the face small and blank, the pose a signpost, the thread passes through him, his value merges with the hills | **Accepted**, for the second pass |
| 3 | The flat dark slab under him reads as a stage | **Accepted**: a hillside path |
| 4 | Frame: a paper mat with a double rule; controlled breaks; panel height varies | **Accepted** |
| 5 | Korean type looks lighter than the English; use a serif Korean face | **Partly.** No serif in the font pack. Korean sets larger to match the English's weight. |

### The hero sheet's reviews: what changed

The child test passed: *"They're the same boy, just at different ages."* The
art director scored the figures 5/10 and the pig 5.5/10
([review](reviews/01-hero-artist.md)).

| # | Point | Decision |
|---|---|---|
| 1 | Stiff poses, lollipop hands; the baby floats | **Done:** mitten hands with a thumb, and a holding arm that cradles the baby (`cb-ch-held`) |
| 2 | Women's hanbok: the jeogori and chima join is missing | **Done:** a short jeogori over a chima tied high, a white collar (동정), long ribbons (고름), pleats |
| 3 | The pig isn't menacing: mustard, cartoon | **Done:** gold-leaf sheen and speckle, a minhwa tiger's eye, a brow, teeth, two tusks, a humped shoulder |
| 4 | The boy's yellow is too close to the pig's gold | **Done:** green, with 색동 rainbow sleeves |
| 5 | Identical faces; no toddler proportions | **Done:** long eyes for adults, round eyes for children; `cb-ch-age /tot` |
| 6 | The dead pig on its back reads as a comic bug | **Done:** sprawled, eye shut, the spotted deerskin on the back of its head |
| 7 | The putou isn't Silla | **Declined:** Silla adopted Tang court dress, putou included, in 649 under Kim Chunchu. The wings are shorter, and grown Chiwon wears a gat at the end (p. 29) |

## Checkpoint 2: the retelling

Draft 1 had 919 words. The panel was a child (7), a parent, an educator, the
editor (6.5/10) and the Korean reader.

**Lesson gate on draft 1: passed.** The intended lesson is *what people
whisper about you does not decide who you become; what you do does*.

- **Child:** "Don't just believe what people whisper about someone. Watch what they do."
- **Parent:** "…what you do matters more than what they say, and the grown-ups who believed the whispers should say sorry."
- **Korean reader, from the Korean alone:** "사람들이 수군거리는 말만 듣지 말고, 그 사람이 하는 일을 보고 알아봐야 해."

| # | Point (who) | Decision |
|---|---|---|
| 1 | p. 19 "things change in the dark" tells the idea one page early (editor); it is confusing (child) | **Done:** "He held the stone box to his ear and listened for a long time." The boy listens to the thing itself. |
| 2 | The father's line is a logic slip: a newborn has done nothing (editor) | **Done:** "I listened to what people said about you. I should have watched what you did." It is seeded on p. 17: Unyeong "watched what he did, not what they said". |
| 3 | The boy goes passive after the box (editor) | **Done:** p. 23 he leaps back, turns aside and pushes the bowl away. p. 26 he refuses the Emperor: "I have a promise to keep." |
| 4 | p. 29's "immortal" follows his vanishing, not his deeds (editor, parent) | **Done:** "Now they read his poems and say: he lives forever." / "그의 시를 읽으며 '신선이 되었대'." |
| 5 | The deerskin is never planted (parent, educator) | **Done:** the pouch on its cord is shown on p. 2 and named on p. 5, so the cord is a page-turn. |
| 6 | The strange fingernails are never paid off (parent) | **Done:** p. 28 "strange fingernails and all". |
| 7 | The mother vanishes after p. 11 (editor, parent) | **Done:** p. 12 the boy looks at his father a long time, then runs to his mother. The pavilion's naming moves to p. 13. |
| 8 | p. 9 "animals kept away" reads as shunning (all) | **Done:** "no wild beast came near to harm him", and white cranes. |
| 9 | p. 16: why the capital, how old, and the whisper there has no consequence | **Done:** "At ten… to study… chose to work off the debt… and gave him the worst jobs." |
| 10 | p. 24's exile needs a cause and a sensible register | **Done:** "…whispered the old story… And the Emperor listened." / "그 말은 황제의 귀에도 들어갔어요." |
| 11 | p. 25: the boy's feelings are never named (educator) | **Done:** "He was hungry and alone." |
| 12 | p. 26's reversal has no cause (parent) | **Done:** the Emperor reads his poems from the island. |
| 13 | Unyeong has no act of her own (parent) | **Done:** she keeps the peony garden while she waits (p. 27). |
| 14 | 헛소문 settles the mystery (educator) | **Done:** 소문. |
| 15 | Refrain: drop the 의 (Korean) | **Done:** "금돼지 자식이래." |
| 16 | Korean line edits: 번역투, mimetic words, speaker tags, 삐악삐악, 종종걸음, 갓 for the hat (Korean) | **Done**, nearly all. 갓 means grown Chiwon wears a gat on p. 29. |
| 17 | Was he the pig's child? The book dodges it (parent) | **Back matter (p. 30):** "The old tellings disagree, and this book doesn't say: what we know is what he did." |
| 18 | Pronunciation key; Silla, Tang; 고운 (孤雲), 문창후, 파경노 (educator, Korean) | **Back matter (p. 30)** |
| 19 | Draw hanja, not hangul, in the sand (educator) | **Storyboard note** on p. 10 |
| 20 | "Unyeong" will remind Korean adults of *운영전* (educator, Korean) | **Kept:** the source names Minister Na's daughter 운영 (English Wikipedia, EncyKorea, Digital Gunsan; research.md beat 19). The back matter says so. |
| 21 | Page "23b" (child) | **Done:** renumbered 1–29, plus the back matter as p. 30. |
| 22 | The China stretch tests his charms, not him (editor) | **Partly:** he now acts in each trap. The reader chose to keep the charms. |
| 23 | The p. 27 wedding page can't show "the court would not have him" (educator) | **Accepted risk:** the storyboard decides; the mountains stand beyond the wedding. |

**Fit, measured on every page** (draft 2): every page fits in up to 4 Korean
lines (20 pt, leading 1.42) and 4 English lines (19 pt). Five pages needed a
fourth Korean line, so the panel's top moves from 476 to 462. Draft 2 has
920 English words.

- [x] Every page has one drawable moment, and the text names only what it shows (fixes 5, 8, 19 and 23).
- [x] Every page is within the budget (measured, not guessed).
- [x] The refrain appears four times before the turn, and the turn comes on the last page.
- [x] The last page pays off the first: wives dragged into a mountain at night, against two people walking into one freely at golden evening.
- [x] The heart is acted: the boy refuses (p. 11), names himself (p. 18), listens and answers (pp. 19–20), refuses the Emperor (p. 26). One character says it (p. 28).
- [x] The obstacle tests the heart: the whisper costs him his home, his work and his place at court.
