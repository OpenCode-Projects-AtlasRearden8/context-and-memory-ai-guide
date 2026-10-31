# Context & Memory: The AI Guide Nobody Handled You

*A friend-toned manual for the part of AI nobody explains — context windows, tokens, and chat memory. By [Dylan Asdale](https://dylanasdale.github.io) / Asdale Dynamics, LLC.*

---

## What this is

Most AI guides start with "here's how to write a prompt." This one starts earlier — with the stuff that *actually determines* whether your AI sessions go well or go sideways:

- **Tokens** — how AI reads your words (and why it occasionally misreads them)
- **Context windows** — the AI's working memory, and how fast you fill it
- **Chat memory** — what your assistant remembers across messages, and what it quietly forgets
- **When to start a fresh chat** — the single most underused skill in AI
- **Summarizing and pinning key facts** — so you never re-explain yourself five times
- **Pasting documents the smart way** — without drowning the AI
- **Why answers drift** — the slow slide into confusion, and how to stop it
- **Per-tool memory settings, decoded** — ChatGPT, Claude, Gemini, Copilot, and local AI

Written in plain English, step by step, like a friend would explain it. Never condescending.

## What this is NOT

- **Not** a token-budget calculator — that's the separate `token-budget-calculator-cli` project
- **Not** a guide to model settings dials (temperature, top-p, etc.) — that's `model-settings-decoded-guide`
- **Not** medical advice, financial advice, or legal advice
- **Not** hype, jargon, or a sales pitch

## Who it's for

Anyone who chats with AI and has ever thought: *why did it just forget that?* — nurses, small-business owners, students, resellers, authors, and total beginners. No technical background needed. If you can send a text message, you're qualified.

## Read it

- **[Start here: Read me first](docs/00-read-me-first.md)**
- All chapters live in [`docs/`](docs/) as Markdown.
- Build the friendly HTML site locally: run `./build.sh`, then open `site/index.html` in your browser.

## The docs

| Doc | What it covers |
| --- | --- |
| [00-read-me-first.md](docs/00-read-me-first.md) | The two-minute orientation |
| [01-tokens.md](docs/01-tokens.md) | What a token is, why it matters |
| [02-context-windows.md](docs/02-context-windows.md) | The AI's working memory |
| [03-chat-memory.md](docs/03-chat-memory.md) | Across the chat, and across chats |
| [04-when-to-start-fresh.md](docs/04-when-to-start-fresh.md) | The fresh-chat skill |
| [05-summarize-and-pin.md](docs/05-summarize-and-pin.md) | Carrying context forward |
| [06-pasting-documents.md](docs/06-pasting-documents.md) | Feeding docs without drowning the AI |
| [07-why-answers-drift.md](docs/07-why-answers-drift.md) | The slow slide, and the fix |
| [08-memory-settings.md](docs/08-memory-settings.md) | Per-tool settings, decoded |
| [worksheet.md](docs/worksheet.md) | Your context audit worksheet |
| [checklist.md](docs/checklist.md) | The context & memory checklist |
| [glossary.md](docs/glossary.md) | Every term, plainly defined |

## Build & test

Requirements: Python 3.8+ (no packages to install — the build is zero-dependency).

```bash
./build.sh        # builds docs/*.md into site/*.html
python3 tests/run_tests.py   # runs the test suite
./build.sh --check   # build + tests in one go
```

Output goes to `site/`. Open `site/index.html` in any browser. Everything is local — no server, no account, no data leaves your machine.

## Repository layout

```
docs/    the manual (Markdown, readable as plain text or built HTML)
site/    the built static HTML site (generated — rebuild anytime)
tests/   a zero-dependency test suite for the build
build.py the Markdown → HTML converter
build.sh the friendly wrapper
```

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Asdale Dynamics, LLC.

Built by **Asdale Dynamics, LLC** — Dylan Asdale's LLC for beginner-friendly AI education, books, and practical tools. Learn more at [dylanasdale.github.io](https://dylanasdale.github.io).
