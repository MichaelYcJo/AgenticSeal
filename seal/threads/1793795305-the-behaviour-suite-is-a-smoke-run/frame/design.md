# Design: the behaviour suite is a smoke run (#1254)

Issue #1254, in milestone `release: 0.32.0`. The framer read its body as
the spawn folded it, and `gh issue view 1254 --json comments` prints no
comment (executed, 2026-11-04). Every coordinate below is read at
`bac426446`, the branch's HEAD, which descends from `479a79d15`
(`origin/main`) by the routing commit alone (executed: `git log --oneline -1`).

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `routing.md` (read) | Planning `framer`, Implementation `crafter`, through the review chain, open the pull request, Automation `yes`. Nobody is asked anything after routing, so every open point below is decided here or left to the work |
| The orchestrator's spawn (the orchestrator's finding; the framer opened the coordinates it names) | #1255 and #1256 are built after this work item, on their own branches, and own `tests/censuses.py`, `CONTRIBUTING.md` *House rules*, the entry-point `__main__` files, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `docs/` *The dependency rule*. This work item edits none of them. It is the release's first work item, so it carries the version move (plan *Operational impact*) |
| The measure, `seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-1.md` at `569780eff`, *The decisions* row C8, *Command C8* and *Instances C8* (executed: `git show 569780eff:<path>`) | 28 compare records over 32 sides, 544.17 USD and 24.4 hours. 15 read `fail`. The one fail later confirmed as a defect was the rewritten warden leaving a finding's `verdict:` line out of its records, and the shape graders of rule 3 read it (instances 4 and 5). One fail was acted on for bytes, which a byte count answers with no run (instance 12). The fails on rule 5 alone, or on rules 1 and 2, were carried, recorded as noise, or diagnosed as variation, and shipped (instances 2, 6, 7, 13, 14 and 15). The other fails that name rule 3 are a definition the contract contradicted (instance 3) and a model comparison (instance 8), and instances 9 to 11 regrade earlier sides with no new run. The decision is `narrow`: the shape and reach graders stay as a smoke run, and the rest judges nothing. Removal was weighed as an equal there and rejected (plan *Alternatives* row A1 here) |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "A mechanism stays only while its record of what it caught outweighs what it costs." Rules 1, 2, 4 and 5 of the verdict caught nothing on the measure's record, so they leave the verdict, and their constants and their cases leave with them. "A change rewrites the text it amends in place, and in the same commit removes what stood on the old fact." That is why *Scope* S3 to S5 exist |
| `skills/core/SKILL.md` *The first value* (read) | "Whether two things mean the same or give the same result is the judgment the workflow delegates", and the proofer gates it. A pass of the smoke run therefore claims nothing about meaning. The measure's row C8 says so in its grounds: "A pass does not judge a shift in meaning, which the proofer's reading of the diff judges" |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | This work item's subject is the code: a verdict, its statement in `evals/README.md`, and sentences that cite it. So the one sentence of `docs/` it corrects goes through `## Rule changes` and is not edited in the pull request |
| `docs/README.md` (read) | The index names `docs/running/measuring-a-run.md`, the one `file:` of `## Rule changes` |
| `docs/running/measuring-a-run.md` *What a measurement must survive, and what it must not invent* (read, lines 78 to 98) | The paragraph opening "A band flags a reading for judgment" says "the pass rules of `evals/README.md` *The behaviour suite* decide whether one preload rewrite proved itself not worse". It also calls those rules "a margin a claim fixes before its run". After S2 the verdict holds no margin, so both halves change |
| Unsettled `## Rule changes` (executed: `awk` over the `## Rule changes` section of every `frame/design.md` under `seal/threads/`, the `file:` and `section:` lines) | Two designs hold pending operations: 1793726048 on `docs/running/the-run.md` *The run*, and 1793732301 on `docs/layout/the-record-layout.md` *The root records*. Neither names `docs/running/measuring-a-run.md`, so nothing pending stands on the sentence this work changes |
| `seal/follow-up.md` (read) | No row names the behaviour suite, its verdict or `evals/`. No item waits on this work |
| `seal/parity.md` (executed: `ls` finds none) | No migration config, so no original ranks between the ticket and the code |
| `docs/layout/the-record-layout.md` *A change to the way of working writes its process row in its own fragment* (read), the latest release's body (executed: `gh release view --json body` names `v0.31.2` and holds no `### Process changes` heading) and the fragments under `seal/threads/` (executed: `grep` over every `changelog.md` for `eval`, `suite` and `preload`) | The diff touches none of `skills/core/SKILL.md`, `CLAUDE.md`, `agents/*.md`, `skills/*/orchestration.md` or `skills/implement/bootstrap.md`, so the fragment carries no `### Process changes` table. No process row on record touches the suite |
| `docs/releasing/branch-and-release.md` *Cutting a release* (read) and `.claude-plugin/plugin.json` (executed: `grep version` prints `0.31.2`) | "The orchestrator moves it in the commit that adds the changelog fragment of the release's first work item." This work item moves it to `0.32.0` |
| `evals/scripts/noninferiority.py#verdict`, lines 776 to 912 (read) | Rule 3 is three clauses. The pooled passes of every shape and reach grader both sides ran are no fewer on the new side. No such grader fails every new run where the baseline passed it at least once. A grader the baseline lacks passes every new run. Before those, four checks give `no result`: a side cut short, a case the baseline ran and the new side did not, a case run a different number of times, and a side whose tokens, tool calls or preload bytes are unknown or whose tool calls are none |
| `evals/scripts/noninferiority.py#compare`, lines 1173 to 1206 (read) | `compare` reads the baseline as a side file that `run` wrote (`--old`). It refuses a side that records no suite, and two sides whose suite trees differ. It does not ask when or at which tree the baseline was run. So the issue's "a recorded baseline" is a side already run and kept, which `compare` reads today, and S1 states it with nothing built for it |
| `evals/scripts/noninferiority.py#cheaper_model` (read) | `model` returns `opus` on any `no result` of `verdict`, and otherwise reads every grader and the spend itself. A grader counts as lost where `new passed × old runs < old passed × new runs`. A grader the baseline lacks has 0 old runs, so it is never lost. So after S2 the narrowed verdict can still fail on a record `model` reads past, which is what the case of S4's `model_numbers` needs |
| `tests/evals/test_noninferiority.py`, lines 1478 to 1690 and 1946 to 2021 (read) | `VERDICTS` holds a row for each rule and each `no result`. `Test_verdict` asserts them, asserts rule 3's lines in order, and asserts one line for each of rules 1, 2, 4 and 5. `test_passes_a_figure_exactly_at_a_margin_whose_float_falls_short` monkeypatches `TOKEN_MARGIN`. `Test_cheaper_model` asserts that `model_numbers()` fails its own verdict on rule 4. `Test_render` asserts the title `# proofer — phase 3 non-inferiority` |
| The `check:` lines naming a case of the suite (executed: `git grep -n -E '^check:.*evals/behaviour/' -- ':!seal/'`, fixtures of `tests/github/test_rules.py` left out) | 13 lines in 7 files: `agents/framer.md` 1, `agents/proofer.md` 1, `agents/sealer.md` 4, `docs/running/the-agent-set.md` 1, `skills/agent-contract/SKILL.md` 3, `skills/code-review/SKILL.md` 2, `skills/verify/SKILL.md` 1. This is the measure's figure, unchanged at HEAD. The cases stay, as the issue's *What stays* says |
| The sentences that call the suite the proof of a rewrite, found by three commands (executed at HEAD; plan *Technical context* gives each) | The citation census: every file outside `seal/`, `.test_durations` and `evals/behaviour/` that names `evals/README`, `noninferiority`, `evals/behaviour` or the behaviour suite or evals, 32 files, each hit that is not a `check:` line read. The phrase sample: `non[-_ ]?inferior`, `not worse`, `no worse`, `proved on`, `proved itself`, `five pass`, `pass rules`, the two margins, `(rule N)`, and `증명하는`. The file listing: `git ls-files '*non_inferior*'`. Together they list `evals/README.md` *The behaviour suite*, the docstrings and the record title of `evals/scripts/noninferiority.py`, `tests/evals/test_noninferiority.py`, `README.md:357`, `README.ko.md:362-364`, `docs/running/measuring-a-run.md:83-87`, and the module name `tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py` with the four docstrings that cite it. Every other hit names the suite and claims nothing about a rewrite |
| `tests/behaviour/test_a_cited_section_stands_in_its_file.py:689-695` (read) | Its docstring gives "the behaviour suite's pass rules" as an example of a numbered list outside the contract. The file is #1255's. S1 keeps the pass rules numbered, so that example stays true and the file is not touched |
| This design's `## Rule changes` (executed: `rule_changes.py#parse(text, "docs")` from a `git clone --no-local` of `bac426446` under the scratchpad, over this file; and the `from` text, whitespace collapsed, searched in `docs/running/measuring-a-run.md` at the same commit) | The reader returns one `change` on `docs/running/measuring-a-run.md`, section *What a measurement must survive, and what it must not invent*, with no error and nothing unread. The `from` text stands in the section |
| `.test_durations` (executed: `python3 -I` sums the file) | The module S5 renames has one entry, 0.012 of 1614.4 seconds. That is far below the one second in twenty that `test_the_durations_file_prices_the_suite` allows for stale entries (`CONTRIBUTING.md`, read), so the file is not edited by hand |

