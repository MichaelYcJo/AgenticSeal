# Review round 1: 1792627930-the-section-sign-is-still-syntax

target: a9d9423c against release/v0.22.3

This is round 1, so no fact is carried from an earlier round. Every
coordinate below was opened or run in this round, in a `git clone --no-local`
of the branch at a9d9423c.

## Findings

### 1. The new section-sign sweep is not registered with the git-listing census, and CI fails on three legs

severity: must
location: `tests/test_a_shrunken_corpus_declines_to_judge.py:154-183`, `tests/test_no_living_file_writes_the_section_sign.py:27-45`
evidence: executed `bin/test tests/test_a_shrunken_corpus_declines_to_judge.py -q`
verdict: open

CI run 39711220166 at ce84116a failed on the ubuntu leg, macOS shard 1 and
Windows shard 1. The coordinator read that run; this round reproduced it.
ce84116a and a9d9423c differ only in `spec.md`. The run here gives 2 failed
and 15 passed. Both failures have one cause.

`tests/test_a_shrunken_corpus_declines_to_judge.py` keeps a census of every
test scope that builds a path list from git. A scope missing from all six of
its tables turns the case red. Phase 3 added
`tests/test_no_living_file_writes_the_section_sign.py#signs`, which lists
paths with `git_listing(root, "ls-files")` and does apply `on_disk` at line
34. It was never added to `APPLIES_THE_SHARED_GUARD`. So
`test_no_scope_in_the_suite_lists_paths_from_git_without_a_guard` (line 420)
names it as unaccounted. `test_an_unguarded_scope_is_named_although_a_module_is_mid_edit`
(line 600) expects the planted scope to be the only unaccounted one, and
`signs` is a second. Its message prints only the dict, which hides the
shared cause.

The phase 3 record says the new module's nearest group is
`tests/test_no_real_identifiers.py`. That module's `tracked_text_files` is the
first row of this table, and the new sweep was not entered beside it. No
phase boundary run included this module.

Applying the fix below in the scratch clone turned the module green: 17
passed. The edit was then reverted.

```python
    # #967's T5 reads every tracked file for a citation of `implement`'s
    # headings. It judges what it finds, so it skips the missing half.
    "tests/test_the_set_a_work_item_always_has.py#cited_files": 1,
    # #1005's sweep for the section sign over every tracked living file. It
    # judges what it finds, so it skips the missing half.
    "tests/test_no_living_file_writes_the_section_sign.py#signs": 1,
}
```

answer:

### 2. Deleting the fence agreement case leaves the three fence walks and the unclosed report of `fence_only` held by nothing

severity: should
location: `tests/test_unverified_rows_close.py:2502-2520`, `hooks/blocks.py:154-175`
evidence: executed `bin/mutation-check hooks/blocks.py --replace '    return hidden, opened_at' '    return hidden, None' --tests 'bin/test tests/test_routing_is_recorded.py tests/test_one_table_walker_reads_what_gfm_renders.py tests/test_the_release_check_watches_what_ships.py tests/test_the_seal_is_taken_once_by_the_sealer.py tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py tests/test_a_declared_label_reaches_the_tracker.py tests/test_the_mode_question_is_asked_once.py tests/test_the_hooks_hide_what_a_renderer_hides.py tests/test_unverified_rows_close.py -q -x' --timeout 400`, `git checkout 0d62145a`, `bin/mutation-check hooks/blocks.py --replace '    return hidden, opened_at' '    return hidden, None' --tests 'bin/test tests/test_unverified_rows_close.py -q -x -k agrees_with_the_config_reader' --timeout 300`
verdict: open

