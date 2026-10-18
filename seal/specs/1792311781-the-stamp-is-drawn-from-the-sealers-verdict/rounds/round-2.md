# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — review round 2

target: 981b0acc, fixes a0ee12eb..981b0acc

## Findings

### 1. The documents still call the gate's run a seal in the sentences round 1's fix pass left as Seal Test vocabulary

severity: should
location: `README.md:76`, `README.ko.md:68`, `README.ko.md:70`, `README.ko.md:73`, `skills/verify/SKILL.md:251`, `skills/verify/SKILL.md:273`, `skills/verify/SKILL.md:276-277`, `skills/verify/SKILL.md:285`, `skills/verify/SKILL.md:385`, `skills/verify/SKILL.md:529`, `tests/test_broad_gate_rule.py:54`, `tests/test_the_gate_names_every_step_ci_runs.py:172`, `tests/test_the_seal_is_taken_once_by_the_sealer.py:3974`
verdict: open
reopens: round-1#2

Why the close does not hold. Round 1's finding 2 was a class: documents
outside the gate that call the gate's run a seal. 212db890 reworded the seven
sentences it named and more members of the class, and those hold (read, the
diff; their pins green, probe row 1). Its answer then left a set of sentences
as Seal Test vocabulary for the owner. `questions.md` Q6 has since been
answered (a): the code names and the concept name *the Seal Test* stay, and
"words a person reads in the gate's output and the documents follow". Each
sentence below was judged by what its own paragraph says it names, and each
names the gate's run.

Read:

- `README.md:76` ends the paragraph "At the gate, the run is read against the
  base commit ... and nothing edits between that seal and the PR". `that seal`
  points back at the run, so the sentence names the gate's run a seal.
  `README.ko.md:73` is its twin ("그 봉인과 PR 사이에는"). `README.ko.md:68`
  and `:70` call the full-suite runs taken before the rounds `봉인`, where the
  English twin says "a full suite taken before the rounds" and "none
  surviving".
- `skills/verify/SKILL.md:529` opens "**Nothing edits between the broad seal
  and the PR.**", and the next two sentences say what that seal is: "The tree
  that passed is the tree that ships. One more small fix after the run means
  the run is stale, and the gate is paid for again." `:251` restates the same
  rule. `:285` is the Scope table's cell for the row whose `What runs` is
  "full suite, lint, typecheck — once", and it reads "the one broad seal".
