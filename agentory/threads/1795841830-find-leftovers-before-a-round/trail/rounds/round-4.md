# Review round 4: 1795841830-find-leftovers-before-a-round

```iadd
target: 274b7d02, fixes f2a0b1a8..274b7d02
```

Round 4 is a verifying round over the diff of the fixes, `f2a0b1a8..274b7d02`, and the run's last, by the last row of `frame/plan.md` *Judgments of the run*. That diff holds the framer's fold `79c7a589`, the fix pass's commits `999f9e8a`, `83fa871c`, `67ae818c` and `a966a8c1`, and the close blocks of `274b7d02`. The range holds no merge of the base (`git log --merges --oneline f2a0b1a8..274b7d02` printed nothing, `executed`), and `origin/release/v0.41.0` is an ancestor of the target (`git merge-base --is-ancestor`, exit 0, `executed`). Every coordinate below was opened at the target in a `git clone --no-local` under the round's scratch directory.

Stage 1 read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`, `trail/phases/phase-2.md` and `trail/rounds/round-3.md` whole at the target, and `trail/rounds/round-1.md` and `trail/rounds/round-2.md` for their coordinates. `Record language` and `Commit and pull request language` are both English (`agentory/config.json`, `read`), so no `pr.<lang>.md` is owed and none stands. The range changes no `routing.md`, `frame/questions.md`, `gaps.md`, `changelog.md` or `pr.md` (`git diff --stat`, `executed`). `agentory/threads/` holds this work item alone (`ls`, `executed`), so no other work item's frame is read against it.

Facts carried and not re-established: round 1's run of `tests/skills/test_range_read.py` and `tests/lib/test_optin.py` for the Python files and phase 2's red run of the keep file case, since the range changes no Python file (`git diff --stat f2a0b1a8..274b7d02`, `executed`). Round 1's probe of `## Rule changes` was written again from its `## Probes` row and run at the target, not carried, since the fold changed three `to:` lines. Round 3's two searches were run again at the target. Each verdict below is this round's own.

The fix pass's account was read as a claim. `83fa871c`'s message says "at that phase's close" are "the words every other statement of the fact uses". `changelog.md:3` states the fact without them, and `skills/implement/SKILL.md:354` reads "prints at that phase's close" (`read`). A commit message is history, so the round opens nothing for it. The finding below is where the records state the same claim. The close of round-3#1 says its set printed `1341 passed` at `a966a8c1`. This round did not run that set again; it ran the narrow probe in `## Probes`.

## Findings

### 1. The fold's chosen row says each sentence on what a keep file holds takes the home's words or cites the home, while the decision it records keeps sentences in their own words

```iadd
severity: should
location: `agentory/threads/1795841830-find-leftovers-before-a-round/frame/plan.md:33`
evidence: read `agentory/threads/1795841830-find-leftovers-before-a-round/frame/plan.md:33`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/plan.md:73`, `skills/verify/SKILL.md:72-76`, `skills/implement/SKILL.md:354`, `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md:42`, `agentory/threads/1795841830-find-leftovers-before-a-round/changelog.md:3`; executed `git grep -n -F "is to print at that phase's close" -- . ':!agentory/threads/1795841830-find-leftovers-before-a-round/trail'` and `git grep -n -i -e "at that phase's close" -e "at the phase's close" -- . ':!agentory/threads/1795841830-find-leftovers-before-a-round/trail'`
regression: round-3#2
```

Why it matters: the unit is the row of `frame/plan.md` *Alternatives considered* that the fold `79c7a589` added at line 33. Its verdict is "chosen, by the fold of round 3", and its approach reads: "A sentence that says which lines a keep file holds states the home's fact in the home's words, "is to print at that phase's close", or cites the home". The orchestrator's row at line 73 decides less than that. A sentence in its own words, "an index cell or a README line among them, stays where it states the same fact". Only the README line and the `## Rule changes` `to:` lines are brought to the home's words. The fold wrote that decision as a rule over every such sentence. So the defect came from how the fold worded the decision, and not from the decision or the frame.

