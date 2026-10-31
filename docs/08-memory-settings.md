# Memory Settings, Decoded

---

Every major AI assistant has memory-ish settings, and each one names them something different and hides them in a different place. This chapter is the decoder ring. Menus move constantly, so this is organized by **concept first, tool second** — when the buttons change (they will), the concepts will still find them.

## The universal settings

Almost every assistant with cross-chat memory has some version of these four knobs:

### 1. Saved Memory / Personalization

**What it does:** The tool stores small facts about you ("works in healthcare," "prefers plain English," "runs an eBay store") and injects them into future chats.

**Where:** Usually under Settings → Personalization / Memory.

**How it's used:** You usually say "remember that…" in chat, or the tool auto-records from conversation. You can almost always **view the list and delete items** — go look at it once a month; auto-memory records things you didn't realize were "facts."

**Best for:** durable identity-level facts. Worst for: project details (they pollute other chats).

### 2. Custom Instructions / Profile

**What it does:** A standing "about me" block applied to *every* chat — tone, role, format wants.

**Where:** Settings → Personalization → Custom Instructions / Profile.

**Best practice:** General prefs only. "Plain English, no emoji, be direct, assume I'm a beginner until I say otherwise." Project context lives in your per-chat context header (Chapter 5), not here.

### 3. Training/data controls

**What it does:** Whether your chats are used for model training and how long they're retained.

**Where:** Settings → Data Controls / Privacy.

**The friendly read:** If the "improve the model for everyone" toggle bothers you, find it and flip it — you lose nothing you'd notice. Knowing this exists is the whole point.

### 4. Chat history retention

**What it does:** How long old chats are kept; some tools offer auto-delete after 30 days or manual-only.

**Where:** Settings → Data Controls → Retention.

**The friendly read:** Auto-delete is fine for casual use, but if you rely on reopening old chats for reference (many of us do), set retention thoughtfully — deleting work archives can sting more than a privacy slider feels good.

## Tool-by-tool quick map

> A note on maps: **names and locations below are a snapshot in time — menus get renamed and shipped around constantly.** When a tool contradicts this table, trust the tool. Navigate by names you now recognize from the universal settings above — that's the decoder-ring skill.

| Tool | Memory feature lives under… | Tips |
| --- | --- | --- |
| **ChatGPT** | Settings → Personalization → Memory; "Manage memories" lists facts | Custom Instructions is a separate slot; "Temporary chat" runs memory-free |
| **Claude** | Settings → (Profile/Privacy area); "Projects" give per-project memory instead of global | Projects are the professional's best friend: knowledge base + instructions scoped per project |
| **Gemini** | Settings/apps area; "Saved info" for memories | Tied to your Google account; Saved info items are individually editable |
| **Copilot (Microsoft)** | Tied to Microsoft account personalization controls | Enterprise versions differ sharply from consumer ones — check which you're on |
| **Local AI (Ollama, LM Studio, etc.)** | Usually none by default — every chat starts blank | That's a feature: *you* control all context; pair with Chapter 5's header technique always |

Local AI folks: no auto-memory means the discipline of summarizing is *even more* valuable — your context header is the only memory that exists.

## Three habits worth stealing

1. **Monthly memory audit.** View the saved-memories list. Delete anything stale or wrong ("I moved apartments in 2024" embarrassing no one needs).
2. **Separate identity from project.** Identity facts and tone rules → profile/custom instructions. Project state → context header per chat. Crossing these wires is why your grocery-list chat suddenly knows your quarterly revenue.
3. **Know your fresh-chat behavior.** Some tools show "memories applied" indicators or let you start memory-free chats. If you're ever working with private material, a memory-free or temporary chat is a kindness to your future self.

## A word on shared devices

If anyone else touches your computer or account: chat history is account history. The memory list contains your facts. Chapter 6's privacy discipline (strip identifiers, redact where you can) pairs with this. It's your AI; make it a good housemate.

## Try this

1. Do the audit right now: open your main tool, find the memory list, and read it out loud (seriously — reading aloud reveals what's stale faster than scanning).
2. Write your custom instructions block from today, not from memory of what you set up months ago. Plain English. Five lines max.
3. If your tool has Projects (Claude) or equivalent: think about your busiest recurring task and whether scoping it to its own project would keep its context out of your daily chatter.

---

**That's the manual.** Now the extras: [the worksheet](worksheet.md) to audit your own habits, [the checklist](checklist.md) for when chats feel off, and [the glossary](glossary.md) for the terms everyone else pretends you already know.