- `skills/verify/SKILL.md:273` ("Not one of those seals survived", the twenty
  broad runs), `:276-277` ("Sealing the whole suite before them seals a
  tree") and `:385` ("a seal taken before the rounds is spent by the first
  finding", in §*The broad gate*) each call a broad run a seal.
- Two test failure messages say the same about the gate.
  `tests/test_the_gate_names_every_step_ci_runs.py:172` reads "a step with no
  row is a seal that covers less than the merge is judged by". 212db890
  reworded this sentence's twin in the same file's docstring to "a green run
  covered", and the fix pass's answer said the test messages follow.
  `tests/test_the_seal_is_taken_once_by_the_sealer.py:3974` reads "the gate
  does not name the command it sealed over".

What separates these sentences from the concept is the same file's own
definition. `skills/verify/SKILL.md:241-244` says "the one seal over the
whole project is the sealer's `guarantee.md`", and that a hand-back and a
report are not seals. A broad run called a seal contradicts that, three
paragraphs later.

Judged the concept, and not reported: `templates/config.md:224` ("a default
of `true` seals everything") is the counterfeit seal that
`skills/verify/SKILL.md:37` and `:264` name as the concept. The Scope table's
column header `Seal` holds the condition-4 labels. `skills/verify/SKILL.md:241`
names the sealer's seal.

Pins (executed, `git grep -n -F` of each phrase over `tests/` and `evals/`,
probe row 5): only `tests/test_broad_gate_rule.py:54` pins one of these
sentences. The two READMEs move together under the hygiene step of that
name.

```text
README.md:76
nothing edits between that run and the PR.

README.ko.md:68
회차 앞에서 돌린 전 스위트는 그 회차가 부르는 첫 수정에 깨집니다. 한 작업
README.ko.md:70
살아남은 실행은 하나도 없었으며, 그 값이 세션 도구 시간의 절반을 넘었습니다. smith 는
README.ko.md:73
먼저 있던 실패는 쫓지 않고 follow-up 으로 이름을 붙이며, 그 실행과 PR 사이에는

skills/verify/SKILL.md:250-251
  sealer's seal covers a tree nobody is still editing — which is why *nothing
  edits between the broad run and the PR* is a rule that seal rests on.
skills/verify/SKILL.md:273
edits — 121 after the first, 1 after the last. Not one of those runs survived
skills/verify/SKILL.md:276-277
Review rounds are edits you have already scheduled. Running the whole suite
before them measures a tree that is going to change.
skills/verify/SKILL.md:285
| **After the rounds settle** | full suite, lint, typecheck — **once** | `executed`, broad, once |
skills/verify/SKILL.md:385
holds the reason and the measurement — a run taken before the rounds is spent
skills/verify/SKILL.md:529
**Nothing edits between the broad run and the PR.** The tree that passed is
```

```python
# tests/test_broad_gate_rule.py:54
    assert "Nothing edits between the broad run and the PR" in scope
    assert "broad seal" not in scope

# tests/test_the_gate_names_every_step_ci_runs.py:172
        "third state, and a step with no row is a run that covers less than "

# tests/test_the_seal_is_taken_once_by_the_sealer.py:3974
        "the gate does not name the command it ran, so the sealer "
```

answer:

### 2. The gate's construction sweep takes a `seal` that ends a sentence out as a name, so the word is never refused

severity: should
location: `tests/test_one_word_one_meaning.py:431`
verdict: open
regression: round-1#1

The unit is `GATE_SEAL_NAMES` in `tests/test_one_word_one_meaning.py:427-440`,
which 42ff7d11 added. The frame (`questions.md` Q4 (a)) says nothing a person
reads calls the gate's run a seal. The fix built the sweep from round 1's
paste-ready block as given, and the defect came from that block: the name
alternative `\bseal[-_.][\w.-]*`, meant for `seal.py`, `seal-stamp` and
`seal_stamp`, also matches `seal.` closing a sentence. So the word is taken
out as a name before the refusal reads the line.

Why it matters. The case's docstring says the next spelling "is caught without
being listed", and that is the reason the case exists (contract §12). A
sentence that ends in the word, such as "there is nothing to seal.", is an
ordinary shape for a refusal to take, and the case passes on it.

Executed (probe rows 3 and 4, a `test_tmp_*` file run once and deleted each
time). At 981b0acc, `"the broad run is no seal."` and `# a run that passed is
not a seal.` were not refused, while `a seal; nothing ran` and `seals
nothing` were. With the alternative below, both sentence-final lines are
refused, the name forms `seal-stamp`, `seal_stamp.py`, `seal.py` and
`seal-mark.txt` are still taken out, and the four `GATE_SWEPT` files at
981b0acc still yield no line, so the case stays green on the tree.

In `GATE_SEAL_NAMES`, line 431:

```python
    r"|\bseal[-_.]\w[\w.-]*"
```

The case that holds it, after `test_the_gate_calls_its_run_no_seal_by_construction`.
Its first loop fails against line 431 as it stands at 981b0acc (probe row 3
measured both lines):

```python
def test_the_gate_sweep_reads_a_seal_that_ends_a_sentence():
    """#975 round 2. A name joins `seal` to more of the name; `seal.` that
    closes a sentence is the word, and the sweep refuses it."""
    for line in ('"the broad run is no seal."', "# a run is not a seal."):
        assert GATE_SEAL_WORD.search(GATE_SEAL_NAMES.sub("", line)), line
    for line in ("`seal-stamp --from`", "seal_stamp.py", "seal-mark.txt"):
        assert not GATE_SEAL_WORD.search(GATE_SEAL_NAMES.sub("", line)), line
```

answer:

### 3. spec.md S12 still states the sealer clause that 6f7aacb2 shortened, and no record says the two diverge

severity: should
location: `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/spec.md:99`, `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/spec.md:155`, `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/overview.md`
verdict: open
regression: round-1

The unit is `agents/sealer.md:99-100`, which 6f7aacb2 changed. The frame's
`spec.md` S12 says the `## Never` bullet "says it draws no stamp and that the
stamp is drawn in the orchestrator's session from the sealer's committed
`sealed` verdict, once per work item", and §*Scope*'s row at line 155 says
the same. The fix shortened the clause to "a stamp is drawn once from your
committed `sealed`", to bring the preload under #969's reference after phase
4's evaluation (the commit message's claim). The defect came from the fix:
the tree no longer says "in the orchestrator's session" or "per work item",
and `spec.md` still says it does. `phases/phase-4.md:22-33`, committed at
826cd0da while this round ran (records only, read), records the shortening
and why, but not that S12 and line 155 now state a clause the tree does not
hold.

Why it matters. The sealer reads `spec.md` against the tree. A sealer that
audits S12 finds its `Then` false at `agents/sealer.md:100`, and that is
grounds to withhold the verdict the stamp is drawn from.

The clause itself was judged and holds (read). It sits under `## Never`
beside "draw a stamp", it says the stamp is drawn from the sealer's committed
`sealed` and so not from the gate's run, and it says once. "Per work item" is
implied by a definition whose audit covers one work item. So the repair is
the record, not the clause. The preload was recounted (executed, probe row
6): 8,097 bytes of `agents/sealer.md` and 16,603 of
`skills/agent-contract/SKILL.md`, 24,700 in all, below 24,702.

The row for `overview.md` §*Where spec and implementation diverged*, which
phase 5 writes:

```text
| The sealer's `## Never` clause | S12 and §*Scope* say it reads that the stamp is drawn in the orchestrator's session from the sealer's committed `sealed` verdict, once per work item; 6f7aacb2 made it "a stamp is drawn once from your committed `sealed`" | the shorter clause | phase 4's evaluation failed rule 4 alone at 24,757 preload bytes against #969's 24,702; the shorter clause brings the preload to 24,700 and still says what the owner's rule says: drawn once, from the sealer's committed `sealed`, never from the gate's run |
```

answer:

## Confirmations

confirms: round-1#1
The eighteen lines of `skills/verify/scripts/broad_gate.py` read as the
record gave them (read, the fix diff), and the seam pin at
`tests/test_one_word_one_meaning.py:641` names "there is no command to run".
`test_the_gate_calls_its_run_no_seal_by_construction` fails against
a0ee12eb's `broad_gate.py` on exactly eighteen distinct lines and passes at
981b0acc (executed, probe rows 1 and 2). The sweep's own hole is finding 2,
in the unit this fix added.

confirms: round-1#3
`already_queued` now matches the work item's id alone, and `_queue_one`
queues nothing where `merge-base --is-ancestor <target> HEAD` fails
(`skills/verify/scripts/seal_stamp.py:980-1005`, `:1073-1083`, read). The
three-part split holds: `item_value` returns the digits before the first `-`
(`seal_stamp.py:491-495`), `write_values` names a file
`<nanoseconds>-<id>-<target>` (`:792-812`), and `_git` returns None on a
non-zero exit (`:958-966`). Both new cases fail against a0ee12eb's
`seal_stamp.py` and pass at 981b0acc (executed, probe rows 1 and 2), and
each isolates one check: in the re-seal case the target is an ancestor, so
only the id match stops it, and in the squash case the second clone holds no
file, so only the ancestor test stops it. `docs/the-review-record.md`
§*The stamp* states the three facts, and both cases are on its `Enforced
by:` line (`bin/rules --check` exit 0, probe row 1). One shape stays as
round 1 left it: in a second clone of the same branch, a commit that touches
a `sealed` guarantee with no new run still queues there, held only by the
sealer's `; earlier run:` row (read, not probed; a row below).

confirms: none
6f7aacb2's byte claim holds. The sealer's preload is 24,700 bytes, below
#969's 24,702 (executed, probe row 6). Whether the evaluation passes on it
is a row below.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Phase 4's evaluation of the sealer at 981b0acc, recorded as a pass in the records commit 826cd0da that landed while this round ran; this round read its clause paragraph and did not audit its figures | `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/phases/phase-4.md` | the sealer |
| Whether once per work item needs to hold for a commit touching a `sealed` guarantee in a second clone of the same branch with no new run, which only the sealer's `; earlier run:` row holds today | `skills/verify/scripts/seal_stamp.py:1071-1083` | the orchestrator, under the owner's delegation |
| Phase 5: `overview.md` and the changelog fragment, and the overview test that fails without them | `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/plan.md` row 5 | the orchestrator |
| The full suite, the repository-wide lint and the typecheck: `unverified`. Nothing in the fix pass's answers claims a broad run, which is honest | — | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_one_word_one_meaning.py tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/test_broad_gate_rule.py tests/test_the_gate_names_every_step_ci_runs.py tests/test_the_commit_gate_decides_at_the_commit.py tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py -q`, then `bin/test tests/test_the_seal_is_taken_once_by_the_sealer.py tests/test_the_rules_have_one_owner.py -q`, then `bin/rules --check`, in the clone at 981b0acc | 352 passed, exit 0; 395 passed, exit 0; exit 0, 494 targets in 60 files resolve |
| a0ee12eb's `skills/verify/scripts/seal_stamp.py` and `broad_gate.py` checked out over the clone's, then `bin/test` of `test_a_reseal_whose_row_lost_its_earlier_run_queues_nothing`, `test_a_squash_of_a_sealed_item_in_another_clone_queues_nothing` and `test_the_gate_calls_its_run_no_seal_by_construction` with `-p no:xdist`, then both files restored | 3 failed, exit 1; the sweep listed 18 distinct `broad_gate.py` lines; `git status` clean after the restore |
| `bin/test tests/test_tmp_round2_sweep.py -q -s -p no:xdist`, applying `GATE_SEAL_NAMES` and `GATE_SEAL_WORD` to five planted lines; the file deleted after | `"the broad run is no seal."` and `# a run that passed is not a seal.` not refused; `a seal; nothing ran` and `seals nothing` refused |
| the same file rewritten with the alternative `\bseal[-_.]\w[\w.-]*`, swept over the four `GATE_SWEPT` files and four planted lines; the file deleted after | no line of the tree refused; both sentence-final lines refused; `seal-stamp`, `seal_stamp.py`, `seal.py` and `seal-mark.txt` not refused |
| `git grep -n -F` over `tests/` and `evals/` of `between that seal`, `broad seal`, `those seals survived`, `seals a tree`, `a seal taken before`, `Sealing the whole suite`, `seals everything`, `a rule about that one seal`, `the one broad seal`, `covers less than`, `it sealed over` | one pin, `tests/test_broad_gate_rule.py:54`; the two message lines of finding 1 |
| `wc -c skills/agent-contract/SKILL.md agents/sealer.md` | 16,603 and 8,097, 24,700 in all |
