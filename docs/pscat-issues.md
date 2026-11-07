# pscat friction log

Bugs, missing features and surprises met while making these books with pscat
0.7.0-rc.4, with the upstream issue for each.

| What | Upstream | Workaround here |
|---|---|---|
| PDF output draws text as outlines: the book's words are vector paths, sharp in print, but the PDF has no searchable or copyable text and no embedded fonts. | [PSCatLabs/pscat#1026](https://github.com/PSCatLabs/pscat/issues/1026) (open) | None needed for print. The story's text is in `README.md`. |
| When an operator fails inside a `bind`-ed procedure, the error names the procedure, or a variable near it, instead of the operator. A four-operand `curveto` in `cb-moss` was reported as `OffendingCommand: s`. Repro: `pscat -e '/f { newpath 0 0 moveto 1 2 3 4 curveto } bind def f'` gives `OffendingCommand: f`; without `bind` it gives `curveto`. | [PSCatLabs/pscat#1074](https://github.com/PSCatLabs/pscat/issues/1074) (open) | When an error names something that can't fail, look for a bad operand count on the nearest path operator (`curveto` takes six numbers). |
| `pkwash` `/Grain` on page-sized washes multiplies the PDF size (about 2 MB a page, against 0.4 MB without it) and can't be seen in print at that scale. | n/a (by design) | `cb-bigwash` uses `/Grain 0`; small washes keep it. |
| `pkwash` ignores the caller's `setalpha`: it sets its own alpha per layer, so `gsave 0.6 setalpha … grestore` around a wash has no effect. Found by Codex reviewing *Puff*'s rainbow. | [PSCatLabs/pscat#1075](https://github.com/PSCatLabs/pscat/issues/1075) (open) | Fade a wash with `/Alpha` (`cb-wash`'s strength argument), not `setalpha`. `cb-rainbow` does this. |
