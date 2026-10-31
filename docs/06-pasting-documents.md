# Pasting Documents: The Smart Way

---

At some point every AI user faces it: "I need the AI to actually read this file." A contract. A syllabus. A 12-page PDF. Your own meeting notes.

Pasting is the honest way to do it in most chat tools, and when done well it's *powerful* — the difference between the AI answering in generalities and the AI answering about *your* stuff. Done badly, it drowns the whiteboard and makes everything worse. Here's the smart way.

## The golden rule: paste with a purpose

Every paste should come with an **on-ramp message** that tells the AI what the document is and what you want done with it. The worst paste in the world is a document with no instructions — the AI guesses why you sent it, and its guess sets the tone for the whole session.

Bad:

```
[pastes 8 pages of meeting notes]
```

Good:

```
Below are my meeting notes from Tuesday. I need two things:
1. A bullet list of every deadline mentioned.
2. Which deadline is tightest and why. 

Notes:
---
[the notes]
---
```

Same document. Vastly better answer, because attention gets pointed, not just fed.

## Feed in the right format

When a tool accepts a file upload, use it — parsed text beats pasted text. When pasting, help the AI see *structure*:

- **Keep headings and bullets** from the original — they're the AI's map.
- **Tables are fine** — AI handles pasted tables well.
- **PDFs pasted as text can arrive garbled** (columns scrambled, page numbers interleaved). If you see gibberish in chat, that's a paste artifact, not an AI fault — try re-copying from the PDF viewer's text selection, or reflowing through a text editor first.
- **Strip the junk when you can**: repeating navigational boilerplate, headers/footers repeated per page, signature blocks. They cost tokens and distract.

## Segment before the AI drowns

The full 60-page PDF is usually *not* the thing you need read. Segment:

1. **Cut to the relevant section.** For a contract question about payment, paste the payment clause and its neighbors, not all 60 pages.
2. **If you can't cut, direct the AI where to look**: "The contract is below. Focus ONLY on the parts dealing with refunds."
3. **Multiple documents?** Label each:

```
DOCUMENT 1 — my current listing description:
---
[the text]
---

DOCUMENT 2 — the competitor's listing:
---
[the text]
---

Task: list what Document 2 does that Document 1 doesn't.
```

4. **Huge and unavoidable?** Use a two-step: first send the doc and ask the AI to summarize it into a working overview. Then start a *fresh chat* with the compact overview plus your real task. (This is the Chapter 5 pattern — it works for documents as well as conversations.)

## Documents age badly in long chats

A subtle trap: pasting a document *early* in a long session means by message 40 of tweak, iterate, rework — the doc is 30 messages of whiteboard ago, fading from the AI's attention right when precision matters most. Two moves:

- **Re-show the relevant chunk** when deep into iteration: "Here's the section again for reference: — [paragraph]."
- Or start fresh with a summary + just the relevant excerpt (Chapter 4), which is cleaner still.

## Privacy is a token question too

Anything pasted is potential cross-chat memory, training data (depending on that tool's settings — most major tools let you opt out), or exposure if the account is shared. The friendly rule:

- **Strip personal identifiers before pasting wherever you can.** "My client" not the client's name; "[redacted]" not the bank account.
- **Check your tool's data settings** (Chapter 8). Most let you prevent inputs being used for training.
- **Sensitive docs (medical, legal, financial) for real-world decisions**: use AI to understand *structure and terms*, but never paste in liftable private data to get an answer you'd then act on without a professional. Fun fact: this is an educational guide by a nurse, not a lawyer — same discipline applies to me to you.

## Try this

1. Take a document you've actually pasted lately. Write (for yourself) the one-sentence purpose: *what would I want the AI to do with this?* Now write the full on-ramp message and paste it with purpose.
2. Take a long doc and paste only the specific ~2 relevant pages + a crisp question. Ask: "Quote the evidence you used." Now tell whether it found the *right* paragraph — then compare that against your memory of the full-doc answer.
3. If your tool has file upload or a document library feature — use it next time instead of a paste; watch how structure survives better.

**Next:** [Chapter 7 — Why Answers Drift](07-why-answers-drift.md)
