#!/usr/bin/env python3
"""Test suite for the Context & Memory AI Guide.

Run from the repo root (or anywhere — paths are repo-relative):

    python3 tests/run_tests.py

Zero dependencies. Covers:

  1. Unit tests for the Markdown converter in build.py
  2. Documentation integrity tests (structure, links, no stray artifacts)
  3. Build output tests (site/ contains every page, valid HTML basics,
     internal links resolve, license/credit present)
"""

import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build  # noqa: E402

PASS = 0
FAIL = 0
FAILURES: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  ok    {name}")
    else:
        FAIL += 1
        FAILURES.append(f"{name}{(' — ' + detail) if detail else ''}")
        print(f"  FAIL  {name}{(': ' + detail) if detail else ''}")


def section(title: str) -> None:
    print(f"\n{title}")


# ---------------------------------------------------------------- converter
section("Converter: inline formatting")

html = build.convert("plain text")
check("paragraphs", "<p>plain text</p>" in html)
check("html escaped", "&lt;b&gt;hi&lt;/b&gt;" in build.convert("<b>hi</b>"))
check("bold", "<strong>bold</strong>" in build.convert("**bold**"))
check("italic", "<em>soft</em>" in build.convert("*soft*"))
check("italic not greedy", "<em>a</em> and <em>b</em>" in build.convert("*a* and *b*"))
check("bold inside sentence", "say <strong>this</strong> now" in build.convert("say **this** now"))
check("inline code", "<code>npm run</code>" in build.convert("`npm run`"))
check("code inside link text escapes", "<code>x</code>" in build.convert("[`x`](a.md)") )


section("Converter: links")

check(
    "md link rewritten to html",
    '<a href="01-tokens.html">next</a>' in build.convert("[next](01-tokens.md)"),
)
check("external link untouched", '<a href="https://example.com">' in build.convert("[e](https://example.com)"))
check("anchor untouched", '<a href="#top">' in build.convert("[t](#top)"))


section("Converter: headings")

h = build.convert("## A Heading\n\nbody")
check("h2 produced", "<h2 id=\"a-heading\">A Heading</h2>" in h)
check("paragraph separated", "<p>body</p>" in h)
h = build.convert("### Deep")
check("h3 produced", "<h3" in h and "Deep</h3>" in h)
h = build.convert("# Title ...")
check("h1 produced", "<h1" in h)


section("Converter: lists")

h = build.convert("- one\n- two")
check("unordered list", "<ul>" in h and "<li>one</li>" in h and "<li>two</li></ul>" in h)
h = build.convert("1. one\n2. two")
check("ordered list", "<ol>" in h and "<li>one</li>" in h)
h = build.convert("- [ ] todo\n- [x] done")
check("open checkbox", f'<li>{build.CHECK_OPEN}todo</li>' in h)
check("closed checkbox", f'<li>{build.CHECK_CLOSED}done</li>' in h)
h = build.convert("- **bold item** with *stuff*")
check("inline inside list", "<li><strong>bold item</strong> with <em>stuff</em></li>" in h)


section("Converter: blocks")

h = build.convert("```\nstring = 'x'\n```")
check("fenced code block", "<pre><code>string = 'x'\n</code></pre>" in h)
check("code block escapes html", "&lt;script&gt;" in build.convert("```\n<script>\n```"))
h = build.convert("| A | B |\n| --- | --- |\n| 1 | 2 |")
check("table produced", "<table>" in h and "<th>A</th>" in h and "<td>1</td>" in h)
check("table cell bold converted",
      "<td><strong>1</strong></td>" in build.convert("| A | B |\n| --- | --- |\n| **1** | 2 |"))
h = build.convert("> quoted wisdom")
check("blockquote", "<blockquote>quoted wisdom</blockquote>" in h)
h = build.convert("para\n\n---\n\npara2")
check("horizontal rule", "<hr>" in h)
h = build.convert("line one\nstill same paragraph")
check("paragraph wrap", "<p>line one still same paragraph</p>" in h)
h = build.convert("intro para\n## heading next")
check("heading interrupts paragraph", "<p>intro para</p>" in h and "<h2" in h)


# ---------------------------------------------------------------- docs
section("Documentation: structure and hygiene")

all_source = PAGES = {p.name: p for p in sorted((ROOT / "docs").glob("*.md"))}
check("12 markdown docs present", len(all_source) == 12,
      f"found {len(all_source)}")
