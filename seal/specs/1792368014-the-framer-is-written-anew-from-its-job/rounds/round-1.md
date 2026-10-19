# 1792368014-the-framer-is-written-anew-from-its-job — review round 1

target: 749ebd7f against release/v0.22.2

This round reviewed the branch's own change, `git diff 2ff7b963...749ebd7f`,
read against the merge base. The two merges (461f00c6, ae3f6ccf) brought in
work items reviewed elsewhere, and only their conflict resolutions were read
here. This is the first round of the work item, so no fact was carried from
an earlier record: every coordinate below was opened or run this round, in a
`git clone --no-local` of the branch at 749ebd7f.

## Findings

### 1. Two reading rules of the old framer were dropped, and neither `## Removes` nor the overview names them

severity: should
location: `agents/framer.md:50-60`, `tests/test_waiver_decided_at_start.py`
evidence: executed `git show 2ff7b963:agents/framer.md`, `git grep -n -i -E 'passing test is not|not a claim to re-establish|argued through|already argued|re-?argue' -- . ':!seal/specs' ':!changelog' ':!.test_durations'`
verdict: fixed 5bdad9db

The old reading list told the framer what to do with two of the sources it
reads, not only to read them. Under the `Enforced by:` lines it said *a rule
with a passing test is not a claim to re-establish* (`agents/framer.md:144-146`
at 2ff7b963). Under the earlier work items it said *a decision already argued
through three rounds does not get re-argued in your `plan.md`* (`:153-154`
at 2ff7b963). The new step 4 keeps both sources and drops both consequences.

The frame's `## Removes` does not name either sentence (`spec.md:223-239`,
read). The overview's row *Removals `## Removes` did not name* lists six
other removals and not these two (`overview.md`, the first divergence row,
read). The search above finds neither rule anywhere else in the tree, so
they were dropped rather than moved. The implementer claimed that the
removed phrases are gone and that `spec.md` §*Data & interfaces* lists every
section the new file keeps (`phases/phase-1.md`, read). Both claims hold.
Neither claim accounts for these two rules, which were inside a section the
new file keeps as step 4.

Why it matters: a framer that reads an earlier work item's rounds and is not
told to inherit what they settled can re-open, in its Alternatives table, a
decision three rounds already closed. Inheriting settled decisions is the
reason the step sends it to those rounds. The new rule *What the tree can
answer, you answer* (`agents/framer.md:104-111`) covers judging in general.
It does not tell a framer that a decision argued in earlier rounds stands.

Any edit to `agents/framer.md` changes the definition phase 2 measured
(sha256 `f70b2eb3…`, `phases/phase-4.md`). Whether that re-opens the
measurement is a row of `## Not judged`. The other answer is to record both
removals, with their grounds, in the overview's divergence row, and that
changes no measured file.

```markdown
4. Read wide, in the order of authority. `docs/` first, which outranks the
   ticket and the code alike. The `Enforced by:` lines and the tests they
   name: a rule with a passing test is not a claim to re-establish.
   `seal/follow-up.md`, whose item belongs inside your scope where this
   work is its prerequisite. The earlier work items under `seal/specs/`,
   their round records included where they still stand: a released work
   item's round records leave the tree at the next release, and are read at
   the release tag after that (`git show v<X.Y.Z>:<path>`). A decision those
   rounds argued through is not argued again in your `plan.md`. The ticket
   and its comments, and `seal/parity.md` where it is declared, which puts
   the original between the ticket and the code. A reference root
   (`templates/config.md` §*Reference specs*) is read where the work touches
   what it describes, and cited in `spec.md` by path.
```

```python
# tests/test_waiver_decided_at_start.py, beside the other framer cases
def test_the_framer_inherits_what_the_tree_already_settled():
    """The reading list says what each source settles, not only that it is
    read: a rule with a passing test, and a decision earlier rounds argued
    through, are not re-opened in the frame."""
    framer = flat(read(*FRAMER))
    assert "a rule with a passing test is not a claim to re-establish" in framer
    assert "is not argued again in your `plan.md`" in framer
```

answer: Both rules are back in step 4 as the round worded them: *a rule with a passing test is not a claim to re-establish* under the `Enforced by:` lines, and *a decision those rounds argued through is not argued again in your `plan.md`* under the earlier work items. The pin is `tests/test_waiver_decided_at_start.py::test_the_framer_inherits_what_the_tree_already_settled`, seen red on the definition at 1bdbb586 and named in the judging rule's `Enforced by:`. A `mutation-check` of each sentence turned it red. No other file states either rule (`git grep`).