## Scope

In:

1. **S1 `evals/README.md` *The behaviour suite* states the smoke run.** The
   lead replaces the sentence "A rewrite of an agent's preload is proved not
   worse by running this suite on the old tree and on the new one, judged on
   outcome first and then on cost, each against the baseline and none
   against an absolute." It states that the suite is a smoke run for gross
   breakage of an agent's output: `compare` reads the new side's shape and
   reach graders against a recorded baseline side. It states that a pass
   claims nothing about whether a rewrite is worse or means the same, which
   the proofer's reading of the diff judges. The pass rules become three
   numbered rules, one for each clause of today's rule 3, in today's order.
   Rules 1, 2, 4 and 5 leave the list. The paragraph after the list states
   that recall, the false-finding rate, the tokens read and the tokens per
   tool call are written in the record and judge nothing, beside tokens per
   true find, spend, wall seconds and the preload's bytes. It states that the
   preload's bytes are read with no run: `.github/scripts/release_report.py`
   prints each agent's preload bytes against the last tag on every pull
   request into `main`. Its list of what gives `no result` loses the run
   whose `modelUsage` is missing or short of a count and the trace that
   cannot be read or holds no tool call. The section's last paragraph, which
   said a row count spelt otherwise lets a record edited by hand pass
   `check`, says what `parse_record` reads the count as, which judges
   nothing. The sentence "Nothing in the tree makes a later edit owe a run"
   stays.
