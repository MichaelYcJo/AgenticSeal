# 1792628098-tests-rebuilt-one-file-per-module — review round 3

target: 425d052a against release/v0.22.3

This round did two things at 425d052a. It checked round 2's four closes. It also reviewed everything after cfb846b2: round 2's fix pass (bcab5b41 to ac965ee7, with 5a207e20), phase 6 from 6e7214be to 54b41700, phase 7 from cc391101 to 425d052a, and the framer's amendments 93a009c6, 3ad42cb3, 066e619b, 0b134a29 and 9e92e4e8. Every run was in a scratch clone of the target, or in a second clone moved to the commits the records name. Facts carried from round 2 and not established again: the shipped scripts' AST equality up to cfb846b2, which this round compared only over cfb846b2..425d052a, and the commit flow's per-case resets, which phase 6 did not touch. Round 1's finding 8, deferred to phase 7, is not raised again; the case it waited for passes at the target (Confirmations). The implementer's account was read as claims. Each claim this round checked is named below with what the tree showed.

## Findings

### 1. The move check passes a group whose moved case reads a changed helper, constant or module binding, so "only moved" rests on the smith's record for every name outside the case

severity: should
location: `skills/verify/scripts/test_layout.py:624`, `skills/verify/scripts/test_layout.py:68-75`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:74-76`, `CONTRIBUTING.md:290-306`, `tests/test_test_layout.py`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md:534`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md:597`
evidence: executed `bin/test tests/test_tmp_r3_probe.py -q -p no:xdist -s`, `python3 helpers.py clone 3 6 7 12 15 16 18 19 20 21 22 24 25 27 28 29 30 31 32 35 37 38 40 41 42 43 46 47 48 49 50 52`, `bin/test tests/test_tmp_r3_fix_probe.py -q -p no:xdist -s`, `R3_SHOW=1 R3_SCRIPT=test_layout_fixed.py python3 moves.py clone run clone2 3 6 7 12 15 16 18 19 20 21 22 24 25 27 28 29 30 31 32 35 37 38 40 41 42 43 46 47 48 49 50 51 52`
verdict: open

`spec.md:74` makes the move check the decider: whether a group's modules were only moved "is decided by the move check below, from the two trees and never from the smith's record". `plan.md:46` records the owner's refusal of the smith's record as that decider. A module the check passes skips the mutants, so the check is the whole proof of equal protection for 31 of phase 6's 50 groups and for both phase 7 moves.

The check compares three things: the count, each case's own body, and the fixtures a case requests (`spec.md:76`, `moved` at `skills/verify/scripts/test_layout.py:624`). It compares no name a case reads from the module around it. That covers a helper function the case calls, a constant a `parametrize` mark reads, the module under test bound to a name such as `reader` or `gate`, and a helper a fixture calls. A probe built four old and new file pairs where only that name changed. In each pair the new side tests less or tests another module. All four exit 0 with `0 failed`:

- `parse` changed from `json.loads(s)` to `return [1, 2]`;
- `subject` rebound from `posixpath` to `ntpath`;
- `ROWS` changed from `[('a', 1), ('bb', 2)]` to `[('a', 1), ('a', 1)]`, so the count still matches;
- a fixture's `build()` changed to return `[]`.

The build has used this gap. The smiths saw it and wrote the names out by hand. Group 14 says "Three helpers resolve to conftest's or the new file's where their old file had its own, and the move check reads none of them, so they are named here" (`phases/phase-6.md:534`). Group 15 says "The move check reads no module-level name, so it is named here" (`phases/phase-6.md:597`). Group 15 exited 0, and its moved splitter cases read `reader`. At the base, `reader` was `unverified_check.py` loaded by path. In the new file it is `hooks/blocks.py` (`tests/test_blocks.py:22`). So for that group the smith's sentence is what says the cases still test what they tested. A script outside the tree compared, for every case each exit-0 group moved, the definitions of the module-level names the case reads, followed through `from conftest import`. Names differ in 21 of the 31 exit-0 groups. This round did not judge whether any of those differences lost protection. Most look benign, such as a loader's module-name string or a path constant spelled another way. The defect is that nothing in the tree decides it.

Neither the frame, the script's docstring (`test_layout.py:68-75`, the `body` entry) nor `CONTRIBUTING.md` *The test layout* names this limit. A sealer reading "exit 0, no mutants" reads more than the check established.

There are two repairs, and the orchestrator chooses between them. The first makes the check read the names, below. Its cost was measured with the candidate code. `tests/test_test_layout.py` still passes, 55 cases. The four shapes above exit 1 naming the name. A helper moved into `tests/conftest.py` unchanged still exits 0. Re-run at their recorded commits, 22 of the 31 exit-0 groups and both phase 7 moves (099cd54d, and cc391101's re-run of group 44) then exit 1. Those groups would need the mutants, or bindings kept as they were spelled. The second repair keeps the check as it is and states the limit. `spec.md:74` would then say what the check decides, and each exit-0 group's record would be what decides the names. That is the reading the owner refused on 2026-10-23, so it needs the owner's or the orchestrator's ruling rather than a smith's edit.

```python
# skills/verify/scripts/test_layout.py
# Precondition: none at an OS boundary; pure AST over the two trees' sources.
# Put `import builtins` in the same edit as BUILTIN_NAMES: the edit hook's
# `ruff check --fix` drops an import nothing uses yet.
import builtins