### 2. The reframe rule says to rewrite `plan.md` as §*The run* says, and §*The run* does not say how

severity: should
location: `agents/framer.md:156-164`, `tests/test_waiver_decided_at_start.py`
evidence: executed `git grep -n -i -E 'closed phase|new phase rows|reframe' -- skills docs agents templates`, `sed -n 462,536p docs/the-review-record.md`
verdict: fixed 5bdad9db

The new rule reads: *open `docs/the-review-record.md` §The run, rewrite
`plan.md` and `spec.md` as it says* (`agents/framer.md:159-161`). §*The run*
(`docs/the-review-record.md:462-536`) says that the work item goes back to
its framer, that the framer writes the `Reframed` line, and that the run goes
on with the redesign's build. It says nothing about how `plan.md` is
rewritten.

The old definition said it in place: *You rewrite `plan.md` — new phase rows
for the redesign, every closed phase keeping its commit — and `spec.md`
where the scope moves* (`agents/framer.md:303-305` at 2ff7b963). The search
above finds that rule in one other place,
`skills/code-review/orchestration.md:153`. That line is a row of the
orchestrator's spawn table, which the framer is not told to open. The same
row says the reframe prompt names the round records *and carries nothing
else*, so the spawn prompt will not carry the rule either. `## Removes` does
not name the clause (`spec.md:223-239`, read).

Why it matters: a reframing framer told to *rewrite* `plan.md` can replace
the Phases table. A closed phase's Status cell is the commit that closed it
(`skills/implement/SKILL.md:378-381`, read), and replacing the row loses the
one durable record of what was built before the reframe. The pointer also
sends the framer to a section for a rule that section does not hold, so the
framer reads §*The run* and finds nothing to follow.

The fix keeps `RUN_OWNS_THE_RULE`, the phrase
`tests/test_the_rules_have_one_owner.py:55` pins in this file. The cost note
under finding 1 applies here too.

```markdown
**The one route back is the review chain's.** A builder that finds the
frame does not hold writes it into its phase record and hand-back, and you
are not spawned again for it. You are when the orchestrator routes a
`regression:` to you with that run's round records: open
`docs/the-review-record.md` §*The run*, then rewrite `plan.md` with new
phase rows for the redesign, every closed phase keeping its commit, and
`spec.md` where the scope moves. Add `Reframed <date> by <who>, after round
<N>.` under your mark, never in its place. `docs/the-review-record.md`
§*The run* owns that rule.
Enforced by: tests/test_the_rules_have_one_owner.py::test_every_link_names_the_owner, tests/test_waiver_decided_at_start.py::test_a_reframe_keeps_every_closed_phase
```

```python
# tests/test_waiver_decided_at_start.py, beside the other framer cases
def test_a_reframe_keeps_every_closed_phase():
    """A reframe adds phase rows and keeps each closed phase's commit.
    §*The run* owns the route and does not say how `plan.md` is rewritten,
    so the definition says it."""
    framer = flat(read(*FRAMER))
    assert "every closed phase keeping its commit" in framer
```

answer: The reframe rule now says to open §*The run*, then rewrite `plan.md` with new phase rows for the redesign, every closed phase keeping its commit, and `spec.md` where the scope moves. It still ends with the sentence naming `docs/the-review-record.md` §*The run* as the rule's owner, so `RUN_OWNS_THE_RULE` holds. The pin is `tests/test_waiver_decided_at_start.py::test_a_reframe_keeps_every_closed_phase`, seen red first, named in the rule's `Enforced by:`, and red under a `mutation-check` that drops the clause. The one other statement of the rule, `skills/code-review/orchestration.md:153`, agrees with it and stands.

### 3. The hand-back step tells the framer to label every claim `read`, and the framer runs commands

severity: should
location: `agents/framer.md:71-72`, `tests/test_a_question_says_who_can_answer_it.py`
evidence: read `agents/framer.md:71-72`, `agents/framer.md:52-57`, `agents/framer.md:148-153`, `skills/agent-contract/SKILL.md:62-70`, `seal/specs/1792368014-the-framer-is-written-anew-from-its-job/spec.md:78-158`
verdict: fixed 5bdad9db

