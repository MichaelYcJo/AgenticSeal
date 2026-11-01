# Closing memo: 1793538230-code-text-brought-to-the-tree

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the work item's head. Phase 1 ran its phase-boundary set of 19 modules (`trail/phases/phase-1.md`), and ran `ruff check` and `ruff format --check` on its four changed Python files alone (contract rule 2) | the orchestrator, by `seal gate` after the review rounds settle |
| `frame/questions.md` Q1: whether the case `tests/hooks/test_console.py::Test_module::test_a_release_script_run_on_its_own_gives_the_answer_streams_holds` passes on the Windows legs of `.github/workflows/test.yml`. Phase 1 ran it on darwin alone | the pull request's Windows legs, read by the orchestrator |
| Phase 2's run of its phase-boundary set reported 9 cases skipped among 34 modules, and which cases they were and why was not read (`trail/phases/phase-2.md`) | the orchestrator, by `seal gate`, whose run reads the whole suite |
| A figure about the stream answer's call sites spelled in a way design *Scope* item 5's search does not match. Phase 2 ran that search with a wider list of number words, and it is still a search on words, so it is a sample | the repository owner, through the `seal/follow-up.md` row on a figure about a corpus stated with no moment |

## Not done

nothing
