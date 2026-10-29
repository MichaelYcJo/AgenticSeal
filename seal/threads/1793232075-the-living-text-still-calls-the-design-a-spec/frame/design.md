# Design: 1793232075-the-living-text-still-calls-the-design-a-spec

Issue #1110. The branch is `chore/1110-the-living-text-still-calls-the-design-a-spec`,
cut from `475653e7` on `release/v0.24.0`, and its head at framing is
`884b6ba8`, which adds only `routing.md`. Every coordinate below is read at
`884b6ba8` unless it names another commit.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *Repo rule: text an agent or a check reads has one reading*: "a defined term keeps its one meaning" | A work item's `frame/design.md` gets one name in living text, and the word `spec` stops naming it |
| `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*: "저장소가 정의한 용어는 정의한 뜻으로만 쓰고, 같은 것을 다른 말로 바꿔 부르지 않는다" | One thing, one word. *The term* below says the word and how a reader tells it apart from the `spec` that stays |
| `skills/writing-style/SKILL.md` *여럿이 가질 수 있는 것은 누구 것인지 밝힌다* | Every work item has a design, so the term is written with whose: a work item's design, its design, or the path `frame/design.md` |
| `v0.23.1:seal/process/0.23.0.md` row 2 (read with `git show`): "the frame's design is no longer called a spec" | The decision is made. This work carries it into the words, and the earlier frame `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/questions.md:12` filed it here without asking |
| `skills/implement/SKILL.md` *Document layout, two roots, three lifetimes*: the policy root "is the baseline, and a pull request does not edit it" | The seven `docs/` paragraphs that call the design a spec change through `## Rule changes` below. No file under `docs/` is edited |
| `templates/setup/config.md` *What no row governs*: the marker `<!-- specs/<work-item-id> -->` is read literally | The marker is checker vocabulary and stays. `.github/scripts/publish_release_note.py:292` writes it into every release note |
| `CLAUDE.md` *The rule a mechanism is kept against*: "a change that would be routed `no work item`, such as a formatter run, a dependency bump or an identifier renamed across files by `sed`, is outside that work" | Identifiers (`settle.py#SPECS`, `chain_check.py#SPEC_FILE`, `unverified_check.py#OVERVIEW`, local names) stay. Only text a person or an agent reads moves |
| The same section: "A check gates only a fact it reads; a noisy reading, or one guessed from words, is a report" | No census refuses the word `spec`, and none refuses a new agent name inside a longer word. `plan.md` *Alternatives considered* holds both |
| `evals/README.md`, the paragraph on `regrade`: "a change to a prompt, a scaffold or a `shape-` grader asks the agent something its runs never answered, and only a run measures that" | The eval scaffolds that write `# Feature Specification:` and `## Fed back into the spec` (`evals/scripts/rule_cases.py:128`, `:141`, `:266`, `:360`, `:530`, and the `scaffold.sh` files it generates) stay as they are |
| `tests/censuses.py#OLD_NAME_RECORDS` and `#RECORDED_CASE`: "The records of a moment, which keep the names they were written under" | Records under `seal/threads/`, the replayed and seeded eval cases and `evals/scripts/recurred_truths.json` keep their words |
| Issue #1110 *What this work decides*: "The divergence section of `templates/records/sdd-gaps.md`, *Where spec and implementation diverged*, is #1045's to remove" | `templates/records/sdd-gaps.md:11`, `:13`, `:15` and `skills/implement/SKILL.md:421` stay for #1045 (open, read with `gh issue view 1045`) |
| Contract rules 12, 14, 15 and 19 | The class is enumerated by command, not by example. A changed message is pinned in the same commit. A re-pointed case is seen red first. Every sentence and citation standing on an old wording moves in the commit that changes it |

## The term

**A work item's design** is its `frame/design.md`: the scope, the
grounding, the acceptance, the rule changes and the removals the framer
writes before the build. Living text names it "the design", "its design",
"a work item's design", or by the path. The plural is "designs", as in "the
released designs". In Korean it is 설계, the word `README.ko.md:38` already
uses.

