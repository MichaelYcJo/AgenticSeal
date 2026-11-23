# Review round 1: 1795406406-code-stands-on-facts-that-no-longer-hold

```seal
target: 909602a0b against origin/release/v0.38.6
```

The diff is `origin/release/v0.38.6...909602a0b`, with the base at `02369a0e9`, which the branch merged at `1e98cc798`. This is round 1, so no earlier record carries a coordinate or a verdict. Every fact below was established in this round, in a `git clone --no-local` of the branch checked out at `909602a0b`, under `<scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-1/clone`. The work item's records were read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md` to `phase-5.md`. No `pr.<lang>.md` stands, and none is owed, since `Commit and pull request language` is English. No `seal/parity.json` is declared.

## Findings

### 1. The gate-change judgment says a U+2705 row still blocks in `seal unverified`, and that command now passes it

```seal
severity: should
location: `seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold/frame/plan.md:68`, `seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold/pr.md:2`
evidence: executed `python3 -I <scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-1/test_tmp_round1_probe.py`; read `skills/verify/scripts/unverified_check.py:34-36`, `skills/verify/scripts/unverified_check.py:271-310`, `lib/gaps.py:251-282`, `seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold/changelog.md:9`
```

Why it matters: `CONTRIBUTING.md` *What a change to a gate must carry* asks the pull request to state whether the change makes each gate block more or allow more. The row on what the change carries is where this pull request answers that, and `pr.md:2` quotes its first sentence into the pull request body.

The row claims two things about a U+2705 row. Its first sentence says the change "blocks more in `seal unverified`", and lists `seal unverified` under neither "allows more". Its grounds then say a `## Not verified` row opening with U+2705 is reported where `lib/gaps.py` refused it, and that "it blocks as before, at a different line".

The probe ran `unverified_check.py` from the base tree and from the target on one closing memo whose only row opens with U+2705. At the base it exited 1, naming the U+2705 edit and printing "1 unreadable". At the target it exited 0 and printed the row as `open`. That is the module's own exit rule: 0 for a readable record, where open items are reported and not punished, and 1 for a section it cannot read (`unverified_check.py:34-36`). So for this input `seal unverified` allows more, where the row says it blocks as before. `changelog.md:9` states the same result as the probe: such a row is reported "rather than failing on it".

What still blocks is `seal settle --apply`. `lib/gaps.py#open_record_rows` keeps a directory with an open row, as it kept one with an unreadable section. The row names `seal unverified`, though, and the wrong allow there is the cost the pull request has to state.

The row and its quote in `pr.md` change together. The quote must stay word for word with the row's first sentence.

```markdown
| 2026-11-23 | What this change to the gates carries: it blocks more in `chain-check` and on two root states of `seal unverified`, allows more on a U+2705 row of `seal unverified`, in `seal settle`'s dry run, the release's finding counts, the release seal and the test censuses, and its prompt budget is zero | ... A `## Not verified` row opening with U+2705 is read as an open row, so `seal unverified` exits 0 and lists it as open where it exited 1 and named the edit: that allows more. A wrong allow there reports as open a row that its writer meant as closed, and `seal settle --apply` still keeps the work item's directory for it, as it kept the directory for the unreadable section before. ... | `CONTRIBUTING.md` *What a change to a gate must carry* |
```

The `...` marks stand for the cell's other sentences, which stay as written. `pr.md:2` takes the new first sentence of the Judgment cell, word for word, in place of the old one.

```seal
verdict: fixed b81c42b3c
answer: The finding holds. The row's first sentence now says the change allows more on a U+2705 row of `seal unverified`, and its grounds give the exit 1 to exit 0 the probe measured and what a wrong allow there costs; `pr.md` quotes the new first sentence word for word. The fix touches the work item's records alone, so the sealer reads it.
```

### 2. The gate-change judgment does not say what the changed readers read

```seal
severity: should
location: `seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold/frame/plan.md:68`
evidence: read `CONTRIBUTING.md` *What a change to a gate must carry*, `seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold/frame/plan.md:68`, `lib/fields.py:188-196`, `lib/items.py:30-33`, `lib/gaps.py:164-185`
```

Why it matters: `CONTRIBUTING.md` *What a change to a gate must carry* has a bullet, *What it reads*. A pull request that changes a gate names the form the gate reads and the line the gate names as not read. It also names the agent and the step that judge what the same text means.

This change narrows three readers, each a gate's. `chain-check` now reads a `confirms:` line only as `round-<N>#<n>` and refuses `none` at its line (`lib/fields.py:188-196`). `lib/items.py#unread_block` no longer names a `- none` first line as a near miss of `- nothing` (`lib/items.py:30-33`). `seal unverified` reads a U+2705 row as an open row (`lib/gaps.py:164-185`).

