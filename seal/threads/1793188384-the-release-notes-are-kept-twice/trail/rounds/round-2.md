# Review round 2: 1793188384-the-release-notes-are-kept-twice

target: 2edd0a2d, fixes 65c06518..2edd0a2d

This is the verifying round after round 1. It read the fix diff
`65c06518..2edd0a2d` in a `git clone --no-local` of the branch at
`2edd0a2d`, held in the round's scratch directory. The repository declares
no `seal/parity.md`, so this round has no `original:` line.

Round 1's coordinates were carried, not searched for again: the 0.22.4
fragment `seal/specs/1792926874-the-records-carry-no-comment-and-the-readers-drop-it/changelog.md`,
the release's merge-tagged shape, `b38adc46` as the commit that restored two
0.15.3 directories, the released files at `v0.23.1` as the source of each
release's markers, and `skills/settle/scripts/rule_changes.py#parse` as the
reader of `## Rule changes`. Every verdict below was reached again. Round
1's `evidence: executed` lines were re-run, and its probes were written
again from round 1's `## Probes` rows.

## Findings

### 1. Six sentences still say the note reads every fragment the range added, and since `d60ca012` the reader skips one the previous tag holds

severity: should
location: `.github/scripts/publish_release_note.py:19-21`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:31-32`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:208-209`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:313-314`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/questions.md:9`, `seal/threads/1793188384-the-release-notes-are-kept-twice/changelog.md:3`
evidence: executed `bin/test tests/github/test_tmp_round2_fragments.py -q -s -p no:xdist`, `git grep -n -E 'commit in that range added|commits after the previous|a commit after the previous' -- .github seal/threads/1793188384-the-release-notes-are-kept-twice ':!*/trail/rounds/*'`
verdict: fixed c8f6b31e

`d60ca012` gave `fragments` a second arm. A fragment that the range's lower
tag already holds is skipped, even where a commit in the range added it again
by restoring its directory (0.15.3). The probe showed the arm is real
behaviour. In the case's history, the fixed reader returned only
`1700000001-first`. The same reader with the skip removed also returned
`1700000000-older`, the restored fragment.

`frame/design.md` *Data & interfaces* now states the skip, after
`2edd0a2d`. Six other sentences still state the selection as it was before
`d60ca012`: every fragment a commit in the range added. Each one now
describes the mutant, not the reader that was built:

- `publish_release_note.py:19-21`, the module docstring: "The fragments are
  the ones the commits after the previous `vX.Y.Z` tag added". `d60ca012`
  rewrote the docstring of `fragments` and left this one.
- `frame/design.md:31-32`, *Scope* item 1: "reads every
  `seal/threads/<work-item-id>/changelog.md` that a commit in that range
  added".
- `frame/design.md:208-209`, the `to:` text of a `## Rule changes`
  operation on `docs/branch-and-release.md` *Cutting a release*.
- `frame/design.md:313-314`, the `to:` text of the operation on
  `docs/the-record-layout.md` that rewrites the gather's paragraph.
- `frame/questions.md:9`, the answer to where the work items are found.
- `changelog.md:3`, this work item's fragment, which becomes the release
  note and which `seal pr-body` copies into the pull request body.

Two of these are a danger beyond this work item. The settle writes the
operations at `:208-209` and `:313-314` into the policy root, so the rule
of record would say that a restored fragment goes into the note. A later
change that reads that policy against the code would find the skip
unexplained and could remove it. The sealer reads *Scope* item 1 against the
tree and finds an exclusion that the scope does not state.

The search also found two more lines, and they stay as they are. The comment
at `.github/workflows/publish-release.yml:56-57` says why the job fetches
the whole history, and the skip does not change what has to be fetched.
`frame/plan.md:56` names the chosen approach in a table that compares where
a fragment is read, and the skip does not change that comparison.

This finding carries neither a `reopens:` nor a `regression:` line. Round 1's
finding 1 closes, and its close holds where that finding named. These six
sentences stand in units that no commit of the fix range changed. They were
true of the code until `d60ca012` and stopped being true at it.

