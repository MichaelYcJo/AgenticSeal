# 1791852614 — round 1 report (warden)

Target SHA `2af175bd`, base `origin/release/v0.21.1` (`321e9de1`), the whole
build, phases 1 to 4. Read in a scratch clone of the worktree at the target
SHA, with a second clone at the base for old-against-new runs. Both are
outside the repository; nothing was written in the worktree but this file.

## How the findings relate

```
the fix — a two-dot range is read by the commits it owns
   ├─ 🟡 1  a two-dot range whose start the branch already merged now
   │        reads only the commits after that merge, and says nothing
   ├─ 🟡 2  the new call into chain_check.py can raise a timeout that
   │        main does not catch: a traceback at exit 1
   └─ ⬜ 3  the per-commit pass re-reads and re-parses every file per commit
```

Spec compliance holds for everything `spec.md` §*In* asks: S1 to S11 each
have a case or a check, the refusal text is pinned, and the smith's
divergences hold on their grounds (the 🟢 rows below). The two 🟡 are
shapes the spec did not build.

## 🟡 1 — a two-dot range whose start the branch merged reports nothing removed

**Executed.** `skills/code-review/scripts/survivor_check.py:526`
(`owned`) gives every two-dot range the own-commits reading. Take S6's own
history: `f1` corrects `other.md`, whose twin stands in `copy.md`, and then
the branch merges the base's tip `S1`. Run the sweep as `base..feature`,
with two dots:

| Sweep | exit | removed | `copy.md` reported |
|---|---|---|---|
| base `321e9de1`, `base..feature` | 1 | 1 | yes |
| target `2af175bd`, `base..feature` | **0** | **0** | **no** |
| target `2af175bd`, `base...feature` | 1 | 1 | yes |

`base` is an ancestor of `feature`, so `owned` does not refuse. The merge
base of the two ends is `base` itself, so `base..feature` and
`base...feature` resolve to the same two commits. The two spellings now give
opposite answers on the same pair. `git log --ancestry-path --no-merges`
from `S1` lists `f2` alone, so `f1`'s correction is filtered out of `gone`.
The report says *0 sentence(s) the range removed* and *no removed wording
is still standing*.

By the owner sentence this reading is correct, because the range owns `f2`
alone. The defect is that the run says so nowhere. This shape is the mirror
image of S1 (`f1..f2`): there the commit left unread is the base's, and here
it is the branch's own. Git topology cannot tell the two apart without
reading parent order, which the home refuses. The refusal this work added
names `A...B` only when the start is not an ancestor. When the start is an
ancestor, the same mistake gets no word at all.

Why it matters: `origin/<base>..HEAD` is the spelling git users type by
habit for "my branch", and a branch that has synced with its base is the
normal state at a pull request. Before this work that run reported every
survivor. After it, the run exits 0 and reports a clean range. This is the
*unknown passed* class `spec.md` §*Grounding* names as the one this work
exists to close.

Fix: print the commits a two-dot range lists but does not own, so the
reading is stated in the report itself. On S1's shape the new line names
`S1`, which is accurate, and no current case reads that line. The fix is
the paste-ready block under 🟡 1 below, with the case to plant.

## 🟡 2 — a slow `git log` inside `own_commits` is a traceback at exit 1

**Read.** `owned` calls `chain_check.py#own_commits`
(`skills/code-review/scripts/survivor_check.py:537`), which runs git
through the git helper at `skills/code-review/scripts/chain_check.py:916`,
with `timeout=60`. On expiry `subprocess.run` raises
`subprocess.TimeoutExpired`, and the call does not return None.
`main` catches `Refused` alone (`survivor_check.py:2429`), so the run dies
with a traceback, and the exit code is 1. This module's docstring defines
1 as *survivors*, and 2 as unusable input. Before this work the sweep's own
git helper had no timeout, so this crash path arrived with the new call.

The overview's `Not verified` row asks about the `None` branch at
`survivor_check.py:538`. That branch is reachable only when `git log` fails
after both ends resolved and `merge-base --is-ancestor` succeeded, which in
practice means missing objects. The wider failure, a timeout, never reaches
that branch, because it does not arrive as None.

Measured margin, **executed**: on this repository the same `git log` over
`5f11923f~40..5f11923f` (169 commits) took 0.025 s. So this path is far off
here. On a large repository, or on a machine as loaded as this one, it is
not.

Fix: turn the timeout into the refusal the `None` branch already writes. A
case with a stub chain module reaches both, which also answers the
overview's unverified row.

## ⬜ 3 — the own-commits pass reads each file again for every commit

**Read**, plus the smith's own figure from Q1. `own_changes`
(`survivor_check.py:1385`) runs two `cat-file --batch` processes per owned
commit (`:1402`) and re-parses each touched file twice. A commit's after
blob is the next commit's before blob for the same path, so half of that
parsing is repeated. Q1 measured 23.4 s rising to 89.0 s on a 169-commit
range. Q1 decided there would be no skip, and this note does not reopen
that. One `cat-file` request over every `<full>^:<path>` and `<full>:<path>`,
with the sentences cached by blob text, would remove most of the cost.
This note commissions nothing.

