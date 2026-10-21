# 1792619407-the-replay-scaffold-and-reader-misread-rounds — review round 2

target: 4875eb7b, fixes 8ef3a12c..4875eb7b

## Findings

### 1. With a region left open, a closed fence holding a level-2 heading ends the findings section, and later findings vanish

severity: should
location: `evals/scripts/noninferiority.py:298-325`, `tests/test_a_rewritten_definition_proved_non_inferior.py:1093`
evidence: executed `python3 test_tmp_986_round2.py`
verdict: open
regression: round-1#2

The unit is `noninferiority.py#finding_rows`, which 0cc8be41 changed. Where `chain_check.py#unclosed` refuses the
text, it now splits `reader.gfm_lines(text)` at lines 313 to 314, the raw lines with no fence or comment blanked.
`spec.md` scope item 1 and `plan.md` row R3 say a finding in a shape the check refuses is still a row and never
vanishes. The fix read the whole record raw so that the findings an open region hid would count again. The defect
came from round 1's own fix block, which gave this branch and did not weigh a fence that is closed.

On raw lines, every `## ` line inside a closed fence is a heading. `finding_spans` ends the `## Findings` section
at the first one, and gives no rows when one reads `## Findings`. A paste-ready fix to a document is often a
fenced block of markdown headings, so the shape is a common one. The probe wrote three findings: finding 1's fix
was a fenced block opening with `## Not judged`, and finding 3 opened a comment that never closes.
`finding_rows` gave 1 row. The same record with every region closed gave 3 rows. With the fenced block opening
with `## Findings`, the record gave 0 rows. Before the fix, the readable split gave 3 rows for the first record,
because the open comment in finding 3 hid nothing after it. So on these records the fix lowers the false count
below what it was before. The shape round 1 named, an open comment in finding 1 with nothing fenced, still gives
its three rows, and `test_a_comment_that_never_closes_hides_no_finding_from_the_false_count` passes (executed).

The fix keeps `readable`'s lines up to the opener and reads the lines after it again on their own. A closed fence
after the opener then still hides its own headings, and a second open region is handled the same way. A case beside
the one at line 1093 adds a fenced `## Not judged` before an open comment and asserts three rows. This assumes
`gfm_lines` splits a text joined with newlines back into the same lines. `unclosed` reports the opener's line
1-based, so `[:opened]` keeps the opener's own line as `readable` left it.

```python
def unhidden(check, reader, text):
    """`readable`'s lines of TEXT, where a region nobody closed hides no line
    after the line that opened it: those lines are read again on their own,
    so a closed fence after the opener still hides its own headings."""
    lines = reader.readable(text)
    hidden = check.unclosed(reader, text, "")
    if not hidden:
        return lines
    opened = min(line for _rel, line, _why in hidden)  # 1-based
    rest = "\n".join(reader.gfm_lines(text)[opened:])
    return lines[:opened] + unhidden(check, reader, rest)
```

and in `finding_rows`, in place of the branch at lines 313 to 316:

```python
    lines = unhidden(check, reader, text)
```

answer:

### 2. Three texts say no git fetch brings the shipped code back, and a fetch naming the URL the tree holds does

severity: should
location: `evals/scripts/seed_defects.py:16`, `evals/scripts/seed_defects.py:282-283`, `seal/specs/1792619407-the-replay-scaffold-and-reader-misread-rounds/changelog.md:26`
evidence: executed `git grep -l github.com/MichaelYcJo/SpecSeal`, `sh evals/behaviour/warden/seeded-279a580b/scaffold.sh`
verdict: open
regression: round-1

The units are the module docstring of `seed_defects.py`, the docstring of `seed_defects.py#scaffold` and the
changelog fragment, each rewritten by 0cc8be41. `spec.md` scope item 6 says only that the clone keeps no copy of the
unmutated commit. The fix removed the remote, on the orchestrator's direction, and its texts claim more: that no
`git fetch` brings the shipped code back. The defect came from that wording, not from the frame or from the
removal, which works as built.

The claim is false. In each of the four clones from this round's scaffold runs, `git remote` prints nothing, so a
bare `git fetch` has nowhere to go. But the checked-out tree names the repository's GitHub URL in 7 to 14 tracked
files. A `git fetch` that names that URL brings back the release branches, which hold the shipped code. Each case
prompt also names the pull request numbers, `(#837) (#879)` in `seeded-279a580b`'s. The owner will weigh Q5 on
these texts, and so will the sealer when it reads what the scaffold leaves. A reader told that no fetch reaches
the shipped code reads the network route as closed. The fix says what the removal does, and the remaining routes
go to the Q5 row of `## Not judged` below.

```text
seed_defects.py, module docstring:
  ...the objects, and a `git fetch` with no URL has no remote to fetch from.

seed_defects.py#scaffold:
  ...Then the remote goes, so a `git fetch` with no URL has nowhere to fetch
  from, and the base ref round 1 names is written again...

changelog.md:
  ...the scaffold removes the remote, so a bare `git fetch` fetches nothing,
  then expires the...
```

