# Why Answers Drift

---

This is the chapter for the moment every long-session AI user knows:

You started strong — the AI got you, it had your details, it was sharp. Then, gradually, the answers got *off*. Not wrong exactly. Generic. Or it forgot a rule you set. Or it started blending an old topic into the new one. Or it made a confident suggestion for a problem that isn't yours.

That's **drift**. And here's the reassuring part: it's not your fault, and it's not the AI "getting dumber." It's predictable behavior with predictable causes. Once you see the causes, most drift is easy to prevent or fix.

## The five causes of drift

### 1. Attention, spread thin

An AI doesn't read its whiteboard like a person reads — it *weights* every token's relevance to the current question. The more text in the window (and the more of it that's old or off-topic), the more diluted the attention on what matters. Your carefully-worded instruction from message 2 is competing with 40 messages of chatter.

### 2. The recency/primacy squeeze

Attention is strongest at the **top** (start) of the window and the **bottom** (most recent messages), weakest in the **middle**. Your ongoing task may live entirely in the mushy middle. This is why the Chapter 5 "top of the chat" context header is such a cheat code — it sits where attention is strongest.

### 3. Old goals quietly overrule new ones

This is the sneakiest one. If your early chat was about *starting* a project, and you've since pivoted to *finishing* it, the AI's "inner goal" from the early messages keeps tugging its answers back toward starting-mode. This is why it keeps suggesting beginner steps when you need finisher steps.

### 4. Compaction roulette

When a tool auto-compresses early messages (Chapter 3), the summary keeps what *seemed* generically important — not what *you* consider important. Your constraint ("no jargon") may have looked trivially minor to the compactor and vanished. Summaries preserve the *gist*, not your specifics.

### 5. Accumulated noise

Small misunderstandings left uncorrected — the AI assumed "Friday" meant this week, you didn't correct it, three messages reference the wrong Friday, and now the whole session is quietly off-book. Drift compounds like a slight crooked frame on a road trip: miles of small wrongness.

## How to notice drift early

Drift gives off signals before it wrecks a session:

- **Rules you set fade.** Formatting, tone, or length preferences stop being followed.
- **Answers get shorter and vaguer.** The AI leans on general knowledge instead of the specifics it was given.
- **It stops asking questions.** A fresh, engaged AI asks clarifying questions; a drift-y one pretends it already knows.
- **It mixes contexts.** Your work project bleeds into your weekend project — wrong tool, wrong chapter, wrong deadline.
- **You feel it.** The vague "why is this suddenly work?" feeling is data. Trust it.

## The fix, in escalating order

Work up the ladder; most drifts die at step 2.

1. **Re-anchor.** "Quick reset — re-read my context header. We're focused on [X]. Confirm your understanding, then continue." (Chapter 5's re-anchor move.)
2. **Restate the instruction beside the current task.** Don't say it *referring back*; say it fresh in the same message as the current request. Fresh instructions get fresh attention.
3. **Summarize and checkpoint.** "Summarize what we've agreed on so far in bullets." Read it. Errors reveal the smudges — and your corrected version becomes the new reference point. Paste it back in: "Corrected version — use THIS as our reference."
4. **Start fresh with a handoff note** (Chapter 4's closing ritual). For anything that matters and has drifted long — this one is the honest answer.

## The prevention habit (the actual takeaway)

The pros prevent drift by *chat hygiene* rather than rescue:

- One chat = one purpose. New topic, new chat.
- Big pastes get cut to the needed section (Chapter 6).
- Critical rules live at the top of every chat (context header), not at message 30.
- Sessions get checkpoints ("recap") every dozen or so messages, so the AI re-reads its own state.
- Chats *end on purpose* with a handoff note, not by abandonment.

That's five habits, not five hundred. Chapters 4, 5, and 6 already taught all five.

## Try this

1. Diagnose an old chat. Open your longest, most confusing thread and find which of the five causes matches: attention spread, mid-window squeeze, old-goal tug, compaction, or noise. Naming it is weirdly satisfying.
2. Run a mid-drift rescue using step 3's prompt on your most painful current session. Watch how just "recap, correct, re-paste" fixes the fog.
3. Recruit a checkpoint habit: put a coda at the end of long sessions — "Before we close: 5-bullet handoff note." (If you're going to do ONE thing from this manual, it's this.)

**Next:** [Chapter 8 — Memory Settings, Decoded](08-memory-settings.md)
