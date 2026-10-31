# Chat Memory: Across the Chat, and Across Chats

---

"Memory" gets thrown around a lot with AI, and it means two completely different things. Knowing which one you're talking about is half the battle.

## Memory #1: Inside one chat — the whiteboard

Within a single chat, the AI remembers everything on the whiteboard (Chapter 2). This memory is:

- **Immediate** — anything you say is "known" for the rest of that chat.
- **Fragile at the edges** — the oldest stuff is the first to smudge as the window fills.
- **Weaker than it feels.** The AI doesn't weight every old message the way you'd hope. The most recent messages and anything you've emphasized get the most attention.

So "remember what I said about the deadline" works *great* at message 5 and progressively worse at message 80.

## Memory #2: Across chats — separate rooms

Start a new chat and you get a clean whiteboard in a new room. **It does not know what happened in the last chat.** This is the single most common beginner confusion — people say "but I told it that yesterday!" across sessions and feel betrayed.

Modern assistants bolt on some cross-chat memory with varying levels of ambition:

| Memory type | How it behaves | Typical example |
| --- | --- | --- |
| **Saved/memories** | Small facts pinned across chats ("user is an eBay reseller") | "Remember that I go by Dylan" |
| **Auto-memory / recap on new chats** | Tool summarizes old conversations and hands the summary to new chats | You open a new chat and it nods like a coworker |
| **Provider-level sync (account settings)** | Profile, plans, custom instructions applied everywhere | Tone, role, standing preferences |
| **Everything else** | Gone with the chat | Your project details unless you carry them |

These differ **per tool**, wildly — Chapter 8 is the decoder ring. What's universal:

- Cross-chat memory, when it exists, is *summaries and facts*, not full transcripts.
- You can usually inspect what's been saved (and be surprised — sometimes the tool remembers things you'd rather it hadn't; you can typically view and delete items).
- The *work* memory — the decisions, files, half-formed ideas of your project — never travels automatically. That's yours to carry, and Chapter 5 shows the carry technique.

## The mental model that makes this click

Think of your AI sessions like **working with a smart temp agency**:

- Inside a shift (one chat), your temp is sharp and remembers everything on the job sheet.
- The agency has a *profile* on you (cross-chat memory): "prefers concise answers, works nights, junior developer."
- But the temp from Tuesday doesn't know what happened at Monday's shift — you have to hand over a briefing sheet.

The whole reason briefing sheets exist. Chapter 5 is yours.

## What about "compaction"?

Some tools, when a chat gets long, compress early turns into an internal running summary — sometimes shown as a "compacted" or "summarized" state. That's the tool doing exactly the Chapter 5 move automatically, and it's *better than smudging* — but it has a cost: **you didn't choose what got kept.** The summary might omit the detail you thought was vital. Hand-built summaries beat auto-compaction for anything that matters.

## A theater of failure (and the fix)

Common story, gentlest possible version:

1. Monday: long, productive chat about a project. Ends happily.
2. Wednesday: opens *new* chat. Types, "as we discussed…" Confusion.
3. Reopens *old* chat. Asks new question there. The old chat is now 200 messages of half-dragged-in context, and answers start drifting.
4. Eventually gives up and re-explains everything. Again.

The fix at step 2 (and its echo at step 3) is one habit: **fresh chat + hand-carried summary**. That's Chapters 4 and 5, and it's the skill this whole manual exists to teach.

## Try this

1. In your favorite assistant's account settings, find the section called **Memory**, **Personalization**, or **Data controls**. Read the *list* of what's saved about you. Proceed with mild curiosity — and note the delete button while you're there. The full tour is Chapter 8.
2. In a brand-new chat, ask: **"What do you already know about me and my work?"** Whatever it says is the union of cross-chat memory + profile. Everything else is what *you* carry.
3. Pick your most confusing current long chat. Ask the AI to summarize your project in 10 bullets — then check the summary against reality. Mismatches are exactly where your whiteboard has smudged.

**Next:** [Chapter 4 — When to Start a Fresh Chat](04-when-to-start-fresh.md)
