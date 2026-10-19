# 1792367880-ci-runs-once-when-the-pull-request-opens — phase 2

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 62c38876 |


## What this phase was asked

Build S4 to S10 of `spec.md`. Rename the owner section of
`skills/code-review/orchestration.md` to *Orchestrator: the pull request
opens once the sealer has sealed, and a phase is re-run* and rewrite it in
place. Then rewrite each carrier in the same commit:
- `skills/implement/orchestration.md` step 2 and the acts-table row, but
  never `:381` or `:416`, which are #968's;
- the citation in `skills/verify/SKILL.md`;
- `agents/sealer.md`, where it reads the pull request body and where it says
  "once per ready pull request" (#985 leaves the file alone);
- `docs/the-broad-gate.md:5`;
- `CONTRIBUTING.md` §*Opening a pull request*;
- `broad_gate.py`'s `CELL_UNCOMMITTED`, with Q2's default wording unless the
  code says otherwise;
- the test modules that pin any of these.

Also write the changelog fragment. `chain_check.py` and
`docs/the-review-record.md` stay untouched. Write the pins first and see them
red. Answer Q2 and Q3 here. Name exactly which sentences of `agents/sealer.md`
changed, because the orchestrator measures the sealer after this phase.

## What this phase found

**The heading is one word shorter than the frame's.** The frame's heading is
89 columns as a Markdown line, and
`tests/test_docs_line_wrap.py::test_prose_stays_within_the_wrap_limit[skills/code-review/orchestration.md]`
refuses anything over 88 (executed). A heading cannot wrap, so the section is
titled *Orchestrator: the pull request opens once the sealer seals, and a
phase is re-run*, and every citation uses that title. The rule's own sentence
keeps the frame's wording, `The pull request opens ready, once the sealer has
sealed, and CI runs then.`, so S4's sentence is unchanged. The repository's
wrap rule outranks the frame's wording, and `overview.md` records the
divergence.

**What the owner section now says**, in place of the old rule and the #296
paragraph:
- The pull request opens ready once `guarantee.md` reading `sealed` is
  committed, with `gh pr create --body-file <that file>`, so the body that
  opens is the one the sealer read.
- Where the work's risk is platform-specific, the orchestrator runs
  `gh workflow run tests --ref <branch>` once the build's last phase closes,
  and reads the result before its broad run.
- The stated limit is a defect that only one platform shows. It is found when
  the pull request opens, and it takes the repair path the section already
  has.
- A draft is tolerated. The #296 paragraph's one surviving fact ("Nothing that
  can reach `main` is exempt") is now part of that sentence.

**Four more sentences in the section were rewritten in place:**
- "`broad-gate.md` is read at a READY pull request … before the draft goes
  ready" now names both records and says the steps come before the pull
  request opens.
- The sealer is spawned with "the file holding the pull request body"
  instead of "the pull request". `spec.md` §*Removes* does not name this
  sentence.
- "keeps the pull request a draft" became "opens no pull request".
- "leave the pull request as a draft until they have" became "open no pull
  request until they have".

**`agents/sealer.md` changed in three places, and nowhere else** (read:
`git diff 2d2ffbdb 62c38876 -- agents/sealer.md`). The orchestrator measures
these:
1. Description, `:4-7`. Before: "Spawn once per ready pull request, after the
   review rounds settle, the pull request body and the changelog fragment are
   written, and the orchestrator has run the broad gate: it reads the". After:
   "Spawn once per work item, before the pull request opens: after the review
   rounds settle, the pull request body is written to a file, the changelog
   fragment is written, and the orchestrator has run the broad gate. It reads
   the".
2. Intro, `:38-41`. Before: "The prompt gives you the work item's directory,
   the base, the issue and the pull request; where the session has no tracker
   or remote, it names a file holding the issue body or the pull request
   body, and you read that file." After: "The prompt gives you the work
   item's directory, the base, the issue and a file holding the pull request
   body, which you read: the pull request opens with that body after your
   verdict. Where the session has no tracker, it names a file holding the
   issue body too, and you read that file."
3. Step 2, `:69`. Before: "and the pull request body (`gh pr view <N>`)."
   After: "and the pull request body, from the file the prompt names."

The five sealer evals in `evals/behaviour/sealer/` already pass the body as a
file, `.git/specseal-eval/pr-body.md` (read). Their prompts were not changed.

**Q2.** `CELL_UNCOMMITTED` now ends `CI reads HEAD, so commit it before you
push`. That is the default, and nothing in the code argued otherwise. It is
true when no pull request is open yet, when one is open (the repair path), and
in a repository that opens drafts. The owner section's sentence quoting the
line moved with it, and both pins in
`tests/test_the_seal_is_taken_once_by_the_sealer.py` read the new text.

**Q3.** Renaming the row is enough. The acts-table row was renamed and its
grounds gained one clause: nothing records that a platform-specific change
ran `gh workflow run tests`. `test_every_orchestrator_act_names_its_delivery.py`
passed after the rename. With the row's old heading put back by
`mutation-check`, its one case failed (executed).

**Pins, and how each was seen red.**
- Before any document changed, the rewritten pins failed against the tree as
  it stood (executed): four in `test_the_rules_have_one_owner.py`, one in
  `test_a_parallel_agent_names_its_scratch_after_the_work_item.py`, two in
  `test_broad_gate_rule.py`, one in
  `test_the_stamp_reaches_the_person_it_is_drawn_for.py`, one in
  `test_the_broad_gate_row_is_asked_for_and_runs_as_written.py`, two in
  `test_the_seal_is_taken_once_by_the_sealer.py`, and the new S8 case in
  `test_the_sealer_guarantees.py`.
- After the commits, sixteen `mutation-check` runs were caught (executed).
  Each put back an old sentence, or deleted or changed a new one:
  - the owner sentence;
  - the draft-tolerance sentence;
  - the dispatch command;
  - the stated limit;
  - a draft in the order step;
  - CONTRIBUTING's link;
  - the acts row's old heading;
  - the sealer's description;
  - the sealer's step 2;
  - the sealer's intro;
  - `CELL_UNCOMMITTED`;
  - the owner section's quotation of that line;
  - the `Broad gate` refusal sentence;
  - the owner heading;
  - the `verify` citation, run twice (see the next item).
- Two pins exist that the frame did not list. Both were added after a
  mutation showed nothing caught the change:
  - `test_the_owner_states_the_dispatch_step_and_the_limit` (34c1d2ce). S4
    says the section states both, and no case read either.
  - An assertion in `test_broad_gate_rule.py::test_the_broad_gate_section_states_its_own_timing`
    (62c38876). The `verify` citation had survived a revert to the old
    heading (executed), and the same mutation was caught after this
    assertion was added.

**One changed line has no case.** `docs/the-broad-gate.md:5` now reads
"before the pull request opens". Its mutation back to "before a pull request
is marked ready" survives `test_broad_gate_rule.py` (executed), and no module
reads that sentence. The plan named no pin for it.

**The phase's sweep.**
`git grep -n -e "opens before round 1" -e "as a draft" -e "marked ready" -- skills agents docs CONTRIBUTING.md .github/workflows`
returns one line, `skills/code-review/orchestration.md:183` (executed). It is
the draft-tolerance sentence, which describes what `hygiene` does when a
draft is marked ready, so it stays. `git grep -n "opens before round 1"`
outside `seal/specs/`, `.test_durations` and `changelog/` returns nothing
(executed). Several sentences that describe `chain_check`'s draft behaviour
stay true and stay as they are: `README.md:201-206` and `:605`,
`README.ko.md:599`, `docs/the-review-and-parity-arms.md:100`,
`skills/implement/orchestration.md:637`, and `templates/hygiene.yml`.

**`CONTRIBUTING.md` gained one paragraph.** It tells a contributor to open
the pull request ready once nothing is left to push, because every push runs
the suite on Linux, macOS and Windows (read: `test.yml`'s matrix). It links
the owner section, and rule 6's links now include it.

**The changelog fragment** is in this directory's `changelog.md`, under
`### Changed`, with one entry per phase. It holds no measurement of the
sealer. That row is the orchestrator's to add once it measures.
