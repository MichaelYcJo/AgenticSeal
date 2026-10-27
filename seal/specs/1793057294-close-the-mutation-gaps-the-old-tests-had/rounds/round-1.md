# Review round 1: 1793057294-close-the-mutation-gaps-the-old-tests-had

target: dfd10e1a against release/v0.22.4

Round 1 has no earlier record, so nothing is carried from a round. The round
read the branch's own changes, `git diff 5daa931f...dfd10e1a`, in a
`git clone --no-local` of the worktree at `dfd10e1a`. No `seal/parity.md` is
declared, so no parity comparison applies. The frame (`spec.md`, `plan.md`,
`questions.md`), the seven phase records, `overview.md` and `changelog.md`
were read whole.

How the round sampled. The work adds 171 case definitions over 32 test
files, and the round did not read every one. It rebuilt 26 mutants from the
records' pairs with `bin/mutation-check`, at least two per phase. The sample
holds every row whose record says the case fails by an exception rather than
its own assertion (s60, sd2, h4, rr5, c32, c35), five rows whose case fakes a
dependency under contract rule 13 (the `git_dir` rows of
`hooks/session-lease.py`, the `optin` normpath row, `hooks/implementer.py`'s
`write`, s4 and k3), two rows recorded as already closed by another file
(st13, c18), and m6. It read every equivalent verdict's reason against the
code at the head. It read the new cases of nine test files whole
(`tests/test_label_merged_on_release_branch.py`, `tests/test_tracker_labels.py`,
`tests/test_worktree_consent.py`, `tests/test_sealer_stamp.py`,
`tests/test_optin.py`, `tests/test_session_lease.py`, `tests/test_cmdline.py`'s
`Test__env_walk`, `tests/test_conftest.py`'s ch6 rewrite and `Test_read`, and
the c35 and s60 cases), and ran `bin/test-layout --pairs` and `--check` over
all 32 changed test files.

Carried without re-running: every row's before verdict, the 119 mutants this
round did not rebuild, and phase 3's t5 probe over 1,488 commands. These are
rows of `## Not judged`.

## Findings

### 1. m6's new case pins `LABEL_DESCRIPTION_LIMIT`, a value no shipped code reads, and writes GitHub's 100 a second time

severity: should
location: `tests/test_label_merged_on_release_branch.py:390-396`, `seal/specs/1793057294-close-the-mutation-gaps-the-old-tests-had/phases/phase-7.md:92`, `seal/specs/1793057294-close-the-mutation-gaps-the-old-tests-had/phases/phase-7.md:152-158`, `seal/specs/1793057294-close-the-mutation-gaps-the-old-tests-had/overview.md:28`, `seal/specs/1793057294-close-the-mutation-gaps-the-old-tests-had/overview.md:57-85`, `seal/specs/1793057294-close-the-mutation-gaps-the-old-tests-had/changelog.md:3`
evidence: executed `git grep -n LABEL_DESCRIPTION_LIMIT`, `python3 test_tmp_round1_mutants.py`
verdict: open

Phase 7 claimed that "m6 pins a number, because the number is the decision",
and in the same paragraph that the constant "is read by no function of its
module" (`phases/phase-7.md:152-158`). The search confirms the second half.
The constant is defined at `.github/scripts/label_merged_on_release_branch.py:113`.
No shipped code reads it. One comment names it (`.github/scripts/tracker_labels.py:92`),
and two cases read it as their ruler (`tests/test_label_merged_on_release_branch.py:384`
and `tests/test_tracker_labels.py:146`). So the decision the mutant changes
is made only inside the suite. No input to any shipped function tells 100
from 1000.

`spec.md` *In* item 1 calls that row equivalent. The spec's grounding row on
`CLAUDE.md` *The rule a mechanism is kept against* says code no caller
reaches "is not kept by pinning it with a case". The new case also breaks a
fact's one source. `tests/test_tracker_labels.py:137-145` says the cap "is
read from the module that names it rather than written here, so the number
has one source". The new case writes `100` in a test, so the next person who
changes the cap edits two places, and only the case would tell them so.

