# Review round 1: 1793582903-each-entry-links-its-pull-request

```seal
target: a8d9015fa against origin/release/v0.28.0
```

This is the first round, so no earlier record exists and no fact is carried.
Every fact below was opened or run at `a8d9015fa`. The runs and mutations
took place in a `git clone --no-local` of the worktree under the round's
scratch directory, which is gone. The worktree itself was only read.

## Findings

### 1. `--apply` keeps for ever a released directory in a user's repository whose release notes the plugin never built

```seal
severity: must
location: `skills/settle/scripts/settle.py:472-478`, `skills/settle/scripts/settle.py:508-558`, `skills/settle/SKILL.md:444-474`, `tests/skills/test_settle.py:1766`
evidence: executed `bin/test tests/skills/test_tmp_round1_probe.py -q -s -p no:xdist`, `git grep -n -i publish_release_note -- skills templates hooks bin agents`
```

Why it matters: the check rests on a premise that holds in this repository
only. In every other repository it keeps directories for ever and tells
the person to edit a published note.

- The premise is `docs/the-record-layout.md:40-48`. The release note is
  built from the fragments at the tag by
  `.github/scripts/publish_release_note.py`, so the published note is the
  one copy of a fragment outside the history. That renderer is this
  repository's CI script. Nothing the plugin ships writes a fragment into
  a user's release note. The `git grep` above over `skills`, `templates`,
  `hooks`, `bin` and `agents` finds two comments in `settle.py` (`:299`,
  `:398`) and no renderer or workflow (executed). Phase 2 departure 4 says the same: "the renderer, which is
  not shipped".
- `seal settle --apply` does ship. Where the root is shared, `notes`
  (`settle.py:508-558`) reads any repository's release whose tag holds a
  fragment added by a commit whose subject ends in `(#N)`. `carries`
  (`settle.py:472-478`) accepts only `https://github.com/<o>/<n>/pull/<N>`
  or `<!-- specs/<id> -->`. Neither form is written by anything a user has.
- So in a user's repository on GitHub with `vX.Y.Z` tags, squash merges and
  published Releases, a note that does not link `/pull/N` reads as "lost
  its entry". The class, listed from what produces it: any note that this
  repository's renderer did not write. That covers a hand-written note, an
  empty body on a binaries-only Release, a note whose generator links
  references as `/issues/N` (the conventional-changelog writers likely do;
  not run here), and a GitHub Enterprise host, whose links are not at
  `github.com`. GitHub's own generated notes link `.../pull/N` and pass.
- The probe built one note over `test_settle.py`'s fixtures holding two of
  these shapes: a link to `https://github.com/o/r/issues/42` and a link to
  `https://ghe.example.com/o/r/pull/42`. `--apply` exited 1 and
  printed `kept seal/threads/1700000001-a/: the published note of v1.2.3
  does not carry its entry, a link to pull request #42; repair the note
  ...` (executed). Every later `--apply` repeats the same result. The only
  ways out are editing a published note the user never meant to carry
  fragments, or `rm -r` by hand.
- `skills/core/SKILL.md` *The rule a mechanism is kept against* says a
  script holds a gate only on a fact it reads exactly. The URL test is
  exact as a string. What it decides, that a note lost an entry, is exact
  only where the renderer wrote the note. The same section says a file
  that is not of the form's kind is named as not read, and nothing is
  decided on it. A user's note is such a file.
- The frame considered user repositories in one row only:
  `frame/plan.md:59`, "a user repository whose notes are GitHub-generated
  links its pull requests". No probe stands behind it. Q1 covers notes
  that cannot be found, and does not cover a note found and never built
  from fragments.
- On the owner's question about `## Removes`: the marker the renderer drops
  was the one line that told a note built from fragments apart from any
  other note. With it gone, only the link line's shape tells them apart,
  and that shape lives in the renderer (`publish_release_note.py:281`),
  which the settle cannot load.

The fix below reads a note only where it holds a line in a form the release
note writes. A note with no such line goes as before, named as no note
read. Precondition: `PULL_LINK` is spelt once. Move it into `settle.py`
beside `VERSION_RE` and have the renderer take it, as phase 2 did for
`TAG_RE`. The cost is stated here so the fix pass can weigh it: a note
built from fragments that lost every entry then reads as not built, and its
directory goes. The narrower option, keeping only where the note carries
some other entry of that release, needs every fragment at the tag and is
not shown. A fix pass that keeps the current behaviour should write the
cost to user repositories into `questions.md` beside Q1 and Q2, because the
frame never weighed it.

