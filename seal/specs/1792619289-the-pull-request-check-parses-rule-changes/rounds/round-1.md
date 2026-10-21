# 1792619289-the-pull-request-check-parses-rule-changes — review round 1

target: be5a9330 against release/v0.22.3

This is round 1, so no earlier round carries a coordinate or a verdict here. Every fact below was established this round. `spec.md` cites no reference root, so none was opened. `seal/parity.md` is not declared, so no parity comparison was made. The owner's direction, `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*, was applied to every sentence the diff adds as a review criterion. Findings 3 and 4 rest on it.

## Findings

### 1. A declared pull request that edits another work item's spec merges a section the reader refuses, and nothing reads it

severity: must
location: `skills/code-review/scripts/chain_check.py:1952-1989`, `seal/specs/1792619289-the-pull-request-check-parses-rule-changes/spec.md:55-61`, `seal/specs/1792619289-the-pull-request-check-parses-rule-changes/spec.md:148-150`, `seal/specs/1792619289-the-pull-request-check-parses-rule-changes/plan.md:78-81`, `seal/specs/1792619289-the-pull-request-check-parses-rule-changes/plan.md:92-93`, `tests/test_chain_check.py`
evidence: executed `bin/test tests/test_tmp_round1_probe.py -q -s -p no:xdist -k p1`, `git show --name-status --format= b451e503 -- 'seal/specs/*/spec.md'`, `git show --format= b451e503 -- 'seal/specs/*/spec.md'`
verdict: deferred the frame

This gap lets through the exact loss #1006 exists to stop. The work item's own failure direction (`plan.md` *Operational impact*) calls a wrong allow the expensive mistake: a release whose rule changes apply nothing at the owner's settle.

What the frame claims. `spec.md:55-61` and `plan.md` A2 say a work item's own `spec.md` is always beside a judged declaration, so "a `spec.md` edited by a commit that belongs to no work item is the remaining case". The premise is true. The conclusion drawn from it is false, because a commit of a declared work item can edit a different work item's `spec.md`. That work item's `routing.md` is not in the diff, so `main` never judges it, and `rule_changes_read` is only called from the per-declaration loop (`chain_check.py:1983`).

The release's own history holds this case at scale. #941's squash, b451e503, modified 114 `spec.md` files of other work items. It added a `## Rule changes` heading to each of them, the sections the release's backlog settle reads. It changed none of their `routing.md` files (executed, `git show --name-status` and a count of added `## Rule changes` lines, 114 and 114). Under A1, #941's pull request would have parsed only #941's own spec, and none of those 114 sections.

The probe ran on the module's `branch` fixture on a ready pull request, and each of its three cases exited 0 with no line naming the other work item's spec:

- P1a: the declared branch adds `seal/specs/1788999999-a-merged-item/spec.md` with the no-change block's `why:` continued two spaces in (#941's own defect), and a round 3 targets HEAD.
- P1b: the same edit to a spec that already parsed on the base, reached through a merge, and reviewed the same way.
- P1c: the declaration reads `straight to the PR`, so no round is owed at all.

A2's grounds for rejection do not reach this case. A2 was rejected because it fails "a pull request that declared nothing". A pull request that declares its own work item is not that pull request, and `main` already returns at `if not declarations` before any of this runs. Issue #1006, item 1, also asks for "each work item's `spec.md` the pull request carries". The records arm demands a verifying round for such an edit: P1a's first run, without round 3, was refused with "a verifying round is owed". But no round is told to run the parser (`plan.md` A6), so that round does not close the gap.

The fix reads every `seal/specs/<id>/spec.md` this pull request's own commits add or change, beside the specs of the judged declarations. It runs only after the declared-nothing return, so that promise in `.github/workflows/hygiene.yml` and `CONTRIBUTING.md` still holds. A spec another pull request's squash carried is skipped, by the same `carried_by` rule the declarations use. In the same commit, these sentences have to be rewritten: the frame's *Out* bullet, the A1 and A2 rows, *What breaks in six months*, and the `add` item's "The check reads no other `spec.md`" (`spec.md:148`). Both `hygiene.yml` comments and the docstring's `rule changes` arm also have to say which specs are read. A case under `TestRuleChangesRead` holds P1a: a declared, reviewed branch that edits another work item's spec exits 1 naming that spec.