The probe shows the case does kill its mutant (red after a passing
baseline). The defect is what it pins, not whether it kills.
`overview.md` *Names no input reaches* lists six names of this kind for the
repository owner and leaves this one out.

The fix deletes the case, records m6 as equivalent, and moves it to the
owner's list. Phase 7 then counts 14 killed and 1 equivalent. The totals
become 122 killed and 15 equivalent, or 121 and 16 together with finding 2.

```diff
--- tests/test_label_merged_on_release_branch.py
-    def test_refuses_a_cap_past_the_hundred_characters_github_takes(self):
-        """The cap is GitHub's and no reader here enforces it but the cases:
-        a 101-character description is refused with `HTTP 422 ... (maximum
-        is 100 characters)` (#515). Every description case here and in
-        `tests/test_tracker_labels.py` measures against this constant, so a
-        cap raised past GitHub's passes a description the tracker refuses."""
-        assert signal().LABEL_DESCRIPTION_LIMIT == 100
-
--- phases/phase-7.md, the m6 row
-| m6: `LABEL_DESCRIPTION_LIMIT` is 1000 | `'LABEL_DESCRIPTION_LIMIT = 100'` `'LABEL_DESCRIPTION_LIMIT = 1000'` | SURVIVED, every file | red, `Test_module::test_refuses_a_cap_past_the_hundred_characters_github_takes` | killed by a new case |
+| m6: `LABEL_DESCRIPTION_LIMIT` is 1000 | `'LABEL_DESCRIPTION_LIMIT = 100'` `'LABEL_DESCRIPTION_LIMIT = 1000'` | SURVIVED, every file | SURVIVED | equivalent: no function of this module or of `tracker_labels.py` reads the constant. The description cases of `tests/test_label_merged_on_release_branch.py` and `tests/test_tracker_labels.py` read it as their ruler, so a raised cap changes nothing either script sends |
--- overview.md, a seventh item under *Names no input reaches*
+- **m6, `LABEL_DESCRIPTION_LIMIT` in
+  `.github/scripts/label_merged_on_release_branch.py`.** No shipped code
+  reads it; the two description cases read it as their ruler, so it is a
+  test's value kept in a shipped module (`phases/phase-7.md`).
```

The paragraph at `phases/phase-7.md:152-158`, the module row at `:32`, the
outcome sentence at `:25-27`, the phase 7 row and the total row of
`overview.md`, and the counts in `changelog.md` change with it.

answer:

### 2. k3's case fakes `worktree_consent`'s own `record`, which is no platform guarantee, so the row is equivalent and the case pins an internal call

severity: should
location: `tests/test_worktree_consent.py:271-284`, `seal/specs/1793057294-close-the-mutation-gaps-the-old-tests-had/phases/phase-3.md:118`, `seal/specs/1793057294-close-the-mutation-gaps-the-old-tests-had/phases/phase-3.md:173-178`, `seal/specs/1793057294-close-the-mutation-gaps-the-old-tests-had/overview.md:52`
evidence: read `hooks/worktree_consent.py:118-138`, `hooks/worktree_consent.py:426-441`, `hooks/worktree_consent.py:591-624`, `tests/test_worktree_consent.py:271-284`
verdict: open

Phase 3 claimed that "k3 rests on a guarantee the module gives itself, and
its case removes it (contract rule 13)" (`phases/phase-3.md:173-178`).
Contract rule 13 is narrower: "A defence resting on a platform guarantee is
not verified". `overview.md:52` quotes the rule without the word "platform",
and that is how k3 got into the row.

The code shows no input that tells the mutant apart. With `if not session`
dropped, `main` goes on to `record(top, "")` (`hooks/worktree_consent.py:624`).
There `consent_path` reduces the empty id and returns "" (`:132-134`), and
`record` returns False without writing (`:433-435`). The calls in between,
`creation_directory` and `optin.repo_root`, write nothing. `spec.md` *In*
item 1 defines that outcome as equivalent.

