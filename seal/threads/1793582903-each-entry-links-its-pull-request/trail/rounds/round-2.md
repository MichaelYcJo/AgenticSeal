# Review round 2: 1793582903-each-entry-links-its-pull-request

```seal
target: 1d9a0107d, fixes a8d9015fa..1d9a0107d
```

This is a verifying round over the diff `a8d9015fa..1d9a0107d`: the frame
fold `bbd15ec5e`, the fixes `316bdc2d1` and `4c5e6de76`, the fix pass's
record `1ae1a87ce`, and the second frame fold `1d9a0107d`. All runs took
place in a `git clone --no-local` of the worktree at `1d9a0107d`, under the
round's scratch directory, which is gone. The worktree itself was only read,
and this record is the one file written there.

Facts carried from round 1 and not established again:

- The plugin ships no renderer or release workflow. Round 1's `git grep` over
  `skills`, `templates`, `hooks`, `bin` and `agents` found none, and this
  diff adds no file under those paths apart from the settle's own.
- The renderer skips an empty fragment at
  `.github/scripts/publish_release_note.py:254-256`.
- `seal layout --pairs` names no pair in `tests/skills/test_settle.py`. This
  rests on `phase-2.md`, and round 1 did not run it either.

Every verdict below was reached again on the code at `1d9a0107d`.

## Findings

None. No finding is a `must`, and no `should` is raised. Three things were
weighed and not raised. The grounds for each are under the confirmation
they belong to:

- a user's repository whose notes hold one whole line in the renderer's
  shape;
- a release body with Windows line endings;
- one guard in `_line_of` that no case watches, and a set it fills and never
  reads.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `--apply` now reads a note only in a repository whose
published notes are built from the fragments, and every directory goes
elsewhere, each named.

- The claim: some non-draft release body has to hold a whole line that
  `BUILT_RE` reads. The code: `built` is computed once over every published
  body at `skills/settle/scripts/settle.py:599`, before the per-directory
  branch at `:610`. A repository with no such line gets `NOT_BUILT`
  (`:537`) under each `removed` line (read).
- The fix pass departed from round 1's paste-ready fix, and the departure
  holds. Round 1 proposed a test per tag and named its cost: a note built
  from the fragments that lost every entry would read as not built, so its
  directory would go. The repository-wide test removes that cost wherever
  the repository has any other built note. In this repository, 40 of the
  68 non-draft releases hold a whole marker line, so `built` is true here.
  This was executed: the live release list from `gh api --paginate`, read
  through `published_releases` and `BUILT_RE` in the clone.
- The whole-line test reads a fact exactly. `BUILT_RE` (`settle.py:431`) is
  built by `_line_of` (`:414`) from `PULL_LINK` and `MARKER` (`:410-411`).
  The renderer formats its link line from the same constant
  (`publish_release_note.py:283`), as a line of its own (`:325`, joined by
  newlines). Before #1139 the renderer wrote the marker as the first line
  of an entry. The printed pattern is
  `^\[\#(?P<number>\d+)\]\(https://github\.com/(?P<repo>[^/\s]+/[^/\s]+)/pull/(?P=number)\)$`
  or the marker on a line alone. A leading space or a `- ` prefix fails
  it, and so does a different number in the text and the URL (executed).
  So the script decides only on a line in its own form's one spelling,
  which is what `skills/core/SKILL.md` *The rule a mechanism is kept
  against* allows.
- Weighed, not raised: a user's repository whose notes happen to hold one
  such line. One whole line `[#N](https://github.com/<o>/<n>/pull/N)` in
  any published body makes the repository read as built. From then on,
  every directory whose version's note lacks its link is kept with exit 1,
  and the `kept` line tells the person to repair a note they never meant
  to carry fragments. That is S4's shape, executed this round: the
  `v1.10.0` body in `tests/skills/test_settle.py:1769` holds the whole
  line, and the directory is kept. The way out is to edit the note, or to
  remove the directory by hand. It is not raised for three reasons. The
  line is the plugin's own form in its one spelling, and a script cannot
  tell it from a line the plugin wrote. The generators named in round 1
  put such a link inside a longer line or after a bullet, and the
  conventional-changelog and GitHub-generated shapes are cases in
  `tests/skills/test_settle.py:1920` that read as not built. Release
  Drafter and Changesets likely do the same, but this was not run. And
  `skills/settle/SKILL.md:463` states the rule, so a person who meets the
  `kept` line can find why.
