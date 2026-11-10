# Review round 1: 1794271938-follow-up-holds-seven-owner-questions

```seal
target: 526b47887 against origin/release/v0.37.1
```

The base is the merge base `8657297d5`. `origin/release/v0.37.1` has moved since the branch forked, and the range read is `8657297d5...526b47887`. This is the first round, so no earlier round's facts are carried: each fact below was opened or run in this round. The work item's present-state records were each read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`. No `pr.<lang>.md` stands, and `Commit and pull request language` is English. The three phase records were read too. `seal/parity.json` is not declared.

## Findings

### 1. `argv_words` reads no tuple literal, so the two converted cases lost a catch the fold had, and its docstring calls it strictly stronger than the fold

```seal
severity: should
location: `tests/github/test_close_issues_on_release.py:112`, `tests/github/test_close_issues_on_release.py:86`, `tests/github/test_close_issues_on_release.py:106`, `tests/github/test_release_completeness_check.py:577`, `tests/github/test_label_merged_on_release_branch.py:400`
evidence: executed `.venv/bin/python -m pytest -p no:cacheprovider -p no:xdist -q -s tests/github/test_tmp_argv_shapes.py` in a clone at `526b47887`; read `tests/github/test_close_issues_on_release.py:84-121`
```

Why it matters: `frame/design.md` *Scope* item 1 says that each converted case "keeps every claim it made". The folded cases claimed that the text `"gh", "issue", "<verb>"` stands nowhere in the script's source, inside any container. `argv_words` collects argvs from `ast.List` nodes and from `ast.Call` positional arguments only (`tests/github/test_close_issues_on_release.py:112-113`). An argv written as a tuple literal, such as `subprocess.run(("gh", "issue", "edit", str(n), "--add-assignee", who))`, is a `Call` whose one argument is an `ast.Tuple`. That argument is not an `ast.Constant`, so the call's words are empty, and the tuple itself is never read. The probe parsed that source. `argv_words` did not list the prefix `["gh", "issue", "edit"]`, and the old fold found `"gh", "issue", "edit"` in the folded text. A tuple spread with `*` behaved the same way: the fold caught it and `argv_words` did not. So `test_the_gate_writes_nothing` and `test_the_script_only_ever_creates_a_label_and_adds_one` now pass a tuple-form forbidden argv that they refused at the base.

The docstring says the opposite at `:106`: "this reader is strictly stronger than a fold of the source and blind in a place the fold was blind too." The two readers are not ordered. The parse catches single-quoted words, which the fold missed (the same probe), and the fold catches a tuple, which the parse misses. The changelog's *Changed* second item names one escape that remains, a module-level name, and a reader takes that as the only one.

Claimed: phase 1 says the conversion keeps each claim, and it shows each converted case red against a comment-split plant. Found: those plants hold. The tuple container is a fourth spelling that the plants did not try.

The class is the literal containers that can hold an argv: list, tuple and set. A set is unordered, so it cannot carry an argv's word order, and `ast.Starred` over a tuple is read once tuples are read. Reading `ast.Tuple` beside `ast.List` closes the class. The three scripts hold no tuple that opens with `"gh"` (executed, `grep -n '("gh"'` over the three scripts, no hit), so no case changes its verdict at the target. The fix also owes `frame/design.md` *Data & interfaces* line 72, which says "one list of strings per `ast.List` and per `ast.Call`". That is a frame sentence, so the orchestrator folds it.

```python
def argv_words(text):
    """The string-literal words of every argv in TEXT, a script's source:
    each list or tuple literal's elements and each call's positional
    arguments.
    ...
    So this reader closes what a fold of the source closed, and more, and it
    is blind in a place the fold was blind too. Closing that means resolving
    module-level names before comparing, which is a different checker with
    its own false-positive argument to make; #1493 left it open.
    """
    tree = ast.parse(text)
    argvs = [
        node.elts
        for node in ast.walk(tree)
        if isinstance(node, (ast.List, ast.Tuple))
    ]
    argvs += [node.args for node in ast.walk(tree) if isinstance(node, ast.Call)]
