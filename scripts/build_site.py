#!/usr/bin/env python3
"""Build the GitHub Pages site into dist/ from the repo's Markdown.

    python3 scripts/build_site.py            # -> dist/
    python3 scripts/build_site.py out/       # somewhere else

The Markdown files stay the single source; this only renders them. Pages:

    index.html                 every book, and the process in brief
    process.html               docs/process.md
    pscat-notes.html           docs/pscat-issues.md
    <slug>/index.html          books/<slug>/README.md (the book's landing page)
    <slug>/<stage>.html        books/<slug>/01-ideation.md, 02-manuscript.md,
                               03-storyboard.md, 05-reflection.md, checkpoints.md

Each book's PDF, previews/ and storyboard sheet are copied next to its pages.
Links between Markdown files become links between pages; a link to any other
repo file goes to it on GitHub. Standard library only: no Markdown package.
"""
import html
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "https://github.com/ArtColony/childrens_book"
SITE_TITLE = "Picture books in PostScript"

STAGES = [  # (source name, page name, label)
    ("README.md", "index.html", "The book"),
    ("01-ideation.md", "ideation.html", "1 · Ideation"),
    ("02-manuscript.md", "manuscript.html", "2 · Manuscript"),
    ("03-storyboard.md", "storyboard.html", "3 · Storyboard"),
    ("checkpoints.md", "checkpoints.html", "Checkpoints"),
    ("05-reflection.md", "reflection.html", "5 · Reflection"),
]


# ------------------------------------------------------------------ markdown
def inline(text, link):
    """Inline Markdown -> HTML. link(url) rewrites link targets."""
    codes = []

    def keep_code(m):
        codes.append("<code>%s</code>" % html.escape(m.group(1)))
        return "\x00%d\x00" % (len(codes) - 1)

    text = re.sub(r"`([^`]+)`", keep_code, text)
    text = html.escape(text, quote=False)
    text = re.sub(
        r"!\[([^\]]*)\]\(([^)\s]+)\)",
        lambda m: '<img src="%s" alt="%s" loading="lazy">' % (link(m.group(2)), m.group(1)),
        text,
    )
    text = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        lambda m: '<a href="%s">%s</a>' % (link(m.group(2)), m.group(1)),
        text,
    )
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)
    return text