Step 8 reads: *Every claim is `read`, because you executed nothing*
(`agents/framer.md:71`). The same file tells the framer to run commands: a
released record is read with `git show v<X.Y.Z>:<path>` (`:56`), and a large
file with `sed -n` beside a `wc -l` (`:152-153`). Contract §4 labels what was
run `executed` (`skills/agent-contract/SKILL.md:62-70`). This work item's own
frame, written by the framer, labels seven facts `executed`, among them a
`shasum -a 256` and a `git diff --stat` (`spec.md:81`, `:84`, `:87`, `:92`,
`:113`, `:141`, `:158`). So the framer that drew this frame did not follow the
sentence, and following it would have mislabelled those facts.

The rewrite carried the sentence over from the old `## Report`
(`agents/framer.md:325-326` at 2ff7b963), so it predates this branch. It is
a finding here because the rewrite restated the step, and the step is what
the framer reads and acts on. A hash labelled `read` sends the next reader
to open a file when the claim can only be checked by running the command
again. What is true is narrower: the framer runs no check of the
repository's (`## Job`, `agents/framer.md:21-23`). That is what the sentence
should say. No test pins the sentence today (`git grep -n -E 'Every claim
(in it )?is|executed nothing'` finds only `agents/framer.md:71`). Contract §14
asks for a pin on the corrected text.

```markdown
8. Hand back. Label each claim as contract §4 says: a fact a command you
   ran gave you, a `git show`, a `grep`, a `wc -l`, is `executed`, and what
   you opened is `read`. You ran no check of the repository's, and the
   report says so. The report stands without a file opened beside it:
```

```python
# tests/test_a_question_says_who_can_answer_it.py, beside the other report cases
def test_the_hand_back_labels_what_the_framer_ran_as_executed():
    """A framer runs `git show`, `grep` and `wc -l` while it reads, and a
    frame labels those facts `executed`. A hand-back told that every claim
    is `read` misstates them (contract §4)."""
    report = report_of("framer.md")
    assert "executed nothing" not in report
    assert "is `executed`" in report
```

answer: Step 8 now labels claims as contract §4 does: a fact a command gave, such as a `git show`, a `grep` or a `wc -l`, is `executed`, and what was opened is `read`. It says the framer ran no check of the repository's, which is the narrower claim that stays true. The pin is `tests/test_a_question_says_who_can_answer_it.py::test_the_hand_back_labels_what_the_framer_ran_as_executed`, seen red first and red under a `mutation-check` that relabels the command's fact `read`. No other definition says every claim is `read` (`git grep`).

## Confirmations

confirms: none
The deleted exemption and the deleted preload case leave nothing unheld.
`shape_problems` refuses any `skills:` list other than `agent-contract`
alone, and the shape case is parametrised over the `agents/*.md` glob with
no skip left (`tests/test_every_agent_reads_the_contract.py:25`, `:73-90`,
`:116-126`, read). The removed `test_every_definition_preloads_the_contract`
asserted only that `agent-contract` is among the listed skills, which the
shape case's equality already implies. No `Enforced by:` line, document or
test names the removed case or `NOT_YET_REWRITTEN` outside `seal/specs/`
(executed, `git grep -n -i -E 'not yet (written|rewritten)|written anew in
#|preloads_the_contract'`). The implementer's claim in the overview's fifth
divergence row holds.

confirms: none
Every heading the framer names exists. `implement` carries
`## The language the records are written in` at `:33`,
`### 1. Read the spec before the code` at `:135` and
`### 3. The SDD file set` at `:294`. `writing-style` carries
`## English prose rules` at `:278` and `## 문장 규칙` at `:43` (executed,
`grep -n` over both files). Step 3's fallback, reading the file whole, covers
a renamed `implement` heading, and no check holds those three headings, as
`plan.md` says. Step 6 has no fallback. Its two headings are held by a
check instead: `named_by_agents` reads every `## ` span in a definition's
`writing-style` step, the framer's included, and requires it to stand in the
skill (`tests/test_a_language_section_of_writing_style_opens_alone.py:55-68`,
read; the module passes, executed). The changelog's *where a heading is not
found, it reads the file whole* is true of `implement` and not of
`writing-style`. The check makes that difference harmless.

confirms: none
The other old rules the rewrite did not keep in the definition stand where
the framer reads them. *A ticket asking for what policy forbids* goes to
`questions.md` under `skills/implement/SKILL.md:142-147`, inside §1, which
step 3 opens. *Only where different answers mean different code does the
work wait* is at `:182-184` of the same section. *The first finding round
of a redesign starts the cap's count again* is at
`docs/the-review-record.md:474-478`, inside §*The run* (read). Findings 1
and 2 are the exceptions this round found.

