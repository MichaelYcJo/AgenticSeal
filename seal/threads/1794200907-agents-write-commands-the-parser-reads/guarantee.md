# Guarantee: 1794200907-agents-write-commands-the-parser-reads

The audit read the tree at `3507db3b` against `release/v0.37.0`, which
resolves to `dfd0c995` through its upstream (executed: `git rev-parse
--verify --quiet`). `trail/gate.md`'s newest run names `061ef2f8`, an
ancestor of HEAD, and the one commit after it, `3507db3b`, touches only
`trail/gate.md` (executed: `git log --no-merges --name-only
061ef2f8..HEAD ^dfd0c995`). `seal pr-body <item> --body <file> --check`
exited 0 on the body file the spawn named (executed).

The second run audits `25724484`, after the withhold at `3507db3b`. The
two commits since, `5656e523` and `25724484`, touch only `guarantee.md`
and `frame/design.md` of this work item (executed: `git log --name-only
3507db3b..HEAD`), so no code claim's coordinate changed and the claims of
the first run stand unre-run. `trail/gate.md`'s run at `061ef2f8` is
followed only by paths under this work item's directory (executed), and
`seal pr-body --check` exited 0 again on the same body file (executed).

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| Seen red: the entry for 21 in `FACTS`, with rule 21 absent, fails 5 cases and passes 14 | `trail/phases/phase-1.md:57-63` | in a clone at `3507db3b`, `git checkout dfd0c995 -- skills/agent-contract/SKILL.md`, then `bin/test tests/text/test_the_agent_contract_holds_the_universal_rules.py -q -p no:xdist` | holds (executed): exit 1, 5 failed and 14 passed, `test_each_section_holds_its_rule[21]` on "rule 21 no longer holds the command forms", the other four on `KeyError: 21` |
| Seen red: the two scratch cases fail on their first assertions before their sentences are written | `trail/phases/phase-2.md:16-26` | in the clone, `agents/crafter.md` and the contract restored from `dfd0c995`, then the contract alone from `4c193822`; each time `bin/test tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py -q -p no:xdist` | holds (executed): exit 1, 2 failed and 4 passed both times. At `4c193822` the crafter case fails on the phase directory assertion and rule 21's case on the `<scratchpad>/<work-item-id>/` assertion, the lines the record quotes. At `dfd0c995` rule 21's case fails with `ValueError`, because no rule 21 stands there |
| Mutation: "share one scratchpad" written as "use one scratchpad", and "never names the" written as "names the", each read red | `trail/phases/phase-2.md:28-40` | in the clone at `3507db3b`, both mutants applied through the Edit tool, then the same module | holds (executed): exit 1, 2 failed. Each case fails on the assertion for its own guard: "agents of one session share the scratchpad" and "does not say a removal never names the scratchpad itself" |
| The modules that read a path the diff changed pass at HEAD, the census module among them | `trail/phases/phase-2.md:86-104`, `trail/rounds/round-3.md` *Probes* | in the clone at `3507db3b`, `bin/test` over the scratch module, the contract pin module, `test_every_tracked_file_meets_every_census.py`, `test_a_moved_rule_leaves_its_definition.py`, `test_docs_line_wrap.py`, `test_a_cited_section_stands_in_its_file.py` and `test_every_agent_reads_the_contract.py`, `-q`; then `bin/seal rules --check` | holds (executed): exit 0, 350 passed; rules check exit 0, "all 221 check lines in 68 rule files hold" |
| `$(cat list)` and `xargs … < list` split a list the same way in bash and zsh; an unquoted variable splits in bash and not in zsh; `"${VAR:?}"` stops the line where the variable is unset or empty | `skills/agent-contract/SKILL.md:221-226`, `frame/design.md` G11 | `bash -c` and `zsh -c` over a two-line list, `F="x y"; printf "[%s]" $F`, and `${V:?}` with `V` empty and with `Q` unset | holds (executed): both shells print `[a][b][c]` for both list forms; bash prints `[x][y]` and zsh `[x y]`; the guard exits 127 in bash and 1 in zsh, empty and unset alike |
| The crafter removed the whole scratchpad twice, at 05:34:41Z and 05:46:32Z | `frame/design.md` G18, `changelog.md` *Fixed* the fourth item | a read-only Python scan of the `rm -rf` Bash calls in the crafter's transcript `agent-a5cc507e4ff134b78.jsonl` | holds (executed): two calls, `rm -rf "<scratchpad>"`, at 2026-11-09T05:34:41Z and 05:46:32Z |
| `rm -f "$f"` is gone from `skills/update/SKILL.md`, and no file outside `seal/threads/` names `0.36.0` | `frame/design.md` *Scope* item 3, `frame/plan.md` *Operational impact* | `git grep -n -F 'rm -f "$f"' -- skills`; `git grep -n -F '0.36.0'` outside `seal/threads/` | holds (executed): no match for either; `.claude-plugin/plugin.json:4` reads `0.37.0` |
| `frame/design.md` `## Removes` reads `nothing`, and the changelog names no removal | `frame/design.md:87-90`, `changelog.md` | read | holds (read): nothing is owed absent from the tree |
| Every quote in `pr.md` stands word for word in its source | `pr.md` | a read-only Python comparison of each quote with `changelog.md` and `gaps.md`, runs of whitespace collapsed | holds (executed): nine of nine |
| Round 3 finding 1, `fixed 647a5495`: the frame counts two removals of the scratchpad | `trail/rounds/round-3.md` finding 1, `frame/design.md:90`, `frame/plan.md:62` | `git show --name-only 647a5495 061ef2f8`; `git grep -n -i -E 'three (times\|removals)\|removed three'` over the work item | holds (executed): both commits touch only the work item's records; the design says "the two removals" and the plan row "twice"; "three" stands only in round 3's own quotes of the old text |
| Rule 21's check line names one module (the first run, at `3507db3b`) | `frame/design.md:63`, *Data & interfaces* | read `skills/agent-contract/SKILL.md:232`; `git blame -L 63,66` on the design | did not hold (executed): the check line names `tests/text/test_the_agent_contract_holds_the_universal_rules.py` and `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`. Line 63 was the first frame's (`2831458a`); the fold `4c193822` added line 66 with the two-module line and left line 63 standing |
| The fix `25724484`: the design states rule 21's check line once, naming both modules | `frame/design.md:63`, `frame/design.md:66` | `git diff 3507db3b HEAD -- frame/`; `git grep -n 'check:'` over the design | holds (executed): line 63 now reads "Its last line is the check line below", and line 66 is the one statement of the check line, naming both modules as `skills/agent-contract/SKILL.md:232` does. The other `check:` in the design, line 85, is the rule change's for `docs/running/the-agent-set.md`, not rule 21's |
| The records still meet the record and census modules at the new HEAD | `25724484` | in a clone at `25724484`, `bin/test tests/behaviour/test_every_tracked_file_meets_every_census.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` | holds (executed): exit 0, 121 passed |