```python
# settle.py, beside VERSION_RE. The renderer takes PULL_LINK from here.
PULL_LINK = "[#{number}](https://github.com/{repo}/pull/{number})"
# A line the release note writes above an entry: its link, or before #1139
# its marker. A note holding neither was not built from the fragments.
BUILT_RE = re.compile(
    r"^(?:\[#\d+\]\(https://github\.com/[^/\s]+/[^/\s]+/pull/\d+\)"
    r"|<!-- specs/\S+ -->)$",
    re.M,
)
NOT_BUILT = (
    "no note read: the published note of {tag} holds no line the release "
    "note writes above an entry, so no fragment built it"
)

# in notes(), between the `tag not in published` and the `carries` branches:
        elif not any(BUILT_RE.search(b) for b in published[tag]):
            out[work_item_id] = (False, NOT_BUILT.format(tag=tag))
```

A case in `tests/skills/test_settle.py` beside S4 pins the `NOT_BUILT` line
for a note linking `/issues/42`. It is seen red against `a8d9015fa`, where
the directory is kept with exit 1. The rule changes' `add` to
`docs/the-record-layout.md` and the SKILL's bullets gain the sentence.

```seal
verdict: fixed 316bdc2d1
answer: Built to the frame as folded at bbd15ec5e (design Scope item 4), which departs from the paste-ready fix in one place, written here in my own words: the test is repository-wide, not per tag. `notes` reads a note only where some non-draft release body in the one list holds a whole line `BUILT_RE` reads, and otherwise every pending directory goes with `NOT_BUILT` under `removed`. `PULL_LINK` and `MARKER` now live in `settle.py`, the renderer takes `PULL_LINK` from there, and `BUILT_RE` is derived from both by `_line_of`, anchored to a whole line with the number repeated. `test_apply_removes_where_no_published_note_is_built_from_the_fragments` holds the round's `/issues/42` and other-host shapes, a GitHub-generated line and a conventional-changelog line. Run against the source at bbd15ec5e (the two source files stashed, then restored by `stash pop`), it went red at `assert code == 0` with the round's `kept ... does not carry its entry` line. Each guard alone removed went red under `seal mutate`, each exit 0: `elif not built` (the new case), `built = False` (S4, and S7b where the only built line is another release's), the line anchors (the new case, through the conventional-changelog line), and the marker alternative (S5[marker]). S5's link body lost its `- ` prefix, which made it no built line, and S5 now asserts that no `no note read` line is printed. The text followed in 4c5e6de76: the SKILL's *What `--apply` does*, the module docstring, `--apply` help, `REMOVES_HEADING` and its pin, both README rows, both editions of the `seal/` README, and the changelog fragment.
```

### 2. An empty `changelog.md` keeps its directory for ever, because the release note gives it no entry

```seal
severity: should
location: `skills/settle/scripts/settle.py:524-535`, `.github/scripts/publish_release_note.py:254-256`, `tests/skills/test_settle.py:1723`
evidence: executed `bin/test tests/skills/test_tmp_round1_probe.py -q -s -p no:xdist`
```

Why it matters: the renderer and the settle disagree on which fragment
gets an entry. The settle then keeps a directory and tells the person to
repair a note from a file that holds nothing.