2. **S2 `evals/scripts/noninferiority.py#verdict` judges what S1 states.** It
   gives `no result` for a side cut short, a case the baseline ran and the
   new side did not, and a case run a different number of times, as today.
   It gives `fail` on S1's three rules, each reason line ending in its new
   number, `(rule 1)`, `(rule 2)` or `(rule 3)`. It reads no truth grader,
   no row count, no token, call or byte figure, and gives no `no result` for
   an unknown one. `FALSE_MARGIN` and `TOKEN_MARGIN` go.
3. **S3 the script's other text that states the five rules is rewritten.**
   This covers the module docstring's paragraph on the five pass rules, the
   docstrings of `verdict`, `tool_calls` (its rule 5 paragraph) and
   `cost_rows` ("whose figure rule 5 reads"), the comments inside `verdict`
   on rule 5, and the comment above `TOKEN_MARGIN`. The record `render`
   writes opens `# <agent> — phase <N> smoke run` in place of
   `non-inferiority`, because that title is what a person reads above
   `Verdict: pass`. This is rule 14 of the contract: the changed title is
   pinned by `Test_render` in the same commit.
4. **S4 `tests/evals/test_noninferiority.py` pins S2 and S3, each changed
   case seen red first.** Each of the four figures rules 1, 2, 4 and 5
   judged keeps one `VERDICTS` row, which expects `pass`, and the
   `no result` rows for unknown tokens, unknown tool calls, no tool calls
   and unknown preload bytes become rows that expect `pass`. The other rows
   of those rules go, two that failed rule 1 and eight that pinned a margin
   or a noise boundary S2 removes (phase record D1). Each changed row is
   shown red against the verdict before S2. The cases that failed a record
   through rule 1, 2 or 5, in `Test_render`, `Test_read_record`,
   `Test_check_record`, `Test_check` and `Test_model`, fail it through S1's
   rule 1, and the two row-count cases move to `Test_parse_record`, which
   reads the count (phase record D3 and D4). The test names and the module
   docstring that say "no worse" or "five pass rules" are renamed or
   rewritten. `test_passes_a_figure_exactly_at_a_margin_whose_float_falls_short`
   goes with `TOKEN_MARGIN`. `test_refuses_with_a_line_for_each_other_rule`
   becomes a case that a side worse on every figure S1 says judges nothing
   gets `pass` with no reason line. The rule 3 reason literals carry the new
   numbers. `model_numbers` keeps its point, a record whose own verdict
   fails and which `model` reads past, by failing S1's rule 3 (a reach
   grader the baseline lacks, short on a new run) in place of rule 4.
