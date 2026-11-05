# Guarantee: 1793862999-unverified-baseline-is-run-by-a-person-only

The audit read the tree at `37e9bd23`. The base `release/v0.32.5` resolved
through `origin/release/v0.32.5` to `a0303ee9` (executed: `git rev-parse
--verify --quiet`; `release/v0.32.5@{upstream}` and `release/v0.32.5` named
no commit here). `trail/gate.md` records the broad run at `41c2c023`, an
ancestor of HEAD. Only `37e9bd23` follows it, and that commit touches
`seal/threads/1793862999-unverified-baseline-is-run-by-a-person-only/trail/gate.md`
alone (executed: `git log --no-merges --name-only 41c2c023..HEAD ^a0303ee9`).
`seal pr-body <item> --body <pr-body.md> --check` exited 0, so the part of
the body below `## From the records` is the records' own text (executed). No
`seal/parity.md` is tracked (executed: `git ls-files seal/parity.md`), so no
parity comparison is owed.

The re-runs used a `git clone --no-local` of the branch at `37e9bd23` in the
scratchpad, `<scratchpad>/1793862999-unverified-baseline-is-run-by-a-person-only/at-base/`.
For each `seen red`, `skills/verify/scripts/unverified_check.py` was
restored from `a0303ee9`. For each guard claim, HEAD's code was restored and
one guard was removed with the Edit tool. HEAD's code was put back after
every run, and the clone was removed once the runs were done.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| A1 was red against the unchanged script with "DID NOT RAISE SystemExit" | `trail/phases/phase-1.md:88` | in the clone with `unverified_check.py` from `a0303ee9`: `bin/test tests/skills/test_unverified_check.py -q -p no:randomly -p no:xdist -k 'test_refuses_the_baseline_option_it_no_longer_has or ...'` | holds (executed). `Failed: DID NOT RAISE SystemExit` on `Test_main::test_refuses_the_baseline_option_it_no_longer_has`. With HEAD's code, all 69 cases of `Test_main`, `Test_overviews`, `Test_open_record_rows` and `Test_parse_section` pass |
| The settled-root case pins the `SETTLED` sentence without "and nothing left the record without being closed" | `trail/phases/phase-1.md:45-51`; `changelog.md:3` | the same run, `-k test_the_roots_own_specs_path_is_settled_when_nothing_is_under_it` | holds (executed). Both parameters, `[empty]` and `[absent]`, fail at base on `assert "left the record" not in said`, and the base text ends "...being closed" |
| The no-root case pins `ABSENT` without "nothing to compare against the base" | `trail/phases/phase-1.md:52-53`; `changelog.md:3` | the same run, `-k test_accepts_no_root_in_the_tree` | holds (executed). It fails at base, and the base message reads "...there is no record to read and nothing to compare against the base" |
| The link case goes red when the real-path reading is removed; it asserts a team's `specs/` is not read, so rule 15's guard removal applies | `trail/phases/phase-1.md:33-40`, `:92-93` | in the clone with HEAD's code and `os.path.realpath(p)` changed to `os.path.abspath(p)` in `overviews`: `bin/test ... -k 'Test_main or Test_overviews or Test_module'` | holds (executed). Only `Test_overviews::test_refuses_a_reference_root_on_a_walk_reached_through_a_link` fails, on `Left contains one more item: '1788000001-team-thing'`, which names the leaked reference root; 24 pass |
| Phase 3 mutant 1, the header check relaxed to `is_header`, fails `test_refuses_a_section_it_cannot_count_at_its_line[the old column]` (round 1 left phase 3's mutants to the sealer) | `trail/phases/phase-3.md:59-71`; `trail/rounds/round-1.md:220` | in the clone with HEAD's code and `if tuple(cells) != HEADER:` changed to `if not is_header(cells):`: `bin/test ... -k "Test_parse_section or Test_sections or Test_check_text or Test_open_record_rows"` | holds (executed). That one case fails, and 61 pass |
| Phase 3 mutant 6: with the unreadable entry dropped, `open_record_rows` returns zero rows, and the A4 case goes red | `trail/phases/phase-3.md:24-27`, `:68` | in the clone with HEAD's code and the `if errors: found.append(... "cannot be read" ...)` lines removed: the same selection | holds (executed). `Test_open_record_rows::test_refuses_to_read_a_section_it_cannot_read_as_nothing_open` fails on `assert (0 == 1)`, and 61 pass |
| The marker `a-settle-is-no-deletion` stands only on chain_check's settled-declaration case, and that case passes | `trail/phases/phase-1.md:96-97`; design A3 | `git grep -n 'a-settle-is-no-deletion\|one-merge-base' -- tests docs`; in the clone `bin/test tests/skills/test_chain_check.py -k 'test_accepts_a_declaration_a_settle_removed or test_every_reader_of_a_retirement_calls_the_one_predicate'` | holds (executed). The marker in tests appears only at `tests/skills/test_chain_check.py:4026`, and 3 cases pass |
| `seal rules --check` excuses one line, `one-merge-base` at `docs/checks/the-unverified-record.md:14`, and every other line holds | `trail/phases/phase-1.md:94-95` | `bin/seal rules --check` in the clone | holds (executed). Exit 0, "1 excused in 226 check lines of 70 rule files", and the excused line names this work item's settle |
| `seal unverified --baseline` exits 2 as an unknown argument, and the plain run is unchanged | design A1, A2; `changelog.md:3` | `bin/seal unverified --baseline HEAD .`; `bin/seal unverified seal/threads` in the clone | holds (executed). Exit 2 with `usage: seal unverified [-h] [path ...]` and `unrecognized arguments: --baseline`; the plain run exits 0 with `33 closing memos · 112 open · 11 closed · 0 unreadable` |
| `strict_header` and `_text_at` are gone from the tree | `trail/phases/phase-3.md:72-73` | `git grep -n -w` for each of the twelve removed names and `strict_header`, outside `seal/threads` and `.test_durations` | holds (executed). No definition or call of any removed unit remains. The `-w` hits for `spellings`, `real` and `mode_at` are other modules' own words and helpers (`base_spellings`, test-local `real`, `tests/censuses.py`'s `mode_at`) |
| A `workflow_dispatch` run of `tests` at `41c2c023` passed every leg, Windows included, and its output does not name the new link case | the orchestrator's part of the pull request body | `gh run view 41996320401 --json headSha,conclusion,jobs`; `gh run view 41996320401 --log`, searched for `reached_through_a_link` | holds (executed). The head SHA is `41c2c023…`, the conclusion is `success`, and every pytest leg (four Windows, three macOS, one Ubuntu), `lint`, `arms-grammar` and `durations` succeeded. `release-report` was skipped, and it is no test leg. The log names the case 0 times |
| The broad run passed at `41c2c023` with 6300 passed and 12 skipped | `trail/gate.md:4`; the orchestrator's part of the pull request body | read the printed output the prompt names (`gate.log`) | holds (read). `BROAD GATE PASSED ... @ 41c2c023 against origin/release/v0.32.5 @ a0303ee9`, `suite ✓ 6300 passed · 12 skipped`, `chain ✓ exit 0`, `exit=0`. Not re-run: rule 2 makes the broad run the orchestrator's alone |

