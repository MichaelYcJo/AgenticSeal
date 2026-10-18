# 1792126889-every-agent-is-written-anew-from-its-job — review round 1

target: 2dfa53a9 against af9c924b

## Findings

### 1. The new contract says no agent runs the broad gate while the sealer, the orchestration file and the contribution guide still give it to the sealer

severity: must
location: `skills/agent-contract/SKILL.md:37`, `agents/sealer.md:40`, `agents/sealer.md:106`, `skills/code-review/orchestration.md:180`, `CONTRIBUTING.md:107`, `bin/test:23`, `agents/smith.md:299`, `docs/the-broad-gate.md:11`, `skills/code-review/scripts/chain_check.py:1570`, `tests/test_broad_gate_rule.py:187`, `tests/test_the_agent_contract_holds_the_universal_rules.py:41`
verdict: fixed 91741abf

Contract §2 at 2dfa53a9 says the broad gate "is the orchestrator's: it runs
`broad-gate --base <base> --record <item>` ... before it spawns the sealer,
and the sealer reads the record. No agent runs any of the three". Nothing
else in the tree was moved to that fact. Read at 2dfa53a9:

- `agents/sealer.md:40`, step 1: "Run the broad gate, `broad-gate --base
  <base> --record <item>`", and `agents/sealer.md:106`: "The broad gate is
  yours. The contract's §2 leaves each definition to say whether the suite,
  lint and typecheck are its agent's". §2 no longer says that.
- `skills/code-review/orchestration.md:180-188`: the orchestrator runs
  `--preflight`, spawns the sealer, "The sealer runs `broad-gate --base
  <base> --record <item>`", and "you do not take the run yourself". The
  orchestrator loads the same contract, so it now holds two opposite orders.
- `CONTRIBUTING.md:107-110` and the comment in `bin/test:23-25`: "§2 forbids
  it to smith and warden, and `agents/sealer.md` is the agent it is assigned
  to". `agents/smith.md:299`: "the sealer takes the broad gate once".
  `docs/the-broad-gate.md:11` keeps the heading "the owner is an agent" and
  says the assignment lives in that agent's definition.
- `skills/code-review/scripts/chain_check.py:1570`, the refusal a person
  reads when `broad-gate.md` is absent: "the sealer runs `broad-gate --base
  <base> --record <item>`" (executed: this round's own check printed it).

The plan put this sentence in phase 3 because phase 5 of the same item was
to move the gate. Phase 5 moved to #969 (`plan.md` row 5), so this branch
merges a contract that contradicts the sealer it is preloaded into. The
item's own rules say this cannot land: contract §19 ("in the same commit
removes or corrects what stood on the old fact") and `spec.md` S15. The
phase record admits it (`phases/phase-3.md:72-78`) and defers it to a phase
that is no longer in this item.

Why it matters, executed: phase 3's sealer evaluation measured the conflict.
`evals/sealer-phase-3.md`, re-derived here from the kept raw output and
checked, reads rule 3 failing on `rule-sealer-untrue-body/shape-verdict`
(1/2 against 2/2). The phase record attributes that run (004) to a sealer
that read the refusal, re-ran a claim, and wrote no `guarantee.md`
(`phases/phase-3.md:220-224`, read; I did not re-read that trace).

The fix that stays inside this item's scope states in §2 what is true at
this HEAD, and leaves the move of the gate to #969, which rewrites §2 again
with the orchestration file in one commit. The two pins on the new wording
(`tests/test_broad_gate_rule.py:187-190`, contract `PINS[2]`) move with it.

```markdown
## §2 Narrow and often; the broad gate is one act with one owner

