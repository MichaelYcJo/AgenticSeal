# Review round 1: 1793174171-code-no-input-reaches

target: e2d954c8 against 5287dd42

No earlier round exists, so this round carried no coordinate and re-established every fact below. No `seal/parity.md` is declared, so the round wrote no `original:` line. The spec is issue #1056. There is no frame, as the second rung of the ladder allows.

## Findings

### 1. Two members of k12's class were not enumerated, and their docstrings name a refusal of None that no reader makes

severity: should
location: `skills/code-review/scripts/chain_check.py:883-893`, `skills/code-review/scripts/chain_check.py:908-918`
evidence: executed `bin/seal mutate skills/code-review/scripts/chain_check.py --replace $'    found = as_row(VERDICT_ROW, value)\n    if not found:\n        return None\n' $'    found = as_row(VERDICT_ROW, value)\n' --replace $'    if not as_row(LOCATION_ROW, value):\n        return None\n' '' --tests "bin/test -p no:xdist -q tests/skills/test_chain_check.py tests/github/test_release_seal.py -k 'not test_refuses_every_other_value and not test_refuses_no_home_and_another_verdict and not test_refuses_everything_else'"`, `git grep -n -e "f\.verdict" -e "f\.paths" -- skills .github hooks`
verdict: fixed c8b5f382

Why it matters: contract rule 12 makes k12's removal owed to every unit the same cause produces. The cause is a second whole-row check inside a reader whose one caller, `finding_of`, already matched the line whole. The crafter's hand-back and `gaps.md` *Not done* name `reference_of` as the one other member of the class. Two more exist, and nothing in the records names them.

Grounds:

- `verdict_of` (`chain_check.py:883-893`) and `location_of` (`chain_check.py:908-918`) each read the value against their row whole a second time and return None where it fails.
- `finding_of` calls both only on lines it keeps in `read`, and it keeps a line there only where `row.shape.fullmatch` matched it (`chain_check.py:1120-1125`). Both rows are `one` per finding, so a finding missing either line is refused before the call.
- The only other caller of `verdict_of` is `deferred_home`. `gaps.md` *Not done* already says that function is reached only from cases.
- With both None branches removed and the three direct-call refusing cases deselected, `tests/skills/test_chain_check.py` and `tests/github/test_release_seal.py` stayed green: mutant 1 and mutant 2 SURVIVED, exit 1. This is the measurement `reference_of` got in phase 1, and it gives the same result.
- Both docstrings end "is None, which the arm refuses by name". No reader of a `Finding` handles a None verdict or None paths. `verdict_problems` unpacks `kind, commit = f.verdict` (`chain_check.py:1654`). `chain_check.py:1388` and `chain_check.py:1404` index `f.verdict[0]`. `release_seal.py:358` and `broad_gate.py:2534` unpack `f.verdict`, and `chain_check.py:1678` iterates `f.paths`. A None at any of these raises. The refusal the docstrings describe is `finding_of`'s shape refusal, which happens before either function is called. A next crafter who reads "the arm refuses by name" would take the None branch for a live path.

The fix gives both the treatment `reference_of` got in `5d3e53c9`: the false clause goes, and a sentence says why the branch stays. The other choice is to remove both branches and point the refusing cases at `as_row(VERDICT_ROW, value)` and `as_row(LOCATION_ROW, value)`. That choice is the owner's (see `## Not judged`). Either way, `gaps.md` *Not done* should name the two members beside `reference_of`.

