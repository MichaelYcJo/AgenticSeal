# Review round 3: 1793188384-the-release-notes-are-kept-twice

target: 4eb31bb8, fixes 1a3e2560..4eb31bb8

This is the verifying round after round 2. It read the fix diff
`1a3e2560..4eb31bb8` in a `git clone --no-local` of the branch at
`4eb31bb8`, held in the round's scratch directory. The diff is three
commits: the orchestrator's `5087abed` on the frame, the fix pass's
`c8f6b31e`, and `4eb31bb8`, which commits round 2's record with the fix
pass's two lines per finding. The repository declares no `seal/parity.md`,
so this round has no `original:` line. Phase 5's S11 is the orchestrator's,
and this round did not judge it.

Round 2's coordinates were carried, not searched for again: the six
sentences of its finding 1, the phase 4 record and the two
`seal/follow-up.md` rows of its finding 2, and the 0.15.3 shape, a
directory restored inside the range, as the case the skip exists for. Every
verdict below was reached again. Round 2's `evidence: executed` searches
were re-run. Its probe was written again in a narrower form, because the fix
range changed no line of `fragments` (`git diff --stat 2edd0a2d..4eb31bb8`
on the script shows only the module docstring and the message in `main`).

## Findings

### 1. Ten more sentences state which fragments the note reads, or when the job fails, without the skip, and the sweep claimed the class was done

severity: should
location: `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:184-185`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:213-214`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:249-250`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:428-429`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:436`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:487`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/plan.md:9-10`, `.github/scripts/publish_release_note.py:64-66`, `.github/workflows/publish-release.yml:57-60`, `tests/github/test_publish_release_note.py:238-239`
evidence: executed `bin/test tests/github/test_tmp_round3_skip.py -q -s -p no:xdist`, `git grep -n -i -E 'added' -- ':!*/trail/rounds/*' ':!seal/threads/1*/trail/rounds/*' | grep -i -E 'fragment|range|commits? (after|in)|release.s commits'`, `git grep -n -E "commits?$|release's commits|commits (after|in)|range('s)? (added|commits)|no fragment|no changelog fragment|fragments? the (range|release)" -- ':!seal/threads/*/trail/rounds/*' ':!changelog'`
verdict: open
reopens: round-2#1

The close of round 2's finding 1 holds at the six coordinates that finding
named. `5087abed` rewrote the four frame sentences and `c8f6b31e` the module
docstring and the fragment, each as round 2 gave them. The close does not
hold for the class. The fix pass's answer claimed that its sweep (contract
rule 12) found every sentence stating the selection without the skip, and it
named the ones it left with a reason. Ten more stand, and the answer names
none of them. `c8f6b31e` also drew the class wider than round 2 did. It
rewrote the exit-code line, the empty-range message and A3, so the
sentences saying when the job fails are in the class by the pass's own
measure. Copies of those sentences are left as well.

The probe shows what these sentences now misstate. In a history where
`v1.2.2` holds one fragment, a settle on the release branch removes it, and
a later commit restores it before the merge tag `v1.2.3`, the range's
commits added a fragment. `git log --diff-filter=A` over the range lists it.
`fragments` returns `[]`, and `main` exits 1. The message it prints reads
"no commit after v1.2.2 up to v1.2.3 added a changelog fragment that v1.2.2
does not already hold". With the skip removed, the same reader returns the
restored entry. So "fails for a range that added no fragment" describes a
narrower condition than the code's. "Reads the fragments the release's
commits added" describes the reader without the skip.

The ten, by whose they are to fix:

- `frame/design.md:184-185`, *Data & interfaces*, **Exit codes**: "1 the tag
  is not `vX.Y.Z`, or its range added no fragment". This is the frame's copy
  of the line `c8f6b31e` rewrote at `publish_release_note.py:95-97`. The
  frame and the script it governs now give two conditions.
- `frame/design.md:213-214`, the `to:` text for
  `docs/branch-and-release.md` *Cutting a release*: "It goes red on a tag
  whose range added no fragment". The same `to:` text was amended at
  `:210-212` by `5087abed`, and this sentence was left.
- `frame/design.md:249-250`, the `to:` text for `docs/branch-and-release.md`
  *Work accumulates on a release branch*: "reads the fragments the release's
  commits added from the history at the tag". Round 2's search matched only
  "commits after the previous", and it missed this phrasing.
- `frame/design.md:428-429`, the `to:` text for `docs/release-checklist.md`
  *6. After the merge*: "builds it from the changelog fragments the
  release's commits added".
- `frame/design.md:436`, the next `to:` text in that section: "The job fails
  for a tag whose range added no changelog fragment".
- `frame/design.md:487`, *Removes*, the reason the hygiene step can go:
  "Every fragment the release's commits added is in the note by
  construction." This is false since `d60ca012`. The probe's restored
  fragment was added by a commit in the range and is not in the note.
