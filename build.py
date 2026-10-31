#!/usr/bin/env python3
"""Context & Memory AI Guide — zero-dependency Markdown-to-HTML site builder.

Converts docs/*.md into site/*.html using a small, purpose-built converter
that supports the Markdown subset this manual uses: headings, paragraphs,
unordered/ordered/checkbox lists, fenced code blocks, blockquotes, simple
tables, horizontal rules, and inline code/bold/italic/links.

Usage:
    python3 build.py            build the site
    python3 build.py --clean    build after wiping site/
"""

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

COPYRIGHT = "Copyright (c) 2026 Asdale Dynamics, LLC"

# (source md filename, page path relative to site root, nav label)
PAGES = [
    ("00-read-me-first.md", "00-read-me-first.html", "Read me first"),
    ("01-tokens.md", "01-tokens.html", "1. Tokens"),
    ("02-context-windows.md", "02-context-windows.html", "2. The context window"),
    ("03-chat-memory.md", "03-chat-memory.html", "3. Chat memory"),
    ("04-when-to-start-fresh.md", "04-when-to-start-fresh.html", "4. Fresh chats"),
    ("05-summarize-and-pin.md", "05-summarize-and-pin.html", "5. Summarize & pin"),
    ("06-pasting-documents.md", "06-pasting-documents.html", "6. Pasting documents"),
    ("07-why-answers-drift.md", "07-why-answers-drift.html", "7. Why answers drift"),
    ("08-memory-settings.md", "08-memory-settings.html", "8. Memory settings"),
    ("worksheet.md", "worksheet.html", "Worksheet"),
    ("checklist.md", "checklist.html", "Checklist"),
    ("glossary.md", "glossary.html", "Glossary"),
]

SITE_TITLE = "Context & Memory: The AI Guide Nobody Passed to You"
SITE_TAGLINE = (
    "A friend-toned manual for the part of AI nobody explains — context windows, "
    "tokens, and chat memory."
)