The fix, in place at each coordinate. The frame, its questions and its rule
changes are the orchestrator's to amend. The docstring and the fragment are
the fix pass's:

```text
.github/scripts/publish_release_note.py:19-21:
in the tree. The fragments are the ones the commits after the previous
`vX.Y.Z` tag added and that tag does not already hold, each read at the
newest commit of that range whose tree holds it, so a work item a settle
removed before the tag still has its entry.

frame/design.md:31-32, Scope item 1:
   parent, and reads every `seal/threads/<work-item-id>/changelog.md` that a
   commit in that range added and the previous tag does not already hold: a
   fragment that tag holds was released there, though a commit in the range
   restored its directory (0.15.3). Each fragment's text is the blob at the newest

frame/design.md:208-209, the to: text:
  to: The fragments are the ones the commits after the previous `vX.Y.Z`
    tag added and that tag does not already hold, each read at the newest
    commit of that range that holds it,

frame/design.md:313-314, the to: text:
    `.github/scripts/publish_release_note.py` reads every fragment the
    commits after the previous `vX.Y.Z` tag added and that tag does not
    already hold, from the history, so a

frame/questions.md:9:
  the history: every fragment a commit after the previous version tag added
  and that tag does not already hold,

changelog.md:3, the clause:
now reads every fragment the commits after the previous version tag added and that tag does not already hold, from the history at the tag,
```

answer: Holds. The orchestrator's `5087abed` rewrites the four frame sentences. This pass's `c8f6b31e` rewrites the module docstring at `publish_release_note.py:19-21` and the clause in `changelog.md:3`, each as the round gives it. The sweep (contract rule 12) found five more sentences that state the selection without the skip, and the same commit rewrites them. They are the docstring's exit-code line, the empty-range message in `main`, `publish-release.yml:17`, the A1 and A3 lines of `tests/github/test_publish_release_note.py`'s summary, and the docstrings of the two emptied modules. The message is something a person reads, so S5 now asserts its new clause, `that v1.2.2 does not already hold`. That assertion failed against the old message and passes after the change (executed). These stay as they are: `publish-release.yml:56-57` and `frame/plan.md:56` for the round's reasons; `test_publish_release_note.py:63`, `:148` and `:236`, which describe the list the cases' stub of `fragments` returns, not the selection rule; and the phase records and `gaps.md`, which already name the skip. Executed: the 5 modules naming `publish_release_note` or this work item's id, 91 passed, exit 0; `ruff check` 0, `ruff format --check` 0, `seal layout --check` 0, `seal rules --check` 0.

### 2. The phase 4 record says the two follow-up rows read the 0.12.2 file at `v0.12.2`, and both rows say `v0.23.1`

severity: should
location: `seal/threads/1793188384-the-release-notes-are-kept-twice/trail/phases/phase-4.md:83-85`
evidence: read `seal/follow-up.md:47`, `seal/follow-up.md:49`, `seal/threads/1793188384-the-release-notes-are-kept-twice/trail/phases/phase-4.md:39-41`, `seal/threads/1793188384-the-release-notes-are-kept-twice/trail/phases/phase-4.md:83-85`
verdict: fixed c8f6b31e

Round 1's finding 3 was about one false fact: that the 0.12.2 file is read
at its own tag, `v0.12.2`, which holds no such file. That finding listed the
frame's two sentences, and `ce0105d9` rewrote both. A third instance of the
fact stands in the phase 4 record, and round 1 did not list it. At
`phase-4.md:83-85` the record says each `seal/follow-up.md` row "names the
v0.12.2 GitHub Release as the released copy and `changelog/0.12.2.md` at
`v0.12.2` as its folded text". In fact both rows, `seal/follow-up.md:47` and
`:49`, say "`changelog/0.12.2.md` read at `v0.23.1`". The same record
already says `v0.23.1` at `:39-41`. So the record now contradicts itself,
and only one of its two sentences matches the tree.

