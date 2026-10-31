# Tokens: How AI Reads Your Words

---

You know how you read by words? AI doesn't. AI reads in **tokens** — and this one quirk explains a surprising number of "why did it do *that?*" moments.

## What's a token, actually?

A token is a chunk of text — usually a chunk of a word, sometimes a whole word, sometimes punctuation, sometimes a single weird character. The AI was trained by breaking enormous amounts of text into these chunks, so it thinks in them.

Rough rules of thumb (they vary by model, and that's fine):

| Text | Rough tokens |
| --- | --- |
| "the", "a", "cat" | ~1 token each |
| "hello!" | ~2 tokens (word + punctuation) |
| "contradictory" | ~3-4 tokens |
| A RFKJx7 serial number | can be many tokens |
| 100 words of English | ~75-130 tokens |
| One page of a book | ~300-600 tokens |

That last row is the handy one: **100 words ≈ 100-ish tokens, give or take.** You never need exact numbers for daily use — you need the *feel* for size.

## Why should you care? Three real reasons.

### Reason 1: Tokens are the unit of the AI's attention

Everything in a chat — your messages, the AI's replies, pasted documents — is made of tokens, and every one of those tokens sits in the AI's working memory. When the container gets full (Chapter 2), what gets squeezed out gets *forgotten*. Long pasted documents? That's tokens.

### Reason 2: Weird characters make AI spend weird attention

Have you ever pasted a serial number, a URL, a chunk of code, or a table of numbers and watched the AI stumble? Those tend to tokenize poorly — turning into many small tokens — which makes them eat more of the window *and* be harder for the model to reason about. Same text, wildly different token cost:

- `Hello, I need help with my project` — about 8 tokens
- `x7F-99aB-Qd3!` — could be 10+ tokens, and harder to "read"

### Reason 3: "Long" is a feeling, tokens make it measurable-ish

When a chat *feels* long, check your token estimate: your messages, the AI's messages, and any docs — add the word counts, divide by roughly 0.75 for tokens (or just call 150 words ≈ 200 tokens and stop there). If you're guessing at tens of thousands, it's time for a fresh chat with a summary. That's chapters 4 and 5.

## The counterintuitive part: shorter chats often beat detailed ones

Beginners think the winning move is to stuff every fact into the chat. What actually happens: the model's attention gets spread across a mountain of text, old instructions blur, and answers get generic.

The fix isn't more detail — it's *relevant* detail, kept current. Which is exactly what Chapters 5 and 6 practice.

## Try this

1. Ask your AI: **"How many tokens do you estimate this conversation has used so far? Are we deep into the context window?"** The number will be an estimate — models can't count their own tokens exactly — but the *answer* tells you something about how the model sees your chat.
2. Take a paragraph from this book (that's ~100 words), then take a 100-word chunk of your own dense notes or a contract. Ask the AI to summarize both. Notice how the dense text takes noticeably more effort — that's tokens at work.
3. Next time a pasted document confuses the model, try asking it: **"Quote the part you found ambiguous."** Often the problem isn't the content — it's which tokens got the model's attention.

## One last thing

Do **not** worry about counting tokens precisely. Tools exist for that (see the related `token-budget-calculator-cli` project if you ever want a calculator), and Chapter 8's memory settings matter more. What you need is the *instinct*: **words are cheap, weird characters are expensive, documents are the real spend, and tired old chats are the most expensive thing of all.**

**Next:** [Chapter 2 — The Context Window: The AI's Working Memory](02-context-windows.md)
