# Guarantee: 1794289597-pr-md-copies-the-changelog-below-the-fold

The audit is of `dc14c54ad` against `release/v0.37.2`, resolved as
`seal gate` resolves it: `release/v0.37.2@{upstream}` answers
`ce915f17e`, as `origin/release/v0.37.2` does; the local
`release/v0.37.2` stands at `df775c52c` and was not used (executed,
`git rev-parse --verify --quiet` on each). The definition applied is the
tree's `agents/sealer.md`, which this diff changes at step 2 only.

**Step 1.** `trail/gate.md`'s last `seal` block reads
`run: 0004bbd60 against ce915f17e`. `0004bbd60` is an ancestor of HEAD, and
`git log --no-merges --name-only 0004bbd60..HEAD ^ce915f17e` lists one
commit, `dc14c54ad`, touching
`seal/threads/1794289597-pr-md-copies-the-changelog-below-the-fold/trail/gate.md`
alone (executed).

**Step 2.** The tree's
`bin/seal pr-body seal/threads/1794289597-pr-md-copies-the-changelog-below-the-fold --body <scratchpad>/1794289597-pr-md-copies-the-changelog-below-the-fold/body.md --check`
exits 0 and prints "matches: … is `pr.md` above `## From the records` and
the records' text below it" (executed). The two language keys of
`seal/config.json` both read `English`, and no `pr.<lang>.md` stands, so the
first part is `pr.md` alone (read). In the body, `## From the records` is
line 11, `## What changed` line 13, `<details>` line 40 and `</details>`
line 129, so the changelog fragment stands above the fold and nothing of it
inside (executed, `grep -n` on the body).

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The S1 layout case, the S2 case and the S4 case each fail against `_composed` as 0.37.1 shipped it, on their layout lines | `trail/phases/phase-1.md`, the paragraph **Each new case was seen red against `_composed` as 0.37.1 shipped it** | In a clone of the worktree at `dc14c54ad` under the scratchpad, `skills/code-review/scripts/pr_body.py` restored from `ce915f17e` (equal to `v0.37.1`, `git diff --stat v0.37.1 ce915f17e` empty): `bin/test tests/skills/test_pr_body.py -q -p no:xdist -k "test_accepts_a_work_item_as_the_records_text or test_accepts_a_missing_changelog_above_the_fold or test_refuses_the_changelog_inside_the_fold_until_written_again"` | Holds. Exit 1, 3 failed. The S1 case fails on `EXPECTED` with `<details>` and its `<summary>` under `## From the records`; the S2 case on `['## From the records', '']`; the S4 case on `assert 0 == 1`, the stale body matching. Each is the line the record names |
| `RULES` row 23 fails with the owner's sentence and the carriers' links absent | `trail/phases/phase-2.md`, the paragraph **`RULES` row 23 was seen red, then green** | In the same clone at HEAD, the owner and the four carriers restored from `ce915f17e`: `bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k 23` | Holds. Exit 1, 2 failed: the owner case names `skills/code-review/orchestration.md` and the sentence; the link case names `skills/commit-pr-convention/SKILL.md`, its first carrier |
| Each carrier's link is held by the link case alone, so taking one carrier back fails on that carrier | `trail/phases/phase-2.md` and `trail/phases/phase-3.md`, the `seal mutate` runs on `skills/implement/SKILL.md`, `templates/setup/config.md` and `skills/writing-style/outside-the-review.md` | In the same clone with HEAD's text restored, each of the three files in turn restored from `ce915f17e`, and put back after its run: `bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k "test_every_link_names_the_owner and 23"`; then the row's two cases with nothing restored | Holds. Exit 1 each time, the failing line naming the restored file as carrying rule 23 without naming the owner. With nothing restored, exit 0, 2 passed |
| The phases' narrow modules pass at HEAD, the three line-number repairs and the regenerated sealer scaffolds among them | `trail/phases/phase-1.md`, the paragraphs on the three line-number repairs and the scaffolds; `trail/phases/phase-2.md` and `phase-3.md`, the phase-boundary runs | In the same clone, clean at HEAD: `bin/test tests/skills/test_pr_body.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_evals_layout.py tests/evals/test_rule_cases.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_the_sealer_guarantees.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py -q`; `bin/test tests/skills/test_chain_check.py -q -k Test_body` | Holds. Exit 0, 360 passed; exit 0, 18 passed |
| The two seal READMEs stay identical | `trail/phases/phase-3.md`; `frame/design.md` D3, the README row | `diff seal/README.md templates/setup/seal-README.md` | Holds. Nothing printed, exit 0 |
| S7 and the out-of-scope files: `skills/implement/orchestration.md`, `skills/code-review/scripts/chain_check.py` and `docs/` unchanged against the base | `frame/design.md` S7, *Scope* "Out", G1, G3, G10 | `git diff --stat ce915f17e...HEAD -- skills/implement/orchestration.md skills/code-review/scripts/chain_check.py docs` | Holds. Nothing printed |
| D3's command lists 18 files at HEAD, each in D3's table, its list, or *Scope* items 3 and 6 | `frame/design.md` D3; `trail/rounds/round-1.md` *Confirmations* | `git grep -l -E 'pr\.md\|pr\.<lang>' -- . ':!tests' ':!evals' ':!seal/threads' ':!docs'` | Holds. 18 files: D3's table names nine, its list six, and the remaining three are `agents/proofer.md`, `agents/sealer.md` and `skills/code-review/orchestration.md` |
| S8: no shipped text outside `docs/` says `pr.<lang>.md` holds the quotes of `pr.md` alone | `frame/design.md` S8; `trail/phases/phase-3.md` | `git grep -n -E 'quotes? of .pr\.md.' -- . ':!docs' ':!tests' ':!seal/threads'` | Holds. Four hits, `agents/proofer.md:132` and `:137`, `skills/code-review/orchestration.md:430` and `:432`, each stating the new shape (read) |
| *Removes* row 2 and the changelog's *Removed* item: the re-read of every quote before each spawn of the sealer stands nowhere | `frame/design.md` *Removes* row 2; `changelog.md:13` | `git grep -n -i -E "before each spawn of the sealer\|opens each quote's source" -- . ':!seal/threads'` | Holds. No hit, under `docs/` included |
| *Removes* row 1: no `changelog.md` quote in `pr.md` | `frame/design.md` *Removes* row 1, S6 | `grep -c changelog.md pr.md` | Holds. 0 |
| *Removes* row 3: the changelog's section is no longer inside the fold | `frame/design.md` *Removes* row 3 | The S1 and S4 runs above; the body's `grep -n` of step 2 | Holds |
| *Removes* row 4: the statements of what `pr.md` and `pr.<lang>.md` hold outside the owner | `frame/design.md` *Removes* row 4, D3 | `git diff ce915f17e...HEAD` over D3's files (read), and the link guards re-run above | Holds outside `docs/`: each D3 carrier cites the owner or no longer states what the files hold. The `from` sentences under `docs/` still stand, as `## Rule changes` routes them to the settle (G1); that is the design's route, not a removal left undone |
| Each quote of `pr.md` stands word for word at its coordinate | `pr.md:1-6` | A `python3 -I` comparison, whitespace collapsed, of each quote with the file it names | Holds. 6 of 6 |
| `seal pr-checks install` never overwrites a workflow in place, so the `Updating:` paragraph's removal first is owed | `changelog.md:9`; `trail/phases/phase-3.md` | read, `skills/implement/scripts/seal.py#install_workflow` | Holds (read): its docstring says "Never overwrites" |
| The chain check passes the records at HEAD | `trail/rounds/round-1.md` *Probes* | `python3 skills/code-review/scripts/chain_check.py --baseline ce915f17e --root <the worktree> --worktree` | Holds. Exit 0; its one line on this item names the guarantee as not yet written |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `seal pr-body` writes the changelog fragment whole between the line `HEADING` holds (after the mark) and the fold; `pr.md` quotes no changelog sentence, owned by `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*; `pr.<lang>.md` renders each changelog list item's opening sentence, then each `pr.md` quote; the re-read before each sealer spawn goes; the carriers cite the owner; `docs/` changes through `## Rule changes`; `chain_check.py` and `skills/implement/orchestration.md` are not edited | #1478 *Done when*, its three lines: the owner's sentence and S6; row 23 and D3; *Scope* item 4. #1478 *Change* says the rewriting paragraph goes; the design keeps its first sentence and the finding sentence on the grounds of G9 and *Alternatives considered* row I, and the exchange row of *Judgments of the run* records the agreement, which `pr.md:4` quotes. The diff and the runs above | none |
| the build | Phases 1 to 3 at `8be913ab1`, `6030c9fbf` and `65c05791c`, each with its `trail/phases/phase-N.md`; `routing.md` answers `Implementation` with `crafter`, and each phase whose Status holds a commit has its record. Phase 1 declined S5's body-arm case; phase 3 named S7's and D3's false statements for a fold | The design, item by item against the diff (read); the claims re-run above. S7 and D3 at HEAD hold the folded text (`7bf23ef25`, `d8febe0fc`, `f778a164f`), and D3's command lists the 18 files it accounts for (executed) | none |
| the last round | Round 1 at `b1a1227c0`: finding 1, `must`, `pr.md` lacks the title row's quote; finding 2, `should`, S5's cell promises a body-arm case the build declined. Both `fixed`: `c3029edd7` and `dd9169206` | Every commit after `b1a1227c0` touches only `seal/threads/1794289597-pr-md-copies-the-changelog-below-the-fold/` (executed, `git log --no-merges --name-only b1a1227c0..HEAD`). Finding 1: `pr.md:5-6` hold the two lines the finding gives, word for word, and both stand at `frame/plan.md` *Judgments of the run*, the title row (executed, the quote comparison). Finding 2: S5's cell holds the finding's text with "of `tests/skills/test_chain_check.py`" added; `test_refuses_the_changelog_inside_the_fold_until_written_again` stands in `Test_main`, whose `--check` calls `compared` (`pr_body.py:1043`), `test_refuses_a_drifted_body_at_its_line` stands in `Test_body` at `tests/skills/test_chain_check.py:3334`, that module holds no `What changed` line, and both pass (executed); the last row of *Judgments of the run* records the fold | none |
| the changelog | *Changed*: five items, the fragment above the fold, `pr.md` quoting no changelog sentence, `pr.<lang>.md`'s new shape, the proofer's three findings and the sealer's step 2, the carriers citing the owner; an `Updating:` paragraph on re-pinning the workflow and re-sending an open body. *Removed*: the re-read before each sealer spawn. *Process changes*: four rows | The diff, item by item (read); `agents/proofer.md:132-138` names the three findings; `RULES` row 23 holds the sentence and four links; `install_workflow` never overwrites; the removal re-run above | none |
| the orchestrator's part of the pull request body | Quotes of G3 and G10, the *Operational impact* paragraph on the tree's `bin/seal pr-body`, the exchange row, and the title row with its grounds: `refactor:`, because "the diff moves where `seal pr-body` writes one record and where the `pr.md` rule is stated; no gate is added or removed, the body arm reads the same function"; then `Closes #1478.` | Each quote stands at its coordinate; `seal pr-body --check` exit 0. The grounds describe the diff: `pr_body.py` moves one section's place, the diff touches no `chain_check.py`, and it adds no check, hook or script; its one added case row is a test, which the convention says never decides a prefix. #1478's own title takes `refactor:` | none |

`routing.md` *Why this way* gives the orchestrator's grounds under
`agentic`: a framer, because the change moves the changelog into what
`seal pr-body` composes and touches that script and the documents stating
the `pr.md` rule; a crafter; the review chain, because the body arm gates
every ready pull request. The diff is that script, the owner section, the
two agent definitions, the carriers D3 names, the regenerated sealer
scaffolds and the cases (read). The grounds describe it.

No `seal/parity.json` stands (executed, `ls`), so no comparison with an
original is owed.

The suite, the lint and the format check were not run here; the broad run
at `0004bbd60` in `trail/gate.md` answers them, and only `trail/gate.md`
follows it. The five sealer eval cases run by an agent stay `unverified`,
answered by the repository owner at the next behaviour-eval run
(`gaps.md:8`).

```seal
target: dc14c54adef0beebbe7c3a84c53fcae9f5cf7ee9 against ce915f17e9289b92f6335427d89f4e5b577790e0
Verdict: sealed
```