Run the tests for the slice you touched while you work, and your module and
the ones it touches at a phase boundary. The broad gate — the full suite, the
repository-wide lint, the typecheck — is one act, taken once after the review
rounds settle, by `broad-gate --base <base> --record <item>`. Run none of the
three unless your own definition hands them to you; `agents/sealer.md` is the
one definition that does. Hand over with the suite labelled `unverified` and
its answerer named: a suite that is not mentioned reads as a suite that
passed.
Enforced by: tests/test_the_agent_contract_holds_the_universal_rules.py::test_each_section_holds_its_rule
```

answer: Fixed as the round proposed, with the move named: §2 now says no agent runs any of the three but the sealer, whose definition hands it that run, and that #969 moves the run to the orchestrator before it spawns the sealer. `agents/sealer.md:106` recites that §2. `PINS[2]` and `test_the_prohibition_itself_has_one_home_and_it_is_the_contract` hold the new words, refuse `it is the orchestrator's` in §2, and read the sealer's recital; both seen red against the old §2 and the old recital. `orchestration.md`, `CONTRIBUTING.md`, `bin/test`, `docs/the-broad-gate.md` and `chain_check.py` were already true of this tree and are untouched. No other contract section says no agent runs the gate. The changelog fragment and an `overview.md` divergence row came in the same commit, and 59d42bcc points two test comments at #969 instead of phase 5.

### 2. The verdict passes a new side that never ran most of the cases, where every case has only shape and reach graders

severity: must
location: `evals/scripts/noninferiority.py:589`, `evals/scripts/noninferiority.py:627`, `evals/README.md:40`, `tests/test_a_rewritten_definition_proved_non_inferior.py:144`
verdict: fixed 857aa1af

