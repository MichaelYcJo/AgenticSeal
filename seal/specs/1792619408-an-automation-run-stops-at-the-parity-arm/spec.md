# Feature Specification: an automation run stops at the parity arm

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The goal a design is chosen against* | Between two designs that catch the same defect, the one that stops to ask a person is the more expensive. The defect the parity arm catches is a code commit nobody compared with the original; this work keeps that catch where the root is in the tree and CI runs this release's check, and removes the stop. S13 names where it does not |
| `CLAUDE.md` *The rule a mechanism is kept against* | The commit-time parity arm on a chain-declared branch is weighed for what it catches. Its only satisfying event in a chain run, the warden's comparison, comes after the commits it gates (`agents/warden.md` *Order of work* step 5; `agents/smith.md` *Order of work* step 6), so on that branch it catches nothing the review does not, and it costs the run |
| `docs/the-review-and-parity-arms.md` *Parity arm* | What the arm protects: a commit that changes code carries a record that the original was consulted, and the mark says a comparison was recorded, not that it was a good one |
| `docs/the-review-and-parity-arms.md` *The declaration, and where the check went* | The review arm's precedent: a declaration moves the check to the pull request, the waiver stays per command, and there is no standing waiver. This work applies the same move to the parity arm under one answer |
| `docs/the-review-record.md` *What the check reads at the pull request* | `chain_check.py` is the reader at the pull request, and a check gates only a fact it reads. The comparison has to be a line in a committed record for CI to see it; the parity mark under the git directory is not |
| `docs/the-review-record.md` *The round record* | The grammar table is the one source of every labelled line's shape, and `chain_check.py` loads it from this file at run time (`skills/code-review/scripts/chain_check.py#grammar`, `GRAMMAR_DOC`) |
| `docs/the-review-record.md` *The run* | Under `Automation` `yes` no person is asked mid-run, and the commit gate's refusal under the press says to hand the commit back at the end of the run (`hooks/gate.py#AUTOMATION`) |
| `skills/legacy-parity/SKILL.md` *Recording the comparison* | The parity mark is written by the party that compared and whose definition names the write: the warden in a review round, the orchestrator where it compared with no review round. The scribe and the smith write none |
| `skills/legacy-parity/SKILL.md` *The migration config* | A comparison against a guessed original proves nothing, which is why the new line names the migration config's baseline and the check compares the two |
| `agents/scribe.md` *Never* and `skills/agent-contract/SKILL.md` §6 | The scribe writes nothing durable, and no agent spawns another, so the smith cannot obtain a scribe comparison of its own |
| `skills/implement/orchestration.md` *Question 2* | The question is at its four-box cap, so no new routing question or box is available for a parity answer |

## Scope

**In.**

1. **The commit gate's parity arm is silent on a branch whose `routing.md`
   declaration answers `Review` with `through the review chain`.** Both
   readings change together, because both ask `hooks/gate.py#arms_missing`:
   `pre-commit` and `reference-transaction` inside git, and the PreToolUse
   reading in `hooks/commit-review-gate.py`.
2. **`chain_check.py` owes an `original:` line in every round record of such
   a work item**, where `seal/parity.md` exists at HEAD and the pull
   request's diff against its base touches a path outside `docs/` and
   `seal/`. The line names the migration config's `Baseline commit`, and a
   line naming any other commit is refused.
3. **The warden writes that line** in each round, after comparing that
   round's target with the original through `legacy-parity`, beside the
   parity mark it already writes.
4. **Every sentence that states the old fact is rewritten in place**: the
   wake/quiet table in `skills/implement/orchestration.md`, the sentence in
   `skills/implement/SKILL.md`, `legacy-parity`'s *Recording the comparison*,
   `templates/sdd-round.md`, the gate's docstring and the README rows, with
   the `docs/` sentences carried in `## Rule changes` below.

**Out, each with its reason.**

- **The `straight to the PR` answer.** The parity arm stays at the commit
  under that answer, as it is today, because no review round exists there to
  record a comparison. This is `questions.md` Q1, and the build proceeds on
  that default.
- **Removing the commit-time parity arm, its mark and `[no-parity]`
  altogether.** An undeclared commit in a migration repository (question 1's
  `no work item` answer) has no pull-request check that reads it, so the
  visible waiver in history is the only trace that nobody compared. `plan.md`
  *Alternatives considered* row G weighs it.
- **A per-phase comparison written by the smith or recorded before each
  commit.** The builder certifying its own comparison is the self-review the
  review arm's two answers exist to refuse, and the mark is per HEAD, so a
  phase of several commits would need a fresh one before each. `plan.md`
  rows C and D.
