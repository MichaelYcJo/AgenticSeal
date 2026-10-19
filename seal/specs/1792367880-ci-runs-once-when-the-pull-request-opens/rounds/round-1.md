# 1792367880-ci-runs-once-when-the-pull-request-opens — review round 1

target: 3ba50b9f against release/v0.22.2

## Findings

### 1. Two places still assume a pull request exists, or does not, at the wrong moment

severity: should
location: `skills/code-review/orchestration.md:153`, `skills/code-review/orchestration.md:175-179`, `skills/code-review/orchestration.md:220-223`, `agents/sealer.md:39-40`
verdict: open

The new order moves the moment the pull request exists. Sentences written
for the old moment now give an instruction that cannot be followed, or
say something false on a path the same section creates. An orchestrator
running under `Automation | yes` acts on them without asking.

Grounds, read:

- `skills/code-review/orchestration.md:153` is a step of the framer's route:
  "The pull request | labelled `chain: reframed`". That route runs in the
  middle of the review run, when a round's `regression:` line sends the
  work item back to its framer (`:134-155`). Under the new rule no pull
  request exists until `guarantee.md` reading `sealed` is committed
  (`:159-163`). So the step names a pull request that does not exist. An
  orchestrator either skips the step without saying so, or opens a pull
  request so there is something to label. The second brings back the early
  pull request this work removes. Nothing reads the label
  (`docs/issues-and-milestones.md:183-185`), so it can wait until the pull
  request opens.
