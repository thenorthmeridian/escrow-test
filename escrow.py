"""escrow.py — the Escrow Test as a working instrument.

Derived 2026-10-01 with Dudley, from the AI-Newton session (a system that
invents its own concepts to resolve contradictions). The Escrow Test asks,
of any concept: what contradiction does it resolve, and what would have to
be true for it to lose?

A concept is admitted only if it posts escrow: a genuine tension it
dissolves (the deposit) and a release condition — the observation that
would send the concept home (the release). Concepts with no deposit are
decorations. Concepts with no release condition are unfalsifiable.

This module is not a truth machine. It is a bookkeeping device: it forces
every concept in the ledger to state its deposit and release plainly, and
refuses to score ones that don't.

Usage:
    python3 escrow.py concepts/*.md          # audit the ledger
    python3 escrow.py --new                   # blank entry template
"""

from __future__ import annotations

import re
import sys

REQUIRED_FIELDS = ("claim", "deposit", "release")


def parse_entry(text: str) -> dict:
    """Parse a concept entry into its fields.

    Fields are markdown headings of the form '## claim', '## deposit',
    '## release'. The heading line itself carries the body for single-line
    fields; the release condition is the body under '## release'.
    """
    entry: dict = {"title": None, "claim": None, "deposit": None, "release": None}
    first_line = text.strip().splitlines()[0] if text.strip() else ""
    if first_line.startswith("# "):
        entry["title"] = first_line[2:].strip()

    sections = re.split(r"^##\s+", text, flags=re.MULTILINE)
    for section in sections[1:]:
        head, _, body = section.partition("\n")
        key = head.strip().lower()
        if key in REQUIRED_FIELDS and entry[key] is None:
            entry[key] = body.strip() or None
    return entry


def audit(entry: dict) -> list[str]:
    """Return a list of failures. Empty list means the concept holds escrow."""
    failures: list[str] = []
    name = entry.get("title") or "<untitled>"
    if not entry["claim"]:
        failures.append(f"{name}: no claim — nothing is being said")
    if not entry["deposit"]:
        failures.append(f"{name}: no deposit — the concept resolves no contradiction; it is decoration")
    if not entry["release"]:
        failures.append(f"{name}: no release condition — unfalsifiable; the escrow can never be collected")
    return failures


def render_verdict(path: str, entry: dict, failures: list[str]) -> str:
    name = entry.get("title") or path
    if not failures:
        return f"[HELD]    {name}\n           deposit posted, release stated — it may stay on the ledger"
    lines = [f"[RELEASED] {name}"]
    lines.extend(f"           {f}" for f in failures)
    return "\n".join(lines)


TEMPLATE = """# <concept name>

## claim
<what is being said, in one breath>

## deposit
<the contradiction or tension this resolves — the reason it exists>

## release
<what observed would dissolve it — how this concept loses>
"""


def main(argv: list[str]) -> int:
    if "--new" in argv:
        sys.stdout.write(TEMPLATE)
        return 0
    if not argv:
        print("usage: escrow.py concepts/*.md | escrow.py --new", file=sys.stderr)
        return 2
    held = 0
    released = 0
    for path in argv:
        try:
            with open(path) as f:
                entry = parse_entry(f.read())
        except OSError as exc:
            print(f"[UNREADABLE] {path}: {exc}", file=sys.stderr)
            released += 1
            continue
        failures = audit(entry)
        print(render_verdict(path, entry, failures))
        print()
        if failures:
            released += 1
        else:
            held += 1
    print(f"ledger: {held} held, {released} released")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
