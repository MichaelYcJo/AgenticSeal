# Implementation Plan: 1795736973-the-preflight-passes-where-a-round-is-owed

## Technical context

The tree as read at `a1cae2026`.

- `skills/code-review/scripts/chain_check.py#_checked` reads the pull request's state through `#pull_request_state`: the event payload, else `gh pr view --json isDraft`, else `unknown`. It sets `unseen` and `strict` from it, and prints each problem as `error` where `strict` holds and as `notice` otherwise. It returns `1 if problems and strict else 0` at both of its returns, the early one for a branch that declares nothing and the last one. `--sealing` moves the broad gate, guarantee, guarantee `original:` and body findings from `problems` to `notices`, and does nothing to `strict`.
- `skills/verify/scripts/broad_gate.py#gate` builds one dictionary of arms for the preflight and the broad run. It skips the command by condition under `--preflight`, runs the chain arm with `--sealing`, and fails an arm on its exit code alone. `failure_lines` quotes the first eight non-empty lines of an arm's output (`QUOTED`) and names the kept file.
- `lib/console.py#annotate` prints `notice` and `error` in one shape outside GitHub Actions, so nothing but the exit code tells the gate which lines refused.
- `tests/conftest.py` puts a `gh` stub answering `unknown` on every case's `PATH`, and `gh_answers` swaps it for a `ready` or `draft` stub. `tests/skills/test_chain_check.py#test_accepts_a_draft_or_an_unseen_pull_request_with_a_notice` pins exit 0 under `--sealing` with no payload.