- The renderer skips an empty fragment: `if body:` at
  `publish_release_note.py:255`. A case pins the skip
  (`tests/github/test_publish_release_note.py:284` and `:309`, "an empty
  fragment became an entry"), so the shape is a supported one.
- `notes` checks presence only. `ls-tree` at `settle.py:527` sees the file,
  `adding_commit` returns the number, `version` returns the tag, and
  `carries` finds no link. The probe wrote `changelog.md` as `"\n  \n"`
  under a commit `feat: a (#42)` and tag `v1.2.3`. `--apply` exited 1 with
  `kept ... does not carry its entry, a link to pull request #42; repair
  the note from git show <at>:seal/threads/1700000001-a/changelog.md`, and
  that file is blank (executed).
- Method (contract rule 12): I took apart every branch of
  `publish_release_note.py#fragments` and `#section` that writes no link
  line for a fragment the settle would check.
  - A path the previous tag holds: the settle reads that earlier tag's
    note, so the two agree.
  - An adding commit with no `(#N)`: `NO_NUMBER`, so the two agree.
  - An entry with no number and no text left: same as the one above.
  - An empty body: the two disagree. This is the one instance.

```python
NO_TEXT = (
    "no note read: its `changelog.md` at {ref} holds no text, so the release "
    "note gives it no entry"
)

# in notes(), the loop body; the text is read at `at`, the commit
# --released-at resolves to. Precondition: the renderer reads the text at the
# newest commit of the tag's range, so a fragment emptied or filled after the
# tag reads differently here. That shape is left as a limit.
            held = git_out(root, "ls-tree", "--name-only", at, "--", path).strip()
            text = git_out(root, "show", f"{at}:{path}").strip() if held else ""
            commit, number = adding_commit(root, at, path) if held else (None, None)
            if commit is None:
                out[work_item_id] = (False, NO_FRAGMENT.format(ref=ref))
            elif not text:
                out[work_item_id] = (False, NO_TEXT.format(ref=ref))
            elif number is None:
```

A case beside S7 in `tests/skills/test_settle.py` pins the `NO_TEXT` line
with no `gh` call. It is seen red against `a8d9015fa`.

```seal
verdict: fixed 316bdc2d1
answer: Applied as the paste-ready fix reads, with `NO_TEXT` worded "holds no text, and the release note gives an empty fragment no entry"; the limit it names (text read at `--released-at`, not at the newest commit of the tag's range) is stated in `notes`'s docstring. `test_apply_removes_a_directory_whose_fragment_is_empty` writes `"\n  \n"` under `feat: a (#42)` and `v1.2.3` beside a built note that lacks #42, and asserts the `NO_TEXT` line and no `gh` call. Against the source at bbd15ec5e it went red at `assert code == 0` with the `kept ... does not carry its entry` line; `elif not text:` changed to `elif False:` went red the same way under `seal mutate`, exit 0. The SKILL, the module docstring and the changelog fragment name the empty fragment as a case of no note read (4c5e6de76).
```

## Confirmations

```seal
confirms: none
```
What matched: the claimed reds of the negative cases were re-run, and each
failed at its own guard's line (executed, `seal mutate` in the clone, each
exit 0). The sample was eight of the 25 reds the two phase records claim:
- `carries` without `(?!\d)` failed S4 at `assert code == 1`, with both
  directories removed.
- `version` keyed by name failed S4 at `assert kept.exists()`, after
  `v1.10.0`'s note was read.
- `published_releases` without the `draft` test failed S7b`[a draft]` at
  `assert code == 1`.
- `if not pending:` changed to `if False:` failed S7 at
  `assert gh.calls() == []`.
- `(True, NO_RELEASE...)` changed to `(False, ...)` failed S7b`[another]`
  at `assert code == 1`.
- `adding_commit` without `--root` failed `[log.showRoot]` at `None == 1`.
- `listed[-1]` changed to `listed[0]` failed the renderer's S1 to S3 case
  at the `#42` link assertion, because `#46` was linked.
- `PULL_REQUEST_RE` without `$` failed `refuses_a_number` at
  `(added, 7) == (added, None)`.

A tenth mutation I wrote myself, `elif tag not in published:` changed to
`elif False:`, failed by `KeyError`. That is my variant and not the
phase's claim, so it shows nothing about the cases.

```seal
confirms: none
```
What matched: `--apply` gates on facts it reads exactly, apart from the
meaning finding 1 names.
- `adding_commit` (`settle.py:290-340`) reads `git log` output and
  anchors `(#N)` at the subject's end.
- `published_releases` (`settle.py:440-469`) refuses empty output and any
  page that is not a list of objects, and takes `draft is False` alone.
- `version` keeps only `VERSION_RE` names and compares their parts as
  numbers.
- Every note is read before the first `rmtree`: `noted = notes(...)` at
  `settle.py:1509` stands before the loop.
- `Unasked` and `Unread` become exit 2 in `main`.

Claimed in `phase-2.md` decision 2: no directory goes before a failing
list is read. Code and S6's sort order agree (read and executed).

```seal
confirms: none
```
What matched: the `## Removes` row holds against what reads the marker.
- `git grep -n -e '<!-- specs' -e 'specs/{'` outside `seal/threads` finds
  one reader, `settle.py:478`, and test fixtures (executed).
- That reader reads notes published at `v0.27.3` and earlier.
- The publish job runs the renderer from the pushed tree
  (`.github/workflows/publish-release.yml:63-92`), so `v0.28.0`'s note is
  the first that holds links, as `plan.md` *Operational impact* claims.
- `skills/implement/SKILL.md`, `templates/setup/config.md`,
  `skills/implement/multi-repository.md` and the old-roots `KEEP` entry
  dropped the marker with no remaining writer.

```seal
confirms: none
```
What matched: the earlier decisions the design names hold in the build
(read).
- #1053's `--full-history` and its skip of a fragment the previous tag
  holds are unchanged in `publish_release_note.py#fragments:228-258`.
- #1117: the number is computed once, in CI at the tag.
- #1044: the link leads to the pull request body `seal pr-body` wrote.
- The owner's report on SHAs: the note names no commit. The SHA appears
  only in the terminal's `kept` line, as `git show <at>:<path>`, and
  `section` writes no SHA for an entry with no number.

```seal
confirms: none
```
What matched: the design's `## Rule changes` parse as four operations with
no error and no unread line (executed, `rule_changes.parse` in the clone).
The four narrow modules `tests/skills/test_settle.py`,
`tests/github/test_publish_release_note.py`,
`tests/text/test_settle_reads_before_it_removes.py` and
`tests/behaviour/test_no_document_names_the_old_roots.py` ran 214 passed,
exit 0 (executed).

```seal
confirms: none
```
What matched: each new case was read against its group.
- `Test_adding_commit`'s two cases cover git config and a mid-subject
  `(#N)`. The renderer's S1 to S3 case covers the oldest add and a
  trailing pair of numbers.
- The S4 to S8 cases each pin a branch of `notes` that no other case
  pins.
- `phase-2.md` reports that `seal layout --pairs` names no pair in the
  module. I did not re-run it (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Q2's default, as a user meets it. On GitHub without `gh`, in shared mode with squash merges and `vX.Y.Z` tags, every `--apply` now exits 2 with `RELEASES_UNASKED` and removes nothing, where before it removed. On a host that is not GitHub, a subject a person ends with `(#N)` for an issue makes `--apply` ask `gh`, which cannot list releases there, so it exits 2 on every run. Squash subjects on GitLab and Bitbucket likely do not end in `(#N)` by default, which would reach `NO_NUMBER` and go. Read, not run against a real host | `skills/settle/scripts/settle.py:539-541`, `skills/settle/scripts/settle.py:663-669` | the owner, through `questions.md` Q2 |
| Whether `gh api` resolves `{owner}/{repo}` in a checkout with several remotes and no `gh repo set-default`, or exits non-zero and stops `--apply`. No such checkout was available | `skills/settle/scripts/settle.py:404` | the owner, at the first settle in such a checkout |
| The full suite, the repository-wide lint and the format check at `a8d9015fa` | the branch | the orchestrator, by `seal gate` after the rounds settle |
| Whether the first real `--apply` after `v0.28.0` removes the directories whose notes carry the old marker (`gaps.md` row) | `skills/settle/scripts/settle.py:472-478` | the owner, at the settle after `v0.28.0` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_settle.py tests/github/test_publish_release_note.py tests/text/test_settle_reads_before_it_removes.py tests/behaviour/test_no_document_names_the_old_roots.py -q` | 214 passed, exit 0 |
| `bin/seal mutate skills/settle/scripts/settle.py --replace OLD NEW --tests "bin/test ... -p no:xdist -x -k K"`, eight claimed mutants and one of mine, each run on its own | each claimed mutant red at the line named under Confirmations, exit 0; one refusal (`OLD occurs 3 times`), run again with a wider `OLD` |
| `bin/test tests/skills/test_tmp_round1_probe.py -q -s -p no:xdist`, two cases over `test_settle.py`'s fixtures: an empty `changelog.md`, and a note linking `/issues/42` and a host other than GitHub's | both exit 1 with the `kept ... does not carry its entry` line; 2 passed; the file was deleted after one run |
| `python3 -I -c` loading `skills/settle/scripts/rule_changes.py` and calling `parse` on `frame/design.md` | 4 ops, `errors=[]`, `unread=[]` |
| `git grep -n -i publish_release_note -- skills templates hooks bin agents` | two comment lines in `skills/settle/scripts/settle.py` and nothing else, so no shipped renderer or workflow |
