# Feature Specification: the pull request check parses each spec's rule changes (#1006)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md holds WHAT this work
delivers and how we'll know. The policy documents in docs/ outrank this file;
the framer cites them and does not restate them. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-review-record.md` *What the check reads at the pull request*, first rule | Which work items the check judges: the `routing.md` naming the pull request's branch and every one the pull request's own commits add or change. A ready pull request fails on any refusal, named `path:line  why`; a draft, or a run that observed no pull request, prints the same lines and exits 0. The new read takes this scope and this strictness unchanged |
| `docs/the-review-record.md` *What the check reads at the pull request*, rule *An item is judged at the pull request that carries it* | A work item a squash of another pull request carried was judged there. Its `spec.md` is read at that pull request and not again |
| `skills/settle/SKILL.md` *Rule changes* | The grammar, and `skills/settle/scripts/rule_changes.py` as the one reader of the section. A block that does not match whole is refused at its line |
| `skills/settle/SKILL.md` *What `--apply` does* | A spec whose section does not parse applies nothing. A spec with no `## Rule changes` is named and stays, so the check leaves it alone too |
| `CLAUDE.md` *The goal a design is chosen against* | The refusal reads a fact from a file and puts no question to a person |
| `CLAUDE.md` *The rule a mechanism is kept against* and `CONTRIBUTING.md` *What a change to a gate must carry* | The pull request states the failure direction (it blocks more), the prompt budget (none) and what the change removes (see `## Removes`). The issue states all three, and the pull request body copies them |
| `docs/the-review-and-parity-arms.md` *The declaration, and where the check went* | Its table states what each `Review` answer owes at the pull request. The new read is owed under either answer, as the frame arm is, and the table names neither, so the table is not changed |

## Scope

**In.**

1. `skills/code-review/scripts/chain_check.py` reads the `spec.md` of every
   work item whose `routing.md` it judges, and parses that file's
   `## Rule changes` section with `rule_changes.parse`, reached through the
   shared reader's loader `skills/verify/scripts/unverified_check.py#rule_changes`.
   The policy root it passes is `unverified_check.py#policy_root` of the
   repository, the value `settle` passes.
2. Each error the parser returns becomes one refusal, at the spec's path and
   the line the parser names, carrying the parser's reason verbatim. Its text
   is in *Data & interfaces*.
3. The refusal is judged like every other refusal of the check. It fails a
   ready pull request, prints and exits 0 on a draft, and stays a refusal
   under `--sealing`, so the orchestrator's `broad-gate` run and its
   `--preflight` meet it before the sealer is spawned.
4. These are left alone, as `settle` leaves them: a `spec.md` with no
   `## Rule changes` section, a section holding the no-change block, a work
   item with no `spec.md`, and a work item whose declaration a settle removed.
   The last two have no spec to read.
5. The prose that lists what the check reads is corrected in place in the
   same commit: `chain_check.py`'s module docstring, the comment above the
   chain step in `.github/workflows/hygiene.yml`, the same comment in
   `templates/hygiene.yml`, and one pointer sentence in
   `skills/settle/SKILL.md` *Rule changes*. The policy root's statement of
   the rule is `## Rule changes` below, applied by `settle` after the
   release.

**Out, each with its reason.**

- **Replaying the operations at the pull request**, to find a `from:` text
  or a `section:` that is not in its document. Whether a `from:` text is
  there at the settle depends on the specs merged before this one, in an
  order the pull request does not fix yet. `settle`'s dry run answers it
  after the release, and issue #1006 asks for the parse alone.
- **A `spec.md` the diff carries for a work item the check does not judge.**
  Every work item commits its `routing.md` before the first edit, so a work
  item's own `spec.md` is always beside a judged declaration. A `spec.md`
  edited by a commit that belongs to no work item is the remaining case, and
  reading it would make the check fail a pull request that declared nothing,
  which `.github/workflows/hygiene.yml`'s comment and `CONTRIBUTING.md`
  promise it never does. `plan.md` A2 weighs it.
- **Refusing a new `spec.md` that has no `## Rule changes` section.** Issue
  #1006 item 3 leaves it alone, and `settle` names it and keeps it. Whether
  a spec added after the template gained the section owes one is a decision
  for the owner, and `questions.md` Q1 holds it.
- **Renaming the hygiene step** *a declared review chain has the round record
  it claimed*. `skills/verify/scripts/broad_gate.py` holds the step's name in
  its partition, and a case holds the two equal. The name still describes the
  step's main arm, and a rename moves three files for no reader.

## User scenarios & acceptance *(mandatory)*