STYLE_CSS = """:root {
  --paper: #fdfbf7;
  --ink: #2d2a26;
  --soft: #6b645c;
  --accent: #2563eb;
  --accent-soft: #dbeafe;
  --line: #e7e2da;
  --card: #ffffff;
  --green: #15803d;
}
* { box-sizing: border-box; }
html { font-size: 16px; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: Georgia, 'Iowan Old Style', 'Times New Roman', serif;
  line-height: 1.7;
}
header.site {
  background: var(--ink);
  color: #fff;
}
header.site .wrap { display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; }
header.site a { color: #fff; text-decoration: none; font-weight: bold; }
header.site .tag { color: #c9c2b8; font-size: 0.9rem; font-style: italic; }
main { max-width: 46rem; margin: 0 auto; padding: 2rem 1.25rem 3rem; }
h1, h2, h3, h4 { line-height: 1.25; font-family: 'Helvetica Neue', Arial, sans-serif; }
h1 { font-size: 2rem; margin: 0.5rem 0 1.5rem; }
h2 { font-size: 1.45rem; margin-top: 2.2rem; border-bottom: 2px solid var(--line); padding-bottom: 0.3rem; }
h3 { font-size: 1.15rem; margin-top: 1.8rem; }
h4 { font-size: 1rem; margin-top: 1.5rem; }
p, li { font-size: 1.05rem; }
a { color: var(--accent); }
a:hover { text-decoration: none; }
code {
  font-family: ui-monospace, 'SF Mono', Menlo, Consolas, monospace;
  font-size: 0.88em;
  background: #efece6;
  border: 1px solid var(--line);
  border-radius: 4px;
  padding: 0.1em 0.35em;
}
pre {
  background: #2d2a26;
  color: #f3efe9;
  padding: 1rem 1.2rem;
  border-radius: 8px;
  overflow-x: auto;
  line-height: 1.5;
}
pre code {
  background: transparent;
  border: 0;
  color: inherit;
  padding: 0;
  font-size: 0.88rem;
}
blockquote {
  margin: 1.2rem 0;
  padding: 0.6rem 1.1rem;
  border-left: 4px solid var(--accent);
  background: var(--accent-soft);
  border-radius: 0 6px 6px 0;
  color: #1e3a8a;
}
table { border-collapse: collapse; width: 100%; margin: 1.2rem 0; font-size: 0.98rem; }
th, td { border: 1px solid var(--line); padding: 0.45rem 0.7rem; text-align: left; }
th { background: #f3efe9; font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 0.9rem; }
tr:nth-child(even) td { background: #faf7f1; }
input[type=checkbox] { margin-right: 0.35rem; accent-color: var(--green); }
hr { border: 0; border-top: 2px solid var(--line); margin: 2.5rem 0; }
footer.site {
  background: var(--ink);
  color: #c9c2b8;
  text-align: center;
  padding: 1.5rem 1rem;
  font-size: 0.9rem;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}
footer.site a { color: #fff; }
nav.pager { display: flex; justify-content: space-between; margin-top: 3rem; font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 0.95rem; }
nav.pager a { text-decoration: none; }
nav.pager .side { max-width: 46%; }
.cards { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 2rem 0; }
@media (max-width: 640px) { .cards { grid-template-columns: 1fr; } }
.card {
  display: block; text-decoration: none; color: var(--ink);
  background: var(--card); border: 1px solid var(--line); border-radius: 10px;
  padding: 0.9rem 1.1rem;
}
.card:hover { border-color: var(--accent); }
.card .num { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 0.78rem; color: var(--soft); text-transform: uppercase; letter-spacing: 0.05em; }
.card .t { font-weight: bold; font-family: 'Helvetica Neue', Arial, sans-serif; margin: 0.15rem 0; }
.lead { font-size: 1.15rem; color: var(--soft); }
.crumbs { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 0.85rem; color: var(--soft); margin-bottom: 1rem; }
.crumbs a { text-decoration: none; }
"""

CHECK_OPEN = '<input type="checkbox" disabled>'
CHECK_CLOSED = '<input type="checkbox" disabled checked>'


def escape_html(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


INLINE_TOKEN = "\x00{}"


def inline(text: str) -> str:
    """Convert inline markdown (code, links, bold, italic) to HTML."""
    code_spans: list[str] = []

    def stash(m: "re.Match[str]") -> str:
        code_spans.append(escape_html(m.group(1)))
        return INLINE_TOKEN.format(len(code_spans) - 1)

    text = escape_html(text)
    # inline code first so its contents are not further processed
    text = re.sub(r"`([^`]+)`", stash, text)
    # links; rewrite local .md targets to .html
    text = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        lambda m: '<a href="{0}">{1}</a>'.format(_rewrite_link(m.group(2)), m.group(1)),
        text,
    )
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    for i, span in enumerate(code_spans):
        text = text.replace(INLINE_TOKEN.format(i), "<code>" + span + "</code>")
    return text


def _rewrite_link(target: str) -> str:
    if target.endswith(".md"):
        return target[:-3] + ".html"
    return target


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.ASCII)
    return re.sub(r"[\s]+", "-", text.strip().lower())[:60] or "heading"