- The stated limit (`:175-179`) is the one path where the sealer runs again
  after the pull request is already open. On that path,
  `agents/sealer.md:39-40` tells the sealer "the pull request opens with
  that body after your verdict", which is false. The repair sentence at
  `:220-223` ("or the pull request body, make it, commit, and spawn the
  sealer again") does not say that a repaired body has to reach the open
  pull request. The body is now a file outside the pull request. So a body
  the sealer asked to be repaired is changed in the file, and the open pull
  request keeps the old body. `docs/release-checklist.md:209-211` already
  names the command a body edit takes.
- The class, enumerated (contract §12). Every other sentence of the owner
  section and of `agents/sealer.md` that names the pull request was read
  against the new order. These hold: `:186-190` ("before it opens"),
  `:218-219` ("opens no pull request"), `:299` ("open no pull request until
  they have"), `:288-290` (the pull request's check), and `agents/sealer.md`
  `:34` and `:68-69`.

```markdown
| The pull request | labelled `chain: reframed` when it opens: `gh pr create --label 'chain: reframed'` |
```

```markdown
**The stated limit: a defect that only one platform shows, in work nobody
expected to be platform-specific, is found when the pull request opens,
after the sealer.** Its fix is a commit outside the work item's records, so
it takes the repair path below: a verifying round on its diff, the broad run
again, and the sealer again. Nothing else is built for it. The pull request
stays open through that repair. Where the repair touches the body, write the
file again and give the open pull request that body with
`gh api -X PATCH repos/<owner>/<repo>/pulls/<N> -F body=@<file>`.
```

```markdown
and a file holding the pull request body, which you read: the pull request
opens with that body after your verdict, or is given it where it is already
open. Where the session has no tracker, it names a file holding the issue
body too, and you read that file.
```

answer:

### 2. The owner section tells a run that stops before the pull request to push the branch

severity: should
location: `skills/code-review/orchestration.md:159-173`, `skills/implement/orchestration.md:327`, `skills/implement/orchestration.md:447`
verdict: open

The person's answer `Destination | stop before the pull request` means the
branch is handed back "committed and unpushed"
(`skills/implement/orchestration.md:327`, read). The review chain still runs
under that answer (`:447`, row `chain | stop before the PR`, read), so the
orchestrator of that run follows the owner section. Two new sentences there
tell it to push, and neither names `Destination`:

- `skills/code-review/orchestration.md:160`: "Push the branch as often as
  you like while the work is built and reviewed".
- `:170-171`: "Push the branch once the build's last phase closes and run
  `gh workflow run tests --ref <branch>`".

A push is an outward-facing act (`skills/implement/orchestration.md:249`),
and the routing answer is the person's. A run under `Automation | yes`
follows the section without asking, so it pushes a branch the person said
should stay unpushed. The old text had the same gap in another form, since
it opened a draft at the same point. These two sentences are this diff's,
though, and they are where the order is now stated.

```markdown
**The pull request opens ready, once the sealer has sealed, and CI runs
then.** Where `Destination` reads `open the pull request`, push the branch as
often as you like while the work is built and reviewed: a branch with no
pull request runs nothing. Under `stop before the pull request` nothing is
pushed, and the branch is handed back committed and unpushed.
```

```markdown
**Where the work's risk is platform-specific, run the other platforms before
your broad run.** Line endings, the shell and the Python version are such
risks. Push the branch once the build's last phase closes and run
`gh workflow run tests --ref <branch>`, then read that run's result before
you take the broad run. A leg that fails there is a defect like any a round
finds, and it is repaired before the rounds settle. Under `stop before the
pull request` push nothing: name the platform risk in the handback, for
whoever opens the pull request.
```

answer:

### 3. Nothing pins the orchestrator's half of the body file, so the file the sealer reads can lose its writer without a case going red

severity: should
location: `tests/test_the_rules_have_one_owner.py`, `skills/code-review/orchestration.md:162-163`, `skills/code-review/orchestration.md:181-184`, `skills/code-review/orchestration.md:186-188`, `skills/code-review/orchestration.md:196-197`, `docs/the-broad-gate.md:5`
verdict: open

S8's case pins the sealer's half: the definition says the spawn prompt
names a file holding the body (`tests/test_the_sealer_guarantees.py:406-422`,
read). The other half is the orchestrator's: write the body to a file, name
that file in the spawn, and open the pull request with it. No case holds
it. Suppose the spawn sentence goes back to "the issue and the pull
request". The orchestrator then passes a pull request that does not exist
yet. The sealer reads no body and cannot compare the parties in its step 4
(`agents/sealer.md:68-69`, `:76-80`). Every case stays green. This is risk
(4) of the round's spawn prompt: a pin that would pass with the old rule put
back.

Grounds, executed:

- Each of three mutations of the owner section survived six modules, 179
  passed every time: `test_the_rules_have_one_owner.py`,
  `test_the_sealer_guarantees.py`, `test_broad_gate_rule.py`,
  `test_every_orchestrator_act_names_its_delivery.py`,
  `test_a_parallel_agent_names_its_scratch_after_the_work_item.py` and
  `test_the_stamp_reaches_the_person_it_is_drawn_for.py`. The three
  mutations were:
  - the spawn sentence (`:196-197`) taking back "the pull request";
  - "written to a file" removed (`:187-188`);
  - `--body-file <that file>` removed from the open command (`:163`).
- Deleting the clause that keeps a draft's record owed (`:182-184`,
  "`ready_for_review` event re-runs it when the draft is marked ready, so the
  record is still owed then") survived `test_the_rules_have_one_owner.py`,
  23 passed. That module's
  `test_a_draft_is_tolerated_and_still_owes_the_record` says in its
  docstring that "BOTH halves are asserted", and its second assertion is the
  general "Nothing that can reach `main` is exempt".

Grounds, read:

- No module under `tests/` or `evals/` contains "written to a file",
  "holding the pull" or `--body-file <that file>`. The only hits for these
  strings are the S8 case on `agents/sealer.md` and unrelated `gh` fixtures.
- `phases/phase-2.md` reports that the `docs/the-broad-gate.md:5` mutation
  survives. That is the builder's claim, and no module that reads that file
  holds the sentence.

The phase-2 record lists sixteen caught mutations. None of these five is
among them, so this is no contradiction of that account.

```python
def test_the_orchestrator_writes_the_body_file_the_sealer_reads():
    """S8 of #943, the orchestrator's half. `agents/sealer.md` reads the pull
    request body from a file the spawn prompt names, because no pull request
    exists when the sealer runs. The owner section writes that file, names it
    in the spawn, and opens the pull request with it. Round 1 of #943 reverted
    each of the three and this module stayed green."""
    text = flat(*ORCH)
    assert "once the pull request body is written to a file" in text
    assert "the issue and the file holding the pull request body" in text
    assert "`gh pr create --body-file <that file>`" in text
    gate = flat("docs", "the-broad-gate.md")
    assert "before the pull request opens" in gate
    assert "before a pull request is marked ready" not in gate
```

And in `test_a_draft_is_tolerated_and_still_owes_the_record`, the half its
docstring names:

```python
    assert (
        "`ready_for_review` event re-runs it when the draft is marked ready, "
        "so the record is still owed then"
    ) in flat(*ORCH)
```

Each assertion above was read against the tree at `3ba50b9f` and holds
there (executed, a `python3 -c` that flattens the two files). Each still has
to be seen red against its mutation (contract §15).

answer:

## Confirmations

confirms: none
Risk (1), the concurrency groups. Neither holds nor cancels a run it
should not. Read: both workflows declare
`${{ github.workflow }}-${{ github.event.pull_request.number || github.run_id }}`
(`.github/workflows/test.yml:19-21`, `.github/workflows/hygiene.yml:20-22`, read).
The two workflow names differ, `tests` and `hygiene` (`:1` of each), so one
pull request's two workflows hold two groups and cannot cancel each other.
A `push` to `main` and a `workflow_dispatch` group on `github.run_id`, so
each takes a group of its own. `test.yml` cancels only where
`github.event_name == 'pull_request'`. `release-report` looks the tag's run
up by `head_sha` and `event=push` (`test.yml:277-279`), and that run is
never grouped with another. The `edited` event `hygiene` keeps (`:12-16`)
cancels a run of the same head, and the newer run checks the same commit
with the newer body. Executed: `tests/test_ci_gives_the_checks_what_they_need.py`
went red under two of phase 1's eleven mutations, the fallback set back to
`github.ref` and the block taken out of `hygiene.yml` (1 failed, 21 passed
each).

confirms: none
Risk (2), a surviving instruction to open a draft. None stands outside the
records. Read: a `git grep` for `draft`, `marked ready`,
`ready pull request`, `gh pr view`, `before round 1` and
`Ready for review` over the tree outside `seal/specs/`, `changelog/`,
`tests/` and `evals/` finds only sentences that describe what `chain_check`
does on a draft: `README.md:201-206` and `:605-606`, `README.ko.md:599`,
`docs/the-review-and-parity-arms.md:100`, `docs/the-review-record.md:152`
and `:254`, `skills/implement/orchestration.md:635`, `templates/hygiene.yml`
and the two workflows' comments. Also the owner section's own history
sentence at `skills/code-review/orchestration.md:164-166`. `tests/` and
`evals/` hold no instruction to open one either.

confirms: none
Risk (3), the sealer and the orchestrator agree on the file, as written.
Read: the owner section writes the body to a file (`:186-188`), names it
in the spawn (`:196-197`) and opens with it (`:162-163`). `agents/sealer.md`
reads it from the prompt (`:38-40`, `:68-69`). The five sealer evals already
pass `.git/specseal-eval/pr-body.md` (each case's `prompt.md:5`). Finding 3
is about whether this agreement is pinned, not whether it holds today.

confirms: none
The build's account against the tree. Read:

- `agents/sealer.md` changed in the three places `phases/phase-2.md` names
  and nowhere else (`git diff 75502328..3ba50b9f -- agents/sealer.md`).
- `CELL_UNCOMMITTED` reads `commit it before you push`
  (`skills/verify/scripts/broad_gate.py:3083`), and both pins read it
  (`tests/test_the_seal_is_taken_once_by_the_sealer.py:3133`, `:3223`).
- Step 2 of the order holds no `draft` (`skills/implement/orchestration.md:37-40`).
- CONTRIBUTING's three platforms match the matrix (`test.yml:69-108`). Its
  "a branch with no pull request runs nothing" matches every workflow's
  `on:` block: `push` only to `main`, `release/*` or `v*` tags.
- The shortened heading is right: the frame's heading is 89 columns as a
  Markdown line and the built one is 84 (executed, `python3 -c` `len`).

Executed: the six modules of finding 3 passed, 179, at `3ba50b9f` as the
baseline of each mutation run.

confirms: none
The files this item must not touch are untouched. Executed:
`git diff --stat 75502328..3ba50b9f` lists neither
`skills/code-review/scripts/chain_check.py` nor `docs/the-review-record.md`.
`skills/implement/orchestration.md`'s hunks are at `:37-42` and `:639`
only. #968's two lines are unchanged in content, and they moved from `:381`
and `:416` to `:379` and `:414`, because step 2 is two lines shorter.

confirms: none
The four divergences in `overview.md` hold on the tree. Read:

- the `github.run_id` fallback;
- `hygiene.yml:180-181` no longer states the old order;
- the shortened heading;
- the spawn sentence at `skills/code-review/orchestration.md:196-197`.

The fallback rests on GitHub cancelling an older pending run in a shared
group. That matches GitHub's documented concurrency behaviour as this
reviewer knows it. It was not opened here, so it is a row of `## Not judged`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether GitHub runs `hygiene` and not `tests` when a draft is marked ready, a newer push cancels the older pull-request runs, and a push to `main` is neither held nor cancelled (`questions.md` Q1). No local run shows trigger or cancellation behaviour | `.github/workflows/test.yml:3-21`, `.github/workflows/hygiene.yml:3-22` | the orchestrator, by `gh run list --branch <branch>` once this item's pull request opens |
| Phase 1's reading of GitHub's documentation that an older pending run in a shared group is cancelled whatever `cancel-in-progress` says. The `github.run_id` fallback rests on it, and this round did not open the page | `seal/specs/1792367880-ci-runs-once-when-the-pull-request-opens/phases/phase-1.md` | the orchestrator, with Q1's measurement |
| How the sealer behaves after its three changed sentences | `agents/sealer.md:4-7`, `agents/sealer.md:38-41`, `agents/sealer.md:69` | the orchestrator, by the sealer measurement it is running |
| `gh workflow run tests --ref <branch>` names this repository's workflow. The owner section ships to other repositories, where the workflow may have another name or no `workflow_dispatch` trigger. `spec.md` §*Scope* item 3 names the command, so it is the frame's choice, not a build defect | `skills/code-review/orchestration.md:170-171` | the repository owner |
| The full suite, the repository-wide lint and the typecheck: not run in this round, so the suite is `unverified` | the branch at `3ba50b9f` | the orchestrator, by `broad-gate --base release/v0.22.2 --record` once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `mutation-check skills/code-review/orchestration.md --replace "the issue and the file holding the pull" "the issue and the pull request; the pull" --tests "bin/test <the six modules of finding 3> -q -p no:randomly"` | SURVIVED, exit 1: baseline green, then 179 passed against the mutation |
| `mutation-check skills/code-review/orchestration.md --replace "written to a file and the" "written and the" --tests` (the same six modules) | 179 passed against the mutation: survived |
| ``mutation-check skills/code-review/orchestration.md --replace '`gh pr create --body-file <that file>`' '`gh pr create`' --tests`` (the same six modules) | 179 passed against the mutation: survived |
| `mutation-check skills/code-review/orchestration.md --replace $'re-runs it when the draft is marked ready, so the\nrecord is still owed then' 'stays where it was' --tests "bin/test tests/test_the_rules_have_one_owner.py -q -p no:randomly"` | SURVIVED, exit 1: 23 passed against the mutation |
| `mutation-check .github/workflows/test.yml --replace "pull_request.number \|\| github.run_id" "pull_request.number \|\| github.ref" --tests "bin/test tests/test_ci_gives_the_checks_what_they_need.py -q -p no:randomly"` | red, exit 0: 1 failed, 21 passed |
| `mutation-check .github/workflows/hygiene.yml --replace "concurrency:" "x-concurrency:" --tests` (the same module) | red, exit 0: 1 failed, 21 passed |
| `python3 -c` flattening `skills/code-review/orchestration.md` and `docs/the-broad-gate.md` and testing finding 3's proposed strings | every proposed assertion holds at `3ba50b9f` |