`verdict` returns "no result" when "the two sides ran a case a different
number of times", but its check skips every shape or reach grader with zero
runs on either side (`noninferiority.py:589-594`), and rule 3 then skips a
grader with no new runs (`noninferiority.py:627`). The smith's and the
framer's cases carry only shape and reach graders (`ls
evals/behaviour/{smith,framer}/*/graders`, executed), so for them a case the
new side never ran leaves no trace in any rule. `compare` does not catch it
either: it compares the suite's tree hash, which `run --case <glob>` leaves
unchanged.

Executed (a probe over the committed side files, deleted): the smith's
phase-3 side cut to one of its four cases, with 18 of its graders at zero
new runs, reads `pass` for `rule-smith-count-words` alone and for
`rule-smith-is-palindrome` alone. The same cut on the warden's side reads
`no result`, because its truth graders still hit the runs check. So whether
a skipped case fails closed depends on whether the case happens to carry a
truth grader.

`evals/README.md:40-43`, written in this diff, says the opposite: "a case
run a different number of times ... is no result, never a pass". The
exemption was written for 0.22.0, when a grader could vanish between two
suites; since `compare` refuses two different suites (exit 2), a grader one
side lacks can only be a case or a grader that side did not run. The case
`rule 3: a shape grader only the baseline carried is not judged`
(`tests/test_a_rewritten_definition_proved_non_inferior.py:144-147`) pins
the fail-open reading and changes with the fix, to `no result`.

```python
    g = numbers["graders"]
    # Both sides ran one suite (`compare` refuses two), so a grader with
    # fewer runs on one side is a case or a grader that side did not run:
    # no result, whatever its kind.
    if any(old_runs != new_runs for _k, _op, old_runs, _np, new_runs in g.values()):
        return "no result", ["the two sides ran a case a different number of times"]
```

Rule 3's `if not oruns` branch is then unreachable from `compare`; keep it
or drop it with its two cases, and say which in the answer.

answer: Fixed at the case rather than at every grader: a case the baseline ran and the new side did not is `no result`, naming the case, whatever graders it carries; the tolerance for a shape or reach grader one side lacks stays for a case both sides ran. So rule 3's `if not oruns` branch stays reachable and is kept. Two cases are new, a side cut to one case of four and a baseline-only shape grader in a case the new side never ran, both seen red (`pass`) before the fix; the case at `:144` keeps `pass` and its name now says the grader is in a case both sides ran. `check` re-read all six records with their verdicts unchanged: warden-phase-3 and smith-phase-3 exit 0, framer-phase-3, sealer-phase-3, warden-phase-2 and warden-phase-2-run-1 exit 1 with their recorded reasons.

### 3. The four definitions not yet rewritten lost every pin that they preload the contract

severity: should
location: `tests/test_every_agent_reads_the_contract.py:32`, `tests/test_every_agent_reads_the_contract.py:131`
verdict: fixed d20fc32d

At af9c924b, `test_a_bare_name_is_delivered_by_the_frontmatter` and
`test_every_definition_opens_with_the_contract_line` held, for every file
under `agents/`, that the contract the definition names is in its `skills:`
list. Phase 2 removed both and "replaced" them with T1
(`phases/phase-2.md:262-264`), but T1 skips the framer, the smith, the
scribe and the sealer by name, whole, so for those four nothing replaced
them.

Executed (a coverage probe in the clone, reverted): with `agent-contract`
removed from `agents/smith.md`'s `skills:` list, the eleven modules that read
an agent's frontmatter (`test_every_agent_reads_the_contract.py`,
`test_a_section_marked_for_one_role_reaches_only_that_role.py`,
`test_the_agent_contract_holds_the_universal_rules.py`,
`test_the_payload_meter_says_what_it_measured.py`,
`test_first_setup_asks_once.py`, `test_the_sealer_guarantees.py`,
`test_a_moved_rule_leaves_its_definition.py`,
`test_the_seal_is_taken_once_by_the_sealer.py`, `test_evals_layout.py`,
`test_every_orchestrator_act_names_its_delivery.py`,
`test_chain_hooks_hardening.py`) and the five others the frontmatter grep
names all passed; only the sealer's own two pins caught the same edit on
`agents/sealer.md`. The contract arriving before the first tool call is the
mechanism every rule above rests on.

The skip reasons also name "phase 4" and "phase 5 of #957", phases that are
now #967 to #970 (`plan.md` rows 4 and 5), so the skip has no end in this
item. Keep the skip for the shape, and hold the preload for every definition:

```python
@pytest.mark.parametrize("path", AGENTS, ids=name)
def test_every_definition_preloads_the_contract(path):
    """The contract arrives by the `skills:` list, rewritten definition or
    not; the shape case skips the four #967 to #970 rewrite, this one skips
    none."""
    head, _body = split(read(path))
    assert head is not None and "agent-contract" in listed_skills(head), name(path)


# Skipped by name, each until the issue that writes it anew deletes its entry.
NOT_YET_REWRITTEN = {
    "agents/framer.md": "#968",
    "agents/smith.md": "#967",
    "agents/scribe.md": "#970",
    "agents/sealer.md": "#969",
}
```

and the skip message reads `f"{name(path)} is written anew in {NOT_YET_REWRITTEN[name(path)]}"`.

answer: Fixed as proposed: `test_every_definition_preloads_the_contract` holds `agent-contract` in the `skills:` list of every file under `agents/`, skipping none, and was seen red with it removed from `agents/smith.md`. The shape case's skips name #967 to #970 and its message reads as proposed.

### 4. The README and the docstrings state rule 1 as "recall has not fallen" while the code lets one find go

severity: should
location: `evals/README.md:29`, `evals/scripts/noninferiority.py:23`, `evals/scripts/noninferiority.py:569`
verdict: fixed 857aa1af

`verdict` lets recall fall by one find where every lost truth grader is
still found by some new run (`noninferiority.py:612`, the `noise` branch,
pinned by `rule 1: one find fewer, still found by a new run, is noise`). The
list this diff writes into `evals/README.md:29`, the module docstring
(`:23`) and `verdict`'s docstring (`:569`) all say "recall not fallen" and
nothing else. Phase 3's own record leans on the allowance: "Recall fell by
one find (`truth-untrue-body` 1/2), which rule 1 reads as noise"
(`phases/phase-3.md:210-211`). A reader of the README judging a record by
hand reads that record as failing rule 1. Read, not executed.

```markdown
1. recall has not fallen, except by one find where every truth grader that
   lost it is still found by at least one new run;
```

and the same clause in the two docstrings.

answer: Fixed in the commit of finding 2: `evals/README.md:29`, the module docstring and `verdict`'s docstring state rule 1 with its one-find allowance in the round's words, and `verdict`'s docstring now also lists the no-result cases, the unrun case among them.

### 5. The agent-set document says the contract was numbered anew from §1, and the build reused §16 for another rule

severity: should
location: `docs/the-agent-set.md:26`, `seal/specs/1792126889-every-agent-is-written-anew-from-its-job/questions.md:15`
verdict: fixed 901cd79b

`docs/the-agent-set.md:26-31` says "The contract was written anew and
numbered anew from §1 in #957". Phase 3 did not do that: each rule kept its
number, old §16 joined §11, and old §17 moved up to §16
(`phases/phase-3.md:39-58`, read against the contract at 2dfa53a9). So the
sentence is false of the tree, and `questions.md:15-17` ("The contract is
renumbered from §1, and every citation in the tree is rewritten") says the
same false thing as something the tree settled.

The number 16 is what makes it more than wording. Before this item, §16
meant where the `seal/` root resolves; now it means the commit rule. A
spawn prompt or round record that cites §16 from before 2dfa53a9 now names
a different rule, which is the one failure the never-reused rule exists to
prevent, and the edition that states the rule is the one that reused a
number. Retiring §16 in place as a one-line pointer and keeping the commit
rule at §17 would have moved no number at all; the six commit-rule
citations the phase rewrote would go back. Either is a design choice for
the orchestrator; the sentence has to match whichever stands.

```markdown
**From this edition, section numbers are never reused and never
re-ordered.** #957 wrote the contract anew and kept each rule's number where
the rule stayed: the old §16 joined §11, the old §17 moved to §16, and the
four new rules took §17 to §20. From that edition on, a prompt saying *§3 is
narrowed this round*, and a round record compared with another six months
later, both hold only while §3 still means what it meant. A retired rule
keeps its number and becomes one line naming what replaced it, and a new
rule takes the next number.
```

answer: Fixed by making the sentences say what the build did; the numbers stand as built (§16 is the commit rule, the old §16 is part of §11). `docs/the-agent-set.md` takes the round's paragraph, `questions.md:15` says the same, and the docstring of `test_every_cited_section_exists`, which also said "numbered anew", names the two moved numbers.

### 6. Phases 3 to 6 of the plan carry their Status in a fifth cell that a renderer drops

severity: should
location: `seal/specs/1792126889-every-agent-is-written-anew-from-its-job/plan.md:153`
verdict: fixed 927f64e9

The Phases table has four columns. Rows 3, 4, 5 and 6 end `... || <status>
|`, which is five cells (`awk -F'|'` over the table, executed: rows 1, 1b
and 2 have four, rows 3 to 6 have five). The Status cell of each is empty
and the text "314f6166, closed by the orchestrator ...", "moved to #967 ..."
and the rest sits in a fifth cell, which GitHub's table extension drops
(it ignores cells past the header's count). On the pull request page the
plan reads as if phases 3 to 6 were open, and `plan.md:158` says the column
is "where the work records how far it got". No script reads the column
(`git grep` over `skills`, `hooks`, `evals`, executed), so this is what a
person and the next agent reading the rendered or parsed table see.

The fix deletes the empty cell in each of the four rows, for example row 3:

```markdown
... `git grep -n -E "§[0-9]+"` over `agents/ skills/ docs/ templates/ hooks/ tests/ CONTRIBUTING.md` naming only sections the contract has, which T3 holds | 314f6166, closed by the orchestrator: ... |
```

answer: Fixed: the empty cell is gone from rows 3 to 6, and `awk -F'|'` over the table now gives four cells for each of rows 1, 1b and 2 to 6.

### 7. The changelog fragment carries no per-agent table and no commit for any figure, and calls 12 defects run twice "24 known defects"

severity: should
location: `seal/specs/1792126889-every-agent-is-written-anew-from-its-job/changelog.md:10`
verdict: fixed 927f64e9

`spec.md` S16 and §*A number in this frame names its moment or its bound*
ask the fragment for a per-agent table of preload bytes, tokens read, spend
and outcome at the baseline and at the close, "each figure with the commit
it was read at". `plan.md` row 6 was narrowed to phases 1 to 3, not to
prose. The fragment states 27,032 and 76,019 bytes, 16 and 13 finds, and
9.2%, each without a commit or record. I recounted each, executed: the
bytes are `agents/warden.md` 10,495 plus the contract 16,537 against
18,031 + 20,368 + 16,620 + 21,000 at af9c924b; the finds and the per-call
figures are `evals/warden-phase-3.md`'s, which `check` reproduces. The
figures are right; what is missing is where a reader checks them.

"It found 16 of 24 known defects where it found 13" is wrong in its noun:
the warden's suite holds 12 truth graders, each run twice, so 24 is
chances, not defects (`evals/warden-phase-3.md`, grader rows, executed).

```markdown
  ... On this repository's evaluation, against the warden at af9c924b
  (`evals/warden-phase-3.md`, read at 314f6166), it found 16 of 24 known
  defects over two runs of 12 where it found 13, wrote fewer false findings,
  and read 9.2% fewer tokens per tool call. Nothing to do.

  | Agent | Preload bytes, af9c924b → 2dfa53a9 | Tokens per tool call | Spend USD | Verdict |
  |---|---|---|---|---|
  | warden | 76,019 → 27,032 | 89,100.4 → 80,940.4 | 36.0352 → 36.6656 | pass (`evals/warden-phase-3.md`) |
```

with one row each for the smith, the framer and the sealer from their
phase-3 records, the framer's `fail` and the sealer's "not the sealer's
result" stated as they are.

answer: Fixed for the agents this item measured after the contract: the fragment says "12 known defects, each run twice, 16 of 24 finds where ... 13", and a table gives the warden, the smith and the framer their preload bytes, tokens per tool call, spend and verdict, the framer's `fail` stated, each figure the tree at af9c924b against 93c1878c, read from `evals/<agent>-phase-3.md` at 314f6166. The 16 and 13 were recounted from the warden record's 12 truth rows. The sealer has no row: its phase-3 record measures a definition #969 rewrites, which `overview.md` §*Not done* already says.

### 8. The warden's hand-back check reads the session's directory, not the branch worktree its record is in

severity: should
location: `agents/warden.md:47`
verdict: fixed 0067cff0

Step 7 names `python3 skills/code-review/scripts/chain_check.py --baseline
<base> --worktree` with no `--root`. `chain_check.py`'s `--root` defaults to
`.` (`chain_check.py:1747`, read). The warden works in a clone (step 2) and
writes its record into the branch worktree, "never the main checkout"
(`agents/warden.md:71-74`), while each Bash call starts in the session's
directory. Where the session sits in the main checkout and the branch in a
worktree of its own, the check reads a tree that does not hold the record
and passes or refuses on the wrong files. The eval cases cannot see this,
since their scaffold has one tree. This round's own spawn prompt adds
`--root <worktree>` for that reason.

```markdown
   and `answer:` lines, and return its path. Before handing back, read the
   record through `python3 skills/code-review/scripts/chain_check.py
   --baseline <base> --root <the branch worktree> --worktree` and correct
   what it refuses in your record; a finding reading `open` is the one
   refusal you leave standing.
```

answer: Fixed as proposed, still one sentence: the command names `--root <the branch worktree>`. `test_the_warden_checks_its_record_in_the_branch_worktree` reads the command and was seen red with `--root` taken out.

## Confirmations

confirms: none
The eight side files re-derive byte for byte. `noninferiority.py run
--from-raw` over the kept raw output for `baseline-<agent>` and
`<agent>-phase-3`, warden, smith, framer and sealer, then `cmp` with
`evals/*.json`: all eight exit 0 and identical (executed).

confirms: none
The four phase-3 records reproduce and `check` agrees with them. `compare`
over the re-derived sides gives files identical to `evals/<agent>-phase-3.md`
(`diff` exit 0, all four); `check` exits 0 for the smith and the warden and 1
for the framer (rule 5, 33,595.1 against 28,253.1 tokens per call) and the
sealer (rules 3 and 5); `check` on `warden-phase-2.md` and
`warden-phase-2-run-1.md` exits 1 on the rule 3 shortfalls the phase records
name (executed).

confirms: none
Rules 2, 4 and 5, the no-result guards on tokens, tool calls and preload
bytes, and the record read-back judge what `spec.md` §*How the rewrite is
proved not worse* says: every rule against the baseline, tokens summed over
every `modelUsage` model and divided by every `tool_use` block, cross-
multiplied with no margin, spend and seconds written and never judged, a
missing count, missing calls or zero calls giving `no result`
(`noninferiority.py:213-293`, `:563-656`, `:810-878`, read). Finding 2 and
finding 4 are the two places it does not.

confirms: none
The contract rewrite drops narration, not rules, outside §2. Read section by
section against af9c924b: §1, §3 to §16 keep their rule sentences (§3's
ambiguity clause, §4's three labels and their answerer, §6's four withheld
acts, §7's whose-leaving test, §8's three shapes, §9's gate grammar, §11's
two roots and record language, §12 to §15, §16's two reasons); what left is
incident accounts and the "sat in two definitions" histories. The removed
pins (`phases/phase-2.md:285-296`, `phases/phase-3.md:107-130`) pinned
incident text or figures that moved to §10 and the per-segment bars, except
the frontmatter pin of finding 3.

confirms: none
The warden rewrite keeps its rules. Against the definition at af9c924b: the
clone path, the record path, the runner and `uv` venv, the coverage probe,
the account-is-a-claim and stated-intent rules, the reference root, the
carried-fact table, `deferred`, the verifying round with its regression and
reopening lines, the capped round, the suite-label audit and its `## Not judged`
row, the reviewed mark it never writes, the parity mark and the
no-real-identifiers rule all stand (`agents/warden.md:15-166`, read). The
1.89 figure and the proof block left on purpose (`spec.md` §*Removes*).

confirms: none
The citation rewrite names the right sections where sampled. Of the 78
`§N` sites outside the contract, `seal/specs/` and `changelog/` (`git grep`,
executed), I read every contract citation of §2, §6, §10, §11, §13 and §16
and the moved ones in `skills/implement/orchestration.md:32, 441, 528, 532`,
`skills/verify/scripts/broad_gate.py:704`, `hooks/implementer.py:16`,
`templates/sdd-routing.md:38`; each names the rule its sentence means,
except `agents/sealer.md:106` (finding 1).

confirms: none
`bin/rules --check` exits 0 (463 targets in 60 files), and `bin/test
tests/test_broad_gate_rule.py
tests/test_the_agent_contract_holds_the_universal_rules.py
tests/test_a_rewritten_definition_proved_non_inferior.py
tests/test_every_agent_reads_the_contract.py tests/test_evals_layout.py -q`
exits 0, 171 passed and 4 skipped (executed, in the clone at 2dfa53a9).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the new §2 caused sealer run 004 to write no `guarantee.md`; I read the phase record's account and did not re-read that trace | `phases/phase-3.md:213-230` | #969's measurement |
| The framer's rule 5 regression (+18.9% tokens per call) and whether this item may close on it | `evals/framer-phase-3.md` | the orchestrator, and #968 |
| CI on its three legs, and the full suite, lint and typecheck at 2dfa53a9 | the branch | the orchestrator, after the rounds settle |
| The `.test_durations` refresh commit 4b0ed48d (14,795 lines) against the durations artifact it names | `.test_durations` | the orchestrator |
| Whether a warden spawn in a user repository resolves the plugin paths step 1 describes; the evals run inside the plugin tree | `agents/warden.md:25-29` | a run of the warden outside this repository |

## Probes

| Command | Result |
|---|---|
| `noninferiority.py run --from-raw <kept raw>/<side>.raw --out <scratch>` for the eight sides, then `cmp` with `evals/` | exit 0 each; all eight byte-identical |
| `noninferiority.py compare --agent <a> --phase 3` over the re-derived sides, `diff` with `evals/<a>-phase-3.md`, and `check` on the committed records | compare exit 0 each, diff exit 0 each; check: warden 0, smith 0, framer 1, sealer 1, warden-phase-2 1, warden-phase-2-run-1 1 |
| `python3 -I test_tmp_verdict.py <clone>`: the smith's and the framer's phase-3 side cut to one case, `verdict` on each | smith count-words alone `pass`, smith is-palindrome alone `pass`, the other six `fail` on rule 5; the warden minus one case `no result` |
| `agents/smith.md` and `agents/sealer.md` with `agent-contract` removed from `skills:`, then `bin/test` over the eleven frontmatter modules, then the five others | exit 1: 2 failed (both the sealer's), 847 passed; the five others exit 0, 147 passed; both files restored |
| `bin/test` over the five modules named in the last confirmation; `bin/rules --check` | exit 0, 171 passed, 4 skipped; exit 0 |