`spec.md` `## Removes` says the two in-step cases can go because "One copy
has nothing to agree with". That holds for
`test_the_walks_line_rule_is_the_readers`. It holds for only one half of
`test_the_fence_rule_agrees_with_the_config_reader`. That case compared two
copies of the delimiter rule. It also compared three walks over 19 shapes:
`unverified_check.py#fence_spans`, `hooks/blocks.py#fence_only`, and
`hooks/config.py#fence_map` with the comment walk behind it. It checked which
lines each one fences and where each one reports an unclosed block. After
phase 5 those are still three loops (`fence_spans` at
`skills/verify/scripts/unverified_check.py:291`, `fence_only` at
`hooks/blocks.py:154`, and the `walk` loop at `hooks/blocks.py:301`). They
call one delimiter rule, but each keeps its own state. The facts that they
agree, and that `fence_only` reports the opener of a fence that never
closes, still ship.

I broke `fence_only` so that it never reports an unclosed opener. At HEAD
the cases survived: no case in the nine modules that reach `fence_only` or
`fence_map` noticed (exit 1, SURVIVED). At the base, the deleted case alone
caught the same mutation (exit 0, red). So the deletion left a shipped fact
held by nothing. The other three mutations of this kind were caught at HEAD:
the closer length check, the closer character check and the unclosed span in
`fence_spans` (round probes M1, M2 and M4). The 19 shapes were run once more
in this round, against the three walks at HEAD, and all agree. So the case
below passes as written.

Keep the agreement half of the deleted case and drop its copy half:

```python
FENCE_SHAPES = [
    ["```", "x", "```"],
    ["~~~", "x", "~~~"],
    ["   ```", "x", "   ```"],
    ["    ```", "x", "    ```"],
    ["```", "x", "    ```", "y", "```"],
    ["```python", "x", "```"],
    ["```", "x", "```python", "y", "```"],
    ["```", "x", "```   ", "y"],
    ["````", "```", "x", "````"],
    ["```", "x", "``````", "y"],
    ["```", "x", "~~~", "y", "```"],
    ["~~~", "```", "x", "~~~"],
    ["```x`", "y", "```"],
    ["``` `x`", "y"],
    ["~~~ `x`", "y", "~~~", "z"],
    ["``", "x", "``"],
    ["```", "x", "y"],
    ["a", "```\r", "x\r", "```\r", "b\r"],
    ["| a |", "```", "| b |", "```", "| c |"],
]


@pytest.mark.parametrize("lines", FENCE_SHAPES, ids=range(len(FENCE_SHAPES)))
def test_the_fence_walks_agree_shape_by_shape(lines):
    """The delimiter rule is written once, in `hooks/blocks.py`, and three
    walks still apply it, each with its own state: `uc.fence_spans`,
    `blocks.fence_only`, and the walk behind `hooks/config.py#fence_map`.
    They agree on which lines are fenced and on where a block that never
    closes opened."""
    from conftest import load_hook_module

    spec = importlib.util.spec_from_file_location(
        "specseal_config_for_fence_walks", os.path.join(ROOT, "hooks", "config.py")
    )
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    blocks = load_hook_module("blocks.py", "specseal_blocks_for_fence_walks")
    fenced = set()
    for first, last in uc.fence_spans(lines):
        fenced.update(range(first, len(lines) if last is None else last + 1))
    unclosed = [first for first, last in uc.fence_spans(lines) if last is None]
    shown, opened_at = config.fence_map(lines)
    assert fenced == set(range(len(lines))) - {n for n, _ in shown}
    assert unclosed == ([] if opened_at is None else [opened_at])
    assert blocks.fence_only(lines) == (fenced, opened_at)
    walked = blocks.walk(lines)
    claimed = {n for n in range(len(lines)) if not walked.uncertain[n]}
    assert set(walked.hidden()) & claimed == fenced & claimed