The row covers the failure direction, the prompt budget, the platform and what is removed. It says nothing for *What it reads*, so the pull request body says nothing either. The cases at each edge exist: `tests/lib/test_fields.py#test_refuses_confirms_none_at_its_line`, the `none` entries of `tests/lib/test_items.py#Test_unread_block`, and the two U+2705 rows of `tests/lib/test_gaps.py#Test_parse_section`. Only the statement is missing.

Add a sentence to the grounds cell of the same row, beside the direction sentences:

```markdown
What each changed reader reads: `chain-check` reads a confirmation block's `confirms:` line in the one form `round-<N>#<n>` and refuses any other value at its line, `none` among them, and the proofer judges whether a line written otherwise meant a confirmation. `lib/items.py#unread_block` names as not read a first line that opens with `nothing` in any case, and no longer a `- none` line, which the section's refusal still meets; the settling session reads what such a line meant. `seal unverified` reads a row's first word, and only the word `closed` closes it, so a U+2705 row is an open row; the settling session judges whether its writer meant it closed. The edges are held by `tests/lib/test_fields.py#test_refuses_confirms_none_at_its_line`, `tests/lib/test_items.py#Test_unread_block` and `tests/lib/test_gaps.py#Test_parse_section`.
```

```seal
verdict: fixed b81c42b3c
answer: The finding holds. The grounds cell now carries the sentence the finding gave on what each changed reader reads, who judges its meaning, and the cases at its edges. The fix touches the work item's records alone, so the sealer reads it.
```

### 3. Two statements still say a left workflow's checks examine nothing, which this change corrected in `seal.py`

```seal
severity: should
location: `skills/implement/scripts/seal.py:1736`, `tests/skills/test_seal.py:2746`, `tests/skills/test_seal.py:2794`, `templates/setup/hygiene.yml:17-20`
evidence: executed `git grep -n -e 'examines nothing' -e 'examine nothing'` at `909602a0b`; read `skills/implement/scripts/seal.py:1847-1856`, `skills/implement/scripts/seal.py:2416-2421`, `skills/code-review/scripts/chain_check.py:1935-1940`, `docs/checks/the-pull-request-check.md:136-144`, `docs/checks/the-routing-check.md` *At the pull request*, `seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold/trail/phases/phase-3.md:11`
```

Why it matters: phase 3 rewrote `seal.py#remove_workflow`'s docstring and the comment in `#mode`'s `--check` branch. They had said that every step of a left workflow "examines nothing". The phase gave the reason in `trail/phases/phase-3.md:11`: the review-chain step still judges the commit trailers, so "reads no routing declaration" is what holds. `chain_check.py#ROOT_LEFT_SAYS` says the same at `chain_check.py:1935-1940`: "the review-chain check judged the commit trailers and nothing else". So does the rule over `check: nothing-declared-nothing-owed` in `docs/checks/the-pull-request-check.md`.

Two other statements of the same claim stand unchanged:

- `seal.py:1736`, the line `seal mode local` prints to a person: `.github/workflows/hygiene.yml stays: in local mode its checks examine nothing and pass`. `tests/skills/test_seal.py:2746` pins it, and `:2794` asserts that the older-pin message does not contain `examine nothing`.
- `templates/setup/hygiene.yml:17-20`, the header every user repository's copy carries: "There every step examines nothing and passes".

`skills/agent-contract/SKILL.md` rule 19 says the commit that corrects a fact also corrects the other sentences that state it. Phase 3's search of its rule's words, which it called a sample, did not search `examines nothing`, so it missed both statements. Each now says something the tree's own rewritten docstring contradicts. The printed line is a message a person reads (rule 14), so the message and its pinning case change in one commit.

