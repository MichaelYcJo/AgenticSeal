# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — review round 4

target: 988d3555, fixes b81de037..988d3555

## Findings

### 1. A `sealed` guarantee that queued nothing now counts as stamped, so the commit that repairs its row draws no stamp at all

severity: should
location: `skills/verify/scripts/seal_stamp.py:1058`, `docs/the-review-record.md:287`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`
verdict: fixed a226da11
regression: round-3#2

The unit is `seal_stamp.sealed_before`, which 076b1ee4 added. The frame
holds once per work item by the `Target SHA` row's earlier run and the
values file's name (`plan.md` B1), and the owner's words in `spec.md` say
the stamp is drawn once, from `guarantee.md` reading `sealed`, and never
twice; the fix took any earlier commit whose guarantee read `sealed` as
proof that a stamp was drawn there, while `_queue_one` draws only where the
audited commit stands in that commit's history, so the defect came from the
fix and not from the frame, and the frame stays as it is.

Why it matters. A commit whose guarantee reads `sealed` over a commit that
is not in its own history queues nothing, by design: a squash or a
cherry-pick was stamped where it was made. The same refusal meets a row
naming a commit this clone does not hold, such as a mistyped or stale SHA.
The pull request's check refuses that guarantee too, so the next step is a
commit repairing the row. Before 076b1ee4 that commit drew the work item's
one stamp. Now `sealed_before` finds the unqueued `sealed` in the history,
takes it as stamped, and the work item ends with no stamp. The owner's rule
is one stamp per work item, and this gives none, from the plugin's own
refusal rather than from a clone it cannot reach. Round 3 named the missing
direction only for a `sealed` committed where no stamp could be drawn: a
foreign hooks slot, or a person's own commit.

Executed (probe rows 4 and 5, a `test_tmp_*` file over the stamp module's
own fixtures, run once and deleted):

- A guarantee reading `withheld` is committed. Then one reading `sealed`
  over `deadbee`, a SHA the repository does not hold, is committed:
  `post-commit` says nothing and queues nothing, at HEAD and with
  b81de037's `seal_stamp.py` alike. Then the row is repaired to name the
  audited commit and committed. With b81de037's module that commit queues
  one stamp. At HEAD it queues nothing, and nothing is queued at all.
- With the change below, the case below fails at HEAD (the repaired commit
  said nothing) and passes with it. The stamp, commit-gate, reader and
  interpreter-floor modules stay green with it, 262 passed, round 3's
  second-clone case among them, and `ruff check` and `ruff format --check`
  of the file pass.

Read: a row naming no SHA of its own is not a trigger. `target_of` takes
the first SHA-shaped word of the row, so `pending against <base>` names the
base, which is in the history, and the first commit queued at HEAD and at
b81de037 alike (probe row 4).

In `skills/verify/scripts/seal_stamp.py`, `sealed_before`'s loop body,
which then counts an earlier commit only where `_queue_one` would have
drawn there. A `sealed` that queued nothing is skipped, and every commit
that did draw a stamp still counts, so round 3's two second-clone shapes
still queue nothing:

```python
        verdicts = chain.verdicts_of(reader, text)
        if len(verdicts) != 1 or chain.verdict_word(verdicts[0][1]) != chain.SEALED:
            continue
        target = chain.target_of(reader, text)
        if target and _git(top, "merge-base", "--is-ancestor", target, sha) is not None:
            return True
    return False
