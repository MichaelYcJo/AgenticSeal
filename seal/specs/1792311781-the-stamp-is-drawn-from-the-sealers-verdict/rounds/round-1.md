# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — review round 1

target: 56172bbe against release/v0.22.1

## Findings

### 1. The gate's own refusals and comments still call its run a seal, and the sweep that should catch them lists spellings instead of reading the class

severity: must
location: `skills/verify/scripts/broad_gate.py:17`, `skills/verify/scripts/broad_gate.py:282-283`, `skills/verify/scripts/broad_gate.py:353`, `skills/verify/scripts/broad_gate.py:413`, `skills/verify/scripts/broad_gate.py:855`, `skills/verify/scripts/broad_gate.py:990`, `skills/verify/scripts/broad_gate.py:1001`, `skills/verify/scripts/broad_gate.py:1010-1011`, `skills/verify/scripts/broad_gate.py:1019-1023`, `skills/verify/scripts/broad_gate.py:1058`, `skills/verify/scripts/broad_gate.py:1064`, `skills/verify/scripts/broad_gate.py:1074`, `skills/verify/scripts/broad_gate.py:1168`, `skills/verify/scripts/broad_gate.py:2245`, `skills/verify/scripts/broad_gate.py:2263`, `skills/verify/scripts/broad_gate.py:2918`, `tests/test_one_word_one_meaning.py:372-411`, `tests/test_one_word_one_meaning.py:599-606`
verdict: fixed 42ff7d11

`questions.md` Q4 was answered (a) on 2026-10-18: the gate's sentences that
say `seal` for the gate's own run say `run` or `pass`, and the fix belongs to
this round's fix pass. Nothing has changed them yet. A person who meets
"there is no command to seal over" reads that the gate's run seals, which is
the reading #975 exists to remove.

Read. The printed sentences, each reaching a person through the gate's
stdout or stderr:

