# Review round 1: 1793188384-the-release-notes-are-kept-twice

target: 9f193554 against origin/release/v0.24.0

This is round 1, so no earlier round's coordinates were carried. Every fact
below was established in this round, in a `git clone --no-local` of the
branch at `9f193554`, held in the round's scratch directory. The repository
declares no `seal/parity.md`, so this round has no `original:` line.

## Findings

### 1. A fragment a settle removed before a release tagged on a merge never reaches the note

severity: must
location: `.github/scripts/publish_release_note.py:186-216`, `tests/github/test_publish_release_note.py:249-302`
evidence: executed `TMP_BOTH_ROOTS=1 bin/test test_tmp_fragments_against_released_files.py -q -s -p no:xdist`, `git log --format=%h v0.22.3..v0.22.4 -- seal/specs/1792926874-the-records-carry-no-comment-and-the-readers-drop-it/changelog.md`, `git log --full-history --format=%h v0.22.3..v0.22.4 -- seal/specs/1792926874-the-records-carry-no-comment-and-the-readers-drop-it/changelog.md`, `bin/test tests/github/test_tmp_merge_tagged_settle.py -q -s -p no:xdist`
verdict: open

`frame/design.md` *Scope* item 1 says each fragment is read "at the newest
commit of the range whose tree holds the path, so a fragment a settle removed
before the tag is still read". It names 0.22.4 as the shape this has to
survive. The work item's `changelog.md` makes the same promise to users. The
built reader does not keep it for a release tagged the way this repository
tags one.

The cause is `fragments` at `publish_release_note.py:210`. It finds the
commits that touched a path with `git log --format=%H <range> -- <path>`. A
path-limited `git log` simplifies history by default: at a merge that is
TREESAME to one parent for that path, it follows only that parent. A release
is tagged on the merge of `release/vX.Y.Z` into `main`
(`docs/branch-and-release.md`). Where the settle removed a fragment on the
release branch, neither the merge nor its first parent holds the path. So the
merge is TREESAME to the first parent, the release branch is never walked,
and the loop finds no commit for that fragment.