```

The case, after `test_a_sealed_item_recommitted_in_another_clone_queues_nothing`:

```python
def test_a_seal_that_queued_nothing_does_not_count_as_stamped(tmp_path):
    """#975 round 4, once per work item. A `sealed` guarantee whose audited
    commit is not in its own history queued nothing, so the later commit
    that repairs the row is the first that can draw the stamp, and draws
    it. Red at 988d3555: `sealed_before` counted the unqueued `sealed` as
    a stamp, and the work item drew none."""
    repo, target, base = guaranteed(tmp_path, verdict="withheld — x")
    assert after_the_commit(repo) == ""
    item = repo / "seal" / "specs" / ITEM_NAME / "guarantee.md"
    item.write_text(guarantee_text("deadbee", base, "sealed"), encoding="utf-8")
    commit_all(repo, "sealed over a commit this clone does not hold")
    assert after_the_commit(repo) == ""
    item.write_text(guarantee_text(target, base, "sealed"), encoding="utf-8")
    commit_all(repo, "the row repaired")
    assert after_the_commit(repo)
    (path,) = queued(repo)
    assert path.endswith(f"-{ITEM_ID}-{target}.json"), path
```

The sentence in `docs/the-review-record.md` §*The stamp* at line 286, with
the case added to its `Enforced by:` line. `sealed_before`'s docstring and
the module's once comment then say the same condition:

```text
guarantee elsewhere, queues nothing; and a guarantee that read `sealed`,
over a commit then in its history, at an earlier commit of that history, or
whose `Target SHA` row's `; earlier run:` chain reads `sealed`, was stamped
then, which holds across clones. The stamp
```

answer: `sealed_before`'s loop body is the record's: an earlier `sealed` counts only where `merge-base --is-ancestor <its target> <that commit>` holds, the condition `_queue_one` draws under, so a `sealed` that queued nothing is skipped and every commit that drew still counts. Its docstring, `queue_for_guarantee`'s docstring and the module's once comment say that condition. `docs/the-review-record.md` §*The stamp* carries the record's sentence and the case on its `Enforced by:` line; `git grep -n -F` of the changed sentence finds no pin under `tests/`. `overview.md`'s round-3 row and §*Fed back into the spec* carry the narrowing, and the fragment says a `sealed` over a commit the branch does not hold draws nothing and a later commit correcting that row in place draws the stamp. The cost the round left open: one `merge-base` per earlier commit that read `sealed`, reached only after every cheaper refusal in `_queue_one`, and the loop returns at the first that counts. The class, enumerated over the three facts that hold once: a values file exists only where a stamp was queued, so `already_queued` cannot count an unqueued `sealed`; the `Target SHA` row's `; earlier run: <sha> sealed` can, and does where the sealer re-runs after a `sealed` over a commit the clone does not hold and keeps that verdict on the row, so that re-run draws no stamp. That instance is left as it stands: it predates round 3, `spec.md` S7 says any earlier run reading `sealed` queues nothing, and `test_a_second_sealed_verdict_queues_nothing` holds it with `bbb2222`, a SHA its repository does not hold, so narrowing it changes the frame and is the owner's call. executed: `test_a_seal_that_queued_nothing_does_not_count_as_stamped` red at eb4303b4 (`assert after_the_commit(repo)` got `''`), green after; `mutation-check` of the new condition: `if True:` turned the new case red, and `if False:` turned `test_a_sealed_item_recommitted_in_another_clone_queues_nothing` red; the stamp, commit-gate, interpreter-floor, line-wrap and reader modules 303 passed; the real-identifier, record-words, changelog, one-word and pasted-passage modules 92 passed; `bin/rules --check` exit 0; `uvx ruff check` and `uvx ruff format --check` of the two Python files exit 0

## Confirmations

confirms: round-3#1
`ruff.toml` carries `chain_check.py` and `unverified_check.py` at `py39`
beside `seal_stamp.py`, and `chain_check.py:893` reads
`list(zip(heads, [*heads[1:], end]))` (read, the fix diff). The two lists
always have the same length, so dropping `strict=False` changes nothing
(read). `test_what_runs_before_any_floor_needs_nothing_its_python3_lacks`
fails with b81de037's `ruff.toml` and `chain_check.py` put back, naming the
two files, and passes at 988d3555 (executed, probe rows 1 and 7). `uvx
vermin --target=3.9- --violations --eval-annotations` over
`hooks/commitgate.py` and the three scripts reports a minimum of 3.8 and no
target missed, and `ruff check` and `ruff format --check` exit 0 (executed,
probe row 2). The class was enumerated by the case itself, which derives
the post-commit path's files from the code rather than from a list.

confirms: round-3#2
The body edit and the fresh-row re-seal in a second clone queue nothing
at 988d3555: `test_a_sealed_item_recommitted_in_another_clone_queues_nothing`
passes at HEAD and fails with b81de037's `seal_stamp.py` put back, at its
first second-clone assertion (executed, probe rows 1 and 6). The docstring,
the module comment, the document's sentence and its `Enforced by:` entry,
the memo's rows and the fragment follow the answer (read). The amend of the
sealing commit in a second clone still queues one, as the memo and the
fragment state (executed, probe row 4). The close holds for what the finding
named; finding 1 above is a separate defect in the same unit.

confirms: none
The memo's `## Not verified` row that opens with `closed` is the form
`skills/verify/scripts/unverified_check.py` reads as closed, and
`bin/unverified-check` on the work item exits 0 (read; executed, probe row
5).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck: `unverified` by this round | — | the orchestrator's broad run, after the rounds settle |
| Whether `merge-base --is-ancestor` per earlier `sealed` commit costs enough on a long guarantee history to matter. It runs only after a commit that touched a `sealed` guarantee with no earlier run, so it is rare | `skills/verify/scripts/seal_stamp.py:1058` | the fix pass |

