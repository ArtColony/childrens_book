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
- [ ] Second study pass: minhwa crags, sangseo-un, a flat moon, the figure
  redrawn.
- [ ] Hero sheet: the people, the pig, the boy at each age ("the same boy,
  getting older").
- [ ] Advisor gate on the interpretation and style.

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