answer:

## Confirmations

confirms: round-1#1
The case now hands the scaffold `repo.as_uri()`
(`tests/test_a_rewritten_definition_proved_non_inferior.py:2548`), with the comment the fix block gave. On macOS,
`bin/test` over the four touched cases passed 4 of 4 (executed). Whether the Windows leg passes is still to come
from run 39691387210, named in `## Not judged`.

confirms: round-1#3
`noninferiority.py#apart` reads the text's JSON form with the scan's own `refused_domains` and
`refused_user_paths`, so the pattern has one home. The probe masked eight texts and scanned each written side line
by line. Every refusal was cleared: the user root before a line break, before a quote, before a tab and before a
backslash, a host after a line break and after U+0001. A clean record and a `location:` line holding a backslash
came back unchanged. So `apart` sets nothing on a line a grader reads (executed). The loop ends because each pass
sets one space or stops, and cdfd5f95 bounds it at the text's starting length. Each pass encodes the whole text
again, so the cost grows with the number of spaces set: 300 lines opening with a host, in about 24 KB, took 3.9
seconds (executed). That is acceptable for a record and is not raised.

confirms: round-1#4
All four regenerated scaffolds exited 0 in empty directories (executed). In each clone, HEAD's committer, email and
committer date equal its author's and the original target's, for example `2026-10-08T08:47:45+09:00` for
`seeded-279a580b`. No commit in these clones is signed, so no signature marks HEAD either (executed: `%G?` reads `N`
on the branch, and the two original targets read carry no `gpgsig`). `git remote` and `config --get-regexp ^remote`
print nothing. The refs are the branch and round 1's base ref, which `update-ref` wrote again after
`git remote remove origin` (`refs/remotes/origin/release/v0.21.0` twice, `release/v0.22.2` and `release/v0.22.1`).
S10 held in all four clones: `git grep` for the item's `rounds/` exits 1 and the directory is absent;
`cat-file -e` of the original target exits 128; `grep -rl` of it under `.git` outside the objects exits 1; and
`fsck --unreachable --no-reflogs` prints nothing.

confirms: round-1#5
`spec.md` scope item 5 now names each case's base ref: v0.21.0 for two cases, v0.22.1 for one, both gone, and
v0.22.2, which the remote still has. That matches what round 1 read at each squash commit. `overview.md`'s
base-ref row and `phase-2.md` point at it and state no count. 5020c9e8 made the change for those two records, and
the framer's 4875eb7b made it for `spec.md` (read).

confirms: none
62b57edb, the orchestrator's change to round 1's record, rewrote two prose lines of finding 3 in words and touched
no labelled line, heading, fix block or verdict (read: `git diff ed2739b6..4875eb7b` over `rounds/round-1.md`).
The fix pass's own changes to that record are the five `verdict:` and `answer:` lines, as its rule allows.

Carried from round 1 rather than re-established: the four round 1 bases equal each branch's fork point, and Q3's
`--list` order. Neither commit in the fix diff touches `ref_base` or the case selection. Re-derived this round:
every verdict above, the S10 checks, and the mask's behaviour.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether finding 1's `as_uri()` fix fetches a SHA under git for Windows | `tests/test_a_rewritten_definition_proved_non_inferior.py:2548` | the orchestrator, from `tests` run 39691387210 |
| With the remote gone, two routes to the shipped code remain. 7 to 14 tracked files of each tree name the GitHub URL, which a `git fetch` naming it reaches. Each prompt names the pull request numbers, which `gh pr diff` reads where `gh` is signed in. Whether either stands beside Q5 is a value for a person | `evals/behaviour/warden/seeded-279a580b/prompt.md` | the repository owner, with `questions.md` Q5 |
| The full suite, the repository-wide lint and the typecheck at 4875eb7b, labelled `unverified` here | the branch | the orchestrator, at its one broad run |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_986_round2.py` in the scratch clone at 4875eb7b | Exit 0. A: all eight edge texts scanned clean in the written side, and the clean record and the backslash `location:` line came back unchanged; 300 host lines took 3.9 s and set 299 spaces. B: open comment in finding 3 plus a fenced `## Not judged` in finding 1 gave 1 row, the same record closed gave 3, and a fenced `## Findings` gave 0. An open comment in finding 1 plus a fenced level-2 heading in finding 2 gave 2 |
| `sh <case>/scaffold.sh` for the four seeded cases, each in an empty scratch directory | Exit 0 each, then the refs, the remote, the committer fields and the S10 checks, as `confirms: round-1#4` gives them |
| `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist -k "seeded_scaffold or never_closes or kept_record_is_masked or scan_loads"` | 4 passed, 118 deselected, exit 0 |
