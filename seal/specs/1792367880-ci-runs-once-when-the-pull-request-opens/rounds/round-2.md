# 1792367880-ci-runs-once-when-the-pull-request-opens — review round 2

target: 83c2c6c6, fixes 46a9bbe3..83c2c6c6

## Findings

This round opens no finding. It read the fix diff `46a9bbe3..83c2c6c6` and
nothing outside it, except the coordinates named below. The three closes
of round 1 hold. Of the three cuts to the sealer's definition, none takes a
rule the sealer acts on. The inverted §6 case is sound for what it guards,
with the limit stated under its entry.

## Confirmations

confirms: round-1#1
The close holds. Read at `95ab5fd0`:

- The framer route's label step is gone from
  `skills/code-review/orchestration.md:150-154`. So is its policy paragraph,
  at `docs/issues-and-milestones.md:183-186`.
- A `git grep` for `chain: reframed` outside `seal/specs/` finds only the
  0.19.0 changelog's history line.
- No workflow or script reads the label. `.github/scripts/release_seal.py`
  reads `chain: capped` alone. The removal stands on the paragraph's own
  words, "nothing reads it", and on `CLAUDE.md` §*The rule a mechanism is
  kept against*.
- The stated limit now says the pull request stays open through its repair
  and gets a repaired body by `gh api -X PATCH`
  (`skills/code-review/orchestration.md:182-186`). The records-only repair
  sentence points there (`:230-231`).
- `agents/sealer.md:35-36` adds "or is given it where already open".

Executed, by `mutation-check` at `83c2c6c6`, each red:

- the spawn sentence set back to "the pull request";
- the PATCH command set to `gh pr edit`;
- the sealer's new clause deleted.

The first two ran against `tests/test_the_rules_have_one_owner.py`, the
third against `tests/test_the_sealer_guarantees.py -k spawned_before`.

confirms: round-1#2
The close holds. Read: the build-and-review push is conditioned on
`Destination` reading `open the pull request`, and `stop before the pull
request` hands the branch back unpushed
(`skills/code-review/orchestration.md:159-163`). The platform step names
the risk in the handback and pushes nothing under that answer
(`:174-176`). Both agree with `skills/implement/orchestration.md:327` and
`:447`, which the fix left as they stood. Executed:
`mutation-check` of `:160` back to an unconditioned "Push" went red against
`tests/test_the_rules_have_one_owner.py`. The case pinning the three
sentences is unique in that module: no other case reads `Destination`
there.

confirms: round-1#3
The close holds. Executed, at `83c2c6c6`: the two round-1 mutations
re-run here went red against `tests/test_the_rules_have_one_owner.py`.
They are the spawn sentence (`:203-204`) and the `ready_for_review` clause
(`:190-191`), both of which survived at `3ba50b9f`. The other three were
not re-run in this round. Read: the new case holds those three, the
"written to a file" clause, `--body-file <that file>` and
`docs/the-broad-gate.md:5`, as plain assertions
(`tests/test_the_rules_have_one_owner.py:184-199`). The fix pass reports
seeing each red, a claim this round did not repeat. The new case and the
S8 case in `tests/test_the_sealer_guarantees.py` pin opposite halves of
one exchange, so neither duplicates the other.

confirms: none
The sealer's three cuts remove restatements. Each rule they carried still
reaches the sealer from a source it acts on. Read:

- **The §6 withheld acts** (`agents/sealer.md:29-30`). The sealer's
  definition preloads `agent-contract` (`:11-12`), whose §6 withholds
  posting, pushing, opening a pull request and spawning "whatever a
  definition says". `tests/test_the_agent_contract_holds_the_universal_rules.py:46`
  pins §6's own list. The sentence that bounds the sealer's writes stays
  (`agents/sealer.md:29`, "is the whole of what you may write"), and it is
  the phrase
  `tests/test_every_agent_reads_the_contract.py::test_every_definition_bounds_what_it_writes`
  reads.
- **The broad-gate rule's body** (`:103-105`). "The orchestrator runs it"
  is contract §2. "A missing or stale record is a `withheld` verdict, never
  a run you take in its place" is still stated where the sealer acts on it:
  step 1's `withheld — no broad run at HEAD` and "Nothing broad is run in
  its place" (`:60-62`), and `## Never`'s first line (`:88-89`).