## Probes

| Command | Result |
|---|---|
| `bin/test` of `test_a_script_says_which_interpreter_it_needs.py`, `test_chain_check.py`, `test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `test_the_commit_gate_decides_at_the_commit.py`, `test_every_reader_ends_a_line_where_gfm_does.py`, `test_docs_line_wrap.py` with `-q`, in the round's clone at 988d3555 | 380 passed, exit 0 |
| `uvx ruff check` of `ruff.toml`, the three scripts and the stamp test module; `uvx ruff format --check` of two scripts and the module; `uvx vermin --target=3.9- --violations --eval-annotations` of `hooks/commitgate.py` and the three scripts; `bin/rules --check` | exit 0; exit 0; minimum 3.8, no target missed; exit 0 |
| `bin/test` of `test_no_real_identifiers.py`, `test_the_record_is_written_in_words.py`, `test_the_changelog_is_gathered_at_release.py`, `test_one_word_one_meaning.py`, `test_no_passage_is_pasted_into_a_second_file.py`, `test_release_hygiene.py` with `-q` | 138 passed, exit 0 |
| `tests/test_tmp_round4_probe.py`, `-s -p no:xdist`, at 988d3555 and with b81de037's `seal_stamp.py`: a `sealed` row over `pending` and over `deadbee` after a `withheld`, then the row repaired; and an amend of the sealing commit in a second clone | `pending`: the first `sealed` commit queued at both; `deadbee`: nothing at the first commit at both, the repaired commit queued one with b81de037's module and nothing at HEAD; the amend queued one at both |
| the probe's planted case at 988d3555; then with the change in finding 1 in the clone's `seal_stamp.py`, the planted case and the `deadbee` case; the stamp, commit-gate, reader and interpreter-floor modules; `uvx ruff check` and `uvx ruff format --check` of the file; `bin/unverified-check` on the work item | 1 failed (the repaired commit said nothing); 2 passed; 262 passed; exit 0 and 0; exit 0 |
| `bin/test tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py -k test_a_sealed_item_recommitted_in_another_clone_queues_nothing` with b81de037's `seal_stamp.py`, then the file restored | 1 failed at `assert after_the_commit(other) == ""` |
| `bin/test tests/test_a_script_says_which_interpreter_it_needs.py -k test_what_runs_before_any_floor_needs_nothing_its_python3_lacks` with b81de037's `ruff.toml` and `chain_check.py`; both restored, the probe deleted, `git status` | 1 failed naming `chain_check.py` and `unverified_check.py`; clean |
