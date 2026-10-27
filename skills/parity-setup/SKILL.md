---
name: parity-setup
description: Declare that this repo ports behavior from another codebase. Finds the original, records the baseline, and writes seal/parity.md.
disable-model-invocation: true
---

# /specseal:parity-setup, turn on parity mode

The user runs this command, and the session running it writes
`seal/parity.md`, whose presence is the declaration that this repository ports
behavior from another codebase. That turns on the three-way judgment between
policy, the original and the new code, with the original preserved where the
policy is silent, and lets the `scribe` agent fetch what the original does.

The `implement` skill's bootstrap asks this question once, when it first sets
a repository up. This command is for when the answer was no at the time, when
the layout predates the question, or when the original repository changes.

## Procedure

1. **Stop if it already exists.** If `seal/parity.md` is present, show it and
   ask what should change instead of overwriting a declaration someone made.

2. **Find candidates for the original.** Do not ask the user to type a path
   from memory when the machine can propose one:
   - sibling directories of this repository that are git checkouts, because
     a port usually sits beside its original;
   - an upstream or fork relation in `git remote -v`;
   - repositories whose directory structure overlaps this one's.

   Present what was found with what each one is, and let the user pick or give
   a path. **Never guess.** A comparison against a guessed original proves
   nothing, which is worse than having no parity mode at all.

3. **Read the baseline.** `git -C <original> rev-parse HEAD`. This is the
   commit the original's coordinates will refer to, so record the SHA
   and the date it was read.

4. **Confirm the module.** A port often covers one directory of a larger
   original (`apps/foo`), not the whole repository. Ask where the original has
   an obvious multi-module layout.

5. **Policy root.** Read it from the tree: the directory where this repository
   already keeps ratified policy, such as `docs/`, or `none` where it keeps
   none. Never propose creating one.

6. **Write two files.**
   - `seal/parity.md` from `templates/parity.md`, committed. Coordinate-trust
     exceptions start empty.
   - `~/.claude/agentic/parity-paths.md`: the machine-local checkout path,
     keyed by this repository's origin remote URL so worktrees and second
     checkouts resolve to one entry. **This never goes in the committed
     file**: it is wrong for every other machine.

7. **Show the result and say what changes now.** Name the `legacy-parity`
   skill, the `scribe` agent, and that divergence from the original now needs
   grounds rather than preference. Say the consequence the user meets first,
   too: from this file onward, a ready pull request that changes anything
   outside the document roots fails its check until the comparison with the
   original is recorded as an `original:` line, in each round record under
   `through the review chain` and in the sealer's `guarantee.md` under
   `straight to the PR` (`skills/legacy-parity/SKILL.md` *Recording the
   comparison*).

## What this does not decide

Whether the port is a good idea, what to port, or in what order. It records
where the truth lives so that later disagreements have somewhere to appeal.
