# Implementation Plan: 1795841830-find-leftovers-before-a-round

## Technical context

The tree as read at `bbb66b38`.

The work rewrites rule text and adds no code. The texts it changes, with their lines at that commit, are `frame/design.md` *Grounding* G3 and G9 to G13: `agents/framer.md` lines 32, 115, 170 to 187 and 250; `agents/crafter.md` lines 19 to 28 and 58 to 60; `skills/verify/SKILL.md` lines 50 to 66, 144 and 197; `skills/implement/SKILL.md` lines 203, 280 and the table of *3. The SDD file set*; `skills/implement/fix-pass.md` lines 95 to 97; `skills/implement/fold-and-reframe.md` lines 22 and 30; `skills/implement/orchestration.md` line 214 and *Under agentic*; and `agentory/follow-up.md`'s table. `agents/framer.md` and `agents/crafter.md` are preloaded by every spawn of their agent, so neither carries a check line (`skills/settle/rule-changes.md` *A rule has one shape*).

**The approach.** The keep file's rule has one home, `skills/verify/SKILL.md` *An absence claim is only as good as the search behind it*, because the framer's search rule already sends its reader there and the builder reads that skill at every phase boundary. `agents/framer.md`, `agents/crafter.md` and `skills/implement/SKILL.md` cite it. The form is the one #1658's work item ran by hand (G4), with the two flags G7 found and the path search G8 found. The suites' commands stand in the plan's *Verified by* cells, which the framer already writes, and the *Phase boundary* row runs its set under them. The split is a paragraph of *Under agentic* that weighs costs.

**Failure scenario, six months out.** A framer writes a keep file of a thousand lines for a rename. Each kept line is judged once, by the framer writing it and by the round reading the frame's commit, and that read is the cost the keep file moves from later rounds to the first. The failure is a rename whose phases rewrap paragraphs: each rewrap changes a kept line, so the builder rewrites keep lines in every phase and the phase record lists them. Where that list grows past what a round reads well, the repair is a keep file that holds fewer lines, by renaming more of them, and not a looser account. A second failure is a repository whose suites no document names: the framer cannot find a built-app suite, the cell omits it, and Scope item 8's rule has the crafter run the file under its suite and name the gap.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A keep file per phase, compared by `git grep`, `sort` and `diff`, with its rule in `skills/verify/SKILL.md` | a phase that rewraps many kept lines rewrites many keep lines, each named in its phase record (*Technical context*) | chosen |
| Keep the three accounts of G3, the structure in place | a named file or an exclusion hides every other line it covers: #1659 records leftovers found in batches in rounds 1, 2 and 5 of Owlery #322, and 19 lines matched E1 at the end of #1658's phase 1 (the issue, `read`); G6 shows the line the account would hide. The premise that would keep it, that a kept file holds no other line of the old name, is what G6 shows false | rejected |
| One keep file for every phase, with each phase's expected diff written beside it | `diff`'s hunk headers move with every kept line a phase adds, so each expected diff is rewritten at every phase (G4, #1658's *Alternatives considered*) | rejected |
| Name the last phase's keep file `frame/keep.txt` and the others `frame/keep-<N>.txt`, as #1658 did | two names for one form; the phase a file belongs to is read from its name only where every file carries the number | rejected; every keep file is `frame/keep-<N>.txt` |
| The keep file for a rename's search alone, other searches keeping the account of G3 | the hole is in the account and not in the rename: a search for a removed sentence that keeps a line in a named file hides the next line of that file the same way. One rule with two accounts asks the reader which one applies | rejected; every search that keeps a line has a keep file, and a search that keeps none has none |
| Copy the census into `plan.md` | a keep file reaches 219,331 bytes (G5), past `Document token ceiling`, and every party that opens the plan pays for it | rejected |
| A script or a gate that reads the keep file at the pull request | a new mechanism with no catch on record, where `git grep` and `diff` already answer exactly; the owner's decision names no script (#1659 point 1) | rejected |
| Only the framer edits a keep file, and every changed kept line is folded | each rewrap of a kept line costs a framer spawn before the next phase; #1658's frame let the builder write them (G4) | rejected; the builder follows the kept kinds and adds none |
| Leave paths out of the keep file's rule | a renamed name that stands in a file's path is a leftover `git grep` never prints; #1658's frame searched paths with a second command (G8) | rejected; `frame/keep-<N>-paths.txt` where a path holds the old spelling |
| Name the suites in a configuration key | the plan's *Verified by* cell already names the checks a phase is verified by (#1659 point 2) | rejected |
| Have the *Phase boundary* row run every suite of the repository | every phase pays for a built-app suite whose files it did not change; the broad gate is the run of everything, once (`skills/verify/SKILL.md` *Scope: cheap and often, broad and once*) | rejected |
| Split every issue whose parts differ in kind | each extra work item costs a broad run, an inspection and a pull request, which a small part does not repay (#1659 point 3) | rejected; *Under agentic* weighs it |
| A `routing.md` row that records a split | a new row is a form `lib/routing.py` reads; the split's grounds are prose that *Why this way* already holds | rejected |
| A new eval case for the framer's keep file | each run costs an agent session, and the suite is a smoke run that no edit owes (`evals/README.md`) | rejected |
| Three phases, one per point | a third crafter spawn reads the whole frame again to write one paragraph of *Under agentic* | rejected; two phases |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope items 1 to 5 | `bin/test tests/text tests/behaviour <each other test file that opens a file the phase changed> -q` passes, each other file named in the phase record; `S1` and `S2` of `frame/design.md` *Data & interfaces* *The searches* print nothing. The eval harness owns no file of the set (G12) | 787a5158 |
| 2 | Scope items 6 to 11 | `bin/test tests/text tests/behaviour <each other test file that opens a file the phase changed> -q` passes, each other file named in the phase record; `S3` of `frame/design.md` *Data & interfaces* *The searches* prints nothing. The eval harness owns no file of the set (G12) | |

## Overlap with the release

The spawn named #1650 and #1655 as the release's other work items. Neither had a frame committed when this frame was read on 2026-11-28; each was read from its issue and from the `routing.md` its routing commit holds, `24c5276f` for #1650 and `3729b409` for #1655.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1650, `1795841829-skill-descriptions` | `skills/verify/SKILL.md` and `skills/implement/SKILL.md`: #1650 their frontmatter `description`, this work their bodies (Scope items 1, 4, 6 and 8). Neither reads a rule or a check the other changes | #1650 | #1650's diff is the smaller and the likelier to be cleared first; the hunks stand apart, so the later merge takes the base with no conflict, and this work's rounds read the merged tree anyway |

#1655 does not meet this work: its issue names `.github/scripts/publish_release_note.py`, `docs/releasing/release-checklist.md` and `skills/settle/SKILL.md`, and its routing names `docs/releasing/branch-and-release.md`, none of which this work changes. Its change reads a release whose range added no fragment, and this work adds a fragment. Where another item of the release also adds a row to `agentory/follow-up.md`'s table, the later merge keeps both rows.

## Operational impact

No migration, no new environment variable and no new dependency. A frame written after the release that carries this work accounts for a kept line by a keep file, and a frame committed before it keeps the account it was written with. A repository's framer names its suites' commands in each *Verified by* cell. This work item does not carry the release's version move: this plan orders it after #1650, and `skills/implement/merge-order.md` gives the move to an item no plan orders after another. At `bbb66b38`, `.claude-plugin/plugin.json` reads `0.40.1` (G23).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