The case replaces `wc.record` with a recorder and asserts that `main` never
calls it with an empty session. That assertion is about `main`'s call
structure, not about anything the hook writes. Suppose a later change drops
`main`'s check because `record` already refuses. The case then fails, and
nothing the hook does has changed. `plan.md` *Technical context* names this
failure ("a count of internal calls") as the one its guard is written
against.

The other seven rows on that line of `overview.md:52` stand. They fake git,
the operating system's refusal of a non-directory, or, for s4, the `stamp`
module that `drawings(stamp, directory)` takes as its own parameter. Those
are boundaries the function crosses. k3's fake is a function of the module
under test.

The fix deletes the case and the `import io` that only it uses. It records
k3 as equivalent and moves it to the owner's list. Phase 3 then counts 14
killed and 4 equivalent.

```diff
--- tests/test_worktree_consent.py
-import io
 import json
...
-    def test_refuses_a_payload_with_no_session_id_where_any_session_is_recorded(
-        self, monkeypatch, repo
-    ):
-        ...
-        assert written == []
-
--- phases/phase-3.md, the k3 row
-| k3: `main` records a payload with no session id | ... | SURVIVED, every file | red, `Test_main::test_refuses_a_payload_with_no_session_id_where_any_session_is_recorded` | killed by a new case, with `record` replaced by one that records any session |
+| k3: `main` records a payload with no session id | `$'    if not session:\n        return\n    tool = data'` `$'    if False:\n        return\n    tool = data'` | SURVIVED, every file | SURVIVED | equivalent: past the test, `main` reaches only `record(top, "")`, whose `consent_path` answers "" for an empty id, so nothing is written either way |
--- overview.md:52, the divergence row
-... 8 rows are recorded killed ... and s4 of `hooks/sealer-stamp.py`; phase 3's k3 of `hooks/worktree_consent.py` | ... | contract rule 13: a defence resting on a guarantee is not verified ...
+... 7 rows are recorded killed ... and s4 of `hooks/sealer-stamp.py` | ... | contract rule 13: a defence resting on a platform guarantee is not verified ...
--- overview.md, an item under *Names no input reaches*
+- **k3, `hooks/worktree_consent.py#main`'s `if not session` return.**
+  `record` refuses an empty session through `consent_path` on its own
+  (`phases/phase-3.md`).
```

answer:

### 3. The records count 184 new cases where the work item added 171, and phase 2 counts four guarantee rows where it names three

severity: should
location: `seal/specs/1793057294-close-the-mutation-gaps-the-old-tests-had/overview.md:93`, `seal/specs/1793057294-close-the-mutation-gaps-the-old-tests-had/phases/phase-7.md:195-197`, `seal/specs/1793057294-close-the-mutation-gaps-the-old-tests-had/phases/phase-2.md:198-202`
evidence: executed `git diff 5daa931f...dfd10e1a -- tests | grep -c '^+.*def test_'`, `git diff fa7d1374 5daa931f -- tests | grep -c '^+.*def test_'`, `git diff 134d7203 dfd10e1a -- tests | grep -c '^+.*def test_'`
verdict: open

`overview.md` *Not verified* row 3 and `phases/phase-7.md:195-197` say "the
work item adds 184 lines holding `def test_` since 134d7203". The sealer
reads that row, and the pull request body is written from these records.
The spawn prompt for this round repeated the number as the work's size.

`git diff 134d7203 dfd10e1a` counts 184. That range includes the merge
95fa9fb7, which brought in 13 case definitions from `release/v0.22.4`
(#1050 and #1037, counted over `fa7d1374..5daa931f`). The branch's own
changes add 171. The phase ranges give the same total:
23 + 26 + 20 + 32 + 11 + 35 + 24 = 171.

`phases/phase-2.md:198-202` says "Four rows rest on a guarantee their caller
gives" and "Three are git's", then names two git rows and s4, three in all.
`overview.md:52` counts phase 2 as three and notes the mismatch. So the
phase record's sentence is the wrong one.

```markdown
| whether `.test_durations` still prices the suite within its share (`questions.md` Q5): the work item adds 171 lines holding `def test_` (`git diff 5daa931f...HEAD -- tests`) and prices none of them; `git diff 134d7203 HEAD` counts 184, because it also holds the 13 the merge of `release/v0.22.4` brought | ... |
```

```markdown
**Three rows rest on a guarantee their caller gives, and their cases remove it
(contract rule 13).** Two are git's: `hooks/implementer.py#git_dir` and
`hooks/review-skill-gate.py#git` on a non-zero exit, ...
```

answer:

## Confirmations

confirms: none
`gh_json`'s removal leaves nothing standing on it. `git grep -n gh_json`
at `dfd10e1a` finds only the records of #942 and of this work item. No
`.py`, workflow or document names it. `_issue_api` still uses the module's
`json` import (`.github/scripts/close_issues_on_release.py:168`). The diff
outside `tests/` and `seal/` is the four lines of 6e7d552b in that one file.
`tests/conftest.py` is unchanged. Executed with `git grep` and
`git diff --stat 5daa931f...dfd10e1a`.

confirms: none
Each of the 26 sampled mutants is red against the case its record names,
and each run's baseline passed. The sample covers phase 1 (session-lease
`git_dir`, routing one-cell, optin normpath), phase 2 (implementer `write`,
s4, `to_utf8`), phase 3 (k3, m47, c14), phase 4 (s60, s57, mc21 batch,
invocation_dir), phase 5 (sd2, g18, r4, and st13 already closed on
`tests/test_settle.py`), phase 6 (h4, h2, rr5, i7) and phase 7 (c32, c35,
c18 already closed on `tests/test_label_merged_on_release_branch.py`, m6,
t6). Every pair landed exactly once, and the clone was clean afterwards.
The six cases that fail by an exception each assert what the caller is
owed. For example, c35 asserts that #61 stays open and #88 closes
(`tests/test_close_issues_on_release.py:965-977`), and s60 asserts that the
output parses as JSON with the two segment rows
(`tests/test_session_cost.py:4823-4833`). Executed with the probe.

confirms: none
The totals add up. The phase tables' module rows sum to each phase's
outcome line. The seven phases and the spec's 30 settled rows sum to the
overview's 180, split as 123, 9, 14 and 34, with 145 mutants. The spec table
*Rows whose code left the tree* lists 30 rows. Read.

confirms: none
The equivalent verdicts hold against the code at the head:

- h4 and h8: `hooks/hooksession.py:55-75`. `is_claude("")` is false,
  `int("")` raises, and pid 0 meets the `<= 1` floor.
- `undeclared`: `optin.home_at` returns only "" or a found directory
  (`hooks/optin.py:189-207`).
- `notify`: `hooks/implementer-notice.py:143-153` with `routing.for_branch`.
- o2 and o10: `hooks/one_heredoc.py:52-96`.
- lint-python's missing runner: `resolve_runner` returns None, and
  `[*None]` raises inside the loop's `try` (`hooks/lint-python.py:70-105`).
- k12: `as_row` prefixes the label, and the two shapes share their groups
  (`skills/code-review/scripts/chain_check.py:865-932`).
- s47: `issubclass(NotImplementedError, RuntimeError)` is True, executed.
- i12 and i13: `.github/scripts/issue_claims_check.py:237-265`.
- r18: `.github/scripts/roll_flow_measurement_issue.py:397-401`.

i7's reclassification from equivalent to gap holds, because `segments` is
public and its own return differs. Read, plus the one execution.

confirms: none
m47's case reads env's grammar correctly on both implementations. This
answers `overview.md` *Not verified* row 4. GNU coreutils 9.7 `env -iS ''
-vS 'echo split-ran'` splits the second string and executes `echo`, and so
does the macOS env. So an empty split string does not end env's options,
which is what the case asserts. Executed with `genv` and `/usr/bin/env`.

confirms: none
s4's stand-in is sound. `drawings(stamp, directory)` takes the module as its
own parameter, and its docstring says the draw before the claim "is what
proves the file draws at all" (`hooks/sealer-stamp.py:110-150`). A module
whose draw fails is therefore input the function is written for. The rule 13
grounds also hold for the git rows and the two directory rows, whose fakes
stand where git or the operating system refuses. Read.

confirms: none
No case was removed, and `.test_durations` prices no removed case. The
diff removes no line holding `def test_`. Its removed lines are import lines
and the body of the ch6 case, which still stands under its name. The 32
changed test files collect 2,067 node ids. `.test_durations` prices 1,846
ids in those files, and every one of them is still collected, so none is
stale. 221 collected ids are unpriced. The `tests` run 40441381574 at
`dfd10e1a` passed on Linux, on all three macOS groups and on all four
Windows groups. Its Linux job ran `pytest tests/`, which collects the whole
suite, with 6,745 passed and none failed, so
`test_the_durations_file_prices_the_suite` passed there. That answers
`overview.md` *Not verified* row 2, and it answers Q5 from CI. The broad
gate is still the orchestrator's. Executed with `bin/test --collect-only`,
a comparison against the file, and `gh run view`.

confirms: none
No new case near-duplicates its group in a way the records do not name.
`bin/test-layout --pairs` over the 32 files prints 33 pairs, and 7 of them
involve a new case: `Test_comments_on`, `Test_close_issue`,
`Test_existing_labels`, `Test__invocation_dir`, and three in
`tests/test_tracker_labels.py::Test_main`. These are the pairs phases 4 and
7 name, and in each the two cases differ in what the faked reader answers
or in `DRY_RUN`. `--check` reads 32 files and refuses none. Reading the
sampled files, each case that reads the platform fakes it. The `normpath`
cases use a `..` segment, the lease blocker is a file rather than a mode
bit, the console case uses cp949 text streams, and the walk uses
`stub_process_tree`. Executed for the layout runs, read for the rest.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three; the CI run is evidence, not the broad gate | `broad-gate.md` | the orchestrator, by `broad-gate --base release/v0.22.4 --record` once the rounds settle |
| The 180 rows against the issue's body and its three comments: whether each row of #1017 is in exactly one table, and the 135, 33, 6 and 4 per source. The round did not open the issue | `spec.md` *What the list is*, `overview.md:30-32` | the sealer, in its sample of claims |
| The before verdicts of every row, and the 119 mutants this round did not rebuild. Carried from the phase records | `phases/phase-1.md` to `phases/phase-7.md` | the sealer, in its sample of claims |
| t5's equivalence rests on phase 3's probe over 1,488 commands, carried and not re-run | `phases/phase-3.md:148-155` | the sealer, in its sample of claims |
| Q1 to Q4 stand on their defaults, Q5 is answered by CI above | `questions.md` | the owner, at the pull request |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_round1_mutants.py` (26 pairs from the phase tables, each through `bin/mutation-check <module> --replace OLD NEW --tests "bin/test <file> -q -x -p no:xdist -k <case>"` in the scratch clone) | 26 of 26 exit 0, `red` after a passing baseline; the clone's status empty afterwards; the probe file is deleted |
| `git grep -n LABEL_DESCRIPTION_LIMIT` | one definition, one comment in `tracker_labels.py`, three reads in two test files, no shipped reader |
| `git diff 5daa931f...dfd10e1a -- tests \| grep -c '^+.*def test_'` and the same over `fa7d1374 5daa931f` and `134d7203 dfd10e1a` | 171, 13 and 184; no removed `def test_` line |
| `bin/test-layout --pairs` and `--check` over the 32 changed test files | 33 pairs, 7 with a new case; 32 files read, 0 refused |
| `bin/test --collect-only -q -p no:xdist` over the 32 files, compared with `.test_durations` | 2,067 collected, 1,846 priced in those files, 0 priced and not collected, 221 unpriced |
| `gh run view 40441381574` | success at `dfd10e1a` on every job; the Linux job 6,745 passed, 17 skipped |
| `genv -iS '' -vS 'echo split-ran'` and `/usr/bin/env -iS '' -vS 'echo bsd-ran'` | both execute `echo` with the second string's word |