Not re-run: the transcript counts of `frame/design.md` G8 to G10 are the
framer's reading (unverified; the measurement `frame/questions.md` Q1 names
answers it). Whether agents follow rule 21 and crafters keep to their
directories once they run under 0.37.0 is unverified; `gaps.md` *Not
verified* names the measurement that answers it. The broad gate is the
orchestrator's run that `trail/gate.md` records at `061ef2f8`; this audit
ran nothing broad.

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | contract rule 21 with its forms as examples, its pin in `FACTS`, the guarded `rm` in `skills/update/SKILL.md`, step 1's pointer for the orchestrator, the crafter's `phase-<n>/` and `fix-<n>/` directories, rule 21's removal clause and their two cases; no check reads a command; `## Removes` is nothing | the issue's *Done when* (the rule stated once with the two zsh forms as examples, no check added), its two comments, the build, the changelog | none at `25724484`. At `3507db3b`, `frame/design.md:63` said rule 21's last line named one module, where `frame/design.md:66`, *Scope* item 6 and `skills/agent-contract/SKILL.md:232` name two; `25724484` removed that statement |
| the build | the diff of `.claude-plugin/plugin.json`, `agents/crafter.md`, `skills/agent-contract/SKILL.md`, `skills/implement/orchestration.md`, `skills/update/SKILL.md` and two test modules, with phase records for phases 1 and 2 at `df508485` and `ba3ba7a4`, both on the branch | the design's *Scope* items 1 to 8 and *Data & interfaces*, line 63 among them since `25724484`; the phase records' seen red and mutation claims re-run above; no file under `hooks/`, `bin/` or a `scripts/` directory changed | none |
| the last round | round 3 at `94a52303`: one `should` finding on the removal count, fixed in the records at `647a5495`; confirmations of the crafter's rule, rule 21's clause, the two cases and their seen red | the tree at HEAD and the fix as read above | none |
| the changelog | four *Fixed* items and two *Process changes* rows, for `skills/implement/orchestration.md` and `agents/crafter.md`; the 21 prompts, 19 in two shapes, as G9 counts them | the diff, `frame/design.md` G9 and G18, the crafter's transcript | none |
| the orchestrator's part of the pull request body | `pr.md`: nine quotes of `changelog.md` and `gaps.md`, then `Closes #1445.` | each quote's source, word for word; the issue it closes | none |

```seal
target: 3507db3b against dfd0c995
Verdict: withheld reason: the design (framer, folded at 4c193822) states at frame/design.md:63 that rule 21's last line is `check: tests/text/test_the_agent_contract_holds_the_universal_rules.py`, where frame/design.md:66 and the tree at skills/agent-contract/SKILL.md:232 name that module and tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py; line 63 is the old statement the fold left beside its correction
```

```seal
target: 25724484 against dfd0c995
Verdict: sealed
```
