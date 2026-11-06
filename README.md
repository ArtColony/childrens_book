# childrens_book

***Moss Goes to the Sea***, a picture book written, illustrated and typeset
entirely in PostScript, and rendered with
[pscat](https://github.com/PSCatLabs/pscat) into a print-ready PDF.
An [ArtColony](https://github.com/ArtColony) project.

**[Read the book (PDF)](moss-goes-to-the-sea.pdf)**: 15 pages, 8.5 × 8.5 in, vector throughout.

![cover](previews/00_cover.png)

A small snail named Moss hears from a gull that the sea is big and blue and
sings all day. She sets off to hear it, slowly, past the cabbages, under the
gate, through grass as tall as trees and through the rain. When she arrives
at night, the sea sings *hush … hush … hush*. She falls asleep in her
shell, and finds she can still hear it there.

| | | |
|---|---|---|
| ![](previews/01_home.png) | ![](previews/02_gull.png) | ![](previews/06_meadow.png) |
| ![](previews/08_ladybird.png) | ![](previews/09_dusk.png) | ![](previews/11_the_sea.png) |

## How it's made

Every page is a short PostScript program in `book/`. Nothing is drawn by hand
or imported, and there are no bitmaps. The pictures come from pscat's
painting library (`lib/paintkit.ps`), wrapped in a small house style:

- **Watercolour.** `pkwash` lays translucent, wobble-edged washes with a
  darker rim where the pigment pools. `pkpaper` is the paper grain under
  every page.
- **Ink.** `pkliner`, a flexible brush that wanders slightly off its path and
  tapers, outlines everything near the eye.
- **Grass, rain and stars.** `pkpull` pushes up grass blades. `scatter`
  places raindrops and stars.
- **Moss.** She is one procedure, `cb-moss` in `lib/cb_moss.ps`, with a few
  options: which way she faces, eyes open, closed or looking up, tucked into
  her shell, and how long a silver trail she leaves. That keeps her the same
  snail on every page.
- **Type.** New Century Schoolbook, a classic picture-book face and one of
  the standard 35 PostScript fonts. A small word-wrapper (`cb-text`) sets it
  with curly quotes.

`scripts/book.sh` runs every page inside its own `save … restore` and has
pscat write them as one multi-page PDF. The PDF keeps real transparency for
the washes. The text is drawn as vector outlines, so it prints sharply but
can't be searched; see `docs/pscat-issues.md`.

## The story

> **1.** In a corner of the garden, under a big green leaf, lived a small snail named Moss.
>
> **2.** One morning a gull landed on the fence. "I have just come from the sea," said the gull. "It is big and blue, and all day long it sings."
>
> **3.** "I would like to hear the sea sing," said Moss. So she packed nothing at all, because a snail carries her house with her, and off she went.
>
> **4.** She went past the cabbages. *Slowly.*
>
> **5.** She went under the gate. *Slowly.*
>
> **6.** She went through the meadow, where the grass was as tall as trees. *Slowly, slowly.*
>
> **7.** Then it began to rain. Moss did not mind one bit. Snails like rain.
>
> **8.** "Where are you going?" asked a ladybird. "To hear the sea sing," said Moss. "That is very far for a snail," said the ladybird. "Then I will go very far," said Moss.
>
> **9.** The sun went down. The stars came out. Moss kept going.
>
> **10.** At last the grass turned to sand, and the sand ran all the way down to the water.
>
> **11.** There was the sea, big and silver under the moon. And it sang: *hush . . . hush . . . hush.*
>
> **12.** Moss listened until her eyes grew heavy. Then she curled up inside her shell, the way snails do.
>
> **13.** And there, inside her own small house, she could still hear the sea singing: *hush . . . hush . . . hush.*
>
> *The End*

## Setup

This repo uses the **released** pscat at the version pinned in
`.pscat-version` (a 0.7 release candidate, like the other ArtColony
projects). Install it from the
[releases page](https://github.com/PSCatLabs/pscat/releases):

```sh
v=$(cat .pscat-version)
t=aarch64-apple-darwin          # or x86_64-apple-darwin, x86_64-unknown-linux-musl, ...
gh release download "v$v" -R PSCatLabs/pscat -p "pscat-$v-$t.tar.gz" -p SHA256SUMS
shasum -a 256 -c SHA256SUMS --ignore-missing
tar xzf "pscat-$v-$t.tar.gz"
# keep the bundle together and put pscat and pscat-mcp on your PATH
pscat --version
```

## Building the book

```sh
scripts/book.sh                              # the whole book -> renders/moss-goes-to-the-sea.pdf
scripts/book.sh moss-goes-to-the-sea.pdf     # refresh the committed copy
scripts/render.sh                            # every page as a PNG -> renders/
DPI=144 scripts/render.sh book/01_home.ps    # one page at 2x
scripts/render.sh -D Seed=4 book/07_rain.ps  # another seed: different brush wobble, rain
scripts/render.sh --sweep-seed 1:9 book/07_rain.ps   # contact sheet of seeds
```

The whole book binds in a few seconds. Renders go to `renders/` (git-ignored),
or to `$CB_RENDERS` when that's set. Every run is strictly linted: an error, or
a leaked stack item or `gsave`, fails it.

## Layout

| Path | What |
|---|---|
| `book/NN_name.ps` | One file per page, in reading order: `00_cover` … `14_the_end` |
| `lib/cb_book.ps` | What every page loads: artkit, paintkit and the three `cb_` libraries |
| `lib/cb_kit.ps` | House style: trim size, palette, `cb-wash` / `cb-bigwash` / `cb-line`, `cb-text` (wrapped type), `cb-folio`, `cb-local` |
| `lib/cb_moss.ps` | `cb-moss`: the hero, with options `cb-face`, `cb-eyes`, `cb-tuck`, `cb-trail` |
| `lib/cb_world.ps` | Scenery: sky, hills, grass, flowers, leaves, cabbages, clouds, sun, moon, stars, gull, ladybird, fence, rain, sea, waves |
| `scripts/render.sh` | Render pages to PNG with strict lint and timing; `-D Name=value`, `--sweep-seed` |
| `scripts/book.sh` | Bind all pages into one PDF and check the page count |
| `moss-goes-to-the-sea.pdf` | The finished book |
| `previews/` | Chosen page renders for this README |
| `docs/pscat-issues.md` | pscat bugs and surprises met along the way |

## Licence

[CC0 1.0](LICENSE): the story, pictures and code are in the public domain.