check(
    "expected doc files exist",
    set(all_source) == {
        "00-read-me-first.md","01-tokens.md","02-context-windows.md","03-chat-memory.md",
        "04-when-to-start-fresh.md","05-summarize-and-pin.md","06-pasting-documents.md",
        "07-why-answers-drift.md","08-memory-settings.md","worksheet.md","checklist.md","glossary.md",
    },
)

for name, path in all_source.items():
    text = path.read_text(encoding="utf-8")
    check(f"{name}: starts with H1", re.match(r"^# ", text) is not None)
    check(f"{name}: no TODO/FIXME/XXX markers", not re.search(r"\b(TODO|FIXME|XXX)\b", text))
    check(f"{name}: non-ASCII only in known set",
          all(ch.isascii() or ch in "’‘“”—…→←·¾≈&©" for ch in text))

# every internal .md link must point to a real doc
linked = 0
for name, path in all_source.items():
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\((?!https?|#)([^)#\s]+?\.md)\)", text):
        linked += 1
        check(f"{name}: link target exists ({target})", (ROOT / "docs" / target).exists())
check("internal markdown links were exercised", linked > 10, f"only {linked} found")


# ---------------------------------------------------------------- output
section("Build output: site/")

with tempfile.TemporaryDirectory() as tmp:
    # build into a temp dir to verify build() works anywhere, then into site/
    orig_site = build.SITE
    try:
        build.SITE = Path(tmp) / "site"
        build.build()
        produced = sorted(p.name for p in build.SITE.glob("*.html"))
        check("index + 12 pages produced", len(produced) == 13, str(produced))
        check("stylesheet copied", (build.SITE / "assets" / "style.css").exists())
        body_count = sum(
            (build.SITE / p.name).read_text(encoding="utf-8").count("<body>") == 1
            for p in build.SITE.glob("*.html")
        )
        check("every page has exactly one <body>", body_count == 13)
    finally:
        build.SITE = orig_site


# real site/ must be present and consistent (run `python3 build.py` first)
if not (ROOT / "site" / "index.html").exists():
    print("note: site/ missing; running build.py to generate it")
    build.main()


def rel_links_resolve(page: Path) -> None:
    text = page.read_text(encoding="utf-8")
    for href in re.findall(r'href="([^"#]+?\.html)"', text):
        check(f"{page.name}: resolves {href}",
              (ROOT / "site" / href).exists() or href.startswith("http"))


for page in (ROOT / "site").glob("*.html"):
    text = page.read_text(encoding="utf-8")
    check(f"site/{page.name}: title set", "<title>" in text)
    check(f"site/{page.name}: footer credit",
          "Asdale Dynamics, LLC" in text)
    check(f"site/{page.name}: no unresolved md links", '.md"' not in text)
    check(f"site/{page.name}: no raw unescaped ampersand",
          not re.search(r"&(?!(amp|lt|gt|quot|middot|#\d+|larr|rarr|mdash);)\S{0,8};", text), )
    rel_links_resolve(page)


section("License and README")

lic = (ROOT / "LICENSE").read_text(encoding="utf-8")
check("LICENSE: MIT named", "MIT License" in lic)
check("LICENSE: exact copyright line", "Copyright (c) 2026 Asdale Dynamics, LLC" in lic)
readme = (ROOT / "README.md").read_text(encoding="utf-8")
check("README: credits Asdale Dynamics, LLC", "Asdale Dynamics, LLC" in readme)
check("README: no secrets markers", not re.search(
    r"(api[_-]?key|secret|password|token=)[\s:=]+\S", readme, flags=re.IGNORECASE))


section("build.py PAGES wiring")

src_names = {src for src, _p, _l in build.PAGES}
check("PAGES source names match docs exactly", src_names == set(all_source), str(src_names ^ set(all_source)))
check("PAGES output names are .html", all(p.endswith(".html") for _s, p, _l in build.PAGES))
check("PAGES outputs unique", len({p for _s, p, _l in build.PAGES}) == len(build.PAGES))


# ---------------------------------------------------------------- summary
print(f"\n{'=' * 60}")
print(f"{PASS} passed, {FAIL} failed")
if FAILURES:
    print("\nFailures:")
    for f in FAILURES:
        print(f"  - {f}")
sys.exit(1 if FAIL else 0)