```

The `...` stands for the docstring's two paragraphs that stay as they are. "Closes what a fold closed, and more" holds only once tuples are read. If the fix pass names the tuple escape in the docstring instead of closing it, the changelog's *Changed* second item owes the same sentence, and `pr.md` line 4 quotes that item.

```seal
verdict: fixed 3a0054d24
answer: `argv_words` reads `ast.Tuple` beside `ast.List` (`tests/github/test_close_issues_on_release.py:116-118`). A tuple spread whole, `run(*("gh", …))`, is read through the same half, because the spread tuple is its own node; a mixed spread such as `run("gh", *("issue", "close"))` stays unread, as the fold left it. The docstring names the tuple and the whole spread, and says the reader closes every argv a fold closed, a list, a tuple and call arguments, and more. Seen red with `seal mutate` planting, in each of the three scripts, one forbidden argv as a tuple and one as a whole-spread tuple: all six stayed green at `a5e6c5038` and all six went red at `3a0054d24`, each on its forbidden-verb assertion (executed). `changelog.md` *Changed* second item now says the reader reads a list, a tuple or call arguments, and that any first-three word that is not a string literal escapes. Removing the `ast.Tuple` half leaves the three `Test_module` groups green at HEAD, since no script holds a tuple argv (executed, `SURVIVED`); `gaps.md` *Not done* records it. `frame/design.md:69`, the docstring's first line in *Data & interfaces*, and `pr.md` line 4 are the orchestrator's to fold.
```

### 2. The release note says the owner decided row 5 and that `--worktree` keeps reading routing from HEAD, and the issue and `chain_check.py` say otherwise

```seal
severity: should
location: `seal/threads/1794271938-follow-up-holds-seven-owner-questions/changelog.md:9`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/pr.md:7`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/questions.md:16`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/routing.md:21`
evidence: executed `gh issue view 1493 --json title,body,comments,state`; read `skills/code-review/scripts/chain_check.py:362-381`, `skills/code-review/scripts/chain_check.py:495-506`, `skills/code-review/scripts/chain_check.py:2088-2093`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:21`
```

Why it matters: the changelog's *Removed* first item becomes a release-note line, and `pr.md` line 7 quotes it into the pull request body. Two of its claims are wrong.

First, the owner. The sentence says "the owner decided that the width of a comment line in a shipped script earns no check". The issue's *Decided* names the owner for row 2 ("owner, 2026-11-10"). For row 5 it says "closed without a check ... (orchestrator's default, reported to the owner)". The same misattribution stands in two records that state the present. `frame/questions.md:16` says "The owner decided rows 2 and 5 in the issue's *Decided*", which cites the very bullet that says otherwise. `routing.md:21` says "The owner answered rows 2 and 5". A reader of the release note, and the sealer reading the records against the issue, would take an orchestrator's default for an owner's decision. If the owner did decide row 5 after the issue was written, the issue body is where that belongs, and then these sentences hold.

Second, `--worktree`. The sentence says "`chain_check.py --worktree` keeps reading routing from HEAD". Under `--worktree`, `changed` diffs the working tree and counts untracked files as added (`chain_check.py:369-381`). `read_record` reads each declaration from disk (`:495-504`), and the comment at `:2088-2093` says the working tree is "where `read_record` and `changed` read the declarations from". Only the branch's own declaration is found from what HEAD carries (`tracked_declarations`). `frame/design.md:21` (G13) says the same: `--worktree` "already reads the records from the working tree". What row 1's closure keeps is narrower. A local-mode root sits under the common git directory, so `--worktree` still finds no declaration there and reports that it examined nothing.

The fix rewrites the one sentence. `pr.md` line 7 must then quote the new text word for word. The two frame and routing sentences are the framer's and the orchestrator's, so the orchestrator folds them.

```markdown
Rows 1, 4 and 5 close with no change to the tree. `chain_check.py --worktree` still reads no declaration from a local-mode root, which git does not carry. A checker for a figure stated with no moment would block on a reading guessed from words. The width of a comment line in a shipped script gets no check, by the orchestrator's default reported to the owner.
```

`frame/questions.md:16` and `routing.md:21`, unless the owner's decision on row 5 is recorded in the issue:

```markdown
The owner decided row 2 in the issue's *Decided*, row 5 closed by the orchestrator's default reported to the owner, and the tree or a probe answered the rest.
```

```seal
verdict: fixed 3a0054d24
answer: `changelog.md` *Removed* first item carries the round's sentences word for word, read first against #1493 *Decided* (executed, `gh issue view 1493`) and `skills/code-review/scripts/chain_check.py:362-381`, `:495-506` and `:2085-2093` at HEAD (read): `--worktree` diffs the working tree and its untracked files, and a local-mode root under the common git directory is in neither. Its last clause now says the measurements are in #1493's body, as `frame/design.md` *Scope* item 8 reads after `a5e6c5038`. `frame/questions.md` and `routing.md` were folded at `a5e6c5038` and read whole at HEAD agree with the issue. `pr.md` line 7 still quotes the old sentence and is the orchestrator's to rewrite.
```

## Confirmations

What matched: *Scope* item 1 holds apart from finding 1. `argv_words` stands at module level at `tests/github/test_close_issues_on_release.py:84-121`. The three cases read through it (`:1187`, `tests/github/test_release_completeness_check.py:577`, `tests/github/test_label_merged_on_release_branch.py:400`), and neither converted module folds the source any longer (read). The sentence that cited `seal/follow-up.md` now says that #1493 left the escape open (`:109`). The six changed test modules passed in one narrow run, 170 passed, exit 0 (executed).

What matched: *Scope* item 2. `tests/behaviour/test_waiver_decided_at_start.py:231-240` compares `offered(template, routing.IMPLEMENTATION)` with `routing.IMPLEMENTATION_ANSWERS`, and the case is renamed `test_the_template_PARSES_into_the_THIRD_axis_it_ships` (`:177`). No sibling case covers the comparison already. The only other readers of `IMPLEMENTATION_ANSWERS`, at `tests/lib/test_routing.py:128` and `:335-347`, parse strings the test builds and never read the template (read). The literal pin at `:211` and the substitution loop at `:222-227` do not see a constant renamed with the template untouched, so the new assertion covers what its group did not. Phase 2's red runs of it are claimed, and this round did not re-run them.

What matched: *Scope* item 3. The two `next time` lines are gone, and the header pins stand at `tests/text/test_a_rider_reaches_its_file.py:87-88`. The docstring says that the case reads no row (read).

What matched: *Scope* item 4 and S6. `skills/implement/SKILL.md:325-328` carries the *Data & interfaces* sentence word for word, and lines 112 to 116, which hold `KNOWN_PROSE`'s line, are untouched (read). This round ran a `git grep -n -i` over the tree, outside `seal/threads/` and `.test_durations`, for `status cell`, `status column`, `commit that closed`, `tick and`, `where a hash` and `a hash is not`. It also grepped `lib/`, `skills/*/scripts` and `.github/scripts` for `Status` and `Phases` (executed). Every statement found says what a closed phase carries or who writes the cell: `seal/README.md:113-116`, `templates/setup/seal-README.md:113-116`, `agents/crafter.md:177`, `agents/sealer.md:99-101`, `skills/implement/orchestration.md:130`, `docs/running/the-run.md:87` and `docs/running/the-agent-set.md:117`. None states the cell's values as a closed set, and no script reads a Status cell. The class is a spelling class, so this list is a sample, as phase 3's own list is.

What matched: *Scope* item 5 and S5. `seal/follow-up.md` keeps the heading *Schedulable items with nowhere else to go* and its header row with no rows, and its header prose is unchanged (read).

What matched: *Scope* item 6 and S7. The four comments now state their reason without citing a row: `.github/scripts/run_tests.py:57-58`, `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:403-408`, `tests/conftest.py:293-297` and `tests/test_conftest.py:364-366` (read). This round ran `git grep -n "follow-up"` outside `seal/threads/` and `.test_durations` and read each hit, and grepped `follow-up list`, `followup` and `schedulable` too (executed). No hit says that `seal/follow-up.md` names or carries a particular item. The list reaches only the citations that use one of those spellings, so it is a sample.

What matched: the issue comment of *Data & interfaces*, read against what it cites. `8657297d5:seal/follow-up.md` holds the seven rows at lines 42 to 48. `aa687d357:seal/specs/1788817289-local-mode-from-first-setup-to-the-gate/spec.md` holds *The sharp question — where an untracked declaration lands* at its line 43. `11f3cde8` does not resolve, as item 6 says (executed, `git cat-file` and `git show`). Each row's measurements, its dates, commits, counts and round numbers, appear in the comment's matching item (read against `8657297d5:seal/follow-up.md:42-48`). Item 5's 292 lines and `ba4d85629` match the issue's *Decided* (executed, `gh issue view 1493`).

What matched: each of the nine quotes in `pr.md` stands word for word, with whitespace runs collapsed, at the source its coordinate names (executed, a `python3 -I` read of `pr.md`, `changelog.md` and `frame/plan.md`).

What matched: `gaps.md` *Not done* claims that the branch changes neither `tests/censuses.py` nor `lib/optin.py`. `git diff --stat 8657297d5...HEAD` lists neither. In `tests/conftest.py` and `tests/test_conftest.py`, the diff changes only the docstrings at `tests/conftest.py:291-298` and `tests/test_conftest.py:364-366` (executed, read). The diff does not touch what `Test_census_case` reads.

What matched: `uvx ruff check` and `uvx ruff format --check` over the nine changed `.py` files both exited 0 (executed). This is a narrow run of the changed files, not the repository-wide lint.

One gap of a case that holds no fact the frame states: the `isinstance(a.value, str)` filter at `tests/github/test_close_issues_on_release.py:118` came over from the case-local `words` unchanged and no case pins it, as `gaps.md` *Not done* says.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate, the full suite and the repository-wide lint. It is `unverified` in this round, and `gaps.md` names the orchestrator's run and `trail/gate.md` as its record | `seal/config.json` `Broad gate` | the orchestrator |
| The two `tests/test_conftest.py::Test_census_case` failures that phase 3 records. The diff does not touch what they read (Confirmations), so this round did not run them | `tests/test_conftest.py`, `tests/censuses.py` | the orchestrator, at the broad gate |
| Whether a comment on #1493 meets the issue's *Done when*, which says the measurements "move to the issue body or the commit message where the row is closed". `470b27194`'s message carries none, and the comment is not posted yet | `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:38` | the orchestrator, who posts the comment or moves the text into the issue body |

## Probes

| Command | Result |
|---|---|
| `.venv/bin/python -m pytest -p no:cacheprovider -p no:xdist -q -s tests/github/test_tmp_argv_shapes.py`, in a `git clone --no-local` at `526b47887` under the round's scratch directory, with the probe file deleted after its one run | 1 passed. It printed `tuple: argv_words sees False fold sees True`, `splat: argv_words sees False fold sees True` and `single quotes: argv_words sees True fold sees False` |
| `.venv/bin/python -m pytest -p no:cacheprovider -q` over the six changed test modules, in the same clone | exit 0, 170 passed |
| `uvx ruff check` and `uvx ruff format --check` over the nine changed `.py` files | exit 0 for both, and `9 files already formatted` |
| `gh issue view 1493 --json title,body,comments,state` | open, no comments. *Decided* names row 2 as the owner's and row 5 as "orchestrator's default, reported to the owner" |