- Weighed, not raised: Windows line endings. The `$` anchor does not match
  before `\r`, so a body saved with `\r\n` holds no built line. A body
  edited in GitHub's web form is likely saved that way, which was not run.
  No body in this repository's live list holds `\r\n` (executed). `built`
  needs only one body, so in this repository a note repaired through the
  web form changes nothing. `carries` searches anywhere in a body, so a
  carried link in such a body still counts.
- The fix pass's mutants were run again, one at a time, with
  `bin/seal mutate` in the clone. Each red result was exit 0:
  - `elif not built:` changed to `elif False:` failed at
    `test_settle.py:1945`, `assert code == 0`, with the `kept ... does not
    carry its entry` line.
  - `built = False` failed S4, S5`[link]`, S5`[marker]`, S7b`[another]`
    and S7b`[a draft]`. The close names S4 and S7b, so S5 is an extra
    case that also catches it.
  - With the anchors dropped, `_line_of` returns the pattern alone. That
    failed at `test_settle.py:1945`, and the conventional-changelog line
    is what made it built.
  - With the marker alternative dropped, S5`[marker]` failed at
    `test_settle.py:1837`, `assert "no note read" not in text`.
- Weighed, not raised: one guard of `_line_of` that no case watches. I
  changed the repeated field's back-reference to the field's own pattern,
  `(?P=number)` to `\d+`, and the mutant SURVIVED, exit 1. No case holds a
  whole line whose two numbers differ. If the guard went, `BUILT_RE` would
  also accept such a line. That line is the plugin's form in every way but
  the number, and no writer is known to produce it, so the release would
  ship no wrong verdict. In the same function, `seen` (`settle.py:418`,
  `:423`) is filled and never read. It changes nothing.
- The close says the fix pass ran its red-first check by stashing two
  source files and running `stash pop`. The worktree's stash list is empty
  now (executed). The two new cases were also seen red independently of
  that check, by the mutants above and under round-1#2.

```seal
confirms: round-1#2
```
What holds: an empty `changelog.md` now goes with `NO_TEXT` (read).

- `settle.py:582` reads the fragment's text at `--released-at`, and
  `:586` turns an empty one into `NO_TEXT` (`:521`). Both run before the
  pull request number or the tag is asked for.
- The test is the renderer's own: `.strip()`, then empty means no entry
  (`publish_release_note.py:254-256`).
- The text is read at a different commit from the renderer's. The
  renderer reads the newest commit of the tag's range; the settle reads
  `--released-at`. `notes`'s docstring names this as a limit, as round 1
  asked.
- `elif not text:` changed to `elif False:` failed
  `test_apply_removes_a_directory_whose_fragment_is_empty` at
  `test_settle.py:1966`, `assert code == 0`, with the `kept ... does not
  carry its entry` line (executed, `bin/seal mutate`, exit 0). The case
  also asserts that `gh` is never called.
- Claimed in the close: "Applied as the paste-ready fix reads". The code
  matches round 1's snippet, apart from the wording of `NO_TEXT`.

```seal
confirms: none
```
What matched: the text that states the note rule agrees with the code
(read).

- The method was `git grep` outside `seal/threads` and `tests` for "carry
  its entry", "carries its entry", "lacks its entry" and "published note".
  It searches for wordings, so the list is a sample.
