# Phase 2: 1795439973-six-test-modules-cost-past-the-rewrite-bound

## What this phase found

### The frame, read against the tree before the build

The frame holds for the arm classes, with two facts it did not state. At `a6f69fbba` the coordinates `frame/design.md` *Grounding* gives stood where it says (read): `_branch_template` at `:239`, `branch` at `:291`, `seal` at `:300`, `put_spec` at `:1468` and the `item` fixture at `:2747`, each the decorator line above the definition the frame cites. In `skills/code-review/scripts/chain_check.py`, `pins_and_copies_in` reads git only where `sources` is empty (`:1289`), and `read_record` reads the disk where `WORKTREE` is set (`:505`).

- **`Test_broad_gate` ran `main` in none of its cases at the base.** Its seven cases called `broad_gate` directly. *Scope* item 2 keeps one or two `main` runs per arm. For this arm the phase kept the arm's one real-git case and added no `main` run, since none stood there to keep (*Departures from the frame*).
- **`main` leaves `chain.WORKTREE` as its last run set it.** `main` assigns the module flag at every run and never restores it (`chain_check.py#main`, `global WORKTREE`). A unit call after a case whose last `main` run passed `--worktree` would read the disk where it meant HEAD. `frame/plan.md` *Technical context* asks a unit call to set such a flag through `monkeypatch`, so the phase's one seam, `reading`, holds `WORKTREE` False for its case.

### Q1: where the arm classes' seconds went before the rebuild

`bin/test tests/skills/test_chain_check.py -q -p no:xdist --durations=0` at `a6f69fbba` passed 252 cases in 111.3 s on this macOS machine (executed). The seven arm classes took 73.9 s of it, 13.2 s in setup and 60.7 s in their calls. The test file at `a6f69fbba` is the file at `2d343a752`.

The seconds were git processes, in three places (read from the profile and the case bodies).

