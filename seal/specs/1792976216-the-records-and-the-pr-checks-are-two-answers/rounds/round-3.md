# Review round 3: 1792976216-the-records-and-the-pr-checks-are-two-answers

target: 64a13a36, fixes d1647de2..64a13a36

## Findings

### 1. The settle that applies this spec turns the line-wrap case red, because the rewritten `change` to the arms document leaves a 91-column line

severity: should
location: `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/spec.md:449-451`, `docs/the-review-and-parity-arms.md:110`
evidence: executed `python3 -I test_tmp_round3_rules.py clone --write`, `bin/test tests/test_docs_line_wrap.py -q`, `python3 -I test_tmp_round3_rules.py clone --spec-ref=d1647de2 --write`
verdict: open
regression: round-2#3

The unit is the `change` item to `docs/the-review-and-parity-arms.md` *The
declaration, and where the check went* (`spec.md:445-451`). Round 1's fix
pass made it in `64a73e7b`. `4cdfef95` rewrote its `to` text for round 2
finding 3, although that finding said this item already used the one term
and could stay. The frame, `spec.md` *In* item 6 and scenario S8, asks the
rule changes to state the no-root condition in one term and to apply cleanly.
The fix kept the term and made the first `to` line three columns longer.
`rule_changes.py#apply_op` writes the `to` lines as they stand, after the
text that comes before `from` on the same line, so the defect came from the
rewrite and not from the frame.

The round applied all 17 items to `docs/` at `02ee12de` in a clone. Line 110
of `docs/the-review-and-parity-arms.md` then reads "`retired: a settle`;
where it does not, the refusal stands, except where the tree the check", 91
columns. `tests/test_docs_line_wrap.py` fails on it: "is 91 columns (limit
88)". With the spec at `d1647de2` applied instead, the same line is 88
columns and the module passes, 39 of 39 (executed). So this fix pass made
the failure.

This is the class of round 1 finding 3 and round 2 finding 1: a case green
on the branch that goes red at the settle, and `settle --apply` writes no
sentence by hand. The round enumerated the class over the 77 test modules
whose code names a changed document, a README or `docs/` (`## Probes`). With
the 17 items applied, this case and one unrelated to `docs/` failed, and
3236 passed. The unrelated one is a row of `## Not judged`.

It is a second regression on the rule-change items that state the no-root
condition. Round 1 finding 1's fix made them, round 2 finding 3 was the
first regression on them, and this one came from that finding's fix pass.

The fix wraps the `to` text so that its first line fits after the text
before it. Executed in the clone with finding 3's word applied as well:
line 110 is 81 columns and line 111 is 74. `tests/test_docs_line_wrap.py`,
`tests/test_no_passage_is_pasted_into_a_second_file.py`,
`tests/test_one_word_one_meaning.py`,
`tests/test_both_editions_carry_the_same_folds.py` and
`tests/test_a_document_has_room_for_the_next_fold.py` gave 81 passed.

```markdown
- change
  file: docs/the-review-and-parity-arms.md
  section: The declaration, and where the check went
  from: where it does not, the refusal stands.
  to: where it does not, the refusal stands, except where the tree
    the check reads has no top-level `seal` entry (`docs/the-review-record.md`
    *What the check reads at the pull request*).
```

answer:

### 2. No case reaches the `--worktree` answer that the root is gone, so a mutant that never gives it passes every case

severity: should
location: `tests/test_chain_check.py:3417-3441`, `skills/code-review/scripts/chain_check.py:2192-2193`
evidence: executed `bin/test tests/test_chain_check.py tests/e2e/teammate/test_teammate_flow.py tests/test_unverified_check.py -q`, `bin/test tests/test_tmp_round3_probe.py -q -k accepts_under_worktree`, `git grep -l -e --worktree -- tests evals`
verdict: open
regression: round-2#2