- `missing_row`, lines 990, 1010, 1011, 1019 ("there is no command to seal
  over", "If it is the command to seal over") and 1023 ("a session that
  picks a command here seals its own choice").
- `walker_refusal`, lines 1058 and 1064 ("there is no command to seal over").
- `not_as_written`, line 1168 ("A seal drawn from that 0 covers nothing
  that ran").
- `PARTITION`, line 2245, the reason `coverage_line` prints for the CLAUDE.md
  block step ("a repository that wants it sealed names it in the `Broad
  gate` row").
- `gate`, line 2918 (`has no HEAD to seal — nothing ran`).

The same class stands in the module's docstring and comments, which the next
person editing the gate reads: line 17 ("a seal taken over a command nobody
chose"), 282-283 ("seals itself", "named on the stamp by `tree`", a stamp the
gate no longer prints), 353 ("every seal is redirected"), 413 ("where the
gate sealed a branch green"), 855 ("the command this gate seals over"), 1001
and 1074 ("seal over"), and 2263 ("a seal that counted them").

Executed. A construction sweep over the four files in `GATE_SWEPT`, taking
out every name a `seal` word may legitimately be part of and refusing any
`seal` word left, reports exactly these 18 lines and nothing else (probe row
3). `test_the_gate_never_says_sealed` passes on the same tree (probe row 2),
because `GATE_PHRASES` lists the spellings somebody thought of and none of
these is among them. That is contract §12's failure in the check itself: the
class is "the gate's run called a seal", and a list of phrases narrows it
without closing it.

Pins: `tests/test_one_word_one_meaning.py:599` holds "never read it, and
there is no command to seal over" as the string-literal seam the fold case
reads. It must move to the new wording in the same commit. No other test
pins any of these sentences (`git grep -n -F` of each phrase in `tests/` and
`evals/`, probe row 4), so contract §14 asks for the new sweep below, which
pins their absence.

The replacements, line for line in `skills/verify/scripts/broad_gate.py`:

```text
17     nothing run**: no row at all, because a run over a command nobody
282-283
       # tree that breaks an arm passes itself — that is the stated cost, named
       # in the report by `tree` and caught at the pull request by the same scripts.
353    every run is redirected to the tree's copy, so it read `tree <version>`
413    # soon as the local ref falls behind — #423, where the gate passed a branch
855    from being the command this gate runs (#429). It also makes a
990    f"nothing reads it, and there is no command to run.\n{where}\n"
1001   # is the command to run.
1010   "commented out, and there is no command to run.\n"
1011   "If it is the command to run, take the row out of the "
1019   "there is no command to run — and choosing one is not this "
1023   "command here checks its own choice.\n"
1058   "there is no command to run."
1064   "So there is no command to run."
1074   # run a command nobody chose (#871, shape 7).
1168   "check has finished. A pass read from that 0 covers nothing that "
2245   "that wants it run names it in the `Broad gate` row",
2263   # judged. On any other base CI never asks them, so a run that counted them
2918   raise Refused(f"broad-gate: {root} has no HEAD to run over — nothing ran")
```

The sweep, in `tests/test_one_word_one_meaning.py` under `GATE_PHRASES`:

```python
# Every `seal` word the gate's files may carry is part of a name: a path under
# the `seal/` root, a script or a command (`seal-stamp`, `seal_stamp`,
# `seal mode`, `seal.py`, `seal-mark.txt`), the sealer, the chain arm's
# `--sealing` flag, the verdict word in backticks, the Seal Test, a work item
# the sealer sealed, and the fold markers that name spec directories.
# Anything else calls the gate's own run a seal (#975, `questions.md` Q4).
GATE_SEAL_NAMES = re.compile(
    r"<!--[^>]*-->"
    r"|\bseal/\S*"
    r'|"seal"'
    r"|\bseal[-_.][\w.-]*"
    r"|\bseal mode\b"
    r"|\bsealer\w*"
    r"|specseal\w*"
    r"|--sealing\b|(?-i:\b\w*SEALING\w*\b)"
    r"|`sealed`"
    r"|\bSeal Test\b"
    r"|\bsealed work item\b",
    re.I,
)
GATE_SEAL_WORD = re.compile(r"\bseal(?:s|ed|ing)?\b", re.I)


def test_the_gate_calls_its_run_no_seal_by_construction():
    """#975 Q4 (a). `GATE_PHRASES` lists the spellings somebody thought of,
    and "no command to seal over" was not one of them. This reads every line
    of the gate's files with its names taken out and refuses any `seal` word
    left, so the next spelling is caught without being listed. Red at
    56172bbe on 18 lines of `broad_gate.py`."""
    found = []
    for parts in GATE_SWEPT:
        for n, line in enumerate(read(*parts).splitlines(), 1):
            if GATE_SEAL_WORD.search(GATE_SEAL_NAMES.sub("", line)):
                found.append(f"{'/'.join(parts)}:{n}: {line.strip()}")
    assert not found, "\n".join(found)
```

And the seam pin at `tests/test_one_word_one_meaning.py:599`, which still
crosses the literal seam at `broad_gate.py:1057-1058` after the rewording:

```python
    joined = "never read it, and there is no command to run"
```

answer: the 18 lines reworded as the record gives them, and the seam pin at `tests/test_one_word_one_meaning.py` moved to `there is no command to run`. `test_the_gate_calls_its_run_no_seal_by_construction` added with `GATE_SEAL_NAMES` as given, with two changes: the verdict word in backticks is taken out lower-case only, so `` `SEALED` `` stays refused by this case as well as by the token case, and the comment says why `sealed_names` and `CHAIN_SEALING` need no entry (`_` is a word character) while `--sealing` and `chain_check.SEALING` do, per Q6 (a). `GATE_PHRASES` is kept: `spec.md` S1 names its phrases and the seam-safety case reads it. executed: the new case red at a0ee12eb on exactly the 18 lines this record lists, green after; `bin/test tests/test_one_word_one_meaning.py tests/test_broad_gate.py tests/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py tests/test_the_gate_names_every_step_ci_runs.py tests/test_the_seal_is_taken_once_by_the_sealer.py -q` 463 passed

### 2. Documents outside the gate still call its run a seal, and one moved paragraph still calls the stamp a run's

severity: should
location: `templates/config.md:27-28`, `skills/config/SKILL.md:53`, `skills/config/SKILL.md:81`, `skills/verify/SKILL.md:408-409`, `skills/verify/SKILL.md:471`, `docs/the-review-record.md:303-304`, `hooks/sealer-stamp.py:114`, `tests/test_broad_gate_rule.py:446`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:1213`
verdict: fixed 212db890

Claimed: phase 3's record says every sentence that called the broad gate's
run a stamp or a seal was found by sweeping the shipped documents for six
phrases, and reworded. Found: the sweep matched phrases within one line, and
it did not include the gate's refusal wording that Q4 has since reached.
Each sentence below is one an agent or a person reads and acts on.

Read, with the sweep executed across line breaks (probe row 5):

- `templates/config.md:27-28` and `skills/config/SKILL.md:53` say
  `broad-gate` exits 2 "because a seal taken over a command nobody chose
  seals nothing". This is the same claim as the gate's own absent-row
  refusal, which Q4 rewords.
- `skills/config/SKILL.md:81` says "the sealer sealed over its command
  (#429)". The sealer runs no command since #969, so the sentence now
  credits the sealer with a run it never takes.
- `skills/verify/SKILL.md:408-409` says the preflight "runs no suite, and
  seals nothing". Read beside the broad run, this says the broad run is what
  seals. It is pinned by `tests/test_broad_gate_rule.py:446`.
- `skills/verify/SKILL.md:471` says "A repository that wants checks of its
  own sealed names them in the `Broad gate` row". This is the document twin
  of `broad_gate.py:2245` in finding 1.
- `docs/the-review-record.md:303-304`, the budget paragraph moved from
  `docs/the-broad-gate.md`, says "one real run's stamp goes out per
  message". The stamp is no longer a run's. The phrase is broken across a
  line, which is why a `git grep -F "run's stamp"` sweep missed it. It is
  pinned by `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:1213`.
- `hooks/sealer-stamp.py:114` says "a file that is not a run's values",
  while the same docstring's other sentence was moved to "a stamp's values"
  in phase 3.

```text
templates/config.md:27-28
  `broad-gate` names the row and exits 2 with nothing run, because a run
  over a command nobody chose proves nothing. The section on it below says why

skills/config/SKILL.md:53
  because a run over a command nobody chose proves nothing. Show it as absent

skills/config/SKILL.md:81
  the broad run ran its command (#429). Put the prose under the table the

skills/verify/SKILL.md:408-409
  is not this run: it runs the gate's record arms, runs no suite, and writes
  nothing (#638).

skills/verify/SKILL.md:471
  repository that wants checks of its own run names them in the `Broad gate`

docs/the-review-record.md:303-304
  of a stamp's size, so one stamp of a real work item's size
  goes out per message and a second waits for the next turn. A seal past

hooks/sealer-stamp.py:114
  claimed, so a file that is not a stamp's values — whatever it fails on — is
```

The two pins move with them:

```python
# tests/test_broad_gate_rule.py:446
    assert "runs no suite" in said and "writes nothing" in said, said

# tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:1213
    assert "one stamp of a real work item's size goes out per message" in rule
```

answer: the seven sentences reworded and both pins moved, each pin seen red against the old documents first (executed: 3 failed, the third being the class member below). One paste-ready line did not hold: `skills/config/SKILL.md:53` as given made a 20-word run shared with `templates/config.md:27-28`, which `tests/test_no_passage_is_pasted_into_a_second_file.py` refused (executed), so it reads `because what a command nobody chose reports proves nothing`. The class, enumerated by a whitespace-folded sweep of the shipped tree for `seal` words near gate, run, suite or stamp words: also fixed are `templates/config.md:315` and `hooks/config.py:273` (the #429 twins, which credited the sealer with the run), and `skills/verify/SKILL.md`'s coverage section, which called the gate's run a seal three times (the heading `A run says what it did not answer`, `a green run covered`, `A run on a SpecSeal feature branch reads`), with its pin `tests/test_the_seal_is_taken_once_by_the_sealer.py::test_the_documents_name_the_ci_also_row` moved and an absence assertion added; the test docstrings and messages carrying the same sentences follow. Left, as Seal Test vocabulary the round puts to the owner: `the broad seal` and `the one broad seal` in `skills/verify/SKILL.md` (its line 251 defines that seal as the sealer's), `README.md`'s `that seal`, `Not one of those seals survived`, `seals a tree that is going to change`, and a default of `true` seals everything. executed: the pinning modules and `tests/test_docs_line_wrap.py`, `tests/test_no_passage_is_pasted_into_a_second_file.py` green

### 3. Once per work item rests on a row an agent writes and on one clone's files, so a fresh re-seal row or a squash in another clone draws a second stamp

severity: should
location: `skills/verify/scripts/seal_stamp.py:977-993`, `skills/verify/scripts/seal_stamp.py:1058-1063`, `docs/the-review-record.md:281-285`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`
verdict: fixed 33a5b676

The owner's rule in #975 is that a work item is stamped once, never twice.
The build holds it with two facts. The first is the `Target SHA` row's `;
earlier run: <sha> sealed`, which the sealer writes by instruction
(`agents/sealer.md:134-141`) and which no check holds on a real re-run. The
template test holds only the template. The second is a file name keyed on
the work item and the audited commit, which a later sealed verdict at a new
commit does not share. Neither covers a commit whose audited SHA is not in
its own history.

Executed (probe row 1, a `test_tmp_*` file over the module's own fixtures,
run once and deleted):

- P1. A sealed guarantee is committed and drawn. Then a fix is committed
  and the guarantee is rewritten `sealed` at the new commit with its row
  written fresh, without the earlier run. `post-commit` printed the queued
  line and a second values file stood beside the drawn one. That is two
  stamps for one work item.
- P3. A sealed guarantee is committed in one clone. The branch is
  `merge --squash`ed into `main` in a second clone of it. The squash commit
  queued a stamp there, although the work item was stamped in the first
  clone.
- P2, for contrast. The same squash in the same clone queued nothing,
  because the drawn file matched the name.

Both gaps close inside the clone, with no count beside the tree. The work
item's id alone decides whether a file stands, whatever commit it named. A
commit whose audited commit is not an ancestor of HEAD, such as a squash or
a cherry-pick of the guarantee onto another branch, queues nothing, because
the verdict was stamped where it was made. The earlier-run check stays for
the case neither covers: a re-seal in a second clone of the same branch. The
fail direction stays a missing stamp. A `Target SHA` that does not resolve
in the clone makes `merge-base` exit 128, and nothing is queued.

```python
def already_queued(common, ident):
    """True where a values file for work item `ident` stands under any
    session's directory of the clone, pending or drawn. A work item is
    stamped once (#975), whatever commit its guarantee audited, so the
    audited commit is not part of the question. A name is
    `<ns>-<ident>-<target>.json`; a file an older gate wrote is
    `<ns>-<tree>.json` and has no middle part to match."""
    root = os.path.join(common, VALUES_DIR)
    try:
        sessions = os.listdir(root)
    except OSError:
        return False
    for session in sessions:
        try:
            names = os.listdir(os.path.join(root, session))
        except OSError:
            continue
        for name in names:
            parts = name.split("-")
            if (
                len(parts) == 3
                and parts[1] == ident
                and name.endswith((PENDING, DRAWN))
            ):
                return True
    return False
```

In `_queue_one`, replacing lines 1058-1063:

```python
    if any(word == chain.SEALED for _sha, word in chain.earlier_verdicts(cell)):
        return None
    ident = item_value(name)
    if already_queued(common, ident):
        return None
    # The audited commit is in this commit's history. A squash or a
    # cherry-pick of the guarantee onto another branch, in this clone or
    # another, carries a verdict that was stamped where it was made.
    # Precondition: `target` resolves in this clone; where it does not,
    # `merge-base` exits 128 and nothing is queued.
    if _git(top, "merge-base", "--is-ancestor", target, "HEAD") is None:
        return None
    key = f"{ident}-{target}"
```

The two regression cases, in
`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` after
`test_a_recommit_of_the_same_guarantee_queues_no_second_file`. Each was seen
red against 56172bbe by probe row 1, where each queued a file:

```python
def test_a_reseal_whose_row_lost_its_earlier_run_queues_nothing(tmp_path):
    """#975, once per work item. The sealer ran again at a new commit and
    wrote its row fresh, without `; earlier run: <sha> sealed`: the clone
    already holds the work item's stamp, so nothing more is queued."""
    repo, _target, base = guaranteed(tmp_path)
    assert after_the_commit(repo)
    stop(repo)
    item = repo / "seal" / "specs" / ITEM_NAME
    (repo / "x.txt").write_text("a fix after the seal\n", encoding="utf-8")
    commit_all(repo, "a fix")
    new = git(repo, "rev-parse", "--short", "HEAD").stdout.strip()
    (item / "guarantee.md").write_text(
        guarantee_text(new, base, "sealed"), encoding="utf-8"
    )
    commit_all(repo, "the sealer again, its row written fresh")
    assert after_the_commit(repo) == ""
    assert len(queued(repo)) == 1, queued(repo)


def test_a_squash_of_a_sealed_item_in_another_clone_queues_nothing(tmp_path):
    """#975, once per work item. The guarantee was stamped in one clone; a
    squash of its branch in another clone carries the verdict onto a commit
    whose history does not hold the audited commit, so nothing is queued."""
    repo, _target, _base = guaranteed(tmp_path)
    assert after_the_commit(repo)
    other = tmp_path / "other"
    subprocess.run(
        ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
    )
    git(other, "switch", "-q", "main")
    git(other, "fetch", "-q", "origin", "feat/x:feat/x")
    git(other, "merge", "--squash", "feat/x")
    commit_all(other, "the squash, elsewhere")
    assert after_the_commit(other) == ""
    assert queued(other) == []
```

The sentence in `docs/the-review-record.md:281-285` that states the rule,
with both cases added to its `Enforced by:` line:

```text
nothing. `withheld` and `undecided` queue nothing. Once per work item is held
by what the clone and the tree carry, with no count beside them: a values
file already named for the work item, pending or drawn, under any session's
directory is not written twice, whatever commit it named; a commit whose
audited commit is not in its own history, a squash or a cherry-pick of the
guarantee elsewhere, queues nothing; and a `Target SHA` row whose `; earlier
run:` chain reads `sealed` was stamped at that run, which holds across
clones. The stamp carries what the records at the
```

answer: `already_queued` matches the work item's id alone, and `_queue_one` queues nothing where `merge-base --is-ancestor <target> HEAD` fails, as the record gives them; `queue_for_guarantee`'s docstring, the module comment above `GUARANTEE_PATH`, and `docs/the-review-record.md` §*The stamp* with both cases on its `Enforced by:` line state the three facts. This closes the failure scenario `plan.md` B1 accepted (a re-run whose row lost its earlier run); `spec.md` S8 stays true as a narrower case. executed: both new cases red at a0ee12eb (each queued a file), green after; `test_a_reseal_after_withheld_queues_the_stamp`, `test_a_second_sealed_verdict_queues_nothing`, `test_a_recommit_of_the_same_guarantee_queues_no_second_file` and `test_a_sealed_guarantees_commit_queues_one_stamp` green; `mutation-check` breaking the ancestor test (`if False:`) turned the squash case red, and breaking the id match (`parts[2]`) turned the re-seal and re-commit cases red; `bin/rules --check` exit 0

## Confirmations

confirms: none
S1 holds. The gate's heads are `GATE_PASSED`/`GATE_FAILED` at
`skills/verify/scripts/broad_gate.py:2814-2815`, and `main` prints the head,
the panel's rows as text and the uncommitted line, with no drawing and no
values file (`broad_gate.py:3045-3068`, read). The narrow run of
`tests/test_one_word_one_meaning.py` passed with
`test_the_gate_never_says_sealed` in it (executed, probe row 2).

confirms: none
Nothing draws a stamp from the gate's run any more. `write_values` has one
caller, `seal_stamp.py:1083` inside `_queue_one` (executed, `git grep -n
write_values` over the shipped tree), and every pre-#975 outcome name is
gone (executed, `git grep -n -F` of each).

confirms: none
S4 to S8 hold in the shapes the frame names (executed, the module's cases in
probe row 2). Two shapes the frame did not name also hold. A
`merge --squash` of a stamped branch in the same clone queues nothing (P2),
and one commit carrying two work items' sealed guarantees queues one file
and prints one line for each (P4) (executed, probe row 1).

confirms: none
The post-commit addition cannot fail a commit. `commitgate.post_commit`
returns 0 on every path. The module load and the queue sit under one guard
that also catches `SystemExit`, which `chain_check.py` raises at import when
it cannot read its grammar table (`hooks/commitgate.py:331-352`, read). git
ignores `post-commit`'s status in any case. The latency figure is phase 2's
and was not measured again (a row below).

confirms: none
S14 holds. `git diff --stat f6ae6db6 56172bbe -- hooks/git/` is empty
(executed), so no clone's stubs are rewritten. The cost of that is that
`hooks/git/post-commit.py`'s docstring still names the notice alone, which
the frame accepts.

confirms: none
Every `Enforced by:` target resolves (executed, `bin/rules --check`, exit 0,
492 targets in 60 files). This confirms phase 3's claim of the same.

confirms: none
Phase 3's claim that `SEALED` in the shipped tree is now only the stamp's
title row and label and `chain_check.py`'s verdict constant holds, apart
from `.github/scripts/release_seal.py`, which `spec.md` §*Scope* puts out
(executed, `git grep -n -F SEALED` outside records and tests).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether Q4 reaches names as well as sentences. The chain arm's flag `--sealing` prints as `--sealing:` before its notices inside the gate's run, and `seal_stamp.sealed_names` composes the gate's `BROAD GATE PASSED` line. Finding 1's sweep allows both as names | `skills/code-review/scripts/chain_check.py:207-211`, `skills/verify/scripts/broad_gate.py:151`, `skills/verify/scripts/seal_stamp.py:667` | the orchestrator, under the owner's delegation |
| The Seal Test's own vocabulary applied to a broad run, which phase 3 left on purpose: "Not one of those seals survived", "a default of `true` seals everything" | `skills/verify/SKILL.md:273-277`, `templates/config.md:223-224` | the owner |
| `SEALED` on the release seal's PNG | `.github/scripts/release_seal.py:126` | the owner (`spec.md` §*Scope* puts it out) |
| The post-commit latency, 343 against 333 ms and 375 against 336 ms, read from phase 2's record and not re-measured | `docs/the-commit-gate-inside-git.md:239-244` | the sealer's sample |
| Phases 4 and 5: the sealer's paid evaluation, `overview.md` and the changelog fragment | `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/plan.md` rows 4 and 5 | the orchestrator |
| The full suite, the repository-wide lint and the typecheck: `unverified`. The smith's phase records label the suite as not run broad, which is honest | — | the orchestrator's broad run |
| The spawn prompt asked the warden to commit this record; `agents/warden.md` §*Never* withholds that act, so the file is written and not committed | this file | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_tmp_once_per_item.py -q -s -p no:xdist` in the clone, the probe file deleted after | 4 passed, printing what each scenario queued. P1: a second values file beside the drawn one. P2: none. P3: one file in the second clone. P4: two files and two lines |
| `bin/test tests/test_one_word_one_meaning.py tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/test_the_commit_gate_decides_at_the_commit.py -q` | 247 passed, exit 0 |
| a Python sweep of the four `GATE_SWEPT` files, refusing any `seal` word left after `GATE_SEAL_NAMES` is taken out | 18 lines of `skills/verify/scripts/broad_gate.py`, listed in finding 1, and nothing else |
| `git grep -n -F` of each finding-1 phrase over `tests/` and `evals/` | one pin, `tests/test_one_word_one_meaning.py:599` |
| a Python sweep of the shipped tree with whitespace folded, for phrases that call the stamp a run's or the gate a stamper | `docs/the-review-record.md:303`, `hooks/sealer-stamp.py:114`, and compatibility sentences about older gates' files, which are true |
| `bin/rules --check` | exit 0, 492 targets resolve |
| `git diff --stat f6ae6db6 HEAD -- hooks/git/` | empty |