```

answer:

### 3. The contract citation reader neither reads nor refuses a near-miss spelling, so a dangling number in one passes

severity: should
location: `tests/test_the_agent_contract_holds_the_universal_rules.py:75-76`
evidence: executed `.venv/bin/python test_tmp_round1_probes.py`
verdict: open

`spec.md` *Grounding* holds this work to "A check reads one spelling and
refuses a near miss at its line". `CITATION` reads `contract rule <N>` only.
The probe handed `dangling` each of these three in `skills/x/SKILL.md`:
`Contract Rule 21`, `contract rules 7 and 21` and `the contract's rule 21`.
Each came back empty. The reader neither read the citation nor refused it,
so the dangling 21 passed. The base reader read the possessive
(`[Cc]ontract(?:'s)?`) and the list form, so this is a narrowing.
`spec.md` scope item 2 forbids the plural and the list form, but nothing
enforces it. A `git grep -P` over the living files finds no such spelling at
HEAD, so the case below is green today.

The other spellings the owner asked about hold. A citation wrapped after
`contract` is read at its start line. A wrap between `rule` and the number
is read too. In `agents/`, `Rule 21` is read. A fence opener in the
reader's input reads the fenced citation, which errs toward refusing.

```python
# A spelling that means a contract citation and is not the one CITATION
# reads: a plural or a list, a possessive, or a capital `Rule`.
NEAR_CITATION = re.compile(r"\b[Cc]ontract(?:'s)?\s+[Rr]ules?\s+\d")


def near_citations(text):
    """[line] where a near miss of `contract rule <N>` starts."""
    return [
        text.count("\n", 0, m.start()) + 1
        for m in NEAR_CITATION.finditer(text)
        if not CITATION.match(text, m.start())
    ]


def test_no_file_cites_the_contract_in_a_near_miss():
    found = [
        f"{rel}:{n}" for rel in tree_files() for n in near_citations(read(rel))
    ]
    assert not found, (
        "cite one contract rule as `contract rule <N>`, one number each: "
        + ", ".join(found)
    )


@pytest.mark.parametrize(
    "text",
    ["Contract Rule 21", "contract rules 7 and 21", "the contract's rule 21"],
)
def test_a_near_miss_citation_is_refused_at_its_line(text):
    assert near_citations("intro\n" + text) == [2]
```

answer:

### 4. The review skill states the regression grounds rule a fourth time

severity: should
location: `skills/code-review/SKILL.md:130-133`
evidence: read `skills/code-review/SKILL.md:130-133`, `docs/the-review-record.md:494-504`, `skills/code-review/orchestration.md:117-122`, `agents/warden.md:120-126`
verdict: open

`spec.md` scope item 11 says a sentence that its home already states is
removed, and only a sentence the home does not state moves there. Phase 4's
record says the `regression:` half was already stated in
`docs/the-review-record.md` *The run*, and that only the `reopens:` half
moved. The commit wrote both halves into *The record*: "The grounds open
with the unit where `regression:` stands". That rule already stands in
`docs/the-review-record.md:500`, in `skills/code-review/orchestration.md:119`
and in `agents/warden.md:124`. This makes a fourth copy, against `CLAUDE.md`
*Repo rule: text an agent or a check reads has one reading*, which bars
stating a value twice. `tests/test_chain_check.py` pins only the phrase
"where `reopens:` stands", so the fix below keeps that case green.

```markdown
- Each finding gives why it matters and its grounds, then the paste-ready
  fix in a fenced block, then its `answer:` line. The grounds open with why
  the earlier close does not hold where `reopens:` stands.
```

answer:

### 5. The closing memo lists as not done the verdict spelling that the frame's Rule changes now rewrites

severity: should
location: `seal/specs/1792627930-the-section-sign-is-still-syntax/overview.md:28-32`
evidence: read `seal/specs/1792627930-the-section-sign-is-still-syntax/overview.md:28-32`, `seal/specs/1792627930-the-section-sign-is-still-syntax/spec.md:279-286`
verdict: open

`overview.md` `## Not done` says `docs/the-review-record.md` *The guarantee*
still spells the verdicts with dashes. It says that `docs/` is the framer's
to change through `## Rule changes`, and that "this work changed no sentence
there". a9d9423c adds that change as the third item of `spec.md`
`## Rule changes`, and this round's replay places it. So the memo now
reports as undone a change the frame has taken. The sealer reads the memo,
and the pull request body copies factual sentences from the records. A
reader of either would take the dash spelling as left behind.

