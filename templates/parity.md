# Migration config

This file's presence is the declaration: **this repository ports behaviour
from another codebase.** It turns on the three-way judgment of policy,
original and new, and lets the scribe fetch what the original actually does.
Deleting it makes the project greenfield again.

Machine-local checkout paths never belong here: they differ per machine and
would be wrong for everyone else. They live in
`~/.claude/agentic/parity-paths.md`, keyed by this repo's origin remote URL.

| Field | Value |
|---|---|
| Original repo | `<org/repo>`, module `<path within it, or "whole repo">` |
| Baseline commit | `<SHA>`, the commit the original's coordinates refer to |
| Policy root | `<the directory the repository keeps its ratified policy in, such as docs/, or none>` |
| Coordinate-trust exceptions | none |

## Coordinate-trust exceptions

Paths whose recorded coordinates need re-verification before they can be
trusted, and why. Empty is the normal state; a row arrives when someone finds
a coordinate that moved without anybody noticing.

| Path | Why it needs re-verification | Noticed |
|---|---|---|
| | | |

## Scope notes

What this migration does and does not cover, when that is not obvious from the
original repo alone. For example: endpoints being ported in a later phase, or
behaviour deliberately left behind with the decision recorded under the policy
root.
