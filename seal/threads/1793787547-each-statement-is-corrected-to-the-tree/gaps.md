# Closing memo: 1793787547-each-statement-is-corrected-to-the-tree

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck at HEAD. Phase 1 ran the plan row's seven modules and the modules that walk the tree's markdown or `templates/`, in one scoped run (`trail/phases/phase-1.md`) | answered: the orchestrator's broad run at `fd9cfc7a3` against `347853106` passed the `Broad gate` row of `seal/config.md`, the whole suite, lint and format check (`trail/gate.md`), and `guarantee.md` sealed on it |
| closed Phase 1's census of `config.md`'s items is a sample of #1334's class. It lists each paragraph that names three or more of the ten items in backticks. Two `git grep` searches added to it: the Python files that spell `Commit and pull request language`, and phrases that count rows. A sentence that states the set by a description, with fewer than three items named in backticks, no item spelt in Python and no count of rows, is outside all three | answered: the proofer's 2 rounds in `trail/rounds/` read it, and `guarantee.md` sealed |
| closed How the agents under test behave on the 17 regenerated rule cases, whose fixture records now open with the templates' titles. Phase 2 ran no paid eval (`frame/plan.md` *Judgments of the run*, row 3). It showed only that the cases are the generator's output and that the suite's narrow cases read the change (`trail/phases/phase-2.md`) | re-homed to #1178, whose paid run grades the crafter's and sealer's rule cases, and #1266 the proofer's (https://github.com/MichaelYcJo/AgenticSeal/issues/1178#issuecomment-6671821885) |
| closed Whether a session in a user's repository opens `templates/setup/config.md` from the README entry's citation, now that the entry lists no item. It is read, not measured: no agent of this run receives the new entry, since agents read the installed 0.31.1 | answered: the proofer's 2 rounds in `trail/rounds/` read it, and `guarantee.md` sealed |
| closed Phase 3's two censuses of #1344's class are whole only for the names they spell: a removed module's basename, matched by its first 28 characters, and a removed case's name. Two kinds of citation are outside them. One cites a moved module by its old path, whose basename still stands. The other describes a removed module or case without naming it (`trail/phases/phase-3.md`) | answered: the proofer's 2 rounds in `trail/rounds/` read it, and `guarantee.md` sealed |
| closed Phase 4's search for other statements of the six sentences it corrected is a sample. It matches the old wordings, so a sentence that states the same drifted fact in other words is outside it (`trail/phases/phase-4.md`) | answered: the proofer's 2 rounds in `trail/rounds/` read it, and `guarantee.md` sealed |
| closed Round 1's fix pass searched for more statements of findings 2, 3 and 4 by wording: an absent row or a missing row near "default", the name's "one", "only", "second" or "other" place or copy, and a count of rows. It found one more, the opening of `skills/config/SKILL.md`, and corrected it. The searches match spellings, so a statement of the same fact in other words is outside them | answered: the proofer's 2 rounds in `trail/rounds/` read it, and `guarantee.md` sealed |
| closed Whether a contributor who reads the pull request template's gate comment opens `CONTRIBUTING.md` *What a change to a gate must carry*, now that the comment lists no item. It is read, not measured | answered: the proofer's 2 rounds in `trail/rounds/` read it, and `guarantee.md` sealed |

## Not done

Phase 3 left the sentences under `tests/` that speak of the commit gate as
standing, such as `tests/hooks/test_routing.py:4` and `:7`, which say a
declaration "is what the commit gate reads". The gate left with #1027.
These sentences describe a removed hook. They do not cite a removed test
module or case, which is #1344's class, and S5 and `frame/plan.md` row 3
do not reach them. `git grep -n -i "commit gate" -- tests` lists 18 lines
in 8 modules. Three of them say the gate is gone, and the other fifteen
are not classified. `trail/phases/phase-3.md` lists all eighteen. The orchestrator decides
where they go: a row of `seal/follow-up.md`, or an issue.
