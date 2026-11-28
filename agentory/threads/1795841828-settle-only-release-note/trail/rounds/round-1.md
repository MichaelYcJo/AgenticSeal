# Review round 1: 1795841828-settle-only-release-note

```iadd
target: 07f6f49a against origin/release/v0.41.0
```

Round 1 is a finding round over the whole range `origin/release/v0.41.0..07f6f49a`, read in a `git clone --no-local` of the branch worktree checked out at `07f6f49a`. No earlier round exists, so no fact is carried; every coordinate below was opened this round. No `agentory/parity.json` is declared, so no parity comparison is owed. The records read whole at the target are `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md`. The record language is English, so no `pr.<lang>.md` stands.

## Findings

### 1. Four statements of what the note carries when the pull requests cannot be listed still say "the fragments alone", and the closing memo names only one of them

```iadd
severity: should
location: `.github/scripts/publish_release_note.py:52-54`, `.github/scripts/publish_release_note.py:95-98`, `.github/scripts/publish_release_note.py:607-610`, `.github/scripts/publish_release_note.py:635-646`, `tests/github/test_publish_release_note.py:1070`, `docs/releasing/release-checklist.md:291-293`, `agentory/threads/1795841828-settle-only-release-note/frame/design.md:60-110`, `agentory/threads/1795841828-settle-only-release-note/gaps.md:12`
evidence: executed `git grep -n -F "fragments alone" -- .github docs skills tests` and `git grep -n -F "or a fragment" -- .github docs skills tests` at 07f6f49a; read `.github/scripts/publish_release_note.py:1026-1049`, `.github/scripts/publish_release_note.py:906-911`
```

Why it matters: the settle-only path makes the note's folded text the release pull request's body (`.github/scripts/publish_release_note.py:1028-1038`, then `release_body(theme, rendered, ...)` at line 1049). Where `merged_pulls` then fails, `release_body` returns the theme line and `rendered` unfolded (its docstring, lines 906-911, already says `rendered`). The note is then the theme line and the release pull request's body. Four texts still say it is the fragments:

- the module docstring, lines 95-98: "A `gh` call that cannot list the pull requests publishes the theme line and the fragments alone";
- the `merged_pulls` docstring, lines 607-610: "the caller publishes the theme line and the fragments alone";
- the two lines `merged_pulls` prints, lines 635-638 and 643-646, which the job log shows;
- `docs/releasing/release-checklist.md:291-293`, which tells the person reading that log that "the note went out as the theme line and the fragments alone". Rule change 2 of `frame/design.md` rewrites the sentence before it in the same paragraph and leaves this one.

The module docstring at lines 52-54 states the same fact the other way round: "every line is a milestone's sentence, a pull request title, a number, a handle or a fragment". A settle-only note's folded lines are the release pull request's body, and that body is none of those.