```markdown
`.test_durations` still names the test cases this work removed; CI's
measuring runs rewrite that file, and no case fails on a stale entry, so it
was not edited by hand.
```

answer:

## Confirmations

confirms: none
`spec.md` `## Rule changes` replays against the docs at HEAD. Executed:
`rule_changes.parse` on the spec returns no error and five operations, three
`change` and two `add`. `apply_op` places each one. The changed text reads
`contract rule 3`, `contract rule 11`, and the three verdict shapes that
`skills/code-review/scripts/chain_check.py:107-110` (`VERDICT_SHAPE`) reads.
The two `add` items land under *seal/specs/<work-item-id>/* in
`docs/the-record-layout.md`.

confirms: none
The preamble's list of agent names was read by nothing. Executed: `git grep`
at the base for its words finds only the contract line itself. The one
document citing the preamble, `docs/the-agent-set.md:19-22`, cites it for
how a retired rule keeps its number, and that sentence remains at
`skills/agent-contract/SKILL.md:24-26`. The skill's `description`, which the
harness injects, still names the agents at `skills/agent-contract/SKILL.md:3-4`.

confirms: none
The fence import is one copy. Executed: `fence_opener`, `fence_closes` and
`gfm_lines` of `unverified_check.py` have `hooks/blocks.py` as their code
file. Breaking the closer length check or the closer character check in
`hooks/blocks.py`, or dropping a carriage return from `GFM_LINE_RE`, each
turned the remaining cases red (M1, M2, M5).

confirms: none
Each moved template sentence that was sampled is pinned at its new home.
Executed, each red against a break of the sentence at that home:
`opens rows and does not own their answers` in `skills/implement/SKILL.md`
(T1), `FINDING OUT or WRITING DOWN` in `skills/implement/orchestration.md`
(T2), `goes missing without a trace` in `skills/implement/SKILL.md` (T3), and
the example row of a closed `## Not verified` item, now run through
`check_file` (T4).

confirms: none
Each deleted test function was judged, as the owner asked. Read, except
where a probe is named.
`test_each_section_comment_states_the_failure_it_prevents` held that each
phase-record section and `## Removes` states its failure. The skill and the
framer now state it, and
`tests/test_a_phase_hands_the_next_one_a_record.py#test_each_record_section_states_the_failure_it_prevents`
holds it (T3).
`test_plan_names_the_phase_record_path` held that a reader of the plan finds
the phase-record path and its template. The plan template no longer carries
the pointer. The skill's file-set row names both, held by
`test_skill_file_set_table_carries_the_phase_row` at
`tests/test_a_phase_hands_the_next_one_a_record.py:265-273`.
`test_the_phase_templates_own_path_comment_matches_the_round_templates` held
the spelling of a comment that no longer exists, so no shipped fact is left.
`test_the_template_names_the_three_answerers_and_only_those` and
`test_the_template_says_the_framer_does_not_own_the_answers` are held by
their `test_the_skill_` counterparts against `skills/implement/SKILL.md`
(T1).
`test_another_files_section_in_a_definition_is_not_the_contracts` held a
file-name exception for the section sign in `agents/`. The exception and the
form it excused are gone, as `## Removes` names. Its near relative is
finding 3.
`test_the_walks_line_rule_is_the_readers` held two copies of the line split
equal. One copy is left, which
`tests/test_unverified_rows_close.py#test_the_fence_rule_and_the_line_split_are_the_hooks`
pins. Its behaviour is pinned by
`tests/test_every_reader_ends_a_line_where_gfm_does.py` (M5).
`test_the_template_says_why_a_tick_is_refused` is held by
`tests/test_the_set_a_work_item_always_has.py:248` against the skill.
`test_the_template_shows_the_word` is held by `test_the_skill_shows_the_word`,
which now runs the example through the reader (T4).
`test_the_fence_rule_agrees_with_the_config_reader` is held for its copy
half. Its agreement half is held by nothing, which is finding 2.
`test_the_template_ships_the_vocabulary_the_parser_accepts` is held by
`tests/test_waiver_decided_at_start.py:1026` against the orchestration. The
template's placeholders are read by `offered` in the two PARSES cases.
The deleted constants follow their readers. The five heading copies are
imported from one place. `NUMBER`, `OTHER_FILE` and `CITED_NUMBER` went with
the forms `## Removes` names. The `*_LINK` and `POINTER_LINK` constants
collapse into one spelling. `FENCE_SHAPES` is finding 2, and `PLAN_TEMPLATE`
and `BLOCKS` lost their only readers.
Two surviving functions lost assertions.
`test_every_copy_of_the_splitter_is_the_readers` lost three, which compared
the copy that is gone.
`test_the_template_is_the_record_the_check_reads` lost one, which read the
template comment. It now asserts the skill's `reopens:` sentence.

confirms: none
No living file writes the section sign, and S9 holds. Executed: `git grep -P`
for U+00A7 outside the four record paths matches only two binary PNG files
under `assets/seals/candidates/`. `git diff --name-only 0d62145a..a9d9423c`
over `seal/specs`, `changelog`, `CHANGELOG.md` and `evals/behaviour` lists
only this work item's directory.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at a9d9423c. This round ran only the modules named in `## Probes`. The smith labels the suite `unverified`, and that label is honest: no phase record claims a full run, and finding 1 is a module no boundary run took | the whole tree | the orchestrator, through `broad-gate` after the rounds settle |
| The legs of CI run 39711220166 other than the two failing cases of finding 1 | the run's logs | the coordinator, who read the run |
| The paid non-inferiority run for the five rewritten preloads. The preload byte figures in `phases/phase-5.md` were not re-measured in this round | `evals/scripts/noninferiority.py` | the repository owner, at the pull request (`questions.md` Q3) |
| Whether every one of the 46 guidance rows in `phases/phase-4.md` stands at the home it names. This round sampled four by mutation and read about ten | `seal/specs/1792627930-the-section-sign-is-still-syntax/phases/phase-4.md:33-81` | the next round |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_unverified_rows_close.py tests/test_the_hooks_hide_what_a_renderer_hides.py tests/test_the_mode_question_is_asked_once.py tests/test_chain_check.py -q` | 650 passed: the baseline for the mutations |
| `bin/test tests/test_a_shrunken_corpus_declines_to_judge.py -q` | 2 failed, 15 passed: the CI failure reproduced, then 17 passed with finding 1's fix applied and reverted |
| `.venv/bin/python test_tmp_round1_probes.py` | Replay: the five rule changes all placed. Citation reader: near misses unread (finding 3), wrapped forms read. Heading reader: `## 1.`, `##  1` and `## 1` with no title were refused at their line, while `##1` and `### 1` were neither refused nor read, as at the base. A `## 99` inside a fence was read as a rule, as at the base. Implement reader: a wrapped dangling title was refused, and a possessive or `step` form was not read, as at the base. Fence: 19 shapes and 0 disagreements among the three walks |
| M1: `bin/mutation-check hooks/blocks.py` with the closer length check made true, over six fence modules | red, exit 0 |
| M2: the same, with the closer character check made true | red, exit 0 |
| M3: the same, with `fence_only` returning no unclosed opener, over the six and then over all nine modules that reach it | SURVIVED, exit 1, both times; red, exit 0, at 0d62145a with the deleted case alone (finding 2) |
| M4: `bin/mutation-check skills/verify/scripts/unverified_check.py`, with `fence_spans` closing an unclosed block at the last line | red, exit 0 |
| M5: `bin/mutation-check hooks/blocks.py` with the carriage return dropped from `GFM_LINE_RE`, over `tests/test_every_reader_ends_a_line_where_gfm_does.py` | red, exit 0 |
| T1 to T4: `bin/mutation-check` on the moved sentences named in `## Confirmations`, each over its module | red, exit 0, all four |
