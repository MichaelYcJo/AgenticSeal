# Design: 1795736973-the-preflight-passes-where-a-round-is-owed

## Grounding

The tree as read at `a1cae2026`.

| Policy clause | What it fixes for this work |
|---|---|
| `docs/running/the-broad-gate.md` *What the gate runs*, the paragraph opening **The gate that measures a tree is the copy that tree ships** | It states that "the gate exists to say what CI will say". At the pull request CI judges the records as a ready pull request (`.github/workflows/hygiene.yml` passes no `--sealing`). A gate whose chain arm passes over what CI will refuse breaks this clause. (read) |
| `docs/checks/the-pull-request-check.md` *What the check reads at the pull request*, its first paragraph | "A ready pull request fails on any refusal ...; a draft, or a run that observed no pull request, prints the same lines and exits 0." This sentence is the policy that the gate's arm inherits today, and the one `## Rule changes` amends for the gate's run. (read) |
| `docs/running/what-a-script-gates.md` *Which gate a script holds* and *The checks*, the `chain_check.py` row | A script gates on a closed form, an exit code among them. The row says the check runs at "the pull request; the preflight and the broad run". The gate reads the arm's exit code and nothing else, and the design keeps it so. (read) |
| `skills/core/SKILL.md` *Judgment is not licence to skip a party*, the sentence under the table | "The check refuses only a ready pull request, where its GitHub Actions workflow is installed; before the pull request, and in local mode, the four rows are held by `agents/sealer.md` step 1 and by the orchestrator". The change makes the first clause false for the gate's run, so *Scope* item 4 rewrites it. The core is plugin text and not the policy root, so it is edited in place. (read) |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* | A mechanism is weighed by what it caught against what it costs; a script holds a gate on an exact fact. The design adds no flag and no mark: it changes what the existing `--sealing` flag means, and removes the `gh` call that flag makes (`## Removes`). (read) |
| `skills/code-review/gate-to-pull-request.md` *Orchestrator: from the preflight to the open pull request*, the paragraph opening **The preflight is yours, and it is not the broad gate** | "a refusal on a record arm, which the broad run would return after that suite, arrives before it." The paragraph three above it says "Your broad run asks the records arm first, and that arm refuses a commit outside the work item after the last round's `target:` commit". Both describe a refusal the code does not give before a pull request exists. The design makes the code give it. (read) |
| `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*, the paragraph opening **Whether a round follows a fix pass is read off the chain check** | The orchestrator reads the words of `chain_check.py --worktree` after it commits a fix pass's record, and decides on the line that names the record, not on the exit code. That read stays as it is (`frame/plan.md` *Alternatives considered*, A6). (read) |

What the code does at `a1cae2026`:

- `skills/code-review/scripts/chain_check.py#_checked` sets `unseen = state == "unknown" and not event_payload_present()` and `strict = state != "draft" and not unseen`. Unstrict, every problem prints as a `notice` and the check returns 0. `--sealing` changes only which arms print in place of failing: the broad gate arm, the guarantee arm, the guarantee's `original:` line and the body arm. (read)
- `skills/verify/scripts/broad_gate.py#gate` runs the chain arm as `chain_check.py --baseline <base> --root <root> --sealing`, in the preflight and in the broad run alike, and fails it on its exit code alone. (read)
- `lib/console.py#annotate` prints a notice and an error in the same `path:line  message` shape outside GitHub Actions. So the kept `chain.txt` does not say which lines refused. (read)
- The `unseen` clause came from #866 (`c38f97d71`), whose round 1 finding 1 was that the round-record generator, `round_record.py new` and `close`, exited 1 on a correct mid-run record where no pull request was visible. No script loads `chain_check.py#main` in process today: `git grep -n chain_check -- '*.py'` outside `tests/` names `broad_gate.py`, `seal_stamp.py`, `pr_body.py`, `release_seal.py` and `finding_counts.py`, and only `broad_gate.py` runs the check as a command. (executed)

Probes, each in a `git clone --no-local` of this repository under `<scratchpad>/1795736973-the-preflight-passes-where-a-round-is-owed/frame/`:

- **The issue reproduces.** At `e902ea9a3`, fetched by its full SHA from this repository (no branch holds it), `python3 skills/verify/scripts/broad_gate.py --root <clone> --base 8dea1ca7b --preflight` with `GITHUB_EVENT_PATH` and `GITHUB_ACTIONS` unset printed `PREFLIGHT PASSED` and exited 0. Its kept `chain.txt` holds the state line "the pull request's state is unknown, and it is not judged as a ready pull request", and three lines on `seal/threads/1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home/trail/rounds/round-1.md` ending "a verifying round is owed". (executed)
- **The cause is the strict line, and only it.** With that commit's `strict = state != "draft" and not unseen` changed in the clone to `strict = args.sealing or (state != "draft" and not unseen)`, the same command printed `PREFLIGHT FAILED`, exited 1, and quoted the three refusals among the failure form's eight first lines. (executed) This answers the issue's first *Not known*: the preflight runs the records arm whole, and the arm reads the verifying round and prints it as a notice.
- **What the strict arm does at real gate runs.** The patched check of `a1cae2026`, run as `chain_check.py --baseline <base> --root <clone> --sealing` at the five `run:` commits that `trail/gate.md` records for the work items of releases 0.39.0 and 0.39.1, exited 0 at three and 1 at two (`test_tmp_sealing_runs.sh`). (executed) The two are #1614 at `4836857a1` against `6f4802fa8`, where `trail/rounds/round-2.md` owes a verifying round, and #1612 at `cc88ba151` against `8d99b99e2`, where `trail/rounds/round-5.md` owes one. In both the round that read those fixes, #1614's round 3 and #1612's round 6, names the gate's tree as its `target:`, so its record was committed after the gate ran. The strict arm would have refused each run until that record was committed. At both, and at `e902ea9a3`, every line before the first refusal is a notice, and the first refusal stands at line 5 of the check's output. (executed)
- **The 0.39.1 record.** `seal/threads/1795642930-a-session-fix-pass-reads-no-records-whole/trail/gate.md` holds `run: d340999df against 4e7ad2362`. The strict check exits 0 there, so that run's `chain ✓ exit 0` would have read the same under this design. (executed)

The issue carries no comments (`gh issue view 1620 --json body,comments`). (executed)

## Scope

**In.**

1. **Under `--sealing`, `chain_check.py` judges as at a ready pull request, whatever the state.** `#_checked` reads no pull request's state where `--sealing` is given, and `strict` holds. Every refusal of every arm fails the run, except the arms `--sealing` already prints: the broad gate arm, the guarantee arm, the guarantee's `original:` line and the body arm. A run without `--sealing` keeps today's judgment: a draft, and a run that observed no pull request, print and exit 0. CI passes no `--sealing` and is unchanged.
2. **The state line says what the run judged.** Under `--sealing` the first line the check prints says that the run is the broad gate's and is judged as a ready pull request, in place of the state line it prints today. It does not print `UNSEEN_SAYS`, which says the run is not judged as a ready pull request. The new text is a constant beside `SEALING_SAYS`, and a case pins it (contract rule 14).
3. **The code's own statements of the old fact are rewritten in place.** In `chain_check.py`, the module docstring's sentence "A ready pull request fails on any of them. A draft, or a run that observed no pull request, prints the same lines and exits 0." and its paragraph on `--sealing` under *Usage* say that `--sealing` judges as a ready pull request. In `broad_gate.py`, the module docstring's arm 2 line, "judged by the pull request's state as the check reads it", and the comment above `sealing = sibling.load(CHAIN_CHECK).SEALING` in `#gate`, which says the pull request's state is the check's to read, say the same.
4. **`skills/core/SKILL.md`, the sentence under the invariants table.** It says that the check refuses at a ready pull request where the workflow is installed, and in `seal gate`'s preflight and broad run whatever the state. It also says that before the pull request the gate's run holds the first two rows and prints the last two, and that `agents/sealer.md` step 1 and the orchestrator hold the last two then, and all four in local mode, where the check judges no work item.
5. **`skills/code-review/gate-to-pull-request.md`.** The paragraph opening **The preflight is yours, and it is not the broad gate** gains the reason its refusal arrives: the chain arm judges as a ready pull request whatever the state, so a line it names, a verifying round owed among them, is a refusal. The sentence "Your broad run asks the records arm first, and that arm refuses a commit outside the work item after the last round's `target:` commit" is rewritten: the broad run asks the records arm after its suite. The rest of that sentence's claim, that a run taken straight after the fix returns the same refusal, is true under item 1 and stays.
6. **Cases.** In `tests/skills/test_chain_check.py`: under `--sealing` with no payload, and again with a draft payload, a branch whose last record owes a verifying round exits 1 and prints the line `chain_check.py#VERIFYING_ROUND` holds; without `--sealing` and with no payload the same branch exits 0. Under `--sealing` no `gh` is asked. The state line of item 2 is pinned. The clause of `test_accepts_a_draft_or_an_unseen_pull_request_with_a_notice` that asserts exit 0 under `--sealing` with no payload is rewritten to the new behaviour. In `tests/skills/test_broad_gate.py`: `seal gate --preflight` over a fixture whose last record owes a verifying round, with no payload, exits 1, prints `PREFLIGHT FAILED`, and its failure form holds the `VERIFYING_ROUND` line. The broad run shares the arm list with the preflight (`#gate` skips only the command, by condition), so one gate case holds both. Each case is seen red against the code at `a1cae2026` (contract rule 15).
7. **The version moves to 0.39.2** in `.claude-plugin/plugin.json`, and `changelog.md` is written for the work item. This is the release's first pull request.