def convert(md_text: str) -> str:
    """Convert manual-subset Markdown to an HTML fragment."""
    lines = md_text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # fenced code block
        if stripped.startswith("```"):
            i += 1
            block: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1  # skip closing fence
            out.append("<pre><code>" + escape_html("\n".join(block)) + "\n</code></pre>")
            continue

        # horizontal rule
        if re.fullmatch(r"-{3,}", stripped) or re.fullmatch(r"\*{3,}", stripped):
            out.append("<hr>")
            i += 1
            continue

        # headings
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            level, text = len(m.group(1)), m.group(2)
            idattr = ' id="' + slugify(re.sub(r"[*`]", "", text)) + '"'
            out.append(f"<h{level}{idattr}>{inline(text)}</h{level}>")
            i += 1
            continue

        # table
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(
            r"^\|[\s:|-]+\|?$", lines[i + 1].strip()
        ):
            header = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append("<table>")
            out.append("<thead><tr>" + "".join("<th>" + inline(c) + "</th>" for c in header) + "</tr></thead>")
            if rows:
                out.append("<tbody>")
                for row in rows:
                    out.append("<tr>" + "".join("<td>" + inline(c) + "</td>" for c in row) + "</tr>")
                out.append("</tbody>")
            out.append("</table>")
            continue

        # blockquote
        if stripped.startswith(">"):
            quotes: list[str] = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quotes.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append("<blockquote>" + inline(" ".join(quotes)) + "</blockquote>")
            continue

        # unordered list (with checkbox support)
        if re.match(r"^-\s", stripped):
            items: list[str] = []
            while i < len(lines) and re.match(r"^\s*-\s", lines[i]):
                item = re.sub(r"^\s*-\s+", "", lines[i])
                check = re.match(r"^\[( |x|X)\]\s+", item)
                if check:
                    boxes = CHECK_CLOSED if check.group(1).lower() == "x" else CHECK_OPEN
                    item = re.sub(r"^\[( |x|X)\]\s+", "", item)
                    items.append("<li>" + boxes + inline(item) + "</li>")
                else:
                    items.append("<li>" + inline(item) + "</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue

        # ordered list
        if re.match(r"^\d+\.\s", stripped):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s", lines[i]):
                item = re.sub(r"^\s*\d+\.\s+", "", lines[i])
                items.append("<li>" + inline(item) + "</li>")
                i += 1
            out.append("<ol>" + "".join(items) + "</ol>")
            continue

        # blank line
        if not stripped:
            i += 1
            continue

        # paragraph
        block = [stripped]
        while (
            i + 1 < len(lines)
            and lines[i + 1].strip()
            and not re.match(r"^(#{1,6}\s|\|[-:\s|]*\||>|-{3,}$|\*\*\*+$|- |\d+\. |```)", lines[i + 1].strip())
            and not lines[i + 1].strip().startswith(">")
        ):
            i += 1
            block.append(lines[i].strip())
        out.append("<p>" + inline(" ".join(block)) + "</p>")
        i += 1

    return "\n".join(out) + "\n"


def title_of(md_text: str) -> str:
    m = re.search(r"^#\s+(.+)$", md_text, flags=re.MULTILINE)
    return m.group(1).strip() if m else "Untitled"


def page_html(content: str, title: str, index: int) -> str:
    """Wrap a converted fragment in the site template with pager links."""
    source, path, label = PAGES[index]
    prev_page = PAGES[index - 1] if index > 0 else None
    next_page = PAGES[index + 1] if index + 1 < len(PAGES) else None

    def pager_link(page, kind):
        if page is None:
            return '<span class="side" style="visibility:hidden"></span>'
        _src, out_path, lbl = page
        if kind == "prev":
            return (
                f'<a class="side" style="text-align:left" '
                f'href="{out_path}">&larr; {lbl}</a>'
            )
        return (
            f'<a class="side" style="text-align:right" '
            f'href="{out_path}">{lbl} &rarr;</a>'
        )

    prev_html = pager_link(prev_page, "prev")
    next_html = pager_link(next_page, "next")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{SITE_TAGLINE}">
<title>{escape_html(title)} — {escape_html(SITE_TITLE)}</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site"><div class="wrap" style="max-width:46rem;margin:0 auto;padding:0.9rem 1.25rem">
<a href="index.html">Context &amp; Memory</a>
<span class="tag">the AI guide nobody passed to you</span>
</div></header>
<main>
<p class="crumbs"><a href="index.html">Reading guide</a> &middot; {escape_html(label)}</p>
{content}
<nav class="pager">{prev_html}{next_html}</nav>
</main>
<footer class="site">
<p>{escape_html(SITE_TITLE)}</p>
<p>Built by <a href="https://dylanasdale.github.io">Asdale Dynamics, LLC</a> &middot; {escape_html(COPYRIGHT)} &middot; MIT License</p>
</footer>
</body>
</html>
"""


def index_html() -> str:
    cards: list[str] = []
    toread = [
        ("00-read-me-first.html", "Start here", "The two-minute orientation"),
        ("01-tokens.html", "Chapter 1", "Tokens: how AI reads your words"),
        ("02-context-windows.html", "Chapter 2", "The context window: the AI's working memory"),
        ("03-chat-memory.html", "Chapter 3", "Chat memory: across the chat, and across chats"),
        ("04-when-to-start-fresh.html", "Chapter 4", "When to start a fresh chat"),
        ("05-summarize-and-pin.html", "Chapter 5", "Summarize and pin: carrying context forward"),
        ("06-pasting-documents.html", "Chapter 6", "Pasting documents the smart way"),
        ("07-why-answers-drift.html", "Chapter 7", "Why answers drift — and how to stop it"),
        ("08-memory-settings.html", "Chapter 8", "Per-tool memory settings, decoded"),
        ("worksheet.html", "Extra", "The context audit worksheet"),
        ("checklist.html", "Extra", "The context & memory checklist"),
        ("glossary.html", "Extra", "Glossary, in plain English"),
    ]
    for href, num, text in toread:
        cards.append(
            f'<a class="card" href="{href}"><span class="num">{escape_html(num)}</span>'
            f'<div class="t">{escape_html(text)}</div></a>'
        )
    cards_html = "\n".join(cards)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{SITE_TAGLINE}">
<title>{escape_html(SITE_TITLE)}</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site"><div class="wrap" style="max-width:46rem;margin:0 auto;padding:0.9rem 1.25rem">
<a href="index.html">Context &amp; Memory</a>
<span class="tag">the AI guide nobody passed to you</span>
</div></header>
<main>
<h1>Context &amp; Memory</h1>
<p class="lead">A friend-toned manual for the part of AI nobody explains: context windows, tokens, and chat memory. When to start a fresh chat, how long threads quietly forget, pasting documents the smart way, why answers drift, and per-tool memory settings — decoded.</p>
<p>New to this? <a href="00-read-me-first.html">Start with the two-minute orientation</a>. Already use AI daily? Skip to <a href="05-summarize-and-pin.html">the context-header technique</a> or <a href="08-memory-settings.html">the settings tour</a>.</p>
<div class="cards">
{cards_html}
</div>
<p>Sources live as Markdown in <code>docs/</code>; this site is generated by <code>build.py</code> (zero dependencies, fully local).</p>
</main>
<footer class="site">
<p>{escape_html(SITE_TITLE)}</p>
<p>Written by Dylan Asdale &middot; Built by <a href="https://dylanasdale.github.io">Asdale Dynamics, LLC</a> &middot; {escape_html(COPYRIGHT)} &middot; MIT License</p>
</footer>
</body>
</html>
"""


def build() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "assets").mkdir(parents=True)
    (SITE / "assets" / "style.css").write_text(STYLE_CSS, encoding="utf-8")

    for index, (source, path, _label) in enumerate(PAGES):
        md_path = DOCS / source
        if not md_path.exists():
            raise SystemExit(f"build error: missing source doc {source}")
        md_text = md_path.read_text(encoding="utf-8")
        html = page_html(convert(md_text), title_of(md_text), index)
        (SITE / path).write_text(html, encoding="utf-8")

    (SITE / "index.html").write_text(index_html(), encoding="utf-8")
    print(f"built {len(PAGES) + 1} pages into {SITE}")


def main() -> None:
    if "--clean" in sys.argv:
        if SITE.exists():
            shutil.rmtree(SITE)
    build()


if __name__ == "__main__":
    main()
