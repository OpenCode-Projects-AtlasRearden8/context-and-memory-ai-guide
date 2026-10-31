# STATUS — context-and-memory-ai-guide

Last updated: 2026-10-31

## What was built

A complete, self-contained manual repo: **"Context & Memory: The AI Guide Nobody Passed to You"** — a friend-toned beginner manual for AI context windows, tokens, and chat memory, in the plain-English style of Dylan Asdale / Asdale Dynamics, LLC.

**Content (12 Markdown documents in `docs/`):**

- `00-read-me-first.md` — two-minute orientation
- `01-tokens.md` — what tokens are and why they matter
- `02-context-windows.md` — the working-memory "whiteboard" model
- `03-chat-memory.md` — inside-chat vs. across-chat memory
- `04-when-to-start-fresh.md` — when/how to restart, including the one-message handoff-note ritual
- `05-summarize-and-pin.md` — the 6-part context-header template, pinning, custom instructions
- `06-pasting-documents.md` — on-ramp messages, segmentation, privacy discipline
- `07-why-answers-drift.md` — five causes of drift + escalating fixes
- `08-memory-settings.md` — universal settings concepts + per-tool quick map (ChatGPT, Claude, Gemini, Copilot, local AI)
- `worksheet.md` — 11-question self-audit with follow-through
- `checklist.md` — situation-ordered action checklists
- `glossary.md` — ~35 terms in plain English

**Tooling:**

- `build.py` — zero-dependency Python Markdown-to-HTML converter for the manual's Markdown subset (headings, lists, checkboxes, tables, fenced code, blockquotes, inline styles, links with `.md` → `.html` rewriting). Builds `site/index.html`, 12 chapter pages, and `site/assets/style.css` (inline CSS, no dependencies).
- `build.sh` — wrapper; `./build.sh` builds, `./build.sh --check` builds + runs tests.
- `tests/run_tests.py` — 219-test zero-dependency suite: converter unit tests, doc hygiene (H1s, no TODO markers, internal `.md` links resolve), build-output tests into a temp dir, real-site checks (link resolution, footer credit, no raw `&`, tag-balance sanity), LICENSE/README verification, and `build.PAGES` wiring checks.

**Deliberately distinct from sibling projects:** no token calculator (that's `token-budget-calculator-cli`) and no model-settings dials guide (that's `model-settings-decoded-guide`) — only referenced as related reading.

## How to run it

```bash
./build.sh                 # build site/ from docs/
./build.sh --check         # build + run the test suite
python3 tests/run_tests.py # tests only
```

Then open `site/index.html` in any browser. Fully local — no server, network, accounts, or packages required beyond Python 3.8+.

## Verification results

- `./build.sh --check`: builds 13 pages; **219 passed, 0 failed.**
- HTML tag-balance check (html.parser) across all 13 pages: OK.
- Every internal `.md` link in docs resolves to a real file; every `.html` link in site/ resolves.
- LICENSE contains the exact line `Copyright (c) 2026 Asdale Dynamics, LLC`; README and every site footer credit Asdale Dynamics, LLC.
- Site is locally browsable: stylized index with chapter cards, per-page prev/next pager, print-friendly serif layout.
- Git: initialized locally, single clean commit, no remote, nothing pushed/published. No secrets or personal data in any file (checked by a test).

## Known gaps

- The converter implements a scoped Markdown subset (no nested lists, image syntax, or arbitrary HTML pass-through). If future chapters need more syntax, extend `build.py` — the test suite will catch regressions.
- Chapter 8's per-tool settings are concept-first with a snapshot table; product menus change, so that table will need occasional refreshes.
- No search box in the site; the glossary and index linking cover navigation for a doc this size.
- No dark mode (kept the warm paper-light theme intentionally simple).
- The site is generated, so a fresh clone needs `./build.sh` before opening `site/` — though the generated pages are committed as well.