```python
    fork = reader.merge_base(root, args.baseline)
    problems, notices = [], []
    # Every work item spec.md this pull request's own commits add or change,
    # beside the judged declarations' own: a declared work item can edit
    # another's section (b451e503 did it 114 times). A pull request that
    # declared nothing returned above and never reaches this line.
    depth = len(routing.WORK_ITEMS.split("/")) + 2
    edited = sorted(
        {
            os.path.dirname(p)
            for p in paths
            if p.startswith(f"{routing.WORK_ITEMS}/")
            and len(p.split("/")) == depth
            and os.path.basename(p) == "spec.md"
            and p not in moved
            and carried_by(root, args.baseline, p) is None
        }
        - {os.path.dirname(rel) for rel in declarations}
    )
    ...
    # after the per-declaration loop, before the notices print:
    for item in edited:
        try:
            problems.extend(rule_changes_read(reader, root, item))
        except (OSError, SyntaxError, ImportError, SystemExit) as exc:
            print(
                f"chain-check: the rule-changes reader would not load ({exc})",
                file=sys.stderr,
            )
            return 2
```

answer: The framer reframed this at 4fb593a8, and the build landed it in phase 2 at e077c5d5, with the cases that hold its filters at 2a3ea1a2. `chain_check.py#edited_work_items` gives every `<WORK_ITEMS>/<id>/spec.md` this pull request's own commits add or change, less an exact move and less what `carried_by` assigns to another pull request's squash. `main` reads that set after the per-declaration loop, under the one exit-2 guard `rule_changes_of`, and it reaches the set only after the declared-nothing return. S12, S13 and S14 hold P1a, P1b and P1c. Each was seen red against 22bfec31 on `assert 0 == 1`. S15 holds the declared-nothing promise. The frame's sentences this finding names were rewritten by the reframe.

### 2. The broad run and the preflight pass a spec whose section does not parse, while the frame and the changelog say they meet it

severity: should
location: `seal/specs/1792619289-the-pull-request-check-parses-rule-changes/spec.md:32-35`, `seal/specs/1792619289-the-pull-request-check-parses-rule-changes/spec.md:87`, `seal/specs/1792619289-the-pull-request-check-parses-rule-changes/changelog.md:10-11`, `tests/test_chain_check.py:1997-2006`
evidence: executed `bin/test tests/test_tmp_round1_probe.py -q -s -p no:xdist`
verdict: deferred the frame

The orchestrator and the sealer act on these two sentences. They read them as saying that the broad run stops a broken section before the sealer is spawned. In this repository's flow it does not.

What is claimed. `spec.md:32-35` says the refusal "stays a refusal under `--sealing`, so the orchestrator's `broad-gate` run and its `--preflight` meet it before the sealer is spawned". `changelog.md:10-11` says it "stays a refusal in the broad gate's own run".

What the code does. `chain_check.py:1932-1933` judges strictly only where the state reads ready, or where it reads unknown while an event payload is present. `chain_check.py:2004` returns 1 only when the judgement is strict. `skills/code-review/orchestration.md:140` opens the pull request after the sealer has sealed. So when `broad-gate` and `--preflight` run, no pull request exists. `gh pr view` finds none, the state is unknown with no payload, and the check prints the refusal and exits 0.

Probe P2 ran the check the way `broad_gate.py:2995-2999` runs it: a subprocess with `--sealing`, every `GITHUB_` variable removed, and S1's spec committed. It exited 0. It printed "`gh pr view` exited 1: no pull requests found" and then the refusal as a plain line. S6 passes only because the `ready` fixture writes a payload, which the broad run never has in this flow.

The refusal does reach the pull request's own CI, which is the issue's ask, so this is a wrong claim and not a missing gate. Whether the broad run should judge this refusal strictly when no pull request exists is a design choice. It is a row of `## Not judged`. The fix below makes the two sentences true of the code as it stands.

```markdown
3. The refusal is judged like every other refusal of the check. It fails a
   ready pull request, and it prints and exits 0 on a draft. Under
   `--sealing` it stays in `problems`, never among the notices, so it fails
   the `broad-gate` run and its `--preflight` only where the check reads the
   pull request's state as ready. Both run before the pull request opens
   (`skills/code-review/orchestration.md` *the pull request opens once the
   sealer seals*). There the check reads the state as unknown, prints the
   refusal and exits 0, and the pull request's own CI is where it fails.
```