Measured on the real history. In the clone, with the fragment pattern widened
to also read `seal/specs/` (the root before #1092), the built reader matched
every released file's markers for 0.14.0 to 0.23.1 except 0.22.4. For
0.22.4 it gave 0 fragments against 9 markers. The same reader with
`--full-history` on the path-limited log gave all 9. The two `git log`
commands on one 0.22.4 fragment show why. The default form prints nothing.
`--full-history` prints `de11df75`, the settle, then `97bf7a9a`, the last
commit holding the fragment. A probe built the release's shape in a fresh
repository: `release` branched off `v1.2.2`, a fragment added, a settle
removing it, then `main` merging `release` with `--no-ff` and the tag on the
merge. The built `fragments` returned `[]`; the fixed one returned the entry.

This is a must for two reasons. When every fragment of a release was settled
before its tag, the job exits 1 at the tag, after `main` has moved. When only
some were, the note goes out without them and nothing says so. S1 does not
catch it, because its history is linear and its tag is the settle commit
itself. The 18 mutants phase 1 reports were all red, and that shows S1 tests
what it covers. It does not show the reader is safe.

The frame's own measurement cannot have been of this reader. The fragment
pattern at `:114` reads `seal/threads/` alone, and before #1092 the fragments
lived under `seal/specs/`. So for 0.19.0 to 0.22.4 the built reader returns
nothing at all; with both roots it still misses 0.22.4. Releases from 0.24.0
on read `seal/threads/` only, so the root is no defect going forward. It only
means the frame's "Executed ... equals" claim does not cover the code that
was built.

`--full-history` alone brings one shape back, so the fix carries a guard for
it. In 0.15.3, commit `b38adc46` restored two directories that an earlier
release had shipped and that `c52e8350` had removed in the same range. Read
with `--full-history` and no guard, the reader put both restored fragments
into 0.15.3's note. A fragment the previous tag already holds was released
there, so the fix skips it. With both changes, the reader matched all 26
releases from 0.14.0 to 0.23.1 (both roots read, executed).

The fix, in `fragments`. It keeps the signature, so the cases' stub of
`fragments` and #1117's seam stay as they are:

```python
    out = []
    # The range's lower end, where there is one: a fragment that tag already
    # holds was released there, and a commit that restores its directory
    # adds nothing new (0.15.3).
    previous = revisions.split("..")[0] if ".." in revisions else None
    # exempt from splitlines: git output
    for path in sorted(set(added.splitlines())):
        found = FRAGMENT_RE.match(path)
        if not found:
            continue
        if previous and git("ls-tree", "--name-only", previous, "--", path).strip():
            continue
        # `--full-history`: the tag is a merge into `main`, whose first parent
        # never held the path. Where a settle removed the fragment on the
        # release branch, the default simplification follows that first
        # parent alone and finds no commit (0.22.4).
        for commit in git(
            "log", "--full-history", "--format=%H", revisions, "--", path
        ).split():
            if git("ls-tree", "--name-only", commit, "--", path).strip():
                body = git("show", f"{commit}:{path}").strip()
                if body:
                    out.append((found.group(1), body))
                break
    return out
```

The case that pins the fix goes in `tests/github/test_publish_release_note.py`,
`Test_main` or `Test_module`. It is the probe's history. Against the build it
gives `[]`, and with the fix it gives the one entry (executed):

```python
    def test_a_fragment_the_settle_removed_reaches_a_note_tagged_on_a_merge(
        self, tmp_path, monkeypatch
    ):
        """The release's shape: the tag is the `--no-ff` merge of the release
        branch into `main`, whose first parent never held the fragment, and the
        settle removed it on the release branch (0.22.4). A fragment of the
        release before, restored by a commit in the range, is not read again
        (0.15.3)."""
        repo = git_repo(tmp_path / "repo")
        thread = "seal/threads/{}/changelog.md"
        write(repo, thread.format("1700000000-older"), "- older entry\n")
        commit_everything(repo, "the release before")
        git_out(repo, "tag", PREVIOUS)
        git_out(repo, "switch", "-q", "-c", "release")
        write(repo, thread.format("1700000001-first"), "- first entry\n")
        commit_everything(repo, "the work item")
        git_out(repo, "rm", "-q", "-r", "seal/threads/1700000001-first")
        git_out(repo, "rm", "-q", "-r", "seal/threads/1700000000-older")
        commit_everything(repo, "the settle")
        write(repo, thread.format("1700000000-older"), "- older entry\n")
        commit_everything(repo, "a directory restored")
        git_out(repo, "switch", "-q", "-")
        git_out(repo, "merge", "-q", "--no-ff", "-m", "the release", "release")
        git_out(repo, "tag", TAG)
        mod = publisher()
        monkeypatch.setattr(mod, "ROOT", str(repo))
        revisions = mod.commit_range(mod.previous_tag(TAG), TAG)
        assert mod.fragments(revisions) == [("1700000001-first", "- first entry")]
```

The docstring of `fragments` at `:187-195` gains one sentence for each of the
two arms. `frame/design.md` *Data & interfaces* names the per-path
`git log`, so the fix pass adds `--full-history` and the guard there too.

answer:

### 2. Step 3 of the update skill prints every release body ever published into the session, about 880 KB today

severity: should
location: `skills/update/SKILL.md:72-90`, `tests/behaviour/test_release_hygiene.py:1080-1101`
evidence: executed `curl -fsS "https://api.github.com/repos/$repo/releases?per_page=100" -o /dev/null -w '%{size_download} bytes, http %{http_code}\n'`
verdict: open

Step 3 tells the session updating the plugin to run
`curl -fsS ".../releases?per_page=100"`, then read the `body` of each release
in the span. The command prints the whole list: up to 100 releases, each
with its full note. Run against this repository's `origin` on 2026-10-28, it
returned 881,917 bytes with HTTP 200. Phase 5 appends 26 more released files
to 26 of those notes, so the list grows further. A session running
`/agentic:update` from 0.23.1 to the next release then pays for close to a
megabyte of output to read one release. A harness that puts large output in
a file leaves the session to page through it. The old step read only the
files in the span, so this is a cost the change brings in.

Phase 2's record says the command ran and returned 58 releases. That is
true, and it shows that the read works, not that the step can be followed
cheaply. Nothing in the frame asks for the whole list to be printed. *Scope*
item 6 asks for the releases "after the old version up to the new one,
oldest first".

The fix keeps the S8 case's words and selects the span before printing it.
Measured with the filter below for 0.22.4 to 0.23.1: 16,760 bytes in place
of 881,917, with every pipe status 0. The download goes to a file, so the
step can still read curl's exit code on its own:

```bash
repo=$(git -C ~/.claude/plugins/marketplaces/agenticseal remote get-url origin | sed -E 's#^.*github\.com[:/]##; s#\.git$##')
f=$(mktemp)
curl -fsS "https://api.github.com/repos/$repo/releases?per_page=100" -o "$f"; echo "curl exit $?"
python3 -c '
import json, sys

def key(name):
    try:
        return tuple(int(n) for n in name.lstrip("v").split("."))
    except ValueError:
        return None

old, new = key(sys.argv[2]), key(sys.argv[3])
with open(sys.argv[1], encoding="utf-8") as handle:
    releases = json.load(handle)
for release in reversed(releases):
    at = key(release["tag_name"])
    if at and old < at <= new:
        print("## " + release["tag_name"])
        print(release["body"])
' "$f" <old version> <new version>
rm -f "$f"
```

The sentence after the block becomes: "It prints the `body` of every release
after the old version up to the new one, oldest first, each under its tag.
Summarize every entry in them." The S8 case at
`tests/behaviour/test_release_hygiene.py:1080-1101` gains `"reversed("` and
`"old < at <= new"` among the words it needs. Its refusal of `"gh "` reads
the flattened step, so the step's prose must still hold no word that ends in
"gh" before a space.

answer:

### 3. The frame still reads the 0.12.2 file at its own tag, and `v0.12.2` holds no such file

severity: should
location: `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:97-100`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/questions.md:13-16`
evidence: executed `git cat-file -e v0.12.2:changelog/0.12.2.md`, `git cat-file -e v0.23.1:changelog/0.12.2.md`
verdict: open

The orchestrator folded phase 4's divergence into the frame at `8b286eb7`
and `9f193554`, rewriting *Scope* item 5, S11 and the plan's phase 5 row.
Two sentences that state the old fact were left. *Scope* item 8 says the
v0.12.2 GitHub Release's folded text "after the republish is
`changelog/0.12.2.md` at `v0.12.2`". `questions.md` says "the files stay
readable at their own tags". `git cat-file -e v0.12.2:changelog/0.12.2.md`
exits 128 with "path 'changelog/0.12.2.md' does not exist in 'v0.12.2'". The
same file at `v0.23.1` exits 0. The two `seal/follow-up.md` rows, as built,
say `v0.23.1`. So the frame now disagrees with the build it governs. Phase 5
is run from this frame, and the sealer reads it against the tree, so an
agent acting on either sentence reads the wrong coordinate.

```text
design.md:97-100, in place:
   the two `seal/follow-up.md` rows that name `changelog/0.12.2.md`. Those
   two rows keep their question and their answerer, and their coordinate
   becomes the v0.12.2 GitHub Release, whose folded text after the
   republish is `changelog/0.12.2.md` at `v0.23.1`.

questions.md:13-16, in place:
  reader of one release reads one file; the GitHub Release page is one
  release, and the files stay readable at `v0.23.1`, the last tag that
  holds them all (read: #728's body; executed: `git cat-file -e` finds a
  tag's own file only from `v0.18.1`). #557 fixed `survivor_check.py`'s
```

answer:

### 4. Three sentences still state the gather or its files, and neither the build nor `## Rule changes` reaches them

severity: should
location: `docs/the-record-layout.md:36-37`, `docs/release-checklist.md:146`, `skills/verify/scripts/unverified_check.py:257`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:189-463`
evidence: executed `git grep -n -i -E 'changelog/|CHANGELOG\.md|gather|changelog marker|release file|released file' -- docs`, `git grep -n -i -E 'changelog marker|marker the changelog|gathered entr|ungathered|live_markers'`
verdict: open

*Grounding* row 3 of the frame asks that every sentence naming the gathered
files or the gather be removed or re-pointed. Outside `docs/` the build does
that in place. Inside `docs/`, `## Rule changes` does it at the settle. A
search of `docs/` for the gather's words, held against the 35 operations,
found two sentences that no operation names. A search of the tree for the
changelog marker's reader found a third, outside `docs/`. Each will still
stand after the settle:

- `docs/the-record-layout.md:36-37`, *A change writes fragments, never a
  shared file*: a change writes its entry "never under a heading of
  `CHANGELOG.md`". The operations in that section remove the sentence after
  it and rewrite the paragraph below, and leave this one naming a file that
  no longer exists.
- `docs/release-checklist.md:146`, *3. Verify before committing*: the
  shipped set is read from the tags "never from this file, because this
  commit writes the heading and the bump together". The preparation commit
  writes no heading after this work, and phase 4 moved the case this row
  describes from `shipped_versions` to `shipped_tags`.
- `skills/verify/scripts/unverified_check.py:257`: "A reader of a line that
  HOLDS something — a changelog marker, an open row — reads it". The frame's
  *Grounding* row on `live_lines` says that `gather_changelog.py#live_markers`
  was the only reader of the marker. Phase 3 rewrote the same example at
  `:532` and `:579` and left this one.

The `from:` texts below were each found once in their documents (executed).
Two operations go in `frame/design.md` `## Rule changes`, and one edit goes
in the script:

```text
- change
  file: docs/the-record-layout.md
  section: A change writes fragments, never a shared file
  from: never under a heading of `CHANGELOG.md`.
  to: never under a heading of a file every branch shares.
- change
  file: docs/release-checklist.md
  section: 3. Verify before committing
  from: never from this file, because this commit writes the heading and
    the bump together
  to: never from a file this commit writes
```

```python
    **An unclosed block is reported, not decided.** `blank_fences` blanks it
    to the end, because a gate reading a record treats it as quoted. A reader of a
    line that HOLDS something — an open row — reads it,
```

answer:

## Confirmations

confirms: none
The seam the frame promised #1117 holds, except for finding 1, which #1117's
merge-tagged flow would also meet. Read at `9f193554`. `main` at
`.github/scripts/publish_release_note.py:623-679` reads `TAG`, `REPO` and
`DRY_RUN` from the environment, `gh` takes `GH_TOKEN`, and `write_output`
writes `created=true` or `created=false` to `GITHUB_OUTPUT` at `:656`, `:674`
and `:678`. `fragments` at `:186` is the one function that picks the
fragments, and `section` at `:219` is the one that renders them. Nothing on
the path reads a preparation commit. The range comes from the tags, and
`PREPARATION_RE` only leaves the preparation pull request out of the
summary.

confirms: none
Every `from:` text of the frame's 35 `## Rule changes` operations is found in
the section it names. Executed: a probe parsed the section with
`skills/settle/scripts/rule_changes.py#parse` and searched each section that
`section_lines` gives with `rule_changes.pattern`. It printed no parse
error, 35 operations and 0 missing.

confirms: none
No reader of `changelog/` or `CHANGELOG.md` is left outside `docs/` and
`seal/threads/` that sends a reader there for the notes. Executed: `git grep
-n -E` for both paths outside those two roots. The hits are the eight lines
phase 4's S12 table lists, the two emptied modules' docstrings, and the two
`seal/follow-up.md` rows, which name the file at `v0.23.1` as the folded text
of the v0.12.2 note. A broader search for the gather's words outside `docs/`
found `skills/implement/orchestration.md:541` and `:578`, which `gaps.md`
hands to #1041, and the line in finding 4.

confirms: none
The crafter claimed that `## Removes` missed readers of the gather, and that
it rewrote them: `CONTRIBUTING.md`, `skills/verify/orchestration.md:91-94`,
four step-count cases, the `hygiene.yml` comment, three docstrings in
`test_release_hygiene.py`, the record-prefix loop and the `note` call in
`test_release_seal.py`. Each stands in the diff `8a1173c8..9f193554` as
described (read). The count case at
`tests/behaviour/test_the_gate_names_every_step_ci_runs.py:113-147` builds
the sentence from `PARTITION`'s counts and leaves a kind with no step out, so
it still fails when a step is added to either kind (read). The record-prefix
loop iterated over nothing once `"changelog/"` was gone, so removing it
weakens no case (read).

confirms: none
The crafter claimed that `tests/behaviour/test_first_setup_asks_once.py`
still passes `fold_ledger`, a script #950 removed. Executed: `git ls-files`
holds no path naming `fold_ledger`. The parameter reads nothing, the branch
did not cause it, and `gaps.md` *Not done* records it.

confirms: none
The crafter claimed that `skills/implement/orchestration.md:530`, `:538`,
`:541` and `:578` still describe the gather. Read: `:530` says the entries
"are gathered and dated", `:538` and `:541` speak of "one fragment per work
item that a release gathers" and of "running the gather", and `:578` names
"the marker the changelog gather writes". Under `frame/questions.md` Q4's
default (a) the file is #1041's, and the build left it alone.

confirms: none
The divergence `gaps.md` records on where a released file is read holds.
Executed: `git cat-file -e` finds `changelog/0.12.2.md` at `v0.23.1` and not
at `v0.12.2`. This work item's `changelog.md` and the two follow-up rows name
`v0.23.1`.

confirms: none
The narrow verification for this round passed. Executed in the clone: 96
test modules ran with `bin/test -q`, 4339 passed, 11 skipped, exit 0. They
are every module under `tests/` that `git grep -l` finds naming a path this
branch changed or removed, or a script's name, with
`tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` and
`tests/test_censuses.py` among them. `bin/seal layout --check` exited 0, and `bin/seal rules --check`
exited 0 with all 266 check lines holding. This is not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| S11: every released version's note holds its file after the republish of the 26 | `frame/plan.md` phase 5 row | the orchestrator, in phase 5 |
| Whether the tag's job can list the milestones under `contents: write` alone (Q3, default (a)) | `.github/workflows/publish-release.yml` | the orchestrator, reading the log of the tag run of the release carrying this work |
| The full suite, the repository-wide lint and the typecheck: unverified | the branch at its last fix | the orchestrator, at `seal gate`, before the sealer is spawned |
| The mutation runs the phase records report (18, 5, 2 and 2 mutants), not re-run here | `trail/phases/phase-1.md` to `phase-4.md` | the sealer, re-running a sample of the crafter's claims |
| Whether the pull request body hands `skills/implement/orchestration.md:530`, `:538`, `:541` and `:578` to #1041 | the pull request body | the orchestrator, when it writes the body |
| Step 3 of the update skill run by a session updating across a real release | `skills/update/SKILL.md` | the first person to update to the release carrying this work |

## Probes

| Command | Result |
|---|---|
| `bin/test test_tmp_fragments_against_released_files.py -q -s -p no:xdist`, comparing `fragments` with each released file's markers from 0.14.0 to 0.23.1 at `v0.23.1` | as built: 0 fragments for every release before 0.23.0, because the fragments then lived under `seal/specs/`; 0.23.0 and 0.23.1 matched |
| the same with `TMP_BOTH_ROOTS=1`, the pattern widened to `seal/specs/` | every release matched except 0.22.4: 0 fragments against 9 markers |
| the same with `TMP_FULL_HISTORY=1` added | 0.22.4 matched 9 of 9; 0.15.3 gave 2 extra, the directories `b38adc46` restored |
| the same with `TMP_FIXED=1`, the fix in finding 1 | all 26 releases matched; mismatched list empty |
| `git log --format=%h v0.22.3..v0.22.4 --` one 0.22.4 fragment, then with `--full-history` | default: no commit; with `--full-history`: `de11df75` then `97bf7a9a` |
| `bin/test tests/github/test_tmp_merge_tagged_settle.py -q -s -p no:xdist`, the case in finding 1 | as built `[]`; fixed `[('1700000001-first', '- first entry')]` |
| `bin/test test_tmp_rule_change_froms.py -q -s -p no:xdist` | no parse error, 35 operations, 0 `from:` texts missing |
| curl of the releases list from the `origin` repository, writing to /dev/null with the size printed | 881917 bytes, HTTP 200, exit 0 |
| the span filter of finding 2 over that list for 0.22.4 to 0.23.1 | 16760 bytes; pipe statuses 0 0 0 |
| `git cat-file -e` for `changelog/0.12.2.md` at `v0.12.2` and at `v0.23.1` | exit 128, then exit 0 |
| `bin/test -q` over the 96 modules the last confirmation names | 4339 passed, 11 skipped, exit 0 |
| `bin/seal layout --check`, `bin/seal rules --check` | exit 0, exit 0 |

Each probe file was deleted after its run, and `git status --short` in the
clone printed nothing.