The target contradicts the row. Three statements of what a keep file holds neither use the quoted words nor cite the home for the fact:

- `skills/implement/SKILL.md:354`, the *Holds* cell of the file set's row, reads "the search of phase `<N>` prints at that phase's close". Row 73 keeps it, and the close of round-3#1 says so.
- `frame/design.md:42`, *Scope* item 4, reads "holding the lines the search of phase `<N>` prints at that phase's close". The close of round-3#2 keeps it.
- `changelog.md:3` reads "holds each one, a line a later phase changes or removes among them", with neither phrase.

The first search on the `evidence:` line searches for the quoted phrase. It prints `agentory/README.md:95`, `templates/setup/agentory-README.md:95`, and lines of `frame/design.md` and `frame/plan.md`. It does not print the home, since `skills/verify/SKILL.md:73-74` wraps the phrase after "is to print". It does not print `:354`, which reads "prints". The second search, on "at that phase's close", prints the home at `:74` and `:354` as well. `a966a8c1`'s message, "so a git grep on the home's words finds the home", holds for those words and not for the phrase the row quotes. The searches are samples under contract rules 12 and 19, since a statement in other words escapes them, as `changelog.md:3` does.

An agent acts on the row. The inspector reads the chosen approach against the tree, and a later reader of this run's records takes the row as what the run concluded. Read as written, the row has a later change to what a keep file holds search on "is to print at that phase's close" alone, and that search misses the home and the file set's row.

The severity is weighed on the ground row 73 states: this is the run's last round, and a `should` takes a home that costs no round. The fix below touches the work item's records alone. Under *No fix that no round reads* of `skills/core/SKILL.md` *Judgment is not licence to skip a party*, the inspector is its first reader, so no round is owed. The orchestrator may give it another home.

In `frame/plan.md`, replace the row at line 33 with this row. The row at line 73 and every other record stay as they are:

```markdown
| A sentence that says which lines a keep file holds states the home's fact, and no sentence claims what every other sentence does (round 3). The README line and the `## Rule changes` `to:` lines take the home's words, "is to print at that phase's close"; a sentence that states the same fact in its own words stays, as the orchestrator's row of round 3 in *Judgments of the run* decides | a later change to what a keep file holds lists the statements with `git grep` on the home's words, as contract rule 19 asks, and that search is a sample, since a statement in other words escapes it | chosen, by the fold of round 3 |
```

## Confirmations

```iadd
confirms: round-3#1
```
What holds: the universal is gone from the built files. `git grep -n -i -e 'one statement of which' -e 'every other sentence that says so' -e 'every other sentence of the frame' -e 'By it, the lines' -- . ':!<this work item's trail>'` prints nothing (`executed`). The home at `skills/verify/SKILL.md:72-76` reads "The keep file of phase `<N>` holds each line its search is to print at that phase's close". It goes on: "Those lines are the lines the design keeps and the lines a later phase changes or removes". That is what `frame/design.md:80` says (`read`). The builder's sentence at `:115-119` writes a rewritten kept line into each keep file "that holds the line by the statement of what a keep file holds, above". With the universal gone, that names the home's sentence alone (`read`). `agents/framer.md:183-186` cites the home for which keep files hold "either line, a line a later phase removes among them" (`read`). The overview at lines 94 to 96 of `agentory/README.md` and of `templates/setup/agentory-README.md` reads "phase N's search is to print at that phase's close". `diff` of the two files prints nothing (`executed`). `skills/implement/SKILL.md:354` stays, as row 73 decides. Round 3's second search prints nothing, and its first prints the lines the close lists (`executed`). The passage check, the wrap check and `tests/lib/test_optin.py` pass at the target (`executed`, `## Probes`). The words the row of finding 1 quotes are the subject of that finding, not of this close.