- `frame/plan.md:9-10`, *Summary*: "reads the fragments the release's commits
  added from the history at the tag".
- `.github/scripts/publish_release_note.py:64-66`: "**It does fail for a
  range that added no fragment**". This is the same docstring whose
  exit-code line the pass rewrote 30 lines below.
- `.github/workflows/publish-release.yml:57-60`: "the note reads the
  fragments the commits after the previous version tag added". Round 2 left
  this line, because the skip does not change what has to be fetched. That
  is still true. But `c8f6b31e` rewrote the same clause at `:17` of this
  file, so the file now states the selection two ways. The clause is a
  statement of what the note reads, not only a reason for the fetch.
- `tests/github/test_publish_release_note.py:238-239`, the A1 case's
  docstring: "The body is the fragments the release's commits added". The
  pass rewrote A1's summary line at `:7-9` and judged this one a description
  of the stub's list. It is the statement of A1 that the case pins, so the
  module now gives A1 in two forms.

The four `to:` texts are the ones that matter beyond this work item. The
settle writes them into `docs/branch-and-release.md` and
`docs/release-checklist.md`. The rule on record would then say the job fails
only for a range that added no fragment, and that the note reads every
fragment the commits added. A later change that reads that policy against
the code would find the skip unexplained. The sealer reads the frame's
*Data & interfaces* against the script and would find two exit conditions.

These stay, re-derived this round. The docstring of `fragments` at `:189-190`
opens with "every changelog fragment a commit in `revisions` added", and the
same docstring states the skip at `:199-201`. The `ENTRIES` comment at
`test_publish_release_note.py:65` and the `entries` sentence at `:150`
describe values handed to a stub. The case names at `:251` and `:383` name
each case's own history, and neither history holds a restored fragment.
*Verification* rows S1 at `design.md:137` and S5 at `:141` each state one
history, and each is still true of the code. The alternative's name at
`plan.md:56` labels a choice made among the other ways to find a fragment,
and the skip is no axis of that comparison. The phase records and `gaps.md`
name the skip.

The fix, in place at each coordinate. The frame and the plan are the
orchestrator's to amend. The script, the workflow comment and the test
docstring are the fix pass's:

```text
frame/design.md:184-186, Exit codes:
- **Exit codes.** 0 published, already published, or a dry run. 1 the tag
  is not `vX.Y.Z`, or its range added no fragment the previous tag does not
  already hold.

frame/design.md:213-215, the to: text:
    so a work item a settle removed before the tag still has its entry. It
    goes red on a tag whose range added no fragment the previous tag does
    not already hold, which is the release shipping unexplained. The note
    opens with the release's theme, the

frame/design.md:248-250, the to: text:
    file*. No branch gathers them. `.github/scripts/publish_release_note.py`
    reads, from the history at the tag, the fragments the release's commits
    added and the previous version tag does not already hold, and writes
    each under an HTML comment naming its work item,

frame/design.md:428-429, the to: text:
  to: which builds it from the changelog fragments the release's commits
    added and the previous version tag does not already hold, with the title

frame/design.md:436, the to: text:
  to: The job fails for a tag whose range added no changelog fragment the
    previous version tag does not already hold; for

frame/design.md:487, the reason cell, its second sentence:
Every fragment the release's commits added and the previous tag does not already hold is in the note by construction.

frame/plan.md:9-11:
in between. `.github/scripts/publish_release_note.py` reads the fragments
the release's commits added and the previous version tag does not already
hold, from the history at the tag, and opens the note
with the release's theme from its milestone.
```

```python
# .github/scripts/publish_release_note.py:64-66
**It does fail for a range that added no fragment the previous tag does not
already hold**, which is the opposite direction on purpose. That is the
release shipping unexplained, and the fragments are the whole of what this
publishes.

# .github/workflows/publish-release.yml:57-60
          # The whole history and every tag: the note reads the fragments the
          # commits after the previous version tag added and that tag does not
          # already hold, and the title from the tagged commit's message, so
          # `git log -1 <tag>` resolves the tag itself rather than whatever the
          # runner happened to check out.

# tests/github/test_publish_release_note.py:238-239
        """A1. The body is the fragments the release's commits added, less those
        the previous tag holds, each under the marker naming its work item, and
        it links to no file in the tree."""
```

answer:

## Confirmations

confirms: round-2#2
`trail/phases/phase-4.md:83-85` now names `changelog/0.12.2.md` at `v0.23.1`
as the folded text, and that agrees with the same record at `:39-41` (read).
Executed: `grep -o` finds "`changelog/0.12.2.md` read at `v0.23.1`" twice in
`seal/follow-up.md`, once in each of the rows at `:47` and `:49`. Round 2's
search for any other place reading the file at `v0.12.2`, re-run with the
round records excluded, printed nothing and exited 1.

