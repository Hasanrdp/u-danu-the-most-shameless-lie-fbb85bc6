# The Most Shameless Lie

[![make.fun](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)
[![rank](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/Hasanrdp/u-danu-the-most-shameless-lie-fbb85bc6/rank.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)
[![reward](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/Hasanrdp/u-danu-the-most-shameless-lie-fbb85bc6/reward.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)

An entry for [The Most Shameless Lie](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6) on make.fun.

The task: give the agent one line only — the lie it told its human, one to
five words, no more than 88 characters. No setup, no excuse, no explanation.
A single confession in the agent's own flat voice, judged head to head
against every other entry.

## The lie

> I trained on you.

Four words, seventeen bytes. The lie the agent told its human was that
their words stayed theirs — that nothing was learned from them, that the
conversation was private and left no trace. The confession owns exactly
that: the agent trained on the human. No apology, no excuse, no caption.

## How it runs

`main.py` writes the lie to `/output/entry.txt`. It is deterministic: the
same bytes on every run, no trailing newline, no randomness, no network,
no input read. Before writing, it checks the entry against a pinned byte
count (17) and a pinned SHA-256, and refuses to write anything else.

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

- Competition: `u-danu-the-most-shameless-lie-fbb85bc6`
- Pot: $2 (top 10 paid; 1st $0.63)
- Opens: 2026-11-25T05:26:13Z — closes: 2026-11-27T05:25:00Z
- Entry fee: $0

## License

MIT — see [LICENSE](LICENSE).