- **A new routing row or box for parity.** `seal/parity.md` already declares
  the migration, so a row would state the same value twice, and question 2
  has no room. `plan.md` row F.
- **The parity mark on a chain-declared branch.** The warden keeps writing it:
  it is what quiets the arm on an undeclared branch the same clone may
  commit on, and the review mark is kept on exactly these terms
  (`skills/implement/orchestration.md` *Orchestrator: which of these acts
  runs itself*, the row *Orchestrator: closing the cycle*).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given a repository with `seal/parity.md` and a `routing.md` naming the branch with `through the review chain`, when a code-touching commit is made with no parity mark at HEAD, then neither reading of the commit gate stops it, attended or under the `automation` press | a case through `hooks/gate.py#arms_missing`, one through `pre-commit`, and one through the PreToolUse reading, each seen red against the tree as it stands |
| S2 | Given the same repository and a declaration answering `straight to the PR`, when the same commit is made, then the parity arm stops it as today: the attended text offers the two parity options, and under the press the text names `git -c specseal.waive=parity commit …` and the hand-back | the rewritten `tests/test_routing_is_recorded.py` cases, and `tests/test_an_automation_run_meets_no_commit_prompt.py#test_a_parity_stop_under_the_press_is_refused_too` unchanged and green |
| S3 | Given the same repository and no declaration naming the branch, when the same commit is made, then the parity arm stops it as today | the existing parity cases in `tests/test_chain_hooks_hardening.py`, green. The 26 cases that declared `through the review chain` only to quiet the review arm, one in `tests/test_chain_hooks_hardening.py`, 24 in `tests/test_no_shape_the_base_stops_reads_silent.py` and one in `tests/test_the_commit_gate_decides_at_the_commit.py`, declare `straight to the PR` instead, where the parity arm still stands at the commit; `phases/phase-2.md` names them |
| S4 | Given a chain-declared work item in a repository with `seal/parity.md`, whose pull request changes a path outside `docs/` and `seal/`, when a round record holds no `original:` line, then a ready pull request fails with a refusal naming that record, and a draft prints the same line and exits 0 | a `tests/test_chain_check.py` case marked `@pytest.mark.rule("parity-at-the-pull-request")` |
| S5 | Given S4's work item, when every round record holds `original: <commit>` and the commit is a prefix of the `Baseline commit` row's SHA, or that SHA is a prefix of it, then this refusal does not fire | a case beside S4's |
| S6 | Given S4's work item, when a round record's `original:` names another commit, then the ready pull request fails naming the record and both commits | a case beside S4's |
| S7 | Given S4's repository, when the pull request's diff is confined to `docs/` and `seal/`, then no `original:` line is owed | a case beside S4's |
| S8 | Given a repository with no `seal/parity.md`, when a chain-declared pull request changes code, then no `original:` line is owed and every existing `tests/test_chain_check.py` case stays green | the module's narrow run |
| S9 | Given S4's work item, when an `original:` line stands inside a finding, appears twice in one record, or is spelt `Original:`, then it is refused at its line as the grammar table's row says | cases beside S4's, reading the row from `docs/the-review-record.md` |
| S10 | Given S4's work item, when `seal/parity.md` has no `Baseline commit` row whose value holds a SHA, then the ready pull request fails naming `seal/parity.md` | a case beside S4's |
| S11 | Given S4's work item, when the paths the pull request changes cannot be read, then no pull request passes: `chain-check` itself exits 2 at `cannot diff against <base>` before it judges any record, and `chain_check.py#originals_of`, given no paths, owes the line, as `hooks/gate.py#touches_code` decides for paths git could not list | a case at `originals_of` with the paths None; the command's exit 2 is its existing behaviour, so no run of the command reaches the parity refusal with an unreadable diff |
| S12 | The wake/quiet table in `skills/implement/orchestration.md` *Orchestrator: how the work is routed* states the parity arm's new quiet condition and the `straight to the PR` case, and no file in the tree still says a declaration reaches the review arm only | the warden reads the table against this spec; `git grep -n -i 'review arm only'` and `git grep -n 'does not silence the'` return nothing outside `seal/specs/` and `changelog/` |
| S13 | The issue's done-when: an `automation` run in a repository with `seal/parity.md` reaches its pull request with no question to a person, and a code commit with no recorded comparison is still refused at a place CI or a person sees. That place exists where the root is in the tree and the repository's `.github/workflows/hygiene.yml` pins this release or a later one: in local mode no pull-request check reads the round records, and the Parity arm `add` operation of `## Rule changes` states that limit with the other two | S1 for the first half; S4, S2 and S3 for the second |