The sealer re-runs a sample of the crafter's claims against the tree, and
this one fails when it is opened. `db3c20cf` corrected what round 1 found
false in `phase-1.md`, `phase-2.md` and `gaps.md`, and it did not touch
`phase-4.md`. The line is outside the fix diff. It turned up while this round
enumerated the class of finding 3, so it is reported as a new finding and
not on a `reopens:` line. Round 1's finding 3 named the frame alone, and the
close holds there.

The fix, in place:

```text
phase-4.md:84-85:
names the v0.12.2 GitHub Release as the released copy and `changelog/0.12.2.md`
at `v0.23.1` as its folded text. Each says a published note is never rebuilt,
```

answer: Holds; fixed in place as given at `phase-4.md:84-85`. A search for other places that read the 0.12.2 file at `v0.12.2` found none: `git grep -n -E 'at \`v0\.12\.2\`|v0\.12\.2:changelog'`, with the round records excluded, printed nothing (executed).

## Confirmations

confirms: round-1#1
`fragments` at `.github/scripts/publish_release_note.py:186-232` passes
`--full-history` to the per-path log and skips a path the lower tag holds.
Executed: this round wrote round 1's comparison probe again. The fixed reader,
with both fragment roots read, matched each released file's markers at
`v0.23.1` for all 26 releases from 0.14.0 to 0.23.1, and the list of
mismatches was empty. Round 1's two `git log` commands on the 0.22.4
fragment were re-run. The default form printed no commit, and
`--full-history` printed `de11df75` and then `97bf7a9a`. The same probe
removed each arm from the case's history in turn. Without `--full-history`
the reader returned `[]`. Without the skip it also returned the restored
`1700000000-older`. So
`Test_module::test_a_fragment_the_settle_removed_reaches_a_note_tagged_on_a_merge`
fails when either arm is removed. That shows each arm pinned, and it shows
nothing about shapes no case builds. `frame/design.md:156-165`, as amended
at `2edd0a2d`, states both arms as the code has them (read). Finding 1
above is the six sentences this close left standing.

confirms: round-1#2
Step 3 of `skills/update/SKILL.md:72-107` downloads the list to a file and
prints only the span. Executed: this round piped the skill's block, lines
81 to 102, to `bash` as written. With `old=0.22.4` and `new=0.23.1` it
printed 16,772 bytes holding `## v0.23.0` and `## v0.23.1`, with
`curl exit 0` among them. The 16,760 bytes that `phase-2.md` reports plus the
12-byte `curl exit 0` line make the same figure. With `old` equal to `new`
it printed only the `curl` line. Round 1's size command, re-run, gave
897,660 bytes with HTTP 200, so the whole list is still close to a megabyte.
The quoted arguments `"$old" "$new"` read as two arguments: the run would
not have printed the span otherwise. The extended S8 case passed in the
narrow run. With `old` empty, the filter stops with a `TypeError` traceback
and prints no release. Step 3's "the list holds no release in that span"
covers that case, so the session goes on to step 4, and it is no finding.

confirms: round-1#3
`frame/design.md:97-100` and `frame/questions.md:13-17` now read the file at
`v0.23.1` (read). Executed: `git cat-file -e` exits 128 for
`v0.12.2:changelog/0.12.2.md` and for `v0.18.0:changelog/0.18.0.md`. It exits
0 for `v0.18.1:changelog/0.18.1.md` and for `v0.23.1:changelog/0.12.2.md`, so
the new "only from `v0.18.1`" in `questions.md` holds. The instance that
round 1 did not list is finding 2.

confirms: round-1#4
Executed: the rule-change probe was written again and parsed the frame's
section with no error. It found 37 operations, and every `from:` text was
found in the section that the operation names, the two that `ce0105d9` added
among them. `skills/verify/scripts/unverified_check.py:257` no longer names
the changelog marker (read). Round 1's sweep, re-run outside `docs/` and
`seal/threads/`, finds only `tests/skills/test_unverified_check.py:665-673`.
That is a helper which phase 3 kept in the test, and it reads the marker's
shape through `live_lines` to test `live_lines`, not the gather (read).

