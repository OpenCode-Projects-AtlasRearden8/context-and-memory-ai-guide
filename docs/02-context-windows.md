# The Context Window: The AI's Working Memory

---

Picture a whiteboard. Not a notebook — a **whiteboard**. At the start of a chat, your AI's whiteboard is spotless. Everything anyone writes during the chat goes on that whiteboard, including everything the AI itself writes. There are no sticky notes, no pages behind it, no filing cabinet in the next room.

When the whiteboard fills up, something happens. Depending on the tool and model, it either:

1. **stops accepting new input** (rare, dramatic, obvious), or
2. **quietly begins smudging the oldest writing** so newer content fits (common, subtle, dangerous), or
3. **routinely "compacts"** — compresses early messages into an automatic summary — which is closer to memory than forgetting, but *isn't* the same as remembering everything. (Chapter 3 covers this.)

Every tool does some mix of these. The point isn't which — it's that **long chats lose old stuff, always**, and no tool warns you loudly when it starts.

## How big is it?

Context windows have grown enormously — think of it in units of *the number of tokens that fit on the whiteboard*. In rough terms (numbers change constantly, and that's the point — check your tool's docs):

| Generation | Feel |
| --- | --- |
| Short-book size | ~10k-40k tokens — fills fast with pasted docs |
| Novels-wide | ~100k-200k tokens — a few hundred messages of plain chat |
| Larger/enterprise sizes | feeds whole codebases, legal packets, days of thread |

A 100-word message is around 200 tokens; some public figures matter more than precision. What actually matters for *you*:

- **Plain chat doesn't fill the window very fast.** Hundreds of back-and-forths fit in comfortably.
- **Documents do.** A pasted 20-page PDF can eat 15-40% of the container *by itself*.
- **Code, tables, and data are gas-guzzlers.** The AI's own long answers count, too — and if you're having it rewrite things in full, the chat fills from both sides.

## What "filling up" actually looks like

Nobody hits a wall and gets an error. What real users notice is drift:

- Formatting rules you set in message 2 no longer apply in message 40.
- The AI starts mixing up two projects you discussed.
- Answers get shorter and more generic — the model leans on its general knowledge instead of *your* specifics.
- It stops asking clarifying questions, because the pile of old messages makes it feel like it already knows what you want.

Full chapter on that in [Chapter 7](07-why-answers-drift.md). The fix is the same in every case: **the whiteboard, not your prompt, is the problem.** Blank it (fresh chat) and restore only the important writing (your summary).

## A quick map of what goes on the whiteboard

Everything, in rough order of how much room typical sessions take:

1. **Your messages** — small.
2. **The AI's messages** — slightly bigger, since it talks in paragraphs.
3. **Pasted documents** — huge.
4. **Code blocks and tables** — big.
5. **Saved memory / pinned content / custom instructions** — depends on tool; some live in the room *before* the whiteboard (Chapter 8).

## Try this

1. Open a totally fresh chat and paste **only** the last page of a document you're working on, then ask a question about it. Now, in a *second* fresh chat, paste the whole document and ask the same question. Compare answers. Notice how much *cleaner* the small-context answer often is — extra context can be noise as much as fuel.
2. In a long-running chat, ask: **"Recap what we've decided so far in bullet points."** The AI works from its whiteboard, so you'll see exactly what it's holding — including anything it *thinks* you've decided that you haven't.
3. Next time a long chat starts feeling cloudy, resist the urge to type "remember, as I said earlier…" — that's just writing on an already-smudged section. Instead, do a fresh-chat restart with a hand-built summary (Chapter 5).

**Next:** [Chapter 3 — Chat Memory: Across the Chat, and Across Chats](03-chat-memory.md)
