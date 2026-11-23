# Phase 3: 1795439973-six-test-modules-cost-past-the-rewrite-bound

## What this phase found

### The frame, read against the tree before the build

The frame holds for the classes phase 2 did not rebuild, with two facts it did not state. Read at `0a10cc89a`: the module's other classes are `Test_main`, `Test_retired`, `Test_routing_trailers`, `Test_declared_for_this_branch`, the readers of text (`Test_round_of`, `Test_record_findings`, `Test_channel` and their neighbours), the readers that ask git (`Test_changed`, `Test_carried_by`, `Test_follows`, `Test_frame`) and the git predicates `#1482` moved here. The predicates already read worlds `tests/skills/test_unverified_check.py` builds once, so they meet `frame/design.md` G2 as they stand.

- **Six `Test_main` cases build their repository through `tests/conftest.py`, per case.** They take `package`, `shared` or `declared`, and `package` and `shared` are function-scoped fixtures of `tests/conftest.py` (`:1205`, `:1219`). Each of the nine instances runs `git init` and two or three commits before its own commit and its `main` run. The spawn bars `tests/conftest.py`, so the phase left them, and `gaps.md` *Not done* names the change.
- **`Test_declared_for_this_branch` started a Python process for each of its five `main` runs.** `run_check` ran the script under `subprocess.run`. The frame did not name that cost.

### Q1: where the other classes' seconds went before the rebuild

`bin/test tests/skills/test_chain_check.py -q -p no:xdist --durations=0` at `0a10cc89a` passed 252 cases in 59.3 s on this macOS machine (executed). The classes of this phase took 37.1 s of the 57.2 s the cases summed, 4.0 s of it in setup. `Test_main` took 24.6 s over 39 cases, `Test_retired` 4.5 s over 8, `Test_routing_trailers` 3.0 s over 8 and `Test_declared_for_this_branch` 1.4 s over 9. Every other class took under 1 s.