## The smith's divergences and the questions put to this round

- **`separator`** — one reader of the dots, asked by `parse_range` and
  `owned`. It keeps `parse_range`'s return shape, which `whole_range`
  reads. Sound.
- **S3's control** — comparing against a history with the sentence already
  in `root` keeps the tree at the tip, and so every phrase weight,
  identical. The spec's literal control cannot isolate the range. Sound.
- **Two `Corrected ·` rows and 25 `Re-read ·` rows** — the 0.9.3 `S3` row
  lists the exceptions to *fewer times at `b` than at `a`*, and the 0.11.2
  `S2` row lists the ways a path list is accounted for. This work adds one
  to each, which a re-read cannot record. Both corrected rows state the
  addition accurately against the code. `docs/the-evidence-ledger.md`
  provides the `Corrected ·` mechanism for a frozen release.
- **The owner sentence in `parse_range` alone** — that way one deletion can
  turn rule 18's carrier case red. `owned` points at it. Sound, though the
  sentence sits in the docstring of the unit that does not apply the
  reading.
- **The home statement's `Enforced by:` line** — the statement above it in
  the same section carries no marker either, so the line is read by people
  and bound by nothing. Adding a marker would make
  `survivor_check.py#retired_directories` read an unshipped item as folded.
  Consistent with the section.
- **`correction_check.py#parse_range` left alone** — its question is what
  a merge dropped. It walks `rev-list --merges a..b` on purpose, and its
  docstring makes no claim that the two spellings read the same. Right to
  leave it.
- **Q1** — the fix-pass ranges cost 0.28 s to 0.92 s. The 169-commit range
  is the one ⬜ 3 is about.
- **`Reads:` lines** — present on all nine units, and the five census lines
  are gone. The orchestrator's registry run covers this.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | a two-dot range whose start the branch already merged reads only the commits after that merge and reports 0 removed, where it used to report the branch's survivors; the run never says which commits it left unread | `skills/code-review/scripts/survivor_check.py:526` | open | executed: old exit 1 and `copy.md` reported, new exit 0 and 0 removed, on S6's history spelled `base..feature`; `base...feature` still exit 1 |
| 🟡 2 | `own_commits` runs git with a 60 s timeout, and `subprocess.TimeoutExpired` escapes `main`, which catches `Refused` alone: a traceback at exit 1, the survivors code; the `None` branch is the narrower failure and no case reaches it | `skills/code-review/scripts/survivor_check.py:537` | open | read: `chain_check.py:916` sets `timeout=60`; `survivor_check.py:2429` catches `Refused` only; executed: the `git log` takes 0.025 s for 169 commits here |
| ⬜ 3 | the own-commits pass spawns two `cat-file` per commit and re-parses each blob, 23.4 s to 89.0 s on a 169-commit range | `skills/code-review/scripts/survivor_check.py:1385` | open | read, and Q1's figures in `phases/phase-2.md`; commissions no fix |
| 🟢 | `separator` as the one reader of the dots | `skills/code-review/scripts/survivor_check.py:460` | confirmed | `parse_range` and `owned` both ask it; `parse_range`'s return shape is unchanged for `whole_range` |
| 🟢 | S3's control is a history with the sentence already in `root` | `tests/test_the_sweep_reads_a_range_as_its_own_commits.py:197` | confirmed | the tree at the tip is equal, so the pool and the weights are too; the case asserts `code == 1` before comparing |
| 🟢 | 0.9.3 `S3` and 0.11.2 `S2` closed as `Corrected ·`, 25 `Re-read ·` | `seal/ledger/1791852614-survivor-check-reads-a-range-as-its-own-commits.md:10` | confirmed | each corrected row adds one exception or classification and matches the code; a re-read cannot restate a claim |
| 🟢 | the owner sentence kept in `parse_range` alone | `skills/code-review/scripts/survivor_check.py:474` | confirmed | one deletion turns rule 18's carrier case red (`phases/phase-3.md`) |
| 🟢 | the home statement's `Enforced by:` line, bound by no check | `docs/the-record-layout.md:168` | confirmed | the statement above it in the section carries no marker either; a marker would read this unshipped item as folded |
| 🟢 | `correction_check.py#parse_range` left alone | `skills/evidence-check/scripts/correction_check.py:736` | confirmed | it reads the merges inside a range on purpose, and its docstring claims nothing about the two spellings |

## Executed probes