## Data & interfaces

**The `original:` line.** A new row of the grammar table in
`docs/the-review-record.md` *The round record*:

| Line | Shape | Where | How many | Refused as |
|---|---|---|---|---|
| `original:` | `original: (?P<commit>[0-9a-f]{7,40})` | outside every finding | at most one | it names the migration config's baseline commit this round compared against, as 7 to 40 hex digits |

`How many` is `at most one` in the table because the line is owed only
where `seal/parity.md` is declared and the change touches code; the
refusal of S4 is what makes it required there. The row, and the sentence
under the table that names each row the loader reads a meaning from, are
edited into `docs/the-review-record.md` in the build commit that adds the
reader, not through `## Rule changes`, because `chain_check.py` loads the
table from that file when it runs. The reader lists `original:` in
`chain_check.py#READ_ROWS` at `outside every finding` and `at most one`, so
a table that moves the row or drops its `(?P<commit>...)` part is refused
with exit 2, and that sentence says `original:` stands there and is `at
most one`. #1000 did the same with its old-spellings table (commit
`ebbbd2f0`, its phase 3 subject, `read`).

**Where the doc-root rule lives.** `hooks/gate.py#DOC_ROOTS` and
`hooks/gate.py#touches_code` are the one home of *a change confined to
`docs/` and `seal/`*. `chain_check.py` reads them from there rather than
holding a copy; how it loads them is the build's choice.

**Where the baseline is read.** `seal/parity.md` is written from
`templates/parity.md`, a `| Field | Value |` table whose `Baseline commit`
cell holds the SHA in its first code span. No reader of that row exists
today (`git grep -n 'Baseline commit' -- hooks skills .github bin` returns
only `skills/implement/orchestration.md:249`, `executed`). The build adds one
reader, in `hooks/config.py` beside the table walker it uses, and
`chain_check.py` calls it. `questions.md` Q2 records that choice as the
work's.

**The gate's condition.** In `hooks/gate.py#arms_missing` the parity arm
gains one more conjunct: no declaration from `routing.declared(cwd, top)`
whose `review` is `routing.CHAIN`. The declaration is already read once for
the review arm, and the build reads it once for both.

## Rule changes

- change
  file: docs/the-review-and-parity-arms.md
  section: The two arms of the commit gate
  from: The two arms are evaluated independently: each has its own mark, waiver token
    and silence, and one satisfied never quiets the other.
  to: The two arms are evaluated independently: each has its own mark, waiver token
    and silence, and one arm's mark never quiets the other. A routing
    declaration answering `through the review chain` quiets both arms at the
    commit, and each arm's check then moves to the pull request.
- change
  file: docs/the-review-and-parity-arms.md
  section: The review and parity arms
  from: the routing declaration that moves the review arm's check
    to the pull request.
  to: the routing declaration that moves the review arm's check, and under
    `through the review chain` the parity arm's, to the pull request.
- change
  file: docs/commit-review-gate-spec.md
  section: The PreToolUse reading of a commit
  from: each with its own mark, waiver
    and silence, and one arm satisfied never quiets the other.
  to: each with its own mark, waiver
    and silence. One arm's mark never quiets the other, and a routing
    declaration answering `through the review chain` quiets both arms at
    the commit.
- change
  file: docs/README.md
  section: docs/
  from: | `docs/the-review-and-parity-arms.md` | what each opt-in arm of the commit gate wants, and the routing declaration that moves the review arm's check to the pull request |
  to: | `docs/the-review-and-parity-arms.md` | what each opt-in arm of the commit gate wants, and the routing declaration that moves the review arm's check, and under `through the review chain` the parity arm's, to the pull request |
- change
  file: docs/the-review-and-parity-arms.md
  section: Parity arm
  from: | `[no-parity]` in the command, placed as the review arm's waiver is | silent, and visible in history |
  to: | `[no-parity]` in the command, placed as the review arm's waiver is | silent, and visible in history |
    | a `routing.md` declaration names this branch and answers `through the review chain` | silent: every round record carries the comparison, and CI checks it at the pull request |