The seconds were `main` runs and the commits a case made before it (read from the profile and the case bodies). An `ast` census of the classes counted 64 call sites of `main` (`check`, `chain.main`, `checked`, `run_check`) and 91 call sites of a helper that commits (`census.py` in this phase's scratch, executed at both commits). Most `Test_main` cases whose fact is a round record wrote the record, committed it, committed the closing records again with `seal`, and ran `main` two or three times to read it.

### What the rebuild changed

All of it is in `21ad4adc2`.

- **The records arm is called in the process.** A case whose fact is how `records` or `unread` reads the round records calls them through `records_read`. That helper hands the records over through `reading`. Where a case needs another set of rounds, it also replaces `round_records` with the list it gives. Only the commits a verdict or a `target:` names are real, since `is_ancestor`, `touched` and `follows` read them from git.
- **A `main` run that reads a record takes the template.** `main` without `--worktree` writes nothing into the repository it reads: `changed` runs `diff` and `hash-object` without `-w`, and the one `git status`, in `carried_by`, runs only under `WORKTREE` (read: `chain_check.py#changed`, `#carried_by`). So a run whose record reaches it through `reading` takes `_branch_template` with no copy and no commit. This covers the draft run of the open finding, the two runs that print a not-read line, the broad gate's `--sealing` run and the run straight to the pull request. No run under `--worktree` takes a template.
- **The trailer cases about which commits git lists read `routing_trailers` alone.** These are the old key, a co-author trailer, a merge with a GitHub squash, and a cherry-pick by another committer. The `undeclared` branch is built once for the module (`_undeclared_template`) and copied per case.
- **The frame arm's three cases hand it the design and the plan through `reading`** over the template, and `Test_follows::test_accepts_head_and_record_commits_after_it` takes the template, since it writes nothing.
- **`Test_declared_for_this_branch` runs `main` in the process.** `run_check` now calls `chain.main` under `--worktree`. It holds `WORKTREE` through `monkeypatch`, so the next case starts from the module's own value (`frame/plan.md` *Technical context*). The case `Test_module::test_a_script_copied_alone_exits_2_and_names_what_it_misses` still runs the script as a command.
- **The census counts 42 call sites of `main` and 48 of a commit helper** in these classes, against 64 and 91 at the base (executed). A loop counts once.

### Departures from the frame

- **`records_read` replaces `round_records`, a reader the frame does not list.** `frame/plan.md` *Technical context* names `read_record`, `git`, `_tracked` and `sources` as seams. A case whose last record is round 1 needs the arm to read one round where HEAD carries two, and `read_record` cannot remove a file from the listing. *Alternatives considered* A4 replaces "the reader one level up", and the listing is that. The listing from git stays held by cases that read it: `test_refuses_a_chain_with_no_record_and_prints_it_on_a_draft` through `main`, and `test_names_a_record_under_another_name_and_keeps_the_exit` through `unread` over a real commit. Mutants 11, 13 and 51 are red.
- **`Test_retired` and the six `Test_main` cases over `tests/conftest.py`'s repositories keep their worlds as they stood.** Each runs `main`, and its fact is what `main` makes of a removed declaration or of a root at `agentic-seal/`. `Test_retired`'s history differs in each case by its parameters: an open row or none, the rule applied or not, the directory removed whole or in part. One world built once would merge those parameters, and its five cases are fewer than the workers that would each build it (`frame/plan.md` *Technical context*). `gaps.md` *Not done* names both.
- **A draft's fact moved to the case that keeps the run.** `test_refuses_a_last_records_fixed_finding_owing_a_verifying_round` asserted that a draft prints the refusal and passes. Its draft run went. That fact is `main`'s, and it stands in `test_refuses_an_open_finding_on_a_ready_pull_request`'s draft run and in `test_refuses_a_chain_with_no_record_and_prints_it_on_a_draft`. Run alone against mutant 77, which judges a draft as ready, each of the two is red (executed). Mutant 78, which prints a draft's refusals as errors, is red in the module run. Run against the whole module with `-p no:xdist`, it fails one case alone, `Test_rule_changes_read::test_accepts_a_draft_or_an_unseen_pull_request_with_a_notice` (executed). Whether more cases held it at the base was not run.

### The four parts `CONTRIBUTING.md` *The test layout* asks of a rebuilt module

**1. The move check, and the mutation table.**

`bin/seal layout --moved 0a10cc89a --from tests/skills/test_chain_check.py --to tests/skills/test_chain_check.py` exits 1 (executed). Its last line reads `seal layout: moved: 206 old cases, 251 items against 251 at 0a10cc89a734, 65 failed`. So the mutation table carries part 1. The module's table is phase 2's 57 mutants (`trail/phases/phase-2.md`, its first part) and the 85 below.

The mutants sit at the decision points of the functions this phase's classes judge, and at the lines of `main` that hand each arm its input and read its answer. All 85 ran in one call against `21ad4adc2` (executed): `bin/seal mutate skills/code-review/scripts/chain_check.py --replace OLD NEW ... --tests "bin/test tests/skills/test_chain_check.py -q -x"`, built by `run_mutants.py` from `mutants.py` in this phase's scratch. It printed `seal mutate: 85 mutants, 75 red, 10 SURVIVED, 0 with no verdict (880.2s)`. Each row shows the lines the mutant changes, joined. The full OLD and NEW of each are in `mutants.py`.

The base columns are filled for a survivor alone. The ten survivors ran again against the test file at `0a10cc89a`, copied to `tests/skills/test_tmp_chain_check_base.py`, and against the file at `a6f69fbba`, before phase 2, copied to `tests/skills/test_tmp_chain_check_a6f.py`. Each copy was removed after its run. Both calls printed `10 mutants, 0 red, 10 SURVIVED` (executed). So each survivor is a gap older than both phases, and neither phase lost a fact that killed it. Why each lives:

- 1: no `main` run follows a base that moved past the fork, so the two-dot and three-dot diffs agree.
- 7: each case's release squashes one commit, so the newest and the oldest are one.
- 9, 10: no case puts a link or a submodule under `trail/rounds/`.
- 12: git lists `round-1.md` before `round-2.md`, and no case holds ten rounds.
- 16: no case writes a payload whose `draft` is not a boolean.
- 39, 52: no case's finding is located in the records alone while its commit also touched code. The case that touches code beside the records also names `f.txt` in its location, so `located_in_records` refuses it first.
- 43: no case reads the reason `follows` gives for a commit HEAD does not descend from. The refusal of a `fixed` commit off the branch is `verdict_problems`'s own sentence.
- 70: `os.walk` over the fixtures gives the order the sort gives.

The phase adds no case for them, as phase 2 added none for its mutant 8: the frame rebuilds the existing cases (`frame/design.md` *Scope* item 3), and `agents/crafter.md` *Never* bars building beyond the request. `gaps.md` *Not done* names the ten.

| # | Unit | Old | New | New file | `0a10cc89a` | `a6f69fbba` |
|---|---|---|---|---|---|---|
| 1 | `changed` | `f"{base}...HEAD"` | `f"{base}..HEAD"` | survived | survived | survived |
| 2 | `changed` | `if meta[4] == "D":` | `if meta[4] == "X":` | red |  |  |
| 3 | `changed` | `if blob in same_name: moved.update` | `if False: moved.update` | red |  |  |
| 4 | `changed` | `untracked = git(root, "ls-files", "--others", "--exclude-standard", "-z")` | `untracked = ""` | red |  |  |
| 5 | `changed_routing` | `and p not in moved )` | `and True )` | red |  |  |
| 6 | `carried_by` | `or entry[1].strip().lower() != SQUASH_COMMITTER` | (line removed) | red |  |  |
| 7 | `carried_by` | `return commits[0][0].strip(), commits[0][2].strip()` | `return commits[-1][0].strip(), commits[0][2].strip()` | survived | survived | survived |
| 8 | `carried_by` | `if dirty is None or dirty.strip(): return None` | `if dirty is None: return None` | red |  |  |
| 9 | `tracked_files` | `if len(parts) >= 3 and parts[0] in REGULAR: names.append` | `if len(parts) >= 3: names.append` | survived | survived | survived |
| 10 | `worktree_files` | `and not os.path.islink(os.path.join(base, n))` | (line removed) | survived | survived | survived |
| 11 | `rounds_listed` | `others.append(f"{where}/{name}")` | `pass` | red |  |  |
| 12 | `rounds_listed` | `return [rel for _, rel in sorted(found)], sorted(others)` | `return [rel for _, rel in found], sorted(others)` | survived | survived | survived |
| 13 | `unread` | `found += [ (rel, 0, UNREAD_FILE` | `found += [] and [ (rel, 0, UNREAD_FILE` | red |  |  |
| 14 | `unread` | `blocks_of(rel, read_record(root, rel) or "", FIELDS.ROUND_RECORD, found)` | `pass` | red |  |  |
| 15 | `pull_request_state` | `return ("draft" if pr["draft"] else "ready"), path` | `return ("ready" if pr["draft"] else "ready"), path` | red |  |  |
| 16 | `pull_request_state` | `if not isinstance(pr["draft"], bool):` | `if False:` | survived | survived | survived |
| 17 | `pull_request_from_gh` | `` return ("draft" if draft else "ready"), "`gh pr view --json isDraft`" `` | `` return "ready", "`gh pr view --json isDraft`" `` | red |  |  |
| 18 | `pull_request_from_gh` | `return "unknown", f"{NO_PAYLOAD}, and {unrun.line}"` | `return "unknown", f"{NO_PAYLOAD}"` | red |  |  |
| 19 | `issue_of` | `found = ISSUE_RE.fullmatch(home or "")` | `found = ISSUE_RE.search(home or "")` | red |  |  |
| 20 | `location_paths` | `` return [item.strip("`").split(":")[0] for item in value.split(", ")] `` | `` return [item.strip("`") for item in value.split(", ")] `` | red |  |  |
| 21 | `round_read` | `if not rounds and not errors:` | `if False:` | red |  |  |
| 22 | `round_read` | `errors += [(rel, extra.line, SECOND_ROUND) for extra in rounds[1:]]` | `errors += []` | red |  |  |
| 23 | `round_read` | `if number is None or number in numbers:` | `if number is None:` | red |  |  |
| 24 | `round_read` | `if k is not None and why not in NOT_A_BLOCK_LINE: spoilt.add(k)` | `if k is not None: spoilt.add(k)` | red |  |  |
| 25 | `round_read` | `if blind is not None and block.line > blind: continue` | `if False: continue` | red |  |  |
| 26 | `finding_of` | `if not finds: errors.append` | `if False: errors.append` | red |  |  |
| 27 | `finding_of` | `paths += location_paths(closed[FIELDS.LOCATION].value)` | `pass` | red |  |  |
| 28 | `finding_of` | `kind, line = (OPEN, None), first + 1` | `kind, line = (DEFERRED, None), first + 1` | red |  |  |
| 29 | `round_of` | `target = block.fields[FIELDS.TARGET].match["commit"] if block else None` | `target = None` | red |  |  |
| 30 | `channel` | `if k == 0: why = (` | `if False: why = (` | red |  |  |
| 31 | `channel` | `elif n >= here.number or n not in by_number:` | `elif n not in by_number:` | red |  |  |
| 32 | `channel` | `elif m is not None and m not in by_number[n].held:` | `elif False:` | red |  |  |
| 33 | `channel` | `owed = f.verdict[0] in (FIXED, REJECTED)` | `owed = f.verdict[0] == FIXED` | red |  |  |
| 34 | `channel` | `f.verdict[0] == FIXED and not read_at_head(f)` | `f.verdict[0] == FIXED` | red |  |  |
| 35 | `channel` | `if f.verdict[0] == REJECTED or (` | `if False or (` | red |  |  |
| 36 | `touched` | `root, "diff-tree", "--no-commit-id", "--name-only", "-r", "--root", "-z", commit` | `root, "diff-tree", "--no-commit-id", "--name-only", "-r", "-z", commit` | red |  |  |
| 37 | `under` | `return path == stem or path.startswith(f"{stem}/")` | `return path == stem or path.startswith(stem)` | red |  |  |
| 38 | `located_in_records` | `return bool(f.paths) and all(under(q, item) for q in f.paths)` | `return bool(f.paths) and any(under(q, item) for q in f.paths)` | red |  |  |
| 39 | `records_only` | `return bool(changed) and all(under(p, item) for p in changed)` | `return bool(changed) and any(under(p, item) for p in changed)` | survived | survived | survived |
| 40 | `follows` | `if not GITCMD.is_ancestor(root, full, "HEAD"): return ("off", sha, "")` | `if False: return ("off", sha, "")` | red |  |  |
| 41 | `follows` | `root, "rev-list", "--reverse", "--no-merges", "HEAD", f"^{full}", f"^{base}"` | `root, "rev-list", "--reverse", "--no-merges", "HEAD", f"^{full}"` | red |  |  |
| 42 | `follows` | `if not path.startswith(f"{item}/") or (` | `if False or (` | red |  |  |
| 43 | `follows_reason` | `` return f"{what} names `{sha}`, which HEAD does not descend from" `` | `` return f"{what} names `{sha}`, which this repository cannot resolve" `` | survived | survived | survived |
| 44 | `frame_foot` | `r = REFRAME_RE.match(line) if r:` | `r = REFRAME_RE.match(line) if False:` | red |  |  |
| 45 | `frame` | `if read_record(root, f"{item}/{OPTIN.PLAN}") is None:` | `if False:` | red |  |  |
| 46 | `frame` | `elif mark[1] != routing.BY_FRAMER:` | `elif False:` | red |  |  |
| 47 | `frame` | `if by != routing.BY_FRAMER:` | `if False:` | red |  |  |
| 48 | `verdict_problems` | `if kind == OPEN: return [(path, f.line,` | `if False: return [(path, f.line,` | red |  |  |
| 49 | `verdict_problems` | `if not GITCMD.is_ancestor(root, commit, "HEAD"): return [` | `if False: return [` | red |  |  |
| 50 | `verdict_problems` | `if any(under(p, q) for p in changed_paths for q in f.paths):` | `if changed_paths:` | red |  |  |
| 51 | `records` | `if not found: return [ ( rel,` | `if False: return [ ( rel,` | red |  |  |
| 52 | `records` | `located_in_records(item, f) and records_only(root, item, f.verdict[1])` | `located_in_records(item, f)` | survived | survived | survived |
| 53 | `records` | `if last.target is not None: behind = follows(root, last.target, base, item)` | `if False: behind = follows(root, last.target, base, item)` | red |  |  |
| 54 | `records` | `+ (f"; {VERIFYING_ROUND}" if behind[0] == "after" else ""),` | `+ "",` | red |  |  |
| 55 | `local_root` | `return "" if os.path.realpath(home) == os.path.realpath(shared) else home` | `return ""` | red |  |  |
| 56 | `root_name` | `name = optin.home_name_in(lambda rel: git(root, "show", f"{fork}:{rel}"))` | `pass` | red |  |  |
| 57 | `tracked_declarations` | `if os.path.basename(path) != routing.FILENAME: continue` | `if False: continue` | red |  |  |
| 58 | `declared_for_this_branch` | `if len(matching) > 1:` | `if False:` | red |  |  |
| 59 | `declared_for_this_branch` | `if home: return [], (` | `if False: return [], (` | red |  |  |
| 60 | `declared_for_this_branch` | `branch = os.environ.get("GITHUB_HEAD_REF") or routing.current_branch(root)` | `branch = routing.current_branch(root)` | red |  |  |
| 61 | `routing_trailers` | `"--no-merges", "--reverse",` | `"--reverse",` | red |  |  |
| 62 | `routing_trailers` | `if author.strip().lower() != committer.strip().lower(): continue` | `if False: continue` | red |  |  |
| 63 | `routing_trailers` | `f"key={TRAILER},valueonly,separator=%x1e)",` | `f"key=SpecSeal-Routing,valueonly,separator=%x1e)",` | red |  |  |
| 64 | `trailer_findings` | `if value == NO_WORK_ITEM:` | `if False:` | red |  |  |
| 65 | `trailer_findings` | `elif local:` | `elif False:` | red |  |  |
| 66 | `trailer_findings` | `elif value not in judged:` | `elif True:` | red |  |  |
| 67 | `commit_of` | `return (out or "").strip() or None` | `return (out or "") or None` | red |  |  |
| 68 | `merge_base` | `return (out or "").strip() or None` | `return (out or "") or None` | red |  |  |
| 69 | `settled` | `return {d for d in directories if tree_at(root, ref, d)}` | `return set(directories)` | red |  |  |
| 70 | `tree_at` | `dirs.sort()` | (line removed) | survived | survived | survived |
| 71 | `retired` | `gone = [d for d in gone if not os.path.isdir(os.path.join(root, d))]` | `gone = gone` | red |  |  |
| 72 | `_checked` | `if not resolves(root, args.baseline):` | `if False:` | red |  |  |
| 73 | `_checked` | `by = None if rel in own else carried_by(root, args.baseline, rel)` | `by = carried_by(root, args.baseline, rel)` | red |  |  |
| 74 | `_checked` | `gone = not os.path.lexists(os.path.join(root, home))` | `gone = not os.path.isdir(os.path.join(root, home))` | red |  |  |
| 75 | `_checked` | `gone = git(root, "ls-tree", "HEAD", "--", home) == ""` | `gone = not git(root, "ls-tree", "HEAD", "--", home)` | red |  |  |
| 76 | `_checked` | `said = PRINTED_TRAILERS if local else JUDGED_TRAILERS` | `said = JUDGED_TRAILERS` | red |  |  |
| 77 | `_checked` | `strict = state != "draft" and not unseen` | `strict = not unseen` | red |  |  |
| 78 | `_checked` | `kind = "error" if strict else "notice"` | `kind = "error"` | red |  |  |
| 79 | `_checked` | `if item in by_settle:` | `if False:` | red |  |  |
| 80 | `_checked` | `if declared["review"] == routing.CHAIN:` | `if True:` | red |  |  |
| 81 | `_checked` | `notices.extend(unread(routing, root, item, item in chained))` | `problems.extend(unread(routing, root, item, item in chained))` | red |  |  |
| 82 | `_checked` | `notices.extend((p, n, f"{SEALING_SAYS}: {m}") for p, n, m in gate)` | `problems.extend(gate)` | red |  |  |
| 83 | `_checked` | `if trailers is None:` | `if False:` | red |  |  |
| 84 | `_checked` | `if declarations and gone:` | `if False:` | red |  |  |
| 85 | `main` | `except GITCMD.Failed as unanswered: print(f"chain-check: {unanswered.line}", file=sys.stderr) return 2` | `except GITCMD.Failed as unanswered: raise` | red |  |  |

**2. Cases and seconds, before and after, on this macOS machine.** The figures are local. `frame/design.md` *Grounding*, *What a figure of the Windows leg can show*, takes no local figure as evidence of a saving on the Windows leg. Phase 3 closes the module, so its Windows figure is the orchestrator's `workflow_dispatch` run at this phase's Status commit (`frame/design.md` S1).

| Measure | Before, `0a10cc89a` | After, `21ad4adc2` |
|---|---|---|
| Cases of the module | 252 | 252 |
| `bin/test tests/skills/test_chain_check.py -q -p no:xdist`, the module | 59.3 s; the cases sum to 57.2 s, of which 5.2 s setup | 49.3 s; the cases sum to 47.1 s, of which 4.5 s setup |
| The same runs, this phase's classes | 37.1 s, of which 4.0 s setup | 25.9 s, of which 3.2 s setup |
| The same runs, the seven arm classes phase 2 rebuilt | 20.1 s | 21.2 s |
| `Test_main` | 24.6 s | 14.2 s |
| `bin/test tests/skills/test_chain_check.py -q`, under `-n auto` | not run | 11.5 s |
| Call sites of `main` in this phase's classes | 64 | 42 |
| Call sites of a commit helper in this phase's classes | 91 | 48 |
| Windows leg, run 45181872904's `test-durations` artifact, the module | 601 s | not measured |

The arm classes changed in no line between the two runs, and moved from 20.1 s to 21.2 s. That is this machine's spread between two runs of the same cases. `Test_declared_for_this_branch` moved from 1.4 s to 1.3 s: on this machine a Python process for each run cost little. The Windows leg is not shown by that. The per-class figures of both runs are in this phase's scratch, `before-byclass.txt` and `after-byclass.txt`, summed by phase 2's `byclass.py`.

**Q2: the floor.** The phase gives no answer to Q2 for this module, since no local figure is evidence of the Windows leg. After phases 2 and 3 the module holds 73 call sites of `main`, 31 in the arm classes and 42 in the rest. The cases that run them are listed in part 3, each with the fact that needs `main`. The orchestrator reads the module's figure at this phase's Status commit against the modules no phase changed in the same run, as `frame/design.md` *Grounding* says.

**3. The real-git cases kept.** The arm classes' cases are phase 2's part 3. Of this phase's classes, each case below runs `main`, and the number is its call sites.

- `Test_main`: `test_accepts_a_reviewed_branch_on_a_ready_pull_request` (1, the merged item's record is never opened), `test_refuses_a_git_that_did_not_answer_in_one_line` (1 in each of 10 instances), `test_refuses_an_open_finding_on_a_ready_pull_request` (1, a draft), `test_refuses_a_chain_with_no_record_and_prints_it_on_a_draft` (2), `test_names_a_line_it_did_not_read_as_a_notice_and_keeps_the_exit` (2, the line printed plain and as a CI notice), `test_refuses_a_broad_gate_file_naming_another_commit` (2, ready and `--sealing`), `test_refuses_a_straight_to_the_pr_item_without_the_sealers_two_files` (2), `test_refuses_an_unreadable_declaration_and_accepts_none` (2), `test_accepts_a_release_pull_request_leaving_a_squashed_item_to_its_own` (3), `test_refuses_a_baseline_that_does_not_resolve_with_exit_2` (1), and the six `test_s3_` cases over a root at `agentic-seal/` (7 over 9 instances). Each case's fact is which declarations and records `main` hands an arm, or what `main` makes of the arm's answer.
- `Test_retired`: every case (8 call sites over 8 instances). Each case's fact is what `main` makes of a removed declaration.
- `Test_routing_trailers`: `test_refuses_a_commit_naming_a_work_item_no_declaration_names` (2, ready and draft), `test_accepts_a_commit_naming_the_work_item_its_declaration_names` (1), `test_a_work_item_trailer_at_a_local_root_is_printed_not_refused` (1) and `test_refuses_to_run_where_the_commits_cannot_be_read` (1). The cases that read `routing_trailers` alone read it over real commits.
- `Test_declared_for_this_branch`: its five cases that call `run_check` (1 each), now in the process.

These cases read git without `main`, over real commits: `test_refuses_a_fixed_commit_head_does_not_descend_from`, `test_refuses_a_fixed_commit_that_touches_nothing_of_the_finding`, the three `#1148` cases of a last record's `fixed`, `test_refuses_a_code_commit_after_the_last_record` and `test_names_a_record_under_another_name_and_keeps_the_exit` of `Test_main`. The same holds for `Test_changed`, `Test_carried_by`, `Test_follows` and the git predicates.

**4. Old cases cut or rewritten.** No case was cut. Each case below was rewritten. Its name and its facts are as they were, and what changed is how its input reaches the unit. Counts are call sites (`census.py`). A line names the case that now holds a fact the case no longer asserts.

- `Test_main::test_accepts_a_reviewed_branch_on_a_ready_pull_request`, `test_refuses_a_git_that_did_not_answer_in_one_line` and `test_refuses_a_baseline_that_does_not_resolve_with_exit_2`: each kept its `main` run and moved from a `branch` copy to `_branch_template`, which the run does not write.
- `Test_main::test_refuses_an_open_finding_on_a_ready_pull_request`: 3 `main` runs and 3 commit helper calls over a `branch` copy before. It now calls `records` twice over `_branch_template`, for the open and the rejected finding, and keeps 1 `main` run on a draft. Its ready run's exit 1 is `main`'s reading of a ready pull request, which `test_refuses_a_chain_with_no_record_and_prints_it_on_a_draft` asserts.
- `Test_main::test_refuses_a_fixed_commit_head_does_not_descend_from`: 1 `main` run and 3 commit helper calls over a `branch` copy before. It now calls `records` over the copy, with 1 commit helper call for the commit on `main`.
- `Test_main::test_refuses_a_fixed_commit_that_touches_nothing_of_the_finding`: 1 `main` run and 4 commit helper calls over a `branch` copy before. It now calls `records` over the copy, with the 1 call site that commits the four touching commits.
- `Test_main::test_refuses_a_last_records_fixed_finding_owing_a_verifying_round`: 3 `main` runs and 4 commit helper calls over a `branch` copy before. It now calls `records` twice over `_branch_template`, reading round 1 alone. Its draft run went, and *Departures from the frame* names where that fact stands.
- `Test_main::test_passes_a_last_records_fixed_finding_that_touched_only_its_records`, `test_refuses_a_last_records_fixed_finding_that_also_touched_code` and `test_refuses_a_last_records_code_finding_fixed_in_its_records_alone`: 1 `main` run and 4 commit helper calls each over a `branch` copy before. Each now calls `records` over the copy, reading round 1 alone, with 1 commit helper call for its fix.
- `Test_main::test_refuses_a_code_commit_after_the_last_record`: 2 `main` runs and 4 commit helper calls over a `branch` copy before. It now calls `records` after each of its 2 commits.
- `Test_main::test_names_a_line_it_did_not_read_as_a_notice_and_keeps_the_exit`: 3 `main` runs and 4 commit helper calls over a `branch` copy before. It now keeps 2 `main` runs over `_branch_template`, the record handed through `reading`. For the finding whose only block is opened otherwise, it calls `records` and `unread`.
- `Test_main::test_names_no_line_inside_a_fence`: 1 `main` run and 2 commit helper calls over a `branch` copy before. It now calls `records` and `unread` over `_branch_template`.
- `Test_main::test_names_a_record_under_another_name_and_keeps_the_exit`: 2 `main` runs and 4 commit helper calls over a `branch` copy before. It now commits the clean record and `Round-2.md` once, and calls `records` and `unread` over the copy. That the exit stays the clean record's is `main` routing `unread` to the notices, which `test_names_a_line_it_did_not_read_as_a_notice_and_keeps_the_exit` asserts: run alone against mutant 81, it is red (executed).
- `Test_main::test_refuses_an_old_shape_record_and_an_unclosed_fence`: 2 `main` call sites, 3 runs, and 4 commit helper calls over a `branch` copy before. It now calls `records` three times over `_branch_template`.
- `Test_main::test_refuses_a_broad_gate_file_naming_another_commit`: 2 `main` runs and 2 commit helper calls over a `branch` copy before. It now keeps the 2 runs over `_branch_template`, the gate record handed through `reading`.
- `Test_main::test_refuses_a_straight_to_the_pr_item_without_the_sealers_two_files`: 2 `main` runs and 2 commit helper calls over a `branch` copy before. It now keeps the 2 runs over `_branch_template`, with the declaration and the absent files handed through `reading`. The passing run comes first, since `reading` adds to what an earlier call handed.
- `Test_main::test_refuses_an_unreadable_declaration_and_accepts_none`: 2 `main` runs and 2 commit helper calls over a `branch` copy before. It keeps both runs. The removed work item is still committed on the copy, and the garbled declaration is handed to a run over `_branch_template` through `reading`.
- `Test_routing_trailers::test_does_not_read_the_trailer_key_a_commit_before_0_23_0_carries`, `test_a_teammates_commit_is_never_judged`, `test_a_merge_and_a_squash_github_committed_are_not_its_own` and `test_a_commit_its_author_did_not_commit_is_not_judged`: 1 `main` run each before. Each now asserts that `routing_trailers` lists no trailer, over the same commits. That `main` judges what the reader lists stays in the four trailer cases that keep their runs, and mutants 61 to 66 are red in the module run.
- `Test_declared_for_this_branch`'s five cases that call `run_check`: the check ran as a subprocess before, and runs in the process now.
- `Test_frame`'s three cases: a commit of the design over a `branch` copy before. They now hand the arm the design, and the plan where the case has one, through `reading` over `_branch_template`.
- `Test_follows::test_accepts_head_and_record_commits_after_it`: a `branch` copy before, `_branch_template` now.

No case of this phase's classes reads a document's prose as its fact. The two module-level functions, `test_the_proofer_and_the_review_skill_name_every_line_a_finding_needs` and `test_the_template_is_the_record_the_check_reads`, read shipped documents and stand as they were, as `frame/design.md` G3 asks.

### Checks at the phase's close

- `bin/test tests/skills/test_chain_check.py -q -p no:xdist --durations=0` at `21ad4adc2`'s tree: 252 passed in 49.29 s (executed, file order).
- `bin/test tests/skills/test_chain_check.py -q`: 252 passed in 11.45 s (executed, under `-n auto`).
- `bin/seal layout --check tests/skills/test_chain_check.py`: exit 0, `seal layout: 1 files read, 0 refused, 0 declare no TARGET` (executed). It prints 34 `report:` lines, each a function of `chain_check.py` with no class of its own name. A report line refuses nothing, and the phase adds and removes no class.
- The *Phase boundary* set, `bin/test tests/skills/test_chain_check.py tests/behaviour tests/text -q`: 1127 passed, 9 skipped (executed). No other test file opens or imports the module. `tests/lib/test_config.py`, `tests/lib/test_gate.py` and `tests/conftest.py` name it in a docstring alone (read).
- `uvx ruff format` and `uvx ruff check` over the changed file: clean (executed).
- The suite: `unverified`. The broad gate is the orchestrator's, once the review rounds settle.