Every case below goes into `tests/test_chain_check.py`, carries
`@pytest.mark.rule("rule-changes-read-at-the-pull-request")`, and builds on
the module's `branch` fixture, whose work item is declared `through the
review chain` and reviewed to HEAD. A case that expects a refusal is seen
red against `chain_check.py` as it stands at the frame commit, where `main`
returns 0 for it.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a value continued two spaces in | Given the work item's `spec.md` whose no-change block's `why:` continues on a line indented two spaces, committed, on a ready pull request, when the check runs, then it exits 1 and prints one line naming `<item>/spec.md`, the line `rule_changes.parse` names, and the parser's reason | a case comparing the printed line with `rule_changes.parse` run on the same text, so the reason is not spelt a second time in the test |
| S2 prose under the items | Given a `spec.md` whose section holds a `change` item and a prose paragraph under it, when the check runs on a ready pull request, then it exits 1 at the paragraph's line with the parser's reason | a case, as S1 |
| S3 a section that is only the template's comment | Given a `spec.md` whose `## Rule changes` holds only the template's comment, when the check runs on a ready pull request, then it exits 1 with the reason `the section is empty` | a case, as S1 |
| S4 what parses passes | Given, in turn, a `spec.md` with the no-change block, one with a `change` item that parses, and one with no `## Rule changes` section, when the check runs on a ready pull request, then it exits 0 and prints no line naming the spec | a parametrized case |
| S5 a draft prints | Given S1's spec on a draft pull request, when the check runs, then it exits 0 and prints the same line as a notice | a case with the module's `draft` fixture |
| S6 the broad run meets it | Given S1's spec on a ready pull request, when the check runs with `--sealing`, then it still exits 1 | a case |
| S7 either planning answer | Given S1's spec under a declaration whose `Planning` row reads `the session`, when the check runs on a ready pull request, then it exits 1 | a case; the `branch` fixture already declares `the session` |
| S8 carried by a squash | Given a work item with S1's spec that reached the branch inside another pull request's squash (the module's `squash` helper), when the check runs on a ready pull request, then no line names that spec | a case beside `TestCarriedBy` |
| S9 the working tree | Given S1's spec written and not committed, when the check runs with `--worktree`, then it exits 1 naming the spec | a case |
| S10 a reader that will not load | Given `unverified_check.rule_changes` raising when called, when the check reaches a judged work item, then it exits 2 and stderr names the reader | a case with the loader monkeypatched |
| S11 the importers are untouched | Given `hooks/commitgate.py`, `skills/verify/scripts/seal_stamp.py`, `skills/verify/scripts/broad_gate.py` and `.github/scripts/release_seal.py`, which import `chain_check.py`, when they import it, then nothing new loads at import | read by the warden at review: the parse is reached from `main` alone |

## Data & interfaces

- **`chain_check.py#rule_changes_read(reader, root, item)`**, new, returns
  `[(path, line, problem)]` as `records` and `broad_gate` do. It reads
  `<item>/spec.md` through `read_record`, so `--worktree` reads the disk and
  CI reads HEAD. A spec that is not there returns `[]`. Otherwise it returns
  one entry per error of
  `reader.rule_changes().parse(text, reader.policy_root(root))`.
- **`main`** calls it once per judged declaration, after `routing.parse` has
  read the declaration and beside `frame`, and adds its entries to
  `problems`, never to the `--sealing` notices. A declaration that is
  carried, retired by a settle, or unreadable reaches no call, because
  `main` already moves on from each of those before `frame`.
- **The refusal's text** is one constant, `RULE_CHANGES_SAYS`, formatted with
  the parser's reason:

  ```
  `## Rule changes` does not parse, and `settle` applies nothing from this spec: {reason}
  ```

  Printed through `reader.annotate`, it reads
  `<item>/spec.md:<line>  ` followed by that text outside CI, and a GitHub
  annotation at that line in CI.
- **Loading.** `unverified_check.py#rule_changes` loads
  `skills/settle/scripts/rule_changes.py` by path once and caches it; that
  loader already serves `settled`, which `chain_check.py#retired` asks. No
  second loader is written. Where the call raises, `main` prints
  `chain-check: the rule-changes reader would not load (<exception>)` to
  stderr and returns 2, as it does for `hooks/routing.py`.
- The parser returns at its first error, so one spec yields at most one
  refusal.

## Rule changes

- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: reads the declaration, the frame, the records, the broad gate's file
    and the sealer's guarantee, and nothing else of a round record.**
  to: reads the declaration, the frame, the `## Rule changes`
    section of each judged work item's `spec.md`, the records, the broad
    gate's file and the sealer's guarantee, and nothing else of a round
    record.**
- add
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  to: **The check parses the `## Rule changes` section of the `spec.md` of
    every work item whose `routing.md` it judges, with
    `skills/settle/scripts/rule_changes.py`, the one reader of that
    section, and a section the reader refuses is a refusal at the line the
    reader names, carrying the reader's reason.** `settle` reads the
    section after the release and applies nothing from a spec whose
    section does not parse, so a section first read there is a rule
    change that never lands, with no pull request left to fix it in. The
    check reads no other `spec.md`, so a work item a squash of another
    pull request carried is read at that pull request. A `spec.md` with
    no `## Rule changes` section is left alone, as `settle` leaves it. The
    refusal reads a fact from the file and puts no question to a person.
    check: rule-changes-read-at-the-pull-request

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the count of the check's arms, and its arm list without the spec read | `skills/code-review/scripts/chain_check.py#__doc__` (the sentence *The arms are five:* and the list under it) | rewritten in place: the list gains the read of each judged work item's `## Rule changes`, and the count names six |
| the list of what the chain step fails for, without the spec read | `.github/workflows/hygiene.yml` (the comment above the step *a declared review chain has the round record it claimed*, its sentence opening *It fails for what the author can fix*) | rewritten in place: the list gains a `spec.md` whose `## Rule changes` does not parse |
| the same list in the copy that ships to user repositories | `templates/hygiene.yml` (the comment above the same step, its sentence opening *It never fails a pull request that declared nothing*) | rewritten in place, as the row above |
| the first rule's list of what the check reads | `docs/the-review-record.md` *What the check reads at the pull request* (the bold sentence opening *`chain_check.py` reads the declaration*) | the `change` item in `## Rule changes`, applied by `settle` after the release; the pull request leaves the policy root as it is |

## Open questions

Anything a planner must answer lives in questions.md, not inline: unanswered
questions buried in prose read as decided.

Framed 2026-10-22 by framer, before the build.
