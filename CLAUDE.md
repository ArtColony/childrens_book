# childrens_book

*Moss Goes to the Sea*, a picture book written, painted and typeset in PostScript and rendered with pscat into a print PDF. See `README.md` for setup and layout.

- Use the released pscat at the version in `.pscat-version`, never a source checkout. The `pscat`, `psart` and `psviz` skills in `.claude/skills/` come from that same release tag. Refresh them when the pin moves.
- Render pages with `scripts/render.sh` and bind the book with `scripts/book.sh`, not bare `pscat`, so every run is strictly linted. Look at the PNG after every render. Before calling the book done, also rasterize the PDF itself (`pdftoppm`), including a zoomed crop at 300 dpi.
- Never run `pscat file.ps` without `--png`, `--pdf`, `--headless` or `-e`: it opens a window and blocks.
- Disk space on the dev machine is tight. Put renders and temp files on external storage: `CB_RENDERS=/Volumes/YOTUO/dev-cache/childrens_book/renders`, plus `TMPDIR`.
- Each page is one file, `book/NN_name.ps`, with `%%BoundingBox: 0 0 612 612`. It starts with `/Seed where { pop } { /Seed N def } ifelse  Seed srand` and `(lib/cb_book.ps) run`, then `cb-ground`, and ends with `showpage`. File-name order is page order.
- Every repo library and every name it defines uses the `cb` prefix (`lib/cb_*.ps`, `cb-*`), so nothing shadows pscat's built-in `lib/`. `render.sh` refuses other library names.
- Colours and procedures share one namespace. Colours that collide with a procedure take a `c` suffix (`cb-grassc` colour, `cb-grass` procedure). Never name a variable after an operator: `bind` turns a local `ln` into the logarithm.
- Moss is drawn only by `cb-moss` (`lib/cb_moss.ps`), so she looks the same on every page. Change her there, never per page. Set her options (`cb-face`, `cb-eyes`, `cb-tuck`, `cb-trail`) just before a call.
- Draw with the house style in `lib/cb_kit.ps`: `cb-wash` / `cb-bigwash` (watercolour), `cb-line` (ink), `cb-text` (wrapped type, NewCenturySchlbk 21 pt), one palette. Build transformed shapes inside `{ ... } cb-local`, so brushes paint at page scale.
- Keep text in a quiet area (the sky band at the top) and keep stars, grass and other marks out of it.
- Use only the standard 35 fonts: CI has no font packs, and an unknown face silently becomes Helvetica.
- When a pscat bug, a missing feature or a skill-doc mistake turns up, search PSCatLabs/pscat issues (open and closed). File it there with the version and a minimal repro, and add a row to `docs/pscat-issues.md`.
- Work happens on a branch per change, merged by PR into `main` once CI is green. CI renders every page and binds the PDF with the pinned pscat.
