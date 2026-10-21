# Feature Specification: what an agent opens on demand states the current rule, and the CLAUDE.md block has one copy (#940)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against* | A fact has one source and every other place links to it; a change rewrites the text it amends in place and in the same commit removes what stood on the old fact; history goes to git, the changelog and the work record |
| `CLAUDE.md` *The goal a design is chosen against* | Nothing in this run stops to ask; the paid proof is `questions.md` Q1 with a default the owner can overturn at the pull request |
| #940's body, *Decided by the owner* (2026-10-14, 2026-10-15) | The five decisions this frame builds to: what `CLAUDE.md` holds, the block read once from one copy, the design-direction line judged by that rule, one source for the branch-number rule, the approval line alone on its line |
| Owner direction relayed 2026-10-21 (two messages) | Every rewritten instruction has one reading, and the two writing directions are stated in the repository's rules (Scope 1) |
| `skills/implement/SKILL.md` *Document layout* (the `docs/` row) | A pull request does not edit `docs/`. Every `docs/` sentence this item makes false is a `## Rule changes` item below, applied by `settle --apply` after the release |
| `skills/settle/SKILL.md` *Rule changes* and *A rule has one shape* | The grammar of `## Rule changes`, and the `check:` line every rule this item writes ends with |
| `seal/specs/1792459424-docs-states-the-current-rule-in-one-read/questions.md` Q1, Q2 (owner, 2026-10-20) | Q1: no paid run where no behaviour case exercises the changed files. Q2: syntax a check reads outside `docs/` is this item's and a later item's; Scope 8 decides which |
| `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md` *The proof harness, as this item leaves it*; `evals/README.md` *The behaviour suite* | The non-inferiority proof the issue names: both sides run, five pass rules, rule 4 the preload's bytes |
| `docs/the-reader-registry.md` *A frame names what its work removes* | `## Removes` below is the list the review reads against the diff |
| `CONTRIBUTING.md` *What a change to a gate must carry* | Removing the `claude_block.py --check` step from `hygiene.yml` is a gate change: its failure direction is stated in `## Removes` |
| `skills/writing-style/SKILL.md` *여럿이 가질 수 있는 것은 누구 것인지 밝힌다*; `tests/test_one_word_one_meaning.py` | One word, one meaning, and a thing more than one party can have is named with whose |
| `seal/specs/1791076836-every-rule-claude-md-restates-has-one-home/spec.md`; `tests/test_the_rules_claude_md_names_have_one_home.py` | A `CLAUDE.md` row names its rule's home; the module's `LINKED` and `CARRIERS` change where a row leaves |
| `tests/test_no_passage_is_pasted_into_a_second_file.py#BASELINE`; the owner's comment on #940 (2026-10-18) | #755's restatements that the baseline still holds in this item's files are this item's to drain |
| #945's body, sections 1 and 2 | It says #940 writes #945's orchestrator rules into the two orchestration files; #945 is not framed. `questions.md` Q2 |

## Scope

**In.**