```markdown
  names the spec, the line the reader names and the reader's reason. It
  fails a ready pull request and prints on a draft. The broad gate's own run
  prints it, and fails on it only where a ready pull request is already
  open.
```

answer: The framer reframed this at 4fb593a8: `spec.md` *Scope* item 3 now states the limit, and S6 has a second half. The build landed it in phase 2 at e077c5d5. S6's second half runs `--sealing` with no event payload and `gh` finding no pull request, and holds that the check prints the refusal and exits 0. `changelog.md` now says the broad gate's own run prints the refusal, and fails on it only where a ready pull request is already open. The strictness of `--sealing` where no pull request exists is unchanged, and it stays round 1's `## Not judged` row for the owner.

### 3. A near miss of the heading, such as `## Rule Changes`, reads as a spec with no section and passes without a word

severity: should
location: `skills/settle/scripts/rule_changes.py:78-80`, `skills/code-review/scripts/chain_check.py:1566`, `tests/test_chain_check.py`
evidence: executed `bin/test tests/test_tmp_round1_probe.py -q -s -p no:xdist`
verdict: fixed 693c9a8c

The new arm is a check that reads one line, the `## Rule changes` heading. The owner's direction says that line must accept one spelling and refuse a near miss at its line: "검사가 읽는 줄은 정해진 철자 하나만 읽히고 조금 틀린 철자는 그 줄에서 거절되어야 한다. 조금 틀린 철자를 말없이 지나치는 검사는 그 줄을 읽지 않은 것과 같다."

`rule_changes.parse` matches only a level-2 heading whose text is exactly `Rule changes` (`rule_changes.py:78`). Anything else returns `Parsed(None, None, [])` (`rule_changes.py:79-80`), the value for a spec written before the section existed. Probe P3 parsed six near misses over a broken body: `## Rule Changes`, `### Rule changes`, `## Rule changes:`, `## Rules changes`, `# Rule changes` and `## Rule-changes`. Each returned `ops` None and no error. A ready pull request whose spec holds `## Rule Changes` over a valid `change` item then exited 0 with no line naming the spec.

At settle such a spec is "premodel": `settle.py:287-288` names it, keeps its directory, and applies nothing from it. That is the same late loss #1006 moves to the pull request. `questions.md` Q1, default (a), is about a spec with no section at all. A near-miss heading is a section its author wrote, so Q1 does not answer it.

Probe P6 found no `spec.md` under `seal/specs/` with a near-miss heading at any level, so the fix below refuses nothing in the tree today. The fix goes in the one reader, so `settle` holds such a spec instead of naming it premodel and the two still read alike. It narrows the class and does not close it. Letters compared after casefolding catch case, level and punctuation, and not a different word such as `Rules changes`. The verdict that closes this finding has to say so.

```python
def _letters(text):
    """TEXT's letters, casefolded: what a near miss of a heading shares
    with it once case, punctuation and spacing are set aside."""
    return re.sub(r"[^a-z]", "", text.casefold())


    found = [(n, lv) for n, lv, t in marks if lv == 2 and t == HEADING]
    if not found:
        near = [n for n, lv, t in marks if _letters(t) == _letters(HEADING)]
        if near:
            return Parsed(
                [], None, [(near[0] + 1, f"a heading that is not `## {HEADING}`")]
            )
        return Parsed(None, None, [])
```

answer: Fixed in the one reader, as the record proposes, and decided as a class rather than a list of spellings. `rule_changes.py#parse` refuses at its line every heading, at any level, whose letters, case folded, are those of `Rule changes` and that is not `## Rule changes`. It does so whether or not the right heading also stands. The reason names the heading as written and `## Rule changes`, the one heading read. `skills/settle/SKILL.md` *Rule changes* states the class once. `chain-check` needs no change of its own, because it asks the same reader, so `settle` now holds such a spec instead of naming it premodel. The class narrows the gap and does not close it: a heading with other letters, such as `## Rules changes`, is still another section, and `test_a_heading_with_other_letters_is_no_near_miss` pins that boundary. The six near misses of probe P3 are cases in `tests/test_settle_applies_rule_changes_in_place.py`, alone and beside the right heading. All twelve were seen red before the fix. `rule_changes.parse` over the 119 specs under `seal/specs/` refuses none (executed, in memory).