| What was run | Result |
|---|---|
| `SPECSEAL_CASE_CEILING_S=600 bin/test tests/test_a_script_copied_alone_exits_2.py tests/test_a_process_record_drop_passes_the_readers.py tests/test_the_gate_asks_the_range_ci_will_ask.py tests/test_every_reader_ends_a_line_where_gfm_does.py -q` in the clone at `2af175bd`, the modules driving the sweep that the orchestrator's run did not name | exit 0, 229 passed |
| a one-off probe script (deleted after the run) building S6's history and sweeping `base..feature` and `base...feature` with the sweep at `321e9de1` and at `2af175bd` | `base..feature`: old exit 1, 1 removed, `copy.md` reported; new exit 0, 0 removed, nothing reported. `base...feature`: exit 1 for both |
| the same script: `f2` corrects a sentence in a file the merge brought in, with its twin in `copy.md`, over `f1..f2` | exit 0, 0 removed, for old and new alike: a limit of the two-ends count that existed before this work (Deferred) |
| the same script: the base adds a second copy of a sentence in one file and `f2` removes one, over `f1..f2` | exit 0, 0 removed, for old and new alike (Deferred) |
| `git log --ancestry-path --no-merges --no-renames --name-status -z 5f11923f~40..5f11923f`, timed | 0.025 s |
| the broad gate (full suite, repository-wide lint, typecheck) | not yet — the sealer's, after the rounds settle; this round did not run it |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| on a two-dot range, an own commit's correction is not measured where the two ends show no net loss at that path: in a file the merge brought in, or where the base added another copy in the same file. Old and new alike, so the cause is the two-ends count that alternative E kept | a new issue, not filed by this round | the orchestrator, who files it for the owner |

## Paste-ready fixes

### 🟡 1

In `skills/code-review/scripts/survivor_check.py`, beside `owned`:

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

In `main`, after `own = owned(...)`:

```python
        unread = not_owned(root, a, b, own)
```

and pass `unread=unread` to `report`. In `report`, add the parameter
`unread=()`, and print this right after the `examined` line:

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

The case, in `tests/test_the_sweep_reads_a_range_as_its_own_commits.py`:

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

### 🟡 2

In `owned`, `skills/code-review/scripts/survivor_check.py:537`:

```python
    try:
        commits = loaded.own_commits(root, a, b)
    except subprocess.TimeoutExpired:
        commits = None
    if commits is None:
        raise Refused(f"cannot list the commits {a[:7]}..{b[:7]} owns in {root}")
    return commits
```

The case, which also reaches the `None` branch the overview left unverified:

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

## Regression tests to plant

- `tests/test_the_sweep_reads_a_range_as_its_own_commits.py` — the two
  cases above. Show each red first: the first against the sweep without the
  `not read` line, the second with the `try` removed (traceback).

## Facts for the evidence ledger

- The new row for 🟡 1's line, anchored on `report`, `main` and the case,
  once written. The S6 row's claim (`A...B` is read at its two ends) is
  unchanged.
- S7's row could add that a two-dot range that `own_commits` cannot list is
  refused at exit 2, anchored on `owned` and 🟡 2's case.

Needs a fix: yes — 🟡 1 (a two-dot range whose start the branch merged reads silently clean) and 🟡 2 (a timeout in `own_commits` is a traceback at exit 1)
Loses a record or crashes: yes — 🟡 2, a `git log` over the 60 s timeout inside `own_commits` crashes the sweep with a traceback at exit 1

The broad gate has not come due: two 🟡 stay open, and the sealer's run
waits for the rounds to settle.

## Proof block

Opened at `2af175bd`, in the scratch clone:
`seal/specs/1791852614-survivor-check-reads-a-range-as-its-own-commits/`
`spec.md`, `overview.md`, `questions.md`, `changelog.md`,
`phases/phase-2.md`, `phases/phase-3.md`;
`seal/ledger/1791852614-survivor-check-reads-a-range-as-its-own-commits.md`;
`skills/code-review/scripts/survivor_check.py` (module docstring head,
`git` through `read_blobs`, the loaders, `own_changes`, `corrected`,
`paired_across_paths`, `report`, `main`);
`skills/code-review/scripts/chain_check.py` (imports, `load`, `git`,
`is_ancestor`, `own_commits`);
`skills/evidence-check/scripts/correction_check.py` (`parse_range`, `merges`);
`docs/the-record-layout.md` §*A range owns the commits that descend from its
start*; `docs/review-chain-spec.md` around the sweep statements;
`.github/workflows/hygiene.yml` (the sweep step);
`skills/code-review/orchestration.md` and `agents/smith.md` (the sweep's
invocation); `tests/test_the_range_rule_states_no_shape.py`;
`tests/test_a_script_copied_alone_exits_2.py` (docstring);
`tests/test_the_gate_asks_the_range_ci_will_ask.py` (docstring and fixture);
`bin/test`; the full branch diff `321e9de1...2af175bd` for code, tests and docs.
Not opened: `plan.md`, `routing.md`, `phases/phase-1.md`, `phases/phase-4.md`,
and the 25 re-read rows beyond two.