**After this work, `spec` never names a work item's design.** Where the
word stays in living text it is one of these, and a reader tells each from
the design by its form:

| Where `spec` stays | What it names | How a reader tells it from the design |
|---|---|---|
| `docs/worktree-guard-spec.md`, and "Update spec and code together" at the top of four `docs/` files | a policy document, under `docs/` | It is a file under the policy root, or the document speaking of itself. A design lives only at `seal/threads/<id>/frame/design.md` |
| `Reference specs`, and a project's own `specs/` | a reference root: a project's specifications kept before the plugin | It is a config row's key or a directory named `specs`. Neither is under `seal/` |
| `<!-- specs/<work-item-id> -->` | a release-note marker | It is a marker a checker reads. `templates/setup/config.md` *What no row governs* lists it |
| "spec-driven", and the S in SDD | the methodology's name | It qualifies a method, never a document |
| a commit-qualified path such as `0ed5dd3b:seal/specs/<id>/spec.md` | history | It carries a commit, and `git show` opens it as written |

"Design" keeps its ordinary meaning elsewhere, as in "by design", "the
Design Gate" and `CLAUDE.md` *The goal a design is chosen against*. Those
are never written with a work item as owner and never as the path, which is
how the term differs from them.

The closing memo keeps its name: `gaps.md`, "the closing memo"
(`skills/implement/SKILL.md` *3. The SDD file set*). "Overview", its name
before 0.23.0, goes from living text the same way.

## Scope

**In.** Living text is the prose of every tracked file outside
`seal/threads/`, `evals/` and `tests/`: Markdown, JSON, and the docstrings,
comments and printed strings of shipped code under `hooks/`, `skills/` and
`.github/`. In it, this work rewrites:

1. Every `spec` or `specs` that names a work item's design, listed by file
   in *The class, enumerated* below.
2. Every `overview` that names the closing memo.
3. The two places that still name a work item's directory by its 0.22.x
   name `specs`: the mirror path in `skills/commit-pr-convention/SKILL.md:210`,
   and the prose of `skills/verify/scripts/unverified_check.py:60`, `:1346`,
   `:1406`, `:1493` and `:1495`.
4. The titles of `templates/records/sdd-design.md` and
   `templates/records/sdd-gaps.md`, and the heading `## Fed back into the
   spec` of `sdd-gaps.md`.
5. The heading `### 1. Read the spec before the code` of
   `skills/implement/SKILL.md`, which becomes `### 1. Read the documents
   that outrank the code first`, with each of its twelve citations.
6. The name of `code-review`'s first stage, "spec compliance", which
   becomes "compliance": the code against the documents that outrank it,
   the `docs/` policies first and then the work item's SDD set.
7. Each test string that pins a sentence this work rewrites, in the commit
   that rewrites the sentence.
8. Two cases blinded by the 0.23.0 move, which glob `seal/specs/` where no
   file stands and so read nothing:
   `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:244`
   and `:251`, and `tests/behaviour/test_the_sealer_guarantees.py:141`.
   Each reads `seal/threads/` after this work.
9. The `docs/` paragraphs, through `## Rule changes`.

**Out.**

- **Identifiers.** `settle.py#SPECS`, `rule_changes.py`'s `specs` parameter,
  `chain_check.py#SPEC_FILE` and its `spec` local,
  `unverified_check.py#OVERVIEW` and `#overviews`, `seal_stamp.py:1272-1274`.
  `CLAUDE.md` *The rule a mechanism is kept against* names a rename of
  identifiers across files as `no work item` work.
- **The prose of `tests/`.** The issue's table counts no `tests/` path.
  Test docstrings, comments and assertion messages that say `spec` or
  `overview` stay; command C6 below counts them for whoever takes them up.
  A test string changes here only where it pins a sentence this work
  rewrites (item 7) or reads the old directory (item 8).