- **Each case's world.** The `item` fixture ran `git init` and two commits for each of its 24 cases, about 0.18 s of setup each. The `bodied` fixture ran `git init`, four commits and two compositions for each of its 18 cases, about 0.30 s each.
- **Each case's own commits.** A case of the rule-changes, check-line, pin and parity arms committed its design and then the closing records (`put_spec`, `seal`), and often a round at HEAD and the closing records again (`reviewed_to_head`).
- **`main` itself.** One `main` run over a copy of the branch starts 41 git processes (`frame/design.md` *Grounding*). The arm cases held 91 call sites of `check(root` or `chain.main(` at the base (executed: an `ast` census of the seven classes, `census.py` in this phase's scratch).

### What the rebuild changed

All of it is in `36d15a994`.

- **The arms are called in the process.** A case whose fact is how an arm reads its input now calls `rule_changes_read`, `rule_changes_of`, `originals_of`, `guarantee`, `broad_gate` or `body` with that input given. The record reaches the arm through `reading`, which replaces `chain.read_record` for the case and leaves every other path to git's HEAD. A design and the files planted beside it are read from a copy's working tree under `WORKTREE` (`planted`), with the planted files staged so that `git ls-files` lists them as `_read_tree` asks.
- **Two worlds are built once per module.** `_item_template` and `_bodied_template` are module-scoped. The `item` and `bodied` fixtures keep their names and copy them, as `branch` copies `_branch_template`. A case that only reads takes the template itself with no copy: `reading` hands it the record, and `main` over a template writes nothing into it, since `changed` runs `diff` and `hash-object` without `-w` (read: `chain_check.py#changed`).
- **What stood on the old shape went in the same commit.** `bodied_with` was the per-case builder, and `reseal` and `direct_migrating` built the parity history the direct-guarantee cases committed. No case calls them any more, so they are gone. The module docstring now says how the arms are called.
- **The arm cases now hold 31 call sites of `main`**, against 91 at the base (executed: the same census at `36d15a994`). Each call site that stays is a case that shows `main` reaches the arm, or one whose fact is which records `main` hands the arm (*3. The real-git cases kept*).

### Departures from the frame

- **The broad gate arm has no `main` run.** *Scope* item 2 keeps one or two per arm. `Test_broad_gate` had none at the base, and `main`'s call of the arm is held by `Test_main`, which phase 3 rebuilds. The arm's real-git case is `test_lets_the_records_follow_the_run_and_refuses_any_other_path`, which commits after the run and reads `follows` over git. Grounds: `CONTRIBUTING.md` *The test layout*, the paragraph opening "A module's old cases get one verdict each", places a case as it stands where its fact is held.
- **Several cases whose fact is `main`'s choice of what to hand the arm stay `main` runs over a real repository.** They are the rule-changes cases about another work item's design the branch edits, a release's squash, a pull request that declares nothing, a moved design, a draft and an unseen pull request, and the body cases about `--worktree`, `--sealing`, a draft and a merge past a later base commit. No unit call on the arm reaches those facts. `frame/plan.md` *Alternatives considered*, A3, keeps such a case a real-git case, and the phase record names it.

### The four parts `CONTRIBUTING.md` *The test layout* asks of a rebuilt module

**1. The move check, and the mutation table.**

`bin/seal layout --moved a6f69fbba --from tests/skills/test_chain_check.py --to tests/skills/test_chain_check.py` exits 1 (executed). Its last line reads `seal layout: moved: 206 old cases, 251 items against 251 at a6f69fbbaec5, 146 failed`. The rebuilt cases no longer run the old cases' `main` over a new commit, so the check finds no new case standing for most old ones, and the mutation table below carries part 1.

The mutants sit at the decision points of the arms the seven classes judge, and at the lines of `main` that hand each arm its input. All 57 ran in one call against `36d15a994` (executed): `bin/seal mutate skills/code-review/scripts/chain_check.py --replace OLD NEW ... --tests "bin/test tests/skills/test_chain_check.py -q -x"`, built by `run_mutants.py` from `mutants.py` in this phase's scratch. It printed `seal mutate: 57 mutants, 56 red, 1 SURVIVED, 0 with no verdict (546.2s)`. Each row shows the first line the mutant changes. The full OLD and NEW of each are in `mutants.py`.

The base file column is filled only for a survivor. Mutant 8 ran again against the test file at `a6f69fbba`, copied to `tests/skills/test_tmp_chain_check_base.py` and removed after, and survived there too (executed). The gap predates this phase. `_read_tree` skips a `*.md` outside the corpus before it opens it, and `rule_changes.py#copies` skips the same paths again (`skills/settle/scripts/rule_changes.py:578`). With the first skip gone, the copies found are the same, and only an undecodable `*.md` outside the corpus would gain a not-read notice. No case of either file plants such a document. Phase 2 adds no case for it: its frame rebuilds the existing cases and adds no fact, and `agents/crafter.md` *Never* bars building beyond the request. `gaps.md` names it.

| # | Unit | Old | New | New file | Base file |
|---|---|---|---|---|---|
| 1 | `check_lines_in` | `if op.kind not in WRITES_A_TO:` | `if op.kind != "change":` | red |  |
| 2 | `check_lines_in` | `(rel, numbers[n - 1], CHECK_LINE_SAYS` | `(rel, numbers[0], CHECK_LINE_SAYS` | red |  |
| 3 | `check_lines_in` | `notices.extend(` of the near lines | `list(`, the notices dropped | red |  |
| 4 | `check_lines_in` | `except checks.Unreadable as exc:` | `except ValueError as exc:` | red |  |
| 5 | `_tracked` | `unread.append(("", 0, RULE_CHANGES_UNREAD.format(why=why)))` before `return []` | (line removed) | red |  |
| 6 | `_read_tree` | `RecursionError,` in `TEST_UNREADABLE` | (line removed) | red |  |
| 7 | `_read_tree` | `unread.append((path, 0, ...))` for a test that does not parse | (line removed) | red |  |
| 8 | `_read_tree` | `if not in_corpus(path):` | `if False:` | survived | survived |
| 9 | `_read_tree` | `unread.append((path, 0, ...))` for a document that does not decode | (line removed) | red |  |
| 10 | `_section_text` | `return None, why` | `return "", why` | red |  |
| 11 | `pins_and_copies_in` | `out += sources["unread"]` | (line removed) | red |  |
| 12 | `pins_and_copies_in` | `taken, at = op.old, op.lines["from"][0][0]` | `taken, at = op.old, op.line` | red |  |
| 13 | `pins_and_copies_in` | `elif op.kind == "remove":` | `elif op.kind == "removed":` | red |  |
| 14 | `pins_and_copies_in` | `gone.setdefault(op.file, []).append((taken, op.new))` | `gone.setdefault(op.file, [])` | red |  |
| 15 | `pins_and_copies_in` | `elif op.kind == "add" and op.new:` | `elif False:` | red |  |
| 16 | `pins_and_copies_in` | `rules.pins(op, taken, sources["literals"])` | `rules.pins(op, taken, [])` | red |  |
| 17 | `rule_changes_read` | `rel = f"{item}/{OPTIN.DESIGN}"` | `rel = f"{item}/frame/plan.md"` | red |  |
| 18 | `rule_changes_read` | `for line, why in parsed.unread` | `for line, why in []` | red |  |
| 19 | `rule_changes_read` | `for line, reason in parsed.errors` | `for line, reason in parsed.errors[:0]` | red |  |
| 20 | `rule_changes_read` | `if notices is not None:` | `if notices is None:` | red |  |
| 21 | `rule_changes_of` | `return None` | `return []` | red |  |
| 22 | `rule_changes_of` | `except (OSError, SyntaxError, ImportError, SystemExit) as exc:` | `except (OSError, SyntaxError, SystemExit) as exc:` | red |  |
| 23 | `edited_work_items` | `and p not in moved` | `and True` | red |  |
| 24 | `edited_work_items` | `and carried_by(root, base, p) is None` | `and True` | red |  |
| 25 | `edited_work_items` | `and len(p.split("/")) == depth` | `and True` | red |  |
| 26 | `originals_of` | `if text is None or not (items or direct):` | `if text is None or not items:` | red |  |
| 27 | `originals_of` | `if not gate.touches_code(paths, home):` | `if False:` | red |  |
| 28 | `originals_of` | `if sha is None:` | `if sha is None and False:` | red |  |
| 29 | `originals_of` | `found.extend(guarantee_original(said, rel, sha, config))` | `found.extend(original_of(said, rel, sha, config))` | red |  |
| 30 | `originals_of` | `except (OSError, SyntaxError, ImportError, SystemExit) as exc:` | `except (OSError, SyntaxError, SystemExit) as exc:` | red |  |
| 31 | `broad_gate` | `runs, problems = blocks_of(rel, text, FIELDS.GATE, notices)` | `runs, problems = blocks_of(rel, text, FIELDS.GATE, None)` | red |  |
| 32 | `broad_gate` | `sha = runs[-1].fields[FIELDS.RUN]` | `sha = runs[0].fields[FIELDS.RUN]` | red |  |
| 33 | `broad_gate` | `return [(rel, 0, follows_reason(behind, "the newest gate run"))]` | `return []` | red |  |
| 34 | `broad_gate` | `return [(rel, 0, NO_RUN_BLOCK)]` | `return []` | red |  |
| 35 | `broad_gate` | `return [` "git carries no gate record" ... | `return []` before it | red |  |
| 36 | `guarantee` | `return [` "git carries no guarantee file" ... | `return []` before it | red |  |
| 37 | `guarantee` | `verdicts, problems = blocks_of(rel, text, FIELDS.GUARANTEE, notices)` | `verdicts, problems = blocks_of(rel, text, FIELDS.GUARANTEE, None)` | red |  |
| 38 | `guarantee` | `return [(rel, 0, NO_VERDICT_BLOCK)]` | `return []` | red |  |
| 39 | `guarantee` | `newest = verdicts[-1]` | `newest = verdicts[0]` | red |  |
| 40 | `guarantee` | `behind = follows(root, sha, base, item, only=CLOSING_RECORDS)` | `behind = follows(root, sha, base, item)` | red |  |
| 41 | `guarantee` | `if FIELDS.verdict_word(newest) != FIELDS.SEALED:` | `if False:` | red |  |
| 42 | `body` | `if text is None: return [], [("", 0, BODY_UNREAD` ... | `text = ""`, and the return skipped | red |  |
| 43 | `body` | `if len(holders) == 1 or (not holders and len(items) == 1):` | `if len(holders) >= 1 or (not holders and len(items) == 1):` | red |  |
| 44 | `body` | `split = BODY_SPLIT if holders else BODY_NONE_HOLDS` | `split = BODY_SPLIT` | red |  |
| 45 | `body` | `notices = [(item, 0, BODY_WHOLE.format(why=note))] if note else []` | `notices = []` | red |  |
| 46 | `body` | `BODY_LINE.format(line=line, why=said) if line` | `... if False` | red |  |
| 47 | `body` | `path = posixpath.normpath("/".join(p for p in (item, where) if p))` | `path = item` | red |  |
| 48 | `body` | `os.path.join(root, *item.split("/")), text, root, base=base` | `os.path.join(root, *item.split("/")), text, root, base=None` | red |  |
| 49 | `pull_request_body` | `return "", path` | `return None, path` | red |  |
| 50 | `pull_request_body` | `if not isinstance(text, str):` | `if False:` | red |  |
| 51 | `main` | `text, said = (None, BODY_WORKTREE) if WORKTREE else pull_request_body()` | `text, said = pull_request_body()` | red |  |
| 52 | `main` | `notices.extend((p, n, f"{BODY_SEALING_SAYS}: {m}") for p, n, m in found)` | `problems.extend(found)` | red |  |
| 53 | `main` | `found = rule_changes_of(root, [item], notices, sources)` | `found = rule_changes_of(root, [item], None, sources)` | red |  |
| 54 | `main` | `found = rule_changes_of(root, edited, notices, sources)` | `found = rule_changes_of(root, edited, None, sources)` | red |  |
| 55 | `main` | `if args.sealing and rel.endswith(f"/{OPTIN.GUARANTEE}"):` | `if False:` | red |  |
| 56 | `main` | `if found is None: return 2` after `originals_of` | `found = []` | red |  |
| 57 | `main` | `if found is None: return 2` after `rule_changes_of(root, edited, ...)` | `found = []` | red |  |

**2. Cases and seconds, before and after, on this macOS machine.** The figures are local. `frame/design.md` *Grounding*, *What a figure of the Windows leg can show*, takes no local figure as evidence of a saving on the Windows leg, and phase 2 closes no module, so no `workflow_dispatch` run follows it (`frame/plan.md` *Alternatives considered*, A11).

| Measure | Before, `a6f69fbba` | After, `36d15a994` |
|---|---|---|
| Cases of the module | 252 | 252 |
| Cases of the seven arm classes | 104 | 104 |
| `bin/test tests/skills/test_chain_check.py -q -p no:xdist`, the module | 111.3 s, of which 17.2 s setup | 62.1 s, of which 5.3 s setup |
| The same run, the seven arm classes | 73.9 s, of which 13.2 s setup | 20.0 s, of which 1.2 s setup |
| `bin/test tests/skills/test_chain_check.py -q`, under `-n auto` | not run | 14.4 s |
| Call sites of `main` in the arm classes | 91 | 31 |
| Windows leg, run 45181872904's `test-durations` artifact, the module | 601 s | not measured |
| The same artifact, the seven arm classes | 449 s | not measured |

The per-class figures of both local runs are in this phase's scratch, `before-noxdist.txt` and `after-noxdist.txt`, summed by `byclass.py`.

**Q2: the floor.** The module does not close in this phase, so the phase gives no answer to Q2 for it. After this phase, the arm classes still hold 31 `main` call sites, and `Test_main` with the other classes of phase 3 took 37.4 s of the local run before and 37.0 s after. Whether the module comes under 60 s on the Windows leg is read from the orchestrator's run at phase 3's Status commit (`frame/design.md` S1).

**3. The real-git cases kept.** Each case below runs `main` over a real repository, or reads a fact through git that a replaced reader would hide. The rest of the seven classes run no `main`.

- `Test_rule_changes_read`: `test_names_a_near_heading_in_another_work_items_spec_the_branch_edits` (1 run), `test_accepts_a_draft_or_an_unseen_pull_request_with_a_notice` (3), `test_refuses_the_spec_of_a_framer_drawn_frame_the_same_way` (1), `test_accepts_a_spec_another_pull_requests_squash_carried_unread` (3), `test_refuses_to_run_where_its_reader_will_not_load` (2), `test_refuses_another_work_items_spec_the_branch_adds_or_changes` (1), `test_refuses_another_work_items_spec_straight_to_the_pr` (1), `test_accepts_a_pull_request_that_declares_nothing_reading_no_spec` (1) and `test_accepts_a_spec_only_moved_and_a_file_beside_or_below_one` (1). Each judges which designs `main` hands the arm, through `edited_work_items`, `carried_by` and the pull request's state. `test_refuses_the_working_tree_under_worktree_and_reads_head_otherwise` runs no `main` and keeps one commit, so that the design at HEAD and the one in the working tree differ.
- `Test_check_lines_in`: `test_refuses_a_line_the_reader_refuses_at_its_line_in_the_design` (1 run).
- `Test_pins_and_copies_in`: `test_names_a_pin_at_the_froms_line_and_no_docstring_or_three_words` (2 runs, the second under `GITHUB_ACTIONS`).
- `Test_originals_of`: `test_refuses_a_record_with_no_original_line_on_a_ready_pull_request` (2 runs, ready and draft), `test_refuses_to_run_where_the_parity_readers_will_not_load` (1) and `test_refuses_a_direct_guarantee_with_no_original_line_and_accepts_one` (2, ready and `--sealing`).
- `Test_guarantee`: `test_names_a_near_opener_and_reads_no_verdict` (1 run) and `test_a_verdict_other_than_sealed_fails_a_ready_pull_request` (3 runs: ready, `--sealing` and draft). `test_refuses_absent_unfilled_and_behind_head_by_name` runs no `main` and keeps one commit, since `follows` reads the commits after the verdict from git.
- `Test_broad_gate`: no `main` run, as at the base (*Departures from the frame*). `test_lets_the_records_follow_the_run_and_refuses_any_other_path` keeps its two commits, since `follows` reads them from git.
- `Test_body`: `test_refuses_a_body_sent_before_the_seal_at_the_mark`, `test_accepts_the_body_at_a_merge_past_a_later_base_commit`, `test_prints_the_refusal_on_a_draft_and_exits_0`, `test_names_the_body_as_not_read_under_worktree` and `test_prints_a_difference_as_a_notice_under_sealing`, 1 run each.

These are the 31 call sites of `main` the census counts.

**4. Old cases cut or rewritten.** No case was cut. Each case below was rewritten. Its name and its facts are as they were, and what changed is how its input reaches the arm. Where a fact the case asserted through `main` now stands in another case, the line names that case. A count of commit helper calls counts calls of `commit`, `put_spec`, `planted_spec`, `reviewed_to_head` and `migrating` in the case's body (`census.py`).

- `Test_rule_changes_read::test_refuses_a_section_the_parser_refuses_at_its_line`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` over `_branch_template`.
- `Test_rule_changes_read::test_accepts_a_section_that_parses_or_no_section`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` over `_branch_template`.
- `Test_rule_changes_read::test_names_a_near_heading_as_not_read_and_passes`: 2 `main` runs and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` over `_branch_template`.
- `Test_rule_changes_read::test_names_a_near_heading_beside_a_refusal_and_keeps_the_refusal`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` over `_branch_template`.
- `Test_rule_changes_read::test_refuses_the_working_tree_under_worktree_and_reads_head_otherwise`: 2 `main` runs and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` over a `branch` copy.
- `Test_rule_changes_read::test_refuses_to_run_where_its_reader_will_not_load`: 3 `main` runs and 3 commit helper calls over a `branch` copy before; it now keeps 2 `main` runs over a `branch` copy and calls `rule_changes_of` for the reader that will not load.
- `Test_check_lines_in::test_accepts_a_line_the_reader_holds_and_prints_nothing`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` over `_branch_template`, which reads the check lines.
- `Test_check_lines_in::test_refuses_a_target_that_is_no_file_of_the_repository`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` over `_branch_template`, which reads the check lines.
- `Test_check_lines_in::test_refuses_a_line_on_the_field_line_at_the_field_line`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` over `_branch_template`, which reads the check lines.
- `Test_check_lines_in::test_names_a_near_line_as_not_read_at_its_line_and_passes`: 2 `main` runs and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` over `_branch_template`, which reads the check lines.
- `Test_check_lines_in::test_reads_the_to_of_an_add_as_of_a_change`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` over `_branch_template`, which reads the check lines.
- `Test_check_lines_in::test_reads_no_check_line_in_a_from`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` over `_branch_template`, which reads the check lines.
- `Test_check_lines_in::test_ends_at_exit_2_where_its_reader_will_not_load_or_read`: 2 `main` runs and 2 commit helper calls over a `branch` copy before; it now calls `rule_changes_of` over a `branch` copy and reads its `None` and the line it prints.
- `Test_pins_and_copies_in::test_accepts_a_to_that_keeps_the_literal_naming_nothing`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` under `WORKTREE` over a `branch` copy, which reads the pins and copies.
- `Test_pins_and_copies_in::test_names_a_pin_in_a_section_a_remove_takes_out_whole`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` under `WORKTREE` over a `branch` copy, which reads the pins and copies.
- `Test_pins_and_copies_in::test_names_a_copy_at_the_tos_line_and_no_run_of_fourteen`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` under `WORKTREE` over a `branch` copy, which reads the pins and copies.
- `Test_pins_and_copies_in::test_refuses_to_name_a_copy_landing_in_a_korean_edition`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` under `WORKTREE` over a `branch` copy, which reads the pins and copies.
- `Test_pins_and_copies_in::test_names_a_test_file_that_does_not_parse_as_not_read`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` under `WORKTREE` over a `branch` copy, which reads the pins and copies.
- `Test_pins_and_copies_in::test_names_a_rule_document_that_does_not_decode_as_not_read`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` under `WORKTREE` over a `branch` copy, which reads the pins and copies.
- `Test_pins_and_copies_in::test_names_a_copy_a_change_keeps_in_its_to`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` under `WORKTREE` over a `branch` copy, which reads the pins and copies.
- `Test_pins_and_copies_in::test_names_a_passage_two_adds_of_one_design_put_in_two_documents`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` under `WORKTREE` over a `branch` copy, which reads the pins and copies.
- `Test_pins_and_copies_in::test_accepts_a_passage_the_design_moves_naming_no_copy`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` under `WORKTREE` over a `branch` copy, which reads the pins and copies.
- `Test_pins_and_copies_in::test_names_a_section_a_remove_cannot_read_as_not_read`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` under `WORKTREE` over a `branch` copy, which reads the pins and copies.
- `Test_pins_and_copies_in::test_names_a_test_and_a_document_it_cannot_open_as_not_read`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` under `WORKTREE` over a `branch` copy, which reads the pins and copies.
- `Test_pins_and_copies_in::test_names_a_test_the_parser_gives_up_on_as_not_read`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` under `WORKTREE` over a `branch` copy, which reads the pins and copies.
- `Test_pins_and_copies_in::test_names_a_listing_git_could_not_make_as_not_read`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `rule_changes_read` under `WORKTREE` over a `branch` copy, which reads the pins and copies.
- `Test_originals_of::test_accepts_a_record_naming_the_baseline_by_either_prefix`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `originals_of` over `_branch_template`.
- `Test_originals_of::test_refuses_a_record_naming_another_commit_naming_both`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now calls `originals_of` over `_branch_template`.
- `Test_originals_of::test_refuses_a_config_whose_baseline_holds_no_commit`: 1 `main` run and 2 commit helper calls over a `branch` copy before; it now calls `originals_of` over `_branch_template`.
- `Test_originals_of::test_accepts_a_change_confined_to_the_document_roots`: 0 `main` runs and 1 commit helper call over a `branch` copy before; it now calls `originals_of` over `_branch_template` with 0 commit helper calls, its record handed through `reading` or the copy's tree.
- `Test_originals_of::test_refuses_to_run_where_the_parity_readers_will_not_load`: 1 `main` run and 1 commit helper call over a `branch` copy before; it now keeps 1 `main` run over `_branch_template` with 0 commit helper calls.
- `Test_originals_of::test_refuses_a_direct_guarantee_with_no_original_line_and_accepts_one`: 4 `main` runs and 3 commit helper calls over an `item` copy before; it now keeps 2 `main` runs over `_item_template` and calls `originals_of` for the rest.
- `Test_originals_of::test_refuses_a_direct_guarantee_whose_only_original_is_misspelt`: 2 `main` runs and 2 commit helper calls over an `item` copy before; it now calls `originals_of` over `_item_template`.
- `Test_originals_of::test_a_missing_guarantee_is_named_once`: 1 `main` run and 2 commit helper calls over an `item` copy before; it now calls `originals_of` over `_item_template`.
- `Test_originals_of::test_a_direct_guarantee_owes_nothing_for_the_document_roots_alone`: 2 `main` runs and 2 commit helper calls over an `item` copy before; it now calls `originals_of` over `_item_template`.
- `Test_originals_of::test_owes_no_original_line_where_none_is_owed`: 3 `main` runs and 3 commit helper calls over an `item` copy before; it now calls `originals_of` over `_item_template`.
- `Test_guarantee::test_accepts_a_sealed_verdict_at_head`: 0 `main` runs and 0 commit helper calls over an `item` copy before; it now calls `guarantee` over `_item_template` with 0 commit helper calls, its record handed through `reading` or the copy's tree.
- `Test_guarantee::test_accepts_the_newest_of_two_runs`: 1 `main` run and 2 commit helper calls over an `item` copy before; it now calls `guarantee` over `_item_template`. Its `main` run asserted exit 0 over a sealed guarantee, which `Test_originals_of::test_refuses_a_direct_guarantee_with_no_original_line_and_accepts_one` still asserts over the same template, so the older run is `HEAD~2` of the template and no run of `main` is left in this case.
- `Test_guarantee::test_refuses_absent_unfilled_and_behind_head_by_name`: 0 `main` runs and 4 commit helper calls over an `item` copy before; it now calls `guarantee` over an `item` copy with 1 commit helper call, its record handed through `reading` or the copy's tree.
- `Test_guarantee::test_refuses_a_guarantee_of_the_old_shape_naming_the_template`: 0 `main` runs and 1 commit helper call over an `item` copy before; it now calls `guarantee` over `_item_template` with 0 commit helper calls, its record handed through `reading` or the copy's tree.
- `Test_guarantee::test_refuses_a_fence_nobody_closed_between_two_runs`: 0 `main` runs and 1 commit helper call over an `item` copy before; it now calls `guarantee` over `_item_template` with 0 commit helper calls, its record handed through `reading` or the copy's tree.
- `Test_guarantee::test_an_opener_quoted_in_a_code_span_hides_no_verdict`: 0 `main` runs and 1 commit helper call over an `item` copy before; it now calls `guarantee` over `_item_template` with 0 commit helper calls, its record handed through `reading` or the copy's tree.
- `Test_guarantee::test_refuses_a_comment_line_at_its_line`: 0 `main` runs and 1 commit helper call over an `item` copy before; it now calls `guarantee` over `_item_template` with 0 commit helper calls, its record handed through `reading` or the copy's tree.
- `Test_guarantee::test_refuses_a_near_miss_of_the_verdict_at_its_line`: 0 `main` runs and 1 commit helper call over an `item` copy before; it now calls `guarantee` over `_item_template` with 0 commit helper calls, its record handed through `reading` or the copy's tree.
- `Test_guarantee::test_refuses_a_line_that_opens_like_the_verdict_at_its_line`: 0 `main` runs and 1 commit helper call over an `item` copy before; it now calls `guarantee` over `_item_template` with 0 commit helper calls, its record handed through `reading` or the copy's tree.
- `Test_guarantee::test_names_a_near_opener_and_reads_no_verdict`: 1 `main` run and 1 commit helper call over an `item` copy before; it now keeps 1 `main` run over `_item_template` with 0 commit helper calls.
- `Test_guarantee::test_a_verdict_other_than_sealed_fails_a_ready_pull_request`: 4 `main` runs and 1 commit helper call over an `item` copy before; it now keeps 3 `main` runs over an `item` copy and calls `guarantee` for the rest.
- `Test_broad_gate::test_accepts_a_run_at_head`: 0 `main` runs and 0 commit helper calls over an `item` copy before; it now calls `broad_gate` over `_item_template` with 0 commit helper calls, its record handed through `reading` or the copy's tree.
- `Test_broad_gate::test_accepts_the_last_run_block_as_the_newest`: 0 `main` runs and 2 commit helper calls over an `item` copy before; it now calls `broad_gate` over `_item_template` with 0 commit helper calls, its record handed through `reading` or the copy's tree.
- `Test_broad_gate::test_refuses_a_comment_line_at_its_line`: 0 `main` runs and 1 commit helper call over an `item` copy before; it now calls `broad_gate` over `_item_template` with 0 commit helper calls, its record handed through `reading` or the copy's tree.
- `Test_broad_gate::test_refuses_a_record_with_no_run_block_naming_the_command`: 0 `main` runs and 1 commit helper call over an `item` copy before; it now calls `broad_gate` over `_item_template` with 0 commit helper calls, its record handed through `reading` or the copy's tree.
- `Test_broad_gate::test_refuses_a_run_block_that_does_not_parse_at_its_line`: 0 `main` runs and 1 commit helper call over an `item` copy before; it now calls `broad_gate` over `_item_template` with 0 commit helper calls, its record handed through `reading` or the copy's tree.
- `Test_broad_gate::test_names_a_near_opener_as_not_read`: 0 `main` runs and 1 commit helper call over an `item` copy before; it now calls `broad_gate` over `_item_template` with 0 commit helper calls, its record handed through `reading` or the copy's tree.
- `Test_body::test_refuses_a_body_sent_before_the_seal_at_the_mark`: 1 `main` run and 0 commit helper calls over a `bodied` copy before; it now keeps 1 `main` run over `_bodied_template` with 0 commit helper calls.
- `Test_body::test_accepts_the_body_composed_after_the_seal`: 1 `main` run and 0 commit helper calls over a `bodied` copy before; it now calls `body` over `_bodied_template`.
- `Test_body::test_refuses_the_mark_where_the_row_gives_none`: 2 `main` runs and 2 commit helper calls over a `bodied` copy before; it now calls `body` over a `bodied` copy.
- `Test_body::test_accepts_a_folded_body_naming_the_fold`: 2 `main` runs and 0 commit helper calls over a `bodied` copy before; it now calls `body` over a `bodied` copy.
- `Test_body::test_refuses_a_drifted_body_at_its_line`: 1 `main` run and 0 commit helper calls over a `bodied` copy before; it now calls `body` over `_bodied_template`.
- `Test_body::test_refuses_a_null_body_as_an_empty_one`: 1 `main` run and 0 commit helper calls over a `bodied` copy before; it now calls `body` over `_bodied_template`.
- `Test_body::test_prints_the_refusal_on_a_draft_and_exits_0`: 1 `main` run and 0 commit helper calls over a `bodied` copy before; it now keeps 1 `main` run over `_bodied_template` with 0 commit helper calls.
- `Test_body::test_names_the_body_as_not_read_where_the_payload_gives_none`: 1 `main` run and 0 commit helper calls over a `bodied` copy before; it now calls `body` over `_bodied_template`.
- `Test_body::test_names_the_body_as_not_read_with_no_payload`: 1 `main` run and 0 commit helper calls over a `bodied` copy before; it now calls `body` over `_bodied_template`.
- `Test_body::test_names_the_body_as_not_read_under_worktree`: 1 `main` run and 0 commit helper calls over a `bodied` copy before; it now keeps 1 `main` run over `_bodied_template` with 0 commit helper calls.
- `Test_body::test_prints_a_difference_as_a_notice_under_sealing`: 1 `main` run and 0 commit helper calls over a `bodied` copy before; it now keeps 1 `main` run over `_bodied_template` with 0 commit helper calls.
- `Test_body::test_names_the_body_as_not_read_for_two_work_items_with_pr_md`: 1 `main` run and 1 commit helper call over a `bodied` copy before; it now calls `body` over `_bodied_template`.
- `Test_body::test_names_the_body_as_not_read_for_two_work_items_without_pr_md`: 1 `main` run and 1 commit helper call over a `bodied` copy before; it now calls `body` over `_bodied_template`.
- `Test_body::test_refuses_a_missing_pr_md_at_its_path`: 1 `main` run and 1 commit helper call over a `bodied` copy before; it now calls `body` over a `bodied` copy.
- `Test_body::test_refuses_a_repository_without_a_language_row_at_its_config`: 1 `main` run and 1 commit helper call over a `bodied` copy before; it now calls `body` over a `bodied` copy.
- `Test_body::test_reads_the_translation_as_the_bodys_first_lines`: 2 `main` runs and 2 commit helper calls over a `bodied` copy before; it now calls `body` over a `bodied` copy.

No case of the seven classes reads a document's prose as its fact, so none is left in place for that. `test_refuses_a_section_the_parser_refuses_at_its_line[S3-the-template-section]` reads `templates/records/sdd-design.md` only to build its input, and it calls the arm.

### Checks at the phase's close

- `bin/test tests/skills/test_chain_check.py -q -p no:xdist --durations=0` at `36d15a994`'s tree: 252 passed in 62.11 s (executed, file order).
- `bin/test tests/skills/test_chain_check.py -q`: 252 passed in 14.36 s (executed, under `-n auto`).
- `bin/seal layout --check tests/skills/test_chain_check.py`: exit 0, `seal layout: 1 files read, 0 refused, 0 declare no TARGET` (executed). It also prints 34 `report:` lines, each a function of `chain_check.py` with no class of its own name. A report line refuses nothing, and the phase adds and removes no class.
- The *Phase boundary* set, `bin/test tests/skills/test_chain_check.py tests/behaviour tests/text -q`: 1127 passed, 9 skipped (executed). `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` names a case of the changed file, and it is in that set.
- `uvx ruff format` and `uvx ruff check` over the changed file: clean (executed).
- The suite: `unverified`. The broad gate is the orchestrator's, once the review rounds settle.