BUILTIN_NAMES = frozenset(dir(builtins))


def _free_names(node):
    """The names NODE reads and does not bind: what a case, a fixture or a
    helper takes from the module around it."""
    loads, bound = set(), set()
    for inner in ast.walk(node):
        if isinstance(inner, ast.Name):
            (loads if isinstance(inner.ctx, ast.Load) else bound).add(inner.id)
        elif isinstance(inner, ast.arg):
            bound.add(inner.arg)
        elif isinstance(inner, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if inner is not node:
                bound.add(inner.name)
        elif isinstance(inner, (ast.Import, ast.ImportFrom)):
            bound |= {(a.asname or a.name).split(".")[0] for a in inner.names}
    return loads - bound - BUILTIN_NAMES


def _bound(tree):
    """`{name: node}` for each name TREE's top level binds."""
    found = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            found[node.name] = node
        elif isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                found.update(
                    {n.id: node for n in ast.walk(target) if isinstance(n, ast.Name)}
                )
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            found.update({(a.asname or a.name).split(".")[0]: node for a in node.names})
    return found


def _name_forms(tree, conftest, names):
    """`{name: form}` for NAMES as TREE's module binds them, and for each name
    those definitions read in turn: a definition with every docstring
    dropped, an assignment or an import as written. A name `from conftest
    import` brings is read where CONFTEST defines it, so a helper moved into
    `tests/conftest.py` unchanged compares equal."""
    forms, todo = {}, [(tree, n) for n in sorted(names)]
    while todo:
        where, name = todo.pop(0)
        if name in forms:
            continue
        node = _bound(where).get(name)
        if (
            isinstance(node, ast.ImportFrom)
            and node.module == "conftest"
            and conftest is not None
            and where is not conftest
        ):
            original = next(a.name for a in node.names if (a.asname or a.name) == name)
            node, where = _bound(conftest).get(original), conftest
        if node is None:
            continue
        bare = copy.deepcopy(node)
        for inner in list(ast.walk(bare)):
            if isinstance(inner, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                inner.body = _without_docstring(inner.body) or [ast.Pass()]
        forms[name] = ast.dump(bare)
        todo += [(where, n) for n in sorted(_free_names(node))]
    return forms


def _name_change(old_side, new_side, case, requested):
    """The first module-level name CASE, or a fixture it requests, reads whose
    definition the two sides, `(tree, class, conftest)`, bind apart; None
    where every one reads alike."""
    forms = []
    for tree, cls, conftest in (old_side, new_side):
        reads, conf_reads = set(_free_names(case)), set()
        scopes = ([cls.body] if cls is not None else []) + [tree.body]
        for name in requested:
            hit = next((s for s in scopes if name in _fixtures(s)), None)
            if hit is not None:
                reads |= _free_names(_fixtures(hit)[name][0])
            elif conftest is not None and name in _fixtures(conftest.body):
                conf_reads |= _free_names(_fixtures(conftest.body)[name][0])
        both = _name_forms(tree, conftest, reads)
        if conftest is not None:
            both.update(_name_forms(conftest, conftest, conf_reads))
        forms.append(both)
    before, after = forms
    apart = sorted(n for n in set(before) | set(after) if before.get(n) != after.get(n))
    return apart[0] if apart else None


# in `moved`, after the `_fixture_change` test:
            if change:
                lines.append(f"{where}: fixture {change[0]}: {change[1]}")
                continue
            name = _name_change(
                (tree, cls, old_conf), (new_tree, new_cls, new_conf), case, before
            )
            if name:
                lines.append(f"{where}: name {name}: its definition differs from the base's")
```

```markdown
spec.md, The proof of equal protection, the move check bullet, after the third condition:

Fourth, every name a case or a fixture it requests reads from the module
around it, a helper, a constant or a module bound to a name, followed through
the names that definition reads and through `from conftest import`, is
defined alike in both trees, with docstrings dropped; a helper moved into
`tests/conftest.py` unchanged compares equal.

The same condition goes into `test_layout.py`'s docstring as a `names` entry
beside `body` and `fixture`, into `CONTRIBUTING.md` *The test layout*'s move
check bullet, and into `tests/test_test_layout.py::Test_moved` as four rows of
`test_refuses_a_cut_a_merge_an_edited_body_and_a_changed_fixture` (a helper, a
module binding, a row constant, a fixture's helper) and one row of
`test_accepts_a_pure_move` (a helper moved into conftest unchanged), each seen
red against the script at 425d052a.
```

answer:

### 2. The overview says the pairs report names no pair and that one pair stands unmerged, but the report names 210 at the head, and it times the suite "at the head" on a tree before the last move

severity: should
location: `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:5`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:16`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md:59`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/handoff.md:13`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md:1425-1450`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md:1457-1521`
evidence: executed `bin/test-layout --pairs tests/`, `python3 skills/verify/scripts/test_layout.py --pairs tests/test_roll_flow_measurement_issue.py tests/test_tracker_labels.py`, `git log --oneline 6a54be98..425d052a`
verdict: open

The overview is what the sealer reads and what the pull request body copies. Three of its sentences state facts of the head that the head does not show.

`overview.md:59`, under *Fed back into the spec*, ends: "With both, `bin/test-layout --pairs` over `tests/` names 0 pairs." That was true at phase 5. At 425d052a the same command ends `test-layout: 184 files read, 210 pairs`. 120 of them are in `tests/test_run_tests.py::Test_main`, 61 in `tests/test_cmdline.py` (57 in `Test_walk_directories`, 3 in `Test_module`, 1 in `Test_drop_heredoc_bodies`), 20 in `tests/test_session_cost.py` (16 in `Test_post`, 4 in `Test_main`), and one each in nine other classes.

`overview.md:16` is the divergence row on pairs met at placement. It says each pair was merged under rule 2 and that one pair is named and not merged, review-skill-gate's. `spec.md` rule 2 gives `merge` where "the pairs report names it with one". The groups left 210 named pairs unmerged. Most group records name their pairs and give a reason: group 49 for run_tests' 120 (`phases/phase-6.md:1575`), group 33 for session_cost's 20 (:1139), groups 25 and 26 for cmdline's 61 (:902, :927), and groups 1, 8, 10, 23, 31, 32 and 43 for seven of the nine single pairs. Two pairs are in no record. `--pairs` names `Test_find_baseline_issue`'s `test_accepts_one_open_log_and_answers_none_where_there_is_none` and `test_refuses_to_guess_between_two_open_durable_logs` in `tests/test_roll_flow_measurement_issue.py` from group 44's commit 222bf69a. It names `Test_main`'s `test_accepts_a_missing_label_and_creates_it_with_the_documents_sentence` and `test_reconciling_an_already_complete_tracker_writes_nothing` in `tests/test_tracker_labels.py` from group 45's commit efc3a79f. Neither group's record (`phases/phase-6.md:1425-1450`, `phases/phase-6.md:1457-1521`) mentions them. Both groups ran the mutants, so the pairs cost no proof, but no record says why they stay. The main defect is the overview's row. It names one departure from rule 2 where 210 stand, so a reader of the overview learns the opposite of the tree. Most of these pairs are cases that call one function with the same literal arguments over different worlds on disk, such as `main([])`. That is the noise `plan.md:43` dropped a reading of the report for. Whether rule 2's merge stays mandatory for such a pair is the framer's to settle; the overview has to state the departure either way.

`overview.md:5` says `bin/test -q` took "91.4 s over 7,726 at the work item's head". `handoff.md:13` says "91.4 s at the head". `phases/phase-7.md:56` gives the tree as 6a54be98. After it come 099cd54d, which moved the cases of `tests/conftest.py`'s workflow readers and `gh` block, and 3c6b9e0d, which replaced `.test_durations`. The collection at 425d052a is also 7,726 items (Confirmations), but the head was not timed.

```markdown
overview.md:59, the last sentence of the first bullet:

With both, `bin/test-layout --pairs` over `tests/` named 0 pairs at 00674174.

overview.md, ## Where spec and implementation diverged, a row after row 16:

| A pair the report names whose two cases assert different facts | `spec.md` rule 2: `merge` where "the pairs report names it with one" | not merged: at 425d052a `bin/test-layout --pairs tests/` names 210 pairs, 120 in `tests/test_run_tests.py::Test_main`, 61 in `tests/test_cmdline.py`, 20 in `tests/test_session_cost.py` and one in each of nine other classes | the group records name each pair and why neither case covers the other, mostly calls with equal literal arguments over different worlds on disk (`phases/phase-6.md` groups 1, 8, 10, 23, 25, 26, 31, 32, 33, 43, 44, 45 and 49); whether rule 2 keeps the merge mandatory for such a pair is the framer's |

overview.md:5, the last sentence:

Locally, `bin/test -q` took 183.9 s over 7,494 items at the base and 91.4 s over 7,726 at 6a54be98, before 099cd54d's move of the conftest helpers' cases (`phases/phase-7.md` *The suite's wall time, before and after*).

handoff.md:13, the last sentence of the phase 7 row:

Locally the suite ran in 183.9 s at the base and 91.4 s at 6a54be98 (`phases/phase-7.md`).

phases/phase-6.md, group 44's and group 45's records, each a sentence beside
its move check (the reason is the smith's to write after reading the two cases;
the round did not judge it):

`--pairs` names one pair in `Test_find_baseline_issue`,
`test_accepts_one_open_log_and_answers_none_where_there_is_none` and
`test_refuses_to_guess_between_two_open_durable_logs`, which call
`find_baseline_issue` with equal arguments over <what differs>; neither covers
the other because <reason>, so neither is merged.

`--pairs` names one pair in `tests/test_tracker_labels.py::Test_main`,
`test_accepts_a_missing_label_and_creates_it_with_the_documents_sentence` and
`test_reconciling_an_already_complete_tracker_writes_nothing`, which call
`main` with equal arguments over <what differs>; neither covers the other
because <reason>, so neither is merged.
```

answer:

## Confirmations

confirms: round-2#1
The close holds. Read: `spec.md:82` states which columns each earlier table ran, g104 among `broad_gate.py`'s old-column runs. `plan.md:28` and `plan.md:52` drop the order of choosing the mutants from the rule. `overview.md:62-63` carries both departures under *Fed back into the spec*. `phases/phase-5.md:96` names g104 to match its table at :110. Executed: `CONTRIBUTING.md:290-306` is the rewritten record-shape bullet, and `git grep "before the old cases are read\|about 30 per module"` outside `seal/` finds nothing.

confirms: round-2#2
The close holds. Executed: round 2's mutation line again, now aimed at the case the fix added. `bin/mutation-check skills/verify/scripts/seal_stamp.py` with `PANEL_VALUE_WIDTH = 41` set to 42 and to 40, against `tests/test_seal_stamp.py -k test_accepts_a_value_as_wide_as_the_panel_at_eighty_columns`: 2 mutants, 2 red. Read: the comment at `skills/verify/scripts/seal_stamp.py:436-440` names `Test_stamp::test_accepts_a_value_as_wide_as_the_panel_at_eighty_columns`, which stands at `tests/test_seal_stamp.py:794`.

confirms: round-2#3
The close holds. Read: `overview.md:59-61` holds the three clauses with their commits. The divergence table no longer quotes the rewritten rules. `phases/phase-5.md:213` sends its reader to *Fed back into the spec*.

confirms: round-2#4
The close holds. Read: `phases/phase-5.md:662` writes the cut line for `test_a_joined_project_holding_only_its_own_specs_hears_nothing`. Executed: round 2's two mutants of `hooks/root-migrate.py` against `tests/test_root_migrate.py` with `-x`: 2 red.

confirms: none
Every move check the records state reproduces. Executed: the 52 `bin/test-layout --moved` commands of `phases/phase-6.md` and `phases/phase-7.md`, each at the commit its heading names, with `HEAD` read as the commit the record gives, in a second clone. All 52 last lines match the records word for word. That covers the groups that failed and were read line by line (1, 3, 4, 7, 8, 9, 10, 12, 14, 17, 23, 26, 33, 34, 36, 39, 44, 45) and the 31 that exited 0. The whole run took 57 s.

confirms: none
Phase 6's recorded mutants give the verdicts their tables state at the target. Executed: 66 mutants read from the build's drivers in `scratchpad/942-p6/`, run through the clone's own `bin/mutation-check` and not through the drivers, which hard-code the branch worktree. They are 16 batches over `hooks/worktree-guard.py`, the three modules group 13 wrote anew (`hooks/sealer-stamp.py`, `hooks/sealer-stamp-queue.py`, `hooks/commitgate.py`), `hooks/worktree_consent.py`, `hooks/config.py`, `hooks/cmdline.py`, `session_cost.py`, `broad_gate.py`, `chain_check.py`, `issue_claims_check.py`, `roll_flow_measurement_issue.py`, the three tracker scripts and `hooks/commit-review-gate.py`. Every mutant a table lists as SURVIVED survives at the target: s4, s8, c3, c6, k3, k10, k23, config's c6, c13 and c89, m11, m20, m117, s15, s18, s57, b22, b50, b70, g17, g18, i1, i9, i27, r1, r18, the closer's c10, c15 and c36, m6, m9, t4, t6, g12 and g15. Every other mutant sampled is red, among them w5 to w70, s5, s10, s14, q2, q9, q10, c4, c9, c17, k16, and the commit gate's g11, g13, g38 and g42, which group 17 moved the killing cases for. A mutation score licenses *tested*, never *safe*.

confirms: none
Phase 6's closing totals match the group records. Executed, a sum over each group's *Cases and seconds* first figures: 462.6 s before and 421.8 s after. The items come to 7,803 and 7,881 where group 32's "93 passed and 2 skipped" is counted as 93 and 94, which is how the close counts it. The mutants: groups 1, 3, 4, 7, 8, 9, 10, 12, 13, 14, 17, 23, 26, 33, 34, 36, 39, 44 and 45 hold 40, 15, 16, 53, 16, 22, 15, 70, 43, 40, 69, 87, 190, 63, 113, 54, 34, 38 and 77 mutants, 1,055 in all. Their survivors are 8, 6, 4, 3, 5, 8, 5, 0, 4, 6, 7, 12, 17, 13, 4, 3, 10, 4 and 17, 136 in all. Of those, 9 are killed by old cases that did not move (group 14's g11 and g13, group 23's seven) and 2 are answered in group 8, which leaves 125 old gaps.

confirms: none
The autouse fixtures the moved cases came under change no verdict a moved case reads. Executed: `tests/test_worktree_guard.py` run with `_git_asked_once_per_directory`'s caches replaced by a wrapper that also asks the uncached function and logs both answers. The cache was asked 2,289 times and gave the fresh answer every time. The one case that failed under the probe, `Test_repo_paths::test_the_repository_lookup_cannot_hang_the_gate`, reads `inspect.getsource(wg.repo_paths)`, and the probe's wrapper had no `__wrapped__`. Then `tests/test_commit_review_gate.py` was run with `_Press.automation_answered` logging the real reader's answer beside the stub's: 133 calls, 5 apart. All 5 are phase 5's own `pressed-` sessions, whose cases test the stub's press on purpose. Both files were restored by `git checkout`.

confirms: none
Round 2's fix pass and the commit flow's two gap cases hold. Executed: with `hooks/hooksession.py#claude_ancestor`'s depth set to 3, `test_refuses_a_commit_whose_session_the_lease_names[claude-four-levels-up]` is red. With `hooks/githooks.py#_P2` reading `--git-dir` for `--git-common-dir`, `test_refuses_a_commit_in_an_undeclared_linked_worktree_through_the_lease` is red. Read: neither case repeats `test_refuses_through_a_lease_in_a_linked_worktree`, which calls `hooksession.from_lease` alone. `f68fb1b1`'s docstring at `skills/implement/scripts/seal.py:307-311` reads as `Test_export` does, comparing with `MEMBERS` at `tests/test_seal.py:743`.

confirms: none
S14 at cc391101 holds. Executed: three of phase 7's eight mutants rebuilt from their descriptions, n1 (the walk reads the definition alone), n7 (`_resolver` dumps the fixture whole) and n8 (a first `self` kept), against `tests/test_test_layout.py -k Test_moved` with `-x`: 3 red.

confirms: none
The shipped files the range touches change in comments and docstrings only, apart from `test_layout.py`. Executed: an `ast.dump` comparison over cfb846b2..425d052a. `close_issues_on_release.py`, `publish_release_note.py`, `hooks/config.py`, `settle.py` and `seal_stamp.py` compare equal. `hooks/cmdline.py`, `hooks/dispatch.py`, `hooks/launch.py`, `hooks/one_heredoc.py`, `seal.py`, `broad_gate.py`, `session_cost.py` and `unverified_check.py` compare equal once docstrings are dropped. Read: `agents/sealer.md:144`, `agents/smith.md:109`, `agents/smith.md:123`, `agents/warden.md:99` and `skills/writing-style/SKILL.md:268` name the files `spec.md` *The check lines the remaining groups meet* gives them. `bin/arm-check`, `bin/test-layout`, `ruff.toml`, `SECURITY.md` and `skills/verify/SKILL.md` change in prose and examples, and each test file they name exists at the target.

confirms: none
The frame's 67 `## Rule changes` operations apply. Executed: `rule_changes.parse` over `spec.md` gives 67 operations (66 `change`, 1 `add`) over 14 documents of `docs/`, with no error. `rule_changes.replay` applies the spec whole, with none refused. With the replayed documents written into the second clone, `bin/rules --check` holds all 249 check lines in 62 rule files. None of the 19 emptied files `overview.md:43` lists is named by a `check:` line after the replay, and none holds a case. The documents were restored by `git checkout`.

confirms: none
S10's open state and its 115 files are as the overview says. Executed: `bin/test-layout --check --all` at the target exits 1 with `184 files read, 115 refused, 115 declare no TARGET`. The 115 refused files are exactly the files `overview.md:43-47` lists in its five bullets, 19, 1, 1, 13 and 81. `bin/test-layout --check` exits 0 with 0 refused. `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0. `bin/test tests/test_test_layout.py tests/test_censuses.py tests/test_conftest.py tests/test_seal_stamp.py tests/test_root_migrate.py -q`: 486 passed.

confirms: none
The durations file prices the head, which closes what round 1's finding 8 waited for. Executed: `pytest --collect-only` at 425d052a collects 7,726 items. `.test_durations` prices 7,726 ids at 1,662.0 s. 19 collected items have no price, all in `tests/test_conftest.py`, and 19 priced ids are stale, 7.8 s, 0.47% of the file. `bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite`: 1 passed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether any of the 21 exit-0 groups whose moved cases read a module-level name defined differently lost protection. The script found names apart and judged none of them | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md` | the fix pass of finding 1 |
| The other 989 mutants of phase 6's tables, and phase 7's n2 to n6. This round re-ran 66 and rebuilt 3 | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md`, `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md` | the orchestrator |
| The wall times of `phases/phase-7.md` *The suite's wall time*, 183.9 s and 91.4 s. Re-running them is a full suite run, unverified | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-7.md` | the orchestrator, at the broad gate |
| CI run 39966993884 at 425d052a, in flight when this round ended, unverified | `.github/workflows/test.yml` | the orchestrator |
| Whether each of the 81 files left for #923 and the 13 checks across files holds no case of a module's function. This round read the case lists of seven of them | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/overview.md` | #923 |
| Each group record's reason that its named pairs assert different facts, and whether the two pairs no record names do. This round counted the 210 pairs against the records and read none of the pairs | `seal/specs/1792628098-tests-rebuilt-one-file-per-module/phases/phase-6.md` | the framer, with finding 2 |
| The full suite, the repository-wide lint and the typecheck at 425d052a, unverified | the whole tree | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the branch worktree into `scratchpad/942-r3/clone` at 425d052a, and a second clone moved between the group commits; both removed after the round | every run below ran in one of the two |
| `python3 moves.py clone run clone2 1 to 52`, a script outside the tree that checks out each record's commit and runs its `bin/test-layout --moved` command | 52 of 52 last lines as recorded |
| `python3 astcmp.py clone cfb846b2 425d052a` | 5 equal, 8 equal once docstrings are dropped, `test_layout.py` changed; the non-Python files listed in Confirmations |
| `bin/test tests/test_tmp_r3_probe.py -q -p no:xdist -s`, four rows each changing only a module-level name a moved case reads; deleted after the run | 4 passed: each `--moved` run exit 0, `0 failed` |
| `python3 helpers.py clone <the 31 exit-0 groups and 099cd54d>`, a script outside the tree comparing the module-level names each moved case reads | names apart in 21 of the 31 groups; none in 27, 30, 31, 32, 38, 42, 43, 46, 47, 48 and 099cd54d's move |
| the candidate fix of finding 1 in the second clone: `bin/test tests/test_test_layout.py -q -p no:xdist`, `bin/test tests/test_tmp_r3_fix_probe.py -q -p no:xdist -s` (five rows, deleted after), then the 33 exit-0 commands under it; the script restored by `git checkout` | 55 passed; the four shapes exit 1 naming the name and the helper moved to conftest unchanged exits 0; 22 of 31 groups and both phase 7 moves exit 1 |
| `sh mutsample.sh`, 66 recorded mutants in 16 `bin/mutation-check` batches with `-x` against the target | every recorded survivor survives; every other mutant sampled is red |
| `bin/mutation-check skills/verify/scripts/seal_stamp.py`, two widths, and `bin/mutation-check hooks/root-migrate.py`, round 2's two mutants | 2 red; 2 red |
| `bin/mutation-check hooks/hooksession.py` (depth 3) and `bin/mutation-check hooks/githooks.py` (`--git-dir`), each against its new commit-flow case | red; red |
| `bin/mutation-check skills/verify/scripts/test_layout.py`, S14's n1, n7 and n8 rebuilt | 3 red |
| `R3_CACHE_LOG=cache.log bin/test tests/test_worktree_guard.py -q -p no:xdist` with the caches wrapped; `R3_PRESS_LOG=press.log bin/test tests/test_commit_review_gate.py -q -p no:xdist` with the press stub wrapped; both restored by `git checkout` | 2,289 cached answers, 0 apart, 349 passed and 1 failed under the probe; 133 press reads, 5 apart, all phase 5's `pressed-` sessions, 261 passed |
| `python3 replay.py clone2 --write`, then `bin/rules --check`; documents restored by `git checkout` | 67 operations, 0 refused, 14 documents; 249 check lines hold |
| `bin/test-layout --check --all`, `bin/test-layout --check`, `bin/test-layout --pairs tests/`, `bin/rules --check`, `bin/unverified-check seal/specs/` | exit 1 with 115 refused; exit 0; 210 pairs; exit 0; exit 0 |
| `pytest --collect-only -q -p no:xdist tests` against `.test_durations`, and `bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite` | 7,726 collected, 19 unpriced, 19 stale at 7.8 s; 1 passed |