The unit is the `if WORKTREE:` arm that `c09d050a` added to
`chain_check.py#main`, lines 2192 and 2193. The frame, `spec.md` *In* item 6
as `4cdfef95` amended it, says the tree the check reads is the working tree
under `--worktree`, the same tree it reads the declarations from. Round 2
finding 2 named two shapes of that reading. A new untracked root must be
judged. A `seal mode local` that has run and is not committed must read as
nothing declared, as CI reads it once it is committed. The fix pass added
two cases, and both require the declarations judged. Neither reaches the
arm's other answer, so the defect came from the fix pass's cases and not
from the frame.

The smith's answer claims two cases, seen red. That holds for the two
(executed, `## Probes`), and they pin one half of the arm. The round replaced line
2193 with `gone = False`. With that mutant, `tests/test_chain_check.py`, the
flow case and `tests/test_unverified_check.py` gave 603 passed. `git grep`
finds `--worktree` in `tests/test_chain_check.py` and in two modules that
read document text, and in nothing that runs the check. So an edit that
drops the working-tree reading brings back round 2's second shape, a
refused uncommitted switch, with nothing red.

It is a second regression on the no-root test in `chain_check.py#main`.
Round 1 finding 1's fix made the test, round 2 finding 2 was the first
regression on it, and this one came from that finding's fix pass.

The fix adds a case to `Test_retired`. The round ran it as a probe: it
passes at `64a13a36` and fails against the mutant at `assert code == 0`
(executed). It uses only names `tests/test_chain_check.py` already has.

```python
    @pytest.mark.rule("nothing-declared-nothing-owed")
    def test_accepts_under_worktree_a_root_the_working_tree_no_longer_has(
        self, branch, ready, capsys, tmp_path
    ):
        """Round 3 of #952: a switch to local mode, run and not committed,
        leaves no `seal` in the working tree, so under `--worktree` nothing
        is declared, as CI reads the same change once it is committed."""
        root, _code = branch
        remove_an_earlier_item(root, applied=False)
        shutil.move(str(root / "seal"), str(tmp_path / "moved-seal"))
        git(root, "add", "-A", "seal")
        code, out = check(root, capsys, "--worktree")
        assert code == 0, out
        assert "so nothing is declared" in out
        assert "does not carry this file at HEAD" not in out
```

answer:

### 3. The `add` says a deleted declaration is otherwise refused, but one a settle retired is accepted

severity: should
location: `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/spec.md:433-434`
evidence: executed `bin/test tests/test_tmp_round3_probe.py -p no:xdist -s -q`, `python3 -I test_tmp_round3_rules.py clone --write`
verdict: open
regression: round-1#1

The unit is the `add` to `docs/the-review-record.md` *What the check reads at
the pull request* (`spec.md:427-438`), which round 1's fix pass made in
`60f3ea14`. At `d1647de2` it read "a deleted declaration HEAD does not carry
is otherwise refused", and `4cdfef95` shortened it to "a deleted declaration
is otherwise refused". Both say that wherever a `seal` entry is in the tree,
every deleted declaration is refused. `docs/the-review-and-parity-arms.md`
lines 102 to 110 say otherwise: a declaration whose directory a settle
removed is accepted with `retired: a settle`. The probe showed it on two
trees that keep a `seal` entry, a file and a dangling link: the deleted
declaration of the merged work item printed `retired: a settle` and the
check exited 0 (executed).

With the items applied, the section states the deletion rule twice. The
paragraph *The check reads the diff as declarations* says "the deletion is
judged", which is exact, and the new paragraph says "refused", which is not.
`CLAUDE.md` *Repo rule: text an agent or a check reads has one reading* asks
for one statement. A person framing the next change to the retirement arm
from this section reads that it does not exist. Round 2 did not name this,
and its own suggested text carried the same word. So it is a regression of
round 1 finding 1's fix pass, and not a second regression.

The fix uses the paragraph's own word. The round applied it with finding
1's wrap, and the five modules finding 1 names gave 81 passed (executed).

```markdown
    mode deletes every `routing.md` with the root, and a deleted declaration
    is otherwise judged. With no `seal` entry there is nothing to declare,
```

answer:

## Confirmations

