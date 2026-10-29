# Overview: 1793174170-two-facts-kept-in-several-files-have-drifted

## Why this work exists

Seven facts stood in more than one file and two of them had already drifted, so each now has one source, and a case reads the list a prose count stood for.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| A reader outside the frame's list | `frame/design.md` names the stamp module as the one re-pointed reader of the gate prose. `test_first_setup_asks_once.py#test_the_gates_table_says_the_root_may_sit_under_the_git_dir` read every row whose last cell names `` `seal/` `` as a gate row, and the rewritten `seal/` row of the records table made it red | the case reads the gate table's rows alone | Contract rule 18: "When a check refuses code that is correct, fix the check or report the refusal" |
| S6's proof | `frame/design.md` S6 names the re-pointed README case as the proof, and says the skill section "holds the way back, the staged-change reason and the pathspec reason, and cites `docs/one-root-by-lifetime.md`". No case read those reasons in the skill | a second case, `test_first_setup_asks_once.py#test_the_way_back_before_the_commit_to_shared_is_told_in_its_home`, pins them | Contract rule 14: a change to what a person reads "documents it and pins it" in the same commit |
| The `root-migrate` row's wording | Phase 1 wrote `seal/specs/<id>/` and `~/.claude/specseal/` into the row. `tests/test_censuses.py` refuses both names, and a table cell has no line above it for the exemption marker | phase 2 reworded the row: "each 0.22.x work item" and "the state files an earlier release wrote under its old name" | The census reads every tracked file, and the frame did not name a spelling |
| The edition walk's git listing | `frame/design.md` *Data & interfaces* says `pairs()` lists through `git ls-files`, and phase 5 built it with no guard. The broad gate at `930665ec` failed two cases of `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`, whose census refuses a scope that lists paths from git without `on_disk`. That module reads every test module, so a `git grep` on the changed paths never named it | `d91641fb` gave `pairs()` the shared guard and the census's first table the scope. Round 3 found that it declined the whole case over any deleted edition and that a deleted English half dropped its pair unread, so `c81cb9ff` and `27b8deee` rewrote it: `pairs(root)` lists `*.md` once, splits the listing with `on_disk`, and returns each tracked half of a pair the working tree deleted. The outline case judges every pair on disk first, and `unread()` declines only where every unread named pair is explained by a deleted half. A `build_tracked_tree` case pins the decline, the report and the mid-edit neighbour | The census's own rule: "A scope missing from all six tables below turns the case red until somebody classifies it", and `tests/conftest.py#on_disk` says a case proving an entry alive declines on the missing half while a sweep "judges what remains and ignores it"; `test_no_document_names_the_old_roots.py#uncovered` is the conditional decline copied |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck at this work item's last commit | executed by the orchestrator's broad gate at `9e34e9e5` against `5287dd42`, passed (`trail/gate.md`), and this repository declares no typecheck (`seal/config.md` *Broad gate*; #951 would add one) |
| closed The Fires, Does and Where cells of the `worktree_consent` and `root-migrate` rows. S1's case reads a row's name only, and the cells were written from the two hooks' docstrings and `main` | review round 1 read all four cells of both editions against the hooks: every cell held but the Korean root-migrate Does cell, which its finding 2 corrected at `21369c34` (`trail/rounds/round-1.md`) |
| closed That each Korean sentence this work rewrote says what its English one says. No case compares sentences across the two languages | review round 1 read both editions: every rewritten Korean sentence said what its English one says but the root-migrate row, which its finding 2 corrected at `21369c34` (`trail/rounds/round-1.md`) |

## Not done

The `add` to `docs/the-session-hooks.md` *Registration* that `frame/design.md` *Rule changes* states was not written into `docs/`. The spawn prompt names it the settle's, and `skills/implement/SKILL.md` *Document layout* says a pull request does not edit the policy root.

## Fed back into the spec

none
