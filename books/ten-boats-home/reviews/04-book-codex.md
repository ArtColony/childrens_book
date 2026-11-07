# Finished-book review: Codex

*OpenAI Codex (a different model family), run read-only through the Codex plugin on the first revised book: before round 2's fix to p17, which this review also caught. Kept verbatim.*

## A. Code review

Read-only review completed; no repository files changed. All 19 painted pages and 19 storyboard wrappers passed strict headless lint with the pinned pscat version. Running the painted pages sequentially inside `save`/`restore` also left an empty operand stack after every page. I found no operator-shadowing or wrong-operand-count failure on those tested paths.

Findings, ordered by severity:

1. **High — site output can delete source files.** [scripts/build_site.py:239](/Volumes/YOTUO/dev/childrens_book/scripts/build_site.py:239) recursively deletes any existing output directory. **Failure:** invoking the builder with `.` or a book directory destroys that directory before building. This is a latent defect established by inspection; I did not execute it. **Fix:** reject the repository root, its ancestors, and source directories; require an identifiable generated-output directory before deleting it.

2. **High — foreground figures defeat the final counting scenes.** [16_lifts.ps:11](/Volumes/YOTUO/dev/childrens_book/books/ten-boats-home/pages/16_lifts.ps:11) and [17_eleven.ps:12](/Volumes/YOTUO/dev/childrens_book/books/ten-boats-home/pages/17_eleven.ps:12) draw ten boats, then paint the adults over them. **Failure:** p-17 exposes only seven boat silhouettes; p-18 exposes nine, including a tiny yellow fragment. “Eleven” therefore lacks its promised visible set. **Fix:** reserve an unobstructed counting band and place all ten boats plus the lamp within it. Both rendering modes inherit this composition defect.

3. **Medium — Markdown can inject HTML attributes.** [scripts/build_site.py:51](/Volumes/YOTUO/dev/childrens_book/scripts/build_site.py:51) escapes text with `quote=False`, then inserts it into quoted attributes. **Failure:** an in-memory probe using `![a" onerror="alert(1)](missing.png)` produced an actual `onerror` attribute. Unsafe URL schemes also pass through. This is a latent content-handling vulnerability, not an allegation about current book content. **Fix:** parse first, escape attribute values with `quote=True`, and allowlist URL schemes.

4. **Medium — generated review-index links are broken.** [scripts/build_site.py:296](/Volumes/YOTUO/dev/childrens_book/scripts/build_site.py:296) writes `reviews/<file>` links but assigns the generated document a source location already inside `reviews/`. **Failure:** the mocked, entirely in-memory build generated `books/ten-boats-home/reviews/reviews/...` targets; its checkpoints link similarly points inside `reviews/`. **Fix:** use filenames relative to that synthetic source directory and `../checkpoints.md`, or assign the synthetic source a book-root location.

5. **Medium — existing book files are incorrectly assumed to be published assets.** [scripts/build_site.py:275](/Volumes/YOTUO/dev/childrens_book/scripts/build_site.py:275) gives every existing file under `books/` a local site URL, but the copier at [line 335](/Volumes/YOTUO/dev/childrens_book/scripts/build_site.py:335) copies only selected assets. **Failure:** the ideation page’s `01-hero/hero_sheet.ps` link becomes local although that file is never copied. **Fix:** derive local links from an explicit copied-asset manifest; send other source links to GitHub.

6. **Medium — nested-list continuation text changes ownership and reading order.** [scripts/build_site.py:173](/Volumes/YOTUO/dev/childrens_book/scripts/build_site.py:173) separates nested bullets from their continuation lines. **Failure:** rendering the actual ideation document moves “knows the sea and is coming home anyway…” into the parent paragraph, before the nested bullet ending in “Grandpa.” The manuscript suffers the same corruption. **Fix:** parse nested blocks recursively while retaining each continuation with its item.

7. **Medium — helpers overwrite caller options.** [lib/cb_ana.ps:294](/Volumes/YOTUO/dev/childrens_book/lib/cb_ana.ps:294), [line 298](/Volumes/YOTUO/dev/childrens_book/lib/cb_ana.ps:298), [lib/cb_harbour.ps:157](/Volumes/YOTUO/dev/childrens_book/lib/cb_harbour.ps:157), [line 197](/Volumes/YOTUO/dev/childrens_book/lib/cb_harbour.ps:197), and [line 223](/Volumes/YOTUO/dev/childrens_book/lib/cb_harbour.ps:223). **Failure:** probes confirmed that lamp helpers replace an incoming `cb-lit true` with `false`, `cb-gpboat` discards a custom hull colour, and even `[] cb-moored` changes `cb-face -1` to `1`. Later drawing on the same page can silently change. **Fix:** scope temporary options and scratch names in local dictionaries. `book.sh`’s page isolation prevents these becoming cross-page leaks.

