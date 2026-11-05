# Closing memo: 1793853195-the-dispatcher-passes-no-allow

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the branch's HEAD; phase 1 ran the 18 modules that name the dispatcher in one command, round 1's fix pass ran `tests/hooks/test_dispatch.py` alone, and every other module of the suite is unrun, the ones that read the records under `seal/threads/` among them | the orchestrator's broad run |
| The new `Test_merge` cases on the ubuntu and Windows legs; phase 1 and round 1's fix pass ran them on macOS alone | the `tests` workflow on the pull request |
| `merge` under Python 3.9, the oldest `python3` the dispatcher is written for; phase 1 called it by hand under `/usr/bin/python3` 3.9.6 for four shapes, and no CI leg runs 3.9 (`frame/design.md` *What a change to a gate must carry*) | the dispatcher's first run under a stock macOS `python3` after the release |
| Whether the change clears `HOOK_GRANTS_PERMISSION` in the plugin directory's validation (`frame/questions.md` Q1) | the owner, who resubmits the next release's `MichaelYcJo/AgenticSeal@dist` after this release ships and writes the result on #1381 |

## Not done

A lone `{"decision": "approve"}` on `PreToolUse` prints `{}` and not nothing. Printing nothing in its place was within reach and not taken. *Scope* 2 asks the JSON path to print as it does now apart from the two fields, and Claude Code reads an empty object as no decision.

A dropped decision's reason beside a decision-less JSON object is not printed, as plain text beside such an object was not printed before. Carrying a gate's text into the JSON path's object was within reach and not taken. It changes what every event's JSON path prints, which `frame/design.md` *Out* keeps out of this work, and no gate prints either shape (`trail/phases/phase-1.md`).