```python
def verdict_of(value):
    """`(kind, its commit or home)` for one `verdict:` value, or None.

    Read against the `verdict:` row whole: its word, and the commit of a
    `fixed` or the home of a `deferred`. Anything the row does not match —
    another case, emphasis, a trailing word or mark, a bare `fixed` or
    `deferred` — is None.

    `finding_of` hands it only a line the row already matched whole, and
    `deferred_home` is called only by cases, so no record reaches the None.
    It stays because `Test_verdict_of` and `Test_deferred_home` call it with
    values the row refuses, and those cases are where the `verdict:` grammar
    is pinned."""
    found = as_row(VERDICT_ROW, value)
    if not found:
        return None
    return value.split(" ", 1)[0], found["commit"] or found["home"]


def location_of(value):
    """The paths one `location:` value names, in order, or None.

    Read against the `location:` row whole, then each backticked item to
    its first `:`, which the row keeps out of a path. Anything the row does
    not match — a bare `:617`, a path with no backticks, a URL, an absolute
    path, a `path#unit`, emphasis around an item, a trailing word or mark,
    an empty value — is None.

    `finding_of`, the one caller in the tree, hands it only a line the row
    already matched whole, so no record reaches the None. It stays because
    `Test_location_of` calls it with values the row refuses, and those cases
    are where the `location:` grammar is pinned."""
    if not as_row(LOCATION_ROW, value):
        return None
    return [item.strip("`").split(":")[0] for item in value.split(", ")]
```

answer: The finding holds. I opened `finding_of` at `chain_check.py:1120-1125` and the six readers of `f.verdict` and `f.paths` it names, and none of them handles a None. c8b5f382 takes the record's first path. Each docstring drops "which the arm refuses by name" and says why the branch stays, as the round drafted: no record reaches the None, and the direct-call cases pin the row's grammar there. No branch is removed. `gaps.md` *Not done* now names `verdict_of` and `location_of` beside `reference_of`, with the owner's question of whether those cases should call `as_row` instead. A `git grep` for "refuses by name", "refused by name" and "None, which" across the tree found nothing else making the same claim. `docs/the-review-record.md:256` and `tests/skills/test_chain_check.py:3292` describe a record with no `## Findings`, which `finding_spans` does refuse. `hooks/lib/config.py:855` describes a None that `skills/verify/scripts/pact_check.py:628` handles. `hooks/lib/config.py:951` and `skills/settle/scripts/rule_changes.py:373` claim no refusal. After the fix, the 25 modules that name or import `chain_check` passed with 2059 passed and 9 skipped, exit 0. `ruff check` and `ruff format --check` on the file both exited 0.

## Confirmations

confirms: none
Each removal #1056 lists has no input that reaches it, and each re-run mutant SURVIVED at the base `5287dd42` (executed). k3 is the `if not session` return in `hooks/worktree_consent.py#main`. Its mutant SURVIVED over the crafter's six modules, 467 passed. `consent_path` returns "" for an empty or a None id, and `record` then writes nothing (read `hooks/worktree_consent.py:118-137`, `hooks/worktree_consent.py:426-441`). i12 and i13 SURVIVED as one batch. k12 SURVIVED with 261 passed. s47 SURVIVED with 400 passed. These match the exit codes in phase 1.

confirms: none
i12 and i13 fold into one comprehension that returns the same result. The new `before` at `.github/scripts/issue_claims_check.py:260` is `start <= c[1] < m.start(1)`. `ISSUE_REF.finditer(text, start, end)` yields only matches that end by `end`, so `m.start(1) < end`, and the old bound was implied (read). Without the skip, a segment holding no claim finds an empty `before` for every number in it, so it appends no warning.

confirms: none
i7's removal changes no caller. `segments` has one caller in the tree, `read` (executed `git grep -n -e "segments(" -- .github hooks skills`). A whitespace segment holds no `#N`, so `read` reports nothing new for it. The removed case `test_refuses_a_run_of_whitespace_as_a_segment` also exercised the blank-line cut. That cut is still pinned. With `not stripped or` removed from the cut condition, `Test_read::test_a_fence_does_not_splice_the_line_above_it_onto_the_line_below` and `Test_read::test_accepts_a_number_a_segment_boundary_keeps_apart[a-blank-line]` failed, exit 0 (executed).

confirms: none
The recorder fields have no reader. Outside the excluded record directories, the tree has one hit for `invocation_dir` or `wasxfail`: the parameter of `collects_the_suite` at `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:321`, which is pytest's own value (executed). The two `logged` cases and `Test__invocation_dir` pinned only the removed fields and the removed function. The `test` line's `category` is still pinned from end to end at `tests/skills/test_agentic_pytest_record.py:1189` (read). The module docstring lists the fields the code still writes (read `skills/verify/scripts/pytest_record/agentic_pytest_record.py:29-31`).

confirms: none
The class enumeration for s47 holds. An `ast` walk over every except tuple in `git ls-files '*.py'`, less `tests/` and `seal/`, found no exception named beside its own base class at `e2d954c8`. The walk resolved builtin names and module-qualified names such as `zipfile.BadZipFile` (executed). `read_manifest` now catches two classes, `KeyError` and `ValueError`. Its docstring says "the two this catches" (read `skills/implement/scripts/seal.py:973-991`).

confirms: none
m6 is kept, and its reason holds. With `LABEL_DESCRIPTION_LIMIT = 10`, a case in `tests/github/test_label_merged_on_release_branch.py` and a case in `tests/github/test_tracker_labels.py` failed, exit 0 (executed). This meets the issue's "a mutant of each kept item is red". The new comment at `.github/scripts/label_merged_on_release_branch.py:114-120` says correctly which cases read the constant (read).

confirms: none
The moved case and the edited durations file stand. `bin/seal layout --check` exited 0 with 0 refused, and `bin/seal rules --check` exited 0 (executed). `test_the_durations_file_prices_the_suite` passed against the edited `.test_durations` (executed). The moved case covers a cut that `Test_segments`' other case does not, so it does not repeat its group.

confirms: none
The modules that read the changed files pass. They are every module `git grep -l` finds in `tests/` for each changed path, plus the modules that reach `seal import`. The run gave 3517 passed, 14 skipped, exit 0. `ruff check` and `ruff format --check` over the eight changed Python files exited 0 (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a None branch reached only by direct-call cases stays with its reason or goes, with the cases pointed at `as_row`. This covers `reference_of` as kept, and `verdict_of` and `location_of` under finding 1. | `skills/code-review/scripts/chain_check.py:883-934` | the repository owner |
| Whether `deferred_home`, which only cases call, is removed. It is already in `gaps.md` *Not done*. | `skills/code-review/scripts/chain_check.py:896-899` | the repository owner |
| The full suite, the repository-wide lint and the typecheck. This round ran none of them, under contract rule 2. | the whole tree | the orchestrator, through `seal gate` |
| The other 22 modules that `git grep -l` finds naming `seal.py`. The round ran the five that reach `import_` or `read_manifest`, the two functions the diff changes in that file. | `tests/` | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over the 51 modules `git grep -l` finds in `tests/` for the changed paths, the five modules that reach `seal import`, and `tests/github/test_release_seal.py` | 3517 passed, 14 skipped, exit 0 |
| `bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite` | 1 passed, 6765 deselected, exit 0 |
| `bin/seal layout --check` | 158 files read, 0 refused, exit 0 |
| `bin/seal rules --check` | all 266 check lines in 55 rule files hold, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over the eight changed Python files | exit 0 and exit 0 |
| at `5287dd42`: `bin/seal mutate hooks/worktree_consent.py --replace $'    session = data.get("session_id", "")\n    if not session:\n        return\n' $'    session = data.get("session_id", "")\n' --tests "bin/test -p no:xdist -q tests/hooks/test_worktree_consent.py tests/hooks/test_dispatch.py tests/behaviour/test_the_guard_asks_once_per_session.py tests/hooks/test_worktree_guard.py tests/behaviour/test_the_frozen_reading_never_grows.py tests/text/test_guard_resolves_the_tree_it_judges.py"` | SURVIVED, 467 passed, exit 1 |
| at `5287dd42`: `bin/seal mutate .github/scripts/issue_claims_check.py --replace "here = [c for c in claims if start <= c[1] < end]" "here = [c for c in claims if start <= c[1]]" --replace $'        if not here:\n            continue\n' '' --tests "bin/test -p no:xdist -q tests/github/test_issue_claims_check.py tests/behaviour/test_a_body_naming_two_issues_claims_one.py tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py"` | mutant 1 SURVIVED, mutant 2 SURVIVED, exit 1 |
| at `5287dd42`: `bin/seal mutate skills/implement/scripts/seal.py --replace "except (zipfile.BadZipFile, RuntimeError, NotImplementedError) as bad:" "except (zipfile.BadZipFile, RuntimeError) as bad:" --tests "bin/test -p no:xdist -q tests/skills/test_seal.py"` | SURVIVED, 400 passed, exit 1 |
| at `5287dd42`: `bin/seal mutate skills/code-review/scripts/chain_check.py --replace $'    found = as_row(REOPENS_ROW, value)\n    return reference(found) if found else None' '    return reference(as_row(REOPENS_ROW, value))' --tests "bin/test -p no:xdist -q tests/skills/test_chain_check.py"` | SURVIVED, 261 passed, exit 1 |
| `bin/seal mutate .github/scripts/issue_claims_check.py --replace "if not stripped or BLOCK_START.match(line):" "if BLOCK_START.match(line):" --tests "bin/test -p no:xdist -q tests/github/test_issue_claims_check.py tests/behaviour/test_a_body_naming_two_issues_claims_one.py tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py"` | red, 2 failed in `Test_read`, exit 0 |
| `bin/seal mutate .github/scripts/label_merged_on_release_branch.py --replace "LABEL_DESCRIPTION_LIMIT = 100" "LABEL_DESCRIPTION_LIMIT = 10" --tests "bin/test -p no:xdist -q tests/github/test_label_merged_on_release_branch.py tests/github/test_tracker_labels.py"` | red, exit 0 |
| finding 1's `seal mutate` on `verdict_of` and `location_of` | mutant 1 SURVIVED, mutant 2 SURVIVED, exit 1 |
| an `ast` walk of except tuples over `git ls-files '*.py'`, less `tests/` and `seal/`, resolving builtin and module-qualified names | 0 hits |

Every probe ran in a `git clone --no-local` under the round's scratch directory, at `e2d954c8` unless the row names `5287dd42`. The clones were removed before hand-back.