The two `git grep` commands printed these places, and also `tests/github/test_publish_release_note.py:22`. That A5 line describes a release with fragments (#572), so it stays as it is. A search on the fact's words is a sample under contract rules 12 and 19, because a statement in other words escapes it.

The case is narrow: `release_pull_body`'s `gh pr list` has to answer and `merged_pulls`' call after it has to fail. It is still a tool telling a person something wrong, in the log line and in the checklist that explains it. `gaps.md:12` names only the printed line and leaves it. Its grounds are that the frame's *Scope* item 5 does not list it. *Scope* item 5 lists the texts that state the old rule, and these texts state the old fact. `skills/core/SKILL.md` *The rule a mechanism is kept against* says a change removes, in the same commit, what stood on the old fact. The closing memo's list is a sample of the class: it reached the printed line and missed the three docstring statements and the checklist sentence, which the commands above list. Its own reason for leaving the line ("only where the second call fails after the first succeeded") names exactly the case these texts get wrong.

The fix rewrites the four code statements in place, adjusts the one case that pins the printed words, adds a rule change for the checklist sentence, and removes the first *Not done* paragraph of `gaps.md`, since nothing is then left undone. The second case that pins the line, at `tests/github/test_publish_release_note.py:1107`, asserts the prefix "gh pr list failed, so the note is the theme line and the ", which the new words keep. Its other assertion, "alone: `gh pr list --repo", is kept too.

```python
# .github/scripts/publish_release_note.py, lines 52-54
update -- and keeps the fragments beneath, folded. Nothing here composes
prose: every line is a milestone's sentence, a pull request title, a
number, a handle, a fragment, or a line of the release pull request's
body for a range of settles alone.

# lines 95-98
**The summary adds no way to fail.** A `gh` call that cannot list the pull
requests publishes the theme line and the fragments alone, or for a range
of settles alone the theme line and the release pull request's body, and
says so in the job log -- a plain note is fixable in one edit, and a failed
job at the tag is not.

# lines 607-610, in the `merged_pulls` docstring
    the caller publishes the theme line and the fragments or the release
    pull request's body alone rather than failing the tag's job. A `gh`
    that gave no answer is read the same way, and the line names it in the
    runner's words.

# lines 635-638
        print(
            "gh pr list failed, so the note is the theme line and the fragments "
            f"or the release pull request's body alone: {said}"
        )

# lines 643-646
        print(
            "gh pr list printed something that is not JSON, so the note is the "
            "theme line and the fragments or the release pull request's body alone"
        )
```

```python
# tests/github/test_publish_release_note.py, line 1070
        assert (
            "the note is the theme line and the fragments or the release pull "
            "request's body alone" in out
        ), out
```

```markdown
<!-- frame/design.md, ## Rule changes: a fifth entry -->
- change
  file: docs/releasing/release-checklist.md
  section: After the merge
  from: Where the job log says the pull requests could not be listed, the note went out as the theme line and the fragments alone, which one `gh release edit` repairs.
  to: Where the job log says the pull requests could not be listed, the
    note went out as the theme line and the fragments alone, or for a
    range of settles alone as the theme line and the release pull
    request's body, which one `gh release edit` repairs.
```

```iadd
verdict: fixed 137b9523
answer: The finding holds. 137b9523 rewrites in place, in `.github/scripts/publish_release_note.py`, the module docstring's paragraphs *The fragments are also a page of reasoning per change* (now "keeps the fragments beneath, folded, or for a range of settles alone the release pull request's body" and "every line is ... a fragment, or a line of the release pull request's body") and **The summary adds no way to fail**, the `merged_pulls` docstring, and its two printed lines, in the paste-ready fix's words for the two lines. `tests/github/test_publish_release_note.py#test_the_list_is_read_from_the_release_branch` pins the failed line's new words, and now also pins the not-JSON line whole, which no case held before; its docstring names the release pull request's body too. Each assertion was seen red against the old line it pins: with the test edited and the code not, `-k "read_from_the_release_branch or gave_no_answer_is_read"` printed `1 failed, 1 passed` on `assert "the note is the theme line and the fragments or the release pull request's body alone" in 'gh pr list failed, so the note is the theme line and the fragments alone: HTTP 502\n'`; with the failed line fixed and the not-JSON line not, the same command failed on `assert 'gh pr list p...ments alone\n' == "gh pr list p... body alone\n"`. `gaps.md`'s first *Not done* paragraph is removed. The checklist sentence is rule change 5's (a150b892) and is not touched here. After the fix, `git grep -n -F "fragments alone" -- .github docs skills tests` prints `.github/scripts/publish_release_note.py:97` and `:611`, the rewritten sentences, which name the release pull request's body beside the fragments; `docs/releasing/release-checklist.md:293`, which rule change 5 rewrites at the settle; and `tests/github/test_publish_release_note.py:22`, the A5 line of a release with fragments (#572), which stands as the finding says. `git grep -n -F "or a fragment" -- .github docs skills tests` prints nothing. The changelog fragment states nothing of the log line, so it does not change.
```

### 2. The settle skill's new sentence names the plugin's release workflow as "this repository's", which an installed copy reads as the user's repository

```iadd
severity: should
location: `skills/settle/SKILL.md:470-473`
evidence: read `skills/settle/SKILL.md:368-372`, `skills/settle/SKILL.md:470-473`, `.gitattributes:30`; executed `git grep -n "this repository's" -- 'skills/*/SKILL.md'` at 07f6f49a
```

Why it matters: `skills/settle/SKILL.md` ships in `dist` (the plan's *Operational impact*) and is read by a settling session in a user's repository. In that session "this repository" is the user's repository. `.github/` is `export-ignore` (`.gitattributes:30`), so that repository holds no `.github/scripts/publish_release_note.py`. The sentence at lines 470-473 then claims that the user's release workflow builds a settle-only note from the release pull request's body. The same skill already words this fact for an installed copy at lines 368-372: "The release workflow that builds a note from the fragments is the plugin's own (`.github/scripts/publish_release_note.py`), and the plugin ships no copy". So the new sentence contradicts that wording in the same file. `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* asks for one reading of a text an agent reads. Here "this repository's" has one reading in the plugin's clone and another in every installed copy. The `git grep` prints one other SKILL.md hit, `skills/parity-setup/SKILL.md:56`, a different fact (an origin remote URL). The search is a sample. `frame/design.md` *Scope* item 6 uses the same words, but in a record that stays in this repository they have one reading. Item 6 prescribes the content, not the wording, so the fix changes only the skill.

```markdown
So a settle writes no changelog fragment. In the plugin's own repository,
where a release carries settles alone, its release workflow,
`.github/scripts/publish_release_note.py`, builds the note from the body of
the release pull request where any other note carries the fragments.
```

```iadd
verdict: fixed 22bc1b71
answer: The finding holds. 22bc1b71 applies the paste-ready fix as written at `skills/settle/SKILL.md:470-473`, which now reads the same for an installed copy as lines 368-372 do. `frame/design.md` *Scope* item 6 keeps "this repository's", a record of this repository, as the finding says. After the fix, `git grep -n "this repository's" -- 'skills/*/SKILL.md'` prints only `skills/parity-setup/SKILL.md:56`, an origin remote URL, a different fact. The narrow set after both fix commits, executed: `uv run --no-project tests/run_tests.py -q tests/github/test_publish_release_note.py tests/github/test_release_mark.py tests/skills/test_settle.py tests/lib/test_console.py tests/text tests/behaviour` printed `1236 passed, 10 skipped`; `uvx ruff check` and `uvx ruff format` on the two changed Python files printed `All checks passed!` and `2 files left unchanged`. The read of the range, at HEAD `22bc1b71`: `bin/agentic range agentory/threads/1795841828-settle-only-release-note --from 07f6f49a --out <scratch>/fix-1/range.txt` printed `agentic range: 07f6f49a9381330b298b37da0a8ff25959bd49ac..22bc1b710cd37531823ff514ff929e10754d38ee` and `wrote: <scratch>/fix-1/range.txt, 1138 lines`, and was read to its last line. It made no correction, so no correction's hunk is quoted. Statements it leaves standing: `frame/design.md` *Scope* item 6's "this repository's", for the reason above; the second *Not done* paragraph of `gaps.md`, on `chain_check.py#settled`'s docstring, unchanged by this pass. The sample is the two findings' own `git grep` commands above. It reaches only the words they search, and a statement of the same fact in other words, in `docs/` or in a skill, stands outside it.
```

## Confirmations

What matched: `frame/design.md` *Scope* item 1 against `.github/scripts/publish_release_note.py#settles`, lines 294-340, read. The commit list is `git log --no-merges --reverse`. Each commit's deleted paths come from the one-commit `git diff-tree --no-commit-id ... --diff-filter=D`. The directory pattern is bound to `optin.HOME`/`optin.WORK_ITEMS` and takes one path segment. A directory counts as gone only where `ls-tree` at the commit prints nothing, and `chain_check.settled` is asked at `<commit>^`. `phase-1.md` lines 7 and 9 claim that the two departures from the frame's commands (the `git log` and the one-commit `diff-tree`) list the same commits and compare the same trees for a commit other than a merge. I read that as so. The root commit deletes nothing and so reads as no settle, which sends a range with no previous tag to the refusal, the safe direction.

What matched: *Scope* items 2 to 4 against `main`, lines 995-1055, read. The settle reading is asked only where `fragments` returned no entry. `release_exists` still runs first, and the release pull request is read after it and before the title. A refusal exits 1 before `create` and writes no `created`. The existing refusal line keeps its words and is followed by one line per commit that is no settle. `release_pull_body`, lines 343-395, reads `gh pr list --base main --head release/v<version> --state merged` and keeps the entry whose `mergeCommit.oid` is `git rev-parse <tag>^{commit}`. It answers each of the four refusals of *Scope* item 4, and an unanswered `gh`, with its own sentence.

What matched: *Scope* items 5 and 7 and *Removes* against the module docstring (lines 29-38, 80-87, 117-122), the workflow header (`.github/workflows/publish-release.yml:18-23`) and the test module's A3 and A6 lines, read. Each is rewritten in place, apart from the statements finding 1 names.

What matched: the phase record's S6 run and probe claims, executed this round. A second probe ran the script at the target over the real v0.40.0..v0.40.1 history with real `gh` answers, `DRY_RUN=1` and `release_exists` alone answered False (Probes, row 3). It printed a 3171-character note. The note opens with the header `<p>1 pull request merged<br>0 issues closed</p>`, holds one fold of chores naming #1663 and the update section, and has #1664's body inside the closing fold. Its tags are balanced, because #1664's body holds no `details` tag. That agrees with `phase-1.md` line 44 (`release_pull_body` returned #1664's body), with G9 (a single settle commit, `31a5dfac`) and with G12.

What matched: `frame/plan.md` *Alternatives considered* row A9, which the frame left to review because its search was not whole. Method: `git grep -n -i details` over `lib/*.py`, `skills/*/scripts/*.py`, `bin/*`, `.github/scripts/*.py`, `.github/workflows/*.yml` and `hooks/*`, together with a list of the scripts and workflows that read a pull request body. That list holds `close_issues_on_release.py`, `label_merged_on_release_branch.py`, `publish_release_note.py`, `release_mark.py` and `hygiene.yml`. The one refusal of a `details` tag is `skills/code-review/scripts/pr_body.py:240`. It reads the lines `agentic pr-body` copies from a work item's records, never a body written with `gh pr create --body-file`, which is how `docs/releasing/release-checklist.md` *The release pull request* has the release pull request's body written. `close_issues_on_release.py:15` says it does not parse that body. `hygiene.yml`'s `chain_check.py` run judges a work item's body, and a release branch has no `routing.md` that names it. So no reader refuses an unbalanced `details` tag in a release pull request's body. The search is a sample under contract rule 12, since a reader could spell the tag some other way. Rule change 3 of the design and the `release_body` docstring at lines 903-904 put that risk on the owner's read before the merge. The mark is not put at risk: `release_mark.py#mark_release` finds the header by text, above every fold. This round finds no defect in the choice and opens no finding on it.

What matched: `frame/questions.md` Q1, as far as an offline run reaches. A probe built a settle-only note through `main`, with #1664's real body as the release pull request's, and handed it to `release_mark.py#mark_release` in a dry run (Probes, row 2). The mark ran at a tree holding no `routing.md`, as the real `v0.40.1` tree holds none (`git ls-tree -r --name-only v0.40.1 -- agentory/threads` printed no `routing.md`). The mark found the header exactly once and replaced it, so the default the question states, "The header is replaced", holds on this code path. The probe also shows what G13 leaves unsaid: on such a note, the review, work items, capped and deferred badges read `not read`. That is because `release_mark.py#chain_counts` reads a tree with no declaration as an incomplete count. The real `gh release view` and `gh release edit` and the suite at the tag stay unmeasured, as Q1 and the second `## Not verified` row of `gaps.md` say.

What matched: `changelog.md` and `pr.md` against the code and the records, read. Each statement of the fragment stands in the code at the target. Each quote in `pr.md` stands word for word at the coordinate it names: `routing.md` line 16, `frame/questions.md` Q1's default, and the *Judgments of the run* row of `frame/plan.md`.

What matched: `frame/plan.md` *Overlap with the release*, read against the two other work items' committed frames. `agentory/threads/1795841829-skill-descriptions/frame/design.md` changes the frontmatter `description` of `skills/settle/SKILL.md` and no section this work changes or cites. `agentory/threads/1795841830-find-leftovers-before-a-round/frame/design.md` names none of the files this work changes. Neither item's diff was reviewed.

The tests were read against their group, executed. `agentic layout --pairs` prints three pairs inside `Test_release_pull_body`. Each pair calls `release_pull_body` with equal arguments and a different `gh` answer: a match, four refusals, and a `gh` that never answered. Each case covers a branch the others do not, the same shape as the existing `Test_release_exists` pair. No new case duplicates its group.

`phase-1.md` line 29 reports one surviving mutant: `chain_check.settled(ROOT, f"{commit}^", gone)` replaced with `gone`. So no case holds the *Scope* item 1 sentence that a git read failing inside `settled` makes the commit no settle. The path is reachable only where `settled`'s `ls-tree` at `<commit>^` fails after `diff-tree` and `ls-tree` of the same commit answered. That leaves the shipped code as the frame says, so it is named here and opens no finding (`tests/github/test_publish_release_note.py:1454-1496`).

The change adds these failure paths. Every run now loads `skills/code-review/scripts/chain_check.py` when the script is imported (`.github/scripts/publish_release_note.py:155-156`), a release with fragments included. A load that failed would turn every publish red, and it would fail the test module's import first, so the suite meets it before a release does. `settles`' own git reads stop the run. The refusals of `release_pull_body` exit 1. Each is classified as the frame's design (*Scope* items 1 and 4, *Data & interfaces*).

The broad suite stays `unverified` in the phase record's account, and that label is honest: the phase record claims only narrow runs and the phase-boundary set.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at the branch's head, the `Broad gate` command of `agentory/config.json`; this round ran the one module `tests/github/test_publish_release_note.py` | the branch at `07f6f49a` | the orchestrator, at the broad run once the rounds settle |
| The settle-only path's real `gh release create`, `gh release view` and `gh release edit`, and the suite at a real tag; the probes stub each | `frame/questions.md` Q1, `gaps.md:8` | the orchestrator of the first release of settles alone after this ships |
| Whether a settle-only note's mark should show `not read` on its review, work items, capped and deferred badges, where the release's pull requests carry no work item. That is `release_mark.py#chain_counts`' reading of a tree with no `routing.md`, which this work's frame leaves unchanged (*Scope*, *Out of scope*) | `.github/scripts/release_mark.py:333-339` | the orchestrator, who may open an issue for it |
| The `seen red` runs of `phase-1.md` lines 17-25 and the mutation runs of lines 27-32; this round read their claims against the cases and did not rerun them | `agentory/threads/1795841828-settle-only-release-note/trail/phases/phase-1.md:17-32` | the inspector |

## Probes

| Command | Result |
|---|---|
| `uv run --no-project tests/run_tests.py -q -p no:xdist tests/github/test_publish_release_note.py` in the clone at `07f6f49a` | exit 0, 83 passed |
| `test_tmp_mark_settle_only.py` under the round's scratch directory, run with the clone's `.venv` python and `pytest -q -s`: `main` with its GitHub reads stubbed and #1664's real body as the release pull request's, then `release_mark.py#mark_release` in a dry run over the created note at a tree with no `routing.md` | The first run failed on the probe's own stub, which returned None where `milestone_description` returns "". With the stub corrected, the one run passed. The note opened with `<p>1 pull request merged<br>0 issues closed</p>`. The mark printed `items not read`, `capped not read` and `deferred not read`, and a marked header that replaced the plain one, with #1664's body kept below it |
| `test_tmp_dry_v0401.py` under the round's scratch directory: the clone's script with `TAG=v0.40.1`, `DRY_RUN=1` and `release_exists` alone answered False, over the real history and the real `gh` answers | exit 0. It printed the settle-only line, `the note carries the body of the release pull request #1664`, and a 3171-character note whose closing fold holds #1664's body |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.41.0 --root <the branch worktree> --worktree`, run before this record was written | exit 0. It printed no notice at any line of `frame/design.md`, and it named no `round-N.md` under `trail/rounds/` |