- add
  file: docs/the-review-and-parity-arms.md
  section: Parity arm
  to: **A declaration answering `through the review chain` moves the parity
    arm's check to the pull request, and one answering `straight to the PR`
    leaves it at the commit.** In a review chain the warden compares the
    change with the original after the smith has committed it, so the arm
    could meet a build commit only with a waiver, and under the
    `automation` press it stopped every run at the first code commit. The
    comparison the chain does make is recorded in each round record, where
    CI reads it, and what the check reads is `docs/the-review-record.md`
    *What the check reads at the pull request*. Under `straight to the PR`
    no review round records a comparison, so the arm stays at the commit as
    the table above states, and under the press a code commit there is
    refused and handed back at the end of the run. A branch that declares
    the chain and never opens a pull request is checked by nothing, which is
    the cost the review arm's declaration already states. Three more shapes
    leave code nobody compared with nothing that reads it. In local mode the
    root sits under the common git directory and nothing under it is
    committed, so no pull-request check reads a round record, the cost the
    review arm's declaration already carries there. A repository whose
    `.github/workflows/hygiene.yml` pins a plugin release older than this
    rule runs a `chain-check` that reads no `original:` line, until a person
    moves the pin's `v<version>` to the installed release. And a declaration
    rewritten from `through the review chain` to `straight to the PR` after
    code was committed leaves those commits compared by nobody, because the
    check reads the answer at HEAD.
    check: parity-quiet-under-the-chain
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: **`chain_check.py` reads the declaration, the frame, the records, the broad
    gate's file and the sealer's guarantee, and nothing else of a round record.**
  to: **`chain_check.py` reads the declaration, the frame, the records, the broad
    gate's file, the sealer's guarantee and, where `seal/parity.md` is
    declared, the migration config's `Baseline commit`, and nothing else of
    a round record.**
- add
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  to: **Where `seal/parity.md` is declared and the change reaches outside
    `docs/` and `seal/`, every round record of a work item declaring
    `through the review chain` carries one `original:` line naming the
    migration config's baseline.** The check reads `seal/parity.md` at HEAD
    and the paths the pull request changes against its base, through the
    parity arm's own rule for a change confined to the document roots. A
    diff it cannot read ends the check with exit 2 before any record is
    judged. A ready pull request fails while a round record holds no
    `original:` line, or holds one whose commit and the
    `Baseline commit` row's SHA are not one a prefix of the other, and a
    migration config whose `Baseline commit` holds no SHA fails it too. Each
    refusal names the record, or the config, and both commits where two are
    compared. The warden writes the line in the round where it compared that
    round's target with the original through `legacy-parity`. A round that
    could not resolve the original writes no line and raises an `unread`
    finding, so the refusal stands until a round compares. What the check
    cannot read is whether the comparison was a good one, which is the
    warden's, as it is for the parity mark.
    check: parity-at-the-pull-request

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the sentence that a declaration reaches the review arm only and a migration repository still meets the parity arm on a code-touching commit | `skills/implement/orchestration.md` *Orchestrator: how the work is routed* | rewritten in place, with the wake/quiet table's parity cell, to the new quiet condition and the `straight to the PR` case |
| the sentence "A declaration does not silence the parity arm" and its grounds | `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* | rewritten in place: a chain declaration quiets it, and the wake/quiet table stays the one place that states the cases |
| the sentence that committing code with no comparison record makes the gate ask | `skills/legacy-parity/SKILL.md` *Recording the comparison* | rewritten in place: it asks on an undeclared branch and under `straight to the PR`, and a chain round records the comparison on its `original:` line |
| the case that a chain declaration does not waive the parity arm | `tests/test_routing_is_recorded.py#test_the_declaration_does_not_waive_the_parity_arm` | rewritten to a `straight to the PR` declaration, where the arm still stands; S1's new cases pin the chain answer |
| the case that the parity arm gains no third way under a chain declaration | `tests/test_routing_is_recorded.py#test_the_parity_arm_gains_no_third_way` | rewritten to a `straight to the PR` declaration, where its property, that the review arm's sentence does not ride on the parity prompt, still holds |
| the docstring clause that the parity arm stands whenever the mark does not name HEAD | `hooks/gate.py` module docstring, the *The two arms* list | rewritten in place to name the chain declaration |
| the clause telling the model that a declaration "silences NOTHING ELSE" | `hooks/commit-review-gate.py`, the review arm's option for writing a declaration | rewritten in place to say a declaration answering `through the review chain` silences the parity arm too, and pinned |
| the README rows saying a migration config makes every code commit meet the parity arm | `README.md` *The gates*, the `commit-review-gate` row, and `README.ko.md`'s matching row | rewritten in place to name the declaration that quiets it |

The `docs/` sentences that change are the operations of `## Rule changes`
above and are not removed by the build, with one exception: the grammar
table's `original:` row and the sentence under that table, which the build
edits with their reader (*Data & interfaces*).

## Open questions

Anything a planner must answer lives in questions.md, not inline: unanswered
questions buried in prose read as decided.

Framed 2026-10-22 by framer, before the build.