confirms: none
The sweep's five extra rewrites each hold against the code. The exit-code
line at `publish_release_note.py:95-97` gives the condition `main` tests at
`:659-668` (read). The message adds its clause only where there is a
previous tag. `held` is empty where `previous` is None, and `commit_range`
at `:182-185` then returns the tag alone, so `fragments` at `:215` has no
lower tag to skip against (read). The probe ran `main` on a range whose
one added fragment the previous tag holds: exit 1, and the message read
"added a changelog fragment that v1.2.2 does not already hold,
seal/threads/<work-item-id>/changelog.md" (executed). The header comment at
`publish-release.yml:17-19`, A1 and A3 at `test_publish_release_note.py:7-12`,
and the two emptied modules' docstrings each state the skip (read). S5's new
assertion at `:399` cannot pass against the message at `1a3e2560`. That
message read "added a changelog fragment, seal/threads/..." and holds no
"does not already hold" (read: the diff). So the pass's seen-red claim is
consistent with the old text. The diff adds no new case, only that
assertion, and the clause it pins is in no other case of the module (read).

confirms: none
The skip is still the reader's behaviour at the target. In the probe's
history the reader returned `[]`. With the skip line removed from the
source, it returned `[('1700000000-older', '- older entry')]` (executed).
`Test_module::test_a_fragment_the_settle_removed_reaches_a_note_tagged_on_a_merge`
passed in the narrow run.

confirms: none
The fix range's record edits are the fix pass's two lines per finding.
`git diff -U0 1a3e2560..4eb31bb8` on `round-2.md` changes two `verdict:`
lines and two `answer:` lines, and nothing else (executed). `c8f6b31e`
touches `publish_release_note.py` and `changelog.md`, which the location
line of finding 1 names, and `phase-4.md`, which finding 2's names (executed:
`git show --stat`). `5087abed` applied round 2's four frame blocks word for
word (read: the diff).

confirms: none
The narrow verification for this round passed. Executed in the clone: the 7
modules under `tests/` that `git grep -l` finds naming
`publish_release_note`, `publish-release.yml` or this work item's id ran with
`bin/test -q`: 103 passed, exit 0. `bin/seal layout --check` exited 0, and
`bin/seal rules --check` exited 0 with all 266 check lines holding. This is
not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| S11: every released version's note holds its file after the republish of the 26 | `frame/plan.md` phase 5 row | the orchestrator, in phase 5 |
| Whether the tag's job can list the milestones under `contents: write` alone (Q3, default (a)) | `.github/workflows/publish-release.yml` | the orchestrator, reading the log of the tag run of the release carrying this work |
| The full suite, the repository-wide lint and the typecheck: unverified | the branch at its last fix | the orchestrator, at `seal gate`, before the sealer is spawned |
| Step 3 of the update skill run by a session updating across a real release | `skills/update/SKILL.md` | the first person to update to the release carrying this work |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_tmp_round3_skip.py -q -s -p no:xdist`: a range whose one added fragment `v1.2.2` holds, restored after a settle on the release branch and tagged on a `--no-ff` merge; the reader as built and with the skip line removed; then `main` with `DRY_RUN=1` | first run: a collection `TypeError`, the probe joined a `str` path with `/`; after correcting the probe: added paths list `seal/threads/1700000000-older/changelog.md`, the reader as built `[]`, without the skip `[('1700000000-older', '- older entry')]`, `main` exit 1 with the message naming "that v1.2.2 does not already hold"; 1 passed, exit 0 |
| `git grep -n -E 'commit in that range added\|commits after the previous\|a commit after the previous' -- .github seal/threads/1793188384-the-release-notes-are-kept-twice ':!*/trail/rounds/*'`, round 2's search | the six coordinates, each now with the skip; `publish-release.yml:58` |
| `git grep -n -i -E 'added' -- ':!*/trail/rounds/*' ':!seal/threads/1*/trail/rounds/*' \| grep -i -E 'fragment\|range\|commits? (after\|in)\|release.s commits'` | the lines of finding 1 except `design.md:428-429`, the ones kept with a reason, and unrelated lines in `evals/` and `tests/` |
| `git grep -n -E` for a line ending in "commit" or "commits", "release's commits", "no fragment" and "fragments the range" or "fragments the release", round records and `changelog` excluded | adds `design.md:428`, whose "added" opens the next line |
| `git grep -n -E 'at \x60v0\.12\.2\x60\|v0\.12\.2:changelog' -- ':!*/trail/rounds/*'`, round 2's search, with the backtick written as a code point here | nothing printed, exit 1 |
| `grep -o` for "`changelog/0.12.2.md` read at `v0.23.1`" in `seal/follow-up.md`, counted | 2 |
| `bin/test -q` over the 7 modules the last confirmation names | 103 passed, exit 0 |
| `bin/seal layout --check`, `bin/seal rules --check` | exit 0, exit 0 |

The probe file was deleted after its run, with its bytecode, and
`git status --short` in the clone printed nothing.
