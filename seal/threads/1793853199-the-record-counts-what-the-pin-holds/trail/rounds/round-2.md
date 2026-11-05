# Review round 2: 1793853199-the-record-counts-what-the-pin-holds

```seal
target: 51bd48c9, fixes 4cbf5eb7..51bd48c9
```

This verifying round read the diff `4cbf5eb7..51bd48c9` in the branch
worktree the spawn named. It ran its one probe in a `git clone --no-local`
of that worktree at 51bd48c9, under the round's scratch directory, and
removed the clone and its outputs after the run. `seal/parity.md` is not
declared, so no comparison with an original is owed.

The range is three commits. 8131251f is the fix pass: it rewrites the third
sentence of the paragraph at `tests/hooks/test_version_check.py:100-105`
and the matching clause of `changelog.md:3`. b82f346b appends round 1's
close block. 51bd48c9 is the orchestrator's fold of `frame/questions.md`
Q1's Status cell. No file outside the work item's directory changes except
the test module, and there only lines 102-105, all inside the docstring of
`Test_main.test_accepts_a_warning_that_names_the_cheap_move_before_the_expensive_one`
(executed: `git diff --stat` and `git diff` over the range).

Carried from round 1 as coordinates, and opened rather than searched for
again: the two readers outside the module,
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` and
`tests/behaviour/test_no_document_names_the_old_roots.py:94-104`. Round 1's
probe was written again from its `## Probes` rows and re-run, and lines
94-104 were read again. Round 1's confirmations of S2 and S4 over the build
are carried and not re-judged; the fix diff touches neither.

## Findings

No finding. The range adds no case, so no test is read against a group.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the docstring no longer states a closed list of the cases that
refuse a reworded notice. At `tests/hooks/test_version_check.py:101-104`
it reads "A reworded notice is still refused where it breaks an assertion
that another case makes on its text, as the other cases in this module that
read the notice do." The word "only" is gone, and the module's cases stand
as the named example (read). The sentence is true of the tree: with the
notice in `hooks/version-check.py` and its golden string reworded together,
the module exits 0 with `22 passed`, and
`test_every_cited_section_stands_in_its_file` exits 1 naming
`hooks/version-check.py:161` (executed, see `## Probes`).
`test_no_hook_names_the_0_3_x_roots` opens every `.py` file under `hooks/`
and asserts on its text (read, `tests/behaviour/test_no_document_names_the_old_roots.py:94-104`).
So a case outside the module does make an assertion on the notice's text,
as the new sentence allows. "Everything else is carried by the message
below" now reads as the complement of every case's assertions, which is
true. The changelog clause at `changelog.md:3` says the same: "refused where
it breaks an assertion another case makes on its text, the module's other
cases that read the notice among them" (read).

What matched: D1 and S1 still hold for the new text. It names no count of
properties, cases or passes and no measured mutation. It keeps "passes this
case (#238)" and the sentence on the assertion message, and it names the
module's other cases that read the notice, which D1's second bullet asks
for (read, `frame/design.md:32-35`, `:72`). D1's bullet and S1's "are what
remain" can be read as an exclusive list too. They state what the paragraph
must say, and the paragraph says it without the exclusive word. The frame
lists no rule change, so the settle carries no sentence of it forward. This
is no finding.

What matched: the fix pass claimed that `bin/test
tests/hooks/test_version_check.py -q -p no:xdist` exits 0 with 22 passed,
and that `uvx ruff check` and `uvx ruff format --check` on the file each
exit 0. The same three commands at 51bd48c9 exited 0, 0 and 0, the first
with `22 passed` (executed).

What matched: the fix pass claimed its list of the exclusive claim's
instances is closed inside the range and the work item's directory, and a
sample outside it. Inside, `trail/phases/phase-1.md:9` and `:18` quote and
discuss the text at 333a2cfe, the commit the record names, so they stand.
`trail/rounds/round-1.md` quotes the old text as its finding. Neither is a
statement of the present. Outside `seal/threads/`, `git grep -n -i` for
"only where", "in this module makes", "refused only" and "another case in"
found no other statement of the claim; every hit states something else
(executed). That search is a sample over wordings, as the close block
labels its own. The class of sentences in the tree saying what refuses a
reworded notice is open, so a sample is the honest label.

What matched: the fold at 51bd48c9 says round 1's fix pass "rewrote the
third sentence at 8131251f, as its close block in `trail/rounds/round-1.md`
records". 8131251f changes only the third sentence of the paragraph
(executed: `git show --stat 8131251f` and the range's diff of the test
module, which only 8131251f touches). The close block at `trail/rounds/round-1.md:98-101`
names `fixed 8131251f` and says both paste-ready texts were applied (read).

What matched: the new lines at `tests/hooks/test_version_check.py:102-104`
match the paste-ready text round 1 gave, word for word, and the changelog
clause matches its snippet (read, against `trail/rounds/round-1.md:78-93`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD, the modules that read `tests/hooks/test_version_check.py` by a listing of tracked files among them. `gaps.md` labels them `unverified` with the orchestrator as answerer, and that label is honest. This round leaves nothing open, so the broad run is what comes due, then the sealer's spawn | `seal/config.md` *Broad gate* | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| In a `git clone --no-local` of the worktree at 51bd48c9, the notice in `hooks/version-check.py` and the golden string at `tests/hooks/test_version_check.py:119-121` both given the added sentence ``See `docs/running/the-run.md` *No such section here*.``, through the Edit tool; then, from the clone, the worktree's `.venv/bin/python -m pytest tests/hooks/test_version_check.py -q -p no:xdist -p no:cacheprovider` | exit 0, `22 passed` |
| The same clone: `.venv/bin/python -m pytest tests/behaviour/test_a_cited_section_stands_in_its_file.py::test_every_cited_section_stands_in_its_file -q -p no:xdist -p no:cacheprovider` | exit 1, `1 failed`; the failure names `hooks/version-check.py:161` and `tests/hooks/test_version_check.py:122` citing `docs/running/the-run.md` *No such section here*. The clone and its outputs were removed after the run |