- **`evals/`.** A scaffold is a measured input (Grounding, `evals/README.md`).
- **#1045's divergence section**: `templates/records/sdd-gaps.md:11`, `:13`,
  `:15`, and `skills/implement/SKILL.md:421`.
- **The frozen file** `hooks/lib/cmdline_base.py`: `tests/censuses.py#KEPT_FILES`
  says no line of it can change. Its `:14`, `:1225`, `:1693`, `:1773` and
  `:2014` stay.
- **A census for the word, and one for a new name inside a longer word.**
  `plan.md` *Alternatives considered* gives the grounds.
- **#1020's files before #1020 merges.** `CLAUDE.md`,
  `skills/agent-contract/SKILL.md`, `skills/code-review/` and
  `agents/proofer.md` belong to the parallel work item #1020, on branch
  `fix/1020-one-kind-of-finding-recurs-across-review-rounds`. Their
  occurrences are listed below and rewritten in the last phase, after the
  orchestrator merges `release/v0.24.0` into this branch with #1020 in it.

## The class, enumerated

The commands, run from the worktree's root. A later round re-runs them and
reads each hit against the two tables below.

- **C1, the word in living text:**
  `git grep -n -i -w -E 'specs?' -- ':!*.ko.md' ':!seal/threads/' ':!evals/' ':!tests/' ':!.test_durations' | grep -v -E 'spec_from_file_location|module_from_spec|spec\.loader|spec is None|importlib'`
  gives 255 lines in 53 files at `884b6ba8` (executed).
- **C2, the Korean editions:** `git grep -n -i -E 'spec|스펙' -- '*.ko.md'`.
- **C3, the memo's old name:**
  `git grep -n -i -w -E 'overviews?' -- ':!seal/threads/' ':!evals/' ':!tests/' ':!.test_durations'`.
- **C4, the old directory in path parts:**
  `git grep -n -E '"seal", "specs"|/ "specs"|<root>/specs/' -- ':!seal/threads/' ':!evals/behaviour/'`.
- **C5, a substitution inside a word**, the class #1109 fixed: every word
  that holds `design` on an added line, against the branch's base:
  `git diff 475653e7 HEAD -U0 -- ':!seal/threads/' | grep '^+' | grep -o -i -E '[a-z]*design[a-z]*' | sort -u`.
  Only `design`, `designs`, `designed`, `designing` and `redesign` may come
  back, in any case. A word such as `designific` or `indesignt` is a
  substitution that reached inside `specific` or `inspect`.
- **C6, the prose of `tests/`, counted and left:**
  `git grep -c -i -w -E 'specs?|overviews?' -- tests/`.

### Living occurrences this work rewrites

Line numbers are at `884b6ba8`. Phase 3's lines are re-read at the merge,
because #1020 may move them.

