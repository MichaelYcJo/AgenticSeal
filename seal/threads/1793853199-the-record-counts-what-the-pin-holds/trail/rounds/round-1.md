# Review round 1: 1793853199-the-record-counts-what-the-pin-holds

```seal
target: 4cbf5eb74 against release/v0.32.4
```

This round read the branch at 4cbf5eb74 against `release/v0.32.4` at
31558c76, in the branch worktree the spawn named, and ran its one probe in a
`git clone --no-local` of that worktree under the round's scratch directory,
removed after the run. No earlier round exists, so no fact was carried and
every fact below was established here. `seal/parity.md` is not declared, so
no comparison with an original is owed.

The range is five commits: routing (a5bad40f), frame (fe3a9cd0), the build
(333a2cfe, eleven lines of one docstring paragraph of
`tests/hooks/test_version_check.py` replaced by five), the phase record
(af548f1f) and the orchestrator's fold (4cbf5eb74, which adds a sentence
saying the frame's line coordinates are the base's and marks Q1 answered).
No file outside the work item's directory changes except that test module.

## Findings

### 1. The rewritten paragraph says only the module's own cases refuse a reworded notice, and a case outside the module refuses one

```seal
severity: should
location: `tests/hooks/test_version_check.py:101-103`, `seal/threads/1793853199-the-record-counts-what-the-pin-holds/changelog.md:3`
evidence: executed `python -m pytest tests/hooks/test_version_check.py -q -p no:xdist` and `python -m pytest tests/behaviour/test_a_cited_section_stands_in_its_file.py::test_every_cited_section_stands_in_its_file -q -p no:xdist` in a clone with the notice and its golden string reworded together (see `## Probes`); read `tests/behaviour/test_no_document_names_the_old_roots.py:94-104`
```

Why it matters: the paragraph's third sentence, at
`tests/hooks/test_version_check.py:101-103`, reads "A reworded notice is
still refused only where it breaks an assertion that another case in this
module makes on the notice." The changelog fragment repeats it at
`changelog.md:3`. The sentence is the deliverable of `frame/design.md` D1,
and the milestone's purpose is that docstrings under `tests/` "state only
what the tree holds now". This one states a closed list, and the list is
not whole.

The phase record claimed the sentence holds because "a search found no such
reader" outside the module, and it labelled that search a sample over
spellings (`trail/phases/phase-1.md`, the paragraph on the third sentence).
The search looked for words that name the notice or its file:
`reload-plugins`, `marketplace update agenticseal`, `version-check`,
`version_check`. It cannot find a case that reads every tracked file, or
every file under `hooks/`, without naming this one. Such cases exist:

- `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, whose
  docstring says it reads every path `git ls-files` lists and reads
  adjacent `.py` string literals as one. The probe reworded the notice in
  `hooks/version-check.py` and its golden string together, adding a
  sentence that cites a section `docs/running/the-run.md` does not have.
  `tests/hooks/test_version_check.py` then exited 0 with `22 passed`, and
  `test_every_cited_section_stands_in_its_file` exited 1 naming
  `hooks/version-check.py:161`.
- `tests/behaviour/test_no_document_names_the_old_roots.py:94-104`,
  `test_no_hook_names_the_0_3_x_roots`, opens every `.py` file under
  `hooks/` and refuses one that names `.specseal` (read).

So a reworded notice is refused by cases outside the module, and "only
... in this module" is false. A person or an agent who changes the notice
reads this paragraph to learn what will catch the change. The list of
readers is a class a method could make whole (every case that reads
`hooks/version-check.py`, by its name or by a listing of tracked files or
of `hooks/`), so a sentence that rests on it as whole cannot rest on a
search of spellings, contract rule 12.

`frame/design.md` D1's second bullet asks the paragraph to say "that what
still refuses a reworded notice is the assertions of the other cases in the
module that read the notice", and `frame/plan.md` A3 and acceptance row S1
say "the other cases' assertions on the notice". None of the three says
"only", so the fix below drops the exclusive claim and keeps the module's
cases as the named example. It meets D1 and S1 as written, and no frame
text changes. The fix names no count, as D1 requires.

The docstring, at `tests/hooks/test_version_check.py:100-105`:

