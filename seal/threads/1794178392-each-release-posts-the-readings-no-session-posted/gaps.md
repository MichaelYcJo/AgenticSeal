# Closing memo: 1794178392-each-release-posts-the-readings-no-session-posted

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check over phase 1's tree. Phase 1 ran `tests/skills/test_session_cost.py` and 42 modules that read a path it changed, and ran ruff over the two Python files it changed | the orchestrator, at the broad gate after the review rounds settle |
| A real `--post` of a body with `# <file name>` lines and no command text, onto the open `flow-measurement` log. Every case stubs `run_gh`, so no case reaches GitHub's rendering of the fence | the orchestrator, at the next segment reading it posts with the tree's `session_cost.py` |
| The full suite, the repository-wide lint and the format check over phase 2's tree. Phase 2 ran `tests/skills/test_session_cost.py`, `tests/text/test_a_segment_feeds_the_flow_log.py` and the modules its record names, and ran ruff over the three Python files it changed | the orchestrator, at the broad gate after the review rounds settle |
| The full suite, the repository-wide lint and the format check over round 1's fix pass. The pass ran `tests/text`, `tests/behaviour`, `tests/skills/test_session_cost.py`, `tests/skills/test_payload_meter.py`, `tests/skills/test_seal.py` and `tests/github/test_run_tests.py` as one command, and ran ruff over the two Python files it changed | the orchestrator, at the broad gate after the review rounds settle |
| `seal cost --work-item <dir> --post` against the real tracker: a real comment posted, and `gh api --paginate` read over a log whose comments span more than one page. The read-only runs read #1438, which held one comment, so one page; the case for two pages stubs `gh` | the orchestrator, at the 0.36.0 release step, which runs the tree's script for each work item the release ships |

## Not done

Phase 1 leaves the `--spawns` page's `what each cycle spawned` lines as
they are. Those lines print each spawn's `description`, the short label the
orchestrator gives an `Agent` call, into a posted body. They are not command
text, and `frame/design.md` *Grounding* judged `report_spawns` to print none,
so *Scope* item 7 does not reach them. Whether such a label may leave the
machine is a question for the frame, not for this phase.