confirms: round-2#1
The two READMEs no longer copy the rule. `README.md:510-513` says that a
workflow left after a move to local stays in the tree, and names
`docs/one-root-by-lifetime.md` *Shared or local* for which pin passes and how
to move one that fails. `README.ko.md:503-506` names the Korean edition the
same way (read). With the 17 items applied, the round printed both target
sections. *Shared or local* lines 132 to 138 say that a workflow pinned to a
release with the no-root state passes, and that one pinned to an older
release fails until its `--branch` line moves or `seal pr-checks remove`
takes it out. The Korean section, lines 129 to 134, says the same (executed).
So each link lands on a section that states the rule once the settle runs.
`tests/test_no_passage_is_pasted_into_a_second_file.py` passed in the
77-module run with the items applied, where round 2 saw it fail (executed).
The `LEFT_BEHIND` pin holds the new sentences (read
`tests/test_first_setup_asks_once.py:485-499`).

confirms: round-2#2
Under `--worktree` the no-root test asks the working tree, with
`os.path.lexists` at `chain_check.py:2193`, and CI asks `git ls-tree HEAD`
(read). The round ran six tree shapes through both readings: `--worktree`
before the commit, then CI after it (executed). An uncommitted switch now
reads as nothing declared under `--worktree`, as CI reads it once committed.
That was round 2's second shape, which `d1647de2` refused. A `seal` that is a
file, a dangling link and a link to a directory are judged in both readings.
With `chain_check.py` at `d1647de2`,
`Test_retired::test_judges_a_root_the_working_tree_has_under_worktree`
fails, so it was seen red as claimed. With `lexists` mutated to `isdir`,
`test_judges_the_declarations_where_the_working_tree_has_seal_as_a_file`
fails, which is the smith's claim (both executed). Finding 2 above is the
half of the arm no case reaches. One reading is open by design: `lexists`
answers False on any `OSError`, not only on absence, so under `--worktree`
such an error reads as gone, while CI's `git()` None keeps the declarations
judged. Reaching it needs a top level the check cannot search, where it can
read nothing else either (read).

confirms: round-2#3
The condition has one term everywhere it is stated. The `add` and both
`change` items say "the tree the check reads has no top-level `seal` entry"
(read `spec.md:427-451`). So do `ROOT_LEFT_SAYS` and the comment at
`chain_check.py:2043-2048` and `chain_check.py:2184-2190`, the module
docstring's *declaration* arm, the changelog fragment and the `Test_retired`
pin (read). The sentence that said the check reads the tree as the
unverified check does is gone, and `spec.md:164-167` says the two are not one
reading. A `seal` that is a file is judged by both readings of the chain
step (above), while `unverified_check.py#absent_root` asks for a directory,
as the frame now says. Finding 1 is a regression from this fix pass in an
item round 2 finding 3 left alone. It is not a reopening of that finding,
whose one-term close holds.

confirms: none
The 17 items of `spec.md` *Rule changes* parse with `rule_changes.py#parse`
with no error, and each places in order with `apply_op` against `docs/` at
`02ee12de` (executed). `git diff --stat 02ee12de 64a13a36 -- docs` is empty,
so that is still the policy in force (executed).

confirms: none
`--worktree` and CI answer differently on one shape. After the switch is
committed, a `seal/` directory left behind empty, or holding only an ignored
file, is still an entry on disk. So `--worktree` judges the declarations
there, while CI's HEAD has no entry and reads nothing as declared (executed,
the `empty-dir-left` and `ignored-file-left` shapes). The difference errs
toward judging, so a local run is stricter than CI and never looser.
`seal mode local` moves the root with one `os.rename`
(`skills/implement/scripts/seal.py:2360`), and the README's by-hand move
uses `mv` on the whole directory, so neither leaves such a directory (read).
So it is no finding.

confirms: none
The narrow set exits 0 at `64a13a36`: `bin/test` over
`tests/test_chain_check.py`, `tests/e2e/teammate/test_teammate_flow.py`,
`tests/test_unverified_check.py`, `tests/test_first_setup_asks_once.py`,
`tests/test_seal.py` and `tests/test_mode_gate.py` gave 1048 passed (executed).
The six commits after `d1647de2` each carry
`SpecSeal-Routing: 1792976216-the-records-and-the-pr-checks-are-two-answers`
with author and committer both the repository's identity, and each touches
only the files its subject names (executed, `git log` and `git show --stat`).