**The failure scenario of the chosen approach.** Six months on, a repository whose gate runs before a pull request has records the chain arm refuses for a reason the orchestrator cannot repair before the pull request: say an arm that, like the body arm, can only be satisfied by something written after the gate. Today four such arms are printed under `--sealing`. A fifth arm added later without that exemption would refuse every gate run, and the orchestrator would meet it as a gate it cannot pass. The guard is that the exemptions stand in one place, `#_checked`'s `if args.sealing` branches, and that a new arm's pull request names what it reads and when (`docs/running/what-a-script-gates.md` *Which gate a script holds*).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. `--sealing` reads no state and judges as a ready pull request (*Scope* items 1 and 2) | An arm added later that only a post-gate record can satisfy refuses every gate run until it joins the `--sealing` exemptions (*Technical context*) | **Chosen.** The flag has one caller, `broad_gate.py#gate`, which passes it in both runs. The gate already means "the run CI will judge", by `docs/running/the-broad-gate.md` *What the gate runs*. The probes of `frame/design.md` `## Grounding` show the change refuses at `e902ea9a3`, at #1614's and #1612's gate runs, and nowhere else among the 0.39.0 and 0.39.1 runs. It adds no flag and removes a `gh` call |
| A2. A new flag, such as `--ready`, that the gate passes beside `--sealing` | Two flags that one caller always passes together; a later caller passing one and not the other reads a judgment nobody designed | Rejected: a second spelling of the gate's run. `--sealing` is already defined as "the broad gate's own run" (`chain_check.py` *Usage*) |
| A3. The gate reads the arm's output for refusals in place of its exit code | Outside GitHub Actions a notice and an error print in one shape (`lib/console.py#annotate`), so the gate would tell them apart by their words: a "not read:" notice, a `--sealing:` notice, a refusal. A notice reworded later reads as a refusal, or the reverse | Rejected by `skills/core/SKILL.md` *The rule a mechanism is kept against*: a script holds a gate on an exact fact, and the exit code is that fact |
| A4. The gate writes a payload, `{"pull_request": {"draft": false}}`, and points `GITHUB_EVENT_PATH` at it | The body arm reads the same file and finds no body, and every later reader of the variable meets a pull request that does not exist. The gate's comment in `#gate` says nothing is written into the environment for the check | Rejected: it fakes the one input whose absence the check reports, to change a judgment a flag already names |
| A5. Drop the `unseen` clause, so every run outside CI with no pull request is judged as ready, as before #866 | The proofer's and the orchestrator's `--worktree` reads exit 1 on every open finding mid-run, where an open finding is the expected state. #866's round 1 finding 1 found exactly that on the round-record generator. The docstring, the policy sentence and the S6 case all change, for no refusal the gate does not already get from A1 | Rejected. Replacing the structure was weighed: the premise that keeps `unseen` is that the `--worktree` readers read words and not the exit code, which `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* and `agents/proofer.md` step 7 both state (read). A1 changes the gate alone |
| A6. The orchestrator's read after a fix pass becomes `seal gate --preflight` in place of `chain_check.py --worktree` | The preflight's failure form quotes eight lines, while the read decides on the line naming one record among the whole output. The gain is one command at the last pass, where the preflight runs next anyway. The paragraph stands in `skills/code-review/orchestration.md`, which #1624 edits | Rejected: the read is kept. It reads committed records today and works on words, which A1 leaves as they are |
| A7. The check prints refusals before notices, so the failure form's eight lines hold the refusals whatever the notices | Every test that reads the output's order changes, and CI's log order with it, for a case no probe met: at the three commits where the strict arm refused, the first refusal stood at line 5 | Rejected on the measurement. Where notices fill the eight lines, the form names the kept file, which `skills/code-review/gate-to-pull-request.md` tells the orchestrator to read. A run where a refusal falls past line 8 is the record that would reopen this |
| A8. Documents only: `docs/` says the preflight does not read the records before a pull request, and why | The preflight's stated purpose, a record arm's refusal in seconds, holds nowhere before a pull request exists, which is when every preflight runs. Two of the five gate runs of 0.39.0 and 0.39.1 measured a verifying round owed and passed, and the pull request's check was the first reader to refuse | Rejected: the issue's first *Done when* outcome is reachable at one line of code, and `docs/running/the-broad-gate.md` asks the gate to say what CI will say |
| A9. A hook, such as a `PostToolUse` hook on the `Bash` call that commits a round record, that runs the check and blocks where a verifying round is owed | It reads every commit of every session for one state the preflight already reaches, and it blocks the commit where the next act is a round, not a refusal | Rejected: the owner's direction to weigh hooks beside text rules was met, and the gate is already the step that runs the check before the sealer. A hook adds a mechanism with no catch the gate's arm does not make |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 7 | The cases of *Scope* item 6, each seen red against `a1cae2026`; `tests/skills/test_chain_check.py` and `tests/skills/test_broad_gate.py` narrow; `git grep -n -e 'refuses only a ready' -e 'state as the check reads it' -e "is the check's to read" -e 'asks the records arm first' -- ':!seal/threads'` prints nothing (`frame/design.md` S7 accounts for the four lines it printed at `a1cae2026`); `seal mutate` on `#_checked`'s changed lines | `cf9731275` |

## Overlap with the release

The release's other open items are #1624, #1628 and #1629, as `routing.md` *Why this way* names them. None has a frame committed on any branch: `origin/release/v0.39.2` stands at `e65830869` and no branch names their numbers (executed). Each was read from its issue. #1624 changes `skills/implement/fix-pass.md` and the fix-pass sentences of `skills/code-review/orchestration.md`. #1628 and #1629 change where the orchestrator's building rules stand, in `agents/crafter.md` and the files the orchestrator opens when it builds. This work changes none of those files, and *Alternatives considered* A6 keeps it out of `skills/code-review/orchestration.md`. They meet on one check: once a later item's branch takes this work from the base, its own gate runs judge its records as a ready pull request.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1624, #1628, #1629 | No file. Their gate runs read this work's chain arm | #1620 | It is the release's first pull request and carries the version move. Merged first, the later items' preflights refuse what their pull requests would, inside the rounds they run anyway |

## Operational impact

- A gate run, preflight or broad, now exits 1 before a pull request exists where the chain arm finds a refusal, a verifying round owed among them, in every repository that runs this plugin's gate. CI is unchanged, since hygiene passes no `--sealing`.
- No migration, environment variable or dependency.
- The version moves from 0.39.1 to 0.39.2 in `.claude-plugin/plugin.json`, in phase 1's commit that adds `changelog.md`.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