**Out.**

- **The orchestrator's `chain_check.py --worktree` read after each fix pass, and the proofer's read before it hands back.** Both read the check's words and not its exit code, and both run before a verifying round exists, where an open finding is the expected state. They keep the unstrict judgment (`frame/plan.md` *Alternatives considered*, A6).
- **The order in which the check prints its lines.** Notices print before refusals, and the gate's failure form quotes eight first lines. At the three probed commits where the strict arm refused, the first refusal stood within them (`## Grounding`). Where notices fill all eight, the form names the kept file and the refusal stands there. This is a stated limit, not built for (`frame/plan.md` *Alternatives considered*, A7).
- **The sentences that open the gate's step at "the last round record has no finding open"** (`skills/verify/orchestration.md` *The broad gate*, `skills/code-review/SKILL.md`, `skills/implement/orchestration.md` *Orchestrator: drain the rows before the broad run, and keep the records*). They do not stand on the gate passing before a pull request. Whether a round follows a fix pass is `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*'s, and that rule is unchanged; the gate now refuses a run taken against it.
- **The issue's second *Not known*, whether CI refuses the same commit.** CI judges a ready pull request strictly with or without this change, and this design does not touch that path.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. The preflight refuses where a verifying round is owed | Given a branch whose last round record closes a finding `fixed <commit>` that no later record names, and no pull request; when the orchestrator runs `seal gate --preflight --base <base>`; then it exits 1, prints `PREFLIGHT FAILED`, and the chain arm's quoted lines hold the record's path and "a verifying round is owed" | The `tests/skills/test_broad_gate.py` case of *Scope* item 6, seen red against `a1cae2026`; and the probe of `## Grounding` run again at the build's HEAD over `e902ea9a3` |
| S2. The broad run refuses the same tree | Given the same branch; when the orchestrator runs `seal gate --base <base> --record <item>`; then the run prints `BROAD GATE FAILED` with the chain arm among the failing checks, and writes no `trail/gate.md` | Read: `broad_gate.py#gate` builds one arm list for both runs and skips only the command under `--preflight`; the case of S1 holds the arm |
| S3. A draft is judged as ready under the gate | Given the same branch and a pull request open as a draft; when the gate runs; then the chain arm exits 1 as in S1 | The `tests/skills/test_chain_check.py` case of *Scope* item 6 with a draft payload |
| S4. A hand run and CI keep their judgment | Given the same branch with no payload, or with a draft payload; when `chain_check.py` runs without `--sealing`, as the `--worktree` reads and hygiene's step run it; then it prints the same lines and exits 0, and a ready payload still exits 1 | The same case's half without `--sealing`; and read: `.github/workflows/hygiene.yml` and `templates/setup/hygiene.yml` pass no `--sealing` |
| S5. The gate's own records still print | Given a branch whose rounds have settled, with no `trail/gate.md` and no `guarantee.md`; when the gate runs; then the chain arm exits 0, and those arms print under the `--sealing` notice | The existing `a_sealed_run` fixture case, `test_the_fixture_branch_passes`, green at the build's HEAD; and the three passing probes of `## Grounding` |
| S6. The gate asks no `gh` | Given any branch; when `chain_check.py --sealing` runs; then no `gh pr view` is started | The `tests/skills/test_chain_check.py` case of *Scope* item 6, with a `gh` stub that records each call |
| S7. No text states the old judgment for the gate | Given the build's HEAD; when `git grep -n -e 'refuses only a ready' -e 'state as the check reads it' -e "is the check's to read" -e 'asks the records arm first' -- ':!seal/threads'` runs; then it prints nothing | The search, run at `a1cae2026`, printed four lines: `skills/code-review/gate-to-pull-request.md:156` (*Scope* item 5), `skills/core/SKILL.md:117` (*Scope* item 4), `skills/verify/scripts/broad_gate.py:27` and `:2043` (*Scope* item 3). The pathspec leaves out `seal/threads/`, where this frame quotes the patterns and the settle writes `docs/` (executed) |