Facts carried from earlier rounds rather than re-established: where the
chain step's declaration arm lives (`chain_check.py#main`), `questions.md` Q2,
the merge-order hold behind other specs, and the newer-pin row of round 2's
`## Not judged`. Every verdict above was reached this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the flow cases run or skip on the Windows legs of `.github/workflows/test.yml` (`questions.md` Q2). Carried from round 2 and not re-run | `tests/e2e/teammate/test_teammate_flow.py` | the pull request's CI run on `windows-latest`, read by the orchestrator |
| The settle holds this spec behind specs refused for reasons outside this branch. Carried from round 2; the merge-order replay was not run again this round | `seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md:292` | the orchestrator |
| A workflow pinned to a release newer than the installed one gets the "move its `--branch` line" advice, which then names an older release. Carried from round 2 and still not judged | `skills/implement/scripts/seal.py:1842-1868` | the orchestrator |
| Finding 1 is the third instance on this branch of a case green at the pull request and red at the settle. Nothing at the pull request runs the documents' own checks over a spec's applied rule changes. Whether a check or a case should do so was not judged | `skills/code-review/scripts/chain_check.py`, `skills/settle/scripts/rule_changes.py` | the orchestrator |
| `tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview` fails at `64a13a36` with `docs/` as committed, because this work item has a `spec.md` and no `overview.md` yet (executed) | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers` | the orchestrator, with the closing memo before the broad gate |
| The full suite, the repository-wide lint and the typecheck: not run, as contract rule 2 gives them to the broad gate after the rounds settle; the smith's suite stays `unverified` | the branch | the orchestrator, by `broad-gate` |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_round3_rules.py clone`, in a clone at `64a13a36`: parse and place the 17 items against `docs/` at `02ee12de`, print the four changed sections as applied, and list the test modules whose path-like string constants name a changed document, a README or `docs/` | 17 placed, no parse error; 77 modules |
| the same with `--write`, then `bin/test` over the 77 modules | exit 1: 2 failed, 3236 passed, 9 skipped. The failures are `test_docs_line_wrap.py` at `docs/the-review-and-parity-arms.md:110` (finding 1) and the overview case of `## Not judged` |
| `git checkout HEAD -- docs`, then `bin/test tests/test_chain_hooks_hardening.py tests/test_docs_line_wrap.py -q` | 1 failed, 64 passed: the overview case fails without the items too |
| `python3 -I test_tmp_round3_rules.py clone --spec-ref=d1647de2 --write`, then `bin/test tests/test_docs_line_wrap.py -q` | 39 passed: at round 2's spec the line is 88 columns |
| finding 1's wrap and finding 3's word written into the clone's `spec.md`, the items applied again, then `bin/test` over the five document modules finding 1 names | 81 passed; line 110 is 81 columns |
| `bin/test tests/test_tmp_round3_probe.py -p no:xdist -s -q`: six shapes (the switch, `seal` as a file, as a link to a directory, as a dangling link, an empty `seal/` left, a `seal/` holding only an ignored file), each with `--worktree` before the commit and CI after it | as stated in the confirmations and finding 3 |
| `chain_check.py:2193` replaced by `gone = False`, then `bin/test tests/test_chain_check.py tests/e2e/teammate/test_teammate_flow.py tests/test_unverified_check.py -q` | 603 passed: the mutant survives (finding 2) |
| finding 2's case run as `test_tmp_accepts_under_worktree_a_root_the_working_tree_no_longer_has`, at `64a13a36` and against the mutant | passes, then fails at `assert code == 0` |
| `chain_check.py` from `d1647de2`, then `bin/test tests/test_chain_check.py -q -k Test_retired` | 2 failed: the root-on-disk case and the notice-text pin |
| `chain_check.py:2193` with `lexists` replaced by `isdir`, then the same | 1 failed: the `seal`-as-a-file case |
| `bin/test` over the six modules of the narrow set | 1048 passed |

Each source edit and each applied `docs/` was restored with `git checkout
HEAD --` after its run. The two probe files and the clone were removed
before the hand-back.