5. **S5 every other sentence that calls the suite the proof of a rewrite is
   rewritten in place.** `README.md:357` ("the cases each agent's rewrite is
   proved on") and its Korean edition `README.ko.md:362-364` ("에이전트
   정의를 다시 쓸 때 그 정의를 증명하는 케이스") say what the cases are for as
   S1 does. `tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py`
   is renamed with `git mv` for what its one case holds, and the four
   docstrings that cite it change with it: `tests/evals/test_noninferiority.py:4`,
   `tests/evals/test_replay_targets.py:13`, `tests/evals/test_rule_cases.py:10`
   and `tests/evals/test_seed_defects.py:11`. The sentence of
   `docs/running/measuring-a-run.md` changes through `## Rule changes` below
   and is not edited in the pull request.

Out:

- Any paid run. The issue puts it out of scope, and no acceptance row needs one.
- Renaming `evals/scripts/noninferiority.py` or `tests/evals/test_noninferiority.py`.
  The issue names both as its coordinates, and `tests/censuses.py`, which
  #1255 owns, cites the script by path.
- The `regrade` and `model` subcommands' rules. The measure decides neither.
  `model` chooses the sealer's model from every grader and the spend, and
  it changes only by following `verdict`'s narrower `no result`, which S4
  pins.
- The files #1255 and #1256 own (*Grounding*, the spawn's row).
- Records judged before this change, which stand in git history only. No
  compare record stands in the tree at HEAD (executed:
  `git ls-files 'seal/**/evals/*'` prints nothing). `check` judges a record
  by the rules at HEAD.
- The cases under `evals/behaviour/` and the 13 `check:` lines that name them.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A1 A rewrite worse only on figures that judge nothing | Given numbers where recall fell by two finds, the false-finding rate rose past 0.05, the preload is no smaller and both token figures rose past 7%, when `verdict` reads them, then it gives `("pass", [])` | The S4 rows, red against `verdict` at `bac426446` and green after S2: `bin/test -q tests/evals/test_noninferiority.py -k Test_verdict` |
| A2 A rewrite that breaks an agent's output | Given a shape or reach grader whose pooled passes fell, or one failing every new run where the baseline passed it, or one the baseline lacks failing a new run, when `verdict` reads them, then it gives `fail`, each reason line ending in its new rule number, in S1's order | `test_refuses_with_each_rules_line_in_its_order`, with the new literals |
| A3 Figures that are unknown | Given a side with unknown tokens, unknown or no tool calls, or unknown preload bytes, when `verdict` reads it, then it gives `pass`, and `render` writes `unknown` in those cells | The four converted `VERDICTS` rows, red first; `Test_cost_rows` unchanged and green |
| A4 What is still no result | Given a side cut short, a case the new side did not run, or a case run a different number of times, when `verdict` reads it, then it gives `no result` | The `no result` rows of `VERDICTS` that S4 keeps, green before and after |
| A5 The record a person reads | Given two sides, when `compare` writes the record, then it opens `# proofer — phase 3 smoke run` and reads back to the verdict it states | `Test_render`, its title assertion red first; `Test_read_record` and `Test_check_record` green |
| A6 The model choice | Given a model record whose own verdict fails only on S1's rule 3, with every grader held and Sonnet's spend lower, when `model` reads it, then it prints `sonnet`; and on a cut side it prints `opus` | `Test_cheaper_model` with the reworked `model_numbers` |
| A7 No sentence left that calls the suite the proof | Given the branch's last commit, when the three commands of plan *Technical context* run, then every hit is one S1 to S5 rewrote or one that claims nothing about a rewrite, and `git ls-files '*non_inferior*'` prints nothing | The three commands, their output in the phase record |
| A8 The rule change reads | Given this design, when `skills/settle/scripts/rule_changes.py` parses `## Rule changes`, then it returns one `change` on `docs/running/measuring-a-run.md` and refuses nothing | The pull request's `chain-check`, which asks the same reader |

## Data & interfaces

- `evals/scripts/noninferiority.py#verdict(numbers)` keeps its signature and
  its return shape, `(verdict, [reason])`, with the three verdict words of
  `VERDICTS`. It reads `numbers["graders"]`, `old_cut` and `new_cut`.
  `merged` still builds every other key, and `render` and `parse_record`
  still write and read every header row.
- A reason line of rule 1 to 3 keeps today's text, and only its suffix
  changes from `(rule 3)` to the new number.
- The record's first line changes from `# <agent> — phase <N> non-inferiority`
  to `# <agent> — phase <N> smoke run`. `parse_record` never reads the first
  line (read: it reads the header rows, `## Graders`, `## New preload` and
  `Verdict:`).
- No subcommand, argument, exit code or file name of the script changes.

## Rule changes

- change
  file: docs/running/measuring-a-run.md
  section: What a measurement must survive, and what it must not invent
  from: A margin a claim fixes before its run is that claim's criterion and
    not a band in this sense: the pass rules of `evals/README.md` *The
    behaviour suite* decide whether one preload rewrite proved itself not
    worse, and they file nothing.
  to: A criterion a claim fixes before its run is not a band in this sense:
    the pass rules of `evals/README.md` *The behaviour suite* decide whether
    one rewritten preload broke the shape of an agent's output, and they
    file nothing.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| Rule 1, recall not fallen, with its one-find exception | `evals/scripts/noninferiority.py#verdict` | Recall is written in the record's `## Graders` rows and judges nothing (S1). The measure's record shows no recall fail acted on as a defect |
| Rule 2, the false-finding rate within the margin | `evals/scripts/noninferiority.py#verdict` | The report and false row counts stay in the record's header and judge nothing (S1) |
| Rule 4, the preload's bytes below the baseline's | `evals/scripts/noninferiority.py#verdict` | The bytes stay in the record, and `.github/scripts/release_report.py` reads them with no run on every pull request into `main` |
| Rule 5, the two token figures within the margin | `evals/scripts/noninferiority.py#verdict` | Both figures stay in the record's header rows and judge nothing (S1) |
| The `no result` for unknown tokens, tool calls or preload bytes, or no tool calls | `evals/scripts/noninferiority.py#verdict` | No rule reads those figures any more, so an unknown one is written `unknown` and judges nothing, as spend already does |
| `FALSE_MARGIN`, and `TOKEN_MARGIN` with its comment | `evals/scripts/noninferiority.py#FALSE_MARGIN`, `evals/scripts/noninferiority.py#TOKEN_MARGIN` | Rules 2 and 5 were their only readers (executed: `git grep` finds them only in the script, its README and its tests) |
| The reasoning for rule 5's two figures | `evals/scripts/noninferiority.py#tool_calls` docstring, and the rule 5 comment inside `verdict` | No rule weighs a token figure, so the reason why one is chosen over another has nothing to govern. The function stays, because the record still writes the tool-call count |
| Pass rules 1, 2, 4 and 5, the tool-call sentence of rule 5, and two items of the `no result` list | `evals/README.md` *The behaviour suite* | S1's three rules and its paragraph on what is recorded |
| The `VERDICTS` rows that expect `fail` on rules 1, 2, 4 and 5 or `no result` on an unknown figure | `tests/evals/test_noninferiority.py#VERDICTS` | Each figure keeps one row that expects `pass` (S4), and the ten rows that failed rule 1 or pinned a boundary S2 removes go (phase record D1) |
| The margin case and the line-per-other-rule case | `tests/evals/test_noninferiority.py#Test_verdict` | `TOKEN_MARGIN` is gone, and the second becomes A1's no-reason case |
| The module name that says a rewritten definition is proved non-inferior | `tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py` | The same case under a name for what it holds (S5) |

S2 adds no mechanism. It takes four rules and one `no result` arm out of
a verdict and keeps its rule 3.

Framed 2026-11-04 by framer, before the build.
