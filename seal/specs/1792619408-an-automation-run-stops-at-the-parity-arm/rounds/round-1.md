# 1792619408-an-automation-run-stops-at-the-parity-arm — review round 1

target: 77eef010 against release/v0.22.3

This is round 1, so no earlier round carries a coordinate or a verdict, and every fact below was established this round. `spec.md` cites no reference root, so none was opened. This repository declares no `seal/parity.md`, so no parity comparison was made here and this record carries no `original:` line. The owner's direction, `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*, was applied to every sentence the diff adds for an agent or a check to read. The review ran in a `git clone --no-local` of the branch at 77eef010, with `release/v0.22.3` at eae7f0ad as the base.

The implementer's account was checked claim by claim. Claimed: the declaration is read once for both arms; `hooks/gate.py:157` reads it once and both conjuncts use it. Claimed: `gate.touches_code` is loaded by path, not copied; `chain_check.py#parity_readers` loads `hooks/config.py` then `hooks/gate.py` by path, and no copy of `DOC_ROOTS` is in the check. Claimed: `hooks/config.py#baseline_commit` is the one reader of `Baseline commit`; it is the only function that reads the row, and `originals_of` calls it. Claimed: S1's three cases were seen red; removing the conjunct at `hooks/gate.py:169` turned all three red (executed, `## Probes`). Claimed: S12's two searches return nothing; both exit 1 outside `seal/specs/` and `changelog/` (executed).

## Findings

### 1. The rule change that settles the new pull-request paragraph loses a line, and the pull-request check passes it

severity: must
location: `seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm/spec.md:198-201`
evidence: executed `python3 -I <scratch>/test_tmp_replay.py <clone>`, `python3 -I <scratch>/test_tmp_live.py <clone>`
verdict: open

At settle, the second `add` operation of `## Rule changes` writes a policy paragraph into `docs/the-review-record.md` that is missing its subject's second half. The sentence that states the new rule then runs from "every round record of a work item declaring" straight into "config's baseline", with the answer it names and the `original:` line it owes both gone, and no agent or person can act on it. The pull-request check from #1006 (`chain_check.py#rule_changes_read`) parses the section, finds no error, and passes it. So the loss reaches the release unannounced, which is the failure #1006 exists to stop.

The cause is spec line 200. Line 199 ends by opening a code span before the word through, and line 200 begins with the words the review chain and the backtick that closes that span, so line 200 begins inside the span. `rule_changes.parse` keeps only lines that `unverified_check.py#live_lines` reads as live, and a line that begins inside a code span is not live, so it is dropped without an error (`skills/settle/scripts/rule_changes.py:104-108`). The replay probe applied all eight operations to the docs at HEAD. Every `from:` placed, and the diff of the result shows the paragraph without that line. The liveness probe over lines 130 to 216 found line 200 alone dead, and none after the span is closed on the line that opens it. The class was enumerated over all eight operations of this spec: no other `from:` or `to:` line begins inside a span. The reader's silent drop is finding 2.

```markdown
- add
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  to: **Where `seal/parity.md` is declared and the change reaches outside
    `docs/` and `seal/`, every round record of a work item declaring
    `through the review chain` carries one `original:` line naming the
    migration config's baseline.** The check reads `seal/parity.md` at HEAD and the
```

answer: The finding holds, and the fix is the framer's, because `spec.md` is the framer's file; the orchestrator sends it after this fix pass, so the verdict stays `open` until the framer's commit closes it. Since 7eacbe1c, `rule_changes.parse` refuses spec line 200 at its number (finding 2), and `chain_check.py --baseline origin/release/v0.22.3 --worktree` prints that refusal for this spec, so the pull-request check no longer passes it.

### 2. A Rule changes line that begins inside a code span is dropped at parse with no error

severity: should
location: `skills/settle/scripts/rule_changes.py:104-108`, `tests/test_settle_applies_rule_changes_in_place.py`
evidence: executed `python3 -I <scratch>/test_tmp_live.py <clone>`, `python3 -I <scratch>/test_tmp_replay.py <clone>`
verdict: fixed 7eacbe1c