## Data & interfaces

- `chain_check.py --sealing`: the flag keeps its spelling and its one caller, `broad_gate.py#gate`. Its meaning gains one clause: the run is judged as a ready pull request, and the state is not read.
- `chain_check.py#_checked`: under `--sealing`, `pull_request_state` is not called and `strict` is true. Without it, the state is read and judged as today.
- `seal gate --preflight` and `seal gate`: no new flag and no new output form. Exit 1 now arrives where the chain arm refuses before a pull request exists.
- A new string constant in `chain_check.py` for the state line of *Scope* item 2.

## Rule changes

- change
  file: docs/checks/the-pull-request-check.md
  section: What the check reads at the pull request
  from: A ready pull request fails on any refusal, each named
    `path:line  why`; a draft, or a run that observed no pull request,
    prints the same lines and exits 0.
  to: A ready pull request fails on any refusal, each named
    `path:line  why`; a draft, or a run that observed no pull request,
    prints the same lines and exits 0. The run of `seal gate` under
    `--sealing`, in the preflight and in the broad run alike, reads no
    pull request's state and judges as at a ready pull request, so a
    refusal the pull request would meet arrives before it opens. The arms
    that read what is written after that run, `trail/gate.md`,
    `guarantee.md` with its `original:` line, and the body the seal mark
    stands in, print there and do not fail.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `gh pr view` call a gate run makes through the chain arm | `skills/code-review/scripts/chain_check.py#_checked`, the call to `pull_request_state` under `--sealing` | Nothing: under `--sealing` the state decides nothing, so the call, its timeout and its printed source go from both gate runs |
| The state line that says a gate run is not judged as a ready pull request | `skills/code-review/scripts/chain_check.py#_checked`, the print of `UNSEEN_SAYS` under `--sealing` | The constant of *Scope* item 2. `UNSEEN_SAYS` stays for a run without `--sealing` |
| The clause pinning exit 0 under `--sealing` with no payload | `tests/skills/test_chain_check.py#test_accepts_a_draft_or_an_unseen_pull_request_with_a_notice`, its last three assertions | The cases of *Scope* item 6, which pin the refusal |
| The sentences that say the gate's run is judged by the pull request's state | `skills/verify/scripts/broad_gate.py`, the module docstring's arm 2 line and the comment above `sealing` in `#gate`; `skills/code-review/scripts/chain_check.py`, the module docstring's sentence on a draft and the *Usage* paragraph on `--sealing`; `skills/core/SKILL.md` *Judgment is not licence to skip a party*, the sentence under the table | Each is rewritten in place to the new judgment (*Scope* items 3 and 4) |

Framed 2026-11-27 by framer, before the build.