confirms: none
The fix pass wrote two lines per finding in `round-1.md`, and nothing else.
Executed: `git diff -U0 65c06518..2edd0a2d` on the record changes four
lines labelled `verdict:` and four labelled `answer:`. Each `fixed` commit touches a path
that its finding's `location:` names (`git show --stat`).

confirms: none
The new case covers what its group does not. S1,
`Test_main::test_the_note_is_built_from_the_fragments_the_range_added`, builds
a linear history tagged on the settle commit. The new case builds a
`--no-ff` merge tag and a restored directory (read). `bin/seal layout
--pairs` exited 0 and names no pair for this module (executed).

confirms: none
The narrow verification for this round passed. Executed in the clone: 34
test modules ran with `bin/test -q`, 2511 passed, 9 skipped, exit 0. They are
every module under `tests/` that `git grep -l` finds naming
`publish_release_note`, `skills/update/SKILL.md`, `unverified_check`,
`test_release_hygiene`, `test_publish_release_note` or this work item's id;
`tests/censuses.py` is a helper and was left out. `bin/seal layout --check`
exited 0. `bin/seal rules --check` exited 0, with all 266 check lines
holding. This is not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| S11: every released version's note holds its file after the republish of the 26; v0.2.0's note was edited and 25 wait on the owner | `frame/plan.md` phase 5 row | the orchestrator, in phase 5 |
| Whether the tag's job can list the milestones under `contents: write` alone (Q3, default (a)) | `.github/workflows/publish-release.yml` | the orchestrator, reading the log of the tag run of the release carrying this work |
| The full suite, the repository-wide lint and the typecheck: unverified | the branch at its last fix | the orchestrator, at `seal gate`, before the sealer is spawned |
| Step 3 of the update skill run by a session updating across a real release | `skills/update/SKILL.md` | the first person to update to the release carrying this work |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_tmp_round2_fragments.py -q -s -p no:xdist`: round 1's comparison with both roots read, and the merge-tagged case with each arm removed | 26 compared, mismatched list empty; case history: fixed `[('1700000001-first', '- first entry')]`, no `--full-history` `[]`, no skip both entries; 2 passed, exit 0 |
| `git log --format=%h v0.22.3..v0.22.4 --` the 0.22.4 fragment, then with `--full-history` | default: no commit; with `--full-history`: `de11df75` then `97bf7a9a` |
| `git grep -n -E 'commit in that range added\|commits after the previous\|a commit after the previous' -- .github seal/threads/1793188384-the-release-notes-are-kept-twice ':!*/trail/rounds/*'` | the six lines in finding 1, and `.github/workflows/publish-release.yml:57` |
| step 3's block, lines 81 to 102 of `skills/update/SKILL.md`, piped to `bash` with `old=0.22.4 new=0.23.1`, then `old=new=0.23.1`, then `old` empty | 16,772 bytes, `## v0.23.0` and `## v0.23.1`, `curl exit 0`; only the `curl` line; a `TypeError` traceback, no release printed |
| curl of the releases list from the marketplace clone's `origin`, written to /dev/null with the size printed | 897660 bytes, HTTP 200, exit 0 |
| `git cat-file -e` for each of `v0.12.2`, `v0.18.0`, `v0.18.1` and `v0.23.1` holding its own file, and for `v0.23.1:changelog/0.12.2.md` | 128, 128, 0, 0; then 0 |
| `bin/test tests/skills/test_tmp_round2_rule_froms.py -q -s -p no:xdist` | first run: `FileNotFoundError`, the probe joined `docs/` twice; after correcting the probe, no parse error, 37 operations, 0 `from:` texts missing, exit 0 |
| `bin/seal layout --pairs` | exit 0, no pair naming `tests/github/test_publish_release_note.py` |
| `bin/test -q` over the 34 modules the last confirmation names | 2511 passed, 9 skipped, exit 0 |
| `bin/seal layout --check`, `bin/seal rules --check` | exit 0, exit 0 |

Each probe file was deleted after its run, and `git status --short` in the
clone printed nothing.