`rule_changes.parse` is the one reader both `settle` and #1006's pull-request arm use. Its body loop skips every line that is not live and not inside a closed fence. That rule is meant to drop HTML comments, but it also drops a field's continuation line that begins inside a code span opened on the line above. The section then parses clean, settle applies the operation with the line missing, and the pull-request check reports nothing. Finding 1 is one instance in this branch. Any spec that wraps a backticked phrase across two lines of a `from:` or `to:` value is another, and a `from:` missing a line also places against a different text than the one the framer wrote. This code is the base's, not this branch's, so the fix pass may close it `deferred <home>`. It is reported here because this round was asked to read the section under #1006's check, and the check cannot tell this section's defect from a clean one.

The fix refuses such a line at its own line instead of dropping it. A line skipped as a comment is told apart through `unverified_check.py#comment_scan`, which yields whether each line began outside a comment. Precondition: `lines` is `r.gfm_lines(text)`, the list `live` and `fenced` are indexed by, as at `rule_changes.py:91-102`. A case in `tests/test_settle_applies_rule_changes_in_place.py` holds a `to:` value whose code span opens at the end of one line and closes on the next, and expects the error at the second line's number.

```python
    live = [flag for _, flag in r.live_lines(lines)]
    fenced = r.closed_fence_lines(lines)
    began_outside = [began for began, _kept in r.comment_scan(lines)]

    body = []
    for n in range(start + 1, end):
        line = lines[n]
        # opens_comment: NAME NOT IN TREE, the existing test at
        # rule_changes.py:107 for a line that opens an HTML comment, unchanged
        if opens_comment(line) or not began_outside[n]:
            continue  # guidance in a comment, never an operation
        if not live[n] and n not in fenced:
            return Parsed([], None, [(
                n + 1,
                "this line begins inside a code span an earlier line opened, "
                "and settle would drop it: close each span on the line that "
                "opens it",
            )])
        body.append((n + 1, line))
```

answer: Fixed here, as the record's fix gives it. `rule_changes.parse` reads `unverified_check.py#comment_scan`, skips a line that began inside an HTML comment as before, and refuses a line that is not live, began outside a comment and stands outside a closed fence, at its number, so the spec applies nothing. `tests/test_settle_applies_rule_changes_in_place.py#test_a_line_that_begins_inside_a_code_span_is_refused_at_its_line` was seen red against the old reader (the operation parsed with its value cut at the open span), and `mutation-check` turned it red with the refusal removed and with the comment skip narrowed. `skills/settle/SKILL.md` *Rule changes* states the rule, and the changelog fragment names it. Over all 120 `seal/specs/*/spec.md`, `parse` now refuses one: this work item's own `spec.md:200`, which is finding 1.

### 3. In local mode a chain declaration silences the parity arm and no check reads the original line

severity: should
location: `hooks/gate.py:157-170`, `skills/implement/orchestration.md:446-456`, `seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm/spec.md:132-140`, `tests/test_routing_is_recorded.py`
evidence: executed `python3 -I <scratch>/test_tmp_routes.py <clone> <scratch>/work`
verdict: fixed 6a87e4a8

The frame justifies quieting the arm at the commit by its pull-request half: "a code commit with no recorded comparison is still refused at a place CI or a person sees" (`spec.md` S13). In local mode no such place exists. The root sits under the common git directory and nothing under it is committed, so CI cannot run the chain checks (`docs/one-root-by-lifetime.md` *Shared or local*), and `chain_check.py` run by hand prints that it examined nothing (`skills/code-review/scripts/chain_check.py:1980-1990`). Before this branch, local mode met the parity arm on every code commit. Now a chain declaration removes the arm, and nothing reads the `original:` line that replaced it.

The probe built a local-mode repository with `.git/seal/parity.md` and staged a code change. `gate.arms_missing` returned `['parity']` with no declaration and `[]` once a chain declaration named the branch. `chain_check.py --baseline main` then exited 0 with the local-mode notice. `questions.md` Q1 kept the arm at the commit under `straight to the PR` because no record carries the comparison to CI. Local mode is the same condition under the other answer, and the frame does not mention it.

The fix keeps the arm at the commit where the root is local, on Q1's reasoning. The wake/quiet cell at `orchestration.md:446`, the paragraph after it, the first `change` operation (`spec.md:132-140`), the README rows and the changelog fragment then say "where the root is in the tree". A case beside `test_a_chain_declaration_quiets_the_parity_arm` holds a local-mode root and expects `[PARITY]`. If the orchestrator prefers unattended runs in local mode, the other fix is a limit sentence in the new `add` paragraph saying that a local-mode chain branch is checked by nothing. Either way the S13 claim needs the qualifier.

