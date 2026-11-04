# Design: each statement is corrected to the tree (#1346, #1338)

Issue #1346 and issue #1338, both in milestone `release: 0.31.2`. The framer
read #1346's body, #1338's body and the bodies of the ten closed issues
#1346 lists (#1334, #1335, #1336, #1337, #1339, #1340, #1341, #1342, #1344,
#1345) with `gh issue view <N> --json body,comments` on 2026-11-04
(executed). #1346 and #1338 have no comments. Each of the ten has one
comment, which says it was folded into #1346 and that its body stays the
item's scope and *Done when* (executed). No comment changes a request.

The measure each issue cites was taken at `94635718e`. This frame reads
every coordinate at a3e08d64a, the branch's HEAD, which differs from
`94635718e` in 61 files (executed: `git diff --stat`). Each statement below
was found again at HEAD with `git grep` or `sed -n` at the line given
(executed), so the line numbers here are HEAD's.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `routing.md` (read) | Planning `framer`, Implementation `crafter`, Automation `yes`, through the review chain, open the pull request. The *Why this way* paragraph takes #1346's ten items and #1338 in one pull request |
| The orchestrator's spawn (the orchestrator's finding; the framer opened the coordinates it names) | One pull request into `release/v0.31.2`. #1338 names the existing label `hooks-gates` and creates none. #1336 regenerates the eval cases and runs no paid eval. #1343 is out of this work item: the orchestrator edits the tracker for it with no commit |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "A fact has one source, and every other place links to it." This decides #1334 (the README cites the template and lists no items), #1339 (the template cites the section and lists no items) and #1341 (the sentence names the copy the script reads and counts no holders). "A change rewrites the text it amends in place, and in the same commit removes what stood on the old fact." So the case that pins each corrected sentence moves with it (S1, S9) |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | This work item's subject is the text of documents, templates, a config comment and test docstrings. It corrects each statement to the tree and changes what no rule says. It edits `docs/releasing/branch-and-release.md`, the experiment document under `docs/experiments/` and, from round 1's fix pass, `docs/layout/one-root-by-lifetime.md` directly in its pull request, as 1793750411 and 1793756609 did for their `docs/` text (read: their `## Rule changes`). `## Rule changes` holds the no-change block |
| Unsettled `## Rule changes` (executed: `awk` over the `## Rule changes` section of every `frame/design.md` under `seal/threads/`) | Two designs hold pending operations: 1793726048 on `docs/running/the-run.md` *The run*, and 1793732301 on `docs/layout/the-record-layout.md` *The root records*. This work touches neither document and moves no section, so it re-points nothing. Keeping the module name in S4 is part of why: a rename would edit the `check:` line at `docs/layout/the-record-layout.md:188`, which stands in the section 1793732301 changes |
| `docs/layout/the-record-layout.md` *A change to the way of working writes its process row in its own fragment* (read) | The diff touches none of `skills/core/SKILL.md`, `CLAUDE.md`, `agents/*.md`, `skills/*/orchestration.md` or `skills/implement/bootstrap.md`. So the fragment carries no `### Process changes` table |
| `skills/implement/orchestration.md` *Orchestrator: how the work is routed*, the paragraph "Which branch the pull request lands on is decided with the routing question" (read), and `.claude-plugin/plugin.json` (executed: `grep version` prints `0.31.1`) | The first pull request into `release/v0.31.2` moves `plugin.json` to `0.31.2` in the commit that adds the work item's changelog entry. The last build phase makes that commit, as the orchestrator's spawn of phase 4 delegated it |
| The latest release's `### Process changes` table (executed: `gh release view --json body`) | Its rows come from #1317, #506 and #1319, and none touches a file this work edits. #1319 changed the five sealer eval scaffolds. Each of them is still the generator's output (the next row) |
| The eval cases are the generator's output at HEAD (executed: `evals/scripts/rule_cases.py --out` run from a `git clone --no-local` at a3e08d64a, then `diff -rq` of each case it wrote against `evals/behaviour/`) | All 17 `rule-*` cases are byte-identical to the generator's output. So the diff of S3's regeneration holds only what S3 changes |
| What S3's regeneration changes (executed: the four forms changed in the scratch clone's `rule_cases.py`, `routing` given the work item id, and the cases regenerated and diffed) | The generator exits 0. Exactly 17 files differ, one `scaffold.sh` per case. The changes are 17 routing titles, 11 scenario headings, the design title in 10 cases (5 sealer, 4 crafter builds, 1 proofer) and 5 round titles. `routing()` at `evals/scripts/rule_cases.py:157` takes no work item id, and its one caller at `:203` holds `item`. The title `# Routing: <work-item-id>` therefore needs that argument |
| Who reads the four fixture forms (executed: `git grep` for each old form across `tests`, `evals/scripts`, `evals/README.md`, `skills`, `hooks` and `.github`) | No script and no grader reads a fixture's title. `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py#RECORD_LINES` exempts the scenario heading in its exact spelling, so it moves with S3. Round titles in the old shape and `# routing` also stand in test fixtures under `tests/` (`test_chain_check.py`, `test_replay_targets.py`, `test_broad_gate.py`, `test_seal.py`, `test_settle.py`, `test_optin.py`, `test_finding_counts.py`, `test_noninferiority.py`). The measure judged that a title in a test fixture states nothing of the form, because its reader does not read the title (`seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-2.md` *Whether the frame holds*, the item on a fixture's title) |
| `tests/e2e/teammate/test_teammate_flow.py:64` (read: the module docstring and the uses of `SPEC` at `:96` and `:101`) | The fixture design is written into a repository that the steps of `templates/setup/hygiene.yml` run over under `bash`. No agent reads it, and no step reads its title. It is a test fixture of the kind the row above describes, so it stays (O3) |
| What the `seal/` README entry is read by (executed: `git grep` for `seal-README` and `"seal", "README` under `tests/`; read: each case it lists) | `tests/behaviour/test_first_setup_asks_once.py:579` holds the two files byte-identical. `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#ROW_READERS` lists `templates/setup/seal-README.md` as a document that tells a session which language row to read, and its case asserts `Record language` in the file. The entry S1 rewrites is the file's only mention of `Record language` (executed: `grep -n`). So the entry leaves `ROW_READERS` with the list. The other readers assert `config.md`, `follow-up.md         schedulable items`, `seal export` and the settle sentences, and none of those is in the entry's item list |
| The `config.md` items stated as a set elsewhere (executed: a probe listing every paragraph of the tracked `.md`, `.py`, `.yml` and `.sh` files outside `seal/threads/` and `evals/behaviour/` that names three or more of the template's ten items in backticks) | Five paragraphs. The two README copies are S1's. `skills/config/SKILL.md:38` tables the ten items the template documents and agrees with it. `skills/config/SKILL.md:130` names the two fold rows that `templates/setup/config.md` *The fold's values* gives. `tests/skills/test_fold_check.py:220` names two rows a fixture leaves empty. The last three hold. The probe matches backticked names, so it is a sample of #1334's class |
| `docs/releasing/branch-and-release.md:204-206` and its pin (read; executed: `git grep 'holds the one copy'`) | `tests/text/test_the_release_tail_does_not_end_at_the_tag.py#test_the_fixed_name_sentence_names_the_file_that_holds_the_name` asserts the drifted words `.claude-plugin/plugin.json\` holds the one copy`. The case moves with the sentence (S9). `.github/scripts/plugin_directory_check.py#plugin_name` reads the name from `plugin.json` and carries no literal (read). `.claude-plugin/marketplace.json` spells the name at its entry and in `renames`, and both READMEs spell it in two install lines each (read) |
| The tracker's labels (executed: `gh label list --limit 200`) | `hooks-gates` is listed and `gate` is not. `.github/ISSUE_TEMPLATE/gate-misfired.md` is the only issue form that has a `labels:` line, so #1338's class is that one line |
| `seal/follow-up.md` (read whole) | No row waits on this work as its prerequisite. The row at `:42` and the blank line at `:45` are S6's |
| Where the work item `1788817289-local-mode-from-first-setup-to-the-gate` stands (executed: `git log --diff-filter=D`, `git cat-file -e`, `git show ... \| grep -n`) | It lived at `seal/specs/1788817289-local-mode-from-first-setup-to-the-gate/`. f51e634d2 (#497, #504) removed it, and its design was `spec.md`, not `frame/design.md`. `git show v0.13.0:seal/specs/1788817289-local-mode-from-first-setup-to-the-gate/spec.md` holds the heading *The sharp question — where an untracked declaration lands* at line 43. A citation of it takes the hex commit `aa687d357`, the parent of f51e634d2, whose `spec.md` is byte-identical to `v0.13.0`'s: `tests/censuses.py#old_names` refuses a removed path cited under a `vX.Y.Z:` prefix, since `HISTORY_PATH` reads only a hex commit (executed by phase 4, `trail/phases/phase-4.md`) |
| `skills/code-review/scripts/chain_check.py#read_record` (read, through the measure's *Instances R12* and `git grep`) | Its docstring states where the file is read from and warns about nothing. S6 therefore states the row's argument in the row's own words |
| `tests/text/test_a_rider_reaches_its_file.py#COORDINATE` (read) | A row of *Schedulable items with nowhere else to go* may not hold `<file>.md:<line>`. S6's new citation names a file and a heading, with no line |
| Which test modules still raise a `SyntaxWarning` under `ast.parse` (executed: a `test_tmp_*` probe over `git ls-files 'tests/*.py'`, under Python 3.12.11, 3.13.9 and 3.14.3, the versions CI's legs run; the probe was deleted after the run) | 155 modules, no warning under any of the three. The `warnings.catch_warnings` block in `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#derivers` catches nothing. The reason its docstring gives names two modules that left the tree. So the catch and its paragraph go (S5, `## Removes`). The suite sets no `filterwarnings` and no `-W` (executed: `grep` over `bin/test`, `.github/workflows/test.yml`, `.github/scripts/run_tests.py` and `tests/conftest.py`). A warning that a later module raises would therefore print in pytest's summary and fail nothing |
| Removed modules cited under `tests/` (executed: every basename `git log --diff-filter=D --name-only -- 'tests/*.py'` lists that no tracked test file has at HEAD, 131 names, each searched by its first 28 characters with `git grep -F` over `tests/*.py`, output de-duplicated with `sort -u`) | 48 lines, at a3e08d64a and at 8bb802586 (executed by phase 3). Each line was read: the eleven statements of S5 that cite a module, plus one more that the measure missed because a line break splits the name: `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py:38-40`, "its structural half is the precedent this follows". The other lines name the moment they describe, such as "#942's phase 6 placed these cases from", or name a module the tree holds |
| Removed cases cited under `tests/` (executed: every `def test_*` that `git log -p -- 'tests/*.py'` shows removed and that no tracked test module defines at HEAD, each matched by a probe over the text of `tests/*.py`, with a name that a line break splits joined first; the probe was deleted) | 7 names. Four are S5's statements. `test_the_fence_rule_agrees_with_the_config_reader`, `test_it_does_not_pass_n_auto` and `test_the_fourth_axis_is_a_record_and_not_a_fourth_checkbox` name the moment they describe ("at `release/v0.16.0`", "inverted from", "Renamed and rewritten from"). These are the three the measure counts as holding |
| `tests/text/test_the_rules_claude_md_names_have_one_home.py` (read: `:1-50`, `LINKED` and `CARRIERS`) and its citations (executed: `git grep`, outside `seal/threads/` and `.test_durations`) | The module holds three things: each rule's home states its needles (`RULES`), no carrier repeats a needle (`CARRIERS`, with `CLAUDE.md` first), and each linked file names its home (`LINKED`, which holds no `CLAUDE.md`). Its docstring says `CLAUDE.md` keeps a row for each home (`:1`, `:11-13`, `:41-46`), and `CLAUDE.md` keeps none. The name is cited once outside the records and the durations, in the `check:` line at `docs/layout/the-record-layout.md:188` |
| `tests/hooks/test_launch.py:202-212` and `tests/censuses.py:756-764` (read), and every citation of `test_launch` (executed: `git grep`) | `test_launch.py` derives the set and holds it to the table. `tests/censuses.py#floor_syntax` refuses what the floor cannot run. Only `ruff.toml:40-42` and `CONTRIBUTING.md:125-129` say the module refuses |
| `skills/writing-style/SKILL.md` *English prose rules* (read) | `seal/config.md` has no `Record language` row, so the records are English (read) |

## Scope

Each item is one issue's scope. Its *Done when* is the issue's, and each
issue's *Out* stays out. The words of each corrected sentence are the
crafter's. The claim each sentence makes is fixed here.

### S1 The `seal/` README's `config.md` entry (#1334)

The `config.md` entry of *Layout* in `templates/setup/seal-README.md:85-90`,
and the same lines in `seal/README.md`, which stay byte-identical. The entry
says what the file is: what the repository says about itself, one row per
item. It names `templates/setup/config.md` in the plugin as the document of
each item and of what an absent row means, as the comment at `seal/config.md:3-5` does.
It lists no items. It makes no claim about an absent row, including the
clause on `Mode`, which the template states. The `ROW_READERS` entry
`("templates", "setup", "seal-README.md")` in
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` goes,
because the file no longer names a language row (`## Removes`). The
*Grounding* census row names the class's other paragraphs, and each of them
holds.

### S2 The comment on who reads the language row (#1342)

`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:44-45`,
the comment above the second assert of
`test_the_skill_names_the_file_and_the_row`. It says that a session reads
the row by the skill's instruction, and that no script reads it. The assert
stays.

### S3 The eval cases' fixture records take their templates' forms (#1336)

In `evals/scripts/rule_cases.py`:

1. The three design titles at `:263`, `:357` and `:764` become
   `# Design: …`, the form `templates/records/sdd-design.md:1` gives.
2. The four scenario headings at `:270`, `:363`, `:466` and `:771` become
   `## User scenarios & acceptance *(mandatory)*`.
3. `SEALER_ROUND` at `:795` opens `# Review round 1: {item}`, the form
   `templates/records/sdd-round.md:1` gives.
4. `routing` at `:157` takes the work item id, and its title becomes
   `# Routing: {item}`. Its one caller at `:203` passes `item`.

The cases under `evals/behaviour/` are regenerated with
`evals/scripts/rule_cases.py --out` (its default directory is
`evals/behaviour/`). `RECORD_LINES` in
`tests/text/test_no_case_tells_the_agent_it_is_evaluated.py:30-39` takes the
heading with ` *(mandatory)*`, and its comment drops the clause that says
the heading lacks it. No paid eval runs. The pull request body says that the
paid runs #1107, #1178 and #1266 are waiting on will grade the cases this
changes. That is the orchestrator's text, and *Done when* asks for it.

### S4 The docstring of the module that holds the rules' homes (#1335)

The module docstring of
`tests/text/test_the_rules_claude_md_names_have_one_home.py`. It states
what the module's cases hold: `RULES`, `CARRIERS` and `LINKED` as
*Grounding* gives them. It names no `CLAUDE.md` row, because `CLAUDE.md`
keeps none. It offers no removed module as standing. The paragraph at
`:48-49` on `tests/test_the_ledger_rules_have_one_home.py` goes. Where the
docstring says what the module does not hold (`:41-46` today), it says it of
the carriers and not of a `CLAUDE.md` row. The module keeps its name, and
the first line says the rules are the ones `CLAUDE.md` once named.
`frame/plan.md` *Alternatives considered* A4 gives the grounds. The cases,
`RULES`, `LINKED` and `CARRIERS` stay.

### S5 Docstrings and comments under `tests/` that cite a removed module or case as standing (#1344)

Each statement below cites only what the tree holds at the commit that
changes it, or cites the old module or case at a commit where it stood, or
drops the citation. For each statement, the crafter picks the form when it
reads the sentence, and the phase record names the choice. A cited commit
is a tag (`vX.Y.Z:<path>`), or a commit on `main` or a release branch,
which `tests/text/test_a_cited_commit_outlives_the_squash.py` accepts.

1. `tests/behaviour/test_a_phase_hands_the_next_one_a_record.py:30-31`
2. `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:37-39`
3. The same module's `derivers` docstring, `:195-205`. The paragraph on the
   `SyntaxWarning` goes, together with the `warnings.catch_warnings` block at
   `:210-211` and `import warnings` at `:24` if nothing else in the module
   uses it. *Grounding* gives the probe that found no module raising the
   warning (`## Removes`)
4. `tests/behaviour/test_first_setup_asks_once.py:6-8`
5. `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py:38-40`, found
   by this frame's census, which joins a name split across lines
6. `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py:174-175`
7. `tests/behaviour/test_the_set_a_work_item_always_has.py:153-154`
8. `tests/github/test_close_issues_on_release.py:44-48`
9. `tests/hooks/test_question_gate.py:363-364`
10. `tests/text/test_review_axes.py:105-107`
11. `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py:15-17`

The twelfth statement the measure lists stands in S4's docstring. The two
census commands in *Grounding* are the method the pull request names for
*Done when*'s second sentence. Their sources are the removed modules and
the removed cases in git history, and every `tests/*.py` file at the
commit is searched. So the list is built from what produces the defect,
and is whole for names spelt as a module's basename or a case's name. A
citation that names a removed module by a description and not by its name
is outside what the census reads, and the hand-back says so.

### S6 The follow-up row on `chain_check.py --worktree`, and the table's blank line (#1337)

The first row of `seal/follow-up.md` *Schedulable items with nowhere else
to go* (`:42`). The row states its argument in its own words: a found
declaration makes the check demand round records, so reading the working
tree is stricter than reading HEAD. It does not send the reader to
`read_record`'s docstring. It cites the earlier argument as
`aa687d357:seal/specs/1788817289-local-mode-from-first-setup-to-the-gate/spec.md`
*The sharp question — where an untracked declaration lands*, or it drops
that citation where the argument already stands in the row. The question
it asks the owner stays the owner's. The blank line at `:45` goes, so the
four rows below it render as rows of the same table (#1346's line for
#1337).

### S7 The pull request template's gate comment (#1339)

The comment at `.github/PULL_REQUEST_TEMPLATE.md:29-34` keeps its first
sentence, which says why a gate change carries a higher bar. Its list of
four items is cut, and the comment cites `CONTRIBUTING.md` *What a change
to a gate must carry* alone, as the list of what this body answers. It
names no subset of the section's items (`## Removes`).

### S8 What refuses the syntax the floor cannot run (#1340)

The comment above `[per-file-target-version]` at `ruff.toml:40-42` and the
sentence at `CONTRIBUTING.md:125-129`. Each says that
`tests/hooks/test_launch.py` derives the set and holds it to the table, and
that `tests/censuses.py#floor_syntax` refuses what the floor cannot run.

### S9 Where the plugin's name is written (#1341)

The sentence at `docs/releasing/branch-and-release.md:204-206`. It names
`.claude-plugin/plugin.json` as the copy `plugin_directory_check.py` reads,
and it makes no claim that no other file spells the name. The literal
`.claude-plugin/plugin.json\` holds the one copy` in
`tests/text/test_the_release_tail_does_not_end_at_the_tag.py#test_the_fixed_name_sentence_names_the_file_that_holds_the_name`,
and the case's docstring, move to what the new sentence says (contract rule
19).

### S10 The count of runs that edited the clone (#1345)

Item 2 of *What it established* in
`docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.md:28` and
in its Korean edition at `:28-29`. Each counts four runs, as the Results
table (runs 1 to 4 in the marketplace clone) and *Method* ("the first
four") do.

### S11 The gate-misfire form's label (#1338)

`.github/ISSUE_TEMPLATE/gate-misfired.md:4` reads `labels: hooks-gates`. No
label is created (`frame/plan.md` *Judgments of the run*).

### Out of scope

- O1. Issue #1343. The orchestrator edits the tracker for it, with no
  commit.
- O2. Each issue's own *Out*: `templates/setup/config.md` and the README's
  other layout lines (#1334); `CLAUDE.md` and each home's text (#1335);
  every reader of records and the templates (#1336); the question in
  #1337's row and `chain_check.py`; `CONTRIBUTING.md` *What a contribution
  is asked for* (#1339); the tests' code (#1340); the manifests and the
  READMEs (#1341); the assert, and `hooks/lib/config.py`'s code (#1342), whose module docstring round 1's fix pass corrected to `templates/setup/config.md` as #1334's class; the
  sentences that name their moment, and any check (#1344); the Results
  table and *Method* (#1345); the form's fields (#1338).
- O3. `tests/e2e/teammate/test_teammate_flow.py:64` and the other test
  fixtures under `tests/` with an old record title (*Grounding*). The reader
  of each is a script that does not read the title, so the title states
  nothing of a form. Changing one of them would fix a sample of a class the
  measure judged held.
- O4. `CONTRIBUTING.md:43-48`, the bullet "A change to a gate carries a
  higher bar". It lists four items as a preview and says that the section
  below is the whole of it. #1339 puts it out of scope. It is not the form a
  pull request body is written from, which is what made the template's
  list drift. `README.md:367-372` previews three items and says the guide
  "holds the rest" in the same way.
- O5. The rule at `docs/layout/the-record-layout.md` *The root records*, "A
  `CLAUDE.md` row that points at a home carries three things". It states
  the shape of such a row should one exist, and #1335 puts `CLAUDE.md`'s
  side out.
- O6. Renaming `tests/text/test_the_rules_claude_md_names_have_one_home.py`
  (`frame/plan.md` *Alternatives considered* A4).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A1 The `seal/` README names no item (#1334) | Given both README copies after the build, when the `config.md` entry is read, then it lists no item, makes no claim about an absent row, and names `templates/setup/config.md`; the two files are identical | `cmp seal/README.md templates/setup/seal-README.md`; `sed -n '/├── config.md/,/├── parity.md/p' templates/setup/seal-README.md` names no backticked item; `bin/test tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/text/test_settle_reads_before_it_removes.py tests/text/test_the_records_can_be_carried_out_and_in.py tests/hooks/test_optin.py -q`; the *Grounding* census of `config.md`'s items, re-run, lists only paragraphs that hold |
| A2 The comment names the row's reader (#1342) | Given the comment, when it is read, then it names no script as the row's reader | `sed -n '40,48p' tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` |
| A3 Each fixture record opens with its template's title (#1336) | Given the regenerated cases, when they are searched, then no old form stands, and the cases are the generator's output byte for byte | `git grep -n -E 'Feature Specification\|— review round 1\|^# routing$' -- evals/` prints nothing; after the commit, `python3 evals/scripts/rule_cases.py && git status --porcelain evals/behaviour` prints nothing; `bin/test tests/evals/test_rule_cases.py tests/text/test_no_case_tells_the_agent_it_is_evaluated.py tests/behaviour/test_evals_layout.py tests/behaviour/test_the_sealer_guarantees.py tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py -q` |
| A4 The docstring states what the module holds (#1335) | Given the module docstring, when it is read, then it names no `CLAUDE.md` row and no removed module, and its cases are unchanged | `git grep -n 'test_the_ledger_rules_have_one_home\|keeps a row' tests/text/test_the_rules_claude_md_names_have_one_home.py` prints nothing; `git diff` touches the docstring alone; `bin/test tests/text/test_the_rules_claude_md_names_have_one_home.py -q` |
| A5 No docstring or comment offers a removed module or case as standing (#1344) | Given `tests/` after the build, when the two censuses of *Grounding* are re-run, then each line they list names the moment it describes, a fixture's name, or a module the tree holds | the two census commands, each line read; `git grep -n SyntaxWarning tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` prints nothing; `bin/test` on the modules S5 touches; `uvx ruff check` on the same files |
| A6 The follow-up row's coordinates hold (#1337) | Given the row, when each coordinate it cites is opened, then it holds what the row says; the table renders as one table | `git show aa687d357:seal/specs/1788817289-local-mode-from-first-setup-to-the-gate/spec.md \| grep -n 'The sharp question'`; `awk 'NR>=40 && NR<=50' seal/follow-up.md` shows no blank line inside the table; `bin/test tests/text/test_a_rider_reaches_its_file.py -q` |
| A7 The template names no subset (#1339) | Given the template's gate comment, when it is read, then it cites the section and lists none of its items | `sed -n '25,40p' .github/PULL_REQUEST_TEMPLATE.md`; `bin/test tests/behaviour/test_the_contributor_has_a_procedure.py tests/behaviour/test_docs_line_wrap.py -q` |
| A8 Each sentence names the code that refuses (#1340) | Given `ruff.toml` and `CONTRIBUTING.md`, when the sentences are read, then each names `floor_syntax` for the refusal | `git grep -n 'floor_syntax' -- ruff.toml CONTRIBUTING.md`; `bin/test tests/text/test_no_passage_is_pasted_into_a_second_file.py -q` |
| A9 The paragraph names no single copy the tree contradicts (#1341) | Given the paragraph and its case, when both are read, then the sentence names the copy the script reads and the case pins that sentence | `bin/test tests/text/test_the_release_tail_does_not_end_at_the_tag.py -q`; `git grep -n 'holds the one copy\|nothing else in the tree' -- ':!seal/threads'` prints nothing |
| A10 One count, the table's (#1345) | Given both editions, when item 2 is read, then each counts four runs | `sed -n '24,32p'` on each edition; `bin/test tests/behaviour/test_release_hygiene.py tests/behaviour/test_docs_line_wrap.py -q` |
| A11 The form's label is one the tracker lists (#1338) | Given the form, when its `labels:` value is looked up, then `gh label list` lists it | `gh label list --limit 200 --json name --jq '.[].name' \| grep -x "$(sed -n 's/^labels: //p' .github/ISSUE_TEMPLATE/gate-misfired.md)"` exits 0 |
| A12 No mechanism is added | Given the diff, when it is read, then it adds no test, check, hook, mark or rule, and `## Removes` names every removal | the proofer reads `## Removes` against the diff |

## Data & interfaces

`evals/scripts/rule_cases.py#routing` gains a first parameter, the work
item id. Its one caller in the module passes it (executed: `grep -n
'routing('`). No other module calls `routing` (executed: `grep -n routing
tests/evals/test_rule_cases.py` prints nothing). Nothing else changes
shape.

## Rule changes

- nothing
  why: This work item corrects statements of documents, templates, a config comment and test docstrings to the tree, and no rule says anything different afterwards. Its three `docs/` sentences, in `docs/releasing/branch-and-release.md`, the copy-in-force experiment and `docs/layout/one-root-by-lifetime.md` *What the repository decides for itself, and how it is read*, state facts of the tree and a count, so it edits them directly in its pull request under `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*. No section moves, so no unsettled design's operation is re-pointed.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the entry's list of three `config.md` items, and its clause on what no file and no row mean | `templates/setup/seal-README.md:85-90` and `seal/README.md:85-90`, *Layout* | `templates/setup/config.md` documents every item and what an absent row means, and the entry cites it |
| the `ROW_READERS` entry for `templates/setup/seal-README.md` | `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#ROW_READERS` | nowhere: the file no longer names a language row, so it is no longer a document that tells a session which row to read |
| the `SyntaxWarning` catch, its paragraph, and `import warnings` where nothing else uses it | `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#derivers` | nowhere: no tracked test module raises the warning under 3.12, 3.13 or 3.14 (*Grounding*), and the reason given names two modules the tree no longer holds. A warning a later module raises prints in pytest's summary, which is what the paragraph asked for ("rather than filtered globally, which would hide the next one") |
| the comment's list of four of the section's items | `.github/PULL_REQUEST_TEMPLATE.md:31-33` | `CONTRIBUTING.md` *What a change to a gate must carry*, which the comment cites |
| the docstring paragraph offering `tests/test_the_ledger_rules_have_one_home.py` as the shape | `tests/text/test_the_rules_claude_md_names_have_one_home.py:48-49` | nowhere: the module left at 5b1f6faea (#944), and the shape is the module's own cases |
| the blank line inside the table | `seal/follow-up.md:45`, *Schedulable items with nowhere else to go* | nowhere: it splits one table into a table and a paragraph |

A citation that S5 drops, rather than re-points or cites at a commit, is
the crafter's choice per sentence. The phase record names it, and the
proofer reads it against this table as a removal of a citation.

Framed 2026-11-04 by framer, before the build.
