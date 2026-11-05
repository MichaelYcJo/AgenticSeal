# Phase 1: 1793853199-the-record-counts-what-the-pin-holds

## What this phase found

**The frame holds, and the phase builds to it with no departure.** Before the edit, the paragraph `frame/design.md` D1 names stood at `tests/hooks/test_version_check.py:100-111` at `fe3a9cd0`, from "What this does NOT do is check a REWORDING." to "an instruction to a person rather than a check." (executed: `grep -n`). The module held 21 test functions and `test_census` (executed: `grep -n "def test_"`, 21 lines; the narrow run collected 22 cases). #238 is open with no comments, and its body names `tests/test_version_check.py:108`, the ledger row S1·S2·S3 and round 3 of `1788789330-the-update-notice-names-the-expensive-move` (executed: `gh issue view 238`). `seal/follow-up.md` holds no row on this work or on the notice (executed: `grep -n "238\|version"`, no line). The line coordinates D2 gives match the base tree (read). No removal beyond the frame's `## Removes` was made.

**Q1, the words of the rewritten paragraph, answered by this phase.** `frame/questions.md` Q1 left them to the work. The paragraph at `333a2cfe`, `tests/hooks/test_version_check.py:100-105`, reads:

> What this does NOT do is check a REWORDING. An author who changes the notice and pastes the new text in here passes this case (#238). A reworded notice is still refused only where it breaks an assertion that another case in this module makes on the notice. Everything else is carried by the message below, which is an instruction to a person rather than a check.

Each of D1's four points, read against that text:

- A rewording that brings the text along passes this case, with `#238` as the grounds: the second sentence.
- What still refuses a reworded notice is the assertions of the other cases in the module that read the notice, with no number: the third sentence. It names neither a count of properties nor a count of cases.
- The rest is carried by the assertion message, an instruction to a person rather than a check: the last sentence, kept from the base text.
- No measured mutation and no pass count: the list of measured mutations and "Every one left the module at `18 passed`" are gone, and #238's body holds them.

The third sentence says "only", so it is true only if nothing outside the module reads the notice's text. A search found no such reader (executed: `git grep` over `tests`, `evals` and `.github` for `reload-plugins`, `marketplace update agenticseal` and `version-check`, and `git grep -l "version-check.py\|version_check"` over `tests` and `evals`). `tests/hooks/test_optin.py` loads the hook in two cases and asserts that it prints nothing. `tests/hooks/test_dispatch.py` names the file in dispatch tables. Neither reads the notice's text (read). Inside the module, the cases that read the notice are at `:53-57`, `:59-66`, `:198-204` and `:291-298` at `333a2cfe`, besides the exact pin (executed: `grep -n "systemMessage\|notice("`). The search is a sample over spellings: a reader that names the notice in words the search did not hold is not on it. Grounds: `skills/core/SKILL.md` *The rule a mechanism is kept against*, which keeps no stored count beside the tree, so the sentence names where the protection stands and not how much of it there is.

**D2's class, at `333a2cfe`.** The list is the frame's, built by taking the module's text apart into its docstrings, comments and the assertion message. This phase read each entry again after the edit. Coordinates below `:105` moved up six lines.

| Coordinate at `333a2cfe` | Coordinate at `fe3a9cd0` | What it states | Disposition |
|---|---|---|---|
| `:1-8` | `:1-8` | the hook's three limits | stays: it states no property of the pin |
| `:71-79` | `:71-79` | what run 6 of `docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.md` measured | stays |
| `:81-92` | `:81-92` | why the message is pinned exactly: four predicates, each blind one word over | stays (`frame/plan.md` A7) |
| `:94-98` | `:94-98` | a rewording that does not bring the golden string along fails this case | stays, and the rewritten paragraph follows it |
| `:100-105` | `:100-111` | the paragraph above | rewritten (D1) |
| `:123-127` | `:129-133` | the assertion message, the instruction to the person who changes the notice | stays |
| `:268-272` | `:274-278` | why the notice and the hook's docstring must agree | stays |
| `:274-279` | `:280-285` | this case checks the presence half; the absence half is pinned in the case above | stays: "pinned" is true of the text as it stands, and the rewritten paragraph in the case it sends the reader to says a rewording passes the pin |
| `:281-283` | `:287-289` | why the docstring is read whitespace-normalised | stays |

**No case is written and no `seal mutate` runs.** The phase changes prose inside a docstring and adds no behaviour. `skills/verify/SKILL.md` *The narrow command still has to be able to fail* gives "A comment or docstring inside source" the row whose failure is that the module still imports, and `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* asks a case first only of a scenario that adds behaviour.

**The narrow run at `333a2cfe`'s tree** (executed, before the commit, on the same bytes): `bin/test tests/hooks/test_version_check.py -q -p no:xdist` exited 0 with `22 passed`, `test_census` among them. `uvx ruff check tests/hooks/test_version_check.py` exited 0 and printed "All checks passed!" for that one file. `uvx ruff format --check` on the same file exited 0. The phase boundary set of `skills/verify/SKILL.md` *Scope: cheap and often, broad and once* also names the test modules that read the changed file by a glob over a directory that holds it, such as the census modules. The spawn narrowed the run to the module and ruff, so those modules were not run here, and `gaps.md` names who answers them.