- **The description's verdict list** (`:4-9`). Step 5 still names the three
  verdicts (`:78-80`). The description is what a spawner reads to know when
  to spawn, and it still says that.

Executed: `tests/test_the_sealer_guarantees.py`,
`tests/test_every_agent_reads_the_contract.py`,
`tests/test_broad_gate_rule.py` and `tests/test_the_rules_have_one_owner.py`
passed, 88 with 2 skipped. `tests/test_the_seal_is_taken_once_by_the_sealer.py -k "sealer or document"`
passed, 373. `tests/test_docs_line_wrap.py -k "orchestration or sealer or issues"`
passed, 4.

confirms: none
Inverting the §6 case is sound. Read: the old case did two jobs. It held
§6's list, which `tests/test_the_agent_contract_holds_the_universal_rules.py:46`
still holds. It also held the sealer's recitation in step with that list,
and the recitation is gone. The inverted case keeps a guard where the
passage stood, following the precedent of
`test_the_window_the_sealer_shipped_under_is_closed`.

Executed: putting the old sentence back verbatim turned
`-k leaves_s6` red. Its limit, also executed: the same acts recited in
other words ("Nothing is posted or pushed, no pull request is opened and no
agent is spawned") survived. The case guards two spellings, so it narrows
the class and does not close it. Its docstring's "A recitation that returns
is a second source" is wider than what the case holds. That costs a reader
nothing, since §6 binds the sealer either way, so this is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Removing the `chain: reframed` policy is a removal neither `spec.md` §*Removes* nor `overview.md`'s divergences names. The changelog fragment names it, and the sealer's step 4 compares those parties | `seal/specs/1792367880-ci-runs-once-when-the-pull-request-opens/overview.md`, `seal/specs/1792367880-ci-runs-once-when-the-pull-request-opens/spec.md` | the orchestrator, before the sealer's spawn |
| Whether the cut sealer clears rule 4 and behaves as before | `agents/sealer.md` | the orchestrator, by the sealer measurement at `95ab5fd0` it is running |
| Round 1's `## Not judged` rows (GitHub's trigger and cancellation behaviour, Q1; `gh workflow run tests` in other repositories) still stand. This verifying round did not reopen them | `seal/specs/1792367880-ci-runs-once-when-the-pull-request-opens/rounds/round-1.md` | as round 1 names them |
| The full suite, the repository-wide lint and the typecheck, which no round runs: `unverified` | the branch at `83c2c6c6` | the orchestrator, by `broad-gate --base release/v0.22.2 --record` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_the_rules_have_one_owner.py tests/test_the_sealer_guarantees.py tests/test_every_agent_reads_the_contract.py tests/test_broad_gate_rule.py -q -p no:randomly` | exit 0: 88 passed, 2 skipped |
| `bin/test tests/test_the_seal_is_taken_once_by_the_sealer.py -q -p no:randomly -k "sealer or document"` | exit 0: 373 passed |
| `bin/test tests/test_docs_line_wrap.py -q -p no:randomly -k "orchestration or sealer or issues"` | exit 0: 4 passed |
| `mutation-check skills/code-review/orchestration.md --replace "the issue and the file holding the pull" "the issue and the pull request; the pull" --tests "bin/test tests/test_the_rules_have_one_owner.py -q -p no:randomly"` | red |
| `mutation-check skills/code-review/orchestration.md --replace $'re-runs it when the draft is marked ready, so the\nrecord is still owed then' "stays where it was"` (the same tests) | red |
| ``mutation-check skills/code-review/orchestration.md --replace '`gh api -X PATCH repos/<owner>/<repo>/pulls/<N> -F body=@<file>`' '`gh pr edit <N> --body-file <file>`'`` (the same tests) | red |
| ``mutation-check skills/code-review/orchestration.md --replace "Where `Destination` reads `open the pull request`, push" "Push"`` (the same tests) | red |
| `mutation-check agents/sealer.md --replace "or is given it where already open." "." --tests "bin/test tests/test_the_sealer_guarantees.py -q -p no:randomly -k spawned_before"` | red |
| `mutation-check agents/sealer.md` putting the removed §6 recitation back verbatim after "before you were spawned.", `--tests "bin/test tests/test_the_seal_is_taken_once_by_the_sealer.py -q -p no:randomly -k leaves_s6"` | red |
| the same, with the four acts recited in other words | SURVIVED, exit 1 |