def slugify(text):
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def render(md, link):
    """Block Markdown -> HTML: headings, paragraphs, lists (nested, task),
    tables, blockquotes, fenced code, rules."""
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)

    def is_block_start(s):
        return bool(
            re.match(r"(#{1,6} |```|> ?|\||---\s*$|\s*([-*]|\d+\.) )", s)
        )

    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        m = re.match(r"(#{1,6}) (.*)", line)
        if m:
            level = len(m.group(1))
            body = inline(m.group(2), link)
            out.append('<h%d id="%s">%s</h%d>' % (level, slugify(body), body, level))
            i += 1
            continue
        if line.startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            out.append("<pre><code>%s</code></pre>" % html.escape("\n".join(buf)))
            continue
        if re.match(r"---\s*$", line):
            out.append("<hr>")
            i += 1
            continue
        if line.startswith(">"):
            buf = []
            while i < n and lines[i].startswith(">"):
                buf.append(re.sub(r"^> ?", "", lines[i]))
                i += 1
            out.append("<blockquote>%s</blockquote>" % render("\n".join(buf), link))
            continue
        if line.startswith("|"):
            rows = []
            while i < n and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head = rows[0]
            sep = len(rows) > 1 and re.match(r"[-: |]+$", "|".join(rows[1]))
            body = rows[2:] if sep else rows[1:]
            grid = not any(head)  # a headerless table is an image grid
            t = ['<div class="table%s"><table>' % (" grid" if grid else "")]
            if not grid:
                t.append("<thead><tr>%s</tr></thead>" % "".join("<th>%s</th>" % inline(c, link) for c in head))
            t.append("<tbody>")
            for r in body:
                t.append("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c, link) for c in r))
            t.append("</tbody></table></div>")
            out.append("".join(t))
            continue
        m = re.match(r"(\s*)([-*]|\d+\.) ", line)
        if m:
            buf = []
            while i < n and (lines[i].strip() == "" or re.match(r"\s*([-*]|\d+\.) ", lines[i]) or lines[i].startswith("  ")):
                if lines[i].strip() == "" and (i + 1 >= n or not re.match(r"\s", lines[i + 1] or "x") and not re.match(r"\s*([-*]|\d+\.) ", lines[i + 1])):
                    break
                buf.append(lines[i])
                i += 1
            out.append(render_list(buf, link))
            continue
        buf = []
        while i < n and lines[i].strip() and not is_block_start(lines[i]):
            buf.append(lines[i].strip())
            i += 1
        if not buf:  # an unrecognised line that looks like a block start
            buf.append(lines[i].strip())
            i += 1
        out.append("<p>%s</p>" % inline(" ".join(buf), link))
    return "\n".join(out)


def render_list(lines, link):
    lines = [l for l in lines if l.strip()]
    indent = len(lines[0]) - len(lines[0].lstrip())
    ordered = bool(re.match(r"\s*\d+\.", lines[0]))
    items = []
    for l in lines:
        here = len(l) - len(l.lstrip())
        m = re.match(r"\s*([-*]|\d+\.) (.*)", l)
        if m and here == indent:
            items.append([m.group(2)])
        else:
            items[-1].append(l[indent:] if len(l) - len(l.lstrip()) > indent else l.strip())
    tag = "ol" if ordered else "ul"
    out = ["<%s>" % tag]
    for it in items:
        first, rest = it[0], it[1:]
        sub = [r for r in rest if re.match(r"\s*([-*]|\d+\.) ", r)]
        cont = [r.strip() for r in rest if not re.match(r"\s*([-*]|\d+\.) ", r)]
        text = " ".join([first] + cont)
        cls = ""
        m = re.match(r"\[( |x)\] (.*)", text)
        if m:  # a checkpoint item: [ ] open, [x] passed
            cls = ' class="task %s"' % ("done" if m.group(1) == "x" else "todo")
            text_html = '<span class="box" aria-hidden="true"></span>' + inline(m.group(2), link)
        else:
            text_html = inline(text, link)
        nested = render_list(sub, link) if sub else ""
        out.append("<li%s>%s%s</li>" % (cls, text_html, nested))
    out.append("</%s>" % tag)
    return "".join(out)


# ------------------------------------------------------------------ site
def page(title, body, rel, nav):
    """Wrap body in the site chrome. rel is the path back to the site root."""
    links = "".join('<a href="%s%s">%s</a>' % (rel, href, label) for href, label in nav)
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<link rel="stylesheet" href="%ssite.css">
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="%sindex.html">%s</a>
<nav>%s</nav>
</div></header>
<main class="wrap">%s</main>
<footer class="wrap">An <a href="https://github.com/ArtColony">ArtColony</a> project ·
written, painted and set in PostScript, rendered with
<a href="https://github.com/PSCatLabs/pscat">pscat</a> ·
<a href="%s">source</a> · CC0</footer>
</body>
</html>
""" % (html.escape(title), rel, rel, SITE_TITLE, links, body, REPO)


def books():
    d = os.path.join(ROOT, "books")
    return sorted(b for b in os.listdir(d) if os.path.isdir(os.path.join(d, b)))


def title_of(md_path):
    with open(md_path) as f:
        for line in f:
            if line.startswith("# "):
                return line[2:].strip()
    return os.path.basename(md_path)


def first_para(md_path):
    with open(md_path) as f:
        text = f.read()
    for block in text.split("\n\n")[1:]:
        if block.strip() and not block.startswith(("#", "!", "|", "**[")):
            return block.strip()
    return ""


def build(dist):
    if os.path.isdir(dist):
        shutil.rmtree(dist)
    os.makedirs(dist)
    shutil.copy(os.path.join(ROOT, "scripts", "site.css"), dist)

    # every Markdown source -> its page, relative to dist
    pages = {
        "docs/process.md": "process.html",
        "docs/pscat-issues.md": "pscat-notes.html",
    }
    for b in books():
        for src, dst, _ in STAGES:
            if os.path.exists(os.path.join(ROOT, "books", b, src)):
                pages["books/%s/%s" % (b, src)] = "%s/%s" % (b, dst)

    def linker(src):
        src_dir = os.path.dirname(src)
        out_dir = os.path.dirname(pages[src])

        def link(url):
            if re.match(r"[a-z]+:|#|/", url):
                return url
            path, _, frag = url.partition("#")
            target = os.path.normpath(os.path.join(src_dir, path)).replace(os.sep, "/")
            if target.endswith("/") or os.path.isdir(os.path.join(ROOT, target)):
                readme = target.rstrip("/") + "/README.md"
                if readme in pages:
                    target = readme
            if target in pages:
                href = os.path.relpath(pages[target], out_dir or ".")
            elif target.startswith("books/") and os.path.isfile(os.path.join(ROOT, target)):
                # a book's own asset (PDF, preview, sheet): copied beside its pages
                href = os.path.relpath(target[len("books/"):], out_dir or ".")
            else:
                kind = "tree" if os.path.isdir(os.path.join(ROOT, target)) else "blob"
                return "%s/%s/main/%s%s" % (REPO, kind, target, "#" + frag if frag else "")
            return href + ("#" + frag if frag else "")

        return link

    top_nav = [("index.html", "Books"), ("process.html", "The process"), ("pscat-notes.html", "pscat notes")]

    for src, dst in pages.items():
        with open(os.path.join(ROOT, src)) as f:
            md = f.read()
        body = render(md, linker(src))
        rel = "../" * dst.count("/")
        if src.startswith("books/"):
            b = src.split("/")[1]
            tabs = "".join(
                '<a class="%s" href="%s">%s</a>' % ("on" if d == os.path.basename(dst) else "", d, label)
                for s, d, label in STAGES
                if os.path.exists(os.path.join(ROOT, "books", b, s))
            )
            body = '<nav class="stages">%s</nav><article>%s</article>' % (tabs, body)
        else:
            body = "<article>%s</article>" % body
        title = title_of(os.path.join(ROOT, src))
        out = os.path.join(dist, dst)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w") as f:
            f.write(page(title, body, rel, top_nav))

    # each book's assets, beside its pages
    for b in books():
        src = os.path.join(ROOT, "books", b)
        dst = os.path.join(dist, b)
        os.makedirs(dst, exist_ok=True)
        for name in os.listdir(src):
            p = os.path.join(src, name)
            if name.endswith((".pdf", ".png")):
                shutil.copy(p, dst)
            elif name in ("previews",) or (name == "03-storyboard" and os.path.isdir(p)):
                for f in os.listdir(p):
                    if f.endswith(".png"):
                        os.makedirs(os.path.join(dst, name), exist_ok=True)
                        shutil.copy(os.path.join(p, f), os.path.join(dst, name, f))

    # the home page: one card per book, then the process in brief
    cards = []
    for b in books():
        readme = os.path.join(ROOT, "books", b, "README.md")
        if not os.path.exists(readme):
            continue
        cover = "%s/previews/00_cover.png" % b
        img = '<img src="%s" alt="">' % cover if os.path.exists(os.path.join(dist, cover)) else ""
        pdf = "%s/%s.pdf" % (b, b)
        read = ' · <a href="%s">PDF</a>' % pdf if os.path.exists(os.path.join(dist, pdf)) else ""
        cards.append(
            '<div class="card"><a href="%s/index.html">%s</a><h2><a href="%s/index.html">%s</a></h2>'
            "<p>%s</p><p class=\"muted\"><a href=\"%s/index.html\">About the book</a>%s</p></div>"
            % (b, img, b, html.escape(title_of(readme)), inline(first_para(readme), lambda u: u), b, read)
        )
    intro = """<h1>Picture books, written and painted in PostScript</h1>
<p class="lede">An exploration of making long creative artifacts in stages. Each
book here goes from ideas, to a manuscript, to a storyboard, to painted pages
bound into a print PDF, and ends with a reflection on what the finished book
actually says. Every page is a short PostScript program, rendered with
<a href="https://github.com/PSCatLabs/pscat">pscat</a>.</p>
<p><a class="button" href="process.html">Read about the process</a></p>"""
    with open(os.path.join(dist, "index.html"), "w") as f:
        f.write(page(SITE_TITLE, intro + '<div class="cards">%s</div>' % "".join(cards), "", top_nav))
    open(os.path.join(dist, ".nojekyll"), "w").close()
    print("site: %d pages -> %s" % (len(pages) + 1, os.path.relpath(dist, ROOT)))


if __name__ == "__main__":
    build(os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "dist")))