| File | Lines | Reads now | Phase |
|---|---|---|---|
| `templates/records/sdd-design.md` | 1 | `# Feature Specification: <work item>`, which becomes `# Design: <work item>` | 1 |
| `templates/records/sdd-gaps.md` | 1, 27 | `# Overview: <work item>`, which becomes `# Closing memo: <work item>`; `## Fed back into the spec`, which becomes `## Fed back into the design` | 1 |
| `templates/records/sdd-guarantee.md` | 20 | the party "the spec" | 1 |
| `templates/setup/pact.md` | 37 | "framed by this repository's own spec" | 1 |
| `templates/setup/seal-README.md` and `seal/README.md` | 7 each | "released specs' `## Rule changes`"; the two files are identical (executed `diff`), and stay so | 1 |
| `agents/framer.md` | 55, 151 | "unsettled specs'", and the rule lead *A spec states its rule changes* with its citation at :55 | 1 |
| `agents/tracer.md` | 31, 36, 57 | "the spec's Grounding", "the spec had wrong", the rule lead *Start from the spec's coordinates* | 1 |
| `agents/sealer.md` | 84 | "The spec (scope, `Removes`)" | 1 |
| `skills/implement/SKILL.md` | 17, 75 (twice), 146, 160, 172, 231, 426; 215 and 454 for `overview` | "written specs", "A spec states", "released specs", "unsettled specs'", "A spec that contradicts policy", "the spec's `## Rule changes`", "the spec chain", "the spec's scenario table", "fed back into the spec"; "the overview's Not done", "the overview's diff" | 1 |
| `skills/implement/orchestration.md` | 11, 468, 599 | "the spec-first procedure", "write spec, plan and questions", "that repository's own spec" | 1 |
| `skills/settle/SKILL.md` | 17, 18, 19, 20, 31, 32, 47, 69, 78, 81, 152, 154, 160, 161, 164, 184, 223, 279, 280, 355 | every `spec` there names a design | 1 |
| `skills/legacy-parity/SKILL.md` | 12, 67, 87 (twice) | the title "the original is the fallback spec", "A spec's Grounding", "the spec's coordinates, and not only the written spec" | 1 |
| `README.md` | 116, 268 (twice), 445 | "in its spec", "the released specs", "the specs to read whole", "the spec chain" | 1 |
| `README.ko.md` | 112, 261 (twice) | "spec 에 적으며", "릴리스된 spec 들", "통째로 읽어야 할 spec" | 1 |
| `skills/settle/scripts/settle.py` | docstrings 2, 4, 5, 22, 27, 29, 32, 35, 36, 38, 494, 498, 499, 501, 566, 699; strings 100, 363, 377, 868 | the module's account of released specs; the purpose sentence, the dry run's `GROUPS_HEADING` and `WHOLE_HEADING`, and the argparse description | 2 |
| `skills/settle/scripts/rule_changes.py` | 2, 10, 18, 45, 69, 86, 110, 225, 309, 340, 374 | docstrings and comments calling the design a spec | 2 |
| `skills/verify/scripts/unverified_check.py` | `spec` for the design: 140, 172, 632, 1255, 1276. The directory `specs`: 60, 1346, 1406, 1493, 1495. `overview`: 2, 59, 291, 834, 930, 1038, 1237, 1322, 1325, 1480, and the printed tally at 1692 | docstrings, comments, and the summary line a person reads, which counts "overviews" | 2 |
| `skills/implement/scripts/seal.py` | 94, 134, 1053 | "its directory `specs/<id>/`", the `settle` help line "show the released specs", "the case the spec and both READMEs describe" | 2 |
| `skills/commit-pr-convention/SKILL.md` | 210 | the mirror path `<root>/specs/<work-item-id>/pr.ko.md`, which becomes `<root>/threads/<work-item-id>/pr.ko.md` | 2 |
| `CLAUDE.md` | 10 | the heading citation *1. Read the spec before the code* | 3 |
| `skills/agent-contract/SKILL.md` | none | C1 finds no line (executed, at `884b6ba8` and at #1020's head `1d84fefe`) | 3, nothing to do |
| `agents/proofer.md` | 4 | "spec compliance first" | 3 |
| `skills/code-review/SKILL.md` | 4, 9, 13, 22 (twice), 31, 50, 53, 115 | the stage name, the title "spec first, then quality", "the written spec", "fed back into the spec", "what the spec intentionally does *not* filter", "the spec's state machine", "a spec violation" | 3 |
| `skills/code-review/orchestration.md` | 393 | "Spec citations, because clause numbers move" | 3 |
| `skills/code-review/scripts/chain_check.py` | 1604 (refusal text), 1612 (docstring), 2268 (comment) | "cannot group this spec", "git carries no spec", "the diff's specs are read too" | 3 |
| `skills/implement/SKILL.md` | 139 | the heading itself | 3 |
| The heading's other citations | `CONTRIBUTING.md:388`, `agents/framer.md:51`, `hooks/mode-gate.py:38`, `skills/implement/orchestration.md:304`, `tests/hooks/test_question_gate.py:437`, `tests/text/test_the_rules_claude_md_names_have_one_home.py:83`, `tests/hooks/test_mode_gate.py:52` and `:94`, `tests/behaviour/test_chain_hooks_hardening.py:596` | every citation of the heading, found with `git grep -n -i 'Read the spec'` (executed) | 3 |
| The stage name's other copies | `README.md:38`, `:40`, `:177`; `README.ko.md:38`, `:40`, `:171` ("스펙 준수"); `hooks/review-skill-gate.py:69`; `tests/hooks/test_review_skill_gate.py:5` | "spec compliance" as the proofer's first stage | 3 |

Pins that move with their sentence, each in the phase of its sentence:
`tests/text/test_a_moved_rule_leaves_its_definition.py:555` (the tracer's
rule lead, phase 1), `tests/behaviour/test_unverified_rows_close.py:207`
("the proofer reads the overview's diff", phase 1),
`tests/skills/test_settle.py:1532` (the `RULES` purpose sentence, phase 2),
`tests/skills/test_unverified_check.py:2107` (the tally, phase 2), and
`tests/skills/test_chain_check.py:1691` (the refusal, phase 3).
`test_settle.py` reads `GROUPS_HEADING` and `WHOLE_HEADING` through the
module (`:461`, `:507`, `:781`, `:1495`), so those follow the constants.

### Occurrences kept, and why

| Kind | Coordinates | Why it stays |
|---|---|---|
| A policy document's name, or a policy document speaking of itself | `docs/worktree-guard-spec.md` and its citations (`README.md`, `README.ko.md:160`, `hooks/worktree-guard.py` 11 lines, `hooks/worktree_consent.py:306`, `:537`, `hooks/lib/tokens.py:6`); "Update spec and code together" at `docs/worktree-guard-spec.md:5`, `docs/the-routing-check.md:6`, `docs/the-session-hooks.md:5`, `docs/the-review-and-parity-arms.md:7` | The other meaning, a policy document. *The term* says how a reader tells it from the design |
| A reference root and its config row | `templates/setup/config.md:74`, `:367-384`; `skills/config/SKILL.md:52`, `:147`, `:149`; `skills/implement/SKILL.md:79`, `:80`; `skills/settle/SKILL.md:245`, `:246`; `agents/crafter.md:35`; `agents/framer.md:73`; `agents/proofer.md:89`; `docs/one-root-by-lifetime.md:23-26` and its `.ko.md` `:23-26`; `skills/implement/orchestration.md:115`; `hooks/lib/config.py` 11 lines; `skills/verify/scripts/unverified_check.py:77`, `:926`, `:1022`, `:1075` | A project's own specifications. `Reference specs` is `hooks/lib/config.py#REFERENCE_ROW`, a key a checker reads |
| Checker vocabulary | `<!-- specs/<work-item-id> -->` at `templates/setup/config.md:143`, `skills/implement/SKILL.md:62`, `skills/implement/orchestration.md:584`, `.github/scripts/publish_release_note.py:292` | `templates/setup/config.md` *What no row governs*. It moves only with its writer and every release note that carries it |
| The methodology's name | `.claude-plugin/plugin.json:14`, `skills/implement/SKILL.md:4`, `:15`, `CONTRIBUTING.md:55` | "spec-driven" names a method, as SDD does in `templates/records/sdd-*.md` and *3. The SDD file set*; it calls no document a spec |
| History | `.github/workflows/test.yml:85`, `:90`, `:135`; `skills/writing-style/SKILL.md:285`; `seal/follow-up.md:43`; `README.md:381-407` and `README.ko.md:374-398` (the 0.3.x move by hand); `hooks/root-migrate.py` 9 lines; `skills/settle/scripts/rule_changes.py:273` | A commit-qualified path, or the old layout the migration and the by-hand move read. `tests/censuses.py#KEPT_FILES` and `#HISTORY_PATH` keep them |
| The frozen file | `hooks/lib/cmdline_base.py:14`, `:1225`, `:1693`, `:1773`, `:2014` | `tests/censuses.py#KEPT_FILES`: no line of it can change |
| Another meaning in code | `skills/verify/scripts/session_cost.py:894` (a Python format spec), `skills/verify/scripts/payload_meter.py:106` (an `importlib` module spec) | Not the design. C1's filter drops the other `importlib` lines |
| Identifiers | `settle.py#SPECS` and its uses, `rule_changes.py`'s `specs` parameter (`:276`, `:287`, `:299`, `:333`, `:334`, `:339`, `:343`, `:364`), `chain_check.py:1570`, `:1577`, `seal_stamp.py:1272-1274`, `unverified_check.py#OVERVIEW` and `#overviews`, `settle.py:812`, `:852` | Out of scope (Grounding, `CLAUDE.md`) |
| #1045's | `templates/records/sdd-gaps.md:11`, `:13`, `:15`; `skills/implement/SKILL.md:421` | The issue leaves these words to #1045 |
| Records, eval cases, tests' own prose | everything under `seal/threads/` and `evals/`; C6's count under `tests/` | Grounding and *Scope* |

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given this branch after phase 3, when C1, C2 and C3 run, then every line they print is in *Occurrences kept, and why*, and none names a work item's design or the closing memo | Re-run C1, C2, C3 and read each hit against the kept table. The proofer re-runs them at review |
| S2 | Given a framer copying `templates/records/sdd-design.md`, when it opens the file, then the title reads `# Design: <work item>`; a builder copying `templates/records/sdd-gaps.md` reads `# Closing memo: <work item>` and `## Fed back into the design` | `head -1` of each template. `diff templates/setup/seal-README.md seal/README.md` prints nothing |
| S3 | Given a settling session, when it runs `seal settle`, then the dry run's two headings, `settle.py#GROUPS_HEADING` and `#WHOLE_HEADING`, say "released designs", and the line `seal --help` prints for `settle` (`seal.py#TOOLS`) says the same | `bin/test tests/skills/test_settle.py`, and the pin at `:1532` rewritten to the new purpose sentence. Seen red with the old sentence restored in `settle.py`, as rule 15 asks |
| S4 | Given a person running `seal unverified`, when it prints its summary, then the line counts closing memos, not overviews | `bin/test tests/skills/test_unverified_check.py`; the pin at `:2107` moves with the text and is seen red against the old text |
| S5 | Given the two blinded cases, when they run, then each reads `seal/threads/`: the guarantee case finds every `guarantee.md` there, 18 at `884b6ba8` (executed `ls`), and the mirror case lists `seal/threads/*/pr.*.md`, none at `884b6ba8` (executed `ls`) | `bin/test` over both modules. Seen red by adding a second `Verdict: sealed` line to one thread's `guarantee.md` in the working tree and removing it before the commit; the phase record says which file |
| S6 | Given a session opening `skills/implement/SKILL.md`, when it looks for step 1, then the heading reads `### 1. Read the documents that outrank the code first`, and every citation of it names that text | `git grep -n -i 'Read the spec'` prints nothing outside `seal/threads/`. `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/hooks/test_question_gate.py tests/text/test_the_rules_claude_md_names_have_one_home.py tests/hooks/test_mode_gate.py` |
| S7 | Given a person whose session opens a skill named `code-review`, when the review-skill gate asks which review to run, then the AgenticSeal option reads "compliance first, then quality", and `code-review`'s first stage, `agents/proofer.md` and both READMEs use the same name | `bin/test tests/hooks/test_review_skill_gate.py`. `git grep -n -i 'spec compliance\|spec-compliance\|스펙 준수'` prints nothing outside `seal/threads/` and `evals/` |
| S8 | Given the diff against `475653e7`, when C5 runs, then it prints only `design`, `designs`, `designed`, `designing` or `redesign`, in any case | C5, run at each phase's close and once more at review |
| S9 | Given the pull request, when `chain-check` parses this design's `## Rule changes`, then it parses, and each `from` is found in its section at the base | `chain-check` at the pull request (`docs/the-review-record.md` *What the check reads at the pull request*). The `from` values were copied from the files at `884b6ba8` |

## Data & interfaces

No schema, file name, path, marker or checker field changes. What a person
sees changes in five strings: `settle.py#GROUPS_HEADING`,
`settle.py#WHOLE_HEADING`, the `settle` line of `seal.py`'s command table
(`:134`) with `settle.py`'s argparse description (`:868`), the tally line of
`unverified_check.py:1692`, and the refusal at `chain_check.py:1604`. One
prompt changes: the second option of `hooks/review-skill-gate.py#REASON`.
Two template titles and one template heading change; no checker reads them
(executed `git grep -n 'Feature Specification\|# Overview\|Fed back into the spec'`,
whose only readers are eval scaffolds and test fixtures that build their
own text).

## Rule changes

- change
  file: docs/README.md
  section: docs/
  from: A `docs/` document outranks the work items' specs, and a spec that
    finds one wrong states the correction in its `## Rule changes`
  to: A `docs/` document outranks the work items' designs, and a design
    that finds one wrong states the correction in its `## Rule changes`
- change
  file: docs/one-root-by-lifetime.md
  section: The root and its lifetimes
  from: lives until the settle writes its spec's sections and removes it;
  to: lives until the settle writes its design's sections and removes it;
- change
  file: docs/one-root-by-lifetime.ko.md
  section: 루트와 그 안의 수명
  from: settle 이 그 spec 의 절을 쓰고
  to: settle 이 그 설계의 절을 쓰고
- change
  file: docs/release-checklist.md
  section: 2b. Settle what earlier releases left behind
  from: The first prints each group of released specs whose rule changes
    name one section, in merge order,
  to: The first prints each group of released designs whose rule changes
    name one section, in merge order,
- change
  file: docs/the-pact.md
  section: The pact anchor
  from: A signer writes the anchor in a spec's Grounding, recording what
    the work was built against.
  to: A signer writes the anchor in its work item's design, under
    Grounding, recording what the work was built against.
- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: **The settle writes each section as the latest decision among the
    released specs states it, checked against the code.** The specs whose
    rule changes name one section, or a section holding it, are one group,
    and merge order sorts it, so a group is that rule's history. Within a
    group the latest spec that states a rule decides it,
  to: **The settle writes each section as the latest decision the released
    designs state for it, checked against the code.** The designs whose
    rule changes name one section, or a section holding it, are one group,
    and merge order sorts it, so a group is that rule's history. Within a
    group the latest design that states a rule decides it,
- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: an operation's `from` locates the text its spec's framer read, and
    a `from` that no longer matches is history, not a refusal. The rest of
    the document stays as it was, and no marker is written. `settle` groups
    the specs, shows each group's history
  to: an operation's `from` locates the text its design's framer read, and
    a `from` that no longer matches is history, not a refusal. The rest of
    the document stays as it was, and no marker is written. `settle` groups
    the designs, shows each group's history
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: `settle` groups the released specs by the sections their rule
    changes name, and a spec whose section does not parse joins no group,
    so a section first read there is a rule change the settle can place
    only by reading the whole spec, with no pull request left to fix it in.
  to: `settle` groups the released designs by the sections their rule
    changes name, and a design whose section does not parse joins no group,
    so a section first read there is a rule change the settle can place
    only by reading the whole design, with no pull request left to fix it
    in.
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: is left alone here, and the settle reads such a spec whole.
  to: is left alone here, and the settle reads such a design whole.

## Removes

- nothing
  why: Every line the diff takes out is rewritten in place to the same fact under the new word, or, for the two blinded cases, to the directory that holds the files. No sentence, unit, case or record of the base goes.

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-29 by framer, before the build.
