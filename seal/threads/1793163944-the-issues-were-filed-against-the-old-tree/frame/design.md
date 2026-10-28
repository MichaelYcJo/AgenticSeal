# Feature Specification: 1793163944-the-issues-were-filed-against-the-old-tree

## Grounding

Every coordinate below is the tree at `0b75346f`, the commit this branch was
cut from. `executed` marks a fact a command the framer ran printed; `read`
marks a fact the framer opened and read.

| Policy clause | What it fixes for this work |
|---|---|
| `docs/issues-and-milestones.md` *A milestone answers when, and takes three shapes* | A scheduled release milestone's description states the release's purpose and the grounds for the order its issues sit in, and grounds that belong to one ticket sit on that ticket. So each milestone description below states purpose, order and the reason for each step of the order, and a reason that belongs to one issue goes into that issue's body |
| `CLAUDE.md` *The rule a mechanism is kept against* | A change rewrites the text it amends in place and removes what stood on the old fact. So a folded body replaces the old name where it stands, and the line "Read the renamed tree first (#1052): paths above are the 0.22.4 ones" that #1055, #1056 and #1058 carry, and #1091's "Paths and names are as of 0.22.4", go in the same edit, because after the fold they are false |
| `CLAUDE.md` *Repo rule: text an agent or a check reads has one reading* | A folded body is what the next framer reads. It names a file by its path at `0b75346f`, a released record by `<commit>:<path>`, a section by its heading in italics, and never by the section sign |
| `.github/scripts/release_completeness_check.py`, module docstring (read) | A release pull request fails while its milestone holds an open issue the release does not carry. An issue filed into `release: 0.24.0` is therefore work 0.24.0 owes before it ships, and an issue moved out of it stops being owed there |
| Issue #1053 *The change* (read; a ticket, not policy) | The release note will open with the first phrase of its milestone's description, `Purpose:`. Both descriptions below keep `Purpose:` as their opening word |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | No tree file outside this work item's directory changes. Every edit this work makes is on GitHub |

How the read was taken (executed): every open issue of milestones 65
(`release: 0.24.0`) and 67 (`release: 0.24.1`) and closed issue #1044 was
fetched with `gh issue view <N> --json number,title,body,comments,state,milestone`;
the milestone descriptions with `gh api "repos/MichaelYcJo/AgenticSeal/milestones?state=all&per_page=100"`.
Each coordinate an issue names was then opened in the tree with `git grep`,
`grep -n`, `wc` or `sed -n`, and each released record path with
`git cat-file -e <commit>:<path>`.

## Scope

In:

- One verdict per open issue of `release: 0.24.0` and `release: 0.24.1`, and
  for #1044 (closed in `release: 0.23.1`, named by 0.24.1's description).
- The findings #1052's *What the read covers* asks for that no open issue
  holds: three new issues, and four findings folded into an existing issue
  where one already owns the subject.
- The resulting order of both milestones, with which issues of each group can
  run in parallel.
- The GitHub edits that apply all of it, built by the crafter (`plan.md`).

Out:

- Building any of it (#1052 *Out of scope*). No file of the tree changes
  outside `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/`.
- Issues outside the two milestones, including the backlog issues #1049 lists
  (#20, #24, #630, #723, #886, #893, #900): #1049's own work closes or carries them.
- Milestones `release: 0.25.0` and `release: 0.26.0`. Their descriptions name
  only #1038 and #1054, which no verdict here moves.
- The issues' titles. A title is the issue's identity in every commit subject
  and changelog line that cites it, and the read found no title naming a file
  that no longer exists in a way the body cannot correct. #1040's title names
  the old agents and is the one exception argued below.

## Verdicts

### The name mapping every fold applies

Each fold below applies these, where the issue's body uses the old form. A
fold changes nothing else in a body unless its own row says so.

| Old, as the bodies write it | At `0b75346f` |
|---|---|
| the smith, `agents/smith.md` | the crafter, `agents/crafter.md` |
| the warden, `agents/warden.md` | the proofer, `agents/proofer.md` |
| the scribe, `agents/scribe.md` | the tracer, `agents/tracer.md` |
| a live work item's `seal/specs/<id>/` | `seal/threads/<id>/` |
| `spec.md`, `plan.md`, `questions.md` of a work item | `frame/design.md`, `frame/plan.md`, `frame/questions.md` |
| `overview.md` | `gaps.md` |
| `phases/phase-N.md`, `rounds/round-N.md` | `trail/phases/phase-N.md`, `trail/rounds/round-N.md` |
| `broad-gate`, `broad-gate.md` | `seal gate`, `trail/gate.md` |
| `session-cost`, `mutation-check`, `rules --check` | `seal cost`, `seal mutate`, `seal rules --check` |
| `templates/sdd-spec.md`, `templates/sdd-overview.md`, other `templates/sdd-*.md` | `templates/records/sdd-design.md`, `templates/records/sdd-gaps.md`, `templates/records/sdd-*.md` |
| `templates/pact.md`, `templates/hygiene.yml`, `templates/claude-md-block.md`, `templates/config.md` | the same names under `templates/setup/` |
| `hooks/config.py`, `hooks/routing.py`, `hooks/cmdline.py`, `hooks/cmdline_base.py`, `hooks/tokens.py` | the same names under `hooks/lib/` |
| `tests/test_<name>.py` | the path named in the issue's own row below |
| `specseal-eval` | `agentic-eval` |
| `~/.claude/specseal/` | `~/.claude/agentic/` |
| `§Heading` | `*Heading*` |

A released work item's record was removed by a settle, so a fold cites it at
the commit before that settle (executed, `git cat-file -e` on each path below):

| Released records under | Readable at |
|---|---|
| work items the 0.22.4 settle `de11df75` removed (#955, #985, #1005, #1017, #1033, #1005's `1792627930-the-section-sign-is-still-syntax`, `1792540458-on-demand-files-state-the-current-rule`, `1792251842-the-smith-is-written-anew-from-its-job`, `1792368015-every-finding-carries-an-evidence-line`) | `0ed5dd3b:seal/specs/<id>/<file>` |
| `1792367880-ci-runs-once-when-the-pull-request-opens`, removed by #1024's settle `4d5a6917` | `67694cba:seal/specs/<id>/<file>` |
| `1790835050-the-delegated-note-compares-what-it-prints`, removed by `6224f1d8` | `5180b89e:seal/specs/<id>/<file>` |
| `1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by`, removed by the 0.23.0 settle `4a8104db` | `4420ebd5:seal/threads/<id>/<file>` |

A path already written as `<commit>:<path>`, such as #1020's `6fb3b2fd:` and
#1048's `fa7d1374:`, stays as it is.

### Verdict counts

| Kind | Issues |
|---|---|
| Stands as written | #1053, #1096, #1102 (3) |
| Stands with its body folded | 0.24.0: #712, #913, #920, #951, #956, #992, #1020, #1039, #1040, #1041, #1042, #1043, #1055, #1056, #1058 (15). 0.24.1: #947, #1045, #1046, #1047, #1048, #1049, #1091 (7) |
| Already done by the rename or the reorganisation, or by a later merge | #1044, done by #1103 (`5e5275e5`) and already closed (1) |
| No longer stands | none |
| This work item | #1052 |

No open issue is closed. Two issues were partly done since they were filed,
and each keeps only what is left: #1043's first citation and #1055's items 1
and 2 (rows below).

### release: 0.24.0

**#1058, stands, folded.**
- `tests/test_chain_check.py` becomes `tests/skills/test_chain_check.py`, and
  the per-case clearing lines are now `:249`, `:2326`, `:2785`, `:2875`,
  `:2891` and `:2906` (executed, `git grep -n GITHUB_HEAD_REF -- tests`).
  `tests/skills/test_broad_gate.py:77` clears `GITHUB_HEAD_REF` and
  `GITHUB_EVENT_PATH` through its own `AMBIENT` tuple, and is named beside them.
- `tests/conftest.py` still has no fixture for the `GITHUB_*` variables. Its
  two autouse fixtures clear the transcript root and `SESSION_VARIABLES`
  (`:514`, `:536`, read), and the new fixture sits beside the second.
- The second bullet of *The change* names its coordinate:
  `skills/code-review/orchestration.md` *Orchestrator: the pull request opens
  once the sealer seals*, the paragraph opening "Where the work's risk is
  platform-specific", which still runs `gh workflow run tests --ref <branch>`,
  a `workflow_dispatch` run. Since #943 the pull request opens after the
  sealer, and the same section's stated limit covers a defect only one
  platform shows. The body says the limit covers platforms and not the
  environment a `pull_request` event sets, which is this issue's case.
- The closing line "Read the renamed tree first (#1052): paths above are the
  0.22.4 ones." goes.

**#913, stands, folded.**
- `~/.claude/specseal/pact-paths.md` becomes `~/.claude/agentic/pact-paths.md`
  (`skills/verify/scripts/pact_check.py:28`, `:89`, read). `path_map` is
  `pact_check.py:249`, and its loop still reads `config.CONFIG_SEPARATOR` at
  `:269`.
- `hooks/config.py#CONFIG_SEPARATOR` and `CELL` become `hooks/lib/config.py`
  (`:102`, `:98`).
- Part 2: "the pact anchors `pact_check.py` and `chain_check.py` read" becomes
  "`pact_check.py` and `skills/verify/scripts/coordinates.py` read".
  `skills/code-review/scripts/chain_check.py` holds no pact reading
  (executed, `grep -c -i pact` answers 0).
- `templates/sdd-spec.md`'s `## Removes` hint becomes
  `templates/records/sdd-design.md`'s, and `templates/pact.md` becomes
  `templates/setup/pact.md`.
- `seal/specs/1792540458-on-demand-files-state-the-current-rule/spec.md` becomes
  `0ed5dd3b:seal/specs/1792540458-on-demand-files-state-the-current-rule/spec.md`.
- "§*The class*" style citations and "agent contract §12" become
  "contract rule 12". The 0.22.4 move comment stays as history.

**#920, stands, folded, and stays in `release: 0.24.0` among the small fixes.**
- `steer_to_switch` is `hooks/worktree-guard.py:1382`, and its two hints still
  name `[worktree-ok]` (`:1389`, `:1394`, read).
- "agent contract §12" becomes "contract rule 12", and "#903's frame kept
  unchanged (§*The class*)" becomes "(*The class*)".
- It stays where the owner placed it: `questions.md` Q1 was answered (b) on
  2026-10-28, so the hint is fixed in 0.24.0, before #1049 decides whether
  the worktree guard stays, narrows or goes, at the cost of one chain run that
  decision may later remove.

**#712, stands, folded.**
- `session-cost --spawns` becomes `seal cost --spawns`.
- The coordinates: `cycle_label` is `skills/verify/scripts/session_cost.py:2225`
  and never cuts; `report_spawns` pads with four literal `:<30` at `:2318`,
  `:2328`, `:2333` and `:2419`. The per-segment table already has
  `LABEL_WIDTH = 30` at `:2425`, which `segment_label` cuts to (read), so the
  fix can share that name. The helper is
  `tests/skills/test_session_cost.py#delegated_cells` (`:548`).
- The paste-ready fix becomes
  `5180b89e:seal/specs/1790835050-the-delegated-note-compares-what-it-prints/rounds/round-1-report.md`
  *Paste-ready fixes* (the heading is at its line 219, executed).

**#1039, stands, folded.** The settle it waited for has happened and did not
take the three cases.
- The 0.22.4 settle `de11df75` removed `docs/the-commit-gate-inside-git.md`
  (executed, `git log --diff-filter=D`). The three cases and their markers
  `no-verify-met-where-the-branch-moves` and `gits-own-commits-not-judged`
  still stand at `tests/behaviour/test_the_hook_surface_git_offers.py:176`,
  `:273`/`:274` and `:317`/`:318`, and no document names either marker
  (executed, `git grep` outside the records).
- The module path becomes `tests/behaviour/test_the_hook_surface_git_offers.py`.
  The `check:` lines naming it are `docs/worktree-guard-spec.md:360` and `:587`.
- `.test_durations` now prices the three at 3.01 s, 7.10 s and 6.19 s, 16.3 s
  together, and the module at 27.0 s across 10 cases, of 1,252.4 s summed over
  6,788 entries (executed, summed from `.test_durations` at `0b75346f`).
- *Done when*'s first bullet becomes: this issue's pull request deletes the
  three cases and their three `.test_durations` entries. No settle is waited
  for. The third bullet's `rules --check` becomes `seal rules --check`, and
  "both `check:` lines" stays.
- "#1027's `spec.md` (line 720)" becomes
  `0ed5dd3b:seal/specs/1792935671-the-routing-check-moves-to-the-sessions-tools/spec.md`,
  and "`phases/phase-7.md` of #1027" the same commit's `phases/phase-7.md`
  (both executed with `git cat-file -e`).

**#1040, stands, folded, and retitled.** The title names "the smith, warden,
sealer, framer and scribe definitions". A title that names three agents that
no longer exist is the first line a framer reads, so it becomes "the crafter,
proofer, sealer, framer and tracer definitions" with the rest of the title
unchanged. This is the one title this work changes.
- Rule 2's six sentences now stand at `agents/crafter.md:65` and `:138-140`,
  `agents/proofer.md:61` and `:138-139`, `agents/sealer.md:109-110` and
  `:124-126` (read). In the proofer's, "by `broad-gate`, after the rounds
  settle, and `broad-gate.md` holds that run" now reads "by `seal gate`, …
  and `trail/gate.md` holds that run".
- Rule 6's bullets: `agents/crafter.md:69`, `agents/proofer.md:59`,
  `agents/framer.md:106`, `agents/tracer.md:46`. Rule 9: `agents/crafter.md:70`.
  Rule 7: `agents/tracer.md:34`.
- The tests that read the restated wording:
  `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:883` and
  `:886` read `agents/crafter.md`'s "You do not run the full suite, the lint or
  the typecheck" and "rule 2 holds who does" (executed, `git grep`), and
  `tests/text/test_broad_gate_rule.py` reads the crafter (the body's `:144`
  is dropped; the work finds the line). The paste check becomes
  `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, whose
  `BASELINE` holds the agent pairs (`:189` onward).
- `agents/sealer.md`'s `check:` line is `:128` and still names
  `evals/behaviour/sealer/rule-sealer-no-gate/` and `rule-sealer-stale-gate/`.
- The narrowing that stays: `agents/proofer.md:138-147` (a spawn prompt that
  orders one of the three is a `## Not judged` row), `agents/crafter.md:140`
  onward (reading `failing on base too` and `new?`), `agents/sealer.md:124-126`
  (the pointer to step 1), `agents/proofer.md:59` ("Fix the code under
  review"), `agents/crafter.md:66` ("Name any party as the runner of the broad
  gate").

**#1041, stands, folded.**
- The writer sentences: `agents/crafter.md:20` and `:153-154`,
  `docs/the-review-record.md:135-136`, `skills/code-review/orchestration.md:54`
  ("The crafter's fix pass changes two lines per open finding"),
  `skills/implement/SKILL.md:484` (read).
- The *Job* row it cites is `skills/code-review/orchestration.md:100`, in
  *Orchestrator: the run ends with a verifying round*.
- "`docs/the-review-record.md` (through a `## Rule changes` item)" stays.
- The 0.22.4 commits in its table stay as history. The 0.23.x pull requests
  were squashed, so their answer commits cannot be told apart on `main`
  (read: each squash commit carries `+verdict:` and `+answer:` lines in equal
  number), and the body says so in one sentence.

**#1043, stands, folded.** Half of it is done.
- Done: `docs/the-review-record.md:670` now cites `skills/verify/orchestration.md`
  *Measure the segment, and feed the flow log*, corrected by the 0.22.4 settle
  `de11df75` (executed, `git log -S`). The *Done when* bullet asking for a
  `change` of that document goes, and the body says which commit did it.
- Left: `.github/scripts/gather_changelog.py:43-44` still names
  "`docs/the-record-layout.md`'s *A marker counts only on a live line*". That
  document's rule opens *Whether a line is live is asked by what the line
  does* at `:140` (read). The phrase is a bold lead inside the script itself
  (`:38`), not in the document. #1053 later removes the gather step; this fix
  is one line and lands first.
- Left: the resolver case. The implement-only case becomes
  `tests/behaviour/test_the_set_a_work_item_always_has.py#test_every_cited_heading_of_implement_exists`
  (`:487`, `SKILL_NAMED` at `:443`). The contract citation check becomes
  `tests/text/test_the_agent_contract_holds_the_universal_rules.py`; the
  orchestration pin becomes `tests/text/test_broad_gate_rule.py`.
- `seal/specs/` and `changelog/` in "outside `seal/specs/`, `changelog/` and
  `CHANGELOG.md`" become `seal/threads/`, `seal/process/`, `changelog/` and
  `CHANGELOG.md`.
- One sentence: #956's paragraph *The citation reader* is the audit of the
  reader this issue builds, so #956 reads this case after it lands.

**#1042, stands, folded.**
- `.git/specseal-eval/` becomes `.git/agentic-eval/` in all five sealer
  prompts (read), and `tempfile.mkdtemp(prefix="specseal-eval-")` becomes
  `prefix="agentic-eval-"` at `evals/scripts/noninferiority.py:611`.
- The author lines are `evals/scripts/rule_cases.py:205`, `:280`, `:288`,
  `:370` and `:636` (`BY`), and `evals/scripts/seed_defects.py:313`. 18
  scaffolds still commit as `user.name=eval` (executed, `grep -l | wc -l`).
- "The four `replay-*` warden scaffolds" becomes "proofer". The
  `noninferiority.py:185-197`, `:601-640` coordinates are dropped for the
  function names `#run_side` and `#side_path`, because the lines moved.

**#992, stands, folded.**
- The records it cites become
  `67694cba:seal/specs/1792367880-ci-runs-once-when-the-pull-request-opens/evals/sealer-phase-3b.md`,
  `0ed5dd3b:seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md`
  and `0ed5dd3b:seal/specs/1792368015-every-finding-carries-an-evidence-line/evals/warden-phase-3.md`
  (each executed with `git cat-file -e`).
- "#985's warden side" becomes "#985's proofer side, recorded as the warden's".
- `#verdict` is `evals/scripts/noninferiority.py:762`, and rule 5 is still
  tokens per tool call (read, its docstring).

**#956, stands, folded.**
- `hooks/routing.py` becomes `hooks/lib/routing.py`; the config table reader
  is `hooks/lib/config.py`. `chain_check.py#verdicts_of` is
  `skills/code-review/scripts/chain_check.py:1864`.
- `seal/specs/1792627930-the-section-sign-is-still-syntax/` becomes
  `0ed5dd3b:seal/specs/1792627930-the-section-sign-is-still-syntax/`.
- "It is part of the check release that closes 0.22.x. The fixes it names go
  to the patch release after it where their size allows, and to 0.23.0
  otherwise (owner, 2026-10-16)." becomes: it is part of 0.24.0; each fix it
  names is filed, into 0.24.1 where one work item carries it, and otherwise
  left to #1038, which `release: 0.25.0`'s description already says reads
  "#956's larger fixes".
- *The citation reader* gains one sentence: #1043 builds the resolver case
  across the tree, and this audit records how that case fails on what it
  cannot read once it lands.

**#1055, stands, folded.** Items 1 and 2 are partly done.
- Item 1: `README.ko.md` now carries the `implementer-mark` and
  `implementer-notice` rows (`:168-169`), and neither edition names the commit
  gate or the review-history reminder (executed, `grep`). The count now reads
  "Nine of the thirteen gates" (`README.md:417`). `hooks/dispatch.py` registers
  15 scripts in its groups (`:81-105`, read), the 13 the README counts plus
  `worktree_consent.py` and `root-migrate.py`, and no check reads the count.
  Item 1 keeps that, as a count in prose with no check, and drops the rest.
- Item 2: `docs/one-root-by-lifetime.md` now says `seal mode` leaves `.github/`
  alone and `seal pr-checks install` writes the workflow (`:96-102`, `:146-147`,
  read). The drift is corrected. What stays is the point-of-no-return warning,
  now at `README.md:529`, `README.ko.md:522` and `skills/config/SKILL.md:168`
  (executed, `git grep "reset -- :/seal"`).
- Item 3: `templates/hygiene.yml` becomes `templates/setup/hygiene.yml`, which
  still has no `permissions:` or `concurrency:` (`.github/workflows/hygiene.yml:20`,
  `:30` has both, executed). The case becomes
  `tests/text/test_ci_gives_the_checks_what_they_need.py`.
- Item 4: the lines are `README.md:25`, `:45`, `README.ko.md:26`, `:45`;
  "Two hooks reach the network" is `README.md:223`, `CONTRIBUTING.md:439` and
  `README.ko.md:216`; `templates/claude-md-block.md` becomes
  `templates/setup/claude-md-block.md`; `tests/test_chain_hooks_hardening.py`
  becomes `tests/behaviour/test_chain_hooks_hardening.py`.
- Item 5: the case becomes `tests/behaviour/test_both_editions_carry_the_same_folds.py`,
  whose `pairs()` (`:60`) still reads top-level `docs/` only.
- Item 6: `docs/the-agent-set.md` and `skills/implement/SKILL.md` share 20
  runs in `tests/text/test_no_passage_is_pasted_into_a_second_file.py`'s
  `BASELINE`, and the item gains the larger pair the same table holds:
  `README.md` and `skills/config/SKILL.md`, 22 runs (read, `BASELINE`).
- The closing line "Read the renamed tree first (#1052): paths and names
  above are the 0.22.4 ones." goes.

**#1056, stands, folded.**
- `skills/verify/scripts/pytest_record/specseal_pytest_record.py` becomes
  `skills/verify/scripts/pytest_record/agentic_pytest_record.py`; it still
  writes `invocation_dir` (`:294`) and `wasxfail` (`:310`).
- `seal.py#import_`'s clause is `skills/implement/scripts/seal.py:1162`.
- `hooks/worktree_consent.py#main`'s `if not session` return is `:603`.
- `LABEL_DESCRIPTION_LIMIT` is `.github/scripts/label_merged_on_release_branch.py:113`,
  and only `tests/github/test_label_merged_on_release_branch.py:383` reads it
  (executed, `grep`).
- The closing memo becomes
  `0ed5dd3b:seal/specs/1793057294-close-the-mutation-gaps-the-old-tests-had/overview.md`.
- "`git grep` outside `seal/specs/` and the released records" becomes
  "outside `seal/threads/`, `seal/process/`, `changelog/` and `CHANGELOG.md`".
- The closing line "Read the renamed tree first (#1052)…" goes.
- One sentence: #1049 may remove `hooks/worktree_consent.py`; this issue runs
  first and its k3 item stands until then.

**#1020, stands, folded.**
- The warden becomes the proofer and the smith the crafter. The historical
  coordinates `agents/warden.md:99` in its tables stay, marked as #942's
  records at `6fb3b2fd`.
- "the framer is asked the structure question once … a line in `plan.md`
  *Alternatives*" becomes `frame/plan.md` *Alternatives considered*.
- `rounds/round-N.md` becomes `trail/rounds/round-N.md`. "`chain_check.py`
  already runs inside the broad gate" stays: `seal gate` runs
  `chain_check.py --baseline <base> --sealing`
  (`skills/verify/scripts/broad_gate.py:29`, read).

**#951, stands, folded.**
- "## Order: After #923 and #942" becomes "Both have shipped" (executed: #923
  and #942 are closed).
- "A case whose only job a type check now does is a candidate for #942's cut"
  becomes "is a candidate for removal, measured the same way".
- "the first candidate is the hot path alone (the commit gate's hook)"
  becomes "the hot path alone, the `pre-bash` group of `hooks/dispatch.py`":
  #1027 removed the commit gate.
- One sentence names today's broad gate from `seal/config.md`'s `Broad gate`
  row: `uvx ruff check . && uvx ruff format --check . && bin/test -q`, with
  no type check (read).

**#1053, #1096, #1102, stand as written.** Each was filed after 0.23.0 or names
only paths that stand at `0b75346f` (read: `skills/update/SKILL.md`,
`.github/scripts/gather_changelog.py`, `publish_release_note.py`,
`.github/workflows/publish-release.yml`, `hooks/lint-python.py:93`,
`hooks/worktree-guard.py:236-237`, `templates/setup/config.md`,
`assets/seals/owl.svg` all exist). #1053's "55 files, about 788 KB on
2026-10-27" is dated; the directory holds 58 files at `0b75346f` (executed),
and a dated figure is history, so the body is not edited.

### release: 0.24.1

**#947, stands, folded.**
- The preload table's agents become framer, crafter, proofer, sealer and
  tracer, with "(measured as the framer, smith, warden, sealer and scribe at
  `a8d83663`)" beside the *Before* heading, so the old figures keep their
  meaning.
- One row is added under *After* as a reading already taken: preload per spawn
  at `0b75346f`, the agent definition plus the contract it injects, framer
  22,513 B, crafter 21,461, proofer 21,898, sealer 21,386, tracer 15,236;
  `CLAUDE.md` 3,425 (executed, `wc -c`; each definition's `skills:` lists only
  `agent-contract`).
- `session_cost.py --segments` becomes `seal cost --segments`; "§The run"
  becomes *The run*.
- *What it decides* gains #1044's last *Done when* bullet, which no open issue
  holds: the three work items through the chain after #1103 are counted for
  withholds over the pull request body, from each thread's `guarantee.md`
  history, and the count goes on #1044 as a comment.

**#1045, stands, folded.**
- `seal/specs/<item>/` becomes `seal/threads/<item>/` throughout, and "the work
  item's own records" lists `frame/`, `trail/`, `gaps.md`, `changelog.md`,
  `guarantee.md` and `routing.md`.
- `overview.md` becomes `gaps.md`; `templates/sdd-overview.md` becomes
  `templates/records/sdd-gaps.md`, whose section is still *Where spec and
  implementation diverged* (`:11`, read).
- The warden becomes the proofer; `agents/smith.md` becomes `agents/crafter.md`;
  `phases/phase-N.md` becomes `trail/phases/phase-N.md`.
- The settle table is `skills/settle/SKILL.md:189-193`, still three kinds
  (read).

**#1046, stands, folded.** The read adds a fact that changes the cheapest fix.
- The sections are now `skills/implement/orchestration.md:88-279`
  (*Orchestrator: Bootstrap*, 1,847 words) and `:280-300` (*Orchestrator:
  Parity setup*, 146 words), of 7,649 (executed, `wc -w` over each range).
- The readers become `templates/setup/claude-md-block.md:16`,
  `hooks/mode-gate.py:16` and `:51`, and
  `tests/behaviour/test_first_setup_asks_once.py:60`, `:175`, `:243`.
- Added: the two sections are rows of the acts table in
  `skills/implement/orchestration.md` *Orchestrator: which of these acts runs
  itself* (`:657-658`), which
  `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py` holds
  against the `Orchestrator:` headings of `skills/implement/orchestration.md`
  and `skills/code-review/orchestration.md` only (the section's own opening,
  `skills/implement/orchestration.md:607-611`, read). A section
  moved to a third file leaves that check's row set, and the work says what
  replaces the two rows.
- Added: *Orchestrator: Parity setup* restates `skills/parity-setup/SKILL.md`
  steps 2, 3, 5 and 6, the same four fields and the same never-guess rule
  (read, both). `/agentic:parity-setup` is the one source, so the section can
  become one sentence naming that command instead of moving.

**#1047, stands, folded.**
- `spec.md` becomes `frame/design.md` throughout; *Grounding* stays.
- `agents/framer.md:77-79` becomes `:83-85`, and `:22-24` becomes `:23-25`
  (read). The definition still provides for no probe (executed, `grep -n -i
  probe` matches nothing).
- The records become `0ed5dd3b:seal/specs/1793051803-settle-runs-in-local-mode/spec.md:21`
  and `0ed5dd3b:seal/specs/1792993972-settle-writes-each-sections-latest-decision/questions.md:96`
  (each executed with `git cat-file -e`).

**#1048, stands, folded.**
- The smith becomes the crafter. Step 3 is now `agents/sealer.md:78-81`
  (read). `session_cost.py` becomes `skills/verify/scripts/session_cost.py`,
  whose transcript lines `:17-18` and `:41-42` stand.
- `skills/verify/SKILL.md`'s labels are *4. Each claim labelled executed, read
  or unverified*.

**#1049, stands, folded.**
- The cost table is re-measured at `0b75346f` (executed, `wc -l`, `wc -w`,
  and sums from `.test_durations`): `hooks/worktree-guard.py` 3,624 lines;
  `hooks/lib/cmdline_base.py` 2,288; `hooks/worktree_consent.py` 632;
  `hooks/lib/cmdline.py` 1,382; `docs/worktree-guard-spec.md` 713 lines,
  7,511 words; `tests/hooks/test_worktree_guard.py` 5,546 lines, 354 cases,
  75.1 s; `tests/hooks/test_worktree_consent.py` 840 lines, 54 cases, 18.6 s;
  `tests/hooks/test_cmdline.py`, `tests/text/test_guard_resolves_the_tree_it_judges.py`,
  `tests/behaviour/test_the_guard_asks_once_per_session.py` and
  `tests/behaviour/test_the_frozen_reading_never_grows.py` 883 lines, 91
  cases, 1.5 s; the seven guard cases of
  `tests/behaviour/test_the_hook_surface_git_offers.py` 10.7 s. Together about
  106 s of 1,252 s, about 8.5%.
- The importers become: `hooks/question-gate.py` and
  `hooks/routing-edit-gate.py` import `worktree_consent`;
  `hooks/lib/cmdline.py` is imported by `hooks/lib/tokens.py`,
  `hooks/lib/one_heredoc.py`, `hooks/worktree-guard.py` and
  `hooks/worktree_consent.py` (executed, `git grep -l`). The body's
  `implementer-notice.py` is replaced by that list.
- One sentence: #1096 changes `hooks/worktree-guard.py`'s language reading in
  0.24.0, before this decision.

**#1091, stands, folded.**
- "Paths and names are as of 0.22.4. 0.23.0 renames the smith to the crafter,
  and 0.23.1 may move the files." goes.
- `agents/smith.md` *Job*, steps 5 and 6 becomes `agents/crafter.md` *Order of
  work*, steps 5 and 6 (`:40-42`, read). `mutation-check` becomes `seal mutate`.
- The verify table is `skills/verify/SKILL.md` *The narrow command still has to
  be able to fail* (`:329-334`, read).
- #1051's phase record,
  `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/trail/phases/phase-1.md`,
  was removed by the 0.23.0 settle `4a8104db`, and becomes
  `4420ebd5:seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/trail/phases/phase-1.md`
  (executed, `git cat-file -e`). The released-records table above gains that
  row.

**#1044, done.** Closed in `release: 0.23.1`. #1103 (`5e5275e5`) built its
change: `seal pr-body` writes the body from the records, and the sealer runs
`seal pr-body --check` (`seal/process/0.23.1.md`, row 2, read). Its last
*Done when* bullet, the count over the next three work items, could not be
met at close, because no work item had run under the change yet. It goes into
#947 (above). #1044 gets one comment saying where the count now lives, and
0.24.1's description stops naming it.

## Findings no open issue holds

### Filed as new issues

**F1, into `release: 0.24.0`, fixed directly before the small fixes.** Title: "fix: the rename
turned describe into detracer at six places; the agent rename substituted
inside words, and the old-name census reads only the old names".
Evidence (executed, `git grep -n -o -i -E "[a-z]+tracer[a-z]*"` at `0b75346f`;
`git log -S detracer` names `ab14194b`, #1092):
- `skills/implement/orchestration.md:660`, the *Question 1* row of the acts
  table;
- `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:192` and
  `:205`, comments;
- the same file's `:203`, the case name
  `test_the_docstrings_detracer_the_letter_and_the_rows_it_carries`, and its
  key at `.test_durations:1154`;
- `tests/behaviour/test_waiver_decided_at_start.py:696`, a docstring.

The same search for `crafter`, `proofer` and `design` inside a longer word
found nothing but `\ncrafter` in a test string and `redesign`.
`tests/censuses.py#old_names` refuses the old names (`:984-1030`, read), so a
new name substituted into another word passes it. Done when: each site reads
`describe` or `describes`, the case and its `.test_durations` key are renamed,
and the issue's frame says whether one census case is worth adding, given that
the search above found no other instance.

**F2, into `release: 0.24.0`, after #1040 and #1041.** Title: "chore: 0.23.0
stopped calling the frame's design a spec, and the living text still does;
the closing memo's template is still titled Overview". Evidence:
- `seal/process/0.23.0.md` row 2: "the frame's design is no longer called a
  spec" (read). `tests/censuses.py#OLD_NAME` refuses `spec.md` and
  `overview.md` as names and leaves the word (read).
- Lines holding the word `spec` or `specs`, case folded, outside
  `docs/worktree-guard-spec.md`'s name and the Korean editions: `agents/` 11,
  `skills/` 201, `docs/` 17, `templates/` 14, `hooks/` 42, `CLAUDE.md` 1,
  `CONTRIBUTING.md` 2, `README.md` 12 (executed, `git grep -i -w -E 'specs?'`;
  the `hooks/` figure includes Python variables named `spec`, so each figure is
  an upper bound).
- Examples (read): `templates/records/sdd-design.md:1` "# Feature
  Specification"; `templates/records/sdd-gaps.md:1` "# Overview: <work item>",
  with *Where spec and implementation diverged* (`:11`) and *Fed back into the
  spec* (`:27`); `agents/framer.md:55` and `:150`; `agents/tracer.md:31`,
  `:59`; `agents/sealer.md:84`; `skills/settle/SKILL.md:17-20`;
  `docs/the-record-layout.md:98-107`; `skills/implement/SKILL.md`
  *1. Read the spec before the code*.
- A second meaning stands beside it: `docs/worktree-guard-spec.md` is a policy
  document. `CLAUDE.md` *Repo rule: text an agent or a check reads has one
  reading*: a defined term keeps its one meaning.

What its work decides: which word names `frame/design.md`, which occurrences
are a checker's vocabulary (`templates/setup/config.md` *What no row governs*)
and move only with their checker, and the `docs/` occurrences through
`## Rule changes`. The divergence section of `sdd-gaps.md` is #1045's to
remove, so F2 leaves its words to #1045.

**F3, into `release: 0.24.0`, after #956.** Title: "chore: most
contract rules are proved by a phrase of their own wording, so rewording a rule
turns a case red while nothing reads the behaviour; each phrase pin is kept as
a fact or removed". Evidence:
- #1052 names it as measured by the audit of 2026-10-27 and filed by nobody
  (read).
- 16 of the 20 `check:` lines of `skills/agent-contract/SKILL.md` name
  `tests/text/test_the_agent_contract_holds_the_universal_rules.py`
  (executed, `grep -c`). Its `PINS` holds one phrase per rule
  (`:40-65`, read), `test_each_section_holds_its_rule` fails when a rule's body
  loses its phrase, and `test_deleting_a_pinned_phrase_is_caught` pins the pin.
  Each proves the words stand, and none reads what an agent does.
- The same shape elsewhere:
  `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:883-886` and
  `tests/text/test_broad_gate_rule.py:55` pin agent and skill sentences
  (executed, `git grep`).
- A rough count of asserts shaped `assert "<25 or more characters>" in`:
  `tests/text` 193, `tests/behaviour` 340, `tests/skills` 270,
  `tests/github` 67, `tests/hooks` 36, `tests/evals` 15 (executed). It also
  counts asserts on a script's printed output, which are not prose pins, so it
  bounds the class from above and does not size it.
- `CLAUDE.md` *The rule a mechanism is kept against*: "A check gates only a
  fact it reads; a noisy reading, or one guessed from words, is a report", and
  "A rule's proof is the test or behaviour eval its `check:` line names".

What changes: each phrase pin on a rule sentence is kept where the phrase is a
fact a reader needs fixed (a citation's spelling, a heading a reader resolves,
a word a checker matches), and otherwise removed, with the rule's `check:` line
naming what reads the behaviour, or `check: none reader: <who>`. It starts with
the contract module and records the count for the other `tests/text`
modules. #956 asks which way a reader fails on input it cannot read; F3 asks
whether a pin reads a fact at all. #1040 removes sentences two of these pins read.

### Folded into an existing issue

| Finding | Evidence | Goes to |
|---|---|---|
| #1044's count of withholds over the body, after #1103 | #1044 *Done when*, third bullet; closed before any work item ran under the change | #947, 0.24.1 |
| *Orchestrator: Parity setup* restates `/agentic:parity-setup` | `skills/implement/orchestration.md:280-300` and `skills/parity-setup/SKILL.md` steps 2, 3, 5, 6 (read) | #1046, 0.24.1 |
| `README.md` and `skills/config/SKILL.md` share 22 runs of 15 words | `tests/text/test_no_passage_is_pasted_into_a_second_file.py` `BASELINE` (read) | #1055 item 6, 0.24.0 |
| #956's citation reader and #1043's resolver case are one reader | both bodies (read) | a sentence in each, 0.24.0 |

### What the read covered and found nothing to file

- **What each agent reads at spawn, under the new names.** Each definition's
  `skills:` lists only `agent-contract`. Preload per spawn is in #947's fold.
  Every `skills/`, `docs/` and `templates/` path a definition names exists
  (executed: each path extracted from `agents/*.md` and tested with `-f`; none
  missing).
- **A section no agent or check reads.** Of the headings of the three
  `orchestration.md` files and of `implement`, `verify`, `code-review` and
  `settle`'s `SKILL.md`, 18 are cited by no other tracked file (executed, a
  search for each heading in italics or as a quoted heading). Each of those
  files is read whole by the orchestrator or named whole by an agent
  definition (read, the agents' read lists above), so an uncited heading is
  still read, and nothing was filed.
- **A rule stated twice.** The paste check's `BASELINE` is the measured list.
  Its debt pairs are held by #1055 item 6 (fold above) and #1040 (agent
  pairs). Rule 2 and rule 6 restated in agent text are #1040's.
- **The rename's census beyond F1 and F2.** Old names left in living text are
  each exempted on purpose (`README.md:399-405`, `hooks/lib/routing.py:78`,
  `hooks/root-migrate.py`, `skills/settle/scripts/rule_changes.py:273`), held
  as history at a commit, or inside a replay case that checks out a commit of
  the old layout (`evals/behaviour/proofer/replay-*`, `evals/scripts/replay_targets.py`)
  (executed, `git grep` for each old name; read, each hit).

## The resulting order

A group's issues are said to run in parallel where the files each would edit,
read from its body and the coordinates above, do not meet. Where two meet, the
shared file is named and they run in the order given.

### release: 0.24.0

| Step | Issues | Parallel, and the shared file where not |
|---|---|---|
| 1 | #1052 | alone |
| 2, the small fixes | #1058, #913, #712, #920 | all four in parallel. F1 is fixed before them, directly and without a work item: six typo sites are below the SDD ladder (owner, 2026-10-28). #920: `hooks/worktree-guard.py` and its tests, which #1096 in step 8 also edits. #1058: `tests/conftest.py`, `tests/skills/test_chain_check.py`, `tests/skills/test_broad_gate.py`, `skills/code-review/orchestration.md`. #913: `skills/verify/scripts/pact_check.py`, `coordinates.py`, `hooks/lib/config.py`, `templates/records/sdd-design.md`, `templates/setup/pact.md`. #712: `skills/verify/scripts/session_cost.py` and its tests |
| 3 | #1039, #1042, #1043, #1040, then #1041, then F2 | #1039, #1042, #1043 and #1040 in parallel. #1041 after #1040: both edit `agents/crafter.md`. F2 after #1041: it rewords `agents/*.md`, which #1040 edits, and `skills/implement/SKILL.md` and `agents/crafter.md`, which #1041 edits |
| 4, the checks that read written text | #992, #956, then F3 | #992 and #956 in parallel. F3 after #956: both judge checks that read written text, and F3 decides each prose pin against what #956's audit settles (owner, 2026-10-28). #992: `evals/scripts/noninferiority.py`, `tests/evals/test_noninferiority.py`, `evals/README.md`. #956 writes its table on the issue and edits no file. F3: `tests/text/test_the_agent_contract_holds_the_universal_rules.py`, `skills/agent-contract/SKILL.md` |
| 5 | #1055, #1056 | in parallel. #1055: the READMEs, `CONTRIBUTING.md`, `skills/config/SKILL.md`, the two hygiene workflows, `.claude-plugin/marketplace.json`, its listed tests. #1056: the six scripts its items name and their tests |
| 6 | #1053 | alone |
| 7 | #1020, then #951 | not in parallel: both edit `skills/code-review/scripts/chain_check.py`, and #951 annotates every Python file |
| 8 | #1096 | alone |
| 9 | #1102 | last, alone |

Step 3 runs before step 4 because F3 weighs pins that #1040 changes.

### release: 0.24.1

| Step | Issues | Parallel, and the shared file where not |
|---|---|---|
| 1 | #1045, #1047, #1049 | in parallel. #1045: `skills/code-review/scripts/chain_check.py`, `skills/code-review/orchestration.md`, `templates/records/sdd-gaps.md`, `agents/crafter.md`, `agents/sealer.md`, `skills/settle/SKILL.md`. #1047: `agents/framer.md`, `evals/behaviour/framer/`. #1049: the guard's hooks, `hooks/dispatch.py`, the guard's tests |
| 2 | #1046 | after #1045: both can edit `skills/implement/orchestration.md`, whose acts table carries the row for *Orchestrator: the run ends with a verifying round* that #1045 changes |
| 3 | #1048, then #1091 | not in parallel: both edit `agents/sealer.md` and `skills/verify/SKILL.md`. Both come after step 1: #1048 shares `skills/code-review/orchestration.md` and `agents/sealer.md` with #1045, and #1091 shares `agents/crafter.md` with #1045 |
| 4 | #947 | last, the measurement on the final state |

### The two descriptions

The crafter writes these as they stand, with each `F<n>` replaced by the
number its issue was filed under.

`release: 0.24.0`:

> Purpose: review the renamed tree and lighten what it carries, first the checks. Order: #1052 first and alone, one read of the tree after 0.23.0's rename and 0.23.1's reorganisation, which folded each issue below to the new names. F1 was fixed directly, before the small fixes, without a work item. Then the small fixes #1058, #913, #712 and #920, which share no file and run in parallel. Then #1039, #1042, #1043 and #1040 in parallel; #1041 after #1040, because both edit agents/crafter.md; and F2 after both, because it rewords the agent definitions and skills/implement/SKILL.md that they edit. Then the checks that read written text: #992 and #956 in parallel, and F3 after #956, whose audit it builds on and after #1040 has changed the sentences its pins read. Then #1055 and #1056 in parallel, one source per fact and the code no input reaches. Then #1053, the GitHub Release as the release notes, opening with its theme, and changelog/ removed. Then #1020 and then #951, the static type check, because both edit chain_check.py and #951 annotates every Python file. Then #1096, the two environment variables, after #920 because both edit hooks/worktree-guard.py; and #1102 last, the README rewritten for a first reader once the rest of the release has changed what it describes. Released as 0.24.0 after the rename; these issues were planned as 0.22.5.

`release: 0.24.1`:

> Purpose: lighten the process itself, then measure what the 0.22.x and 0.24.x lightening changed. Order: #1045 (verifying rounds over records), #1047 (the framer's read-only probes) and #1049 (the worktree guard weighed against its cost) in parallel, because they share no file. Then #1046, after #1045, because both can edit skills/implement/orchestration.md. Then #1048 and then #1091 (a rename or a move owes no red-first case and no mutation run), because both edit agents/sealer.md and skills/verify/SKILL.md, and each shares an agent definition with #1045. Then #947 last, the measurement taken on the final state, which also counts the sealer's withholds over the pull request body after #1103 shipped #1044 in 0.23.1. Planned as 0.22.6.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1, a folded body | Given an issue this frame folds, when the crafter has applied its row, then the body holds every change its row names, keeps every other sentence, and holds no old form from the mapping table outside a `<commit>:<path>` citation or a sentence of history its row keeps | `gh issue view <N> --json body` read back against the row, and `grep -n -i -E` with the pattern in `plan.md` *Technical context* over the body, each remaining hit judged in the phase record |
| S2, a body left alone | Given #1053, #1096 or #1102, when the work ends, then its body is the one the frame read | `gh issue view <N> --json updatedAt` still reads its value at the read (executed 2026-10-28T05:24:47Z): #1053 2026-10-27T02:26:00Z, #1096 2026-10-28T04:03:25Z, #1102 2026-10-28T04:05:42Z |
| S3, the issue that stays | Given #920, when phase 2 ends, then its milestone is `release: 0.24.0` and it carries no comment about a move | `gh issue view 920 --json milestone,comments` |
| S4, the new issues | Given F1, F2 and F3, when phase 1 ends, then each is open in `release: 0.24.0` with the title above and a body holding every evidence line of its section | `gh issue view <N> --json title,body,milestone` |
| S5, the descriptions | Given milestones 65 and 67, when phase 4 ends, then each description is the text above with the F numbers filled, opens with `Purpose:`, and names each open issue of its milestone once and no closed issue or issue of another milestone | `gh api repos/MichaelYcJo/AgenticSeal/milestones/<n> --jq .description` compared with `gh issue list --milestone "<title>" --state open --json number` |
| S6, #1044 | Given #1044, when phase 3 ends, then it carries one comment saying its count now lives in #947 | `gh issue view 1044 --json comments` |
| S7, the tree | Given this branch, when the work ends, then no file outside this work item's directory differs from `0b75346f` | `git diff --stat 0b75346f..HEAD -- . ':!seal/threads/1793163944-the-issues-were-filed-against-the-old-tree'` prints nothing |

## Data & interfaces

The objects this work edits are on GitHub, in `MichaelYcJo/AgenticSeal`:
issue bodies through `gh issue edit <N> --body-file <file>`, one title through
`gh issue edit 1040 --title`, comments through
`gh issue comment`, new issues through
`gh issue create --milestone "release: 0.24.0"`, and the two descriptions
through `gh api -X PATCH repos/MichaelYcJo/AgenticSeal/milestones/65 -F description=@<file>`
and the same for milestone 67. `-F` with `@` reads the file's contents; `-f`
would send the literal text. No schema, endpoint or file of the tree changes.

## Rule changes

- nothing
  why: the work edits issues and milestones on GitHub and states no rule of the policy root

## Removes

- nothing
  why: no tree file changes; the lines the folds take out of issue bodies are named in each verdict row above

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-28 by framer, before the build.