```python
        What this does NOT do is check a REWORDING. An author who changes the
        notice and pastes the new text in here passes this case (#238). A
        reworded notice is still refused where it breaks an assertion that
        another case makes on its text, as the other cases in this module that
        read the notice do. Everything else is carried by the message below,
        which is an instruction to a person rather than a check.
```

The changelog fragment, the clause in `changelog.md:3` that reads "that a
reworded notice is still refused only where it breaks an assertion another
case in the module makes on the notice," becomes:

```markdown
that a reworded notice is still refused where it breaks an assertion another case makes on its text, the module's other cases that read the notice among them,
```

`trail/phases/phase-1.md` states commit 333a2cfe and stays as written; the
fix pass's own record says what changed.

## Confirmations

What matched: S2 holds. `git diff release/v0.32.4..HEAD -- tests hooks`
changes one hunk, `tests/hooks/test_version_check.py:98-111` at the base,
and every `+` and `-` line lies inside the docstring of
`Test_main.test_accepts_a_warning_that_names_the_cheap_move_before_the_expensive_one`.
No assertion, fixture or hook line changes. `git diff --stat` shows no
other file outside the work item's directory (executed).

What matched: S3 holds. The crafter claimed `bin/test
tests/hooks/test_version_check.py -q -p no:xdist` exits 0 with `22
passed`; the same command in the worktree at 4cbf5eb74 exited 0 with `22
passed`, `test_census` among them (executed). The crafter claimed ruff
check and format are clean on the file; `uvx ruff check` and `uvx ruff
format --check` on `tests/hooks/test_version_check.py` each exited 0
(executed).

What matched: S1 holds apart from finding 1. The paragraph at
`tests/hooks/test_version_check.py:100-105` names no count of properties,
cases or passes and no measured mutation, says a rewording that brings the
text along passes this case, cites `#238`, and keeps the sentence on the
assertion message (read).

What matched: the `## Removes` row says #238's body holds the measured
mutations and the `18 passed` count. `gh issue view 238 --repo
MichaelYcJo/AgenticSeal` shows the body listing the added overclaim, the
flipped gap, the restart named first and the dropped labels, and "leave the
module at `18 passed`" (executed). The changelog's facts on #238 match
that body.

What matched: S4 holds. `trail/phases/phase-1.md` lists D2's nine rows with
their coordinates at 333a2cfe and the paragraph's new text, and each
coordinate matches the file at HEAD: `:94-98`, `:100-105`, `:123-127` (the
assertion message), `:268-272`, `:274-279`, `:281-283`; the cases that read
the notice stand at `:53-57`, `:59-66`, `:198-204` and `:291-298` (read).
The paragraph at `:274-279` still says the absence half "is pinned in the
case above", which D2 kept with grounds, and the rewritten paragraph it
points to says what the pin does not do, so the two agree (read).

What matched: `gaps.md` *Not done* puts the `# Left for #923` comment at
`tests/hooks/test_version_check.py:266`, where it stands at HEAD, and the
`:81-92` paragraph at its length, as `frame/plan.md` A7 leaves it (read).

What matched: no case is added, so contract rule 15 owes no red run, and
`skills/verify/SKILL.md:182` gives a docstring change the row "That the
module still imports", which the narrow run shows (read, executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD, the modules that read `tests/hooks/test_version_check.py` by a listing of tracked files among them; `gaps.md` labels them `unverified` with the orchestrator as answerer, and that label is honest | `seal/config.md` *Broad gate* | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| In a `git clone --no-local` of the worktree at 4cbf5eb74, the notice in `hooks/version-check.py` and the golden string at `tests/hooks/test_version_check.py:111-122` both given the added sentence ``See `docs/running/the-run.md` *No such section here*.``; then `python -m pytest tests/hooks/test_version_check.py -q -p no:xdist -p no:cacheprovider` | exit 0, `22 passed` |
| The same clone: `python -m pytest tests/behaviour/test_a_cited_section_stands_in_its_file.py::test_every_cited_section_stands_in_its_file -q -p no:xdist -p no:cacheprovider` | exit 1, `1 failed`; the failure names `hooks/version-check.py:161` and `tests/hooks/test_version_check.py:122` citing `docs/running/the-run.md` *No such section here*. The clone and its outputs were removed after the run |
