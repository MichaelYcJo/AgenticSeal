# 1791852614-survivor-check-reads-a-range-as-its-own-commits — review round 1

| Field | Value |
|---|---|
| Target SHA | 2af175bd2a3c90b755d9a65c45f2441977979f87 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #919 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `b6b89e8cb8e1690d047c4dde2582d73095b30f84..d3a8221f74b6c5fa304064b0ed297f24f9e1b7d1`, 2 commits |
| Contract changes | report → report, main, post-review-check.md, round-1-report.md, round-1.md, told_now, reverify, reverify_into, pytest |
| New units | not_owned (depth 1); test_a_two_dot_range_names_the_commits_it_does_not_read (depth 1); test_the_base_commit_a_two_dot_range_leaves_out_is_named (depth 1); test_a_range_whose_own_commits_cannot_be_listed_is_refused (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (a two-dot range whose start the branch merged reads silently clean) and 🟡 2 (a timeout in `own_commits` is a traceback at exit 1) |
| Loses a record or crashes | yes — 🟡 2, a `git log` over the 60 s timeout inside `own_commits` crashes the sweep with a traceback at exit 1 |

- [ ] Pass

## What this round was asked

Round 1 of #873, target 2af175bd against `origin/release/v0.21.1` at 321e9de1, over the whole build, phases 1–4. The reviewer was asked to judge the smith's divergences — the new `separator` unit, `Reads:` on `examine` and `survivors`, S3's control, two `Corrected ·` and 25 `Re-read ·` rows over 71 drifted, the owner sentence in `parse_range` alone, the home's `Enforced by:` line fold-check does not reach, Q1's measured cost — and `owned`'s refusal when `own_commits` returns None, which no case reaches, and `correction_check.py#parse_range` left alone.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | a two-dot range whose start the branch already merged reads only the commits after that merge and reports 0 removed, where it used to report the branch's survivors; the run never says which commits it left unread | `skills/code-review/scripts/survivor_check.py:526` | **fixed** `7f08b48f` | fixed at 7f08b48f; executed: old exit 1 and `copy.md` reported, new exit 0 and 0 removed, on S6's history spelled `base..feature`; `base...feature` still exit 1 |
| 🟡 2 | `own_commits` runs git with a 60 s timeout, and `subprocess.TimeoutExpired` escapes `main`, which catches `Refused` alone: a traceback at exit 1, the survivors code; the `None` branch is the narrower failure and no case reaches it | `skills/code-review/scripts/survivor_check.py:537` | **fixed** `7f08b48f` | fixed at 7f08b48f; read: `chain_check.py:916` sets `timeout=60`; `survivor_check.py:2429` catches `Refused` only; executed: the `git log` takes 0.025 s for 169 commits here |
| ⬜ 3 | the own-commits pass spawns two `cat-file` per commit and re-parses each blob, 23.4 s to 89.0 s on a 169-commit range | `skills/code-review/scripts/survivor_check.py:1385` | open | read, and Q1's figures in `phases/phase-2.md`; commissions no fix |
| 🟢 | `separator` as the one reader of the dots | `skills/code-review/scripts/survivor_check.py:460` | confirmed | `parse_range` and `owned` both ask it; `parse_range`'s return shape is unchanged for `whole_range` |
| 🟢 | S3's control is a history with the sentence already in `root` | `tests/test_the_sweep_reads_a_range_as_its_own_commits.py:197` | confirmed | the tree at the tip is equal, so the pool and the weights are too; the case asserts `code == 1` before comparing |
| 🟢 | 0.9.3 `S3` and 0.11.2 `S2` closed as `Corrected ·`, 25 `Re-read ·` | `seal/ledger/1791852614-survivor-check-reads-a-range-as-its-own-commits.md:10` | confirmed | each corrected row adds one exception or classification and matches the code; a re-read cannot restate a claim |
| 🟢 | the owner sentence kept in `parse_range` alone | `skills/code-review/scripts/survivor_check.py:474` | confirmed | one deletion turns rule 18's carrier case red (`phases/phase-3.md`) |
| 🟢 | the home statement's `Enforced by:` line, bound by no check | `docs/the-record-layout.md:168` | confirmed | the statement above it in the section carries no marker either; a marker would read this unshipped item as folded |
| 🟢 | `correction_check.py#parse_range` left alone | `skills/evidence-check/scripts/correction_check.py:736` | confirmed | it reads the merges inside a range on purpose, and its docstring claims nothing about the two spellings |

## Paste-ready fixes

```python
def not_owned(root, a, b, own):
    """The short SHAs of the commits `git rev-list --no-merges a..b` lists
    that `own` does not, oldest first; empty for `A...B` (`own` None).

    Reads: observed — git's list of the range's non-merge commits, against `owned`'s list; unknown refused

    A two-dot range is read by the commits it owns, and what else it lists
    is not read. Printed, so a run whose start is not where the person meant
    names the commits it left out rather than reporting a clean range."""
    if own is None:
        return []
    out = git(root, "rev-list", "--reverse", "--no-merges", f"{a}..{b}")
    if out is None:
        raise Refused(f"cannot list the commits in {a[:7]}..{b[:7]} in {root}")
    mine = {full for full, _short, _changes in own}
    return [full[:7] for full in out.split() if full not in mine]
```
```python
        unread = not_owned(root, a, b, own)
```
```python
    if unread:
        shown = " ".join(unread[:8]) + (" …" if len(unread) > 8 else "")
        print(
            f"  not read    {len(unread)} commit(s) in {a[:7]}..{b[:7]} the "
            f"range does not own: {shown}. For a whole branch write `A...B`, "
            "which is read at its two ends",
            file=out,
        )
```
```python
def test_a_two_dot_range_names_the_commits_it_does_not_read(tmp_path):
    """`base..feature` after the branch merged the base's tip resolves to
    the same two commits as `base...feature` and owns `f2` alone, so `f1`'s
    correction is not read. The report names `f1` as not read and names
    `A...B`, rather than reporting a clean range in silence. Red against
    the sweep without the line: exit 0 and nothing names `f1`."""
    repo = tmp_path / "repo"
    shas = history(
        repo,
        root={"other.md": doc("other", OWN_FOUND), "copy.md": doc("copy", OWN_FOUND)},
        f1={"other.md": doc("other", OWN_REPAIRED)},
    )
    code, text = sweep(repo, "base..feature")
    assert "not read    1 commit(s)" in text, text
    assert shas["f1"][:7] in text, text
    assert "write `A...B`" in text, text
```
```python
    try:
        commits = loaded.own_commits(root, a, b)
    except subprocess.TimeoutExpired:
        commits = None
    if commits is None:
        raise Refused(f"cannot list the commits {a[:7]}..{b[:7]} owns in {root}")
    return commits
```
```python
def test_a_range_whose_own_commits_cannot_be_listed_is_refused(tmp_path, capsys):
    """`own_commits` answers None where git fails and raises where its 60 s
    timeout expires. Either is unusable input, exit 2, never a traceback at
    exit 1, which is the survivors code."""
    import subprocess as sp

    repo = tmp_path / "repo"
    shas = history(repo)
    for failure in (None, sp.TimeoutExpired(["git", "log"], 60)):
        loaded = module()
        real = loaded.chain()

        class Stub:
            is_ancestor = staticmethod(real.is_ancestor)

            @staticmethod
            def own_commits(root, a, b, failure=failure):
                if failure is None:
                    return None
                raise failure

        loaded.chain = lambda: Stub
        code = loaded.main(["--range", f"{shas['f1']}..{shas['f2']}", "--root", str(repo)])
        err = capsys.readouterr().err
        assert code == 2, f"{failure!r}: exit {code}\n{err}"
        assert "cannot list the commits" in err, err
```

## Executed probes

| What was run | Result |
|---|---|
| `SPECSEAL_CASE_CEILING_S=600 bin/test tests/test_a_script_copied_alone_exits_2.py tests/test_a_process_record_drop_passes_the_readers.py tests/test_the_gate_asks_the_range_ci_will_ask.py tests/test_every_reader_ends_a_line_where_gfm_does.py -q` in the clone at `2af175bd`, the modules driving the sweep that the orchestrator's run did not name | exit 0, 229 passed |
| a one-off probe script (deleted after the run) building S6's history and sweeping `base..feature` and `base...feature` with the sweep at `321e9de1` and at `2af175bd` | `base..feature`: old exit 1, 1 removed, `copy.md` reported; new exit 0, 0 removed, nothing reported. `base...feature`: exit 1 for both |
| the same script: `f2` corrects a sentence in a file the merge brought in, with its twin in `copy.md`, over `f1..f2` | exit 0, 0 removed, for old and new alike: a limit of the two-ends count that existed before this work (Deferred) |
| the same script: the base adds a second copy of a sentence in one file and `f2` removes one, over `f1..f2` | exit 0, 0 removed, for old and new alike (Deferred) |
| `git log --ancestry-path --no-merges --no-renames --name-status -z 5f11923f~40..5f11923f`, timed | 0.025 s |
| the broad gate (full suite, repository-wide lint, typecheck) | not yet — the sealer's, after the rounds settle; this round did not run it |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| on a two-dot range, an own commit's correction is not measured where the two ends show no net loss at that path: in a file the merge brought in, or where the base added another copy in the same file. Old and new alike, so the cause is the two-ends count that alternative E kept | a new issue, not filed by this round | the orchestrator, who files it for the owner |
