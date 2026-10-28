# Phase 4: 1793174170-two-facts-kept-in-several-files-have-drifted

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 4ecc77fa |

## What this phase was asked

Build `frame/plan.md`'s phase 4, the shipped workflow as the one source.
`templates/setup/hygiene.yml` gains `permissions` and `concurrency` (S8).
Its chain-step comment names the review record's section instead of listing
refusals (S10). The repository's two shared steps lose their comments to a
pointer, and the case comparing the steps is added (S9). Of
`.github/workflows/hygiene.yml`, only the comments of the two shared steps
are touched. `frame/questions.md` Q2 and Q3 are built on their defaults.

## What this phase found

- **Q2 met its first option.** `docs/the-review-record.md:179` still reads
  `## What the check reads at the pull request` at the branch tip, so the
  template's comment names that heading as framed (read).
- **Q3 met its first option.** The branch carries no commit of #1053 or
  #1117, and `origin/release/v0.24.0` still points at `5287dd42`. The
  phase edited only the two shared steps' comments in
  `.github/workflows/hygiene.yml`, at what were `:132-158` and `:208-224`,
  and none of the release steps. Whether a later merge conflicts is the
  merge's question, as the default says (read).
- **S8, S9 and S10 seen red, then green.** Against the workflows at
  `5287dd42`, the module failed three cases with exit 1: the concurrency
  case on the template's missing `concurrency:`, the new token-scope case
  on its missing `permissions:`, and the new shared-step case on the
  repository's chain-step comment, which was the old history and not the
  pointer. The shared commands already matched, so that case reached the
  comment assertion. After the edits the module passed, 25 cases, exit 0
  (executed).
- **How the template joins the cases.** `workflow_texts()` returns every
  workflow under `.github/workflows/` and the template under its repository
  path. The draft-event and concurrency cases loop over it, so the template
  is held to both reasons the module's docstring gives. `read` and
  `workflows` keep their meaning, because three other modules import them
  (`test_the_suite_has_a_command_that_is_cheap_twice.py`,
  `test_the_windows_leg_runs_in_shards_that_make_the_whole.py`,
  `tests/skills/test_arm_check.py`), and each still passed with exit 0.
- **How the shared steps are paired.** A step of the template is shared
  when its `run:` block names the clone's prefix `"$RUNNER_TEMP/agentic/`.
  Its name must stand in the repository's file, and the two commands must
  be equal once continuation backslashes are joined, whitespace collapsed
  and the prefix taken off with its closing quote. The mode step is two
  lines in the template and one in the repository, so a byte comparison
  of the `run:` bodies would fail on layout and not on the command. The
  first draft also read a one-line `run:` value. Both files write every
  shared step as a `run: |` block, so that branch had nothing to read and
  was removed in `4ecc77fa`.
- **The template's comment on the chain step** now says what the step
  guards in one sentence: a routed work item carries its round record, and
  a commit with no `Seal-Routing` trailer is not judged. It then names the
  plugin's `docs/the-review-record.md` *What the check reads at the pull
  request*. The `on:` comment above still names three refusals a draft
  excuses. The frame scopes S10 to the chain step's comment, so that
  comment stays.
- **The template's new blocks are the repository's**: the same
  `concurrency` group and `cancel-in-progress: true`, and `permissions:`
  with `contents: read` alone. The template has no step that reads issues,
  so `issues: read` is not copied. `tests/e2e/teammate/test_teammate_flow.py`
  passed, 7 cases, exit 0 (executed).
- **Each new unit was mutated, and each went red.** `seal mutate` printed
  `red` with exit 0 for seven mutants: `contents: write` and
  `cancel-in-progress: false` in the template, `--baseline "origin/main"`
  in the repository's chain step only, the repository's pointer reworded,
  the template's section name cut, `command()` keeping its backslashes,
  and `fetch-depth: 1` in the template (executed).
- **Every module that reads either workflow ran green.** Found with
  `git grep -l` on `hygiene.yml`, `"workflows"` and the module's name under
  `tests/`, 27 modules, one per call, each exit 0, among them
  `tests/skills/test_seal.py` (400), `tests/skills/test_chain_check.py`
  (261) and `tests/e2e/teammate/test_teammate_flow.py` (7).
  `tests/test_censuses.py` passed, 175 cases, exit 0. `uvx ruff check` and
  `uvx ruff format --check` passed over the changed test module (exit 0,
  executed).