```python
    declared = routing.declared(cwd, top)
    # The chain answer moves the parity check to the pull request only where
    # CI can read the round records: a root in the tree. A local root is
    # committed nowhere, so there the arm stays at the commit (#988).
    # Precondition: `top` is the repository root, as `routing.declared` takes it.
    chained = (
        declared
        and declared["review"] == routing.CHAIN
        and optin.home_at(top) == optin.home_paths(top)[0]
    )
    ...
    if (
        PARITY not in waived
        and optin.parity_config(cwd)
        and not chained
        and touches_code(paths())
        and (not head or read_mark(cwd, git_dir, MARKS[PARITY]) != head)
    ):
```

answer: The finding holds. The orchestrator chose the record's second fix, a limit sentence, over the gate change: the review arm's declaration already carries the same cost in local mode, and keeping the arm at the commit there brings back the stop this work item removes. 6a87e4a8 states the limit under the wake/quiet table in `skills/implement/orchestration.md`, points to it from `skills/legacy-parity/SKILL.md` *Recording the comparison*, and names it in the changelog fragment. The `spec.md` and `plan.md` side, S13's qualifier and the `add` paragraph's limit sentence, is the framer's.

### 4. The changelog promises a pull-request check that a pinned workflow or a rewritten declaration never runs

severity: should
location: `seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm/changelog.md:12-27`, `seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm/plan.md:136-142`, `seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm/spec.md:168-185`
evidence: read `templates/hygiene.yml:5-11`, `templates/hygiene.yml:58-61`, `docs/branch-and-release.md:198-201`, `skills/code-review/scripts/chain_check.py:2128-2141`
verdict: fixed 6a87e4a8

The two halves of this change reach a user repository at different times. The commit half runs from the installed plugin, so it changes when the plugin is upgraded. The pull-request half runs from `templates/hygiene.yml`, which pins `--branch v<version>` to the release installed at first setup and moves only when a person edits it (`templates/hygiene.yml:5-11`, `:58-61`). A migration repository that upgrades the plugin and keeps its pin therefore gets a commit gate that no longer stops an uncompared code commit on a chain branch. Its CI keeps running a `chain-check` that has no `original:` arm, so the ready pull request passes. The changelog says the chain-declared pull request "owes the comparison in every round record", and `plan.md` *Operational impact* says such a repository "meets the new refusal at its next ready pull request once it upgrades". Both are false until the pin moves, and neither tells the person to move it.

A second shape is in the same class. Code committed while the declaration answered `through the review chain` met no parity arm. If the declaration is then rewritten to `straight to the PR`, the check reads only the answer at HEAD (`chain_check.py:2128`), and under that answer no `original:` line is owed. This shape is outside the normal flow, so it takes a limit sentence and not a guard.

```markdown
changelog.md, after "says of a line the grammar table adds.":
  The pull-request half runs from the plugin release that
  `.github/workflows/hygiene.yml` pins, while the commit half runs from the
  installed plugin. A migration repository moves the pin's `v<version>` to
  this release when it upgrades; until then its CI reads no `original:`
  line, and a chain-declared branch commits code nobody compared.

spec.md, the Parity arm `add` operation, after "the cost the review arm's
declaration already states.":
    The pull-request half runs from the release the repository's
    `.github/workflows/hygiene.yml` pins, so a pin older than this rule
    leaves the commit half without it. A declaration rewritten from
    `through the review chain` to `straight to the PR` after code was
    committed leaves those commits compared by nobody, because the check
    reads the answer at HEAD.

plan.md *Operational impact*: the first bullet names the pin as the
condition under which the refusal is met.
```

answer: The finding holds. 6a87e4a8 adds both limits to the changelog fragment: the pin in `.github/workflows/hygiene.yml` must move to this release before CI reads `original:` lines, and a declaration rewritten to `straight to the PR` after code commits leaves those commits compared by nobody. The same two limits stand under the wake/quiet table in `skills/implement/orchestration.md`, the shipped text. The sentence in `spec.md`'s Parity arm `add` operation and the first bullet of `plan.md` *Operational impact* are the framer's.

### 5. The migration setup skill and the shipped workflow still describe the parity check as it was

severity: should
location: `skills/parity-setup/SKILL.md:55-61`, `templates/hygiene.yml:82-94`
evidence: executed `git grep -n -i -E "original was consulted|whether the original|compared HEAD|specseal-parity" -- ':!seal/specs' ':!changelog' ':!CHANGELOG.md' ':!tests'`, `git log --oneline -3 -- templates/hygiene.yml`
verdict: fixed 6a87e4a8