### 4. The workflow comment lists the new refusal among those that fail a draft, and its template copy lists it among those that do not

severity: should
location: `.github/workflows/hygiene.yml:169-182`, `templates/hygiene.yml:82-91`
evidence: read `.github/workflows/hygiene.yml:169-182`, `templates/hygiene.yml:82-91`, `skills/code-review/scripts/chain_check.py:2002-2004`, `tests/test_chain_check.py:1981-1995`
verdict: fixed 2d234e72

Agents and people both read this comment to learn what the step fails for. The diff wrote one fact into it twice, once in each copy, and the two copies now give it opposite draft behaviours.

`.github/workflows/hygiene.yml:172-176` reads "It fails for what the author can fix: a declaration ..., a declaration that cannot be read, a judged work item's `spec.md` whose `## Rule changes` does not parse, and — on a pull request that is not a draft — a finding still `open` ...". The sentence limits only what follows the dashed clause to ready pull requests. So it says a broken section fails a draft. The code says otherwise: `chain_check.py:2004` fails nothing while the judgement is not strict, and S5 (`tests/test_chain_check.py:1981-1995`) pins that a draft prints the refusal and exits 0. The same comment says so too, at `:182`: "On a draft every refusal prints and none fails". `templates/hygiene.yml:84-86`, the copy that ships to user repositories, places the same item after "once the pull request is no longer a draft", which is correct.

The owner's direction refuses both features of this sentence: a dash used as a separator a reader can take for grammar, and one value in two places that now disagree. The two items before the new one read the same wrong way, and that wrong reading is older than this diff. The fix moves the qualifier to the front so the whole list sits under it, and so it repairs all three.

```yaml
      # It never fails for a pull request that declared NOTHING, for the same
      # reasoning the step above gives for an honest open row: a build that
      # goes red for one teaches people to write none. On a pull request that
      # is not a draft it fails for what the author can fix: a declaration
      # that says "through the review chain" with no committed round record, a
      # declaration that cannot be read, a judged work item's `spec.md` whose
      # `## Rule changes` does not parse, a finding still `open` or one the
      # check cannot read, a last record behind HEAD or with a finding no
      # round after it read, no `broad-gate.md` at HEAD, or no `guarantee.md`
      # reading `sealed` at HEAD (`docs/the-review-record.md`
      # §*What the check reads at the pull request*).
```

answer: Fixed as the record proposes, in both copies and in the same words. The not-a-draft qualifier now opens the list, so every item sits under it, and the dash separator is gone. `templates/hygiene.yml` carries the same list, the two items it lacked included, wrapped to its own indent. This commit came before phase 2's edit to the same list. Phase 2, at e077c5d5, then rewrote the spec item in both copies to name both sets the check reads.

## Confirmations

confirms: none
The check and `settle` refuse the same sections for a work item the check reads. Neither side refuses what the other accepts. `chain_check.py:1564-1571` calls `reader.rule_changes().parse(text, reader.policy_root(root))`, and `settle.py:282-286` calls `rules.parse(text, reader.policy_root(root))`. The function, the loader and the policy-root reader are the same in both. The text is the spec as git carries it, read with `git show` in both. Settle's `or ""` for a missing spec and the check's `[]` for None give one answer, because `parse("")` returns no section. Read.

confirms: none
S11 holds: no importer loads anything new. The diff adds only the constant `RULE_CHANGES_SAYS` and the function `rule_changes_read` at module level (`chain_check.py:1552-1572`). The reader is reached only from `main`, at `:1983`. `git grep` finds `rule_changes_read` called nowhere else. `hooks/commitgate.py:262`, `skills/verify/scripts/seal_stamp.py:1011`, `skills/verify/scripts/broad_gate.py:2517` and `.github/scripts/release_seal.py:288` use readers and constants and never `main`. Probe P5 loaded `chain_check.py` by path in a fresh interpreter. Afterwards `SHARED_READER._rules` was still None and `sys.modules` held no rule-changes module. Executed.

confirms: none
The exit-2 path holds as the spec states it. The guard at `chain_check.py:1982-1989` wraps the whole `rule_changes_read` call, so a `policy_root` load failure gives the same line. That is the overview's second divergence row, and it is true at `:1566`. The four exception classes are the ones `main` catches for `hooks/routing.py`. An exception outside them is a traceback, as it is for that loader. S10 holds both halves: no spec never reaches the reader, and a raising loader gives exit 2 with the stderr line. Read.

confirms: none
This work item's own `## Rule changes` section parses and places. Probe P4 parsed `spec.md` into a `change` and an `add` item with no error. The `change` item's `from:` text occurs once in `docs/the-review-record.md`, and its `section:` heading occurs once. Executed.