## Removes, against the tree

Every code and test row of design `## Removes` is gone at HEAD (executed:
the `git grep -w` above, and `git grep -n -e '--baseline'` over
`skills/verify` and the two test modules, which names only `chain_check.py`'s
and `payload_meter.py`'s own flags and A1's own case). `main` holds no
`--baseline` arm and returns 1 only for an unreadable section (read:
`skills/verify/scripts/unverified_check.py:1342-1415`). `overviews` reads
`os.path.realpath` (`:934`). `open_record_rows(root, directory)` and
`check_text(text)` have the signatures *Data & interfaces* states, and
`settle.py:944` and `:1795` pass no `None` (read). The two prose pins and
`TIP_EN` are gone from `tests/behaviour/test_unverified_rows_close.py`, and
`[--baseline <ref>]` is gone from both READMEs (read).

The four `docs/` rows of `## Removes` stand in the tree on purpose. The
design keeps the policy root for the settle (plan *Alternatives considered*
row 7), and each row has its `## Rule changes` operation. Every `from` those
operations quote stands in its file today, so the settle can apply them
(executed: a whitespace-collapsed match of each `from` and of the removed
section's heading). The `changelog.md` items name no removal that stands.

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `--baseline` and the units only it used leave. The relaxed reading at a ref leaves too. The plain run, the three exit-0 states and the predicates `chain_check.py` and `settle.py` load stay. The proofer reads a deleted row or memo in the closing memo's diff, and `docs/` changes at the settle | the issue's *Decision* and *Done when*, the tree (claims and *Removes* above), the build, the changelog | none. Folds at `1fd6b8d2`, `6b925563`, `c2702707` and `f2298696` record the phases' contradictions, and *Scope* item 9 as folded matches `skills/implement/SKILL.md:382-386` and `skills/code-review/SKILL.md:35-49` |
| the build | Phases 1-3 removed the mode, the eleven units, the relaxed reading and the pins. They added A1 and the link case, and rewrote the docstrings and the two skills' prose. Fix passes `fb1f126e`, `96ce5e6f` and `b250e66a` rewrote the closing-memo paragraph and added the stage-1 reading | the design (including its recorded departures on `SETTLED` and the extra link case), the tree | none. Every sampled `seen red` and guard claim held |
| the last round | Round 3 at `b55f9db2` confirms round 2's two fixes and raises no finding. The stage-1 paragraph keeps the fold rule's merge-base condition and reads "left" as design *Scope* item 9 does | the design, the build, `docs/checks/the-fold.md:11-23`, `unverified_check.py#settled` (`:1160-1174`, read: settled is held-at-ref and gone, nothing else) | none. It carries no `fixed` finding, so no fix-pass claim waits on the sealer |
| the changelog | Two items. `--baseline` is gone: exit 2, exit 1 only for an unreadable section, the proofer as reader, the two exit-0 messages lose their base clauses, and the README rows change. The relaxed reading at a ref is gone, and what either command prints does not change | the tree, as re-run above. "What either command prints does not change" is said of the second item, and at `a0303ee9` `open_record_rows` with `ref` None already called the strict `check_text` (read), which is the only path `settle.py` took | none |
| the orchestrator's part of the pull request body | It quotes the changelog and the issue's decision, closes #1240, says `docs/` is not edited, says the version moves to 0.32.5 here, summarises the three rounds by their finding titles, and gives the broad run and CI run 41996320401 | the changelog (quotes verbatim), the issue's *Decision*, `git diff --stat a0303ee9...HEAD` (no `docs/` file; `.claude-plugin/plugin.json` `0.32.4` to `0.32.5`), the rounds' titles, the gate output, the CI run | none |

The plan's *Judgments of the run* place the version move in this work item.
Rounds 2 and 3 leave open, for the orchestrator at merge time, whether #1240
enters `release/v0.32.5` first. That is a sequencing question, and no party
contradicts the issue or the tree on it. `gaps.md` keeps two open rows: the
broad run at HEAD, which `trail/gate.md` answers at `41c2c023`, and the
Windows run of the link case, which stays unanswered because the CI log names
no case. Both rows name an answerer, and no party claims either is closed.

```seal
target: 37e9bd23 against a0303ee9
Verdict: sealed
```