Contract §19 asks every sentence that stands on the old fact to be rewritten in the same change. Two shipped texts were not in the frame's `## Removes`.

- `parity-setup` step 7 tells the agent to say to the user that from now on "a commit touching anything outside the document roots stops and asks whether the original was consulted, and it keeps asking until `legacy-parity` has recorded the compared HEAD". On a chain-declared branch that is now false, and it is the first thing a migration repository's owner is told.
- The comment over the chain-check step in `templates/hygiene.yml` lists what a ready pull request fails for. #1006 added its `## Rule changes` refusal to that list (eae7f0ad). This branch adds a refusal and does not list it, and the file ships to user repositories.

```markdown
skills/parity-setup/SKILL.md, step 7, from "too: from this file onward":
   too: from this file onward, a commit touching anything outside the
   document roots stops and asks whether the original was consulted, until
   `legacy-parity` has recorded the compared HEAD in
   `<git-dir>/specseal-parity`. A branch whose `routing.md` answers
   `through the review chain` is the exception: there the warden writes an
   `original:` line in each round record, and the pull-request check reads
   it instead.

templates/hygiene.yml, in the list after "that `spec.md`,":
      # that `spec.md`, a round record of a work item reviewed through the
      # review chain with no `original:` line naming `seal/parity.md`'s
      # `Baseline commit`, where that config is declared and the pull
      # request changes a path outside `docs/` and `seal/`, a finding still
```

answer: Fixed as the record gives it. `skills/parity-setup/SKILL.md` step 7 names the chain-declared branch as the exception, where the warden writes an `original:` line and the pull-request check reads it, placed after the sentence on `<git-dir>` so "That is" still points at the mark's path. `templates/hygiene.yml` lists the new refusal after the `## Rule changes` one.

### 6. The overview still lists as not done the two rule changes 77eef010 made

severity: should
location: `seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm/overview.md:23-37`
evidence: read `seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm/overview.md:23-37`, `seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm/spec.md:148-161`
verdict: fixed 6a87e4a8

`## Not done` says the `docs/commit-review-gate-spec.md` sentence and the `docs/README.md` row were left, and that "the orchestrator decides whether `## Rule changes` gains an operation for each". Commit 77eef010 added both operations (`spec.md:148-161`), so an orchestrator or sealer reading the overview is asked to decide something already decided. `## Fed back into the spec` reads "None.", while 77eef010 carried the build's divergences on S3, S11, the loader sentence and the `commit-review-gate.py` clause into `spec.md`. The pull request body is copied from these records, so the stale lines would reach it.

```markdown
## Not done

None. The two `docs/` sentences the build left are the third and fourth
`change` operations of `spec.md` `## Rule changes`, added at 77eef010.

## Fed back into the spec

At 77eef010 the orchestrator carried four divergences into `spec.md`: S3
names the 26 cases that declare `straight to the PR`, S11 is pinned at
`originals_of`, *Data & interfaces* names the loader sentence and the
`READ_ROWS` entry, and `## Removes` names the `commit-review-gate.py` clause.
```

answer: Fixed. `## Not done` now says the two sentences are the third and fourth `change` operations added at 77eef010. `## Fed back into the spec` names the four divergences 77eef010 carried into `spec.md`, S11's wording included.

## Confirmations

confirms: none
S1 holds and its cases pin it. With the conjunct at `hooks/gate.py:169` removed in the clone, `test_a_chain_declaration_quiets_the_parity_arm`, `test_a_chain_declared_code_commit_meets_no_parity_stop_under_the_press` and `test_a_chain_declared_code_commit_meets_no_parity_arm_inside_git` all failed, and with it restored the modules pass (executed).

confirms: none
`straight to the PR` keeps the arm at the commit, and an undeclared branch meets it as before: `arms_missing` adds `PARITY` unless the declaration's `review` is `routing.CHAIN` (`hooks/gate.py:166-172`, read), and `test_a_direct_declaration_does_not_waive_the_parity_arm` and the parity cases of `tests/test_chain_hooks_hardening.py` pass (executed).