confirms: none
The merges' conflict resolutions hold. The README skills row reads one
preloaded, fifteen on demand and six typed, 22 in all. The fifteen named
are the old thirteen plus `implement` and `writing-style`, in both editions
(`README.md:43`, `README.ko.md:42`, read).
`tests/test_chain_hooks_hardening.py::test_the_readme_group_counts_are_derived_too`
derives the groups from the `skills:` lists and passes (executed). The
paste allowances measure exactly at their new ceilings: framer and scribe
4, framer and sealer 14, framer and smith 24, framer and warden 31
(executed, `shared_counts(tree())` against `BASELINE`). No removed framer
pair still measures above zero.

confirms: none
The check fixed in 6fe805e1 refuses the sentence it was written for. The
0.4.0 sentence read *creates the root at `<repo>/seal/` and nowhere else*
(executed, `git show feceb7c`). The case now folds whitespace and refuses
that clause (`tests/test_first_setup_asks_once.py:327-335`, read). The one
*nowhere else* left in `implement`'s two files is the closing-memo sentence
of `skills/implement/SKILL.md`, which is about something else (executed, a
whitespace-folded search over both files).

confirms: none
The changelog states rule 5's breakdown honestly. The new/old ratio of
tokens per tool call is 0.575. It factors into 0.907 from total tokens and
0.634 from tool calls, 109 against 172 (executed, the arithmetic over
`evals/framer-phase-2.md`'s rows). Most of the fall therefore comes from
the larger call count, and the changelog says so in those words
(`changelog.md`, the last paragraph of the second entry, read). The
baseline is a byte copy of #967's side (executed, `cmp`, exit 0), and
`noninferiority.py check` on `evals/framer-phase-2.md` exits 0 (executed).

confirms: none
The new replace-or-keep case pins a rule nothing else in the suite covers.
Its two phrases stand nowhere in the tests outside that case (executed,
`git grep -n -E 'replaces the structure|as an equal of'`), and the old
file carries neither phrase (executed, `git show 2ff7b963:agents/framer.md`
with a count of 0). So the claim that the case was red on the old file
holds as far as reading can settle it. The red run itself is the
implementer's claim and was not repeated.

confirms: none
The docstring claim in `tests/test_a_moved_rule_leaves_its_definition.py:46-50`
holds. The widest run a definition shares with a contract section is the
sealer's 8 words with §2, and the framer's is 5 words with §11 (executed,
`longest_shared` over every definition and section).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a fix to `agents/framer.md` after phase 2's side, as findings 1 to 3 propose, re-opens the measurement. S12 asks for a new side where a section of the read set changes, and phase 3 allows no third side. Recording findings 1 and 2 in the overview changes no measured file | `spec.md:184`, `plan.md` Phases row 3 | the orchestrator |
| The causal sentence of the changelog, *the framer reads each section as its own ranged call, so most of the fall in tokens per call is the larger call count*. The per-run table that supports it was read off traces kept outside the tree, and the baseline has no per-run figures to set the extra 63 calls against | `changelog.md`, `phases/phase-2.md` | the orchestrator, who holds the raw output; the statistic is #992's |
| The full suite, the repository-wide lint and the typecheck on this branch. The suite stays `unverified` here, as contract §2 says | the branch at 749ebd7f | the orchestrator's broad gate, after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test` over `test_every_agent_reads_the_contract`, `test_waiver_decided_at_start`, `test_the_handoff_before_round_one`, `test_a_question_says_who_can_answer_it`, `test_a_phase_hands_the_next_one_a_record`, `test_chain_hooks_hardening`, `test_a_reference_root_is_read_and_never_taken`, `test_no_passage_is_pasted_into_a_second_file`, `test_a_moved_rule_leaves_its_definition`, `test_first_setup_asks_once`, `test_a_language_section_of_writing_style_opens_alone`, `test_the_rules_have_one_owner`, `test_a_rewritten_definition_proved_non_inferior` | exit 0, 564 passed |
| `bin/rules --check` | exit 0, all 548 targets in 60 rule files resolve |
| `shared_counts(tree())` from `tests/test_no_passage_is_pasted_into_a_second_file.py`, the framer's pairs | 4, 14, 24 and 31, each equal to its `BASELINE` entry |
| `longest_shared` from `tests/test_a_moved_rule_leaves_its_definition.py`, every definition against every section | framer 5 (§11), scribe 4 (§7), sealer 8 (§2), smith 6 (§5), warden 6 (§2) |
| `cmp` of `evals/baseline-framer.json` with #967's `evals/framer-phase-4.json` | exit 0 |
| `python3 evals/scripts/noninferiority.py check` on `evals/framer-phase-2.md` | exit 0 |
