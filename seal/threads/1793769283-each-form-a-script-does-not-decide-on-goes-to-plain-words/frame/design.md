# Design: each form a script does not decide on goes to plain words (#1319)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| G1 `skills/core/SKILL.md` *The rule a mechanism is kept against* | A mechanism stays only while its record of what it caught outweighs what it costs. A script holds a gate only on a fact it reads exactly, and whether a line meant a label is the reading agent's judgment. This is the test each census row's decision applies (D2 and D3 below). It also binds the build: a change rewrites the text it amends in place and, in the same commit, removes what stood on the old fact, such as a check, a comment or a copy |
| G2 `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* | A script that answers "these differ" where the meaning is the same gives the worst result the workflow can give. The 0.30.1 case in the issue's second comment is one such answer: the walk refused a `seal` fence that a CommonMark parser reads whole. The census lists that refusal as a cost of the walk, not as a catch |
| G3 `skills/core/SKILL.md` *A document is cut by who opens it and at which step, so a party opens only what its step needs* | A form two parties exchange has one home, and both cite it. Text no agent acts on stands in a document only a person opens. This is the rule for D5 below and for each reason marked *moved* in *The reason census* |
| G4 `skills/core/SKILL.md` *A rule is guidance for a judgment, not a sequence to execute* | A reason an agent weighs at a step is part of the rule, so it stays (the issue's own scope). A reason only a person changing the rule needs moves to the `docs/` document that person opens |
| G5 `skills/core/SKILL.md` *Judgment is not licence to skip a party* | Five invariants, each held by a named mechanism. A form a script reads to hold one of them is listed with its catches and left for the owner (D1, `frame/questions.md` Q1). The table names no arm that reads the frame's mark, the `Seal-Routing` trailer or `routing.md`'s `Answered` line, so none of those is an invariant form (read: the table, rows 1 to 5). The routing row is held by `hooks/routing-edit-gate.py` and `hooks/question-gate.py`, so the `routing.md` rows those two hooks read are invariant forms |
| G6 `docs/running/what-a-script-gates.md` *Which gate a script holds*, and the row *the cases under `tests/text/` and `tests/behaviour/` that read prose* of *The checks* | A closed form is an exit code, a real parser's result, a structure a command wrote, or a line of a form the plugin defines, in the form's one spelling. A case pins a fact a reader acts on, and a case that pins wording goes. A check that is changed names, in its pull request, the form it reads, what it names as unread, and the agent and step that judge the same text. So a branch removed here takes its cell in that table with it, rewritten in place |
| G7 `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | The subject of this work item is the text of the forms: the templates, the agent definitions, the skills, the policy root's form and check documents (`docs/forms/`, `docs/checks/`, `docs/running/what-a-script-gates.md`), and the reasons the preload carries, together with the script branches that read those forms. It edits `docs/` directly in its pull request, as #1317 and #506 did in this release (read: their designs' `## Rule changes`, under `seal/threads/1793750411-rule-text-carries-no-history/` and `seal/threads/1793756609-an-enumeration-the-tree-does-not-hold/`). A `remove` with a `from` would leave a `check:` line in `docs/` that names a removed case refused at HEAD until the settle. That is the argument 1793756609's design gives |
| G8 `templates/setup/config.md` *What no row governs* | This list names each heading and word that stays English because a checker or a pinned case reads it literally at `c186a59ac`; phase 4 narrows the list's ground to what a checker reads literally (`trail/phases/phase-4.md`). A form that loses its last script reader here loses its place in that list, in the same commit |
| G9 The policy in force: the unsettled designs' `## Rule changes` | Two unsettled designs change policy text. `1793726048-the-stop-judgment-holds-against-later-rows` changes three sentences of `docs/running/the-run.md` *The run*, and `1793732301-the-readme-is-written-for-a-first-reader` changes one sentence of `docs/layout/the-record-layout.md` *The root records*. Neither sentence states a record form (read: each operation's `from` and `to`). Where a phase edits either section, it leaves those operations' `from` text standing, so the settle still finds it |
| G10 Precedent: 5a365e8d9 (#1277, 0.30.1) | That commit removed `check: none reader:` and `routing.md`'s `Answer pressed` row. A declaration that still carried the row "reads as before", and the committed declarations holding it leave at the settle (read: `git show --stat --format=%b 5a365e8d9`). C1 below follows it |
| G11 The three candidates of the issue's third comment, at HEAD `d4a43c611` | `confirms:`: `skills/code-review/scripts/chain_check.py:729` keeps only a value whose match has a `round` group, so it drops `none`. The first-record refusal at `:869-872` names `none` only in its message (executed: `grep -n`). Neither `hooks/lib/fields.py#CONFIRMATION_BLOCK`'s shape check of `none` nor any other line uses the value. The mark: `chain_check.py#MARK_RE` (`:211`) and `#REFRAME_RE` (`:212`) match the date and the round number. `#frame` (`:1027-1056`) checks only that neither the date nor who is a placeholder, and compares who with `routing.md`'s `Planning` row (read). `why:`: `skills/verify/scripts/unverified_check.py:702-713` returns the value at `d4a43c611` (read), and no caller outside the tests used it; phase 3 makes `why:` optional and removes the value from the reader's result (`trail/phases/phase-3.md`). The `Answered` line: `git grep -n Answered -- '*.py'` finds no script, only `tests/e2e/teammate/test_teammate_flow.py:62`, a fixture (executed). The comment's coordinates were read at `147285fda`, and these are `d4a43c611`'s. Phase 2 removes the mark's date and round-number checks and the first-record message's mention of `none` (`trail/phases/phase-2.md`) |
| G12 `confirms: none` is not an invariant form | The invariant *No fix that no round reads* is held by "every `fixed` or `rejected` finding is named by the next record" (the core's table, row 3). Only a `round-<N>#<n>` value names a finding, and the reader drops `none` (G11). A value the invariant's reader drops holds nothing for the invariant, so phase 2 judges `confirms: none` by D2 to D4 and not by D1. The `confirms:` key with a `round-<N>#<n>` value is an invariant form |
| G13 `evals/README.md` *The behaviour suite — `behaviour/<agent>/`* | `regrade` refuses a suite that differs from a side's own suite in a scaffold or a `shape-` grader. So a form change that reaches an eval scaffold or grader means the next comparison needs a fresh baseline side. No behaviour run is part of this work. The issue says #1254 narrows the suite in 0.32.0, so each decision carries its grounds instead of a measurement |
| G14 The walk and the parser | `hooks/lib/fields.py`'s docstring says it uses the standard library only and reads fences through `hooks/lib/blocks.py#walk`. `blocks.py`'s docstring calls every line uncertain from the first construct-looking line that "starts some other HTML block (`<` and a letter, `/`, `?` or `!`)" to the end of the file (read). CI installs `markdown-it-py` only for the suite's oracle (`.github/workflows/test.yml:149`, executed: `grep -n`). Plan row A5 weighs the issue's two directions and a third with their costs, and `frame/questions.md` Q2 leaves the choice to the owner |
| G15 Overlap with #1346 (`release: 0.31.2`) | #1346 corrects statements in `templates/setup/seal-README.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `seal/follow-up.md`, `ruff.toml`, `CONTRIBUTING.md`, `docs/releasing/branch-and-release.md`, a comment in `hooks/lib/config.py`, docstrings and comments under `tests/`, the eval fixtures' record titles (#1336) and the copy-in-force experiment (executed: `gh issue view 1346`). This work item can reach three of those: `seal/follow-up.md`'s `Who must answer` column, the eval scaffolds that carry record forms, and test docstrings that state a form. A phase that edits one of these files names it in its phase record, so #1346's build reads the new text. This work item corrects none of #1346's statements |

## Scope

In:

1. **The reason census, built.** Each row of *The reason census* below is built as it says. A sentence marked *cut* leaves its file. A sentence marked *moved* leaves the preload, its fact stands in the home the row names, and the preload cites that home. The cases that pin a moved or cut sentence follow it, and so does every other statement of it found by `git grep` on its words (contract rule 19).
2. **The measurement.** Phase 1 counts characters and lines at the base `c186a59ac`. Phase 4 counts the same files at its last commit, with the same commands (*The measurement* below), and writes both into its phase record as one table. The files are each party's preload and each record template.
3. **Census family A: the forms the pull request check, the stamp and the broad gate's record read.** These are the `seal` blocks of round records, `guarantee.md` and `trail/gate.md`, through `hooks/lib/fields.py` and `hooks/lib/blocks.py`. They are also the routing declaration's rows and its `Answered` line, the frame's mark and `Reframed` lines, the `Seal-Routing` trailer, and the round record headings `chain_check.py` reads. The eval scripts that read a round record (`evals/scripts/`) belong here too. Each form gets one census row, and the decision of each row that is not D1 is built.
4. **Census family B: the sections, tables and line forms the other scripts read.** Those scripts are `unverified_check.py`, `pr_body.py`, `settle.py`, `rule_changes.py`, `fold_check.py`, `.github/scripts/rules.py`, `.github/scripts/publish_release_note.py`, `hooks/lib/config.py`, `pact_check.py` and any other script M3 finds reading a record or a rule file. The forms include `gaps.md`, the plan's `## Phases` and *Judgments of the run*, `## Rule changes` and its no-change block `- nothing` with `why:`, `changelog.md` and its *Process changes*, `check:` lines, `closed`, `## From the records`, the `config.md` rows and the pact table. Each gets a row, and each decision is built. Phase 3 found no `drained` form in the tree and no script reading `# RIDER:` or `seal/follow-up.md`'s columns, so those three take no family B row (`trail/phases/phase-3.md`).
5. **Census family C: the forms agents alone read.** These are the hand-back labels and report shapes the agent definitions and skills ask for, `frame/questions.md`'s columns and `Who can answer` values, the phase record's heading, and the round record's prose sections and labels (`## Confirmations`, `## Not judged`, `## Probes`, `What holds:`, `What matched:`, `Why it matters:`). They also include the guarantee's prose tables and the design and plan headings that no script reads. Each gets a row, and each decision is built.
6. **The record files.** For each record file a work item holds, and the pull request body's copy, the census records each fact it states that another record states too, with D5's decision. Phase 4 builds this, after families A and B have changed what those files hold.
7. **Each form that goes leaves every statement of it.** That covers the template, the rule text in `agents/`, `skills/` and `docs/`, the script branch and its message, the cases that pin it, the eval scaffolds and graders that carry it, `templates/setup/config.md` *What no row governs* and the cells of `docs/running/what-a-script-gates.md` *The checks*. Each leaves in the commit that removes the form (G1, G6, G8).
8. **`gaps.md`**, from `templates/records/sdd-gaps.md`, written when phase 1 closes and added to by each later phase.

Out:

- Changing or removing any invariant form (D1). The census lists each one with its catches, and `frame/questions.md` Q1 holds the owner's decision on its default, which is that none changes here.
- A change to how the `seal` block is found (G14). Plan row A5 weighs the directions, and `frame/questions.md` Q2 holds the owner's choice on its default, which is that none is built here.
- Any behaviour run of `evals/` (G13).
- #1346's statements (G15), #1338 and #1343.
- The version, which reads 0.31.1 and stays (the orchestrator's finding).
- The settle of the released work items under `seal/threads/`, and any rewrite of their records beyond what C1 allows.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The census is whole for its family | Given a phase's family, when the proofer re-runs the phase's enumeration commands (M1 to M3) at the phase's commit, then every form the commands list has a row, and every script constant M3 lists either names a form that has a row or is named in the record as no form | The commands as the phase record states them, run by the proofer; a form with no row is a finding on the method (contract rule 12) |
| S2 Each row carries its columns | Given a census row, when it is read, then it names the form's one spelling and its writer at a coordinate. It names each reader with its kind (decides, uses, shape only, agent at a step, case or eval that pins it), the catches found with the search that found them, any other record holding the same fact, whether it is an invariant form, the decision with its rule (D1 to D6), and where the decision was built | Read each row against *The census row* below |
| S3 A form that goes is gone | Given a row decided D3 or D4, when `git grep -n -F '<the form's spelling>'` runs at the phase's commit, then nothing it lists outside `seal/threads/` writes, reads or pins the form, except a reader C1 keeps for committed records, which the row names | The command, per row, by the proofer |
| S4 An invariant form is untouched | Given a row decided D1, when `git diff c186a59ac..HEAD` is read over the reader branches the row names, then neither the form nor its reader changed | `git diff` over the named units |
| S5 Each reason is where its row puts it | Given each row of *The reason census*, when the core, the contract and the named home are read at HEAD, then a *kept* sentence stands, a *cut* one is gone, and a *moved* one stands only in its home, which the preload cites | Read the three files, and `git grep -n -F` on each moved or cut sentence's words |
| S6 The measurement is repeatable | Given phase 4's table, when *The measurement*'s commands run at `c186a59ac` and at the commit the table names, then they print the table's figures | The commands, by the proofer or the sealer |
| S7 Committed records still read | Given every record committed under `seal/threads/` and every eval scaffold at HEAD, when the suite's readers read them, then none is refused for a form this work changed | The narrow cases each phase names; the suite stays `unverified` until the orchestrator's broad run (contract rule 2) |

## Data & interfaces

### The census row

One row per form, in the phase record of the family that holds it, under `## What this phase found`. Each row has these columns:

- **Form.** The form's one spelling, as its template or rule text gives it.
- **Writer.** Who writes it, at which step, by `path` and heading.
- **Readers.** Each reader is one of these:
  - a script that **decides** on it (it refuses, names or gates), by `path#unit`;
  - a script that **uses** its value (it copies, groups or computes from it, or an eval grades on it);
  - a script that reads it for its **shape only** (the value is dropped or compared with nothing);
  - an **agent**, at a named step;
  - a **case** or an **eval** grader or scaffold that pins or carries it.
- **Catches.** The records in git where the reader refused or named a real record, as opposed to a test fixture, with the commands that found them. A false refusal, such as G2's, is listed separately as a cost.
- **Also in.** Any other record that states the same fact.
- **Invariant.** The row of the core's table it holds, or `no`.
- **Decision.** The decision, with the rule (D1 to D6) it stands on.
- **Built.** The commit that built the decision, or "nothing to build".

### The enumeration methods

Each phase applies the methods to its own family and states its commands in its record (contract rule 12).

- **M1, the templates (a closed set).** Each file under `templates/records/` and each file under `templates/setup/` that a party copies into a record is taken apart into every heading, column header, fixed cell value, fixed line and block key.
- **M2, the forms written outside a template.**
  - Each agent definition under `agents/` is read whole for every fixed form it tells its agent to write. This is a closed set.
  - Each `SKILL.md`, each skill's supporting files, and `docs/forms/` and `docs/checks/` are searched for an instruction that fixes a spelling. This is a sample, and the record says so and names the search.
- **M3, the readers (a closed set of files).** In each script under `hooks/`, `skills/*/scripts/`, `.github/scripts/`, `bin/` and `evals/scripts/`, every module constant, regex and string literal matched against a record's or a rule file's text. The result is crossed with M1 and M2, so a form no script reads and a constant no form gives both show.
- **Catches.** Search with `git log --all -S'<distinctive words of the branch's refusal or notice>' -- seal/` and `git log --all --grep` on the reader's name, then read the records each one lists. Records quote a refusal in more than one way, so this is a sample of an open class, and the row says so.

### The decision rules

- **D1.** A form a script reads to hold one of the core's invariants (G5, G12) is kept. Its row lists its catches, and Q1 holds the owner's decision.
  - A key whose presence names its block's kind to an invariant's reader, such as a block's first key, belongs to that invariant's form.
  - A value that reader drops is judged as a form of its own, by D2 to D4.
- **D2.** A form whose value a script uses is kept. To use a value is to copy it, group by it, compute from it, or grade an eval on it.
  - A branch that refuses input its own use cannot read is part of that use.
  - A use whose output no reader reads is no use. For example, a parsed attribute read by no code outside the tests is no use, and the row then falls to D3.
- **D3.** A form a script reads only for its own shape goes, and so does the script's branch. So does a gate branch whose reading has no catch in the records. With them go their cases, their messages and every statement of them (Scope item 7).
- **D4.** A form only agents read loses its fixed grammar. The template and the rule text say in plain words what the party writes, and the cases that pin only its wording go.
  - A word the agents share as vocabulary is already plain words, such as `must`, `should`, `executed`, `read` and `unverified`. What goes there is any script branch or case that checks its spelling. The rule text keeps the word.
- **D5.** A fact stated in two records keeps one home: the record of the party that establishes the fact. The other record cites it by path and heading, or drops it. A copy stays only where its reader cannot open the home, such as the pull request body for a reader on GitHub. In that case the row names that reader.
- **D6.** Where D1 to D5 do not settle a row, the phase decides it, and records the grounds and the document it judged against (`frame/questions.md` Q3).

### The constraints on a build

- **C1.** No record committed under `seal/threads/` and no eval scaffold becomes unreadable to a reader the suite runs. By default, a reader goes on reading a committed record that still carries a form that went, as G10's precedent did, and a case holds that. The committed records leave at the settle. A phase that rewrites committed records in place instead names each one (`frame/questions.md` Q4).
- **C2.** A change to a script follows `CONTRIBUTING.md` *What a change to a gate must carry*. A removed branch names what it caught and what it cost: its census row.
- **C3.** A refusal or notice whose text changes is pinned by a case (contract rule 14). A new case is seen red first (contract rule 15).
- **C4.** A phase whose change reaches an eval scaffold or grader names each case it touched, so the next comparison knows its baseline side is stale (G13).

### The reason census

The set is closed: every paragraph of `skills/core/SKILL.md` and of `skills/agent-contract/SKILL.md` at `c186a59ac`. Both files are identical to the installed 0.31.0 copies (executed: `diff`, exit 0 for each). Each paragraph that states why a rule holds is a row. A paragraph that only states rules, scope or paths holds no reason and has no row: the core's lines 18-23, the table's foot at 108-112, and contract rules 3, 6 and 11. Each row's decision names the step at which an agent weighs the reason, or names the person who needs it. *Kept* keeps the sentence as it stands, and the issue's "cut to the sentence the judgment needs" is applied in the same row where words around the reason can go.

| # | Coordinate | The reason | Decision | Grounds |
|---|---|---|---|---|
| R1 | core *The first value*, lines 29-33 | "Neither does it alone. An agent that judges everything spends more tokens …; one that only runs scripts … adds nothing a script would not. Verification through the workflow serves this value by buying time and stability." | kept | Every party weighs it when it chooses between judging and running a script, and between a check and no check |
| R2 | core *The first value*, line 34 | "…, which is why it sits above them." | cut | The sentence it closes already says the value decides between designs that break no rule. The clause explains where the value sits in the file, which only an editor of the file reads, and loses nothing when it goes |
| R3 | core *Judgment is spent where meaning is the question*, lines 39-42 | A script that answers "these differ" where the meaning is the same gives the worst result, so it does not re-encode the judgment | kept | The party writing or changing a script weighs it at that step, and this census applies it (G2) |
| R4 | core *Each agent judges its own target*, lines 50-51 | "They are separate agents because their targets differ, and …" | cut to "Each reaches its result without leaning on another's verdict, so one agent's mistake does not pass through the next unread." | The paragraph's lead already says each agent judges its own target. The clause restates the lead as a reason for the agent set, which no agent changes. The rest is what an agent weighs when tempted to lean on another's verdict |
| R5 | core *A document is cut by who opens it*, lines 61-62 | "A party pays for every byte of each file it opens, on every spawn that opens it." | kept | Whoever places text in a file weighs it, and this census does |
| R6 | core *A rule is guidance for a judgment*, lines 70-73 | A rule written as "when X ends, do Y" can only be executed, and an orchestrator that executes it relays finding after finding | kept | The orchestrator weighs it at every route |
| R7 | core *A judgment stands on a source document*, lines 79-87 | "…, where the next session reads it and nothing else has to remember it. The guidance improves from that record, not from memory: …" | kept | The orchestrator weighs it when deciding what a judgment row holds. The settling session acts on its second sentence |
| R8 | core *Asking a person is the most expensive step*, lines 88-91 | The design that asks a person costs more and argues why its question is worth it | kept | The orchestrator and the framer weigh it at each question |
| R9 | core *Judgment is not licence to skip a party*, the table's *What it protects* column | What each invariant protects | kept | A party weighs it to tell an invariant from guidance, which this census does (G5, G12) |
| R10 | core *The rule a mechanism is kept against*, lines 116-140 | "existing is no reason to keep it"; "what exists is a reference, not a constraint" | kept | These are rules more than reasons, and every party weighs them before a fix adapts to a structure |
| R11 | contract preamble, lines 18-19 | "…: a rule that would need a per-role exception here is not universal." | moved | Only a person adding a rule to the contract applies this test. `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each* already states it ("That is the test the shared file applies to itself"), so the contract keeps "This file's rules bind every agent, and nothing here is one agent's own" and cites the home (R18) |
| R12 | contract rule 1, lines 30-32 | "Both forms are written out because the failure is a habit, and the right form has to be as easy to copy as the wrong one." | moved to `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each* | It explains why the rule's text shows the wrong form. No agent acts on that, and an editor who drops the wrong form needs it |
| R13 | contract rule 2, line 41 | "…: a suite that is not mentioned reads as a suite that passed." | kept | An agent weighs it when deciding what its hand-back names |
| R14 | contract rule 4, lines 60-61 | "…: a deferral to nobody is how *someone will look at it* becomes *nobody did*." | kept | It tells an agent what counts as an answerer when it names one |
| R15 | contract rule 5, lines 67-69 | "An aggregate … is not a coordinate: the number can be checked while the claim it stands for cannot." | kept | An agent weighs it whenever a count reaches it as a fact |
| R16 | contract rule 7, lines 91-98 | "The rule is about leavings, not about files: …", "The question is whose the thing is, …" | kept | An agent weighs it when deciding what to delete |
| R17 | contract rule 9, line 103 | "Two reasons point the same way." | cut | Once R19 moves the second reason there is one reason left, and the sentence announces it, nothing more |
| R18 | contract rule 9, lines 103-107 | "An edit must be able to fail: … Where the environment leaves no choice, assert that every substitution matched." | kept | An agent with no edit tool weighs it to know what its assertion must cover |
| R19 | contract rule 9, lines 109-115 | "And the routing check sees only the edit tools. … only the pull request's trailer arm is left to catch the change (`docs/checks/the-routing-check.md` *The edit check*)." | moved | No agent acts on it: the rule already tells it to use the `Edit` tool. `docs/checks/the-routing-check.md` *The edit check* already states the whole fact ("A shell write calls no edit tool, which is why every agent edits through the `Edit` tool … the pull request's trailer arm … is what remains for such a change", read), so the paragraph is a copy. Rule 9 keeps one clause that cites that section |
| R20 | contract rule 10, lines 120-127 | "A round is mostly round-trips and command waits, so cut the trips and never the investigation: …", "…, which is where batching pays most." | kept | An agent weighs it each time it decides what to batch |
| R21 | contract rule 12, lines 157-159 | "The instances in view, or a search for one wording, find only the spellings already seen, …" | kept | An agent weighs it when it chooses its method, as each phase here does |
| R22 | contract rule 13, lines 178-179 | "…: a run with the guarantee in place cannot tell the defence from the platform." | kept | It is the test of when the rule applies |
| R23 | contract rule 14, lines 183-186 | "*Nothing raises* is not the claim *says this*: …" | kept | An agent weighs it to decide whether a change is one a person reads |
| R24 | contract rule 15, lines 190-199 | "A case that asserts something is not named … passes against old code …", "A case that passes against the defect it was written for pins nothing, …" | kept | An agent weighs it to choose which red to show |
| R25 | contract rule 17, lines 205-207 | "…: another session's process or file answers to the same name." | kept | An agent weighs it before any cleanup by name |
| R26 | contract rule 18, lines 213-215 | "Code shaped around a wrong check carries the check's defect into the tree and hides it from the next reader." | kept | An agent weighs it when a check refuses its code |
| R27 | contract rule 19, lines 224-225 | "A correction written beside the sentence it corrects leaves both for the next reader to choose between." | kept | An agent weighs it when it decides where a correction goes |

How the preload cites the moved reasons: the contract's preamble carries one sentence, which names `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each* as where a person changing a rule finds the reasons no agent weighs (R11, R12). Rule 9 keeps its citation of `docs/checks/the-routing-check.md` *The edit check* (R19). Plan row A3 weighs a citation per rule against this.

### The measurement

- **The parties and their files.**
  - Each agent's preload is its definition `agents/<name>.md` plus each `SKILL.md` its `skills:` list names: `skills/core/SKILL.md` and `skills/agent-contract/SKILL.md` for all five agents, as read at the base.
  - The session's preload is `skills/core/SKILL.md`, which `hooks/lib/core.py#output` prints.
  - The two `CLAUDE.md` files are left out, because one of them is the machine's and not the plugin's.
  - Each record template is a file under `templates/records/`.
- **The commands.**
  - For each file: `git -C <repo> show <commit>:<path> | LC_ALL=en_US.UTF-8 wc -lm`, at `c186a59ac` and at the commit phase 4's table names.
  - A party's figure is the sum over its files.
  - A file that does not exist at one of the two commits counts 0 there, and the table says so.

## Rule changes

- nothing
  why: This work item's subject is the text of the plugin's forms and of the reasons the preload carries, together with the script branches that read those forms. It edits `docs/` directly in its pull request under `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (G7), moves no section, and so re-points no unsettled design's operation.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The clause on why the first value sits above the rules (R2) | `skills/core/SKILL.md` *The first value: efficient development through the workflow* | Nowhere. The sentence it closes says the same |
| The clause "They are separate agents because their targets differ" (R4) | `skills/core/SKILL.md` *The first value: efficient development through the workflow*, the paragraph *Each agent judges its own target, independently of the others* | Nowhere. The paragraph's lead says it |
| The per-role exception test in the contract's preamble (R11) | `skills/agent-contract/SKILL.md`, the preamble | `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each*, which already states it |
| Rule 1's reason for showing both forms (R12) | `skills/agent-contract/SKILL.md` *1 Read exit codes directly, never through a pipe* | `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each* |
| "Two reasons point the same way." (R17) | `skills/agent-contract/SKILL.md` *9 Edits go through the `Edit` tool* | Nowhere. One reason is left |
| Rule 9's paragraph on the routing check (R19) | `skills/agent-contract/SKILL.md` *9 Edits go through the `Edit` tool* | `docs/checks/the-routing-check.md` *The edit check*, which already states it. Rule 9 cites that section |
| Each form a census row decides D3 or D4, with its script branch, messages, cases, scaffold lines and every statement of it | Named by the row, by `path` and heading or `path#unit` | The row names where each lands, or why nothing needs to. The rows are known only once each family's census runs, so they stand in phases 2 to 4's records, and the review reads each against the diff there. This frame adds no mechanism, so nothing goes in return for one |
| Each second statement of a fact a census row decides D5 | Named by the row | The home the row names |

Framed 2026-11-04 by framer, before the build.
