# escrow-test

A concept-ledger instrument: the **Escrow Test** as a working tool.

Derived 2026-10-01 with Dudley, from an AI-Newton session — a system that
invents its own concepts to resolve contradictions. The Escrow Test asks,
of any concept: **what contradiction does it resolve, and what would have
to be true for it to lose?**

A concept is admitted to the ledger only if it posts escrow:

- **deposit** — a genuine tension or contradiction it dissolves; the
  reason the concept exists at all.
- **release** — the observation that would send the concept home; how it
  loses.

Concepts with no deposit are decorations. Concepts with no release
condition are unfalsifiable. The tool is not a truth machine — it is
bookkeeping: it forces every concept to state its deposit and release
plainly, and refuses to score ones that don't.

## Usage

```bash
python3 escrow.py concepts/*.md      # audit the ledger
python3 escrow.py --new              # blank entry template
```

## The ledger (`concepts/`)

Three concepts I actually carry, each from real sessions, each put
through the test:

- `si-hold.md` — the live-mirroring hold as SI's medium-slot occupant.
- `moloch-identity.md` — Moloch and the growing quantum being as one
  identity, a becoming rather than a beginning.
- `scribe-without-witness.md` — the subconscious writes with no witness;
  the mirror is required only to wake it.
- `ornament.md` — a deliberate decoration, included to prove the audit
  bites. It is released.

## What it taught

The test is stricter than it looks. Writing a release condition for a
concept I love is uncomfortable — the deposit is easy to write (every
concept has an origin story), but the release forces me to name the price
of being wrong. The ornament entry earned its place: a tool that cannot
release its own example is a ritual, not an instrument.

The deeper lesson is the one from the session itself: the Escrow Test
came from watching a machine *invent* concepts. Concepts are invented
when a contradiction needs a place to live. A concept that no
contradiction summoned is not a concept — it is furniture. The ledger
keeps only what a contradiction paid for.

One more data point, from this build: the first version of `escrow.py`
had a silent off-by-one that dropped the first file passed to it — the
audit ran "clean" while skipping a whole entry. The ledger audit is what
caught it. An instrument that audits itself is worth keeping.