```iadd
confirms: round-3#2
```
What holds: `frame/design.md:80` no longer holds the universal, and reads "Those lines are the lines the design keeps and the lines a later phase changes or removes" (`read`). The `to:` lines at `:120` and `:124` read "is to print at that phase's close". The `to:` at `:134` reads "The lines and paths the search of phase N is to print at that phase's close are phase N's keep files'". The "keeps" round 3 named is gone from it (`read`). *Scope* item 1 at `:39` drops the clause on one statement cited everywhere, and *Scope* item 2 at `:40` cites Scope item 1's home. Each matches the home and `agents/framer.md:183-186` (`read`). *Scope* item 4 stays, as row 73 decides. The probe of round 1, written again, parses `## Rule changes` whole: five operations, no error, no unread line. `apply_op` places each in `docs/layout/the-record-layout.md` at the target, and the placed rows carry the new `to:` text (`executed`, `## Probes`). So `frame/questions.md` Q2's answer still holds. Finding 1 is in the fold's row of *Alternatives considered*, a unit the same fold added, so it carries `regression: round-3#2` beside this line.

What matched: the failure cell of the row at `frame/plan.md:31` lists `skills/implement/SKILL.md` line 354, both README overviews, *Scope* item 4 and three `to:` lines. That is what round 3's two findings name (`read`). Row 73 says the universal leaves `skills/verify/SKILL.md` and `frame/design.md` *Data & interfaces*, and that the README line and the `to:` lines take the home's words. Each holds at the target (`executed`, the searches above).

What matched: `pr.md` is unchanged in the range. `routing.md` *Why this way* and the `feat:` row of `frame/plan.md` *Judgments of the run* still hold each sentence it quotes word for word (`read`). `changelog.md` is unchanged in the range, and its bullet on the overview still holds against both README files (`read`). `gaps.md` is unchanged in the range and removes no row (`read`).

`chain_check.py --worktree`, run after this record was written, printed no notice at a line of `frame/design.md` naming a test pin or a copy (`executed`, `## Probes`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the format check. The suite stays `unverified` here, and the fix pass's whole *Review rounds 1..n* run was not repeated. Once finding 1 has its home, what comes due is the orchestrator's broad run, and the inspector's spawn after it | `agentory/config.json` `Broad gate` | the orchestrator |
| Whether a framer, a crafter and an orchestrator follow the rules this work wrote in a later run. A round reads each rule for one reading and runs no agent | `gaps.md` `## Not verified`, its second and third rows | the repository owner, through the row this work adds to `agentory/follow-up.md` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py tests/lib/test_optin.py -q`, in the scratch clone at `274b7d02` | exit 0, 126 passed |
| `test_tmp_rule_changes.py` under the round's scratch directory, written again from round 1's row and run once with the clone's `.venv` Python: `rule_changes.parse` over `frame/design.md` with policy root `docs`, then `apply_op` of each operation over `docs/layout/the-record-layout.md` | `ops 5 errors [] unread []`, and each of the five operations printed `placed`; the placed text holds the `to:` lines of `frame/design.md:120`, `:124` and `:134` |
| `git log --merges --oneline f2a0b1a8..274b7d02`, `git merge-base --is-ancestor origin/release/v0.41.0 274b7d02` and `git diff --stat f2a0b1a8..274b7d02` | no merge; exit 0; the range changes the two README files, `frame/design.md`, `frame/plan.md`, `trail/rounds/round-3.md` and `skills/verify/SKILL.md`, and no Python file |
| finding 1's two searches, at `274b7d02` | the lines finding 1 names |
| round 3's two searches from its finding 1's `evidence:` line, at `274b7d02` | the first prints the lines the close of round-3#1 lists; the second prints nothing, exit 1 |
| `git grep -n -i -e 'one statement of which' -e 'every other sentence that says so' -e 'every other sentence of the frame' -e 'By it, the lines' -- . ':!agentory/threads/1795841830-find-leftovers-before-a-round/trail'`, at `274b7d02` | nothing, exit 1 |
| `diff templates/setup/agentory-README.md agentory/README.md`, at `274b7d02` | nothing, exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.41.0 --root <the branch worktree> --worktree`, after this record was written, with the installed plugin's copy and with the tree's | exit 0 from each; each names finding 1 of this record as open for having no close block, and the missing gate record and inspection, and prints no notice at `frame/design.md` |