```python
# skills/implement/scripts/seal.py, left_workflow_line
        return (
            f"{WORKFLOW} stays: in local mode its checks read nothing as "
            "declared and pass, and `seal pr-checks remove` takes them out"
        )
```

```python
# tests/skills/test_seal.py, the case at :2744-2747
        assert (
            "  .github/workflows/hygiene.yml stays: in local mode its checks "
            "read nothing as declared and pass, and `seal pr-checks remove` "
            "takes them out\n"
        ) in out
# and the case at :2794
        assert "read nothing as declared" not in out, out
```

```yaml
# templates/setup/hygiene.yml, lines 17-20
# `seal mode` moves the root and leaves this file alone, so a copy can stay
# after a switch to local. There every step passes: no `seal/` is in the
# tree, so the review-chain step reads nothing as declared and judges the
# commit trailers alone, and the mode step finds no root to disagree with.
# `seal pr-checks remove` takes the copy out.
```

The snippet stops at these three files. The search covered `docs`, `CONTRIBUTING.md`, the READMEs, `skills` and `templates` and found no other statement, but a statement in other words is outside what a search on these words reaches. `CONTRIBUTING.md` says the template has to tell the same story as `.github/workflows/hygiene.yml`. That file holds no such header, so it needs no change.

```seal
verdict: fixed f6551bb0d
answer: The finding holds, and the paste-ready fix was applied as read against `seal.py#remove_workflow`, `#mode`'s `--check` branch and `chain_check.py#ROOT_LEFT_SAYS`. `left_workflow_line` now prints that the checks read nothing as declared and pass, the header of `templates/setup/hygiene.yml` says the review-chain step judges the commit trailers alone and the mode step finds no root to disagree with, and the two cases of `tests/skills/test_seal.py` read the new words. The printed-line case was seen red against the old message before the code changed; the older-pin case's negative assert was seen red under `seal mutate` printing the phrase on a line of its own, and the file was restored. The changelog's `### Fixed` gains an entry in `76cf4ebbe`. A search on `examines nothing`, `examine nothing`, `examined nothing`, `checks nothing`, `owes nothing`, `every step passes`, `pr-checks remove`, `outlived its root` and `left in a local` over the tree, a sample, found one more statement of the claim, in a file this work item does not edit: `docs/layout/one-root-by-lifetime.md` *Shared or local* says a workflow left in local mode "passes having examined nothing", and its Korean edition says the same; the hand-back names both for a `## Rule changes` operation. A statement in other words is the part the sample did not reach.
location: `seal/threads/1795406406-code-stands-on-facts-that-no-longer-hold/changelog.md`
```

## Confirmations

What matched: the design's acceptance searches print nothing at `909602a0b`, each exiting 1 (executed): S4 (`absent_root`, `unwritten_root`, `UNWRITTEN`), S5 (`tracker_labels`, `test_tracker_labels` outside `seal/threads` and `docs`), both line searches of S7, S9 (`RIDER:`), both searches of S14, and S15 (`old_names`, `OLD_NAME`). The multi-line calls of S7 were read at `tests/skills/test_chain_check.py:817`, `:2466` and `:4924`, and none passes a reader.

What matched: the narrow modules of the changed units pass (executed): `bin/test -q tests/lib/test_gaps.py tests/lib/test_items.py tests/lib/test_fields.py tests/lib/test_config.py tests/lib/test_routing.py tests/skills/test_unverified_check.py tests/behaviour/test_a_declared_label_reaches_the_tracker.py tests/skills/test_seal.py`, 788 passed, exit 0. `uvx ruff check` and `uvx ruff format --check` over the 39 Python files the diff adds or changes pass (executed).

What matched: `seal.py#other_worktrees` (`skills/implement/scripts/seal.py:1621-1657`) leaves out the clone's own path and the real path of `lib/optin.py#git_common_dir` (read). `git_common_dir` answers `<root>/.git` where that is a directory, and otherwise git's answer joined to the root (`lib/optin.py:123-145`), so both sides of the comparison are absolute before `realpath`. A plain repository's main worktree is listed at its top, not at `.git`, so it stays in the list seen from a linked worktree. That is the A2 measurement of `frame/plan.md`, read against the code.