confirms: none
The cases that are left alone pass, and the draft, ready and carried behaviours hold. S4 covers the no-change block, a `change` that parses and a spec with no section. S5, S6 and S8 cover a draft, `--sealing` on a ready pull request, and a squash-carried item. The unreadable and settled declarations reach `continue` before the call (`chain_check.py:1952-1978`). Read.

confirms: none
The overview's first divergence row is sound. The `branch` fixture declares `Planning | the session` (`tests/test_chain_check.py:196`), so S1 already covers that answer. S7 declares `framer` and writes `plan.md`, so the frame arm passes and the spec is the one refusal. Each new case covers a branch no other case of `TestRuleChangesRead` or `TestFrame` covers. Each refusal case asserts the exit code before the printed line. At the frame commit, which has no read, that first assertion fails on behaviour and not on a missing name. Read.

confirms: none
The rest of the new prose holds under the owner's direction. Findings 3 and 4 take the parts that do not. The docstring's `rule changes` arm, the exit line, the `settle` SKILL.md pointer sentence and `RULE_CHANGES_SAYS` use no separator symbol and state no value twice. They give no instruction that leaves out who acts. `chain-check` is the program name `main` gives argparse. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at be5a9330, which the smith handed over as `unverified`, and that label is honest | `seal/specs/1792619289-the-pull-request-check-parses-rule-changes/overview.md` | the orchestrator, through `broad-gate --base release/v0.22.3 --record seal/specs/1792619289-the-pull-request-check-parses-rule-changes`, once the rounds settle |
| CI run 39685286823 at be5a9330 | the `tests` workflow | the orchestrator, who said it will relay a failure |
| Whether `--sealing` should judge this refusal, or every refusal, strictly where no pull request exists yet, so that the broad run fails on it before the sealer (finding 2 corrects only the claim) | `skills/code-review/scripts/chain_check.py:1932-1933`, `skills/verify/scripts/broad_gate.py:2990-2999` | the orchestrator, for the owner |
| `questions.md` Q1 still reads `open` while the build proceeded on default (a) | `seal/specs/1792619289-the-pull-request-check-parses-rule-changes/questions.md:42` | the orchestrator, when it drains the rows before the broad run |
| The smith's claim that each refusal case was seen red against the frame commit was read, not re-run | `seal/specs/1792619289-the-pull-request-check-parses-rule-changes/phases/phase-1.md` | the sealer, if it samples that claim |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_tmp_round1_probe.py -q -s -p no:xdist` in a scratch clone at be5a9330, with P1 to P6 in one file | P2 exit 0 with the refusal printed (finding 2). P3: six near misses each parsed to no section and no error, and a ready pull request exited 0 (finding 3). P4: the own section parsed into `change` and `add`, and `from:` and `section:` each occur once. P5: `True False`. P6: no near-miss heading in the tree. P1a and P1b were refused for "a verifying round is owed", because the edit stood after the last round. A wildcard import also collected and re-ran the 110 cases of `tests/test_chain_check.py`, all of which passed |
| `bin/test tests/test_tmp_round1_probe.py -q -s -p no:xdist -k p1` after adding a round 3 at HEAD to P1a and P1b, and adding P1c | 3 passed: P1a, P1b and P1c each exit 0 with no line naming the other work item's spec (finding 1) |
| `git show --name-status --format= b451e503 -- 'seal/specs/*/spec.md'` and a count of added `## Rule changes` lines | 114 modified specs, and 114 sections added. Their `routing.md` files are unchanged, and the one rename is #941's own declaration |