confirms: none
The moved hardening cases still test what they tested. Each used the declaration only to quiet the review arm while judging the parity arm or a command shape. `straight to the PR` quiets the review arm exactly as the chain answer does (`hooks/gate.py:159-165`, read) and leaves the parity arm standing, so each case keeps its property. `tests/test_no_shape_the_base_stops_reads_silent.py`, `tests/test_chain_hooks_hardening.py` and `tests/test_the_commit_gate_decides_at_the_commit.py` pass at 77eef010 (executed). The count of 24 parametrized ids was not recounted. The module's 13 `make_repo(..., declared=True)` calls were read.

confirms: none
A pull request that declares nothing is not a new route. On a branch no committed declaration names, the parity arm stood at every code commit, and it still does. A declaration the pull request removes is refused unless a settle retired it (`chain_check.py#main`, read). A chain declaration written on disk and never committed quiets both arms and passes with a notice. That is the review arm's stated cost, "a repository that adopts the declaration and not the workflow" (`docs/the-review-and-parity-arms.md:92-100`, read), now shared by the parity arm.

confirms: none
A round whose `original:` names the right commit but compared nothing passes the check. The new `add` paragraph and `plan.md`'s failure scenario state this as the limit the parity mark already has. The template's commented example line is not read as a line: a record copied from `templates/sdd-round.md` with the comment intact is refused as having no `original:` line (executed, `## Probes`).

confirms: none
The new arm sits beside #1006's correctly. `rule_changes_of` runs for each judged item and for the edited items, and `originals_of` runs after both. Each returns None for a reader that will not load, and `main` exits 2 on it (`chain_check.py:2120-2144`, read). This spec's `## Rule changes` parses into eight operations with no error, and every `from:` places once at HEAD (executed). Finding 1 is the one defect.

confirms: none
The writing rules hold for `agents/warden.md` step 5, the `templates/sdd-round.md` comment and the `legacy-parity` paragraph. Each names the warden, the round, the record and the line it writes. `unread` is the parity verdict word `skills/legacy-parity/SKILL.md:95` defines, not a new term. No sentence the diff adds uses a dash or an arrow as a separator.

confirms: none
S12 holds: `git grep -n -i 'review arm only'` and `git grep -n 'does not silence the'` exit 1 outside `seal/specs/` and `changelog/` (executed). `docs/the-review-and-parity-arms.md:82` still says a declaration moves the review arm's check, which is still true. The other `docs/` sentences that named the review arm alone are `## Rule changes` operations.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at 77eef010 | the whole tree | the orchestrator's broad run, `broad-gate --base release/v0.22.3 --record seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm` |
| The `tests` run 39696614659 at 77eef010, including the Windows leg of the new cases | CI | the orchestrator, who relays a failure |
| Whether local mode keeps the arm at the commit or takes a limit sentence (finding 3 gives both fixes) | `hooks/gate.py:157-170` | the orchestrator, under the owner's `automation` answer and Q1's reasoning |

## Probes

| Command | Result |
|---|---|
| `python3 -I <scratch>/test_tmp_replay.py <clone>` | the spec's `## Rule changes` parsed into 8 operations with no error; `rule_changes.replay` applied all 8 to the docs at HEAD; the settled `docs/the-review-record.md` paragraph lacks spec line 200 |
| `python3 -I <scratch>/test_tmp_live.py <clone>` | over spec lines 130 to 216, line 200 alone reads dead and outside a fence; with the span closed on its own line, no line reads dead |
| `python3 -I <scratch>/test_tmp_routes.py <clone> <scratch>/work` | local mode: `arms_missing` gave `['parity']` with no declaration and `[]` with a chain declaration; `chain_check.py --baseline main` exited 0 with the local-mode notice; a template copy's commented `original:` line was not read, and `original_of` refused the record as having none |
| `bin/test tests/test_routing_is_recorded.py tests/test_an_automation_run_meets_no_commit_prompt.py tests/test_the_commit_gate_decides_at_the_commit.py -q -p no:xdist -k chain_declar`, with the conjunct at `hooks/gate.py:169` removed | 3 failed, the three S1 cases; the line was restored and `git status` read clean |
| `bin/test tests/<module>.py -q` for `test_chain_check`, `test_routing_is_recorded`, `test_no_shape_the_base_stops_reads_silent`, `test_chain_hooks_hardening`, `test_the_commit_gate_decides_at_the_commit`, `test_an_automation_run_meets_no_commit_prompt`, one command each | 126, 69, 51, 56, 189 and 18 passed, each exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline release/v0.22.3 --worktree`, before this record | exit 0, not judged ready; the three refusals are the records this work item does not hold yet |
