# Finished-book review: Codex

*OpenAI Codex (a different model family, for a read not anchored on ours), run read-only through the Codex plugin after the book was complete. It reviewed the code and the book: page images, story and the author's reflection.*

## A. Code review

All 15 page programs passed headless execution with strict lint on the pinned pscat; there were no current stack leaks, operand-count errors or overflowing text. The defects are latent:

1. **Medium: nested `cb-local` calls corrupt the CTM.** `lib/cb_kit.ps`. Every call saves into one shared `cb-lm`, so an inner call overwrites the outer's saved matrix. Verified: nesting translations of 10 and 20 leaves 10 after both return.
2. **Medium: filenames aren't escaped as PostScript strings.** `scripts/book.sh`, `scripts/render.sh`. `($p)` breaks on a `(` or `\` in a path.
3. **Medium: text can silently exceed its column or page.** `lib/cb_kit.ps`. A word wider than the column is accepted (a 322 pt word in a 30 pt column), and there's no bottom limit (a long paragraph ran to y ≈ −275).
4. **Medium: empty paragraphs advance twice.** `cb-lines` returns `[()]` for an empty paragraph, and a second decrement adds another line.
5. **Low: seed sweeps bypass strict lint.** `scripts/render.sh`.
6. **Low: local builds don't enforce the interpreter pin.** It only warns, so `book.sh --commit` could replace the PDF with output from another pscat.

## B. Book critique

**Story:** a coherent, comforting bedtime journey, best for ages 3–4. "Then I will go very far" is the strongest moment, but few events develop or change Moss.

**Language:** clear and economical. "Packed nothing at all" and "Slowly" work; it doesn't moralise; the opening is conventional.

**Pictures:** Moss is appealing and consistent; the meadow's scale and the tiny snail before the sea work. But the images read as flat vector illustration: horizontal sky bands, repeated grass marks, similar compositions, and sparse expressions and incidental storytelling.

**Text and picture:** strong on literal action, but the pictures mostly illustrate what the words already say. The last pages suggest sound around the shell without showing a remembered experience.

**Layout:** readable, with generous margins, but centred text over a low illustration on page after page is monotonous. The sun crowds the text on the gull page.

**Versus the reflection:** agrees that slowness is positive and persistence weakly tested. **Disagrees** that a hardship is needed (sensory discovery could deepen it instead), that the adult reading holds (the snail is still *at* the sea, so hearing it in her shell is literal, and "now" wouldn't establish memory), and that the gull must return.

**Score: 6/10** against published picture books.