What matched: `chain_check.py#round_read`'s `else` reads `block.fields[FIELDS.CONFIRMS]` from every confirmation block outside the findings (read, `skills/code-review/scripts/chain_check.py:760-770`). A `confirms:` line that fails its pattern leaves no block, which `tests/lib/test_fields.py#test_refuses_confirms_none_at_its_line` pins as `found.blocks == []`. So the `else` meets no block without the key.

What matched: `lib/config.py#reference_roots("", name)` answers `None`, and `under_reference_root` reads `None` as the default (read, `lib/config.py:264-321`). Its one caller is `unverified_check.py#references_at` (executed: `git grep -n -e 'reference_roots(' -e 'references_at(' -e 'under_reference_root('`), so the changelog entry's scope, `seal unverified`'s walk, is the whole of the change.

What matched: `seal/follow-up.md` holds the two rows of *Scope* item 10 and no other, each naming `the repository owner` with no condition (read, design S16). `_moved_main` stands at `skills/verify/scripts/test_layout.py:1083`. `SITE_KINDS` and `classify` stand at `tests/skills/test_session_cost.py:887` and `:1325`. `CONTRIBUTING.md` *The test layout* names the move check at `CONTRIBUTING.md:337` (executed: `grep -n`).

What matched: the two quotes of `pr.md` stand word for word in the Judgment cells of `frame/plan.md:67` and `:68` (read). The changelog carries seven `### Removed` entries and one `### Fixed`, as *Scope* item 10 states (read). The tree's `chain_check.py`, run with `--baseline 02369a0e9 --worktree` before this record was written, printed no notice at a line of the design about a test pin or a copy (executed).

Two new cases were not claimed seen red, and each holds a fact the frame states. Neither is a finding. `tests/lib/test_routing.py#Test_rounds_unreadable.test_accepts_any_link` asserts an answer the base gave too. Reading `lib/routing.py:401-432` shows it fails with the link arm removed. The `a file` parameter of `tests/lib/test_routing.py#Test_rounds.test_refuses_an_item_with_no_rounds_directory` holds an answer that `rounds` gave at the base as well, now through `_ordered`'s `except OSError`. It guards that removal and pins no new behaviour.

The branch is `refactor/1576-code-stands-on-facts-that-no-longer-hold` while `frame/plan.md:67` gives the pull request `fix:`, and 11 of the branch's commits are `refactor:`. Feature branches squash, so no commit subject reaches the base. A branch name is read only in a list of branches, so this is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the target: the full suite, the repository-wide lint and the format check (`Broad gate` of `seal/config.json`). The suite stays `unverified` (contract rule 2) | `seal/config.json` | the orchestrator's broad run |
| The close-issues workflow without the label step, on a push to `main` | `.github/workflows/close-issues-on-release.yml` | the close-issues run when this release reaches `main`, read by the repository owner (`gaps.md`) |
| The Windows leg of the narrow modules this round ran on macOS | `tests/skills/test_seal.py#Test_other_worktrees`, `tests/lib/test_routing.py#Test_rounds_unreadable` | the pull request's CI |

## Probes

| Command | Result |
|---|---|
| `python3 -I <scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-1/test_tmp_round1_probe.py`, which runs `skills/verify/scripts/unverified_check.py` from the base tree (`git archive 02369a0e9`) and from the target on one `gaps.md` whose only row opens with U+2705 | base: exit 1, `1 unreadable`, the row refused with the U+2705 edit; target: exit 0, the row listed as `open`, `0 unreadable` |
| `bin/test -q` over the eight modules named under *Confirmations* | 788 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over the diff's 39 added or changed Python files | both exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline 02369a0e9 --root <the branch worktree> --worktree`, the target's copy, before this record | exit 0; no notice at a line of the design; the work item named as holding no round record, no gate record and no guarantee |
| The acceptance searches S4, S5, S7, S9, S14 and S15 of `frame/design.md` at `909602a0b` | each printed nothing and exited 1 |