8. **Medium — a failed book build can replace the good PDF.** [scripts/book.sh:45](/Volumes/YOTUO/dev/childrens_book/scripts/book.sh:45) writes directly to the destination before the page-count check at line 49. **Failure:** a successfully rendered but incorrectly paginated `--commit` build replaces the committed PDF, then reports failure. **Fix:** render and validate a temporary PDF, then atomically rename it into place.

9. **Low — table splitting ignores escaped pipes and code spans.** [scripts/build_site.py:121](/Volumes/YOTUO/dev/childrens_book/scripts/build_site.py:121). **Failure:** an in-memory two-column table containing `` `x|y` `` became three body cells with broken code markup; escaped pipes are also split. **Fix:** tokenize table cells while respecting escapes and code spans.

The version pin and explicit page seeds provide useful reproducibility controls. I did not rebuild or compare PDF bytes. Rough and paint paths both passed execution checks; their deliberately different glow treatments mean rough approval alone cannot establish final light quality.

## B. Book critique

Counts below come from inspecting every supplied page image. “Visible” includes identifiable partial boats, but excludes boats completely hidden behind figures.

| Image / story page | Number in text | Counted in picture |
|---|---|---|
| p-01 / cover | Ten, in title | **0 boats**; one handheld lamp |
| p-02 / 1 | Ten sailing out | **10 boats**, though several are very small |
| p-03 / 2 | No numeral; Grandpa’s boat | **1 boat**, inside the memory inset |
| p-04 / 3 | One | **1 boat** |
| p-05 / 4 | Two | **2 boats** |
| p-06 / 5 | Three, four, five | **5 boats** |
| p-07 / 6 | Six, seven, eight, nine | **9 boats**, clearly separated |
| p-08 / 7 | Waiting for ten | **9 boats**; the absence is correct |
| p-09 / 8 | “Ten is fog” | **9 boats**, with the rear-right one particularly faint |
| p-10 / 9 | No numeral | **5 faint boat silhouettes** |
| p-11 / 10 | No numeral | **0 boats** |
| p-12 / 11 | No numeral | **0 boats** |
| p-13 / 12 | No numeral | **0 boats** |
| p-14 / 13 | No numeral | **0 boats** |
| p-15 / 14 | A little boat | **1 boat** |
| p-16 / 15 | Ten | **10 boats**: nine small behind, Grandpa’s large foreground boat |
| p-17 / 16 | Ten boats and one little light | **7 visible boats**, including a partial red one; **2 lights** |
| p-18 / 17 | Eleven | **9 visible boats**—eight clear and one yellow fragment—plus **1 lamp** |
| p-19 / wordless ending | None | **10 boats** |

**Strengths.** The emotional structure is strong: familiar counting becomes anxious waiting, then Ana acts. “Not Grandpa’s” gives the read-aloud a dependable refrain, and “Little. Blue. Grandpa’s.” delivers a satisfying reversal. Mama’s visible presence supports Ana’s agency. The empty mooring, paired lamps, and return to the harbour make useful visual connections.

The clearest counting spread is story page 6: nine distinct boats in two rows. Story page 15 also supplies the full ten. The separate “Nothing” and “higher” pages give Ana’s persistence a meaningful page turn.

**Weaknesses.** The ending needs revision. “Eleven” can logically mean ten boats plus one lamp, but the second-to-last image does not display ten countable boats. The lamp has also moved onto a separate post, and Ana is standing apart from Grandpa. That weakens the intimate “Ana/light counts too” interpretation described in the manuscript. A child cannot reliably verify eleven from this picture.

The grouping of three–five and six–nine permits counting the final totals, but gives less support for matching each spoken number to a newly arriving boat. The opening ten are also small for the youngest readers. “Ten is fog” is memorable language, although a literal three-year-old may need an adult to explain that the tenth boat has not arrived.

The pictures communicate setting and action, but repeated poses and harbour compositions limit emotional range. Broad horizontal sky bands and conspicuous concentric glow rings look more schematic than the finish of strong published picture books. The text generally has clear contrast and generous space; the main layout problem is obstruction of counting objects.

The intended distinction between helping Grandpa and rescuing him remains uncertain: “Nothing,” then higher light, then his appearance naturally reads as rescue. His own lamp helps, but does not fully establish the intended distinction.

**Score against published picture books: 6.5/10.** A sound story with effective suspense and repetition; the final counting payoff and illustration finish keep it below publication quality.