1. **The writing requirement, binding on the build and the review from
   phase 1.** Two rules, owner 2026-10-21:
   - (a) Nothing an agent writes or a check reads uses a symbol a reader can
     trip on as syntax; no value is stated twice; no spelling a near miss
     could pass.
   - (b) Shorter never at the cost of a second reading. A sentence that
     tells a party to act names the party (the orchestrator, the smith, the
     warden, the sealer, the framer; never "you" or "the session" in a file
     two parties read), when it acts, on which file, and what counts as
     done. One word, one meaning: a term the repository defines is used as
     defined and never swapped for a synonym. A sentence compressed until
     its actor or its condition drops out is a defect, not a saving.

   The instances (b) guards against, each from this repository: the word
   `seal` read three ways (`tests/test_one_word_one_meaning.py`); "So is …"
   attaching to the wrong clause (#953's sealer, 2026-10-20); "The one
   writer that does is `settle`" read as a rule about who writes `docs/`
   (`seal/specs/1792449518-settle-squashes-specs-into-docs-in-place/spec.md`,
   grounding row on the implement skill's layout); "the session" in a file
   the orchestrator and an implementer both read; a sentence appended to the
   `Approved` line that made the old check read no approval.

   **Where the rules live.** Their full statement goes into
   `skills/writing-style/SKILL.md`, as one new `###` section under the
   existing `## 구성 규칙` heading, written in that section's language: three
   rules, each one bold sentence with its grounds and its own `check:` line
   (Data and interfaces). `## English prose rules` and `## 문장 규칙`, the
   two sections `agents/framer.md`, `agents/smith.md` and `agents/warden.md`
   open, each gain one line linking that section. The skill's `description`
   names text an agent or a check reads (a skill, an agent definition, a
   template, a frame) among its uses. `CLAUDE.md` gets one compact rule
   naming both directions and linking the section, because a session here
   writes skills, agents, templates and frames as its first act and opens no
   writing skill before it. The shipped block gets no line (Scope 2).
2. **The block is read once, from one copy, and holds the rules only.**
   `templates/claude-md-block.md` holds the rules and no reasoning, 1,669
   bytes by `wc -c` at 4c4c8e11 (4,695 at b3154f43; both executed). The
   owner's 1–1.5 KB was the target; the 169 bytes over it are three rules,
   each named with why it is a rule in `overview.md` (`questions.md` Q4). It
   keeps the four headings and their
   rules: tooling, the three safety rules, batching, lint before commit,
   worktrees, and routing. The routing bullet states, in this order: where
   no `seal/` root exists, follow the Bootstrap section of
   `skills/implement/orchestration.md` first; ask question 1 alone
   (`automation`, `per axis`, `no work item`) and the four boxes in a second
   call only under `per axis`; write `seal/specs/<work-item-id>/routing.md`
   from `templates/sdd-routing.md` in a command of its own, then commit it;
   under `no work item` every commit carries `[no-review]` in front of the
   command (`[no-parity]` too where a migration config is declared). Every
   other sentence of today's bullet is reasoning: it is in
   `skills/implement/orchestration.md` *Orchestrator: how the work is
   routed* after phase 2, or it leaves with its grounds in the phase record.
   No design-direction line and no writing-direction line: both apply when a
   design is chosen or text is written, after a session's first action, and
   the file owning each act supplies it then (`questions.md`, head).
3. **This repository's `CLAUDE.md` holds what a session here must know
   before its first action and the owning file cannot supply in time**,
   about 4,500 bytes or fewer (8,524 at b3154f43, executed). The generated
   copy and the comment under it leave. The goal and the tenet stay as
   #923 left them. The rows, judged by that rule:
   - merge method per direction: stays; the party merging opens no file
     that states it;
   - no real identifiers: stays; a smith writing a fixture opens no file
     that states it, and `plugin_directory_check.py` refuses only at the
     pull request;
   - whose: folds into the writing rule of Scope 1, whose home holds it;
   - commit early: leaves; `skills/implement/SKILL.md` *2. Implement
     test-first, and let each rule name its test* states it and is opened at
     the build (`agents/smith.md` step 1; read);
   - fragments: leaves; `skills/code-review/orchestration.md` names the work
     item's `changelog.md` at the step where the orchestrator writes it
     (line 195, read).
   The build checks each premise named here before acting on it.
4. **The block reaches a machine only through `install.sh` and the update
   skill.** `.github/scripts/claude_block.py`, its `hygiene.yml` step and the
   cases holding the copy to the template leave. A session reads the
   installed plugin's block, not the tree's: `skills/update/SKILL.md` step 4
   says, once, that running `./install.sh` from a clone installs that tree's
   block. Every sentence stating the generated copy is rewritten in the same
   commit: `install.sh`, `skills/update/SKILL.md`,
   `skills/preset-setup/SKILL.md`, `README.md` and `README.ko.md` (their
   block rows and install paragraphs), and the docstrings and messages in
   `hooks/mode-gate.py`, `skills/verify/scripts/unverified_check.py` and
   `skills/verify/scripts/broad_gate.py`. Cases that read the block through
   `CLAUDE.md` read `templates/claude-md-block.md` instead.
5. **The branch-number rule moves into the plugin's
   `skills/commit-pr-convention/SKILL.md` *Branch names*, in place.** A
   branch cut from an issue is `<prefix>/<issue number>-<slug>`; two issues
   are joined by a hyphen (`feat/110-117-<slug>`); a change with no issue
   has the slug alone; a release branch keeps `release/vX.Y.Z`. The example
   `perf/403-repositories-built-one-git-call-at-a-time` goes, because its
   number reads as an issue under the new rule. The shape restated at
   line 91 becomes a link to *Branch names*.
6. **`plan.md`'s approval line stands alone on its line.**
   `skills/implement/orchestration.md` states the shape at the step where
   the orchestrator spawns the build (Data and interfaces).
   `skills/code-review/orchestration.md` (the redesign row, line 154) and
   `templates/sdd-plan.md`'s comment name that statement rather than
   restating it.
7. **Each on-demand file states the current rule, once.** Rewritten:
   `skills/implement/orchestration.md`, `skills/code-review/orchestration.md`,
   `skills/verify/SKILL.md`, every skill under `skills/` except
   `agent-contract`, `implement/SKILL.md`, `code-review/SKILL.md`,
   `writing-style/SKILL.md` and `settle/SKILL.md` (rewritten by #968, the
   warden's rewrite and #953), `skills/writing-style/outside-the-review.md`,
   every file under `templates/`, `CONTRIBUTING.md`. A sentence stays only if
   the party reading the file at its act would act wrongly without it.
   Narrated history, dated decisions, measurements kept as anecdote and
   issue numbers a sentence can stand without leave (`#NNN` references at
   b3154f43: verify 22, implement orchestration 19, CONTRIBUTING 16, code-review
   orchestration 9, `templates/config.md` 7; executed). The current shapes
   #953, #941, #1000 and #1002 shipped are stated where their home is and
   linked elsewhere. Headings this item writes or rewrites hold no dash,
   arrow, middle dot, pipe or section sign; a cross-reference is the
   backticked path followed by the heading in italics.
   **`skills/verify/SKILL.md` is split along its own headings:** `## The
   broad gate` and `## Measure the segment, and feed the flow log` are the
   orchestrator's acts (contract §2 names the orchestrator for the broad
   gate) and move to a new `skills/verify/orchestration.md`, the sibling the
   implement and code-review skills already have. What the smith and the
   sealer open stays in `SKILL.md`. Every citation outside `docs/` names the
   new file in the same commit; the two in `docs/` are `## Rule changes`.
8. **Syntax a check reads outside `docs/`: what is this item's** (the
   decision #941's Q2 left here):
   - every section-sign citation of a heading, `§*heading*`, in the
     Markdown files under `skills/` and `templates/`, in `CLAUDE.md` and in
     `CONTRIBUTING.md`, becomes the backticked-path-and-italics form. 85
     lines in these files hold a section sign at b3154f43, outside
     `skills/agent-contract/` (executed, `git grep -c`). A citation of the
     contract's numbered sections (`contract §N`) stays, because the
     contract's own headings carry the number;
   - the arrow in `templates/sdd-spec.md`'s `## Open questions →
     questions.md`: no reader (executed, `git grep` outside `seal/specs`);
     the heading becomes `## Open questions`;
   - the coordinate hint in `templates/sdd-spec.md`'s `## Removes` table: no
     script reads that column (executed, `git grep Removes` over the
     scripts), so the hint becomes the citation form above.
   A later item's, which the owner opens: the contract's `## §N` numbering
   and the four tests that read it, every section sign in `agents/*.md` and
   in `.py` files (58 lines in the scripts outside the contract, executed),
   `coordinates.py`'s `path#unit` grammar and the pact anchors it reads, and
   the changelog's `<!-- specs/<id> -->` lines `gather_changelog.py` writes
   and reads. Each changes a preload or a reader's grammar.
9. **Item D7 from #3.** `skills/implement/SKILL.md` *6. Drain the rows
   before the broad run, and keep the records* names its moment and its
   party: the orchestrator moves each row out once the last round record has
   no finding open, and before it runs `broad-gate --preflight`, because
   every commit after the broad run, a `seal/follow-up.md` row among them,
   leaves `broad-gate.md` stale for the sealer.
10. **#755's restatements in this item's files.** Every
    `tests/test_no_passage_is_pasted_into_a_second_file.py#BASELINE` pair
    with a file this item rewrites is drained from that file where it is not
    the rule's home, and its entry is lowered to the measured count, or
    removed at zero. A pair whose other file is an agent definition, the
    contract or a `docs/` document keeps its residue, named in the phase
    record with whose it is.
11. **The proof.** Free readings, each in a phase record: S13's on-demand
    bytes per agent, S11's census, S10's review. The paid non-inferiority
    run is `questions.md` Q1, default not run.

**Out, and whose.**

| Left out | Whose, and why |
|---|---|
| `agents/*.md`, `skills/agent-contract/SKILL.md` | The preload: a change there owes the paid proof with rule 4 in force. With the syntax of Scope 8's later list, the owner opens that item; none exists at b3154f43 (executed, `gh issue list`) |
| The prose of `implement/SKILL.md`, `code-review/SKILL.md`, `writing-style/SKILL.md`, `settle/SKILL.md` | Rewritten by #968, the warden's rewrite and #953. This item edits them only for Scope 1, 8, 9 and 10 |
| `docs/` | Not edited in this diff: `## Rule changes` |
| #945's rules (fresh spawn per phase, `mergeable` before CI, rebase then a verifying round, a decision folded into one source, a prevention home) | `questions.md` Q2, default #945's own frame |
| The layout of `tests/` | #942. This item edits a test only to follow a sentence it rewrites, retire a pin, or read the template instead of the copy |
| Deleting `~/.claude/skills/commit-pr-convention/SKILL.md` and pointing `~/.claude/CLAUDE.md` at `specseal:commit-pr-convention` | The owner, on the owner's machine, after merge; no file in the tree |
| Deleting the two notes in the orchestrator's machine-local memory that held Scope 1's directions (one is `no-symbols-or-constants-a-reader-can-trip-on.md`, executed `ls`) | The orchestrator, after merge |
| The paid non-inferiority run, and a change to `noninferiority.py#verdict` rule 4 | `questions.md` Q1 |
| `README.md`, `README.ko.md` beyond the rows and paragraphs naming the copy | Not on-demand for an agent |

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the block is the rules | Given the rewritten template, it states each rule of Scope 2 and no reasoning, and every byte past 1,500 by `wc -c` is a rule `overview.md` names | `wc -c`; the pin cases of S4; the `overview.md` row |
| S2 one copy | `git grep -n 'specseal:start' -- CLAUDE.md` prints nothing; `git grep -n claude_block -- ':!seal' ':!changelog'` prints nothing; `hygiene.yml` holds no step running it | the greps |
| S3 install still writes the block | Given an empty `CLAUDE.md`, `install.sh` writes the template's marker region once and a second run changes nothing; `uninstall.sh` removes it | the installer cases kept from `tests/test_the_claude_md_block_has_one_source.py`, in a module named for the installer |
| S4 the routing rule still ships | Cases that read the block's routing bullet (`tests/test_first_setup_asks_once.py`, `tests/test_waiver_decided_at_start.py`, `tests/test_review_axes.py`, `tests/test_broad_gate_rule.py`) read the template and pass on Scope 2's content | those modules |
| S5 `CLAUDE.md` | `wc -c CLAUDE.md` about 4,500 or fewer; its rows are Scope 3's; `tests/test_the_rules_claude_md_names_have_one_home.py` passes with `LINKED` holding the rows that stay | `wc -c`; the module |
| S6 the branch rule | *Branch names* states Scope 5's shapes once, line 91 links it, and no example's number is anything but an issue's | read by the warden; a case pinning the shape, seen red with the sentence deleted |
| S7 the approval line | `skills/implement/orchestration.md` states the shape once, at the spawn step; `code-review/orchestration.md` and `templates/sdd-plan.md` link it; `tests/test_the_set_a_work_item_always_has.py` passes | the module; `git grep -n 'Approved <date>'` |
| S8 no section sign but the contract's numbers | `git grep -n '§' -- 'skills/*.md' 'templates/*.md' CLAUDE.md CONTRIBUTING.md ':!skills/agent-contract'` prints only `contract §N` or `agent-contract` §N citations | the grep, listed in phase 9's record |
| S9 the verify split | `skills/verify/SKILL.md` holds neither moved section; `skills/verify/orchestration.md` holds both; `git grep -n 'verify/SKILL.md' -- ':!seal' ':!changelog' ':!docs'` names no moved heading | the greps |
| S10 one reading | Every imperative sentence a phase writes or rewrites names its actor, its moment, its file and its done state, and uses each defined term as defined; a sentence with a second reading is a finding | `tests/test_one_word_one_meaning.py` and the pins where they reach; beyond them the warden reads each such sentence and records one with a second reading as a finding |
| S11 nothing an agent relies on is lost | Each instruction the old text gave a party has a home after the rewrite, or goes with its grounds; each case that pinned a removed sentence is retired or rewritten, and a new case is seen red | the census table in each phase record; the group's pin modules |
| S12 the restatements drain | `tests/test_no_passage_is_pasted_into_a_second_file.py` passes, and every `BASELINE` entry of a pair Scope 10 drains equals its measured count | the module; phase 9's measured table |
| S13 what each agent opens is not larger | The bytes of the files each definition directs its agent to open (Data and interfaces), by `wc -c`, are no larger at phase 9's commit than at b3154f43 | the two readings in phase 9's record |
| S14 a renamed heading leaves no stale citation | For each heading renamed or moved, `git grep` of its old text outside `seal/`, `changelog/` and `docs/` finds nothing; each `docs/` citation is an item of `## Rule changes` | the grep per heading, listed in the phase record |
| S15 D7 | *6.* names the party and the moment of Scope 9 | read by the warden |
| S16 the writing rules live in the tree | `skills/writing-style/SKILL.md` holds the three rules with their `check:` lines; both language sections link them; `CLAUDE.md` names both directions; the template holds no line for them; `bin/rules --check` exits 0 | `bin/rules --check`; the greps |

## Data & interfaces

**The approval line**, stated once in `skills/implement/orchestration.md`:
one line, `Approved <date> by <who>, when `smith` was spawned.`, where the
clause after `when` may name what was spawned for (`for phases 1 to 3`)
and the line ends at its full stop. A reason, a scope note or a second
approval goes on its own line below. Nothing reads the line in a work item
at b3154f43: `chain_check.py#APPROVED_RE` left with #923 (executed, `git
show 8350c578`); the reader is the warden, and the rule's check line says
`check: none reader: the warden at review`.

**`skills/verify/orchestration.md`**: the two moved sections under their
names without the dash, `## The broad gate` and `## Measure the segment,
and feed the flow log`, and an opening paragraph saying the orchestrator
reads it and the smith and the sealer do not.

**The three writing rules** in `skills/writing-style/SKILL.md`:

- symbols, values and near misses (Scope 1 (a)); `check:` naming the
  readers that refuse a near miss: `tests/test_the_rules_command_reads_each_rule_off_its_test.py`
  and `tests/test_settle_applies_rule_changes_in_place.py`;
- one word, one meaning, and whose; `check: tests/test_one_word_one_meaning.py`;
- one reading per instruction: actor, moment, file, done state; `check:
  none reader: the warden at review`.

Each rule cites its instances from Scope 1 in one line each.

**On-demand sets for S13**, read from the definitions (read at b3154f43);
bytes executed at df686fc9, whose files equal b3154f43's:

| Agent | Files its definition directs it to open | Bytes |
|---|---|---|
| framer | `skills/implement/SKILL.md`, `templates/sdd-spec.md`, `sdd-plan.md`, `sdd-questions.md`, `skills/writing-style/SKILL.md`, `confidence-check`, `feature-planner`, `templates/config.md`, `skills/settle/SKILL.md` | 110,562 |
| smith | `skills/implement/SKILL.md`, `skills/verify/SKILL.md`, `writing-style`, `templates/sdd-phase.md`, `templates/config.md`, `legacy-parity` | 146,526 |
| warden | `skills/code-review/SKILL.md`, `writing-style`, `templates/sdd-round.md`, `legacy-parity`, `templates/config.md` | 76,287 |
| sealer | `skills/verify/SKILL.md`, `templates/sdd-guarantee.md` | 55,861 |
| orchestrator | both orchestration files, `implement/SKILL.md`, `code-review/SKILL.md` | 105,113 |

The orchestrator's row adds `skills/verify/orchestration.md` at phase 9.

## Rule changes

- change
  file: docs/the-review-record.md
  section: The per-segment bars
  from: its rows are `skills/verify/SKILL.md` *Measure the segment, and feed the flow
    log*'s;
  to: its rows are `skills/verify/orchestration.md` *Measure the segment, and
    feed the flow log*'s;
- change
  file: docs/issues-and-milestones.md
  section: A label answers *what it is about*, and survives the move
  from: `skills/verify/SKILL.md` finds the log to post a segment's measurement to by
  to: `skills/verify/orchestration.md` finds the log to post a segment's
    measurement to by
- change
  file: docs/worktree-guard-spec.md
  section: Creation consent
  from: (`skills/implement/orchestration.md` *Question 1 — single-select*),
  to: (`skills/implement/orchestration.md` *Question 1*),

A heading phase 2 or a later phase renames that another `docs/` line cites
adds its item here in the same commit, and S14 lists it. Until the owner's
settle after 0.22.3 applies them, these three `docs/` lines name the old
place; `plan.md` *Technical context* states that window.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The generated block in this repository | `CLAUDE.md`, from `<!-- specseal:start -->` through the comment under `<!-- specseal:end -->` | the installed block a session here already loads from `~/.claude/CLAUDE.md`; `templates/claude-md-block.md` is the one source |
| The copy's generator and its check | `.github/scripts/claude_block.py`; `.github/workflows/hygiene.yml` step *the CLAUDE.md block is the template's, line for line* | nothing is left to drift. Failure direction: the pull request gate blocks less, and what it no longer reads (a copy equal to its template) no longer exists |
| The copy's cases | `tests/test_the_claude_md_block_has_one_source.py`, the cases holding the copy to the template; `tests/test_no_passage_is_pasted_into_a_second_file.py#GENERATED` and the case reading it | the installer cases move to a module named for the installer (S3) |
| Reasoning in the block | `templates/claude-md-block.md`, every sentence of the routing bullet Scope 2 does not keep | `skills/implement/orchestration.md` *Orchestrator: how the work is routed*, or gone with its grounds in phase 3's record |
| Two `CLAUDE.md` rows | `CLAUDE.md` *Repo rule — commit early; on a declared branch it costs nothing*, *Repo rule — a change writes fragments, never the shared file* | `skills/implement/SKILL.md` *2.*; `skills/code-review/orchestration.md` at the changelog step |
| The whose row as a row | `CLAUDE.md` *Repo rule — a thing more than one party can have is named with whose* | the writing rule of Scope 1, and `skills/writing-style/SKILL.md` |
| The orchestrator's sections in verify | `skills/verify/SKILL.md` *The broad gate — after the rounds, then compare against the base*, *Measure the segment, and feed the flow log* | `skills/verify/orchestration.md` |
| The branch shape restated | `skills/commit-pr-convention/SKILL.md`, the line opening "**Branch names stay ASCII**" | *Branch names* in the same file |
| The arrow heading | `templates/sdd-spec.md` *Open questions → questions.md* | `## Open questions` |
| Section-sign citations of a heading | the lines of Scope 8's first item, among its 85; `contract §N` citations stay | the citation form of Scope 7 |
| Narrated history | every file Scope 7 rewrites, each paragraph a census row of its phase | git, the changelog and the issues |
| Cases pinning a removed sentence | `tests/`, each named in its phase record | retired with the sentence, or rewritten to the new one where the rule stays |
| `BASELINE` entries | `tests/test_no_passage_is_pasted_into_a_second_file.py#BASELINE`, each pair Scope 10 drains | lowered to the measured count, removed at zero |

## Open questions → questions.md

Anything a planner must answer lives in questions.md, not inline — unanswered
questions buried in prose read as decided.

<!-- The line below is the framer's mark, and it is the only evidence in the
     TREE that the framing happened — the existing framer mark lives in the
     repository's git dir, and a git dir does not travel, so CI cannot see it.
     Fill in the date and `<who>`; `<who>` takes the two values the `Planning`
     row of `routing.md` takes, `framer` or `the session`, and a mark that
     disagrees with that row is refused at the pull request rather than
     guessed at.
     The shape — verb, date, who, the moment — is the one `routing.md` and
     `plan.md` already end with, which is what keeps three feet-lines from
     becoming three conventions.
     A reframe adds `Reframed <date> by <who>, after round <N>.` UNDER this
     line when the review chain sends the work item back to its framer. It is
     never in this template; only a reframe writes it. -->

Framed 2026-10-21 by framer, before the build.
