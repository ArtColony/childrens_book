#!/usr/bin/env python3
"""Lay page renders out as one labelled contact sheet, to judge a book as a
sequence (storyboard checkpoint) rather than page by page.

    scripts/sheet.py renders/ten-boats-home/03-storyboard sheet.png
    scripts/sheet.py DIR OUT.png --cols 4 --cell 300 [--notes notes.txt]

Each cell is a page, labelled with its file name. With --notes, a text file of
`NN_name<TAB>note` lines adds a note under the matching cell (e.g. the shot
distance and light from the page plan). Needs Pillow (local use only; CI does
not run it).
"""
import argparse
import glob
import os

from PIL import Image, ImageDraw, ImageFont


def font(size):
    for f in ("/System/Library/Fonts/Supplemental/Georgia.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"):
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    ap.add_argument("out")
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--cell", type=int, default=300)
    ap.add_argument("--notes")
    a = ap.parse_args()

    files = sorted(f for f in glob.glob(os.path.join(a.dir, "*.png"))
                   if "-frame" not in f and "-sweep" not in f)
    notes = {}
    if a.notes:
        for line in open(a.notes):
            if "\t" in line:
                k, v = line.rstrip("\n").split("\t", 1)
                notes[k] = v
    pad, lab = 14, 40
    cols = min(a.cols, len(files))
    rows = (len(files) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (a.cell + pad) + pad, rows * (a.cell + lab + pad) + pad), (246, 242, 233))
    d = ImageDraw.Draw(sheet)
    f1, f2 = font(15), font(12)
    for i, f in enumerate(files):
        x = pad + (i % cols) * (a.cell + pad)
        y = pad + (i // cols) * (a.cell + lab + pad)
        im = Image.open(f).convert("RGB")
        im.thumbnail((a.cell, a.cell))
        sheet.paste(im, (x, y))
        name = os.path.splitext(os.path.basename(f))[0]
        d.text((x, y + a.cell + 4), name, fill=(31, 27, 24), font=f1)
        if name in notes:
            d.text((x, y + a.cell + 22), notes[name], fill=(107, 100, 91), font=f2)
    sheet.save(a.out)
    print("sheet: %d pages -> %s" % (len(files), a.out))


if __name__ == "__main__":
    main()
