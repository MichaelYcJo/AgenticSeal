# each budget ratchets and every pull request measures it — overview

<!-- The closing memo (implement skill, step 4). Opened at phase 1's first
divergence; later phases add to it as they go. -->

## Why this work exists

Nothing held the repository's size and speed, so each slowdown was found by a
person; after this work every pull request measures each budget and a raised
ceiling has to say why in the body.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| How the checker knows a pull request is a release | `spec.md` §*Data & interfaces* lists `--baseline`, `--pr-body-env`, `--ci-run`, `--trend`, `--json` and no flag for the base; the code takes `--base-ref <branch>` and treats `main` as a release | code (phase 1) | `spec.md` §*The budgets*: "A pull request into `main` is exempt from the body rule". The rule needs the branch, and a condition inside the script is one a case drives (T6), where a shell guard in `hygiene.yml` would be a second reading the broad gate's `steps_guarded_off_main` reader also counts |
| The hygiene workflow re-runs on a body edit | spec silent; `hygiene.yml` gains `edited` in `on.pull_request.types` | code (phase 1) | S3 is "the body carries the line → exit 0". Writing the line is an edit and no commit, and a re-run replays the original event's body, so without `edited` the line is read only at the next push |
| The broad gate's partition and its printed counts | `plan.md` names no change outside the checker, the workflow step, the test module and the record-layout row; the tree's `tests/test_the_gate_names_every_step_ci_runs.py::test_every_step_the_workflow_runs_is_classified` refuses an unclassified step | code (phase 1): a `PARTITION` row excluding the step with its reason; the feature and release counts pinned at 10/5 and 12/9; `skills/verify/SKILL.md`'s count sentence and its pin moved with them; the two released rows stating the old counts corrected in the ledger fragment | the partition test is the rule that a step reaches the gate's list, and the count sentences are pinned verbatim (`agent-contract` §14) |
| A `CONTRIBUTING.md` sentence the new step made false | `spec.md` §*Scope* names "CI runs five jobs" for phase 3; §*What a contribution is not asked for* said "The remaining two … are always-on and CAN refuse a contribution", and the budget step is a third | code (phase 1): the sentence rewritten in place, saying what the budget step asks of a contribution | `spec.md` §*Scope*: "The in-place rewrites of sentences the new checks make false" |
| A gate row that becomes a `report` | `spec.md` §*The budgets*: "a row that is gone, fails unless the pull request body carries … `Budget removed:`"; silent on a kind change | code (phase 1): a gate row no longer a gate needs the `Budget removed:` line too | a gate turned into a report lifts its ceiling as fully as a deleted row; reading it as unchanged would be the loophole the removal rule closes |
| The names in `plan.md`'s test-rows table | the frame wrote each case without its `test_` prefix, and `evidence-check`'s records arm refused all sixteen names at exit 2, the lenient reading CI's ledger job runs | record corrected (phase 1): the planted names as the tree carries them, T4 as its two cases, and the five later-phase names marked as not yet planted | the arm reads a backticked name as a token of the tree, and no pytest case can carry the bare name |
| The seconds rows against a refreshed `.test_durations` | `spec.md` §*The budgets*: `suite-seconds` and `slow-file:*` are seconds read off the committed file, held to the band. The orchestrator's decision of phase 2, from #931's refresh run 38475370013 (7,861.7 → 8,490.3 s, 553.9 s of it the same cases priced 1.071 higher): with `--baseline` and the file changed, divide HEAD's seconds by the seconds-weighted ratio over the shared case ids, compared in the base's prices | code (phase 2): the ratio is measured as decided, and the level it divides by is a row of `seal/budgets.md`, `## Price level`, that the refresh restates to the base's level times the ratio, per mille; the run fails naming the number where it does not | divided by the base's ratio alone, the refresh's own pull request holds, and the next pull request's base already holds the refreshed file: its ratio is 1, its seconds are in the new prices and its ceilings in the old, and `suite-seconds` fails by 7 % on every pull request after the refresh, the suite case's reading included. Executed by phase 2's probe on a scratch clone; `questions.md` Q6 |
| The rule block of the docs classifier | `spec.md` §*The docs classifier*: "from a line opening with `**` to the next `Enforced by:` line inclusive" | code (phase 2): to that line, or to the end of the block's paragraph where no such line closes it first | read literally, a bold lead with no `Enforced by:` after it makes the rest of the document rule lines: 118 history lines over `docs/` against the frame's 246. Bounded by the paragraph, 251 at 65a0ba5f, four files one off the frame's; `phases/phase-2.md` |
| What a per-file family row's ceiling means | `spec.md` §*Data & interfaces* names the two file tables and §*The budgets* "a file not listed that crosses 120 s fails (the list may not grow)" | code (phase 2): the family's own row in the Budgets table holds every file its table does not list — 120 s for `slow-file`, 0 lines for `docs-history` — and gives the listed files its unit, slack and kind; listing a file above that ceiling is a raise from it and needs its line | one rule for both families, and "the list may not grow" without a line becomes something the ratchet can read |
| The band on `ci-minutes:*` | `spec.md` §*The budgets*: every row is `measured ≤ ceiling ≤ measured × (1 + slack)`, `ci-minutes` at 60 % | code (phase 3): a row read off one run has the slack `one-sided`, a ceiling and no lower band, and only such a row may | the owner's approved default for #929 Q2: one run's minutes swing 1.08 to 1.21 times, and 3 of 5 quiet runs fell under the two-sided band on one leg |
| How the checker reads a run | `spec.md` §*Data & interfaces* lists `--ci-run <id>` | code (phase 3): `--ci-jobs FILE`, the job list the workflow step fetches with `gh api … --paginate --jq '.jobs[]'`; with it the checker holds the run's rows alone, and without it the tree's run shows them unread | the checker reads no network and needs no token, so a case drives it from a file; the step that fetches is the one place the token is used |
| `fetch-depth: 0` on the `budgets` job | spec silent; the job reads no history | code (phase 3): set, with a comment saying why | `tests/test_ci_gives_the_checks_what_they_need.py::test_every_job_that_runs_pytest_has_the_whole_history` picks a job by the word `pytest` in its text, and `needs: pytest` is that word. #931's branch picks by a line that invokes pytest instead; whichever lands second can drop the setting |
| What a byte is | `spec.md` §*The budgets*: "bytes of `agents/<a>.md` + each `skills/<s>/SKILL.md`", read by `payload_meter.py` | code (phase 4): `payload_meter.py` names the files, and each is counted with every CRLF read as one LF | run 38485697284's Windows group 2 measured the fixture at 1,008 bytes where every other leg read 1,000: a checkout that writes CRLF counted each line end twice. The LF count is the bytes git stores under this repository's `eol=lf`, the same on every platform |
| `rounds-bytes` over which work items | `spec.md`: "per open work item" | code (phase 4): every `seal/specs/<id>/rounds/` the tree holds, the largest the reading and each listed | a work item's records stay in the tree until `settle --retire-process` removes them after its release, so the tree is what the next reviewer inherits from; whether a released item still counts as open is not a fact the checker can read |
| What `--trend` compares | `spec.md`: "the trend against the last release tag" | code (phase 4): each budget's ceiling at the tag beside its ceiling and reading today | a two-sided ceiling follows its reading, so the tag's ceiling is the tag's reading within its slack, read off one blob with no checkout of the tag; a one-sided row's line is what the release reads to lower it |
| How `ledger-rereads` reads a row | spec silent | code (phase 4): a row is a line opening with `\| ` and its marker what follows | the fold writes that spelling, and `hooks/config.py#table_cells` declines one 0.21.1 row whose cells carry an even run of backslashes before a pipe, which read 26 `Corrected ·` where the file holds 27 |
| The seconds rows' band and the price level's ratio | the frame: `suite-seconds` at 5 % and `slow-file:*` at 10 %, two-sided; phase 2 built the level as the seconds-weighted ratio over the shared case ids | code (round 1, the orchestrator's decision on its finding 1): both one-sided like `ci-minutes`, each ceiling 1.3 times its reading rounded up, every test file whose reading × 1.3 reaches the 120 s threshold listed (20 files); the level is the median, over the test files of 10 s or more on the shared ids, of each file's ratio | executed in round 1: at #931's refresh (9ffc5f66) the checker as built failed 14 ways with the level restated, its 19 test files of 100 s or more spreading 0.76–1.14 of the level and its 72 of 10 s or more 0.46–1.54 (round 2's note 2, executed by the warden and again here); a cleanup halving one file of three read both untouched files 1.42 times slower under the weighted ratio. With these rows and that median, the same refresh asks for level 1073 (the weighted ratio was 1.071) and then holds, its tightest row at 0.892 of its ceiling, and the cleanup holds at level 1000 |

## Not verified

| Item | Who must answer |
|---|---|
| closed The hygiene step on the branch's pull request, green at the pushed tip | #938's checks green at its merged head; 8350c578 then removed the budget step |
| closed That an edit to the pull request body re-runs the `hygiene` job and the budget step reads the new body | 8350c578 removed the budget step that read the body |
| closed The full suite, the repository-wide lint and the typecheck at this branch's tip | #938, merged with lint and the suite green on the ubuntu, macOS and Windows legs; the repository configures no typecheck |
| closed `test_the_trees_budgets_hold` and the module on the Windows and macOS legs | #938's `macos-latest` and `windows-latest` shards ran green; 8350c578 then removed the module |
| closed That the price level holds against a real refresh: #931's refreshed `.test_durations` beside this branch's rows, the level restated to the number the step names, and every seconds row then holding | 8350c578 removed `seal/budgets.md` and its seconds rows |
| closed The `budgets` job on this branch's pull request: it runs after the pytest legs, reads the job list with its `actions: read` token, and its summary shows three legs against 15, 59 and 32 with the billable line | #938's `budgets` job ran green |
| closed The two fixes of phase 4 on CI: the GFM census green on ubuntu, macOS group 2 and Windows group 1, and the byte cases green on Windows group 2 | #938's three legs, every shard, ran green |
| closed `--trend` on CI: the hygiene step's `git describe --tags --abbrev=0` names the base's last tag in the runner's checkout | 8350c578 removed `budget_check.py` and its `--trend` |

## Not done

`--json`, which the frame listed, is not built and is no longer in
`spec.md` §*Data & interfaces*: no phase of `plan.md` named it and nothing
reads it. The families #923 and #929 frame — `bytes:`, `history:`, an
enforcer gate, `test-cases` and `test-lines` — are theirs to add: each is
one `MEASURERS` entry, or, where it is read per file, one `FILE_TABLES`
entry carrying the reader that measures it, its table found under its own
heading.

## Fed back into the spec

Inferred during implementation, phase 1 — a planner may overturn each:

- A `Budget raised:` or `Budget removed:` line may sit in a markdown list item
  and may put the name in backticks.
- An absolute slack is `+N`, optionally followed by the row's own unit word;
  `+N` in another unit is refused.
- A gate row that becomes a `report` row is a removal for the ratchet.
- The summary lists every raise and removal it read, and marks one the body
  does not declare, since the row's band verdict alone reads `holds`.

Inferred during implementation, phase 2:

- Seconds are rounded to the nearest whole one, a half up, after summing.
- A listed test file may sit under the threshold; its row holds it tighter.
- A file row whose family row is gone needs no line of its own.
- The price level: `## Price level`, its rule above, and that a refresh
  states it rather than raising every seconds ceiling.

Inferred during implementation, phases 3–4:

- A row read off one run is `one-sided`, and so may a `report` row be; no
  other row may.
- A byte is counted with each CRLF as one LF.
- A one-sided ceiling is lowered at the release, to 1.3 times the largest of
  the release's runs, from the trend line (`docs/release-checklist.md` §2).
- `ledger-rereads` reads the release file `.claude-plugin/plugin.json`'s
  version names, and is unread until that file exists.