- Each hit reads true under the new rule:
  - the usage blocks at `settle.py:11` and `skills/settle/SKILL.md:44`,
    which say "where one is read";
  - exit code 1 at `settle.py:132`, which `--apply` still returns only
    where a note is read and lacks the entry;
  - `RELEASES_UNASKED` at `settle.py:726`, since `gh` is still asked in
    order to tell whether the notes are built;
  - `REMOVES_HEADING` and its pin;
  - both README rows, both editions of the `seal/` README, and the
    changelog fragment.
- The `docs/` sections are not edited yet. The design's `add` and
  `change` carry the new text, and the settle writes it there later.

```seal
confirms: none
```
What matched: the folded frame parses, and the checks that read the
changed paths pass (executed).

- `rule_changes.parse` on `frame/design.md` returned 4 operations, 0
  errors and 0 unread lines. `bin/seal rules --check` exited 0.
- `tests/skills/test_settle.py`, `tests/github/test_publish_release_note.py`,
  `tests/text/test_settle_reads_before_it_removes.py` and
  `tests/behaviour/test_no_document_names_the_old_roots.py` ran 216 passed,
  exit 0.
- Every test module that names `seal-README`, `README.ko`,
  `settle/SKILL`, `seal/README` or `publish_release_note` ran 1331 passed,
  exit 0. That run takes in the line-wrap, editions and opt-in modules,
  which read the two `seal/` READMEs the fix lengthened.

```seal
confirms: none
```
What matched: each new case was read against its group (read).

- `test_apply_removes_where_no_published_note_is_built_from_the_fragments`
  (`test_settle.py:1920`) is the only case that reaches `NOT_BUILT`. Its
  four bodies are a pull request linked as an issue, a link on another
  host, GitHub's generated line, and a conventional-changelog line. Each
  is a shape from round 1's class.
- `test_apply_removes_a_directory_whose_fragment_is_empty`
  (`test_settle.py:1955`) is the only case that reaches `NO_TEXT`.
- S5's link body lost its `- ` prefix. Under the new rule, a body with
  that prefix is not built, and S5 would then pass through `NOT_BUILT`.
  The added assertion `"no note read" not in text` (`:1837`) keeps S5 on
  the branch that reads the note.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `1d9a0107d`. This round leaves nothing open, so the orchestrator's broad run comes due, and the sealer's spawn after it | the branch | the orchestrator, by `seal gate` |
| Round 1's rows on Q2's default as a user meets it, on `gh` in a checkout with several remotes, and on the first `--apply` after `v0.28.0`. They stand as round 1 wrote them, and this diff does not touch them | `trail/rounds/round-1.md` *Not judged* | as round 1 names |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_settle.py tests/github/test_publish_release_note.py tests/text/test_settle_reads_before_it_removes.py tests/behaviour/test_no_document_names_the_old_roots.py -q` | 216 passed, exit 0 |
| `bin/test $(git grep -l -e seal-README -e README.ko -e settle/SKILL -e seal/README -e publish_release_note -- tests \| sort -u) -q` | 1331 passed, exit 0 |
| `bin/seal mutate skills/settle/scripts/settle.py --replace OLD NEW --tests "bin/test tests/skills/test_settle.py -q -p no:xdist -x -k 'note or fragment or release'"`, six mutants each run alone (`built = False` without `-x`) | five red, each exit 0, at the lines given under the confirmations. The `(?P=number)` mutant SURVIVED, exit 1. Two of my own spellings went wrong first and measured nothing: one refused because a shell-escaped `$` matched nothing, and one left a syntax error. Both were rewritten and run again |
| `gh api --paginate 'repos/{owner}/{repo}/releases?per_page=100'`, read through `published_releases` and `BUILT_RE` in the clone | 68 non-draft tags, 40 holding a built line, none holding `\r\n` |
| `python3 -I -c` calling `rule_changes.parse` on `frame/design.md` with policy root `docs` | 4 operations, 0 errors, 0 unread |
| `bin/seal rules --check` | exit 0 |
| `git stash list` in the worktree | empty |
