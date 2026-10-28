# Feature Specification: 1793171931-checks-that-read-text-pass-what-they-cannot-read

## Grounding

Every coordinate below is the tree at `c825fd2c`, the commit this branch was
cut from. `executed` marks a fact a command the framer ran printed; `read`
marks a fact the framer opened and read.

| Policy clause | What it fixes for this work |
|---|---|
| Issue #956 *The change* (read; a ticket, not policy) | The deliverable is one audit, reported and not fixed here, and "the result is one table in this issue". For each check that reads text an agent or a person wrote, the table records what it reads and decides, what it does with an input it cannot read (refuse, pass or skip), and whether a pass can let through what the check exists to stop, "with a probe that shows it". Each fix the table names is filed into `release: 0.24.1` where one work item carries it, and otherwise left to #1038. So no file of the tree changes outside this work item's directory |
| `docs/issues-and-milestones.md` *An issue is its body and its comments together* (read) | "Corrections, measurements and improvements land as comments, and the body is what answers *what does this ticket now ask for*." The audit is a measurement and changes nothing #956 asks for, so the table is posted as a comment on #956 and the body is not edited |
| `docs/issues-and-milestones.md` *An issue is titled like a commit* (read) | Each issue this work files takes a commit prefix and states the symptom in its title |
| `CLAUDE.md` *The rule a mechanism is kept against* (read) | "A check gates only a fact it reads; a noisy reading, or one guessed from words, is a report." So a direction cell rests on a probe that was run, never on a docstring alone. And "a mechanism stays only while its history shows what it caught against what it costs", which is why the larger fixes go to #1038, whose body decides each one by the record before anything is built (read) |
| `docs/the-record-layout.md` *Whether a line is live is asked by what the line does* (read, `:140-185`) | The policy already chooses a direction for three kinds of line: a line that holds a claim or an anchor is read on doubt and the wrong answer is loud; a line that excuses or declares is not taken on doubt; a line rows are counted on is blanked the same way on both sides. A reader this section names is judged against the direction it states, and a probe that contradicts that statement is a defect of the reader, not a new direction |
| `SECURITY.md` *What is in scope* (read, `:47-53`) | "A gate that reports a pass it did not establish (**a check that fails open is a security defect here, not a correctness one**, and each gate's test file holds its cases for that class)". So a `yes` in the table's let-through column is a security-class finding by this repository's own definition, and each gate's own test file is the first place a probe looks for an existing case |
| `SECURITY.md` *Reporting* (read, `:3-10`) | A suspected vulnerability is reported privately, not in a public issue. A row whose let-through reaches one of the two situations *What this project is, and where its risk actually sits* names (a fork's pull request in CI, or an untrusted repository checked out locally) is not written in public; `questions.md` Q3 holds the default |
| `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* (read) | A line a check reads is read in one spelling and a near miss is refused at its line. This already states, for the lines a check reads in skills, agent definitions, templates and frames, the rule #923's Q9 asks to put into `CLAUDE.md`. The table's closing paragraph names it beside `SECURITY.md` for Q9 (`questions.md` Q1) |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | The policy root is not edited by a pull request, and this work states no rule change |

## Scope

In:

1. **The class, stated so the review can test the boundary.** A reader is in
   the class when both hold:
   - it reads text whose author is a person or a model, with no script that
     writes that text in a fixed shape: a record under `seal/threads/`, a
     policy or skill document, `seal/config.md` or `seal/README.md`, a
     pull request body, a commit trailer, a Bash command a model typed, a
     test's or a grader's view of a file an agent wrote, or a source file
     read as text rather than through a parser;
   - its result is a verdict something acts on: a hook's deny, a non-zero
     exit, a CI step that fails, a command an agent runs and reads as
     *nothing to refuse* (`seal unverified`, `seal pr-body --check`,
     `seal rules --check`, `seal fold`, `seal settle --apply`), a stamp a
     person reads as *sealed*, a test case, or an eval grader.
2. **The inventory** in *The readers to audit* below, rows R1 to R43, each
   audited into one row of the table.
3. **The citation reader** of #956's paragraph *The citation reader*,
   re-based to `c825fd2c` as *The citation reader, re-based* below says.
4. **The table**, posted as one comment on #956, its closing paragraph
   giving Q9 its inputs (`questions.md` Q1).
5. **The fixes the table names, filed**: one issue per module whose readers
   need a fix, into `release: 0.24.1`, where one work item carries it; a
   `#1038` cell where it does not (*The table* below defines both).

Out:

- **Fixing any reader.** #956 *The change*: "reported and not fixed here".
  No file of the tree changes outside
  `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/`,
  and a probe leaves nothing (contract rule 7).
- **What #1111 keeps.** #1111 decides each phrase pin on a rule sentence:
  kept where the phrase is a fact a reader needs fixed, otherwise removed with
  its rule's `check:` line changed, starting with `PINS` of
  `tests/text/test_the_agent_contract_holds_the_universal_rules.py`, and it
  records the count of phrase pins per `tests/text` module (#1111 *What
  changes* and *Done when*, read). This audit gives #1111 one row, R38: the
  direction a positive phrase pin fails in (a reworded rule turns it red), and
  it judges no pin one by one. A negative pin, an assert that a spelling is
  absent, is not a phrase pin on a rule sentence and is this audit's, R37.
- **What #1043 keeps.** #1043 corrects
  `.github/scripts/gather_changelog.py:43-44`, builds the one case that
  resolves every `` `<path>.md` *<section>* `` citation outside the records,
  and removes the `implement`-only case (#1043 *Done when*, read). This audit
  keeps R33 to R36: how the citation readers standing at `c825fd2c` fail on
  what they cannot read, how each unresolved citation at `c825fd2c` fails,
  whether the reader shape #956 describes is precise enough, and the
  direction row of #1043's case once it lands (`questions.md` Q2). It builds
  no citation case; its resolver is a probe and is deleted.
- **What #1038 keeps.** Deciding, by the record, build or drop for each fix
  this table sends it (#1038 *The candidates*, item 3, read). This work does
  not edit #1038: its body already reads #956's larger fixes from this table.
- **#923's Q9**, whether `CLAUDE.md` gains "a gate fails closed: input it
  cannot read is refused, never passed". The owner decides it with the table
  in hand (#956 *The change*); `questions.md` Q1.
- **The rows of `seal/follow-up.md` the audit meets.** Three rows there are
  instances of this class: the folded readers of
  `tests/github/test_release_completeness_check.py` and
  `tests/github/test_label_merged_on_release_branch.py`, and the guard of
  `tests/text/test_a_rider_reaches_its_file.py` that tests one spelling
  (read). The table names each under R37, and a fix it files names the row it
  answers. The rows stay: deleting one is an edit to the tree, and the fix
  that answers it deletes it.
- **Readers outside the class**, each with the reason, so the review can
  contest the line:
  - readers of code through a parser that raises on what it cannot parse:
    `skills/verify/scripts/arm_check.py`, `mutation_check.py`,
    `test_layout.py`, and the `ast` half of `tests/censuses.py`;
  - readers of text a script writes in a fixed shape:
    `skills/verify/scripts/session_cost.py` (harness transcripts),
    `.github/scripts/durations_union.py`, `.github/scripts/run_tests.py`,
    `skills/verify/scripts/pytest_record/agentic_pytest_record.py`,
    `skills/verify/scripts/broad_gate.py` beyond the config row R16 reads,
    and `chain_check.py#newest_run`, which reads `trail/gate.md` as
    `seal gate --record` writes it;
  - actors, which do something with what they read and return no verdict:
    `.github/scripts/close_issues_on_release.py`,
    `label_merged_on_release_branch.py`, `tracker_labels.py`,
    `roll_flow_measurement_issue.py`, `publish_release_note.py`,
    `release_seal.py`, `hooks/root-migrate.py`, `hooks/sealer-stamp.py`
    (draws what R5 queued). The check over `close_issues_on_release.py`'s
    reading is R26, and R28 compares the three readers of a closing keyword;
  - reports and notices that never fail: `payload_meter.py`,
    `.github/scripts/release_report.py`, `seal rules <doc>` without
    `--check`, `hooks/implementer-notice.py` (its reading is R10's),
    `hooks/version-check.py`, `.github/scripts/plugin_directory_check.py`;
  - exact matches on a field the harness passes: `hooks/implementer-mark.py`
    and `hooks/lib/implementer.py#mark_for` (`subagent_type`, and it decides
    nothing), `hooks/review-skill-gate.py` (the skill name).
  A phase that finds one of these meets both conditions of item 1 adds it as
  a row and says so in its phase record.
- **Files other branches change.** #913 changes `hooks/lib/config.py`,
  `skills/verify/scripts/pact_check.py` and
  `skills/verify/scripts/coordinates.py` (executed,
  `git diff --name-only c825fd2c...fix/913-pact-check-reads-the-retired-grammar`).
  R16, R17 and R26 read the base version at `c825fd2c`, and their rows say so
  and name #913. #1039, #1040 and #1042 had changed no file the inventory
  names when this frame was read (executed, the same command per branch).

## The readers to audit

The inventory was taken by reading the module docstring of every tracked
`.py` file under `hooks/`, `skills/*/scripts/`, `.github/scripts/` and
`evals/scripts/` (executed, `ast.get_docstring` over each) and the function
list of each candidate (executed, `grep -n -E '^def |^class '`), then opening
the readers named below (read). `path#unit` names a unit of code at
`c825fd2c`. The last column is what the tree already says of the reader's
direction; it is a claim for the probe to test, not a verdict.

### Family A: the records on the pull-request path (phase 1)

| Row | Reader | The text it reads, and who writes it | What the tree already says |
|---|---|---|---|
| R1 | `hooks/lib/blocks.py#walk_text` | which lines of any markdown file below stand inside a fence or a comment block | where the walk is unsure it decides nothing and the caller keeps its base reading (module docstring, read) |
| R2 | `skills/code-review/scripts/chain_check.py#grammar` | the two tables of `docs/the-review-record.md` *The round record*, the owner's | a table it cannot read stops it at exit 2, never a pass (`docs/the-review-record.md:63-86`, read) |
| R3 | `chain_check.py#findings`, `#record_lines`, `#confirmations`, `#round_of` | `trail/rounds/round-N.md`, the proofer's and the fix pass's | a line the check cannot read is refused whatever the verdict (`docs/the-review-record.md:104`, read) |
| R4 | `chain_check.py#verdicts_of`, `#verdict_word` | `guarantee.md`'s `Verdict:` line, the sealer's | #956 names it as reading through emphasis; `verdict_word` strips emphasis before matching a retired word (`:1878-1890`, read) |
| R5 | `skills/verify/scripts/seal_stamp.py#queue_for_written_guarantee` and `#sealed_names` | the same `Verdict:` line, through R4's two functions (`:1103-1104`, `:1286-1287`, read) | the stamp is queued where the file reads one `Verdict:` of `sealed` (`:1252`, read) |
| R6 | `chain_check.py#target_row` | `guarantee.md`'s `Target SHA` row, the sealer's | nothing found |
| R7 | `chain_check.py#frame_foot` | the framer's mark and `Reframed` lines at the foot of `frame/design.md` | a design that does not end with the mark is refused (`:1563`, read) |
| R8 | `chain_check.py#routing_trailers`, `#trailer_findings` | `Seal-Routing` trailers of commit messages, any committer's | a commit with no such trailer is not judged (module docstring, read) |
| R9 | `chain_check.py#original_of`, `#originals_of` | `original:` lines of round records and `guarantee.md` | nothing found |
| R10 | `hooks/lib/routing.py#parse`, `#shown`, `#table_rows`, as `chain_check.py`, `hooks/routing-edit-gate.py#decide` and `hooks/question-gate.py#main` call them | `routing.md`, the orchestrator's | the question gate reads every way of not reading the declaration as the attended answer and prints nothing (`hooks/question-gate.py` docstring, read); `#shown` keeps its older reading below an unclosed fence or comment (`docs/the-record-layout.md:163-168`, read) |
| R11 | `hooks/lib/routing.py#rounds`, `#rounds_unreadable`, `#stray_rounds` | the file names under `trail/rounds/` | nothing found |
| R12 | `skills/settle/scripts/rule_changes.py#parse` | `## Rule changes` of `frame/design.md`, the framer's | a block that does not match whole is refused at its line, and a near-miss heading is refused (`skills/settle/SKILL.md` *Rule changes*, read) |
| R13 | `skills/verify/scripts/unverified_check.py#check_text`, `#parse_section`, `#nothing_block`, `#closing_word`, `#live_lines` | `## Not verified` rows of `gaps.md`, the crafter's and the orchestrator's | the module fails on a section it cannot read, "because a tolerant parser reports zero" (`:20-25`, read); #956 still names its "tolerant readings", and which remain is this row's to find |
| R14 | `skills/verify/scripts/deferral_check.py#inspect`, `#runners_in`, `#read_events` | CI workflow files and other CI configs a person wrote, read to say whether a named answerer exists | nothing found |
| R15 | `skills/code-review/scripts/pr_body.py#_check`, `#split` | a pull request body file, the orchestrator's, against the records | `--check` says whether the part above the heading is the records' text (module docstring, read) |

### Family B: the hooks, the config and the commands (phase 2)

| Row | Reader | The text it reads, and who writes it | What the tree already says |
|---|---|---|---|
| R16 | `hooks/lib/config.py#config_table`, `#config_value`, `#declared_mode`, `#policy_root`, `#reference_roots`, `#hidden_lines` (base version; #913 changes the file) | `seal/config.md`, a person's or `seal mode`'s | a row below an unclosed fence declares nothing, and one below an unclosed comment opener still declares (`docs/the-record-layout.md:158-162`, read) |
| R17 | `hooks/lib/config.py#gfm_table`, `#read_table`, `#pact_declaration`, `#pact_signers`, `#baseline_commit` (base version; #913) | the pact declaration and signer tables, and `seal/parity.md`'s `Baseline commit` row | nothing found |
| R18 | `hooks/mode-gate.py#undeclared`, `#decide`, through R16 | the `Mode` row | "a repository this cannot read is one it says nothing about" (`hooks/mode-gate.py:68`, read) |
| R19 | `hooks/lib/optin.py` `MARKER` and `EARLIER_HEADINGS` | the first line of `seal/README.md` | a `seal/` without the marker declares nothing (module docstring, read); every gate runs only where this reads the marker |
| R20 | `hooks/stub-remove.py#is_stub` | the second line of each file in the clone's git hooks folder | a file without the stub marker is never touched (module docstring, read) |
| R21 | `hooks/lib/tokens.py` | the bare words of a Bash command, the model's, read for consent tokens | "a token it cannot read costs one refusal" (`:4-7`, read) |
| R22 | `hooks/lib/one_heredoc.py` | one heredoc shape in a Bash command | it admits one shape, byte for byte (module docstring, read) |
| R23 | `hooks/lib/cmdline.py` and `hooks/lib/cmdline_base.py`, as `hooks/worktree-guard.py` calls them | Bash commands, the model's | no load fallback, and a command it cannot read before expansion is a `CONSTRUCT` (`cmdline.py:26`, `cmdline_base.py:48`, `:1760-1790`, read); `docs/worktree-guard-spec.md` holds the guard's rule |
| R24 | `skills/verify/scripts/pact_check.py#check`, `#grade`, `#near_miss`, `#path_map`, with `skills/verify/scripts/coordinates.py#resolve_unit` (base versions; #913 changes both) | pact anchors in a signer's Grounding, and `seal/pact.md`'s clauses | a line that holds an anchor is read on doubt and the wrong answer is loud (`docs/the-record-layout.md:145-152`, read) |

### Family C: the release and document checks (phase 3)

| Row | Reader | The text it reads, and who writes it | What the tree already says |
|---|---|---|---|
| R25 | `.github/scripts/gather_changelog.py#live_markers`, `#leaves_open`, `#ungathered`, `#heading_re`, as `--check` runs in `.github/workflows/hygiene.yml:124-130` | changelog fragments and the release file's markers | a changelog marker is a declaring line and is not taken on doubt (`docs/the-record-layout.md:153-157`, read) |
| R26 | `.github/scripts/issue_claims_check.py#read`, `#prose_only`, `#claimed_spans`, as `hygiene.yml:62-66` runs it | the pull request body, the orchestrator's | the body's claims are printed and the correction is the author's (`docs/issues-and-milestones.md:261-264`, read); whether the step can fail is this row's to record |
| R27 | `.github/scripts/release_completeness_check.py#judge` and the set D it reads | the release range's pull request bodies' closing keywords an open issue of the milestone that the range carries no closing keyword for fails the release; a carried issue with no `merged:` label reports and passes; a reverted squash stays carried (module docstring, read) |
| R28 | the closing keyword as three readers read it: R26, R27 and `.github/scripts/close_issues_on_release.py#keywords_in` | pull request bodies, the orchestrator's | `close_issues_on_release.py` is an actor (*Scope*, Out); this row records whether the three read one near miss alike, since a body R26 reads as claiming and the closer reads as not is an issue left open with nobody told |
| R29 | `.github/scripts/rules.py#check_lines`, `#parse`, `#line_problems`, `#check` | the `check:` lines of every rule file, every author's | `Unreadable` is raised for a file it cannot read (`:93-107`, read) |
| R30 | `skills/settle/scripts/fold_check.py#index_problems`, `#past_ceiling`, `#config_rows` | the policy root's documents and its `README.md` index | nothing found |
| R31 | `skills/settle/scripts/settle.py#open_rows`, `#survey`, with `--apply` | released work items' records, read for open rows before their directories are removed | the rows `seal settle --apply` refuses to take with a directory are read through `unverified_check.py` (`unverified_check.py:1323`, read) |

### Family D: the test-side and eval readers (phase 4)

| Row | Reader | The text it reads, and who writes it | What the tree already says |
|---|---|---|---|
| R32 | the `Reads:` lines #905 names | none stand: no tracked file outside the records carries a line opening `Reads:` (executed, `git grep -c -E '^\s*(#\s*)?Reads:' c825fd2c` outside `seal/`, `changelog/` and `CHANGELOG.md`, no output); the last commit touching one is `af9c924b` (#964) (executed, `git log -S'Reads:'`) | the row records the reader gone, with the commit that removed it |
| R33 | `tests/behaviour/test_the_set_a_work_item_always_has.py#dangling_implement_citations` and `#cited_files` (`:443-500`); the contract-rule resolver of `tests/text/test_the_agent_contract_holds_the_universal_rules.py` (`:73`, `:286`); the citation pin of `tests/text/test_broad_gate_rule.py:80-86` | citations in every tracked text file outside the records | the `implement` case reads whitespace-collapsed text and fails when fewer than ten citations are recognised (`:495`, read) |
| R34 | each unresolved `` `<path>.md` *<section>* `` citation at `c825fd2c` | the same files | *The citation reader, re-based* below |
| R35 | the reader shape #956 describes: a path immediately followed by an italic heading, read across a line break, with markup inside the heading handled | the same files | *The citation reader, re-based* below |
| R36 | #1043's tree-wide citation case, once it lands | the same files | #1043 *Done when*: a citation a pending `## Rule changes` item corrects is reported, not failed, until the settle (read); `questions.md` Q2 |
| R37 | negative pins: an assert that a spelling is absent from a tracked file, as a class, with the three instances `seal/follow-up.md` names (*Scope*, Out) | documents and source read as text | a `not in` on a literal passes every spelling but one; 305 asserts of the shape `assert "<12 or more characters>" not in` stand under `tests/` (executed, the command in `questions.md` Q4), counting asserts on a script's output too, so the figure bounds the class from above |
| R38 | positive phrase pins on a rule sentence, as a class | documents | a reworded rule turns the case red; #1111 decides each pin (*Scope*, Out) |
| R39 | `tests/censuses.py#_exempted`, `#_held`, `#_trailing` | exemption comments a person writes in source files | nothing found |
| R40 | the eval graders under `evals/behaviour/<agent>/<case>/graders/`, as `claude plugin eval` and `evals/scripts/noninferiority.py#grade` read them | files and tool calls the agent under test wrote | 155 grader files: 76 `regex`, 54 `tool_used`, 25 `file_exists`; 56 carry a lookahead or lookbehind, the shape an absence takes in a regex (executed, `find` and `grep` over `evals`) |
| R41 | `evals/scripts/noninferiority.py#check` | a comparison record `compare` writes and a person may edit | "A record the check cannot read or cannot split is one production reads" (`:297`, read) |
| R42 | `evals/scripts/replay_targets.py#labelled_round`, `#findings`, `#confirmed` | round records, read to make the replay cases' truths | nothing found |
| R43 | `chain_check.py` and `seal_stamp.py`, and any other pair found in phases 1 to 4 that read one line with two readers | the line both read | R4 and R5 share one reader; the row records every other pair a phase finds, and whether the two read a near miss alike |

### The citation reader, re-based

#956 asks how each of "33 of 311 citations" fails, from #1005's resolver at
`a16acb40`. That resolver's command and its 33 are not in #1005's records:
`0ed5dd3b:seal/specs/1792627930-the-section-sign-is-still-syntax/spec.md:186-190`
states the counts and the kinds of false hit in one sentence, and no other
file of that directory names the 33 (executed, `git show` and `grep` over each
file). A count with no command cannot be re-run, so R34 replaces the 33 with
the unresolved citations at `c825fd2c`, read by a probe resolver whose command
the phase record carries. #1043's own read found 22 unresolved of 329, 20 of
them the scanner's misses and 2 real, with no command given (#1043 body,
read); R34 records how its own count compares.

R34 classifies each unresolved citation as one of: a real miss (the heading
or bold rule lead is not in the named file); or the resolver's miss, by kind
(a wrap across a `#` comment marker, a string split across lines, an
f-string, markup inside the heading, a bold rule lead read as absent, or a
kind the phase names). The citation of `docs/the-record-layout.md` at
`.github/scripts/gather_changelog.py:43-44` is a real miss at `c825fd2c`
(#1043 body, read), so a probe that does not report it is blind, and the
phase says so before it classifies anything.

R35 measures the shape #956 describes over the same files. **Precise enough**
means both: every citation it refuses at `c825fd2c` is a real miss, so it
refuses no correct citation; and it recognises every citation
`dangling_implement_citations` recognises, so it loses none the standing case
reads.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 every row audited | Given the inventory R1 to R43, when phase 4 closes, then each row has a table row with every column filled, or the phase record of its family says why it left the class; and a reader a phase added is a row with the reason | the four phase records, read against *The readers to audit* |
| S2 every direction is executed | Given a row's `On input it cannot read` cell, when the review reads it, then the phase record carries the input fed, the command, and the exit code or verdict it printed, labelled executed. A `refuses` cell is probed as a `passes` cell is | the phase records; a sample re-run by the proofer |
| S3 a let-through is shown | Given a `yes` in `Lets through`, when the review reads it, then the cell names what the check exists to stop, and the probe shows that thing passing the check | the phase records |
| S4 the near miss is the likely one | Given a probe, then its input is a near miss of the kind the record shows: emphasis or a code span around a value, a wrap across lines or across a comment marker, a case or whitespace variant, an extra or missing cell, a duplicated line, an empty or absent file | the phase records |
| S5 the citation probe can see | Given R34's probe, when it runs at `c825fd2c`, then it reports the citation at `.github/scripts/gather_changelog.py:43-44` before any classification is recorded | `trail/phases/phase-4.md` |
| S6 every fix is filed | Given a row whose `Fix` cell is not `none`, then the cell names an issue filed into `release: 0.24.1`, or reads `#1038`; each filed issue is titled like a commit, names the rows it answers with their coordinates and probes, and states *Done when* | `gh issue view <N> --json title,milestone,body` for each, read against its rows |
| S7 the comment is the record | Given the table in `trail/phases/phase-5.md`, when the comment is fetched with `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/<id> --jq .body`, then it equals that table and its closing paragraph | `diff`, exit 0 |
| S8 Q9 has its inputs | Given the closing paragraph, then it counts the rows per direction, names every row whose `Lets through` is `yes`, and names `SECURITY.md` *What is in scope* and `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* as where the rule already stands | the comment, read |
| S9 the tree is unchanged | Given the branch at its last commit, then `git diff --name-only c825fd2c..HEAD -- . ':!seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read'` prints nothing, and `git status --porcelain` lists no probe | executed by the proofer |
| S10 nothing private is public | Given a row whose let-through reaches one of `SECURITY.md`'s two situations, then no committed record, comment or issue carries its input or its probe (`questions.md` Q3) | the phase records and the crafter's hand-back, read |

## Data & interfaces

**The table.** One markdown table, one row per inventory row, in this column
order:

| Column | What it holds |
|---|---|
| Row | the inventory number, R1 to R43, and any row a phase added |
| Reader | `path#unit` at `c825fd2c`, and "base version; #913" where R16, R17 or R24 |
| Reads and decides | the text, its author, and the verdict the reader gives |
| On input it cannot read | exactly one of `refuses`, `passes`, `skips` or `mixed` |
| Lets through | exactly one of `yes`, `no` or `limit`, with the thing it exists to stop |
| Probe | the near miss fed and what the reader answered, executed; the full command stays in the phase record |
| Fix | `none`, an issue number filed into `release: 0.24.1`, or `#1038` |

**The direction words.** An input the reader cannot read is one inside the
domain of the text it reads whose spelling or shape the reader does not
recognise (S4 lists the kinds).

- `refuses`: the input fails the check, a deny, a non-zero exit or a finding,
  and the refusal names its file or line.
- `passes`: the check answers as it does for a well-formed input that
  satisfies it.
- `skips`: the reader treats the input as absent, and the cell says what
  absence gets from the check.
- `mixed`: the reader's arms answer differently; the cell names each arm and
  its word.

**The let-through words.**

- `yes`: a pass or a skip lets through what the check exists to stop, and the
  probe shows it.
- `no`: the cell says why: the input it passes cannot carry what the check
  stops, or a named second reader refuses it, by its row number.
- `limit`: the shape cannot arise in the one-issue automation flow, and the
  cell says why; its fix is a limit sentence in the document that states the
  reader's rule.

**Where a fix goes.** One work item carries a fix when the fix changes only
the reader's own module and that module's test files, or writes sentences
into documents, and adds no module, no gate and no reader shared across
modules. Such fixes are filed into `release: 0.24.1`, one issue per module,
and every `limit` sentence in one issue. Every other fix, such as a reader
shared by several modules, a new gate, or a rule over the tree like Q9's, is
`#1038`.

**The comment.** Posted on #956 with `gh issue comment 956 --body-file
<file>`. It opens with one sentence naming the commit the audit read,
`c825fd2c`, and this work item; then the table; then the closing paragraph
of S8. A comment holds at most 65,536 characters; where the text is longer,
the table splits into two comments by family, and the phase record names
both.

## Rule changes

- nothing
  why: the audit reports on the readers and changes no rule of the policy root; Q9's rule is the owner's to decide with the table in hand

## Removes

- nothing
  why: no tree file changes; every probe is deleted before its phase closes and was never committed

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-28 by framer, before the build.
