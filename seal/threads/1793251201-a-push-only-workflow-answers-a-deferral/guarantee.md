# Guarantee: 1793251201-a-push-only-workflow-answers-a-deferral

| Field | Value |
|---|---|
| Target SHA | d56de90ea against 10942072d |
| Broad gate | 6ef65ee06 against 10942072d |

The base `release/v0.24.2` resolved through `origin/release/v0.24.2` to
10942072d (executed). `git log --no-merges --name-only 6ef65ee06..HEAD
^10942072d` names one commit, d56de90ea, touching only this work item's
`trail/gate.md`, and 6ef65ee06 is an ancestor of HEAD (executed).
`seal pr-body --check` on the body file exited 0, through the installed
`seal` and through the tree's `bin/seal` at d56de90ea (executed).

Every re-run below ran in a `git clone --no-local` of the branch at
d56de90ea under the sealer's scratch directory, with
`skills/verify/scripts/deferral_check.py` restored from the named commit and
the test module left at HEAD; the tree under audit was not changed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The new cases were red at the base and the existing cases passed there; #1123 *Done when*: both push-only spellings `too late`, seen red against c825fd2c | `trail/phases/phase-1.md:40`; issue #1123 *Done when* | `git diff --stat c825fd2c 10942072d -- skills/verify/scripts/deferral_check.py`; script restored from 10942072d, `bin/test tests/skills/test_deferral_check.py -q -p no:xdist -rf` | Holds. The diff is empty, so the base script is c825fd2c's. 39 failed, 17 passed, exit 1. `double-quoted-key` and `block-at-four-spaces` of the push-only case fail on exit 0 with `answers ... (trigger unread)`. The 17 passing are the 12 earlier cases and the five pull-request spellings the base already read (`flow-list-trailing-comma`, `name-on-the-line-below`, `name-with-a-comment-below`, `inline-name-with-a-comment-below`, `a-tab-after-the-on-colon`), which the later rounds claim red only at intermediate commits |
| `flow-list-trailing-comma` and `name-on-the-line-below` red at the phase 1 script | `trail/rounds/round-1.md:72` | script restored from 61e2e6be, `bin/test` over the two parameters | Holds: 2 failed, exit 1 |
| `a-name-continued-on-a-deeper-line` and `an-inline-name-continued-on-a-deeper-line` red at bef03a87's script | `trail/rounds/round-2.md:78`, `:136` | script restored from bef03a87, `bin/test` over the two parameters | Holds: 2 failed, exit 1 |
| `a-name-glued-to-a-colon` and `an-on-key-glued-to-its-value` red at 274317f3's script; `a-key-holding-a-glued-colon` answers under f23464df's script | `trail/rounds/round-3.md:108` | script restored from 274317f3, then from f23464df, `bin/test` over the named parameters | Holds: 2 failed and 1 failed, exit 1 each |
| `a-block-line-opened-by-a-unicode-space` and the U+00A0 parameters red at 13b15928's script; `an-on-key-ending-in-a-unicode-space` answers where `ON_KEY` keeps `\s*` before the colon | `trail/rounds/round-4.md:120`, `trail/rounds/round-5.md:75` | script restored from 13b159282, `bin/test` over `a-block-line-opened-by-a-unicode-space`, `an-on-key-ending-in-a-unicode-space`, `a-name-glued-to-a-colon-by-a-unicode-space` | Holds: 3 failed, exit 1; the first fails on `answers ... (on pull_request, push)` |
| The module passes at HEAD with 56 cases | `trail/rounds/round-6.md` *Probes* | script at d56de90ea, `bin/test tests/skills/test_deferral_check.py -q -p no:xdist` | Holds: 56 passed, exit 0 |
| `ruff check` and `ruff format --check` are clean over the two changed Python files | `trail/rounds/round-5.md:164`, `trail/rounds/round-6.md` *Probes* | `uvx ruff check` and `uvx ruff format --check` over `deferral_check.py` and `test_deferral_check.py` | Holds: exit 0 and exit 0 |
| Round 5's findings 4 and 5 are defects older than the work item, still open at HEAD, and posted on #1167 | `trail/rounds/round-5.md:185-188`, `:246-249`, `:221`, `:280` | `python3 -I <script> --kind tests <project>` with the base script and HEAD's, over `on:` / tab `pull_request:` and `# note` U+2028 `on: pull_request` / `on: push`; `gh issue view 1167` | Holds: all four runs print `answers ... (on pull_request)` at exit 0, so both shapes fail open at the base and at HEAD. #1167 is open and its comment names both shapes with this work item's round 5 record |
| Nothing of a `## Removes` row stands | `frame/design.md` *Removes* | `git grep -e 'indent <= 2' -e 'reported as unknown rather than as absent' -e 'three outcomes' -e '(trigger unread)' -e 'not events or' -- skills tests README.md README.ko.md`; read `inspect` and the module docstring at HEAD | Holds: no match; `inspect` sends an empty event set to `unread`, and the docstring says five and lists five |
| The run's round count stays inside the cap and its extension | `trail/rounds/round-4.md:5`; `docs/the-review-record.md` *The run* | `grep -c '^### [0-9]'` and `grep '^Extended past'`, `grep -E '^(regression\|reopens):'` over the six round records | Holds: 2, 2, 1, 1, 5, 0 findings. Round 4 is the one extension, written as round 3 found 1 against round 2's 2 with no regression. Round 5 reads round 4's rung 1 fix, and round 6 is the verifying round of round 5's three `regression: round-4#1` fixes |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `read_events` reads `on`, `"on"`, `'on'`, an event block at any consistent indent, a key with a value or comment, a closed flow list; anything else is unread as a whole; `inspect` prints `unread` and does not count it; `KNOWN_LIMITS` and four texts list the fifth outcome | issue #1123 *Done when*; the diff; `gaps.md`, which records the four places the build departed from *Scope* with grounds | none. Its *Scope* item 1 says a shallower line ends the block; the build makes it unread, and `gaps.md` records that with *Scope* item 2 as the ground (read) |
| the build | the diff and `trail/phases/phase-1.md`: the reader, the `unread` list, the limit clauses, the five-outcome texts, and cases red at the base | the design; the re-runs above; README.md and README.ko.md name the same outcome (read) | none |
| the last round | round 6: no finding; fixes of round 5's findings 1 to 3 hold; findings 4 and 5 are closed `deferred #1167` with their grounds | the re-runs above; #1167's comment; the base's `CLAUDE.md` *The rules steer judgment, and a few invariants hold the chain* (read at 10942072d) | none. Its *Not judged* row on the owner's sentence is answered by the orchestrator's part of the body, which names #1169 as the source |
| the changelog | `seal deferrals` no longer counts a trigger it cannot read; it reads the listed spellings; an unread trigger prints `unread <name> (trigger unread, not counted)`; the limit names filters | the diff and the cases. It claims no fix for the two deferred shapes, which still answer (executed) | none. The printed line pads the label to a ten-character column, which the changelog's quotation drops; the text is the same (read) |
| the orchestrator's part of the pull request body | the version move to 0.24.2 in bef03a87; the stop by judgment after round 5 and its grounds; the tab after a colon as an unmeasured reading; the broad run's counts; `Closes #1123` | the diff (`plugin.json` 0.24.1 to 0.24.2, read); the release branch's two earlier commits since 8d8d63903, #1168 and #1165, change `CLAUDE.md` and a test, and `plugin.json` stood at 0.24.1 at 10942072d (executed); the round counts 1, 1 and 5 (executed); #1167's comment (executed); #1169's diff holds the sentence "these differ" where the meaning is the same is the worst result (executed `gh pr diff 1169`) | none. `unverified`: that the sentence is the owner's; #1169 is an open pull request under the owner's account, not merged into `release/v0.24.2`, so the base's `CLAUDE.md` does not hold it; answerer: the owner. `unverified`: 6095 passed and 11 skipped, which `trail/gate.md` does not record; answerer: the orchestrator |

The stop after round 5 stands on the base's documents without the quoted
sentence. The base's `CLAUDE.md` *The rules steer judgment, and a few
invariants hold the chain* makes a rule guidance for a judgment, names
signals that a path is not converging, and keeps as invariants only no
review without a build, no fix that no round reads, no seal without the broad
run at HEAD, no pull request without a seal, and no question to a person
after routing (read). Round 6 read every fix, and the broad run is at HEAD,
so no invariant is broken. #1167, which that section names, lists
`seal deferrals` reading workflow triggers and the filing ladder among the
things it decides, and its direction is the owner's of 2026-10-29 (read).
Both deferred shapes predate the branch (executed), so no defect this branch
made leaves with a deferral.

Verdict: sealed
