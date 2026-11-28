# Design: IADD is the method and a product only expresses it (#1658)

## Grounding

The tree as read at `1790fab7`.

Each row is labelled `executed` where a command gave the fact and `read` where a file was opened. The framer ran no check of the repository's.

| Policy clause | What it fixes for this work |
|---|---|
| G1. #1658's body and comments, as `gh issue view 1658 --json title,body,comments` printed them on 2026-11-28: no comment. #1651's body as amended on 2026-11-28 and its two comments, as `gh issue view 1651 --json title,body,comments` printed them (`executed`) | #1658 is the source for the three layers and its table *The names*. #1651 *How the repositories move* still rules out a shipped migration, and its *Order* puts CodeChallenge after the release. The comments add nothing to the request: one names #1657 for the comparison, the other names #1658 |
| G2. `routing.md` of this work item (`read`) | Planning `framer`, Implementation `crafter`, the review chain, Automation `yes`, the pull request. It names `release/v0.40.0` at `801465cb` as the base, and says the version is already 0.40.0 there |
| G3. `skills/core/SKILL.md` *The rule a mechanism is kept against*: a script holds a gate only on a line in the one spelling its form gives it, and no script carries a list of spellings (`read`) | No reader accepts `iadd` beside the new spelling. Each format in *Data & interfaces* has one spelling after this work |
| G4. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*: a work item whose subject is the policy root's own text edits the policy root directly, and re-points every unsettled design's rule changes that name a document or section it moved (`read`). The one other work item under `iadd/threads/` is #1656's, `1795798115-the-plugin-is-named-for-the-seal`, whose `## Rule changes` is `- nothing` (`executed`: `ls iadd/threads`; `read`: its `frame/design.md`) | This work rewrites the names the policy documents state, so it edits `docs/` directly and `## Rule changes` holds the no-change block. No unsettled design names a section this work moves |
| G5. `lib/optin.py#HOME`, `#MARKER`, `#SCRATCH`, `#home_paths`, `#home_at`, `#marked_home` (`read`) | The root is found by name and marker at `<repo>/<HOME>/` and then `<git-common-dir>/<HOME>/`. Every reader in shipped code takes the name from `HOME` (`executed`: `git grep -n -P '(?<!\w)(optin\|OPTIN)\.HOME' -- '*.py'`) |
| G6. `skills/code-review/scripts/chain_check.py#changed`, `#changed_routing`, `#edited_work_items` and `#_checked` (`read`) | `changed` puts both names of an exact move, same basename and same blob, into `moved`. `changed_routing` and `edited_work_items` leave a moved `routing.md` and a moved `frame/design.md` out, and `_checked` reads the work items under `routing.optin.HOME`. So #1656's `routing.md` and `frame/design.md` stay no declaration of this pull request only while they move byte for byte |
| G7. `tests/` joins this repository's root by name in 17 lines of 9 files (`executed`: `git grep -n -E 'ROOT, *"iadd"\|ROOT */ *"iadd"\|"iadd", "threads"\]' 1790fab7 -- tests`), and `tests/censuses.py#RECORDS` is `("iadd/threads/", "evals/behaviour/")` (`read`) | The root's name in the code, those cases, `RECORDS` and this repository's own root change in one commit. With `RECORDS` left behind, the readers of `tests/behaviour/test_a_cited_section_stands_in_its_file.py` would read every record under `agentory/threads/` as living text |
| G8. `tests/censuses.py#root_name` and `#_held`: a string that is `HOME`, or opens with it and `/`, is refused outside `lib/optin.py`, `tests/` and `evals/`, and an exemption that excuses nothing is refused (`read`). The exemptions stand above `lib/fields.py#INFO`, above `prog="iadd"` in `skills/implement/scripts/iadd.py#main`, and above `skills/verify/scripts/pact_check.py#MAP_PARTS` (`executed`: `git grep -n 'exempt from root_name'`) | Each exempts a value equal to `HOME` today that names no root. None equals `agentory`, so the commit that changes `HOME` removes all three, whatever the other phases have renamed |
| G9. `.gitattributes` line 28, `/iadd/ export-ignore` (`executed`: `git grep -n -i iadd -- .gitattributes`) | The `dist` archive leaves the root out by its name, so the line follows the root |
| G10. `~/.claude/plugins/installed_plugins.json` names `agentic@agenticseal` at 0.39.4, `which seal` printed a path under the installed plugin's cache, and neither `iadd` nor `agentic` is on `PATH` (`executed`, 2026-11-28) | The installed release reads `seal/`, so no installed tool reads `iadd/` in this checkout and the root can move first. The names this work returns to are the installed ones, so `/agentic:update` reaches 0.40.0 with no new registration. Every subcommand of the run is `bin/<command>` from this checkout |
| G11. At `35bef264` (0.39.4) the manifest's `name` is `agentic` and `displayName` `AgenticSeal`, the marketplace is `agenticseal` with a `renames` map `{"specseal": "agentic"}`, and the README's title is `# AgenticSeal` (`executed`: `git show 35bef264:.claude-plugin/plugin.json`, `:.claude-plugin/marketplace.json`, `:README.md`) | *As at 0.39.x* in #1658's table reads as these values for the plugin's `name`, the prefix and the marketplace. The display name, the title and the description are not 0.39.4's word for word, because `AgenticSeal` was the product's name and the seal's, and questions row Q1 holds them |
| G12. The word diff of `35bef264..801465cb` outside #1656's directory, with git's word regex `[A-Za-z0-9_]+\|[^[:space:]]`, pairs `seal` with `iadd` 3358 times in 272 files, `agentic` with `iadd` 342 times in 100 files, `AGENTIC_EOF` with `IADD_EOF` 458 times, `AgenticSeal` with `IADD` 96 times in 36 files, `agenticseal` with `iadd` 17 times in 6 files, and `seal_home` with `iadd_home` 10 times (`executed`: `git diff -M --word-diff=porcelain` and a pairing script under the framer's scratch) | Every `iadd` at `1790fab7` outside the two work items' directories and the definition came from #1656, and its old word gives its first reading: `agentic` and `AGENTIC_` were the product's, `seal/` the root's, `seal <subcommand>` the command's, and the `seal` fence the records'. The phases read each line for its sense, since `seal` held four senses |
| G13. `docs/method/iadd.md` *The names* and *The record forms*, and `docs/README.md` *docs/method/* (`read`). `ls docs/method/` lists `iadd.md` alone (`executed`) | The definition owns the names, and the records' forms are listed there as the method's. No Korean edition of the definition exists |
| G14. `lib/fields.py#INFO`, `#OPENER`, and `docs/forms/the-round-record.md` *The round record*: a block a script reads fields in opens with three backticks and `iadd` (`read`) | The fence is a record form. #1658 keeps *the vocabulary #1656 gave the records*, the trailer among it, and `docs/method/iadd.md` *The record forms* lists the forms as the method's. So the fence keeps `iadd` |
| G15. `lib/core.py#HEADER` reads `IADD core from {path}, plugin {version}.`, and the core's `description` opens *The values every IADD party judges by* (`read`) | The hook's line names the method's core and keeps `IADD`, and this repository's `CLAUDE.md` keeps quoting it |
| G16. `.github/scripts/publish_release_note.py#fragment_re` and `#fragments` read a fragment at `<HOME>/threads/<id>/changelog.md`, with `--no-renames --diff-filter=A`, and link it to the pull request of the oldest commit in the range that adds that path (`read`). A probe repository that adds `iadd/threads/1-a/changelog.md` in `feat: a (#1656)` and moves `iadd/` to `agentory/` in `feat: b (#1658)` lists `agentory/threads/1-a/changelog.md` as added, and `git log --full-history` on that path names only `feat: b (#1658)` (`executed`, under the framer's scratch `probe-note/`) | After the move, #1656's fragment is read under `agentory/` and its entry in the 0.40.0 note links to this pull request. #1656's fragment also states `iadd` as the command and the root. Scope item 6 rewrites its sentences in place, and questions row Q3 holds the link |
| G17. `evals/behaviour/*/rule-*/` are written by `evals/scripts/rule_cases.py`, and `tests/behaviour/test_evals_layout.py` holds the committed cases to what `rule_cases.py --out` writes (`read`: lines 246 to 282). The hand-written proofer cases `replay-*` and `seeded-*` hold `iadd:proofer` in their prompts and graders and no root path (`executed`: `git grep -n -i iadd -- 'evals/behaviour/proofer/replay-*' 'evals/behaviour/proofer/seeded-*'`) | The generated cases change by running the generator, and the hand-written ones change their agent type alone |
| G18. `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py` lines 156 to 167: the bare command is no locator for the dispatcher because it is also the plugin's name (`read`). At `3de26281` its comment, the docstring of `test_the_bare_command_is_not_a_locator`, the failure message and the message's pin in `test_the_failure_message_offers_a_repair_that_actually_works` give the reason as *also the routing question's first answer*, which phase 2 wrote because the plugin is not yet `agentic` there (`read`: `trail/phases/phase-2.md`) | The case keeps its special case under the new name. From phase 4's commit the bare word is the plugin's name and the routing answer both, so phase 4 adds the plugin's name to the reason in the comment, the docstring and the message, and the pin takes the message's new words, as contract rule 14 asks of a message a person reads |
| G19. `iadd/follow-up.md` row 48 tells the owner to read `seal range` in the records of releases before the one that carries #1651 and `iadd range` from it; no other row waits on this work (`read`) | The records of 0.40.0 hold `iadd range` in #1656's directory and `agentic range` in this one's. The row names the three spellings and keeps `iadd range` |
| G20. `gh release view` on 2026-11-28 named `v0.39.4`, whose note holds no `### Process changes`; #1656's `changelog.md` holds two rows under that heading (`executed`, `read`) | The process changes this work takes over are #1656's two rows: every party runs the command and the root by the names that row gives, which this work changes |
| G21. `git grep -E` with `\b` printed no line on this git, 2.54.0 (Apple Git-157), where `-P` with the same pattern printed 19 (`executed`: `optin\.HOME\b`) | Every search below uses `-P` or `-F`. A pattern with `\b` under `-E` finds nothing whatever the tree holds |
| G22. The searches the frame wrote at `9c84cd8c` as *Data & interfaces* *The searches*, read there with `git show`, run at `1790fab7` with both work items' directories excluded as `:!iadd/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it` and `:!iadd/threads/1795798115-the-plugin-is-named-for-the-seal` (`executed`) | D1 printed 3606 lines in 365 files, D2 483 lines in 28 files, D3 204 lines, D4 five files, D5 56 lines, D6 eight tracked files outside the root and every file under `iadd/` but this work item's, and D7, run on `iadd/threads/1795798115-the-plugin-is-named-for-the-seal/changelog.md`, six lines. E1 printed 1705 lines, E2 1223, E3 225 and E4 200. Of D1's lines, 308 match none of E1 to E4 (`executed`: `comm -23` of D1's and E1 to E4's `path:line` lists): bare `"iadd"` literals, `` `iadd` `` alone and similar, which each phase reads for its sense. Every line D1 to D6 printed is one that a *Scope* item from 1 to 6 renames, except the lines each search's filter or its cell names |
| G23. `iadd/parity.json` is absent (`executed`: `ls iadd/`) | No original stands between the ticket and the code |
| G24. Read at `3de26281`, where phases 1 and 2 have closed: `git grep -P '(?i)iadd' -- . ':!agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it'` printed 1616 lines. Each was sorted by its sense into a kind *The keep file* keeps, 618 lines, or into the phase that renames it: 720 lines for phase 3, 266 for phase 4, and 12 for phase 5, of which 8 are #1656's `changelog.md` and 4 are `docs/method/iadd.md` *The names* (`executed`: a classifier under the framer's scratch `frame-2/`, whose kept lines were read for their kind; `read`: the lines it could not sort, 33, one by one) | The keep files of *The keep file* hold these lines. A line that holds a kept kind and a product's or a place's `iadd` beside it is the phase's, not the keep file's |
| G25. The owner decided on 2026-11-28, in #1659 point 1 and applied to this work item by hand, that the remaining phases' acceptance is an exact diff against a keep file (the orchestrator's message to the framer, not opened by the framer) | Phases 3 to 5 close on *The keep file*'s command, and no filter that strips a part of a line or excludes a path accounts for a line, except this work item's directory |
| G26. The crafter's `grep` refuses `-P` with `grep: invalid option -- P`, so the last filter of D5, as the frame at `9c84cd8c` wrote it, printed nothing whatever the tree held (`read`: `trail/phases/phase-2.md`). In the framer's shell `echo x \| grep -P x` printed `x` (`executed`) | Whether a `grep -P` filter runs depends on which `grep` stands first on the `PATH`. The acceptance command uses `git grep -P`, `sort` and `diff` and no `grep` |
| G27. The alternatives of K, the filter the frame at `9c84cd8c` wrote, `` `iadd` alone `` and `"iadd",? ?\]` stripped the bare command in three lines of `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py` and the eval harness's key wherever it is subscripted, as `run["iadd"]` and `result["iadd"]` in `evals/scripts/noninferiority.py` and `tests/evals/test_noninferiority.py` (`read`: `trail/phases/phase-2.md`; `executed`: at `3de26281` the phase 3 lines of G24 hold 14 lines with `["iadd"]`) | A filter that strips a part of a line hides every other sense the same spelling holds. The keep file holds whole lines, and the eval harness's key is phase 3's |
| G28. `git ls-files -- . ':!agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it' \| grep -i iadd` printed `docs/method/iadd.md`, `skills/verify/scripts/pytest_record/iadd_pytest_record.py` and `tests/skills/test_iadd_pytest_record.py` at `3de26281` (`executed`) | `git grep` reads contents and not names, so the file names have a line of their own in the acceptance. The two pytest recorder files are phase 3's |

## Scope

The plugin's names take the three layers #1658 gives. Nothing the chain does changes: the parties, their order, what each reads and writes and what each check refuses stay as they are at `1790fab7`.

In scope, by number:

1. **The records root is `agentory/`.** `lib/optin.py#HOME` and `#MARKER`, the root's README template, the local-mode root under the common git directory, the export's archive stem, the root's headings and citations, `tests/censuses.py#RECORDS`, `.gitattributes`, and every text, case, fixture and generated eval case that names the root take the values *Formats a script reads exactly* gives. The three exemptions of G8 are removed. In the same commit this repository's `iadd/` moves to `agentory/` with both work items' directories, #1656's byte for byte until item 6 rewrites its fragment, and `agentory/README.md` takes the renamed template's first line.
2. **The command is `agentic`.** `bin/iadd` and `bin/iadd.cmd` become `bin/agentic` and `bin/agentic.cmd`, the dispatcher becomes `skills/implement/scripts/agentic.py`, and every `iadd <subcommand>` a text, a message, a heading or a workflow names becomes `agentic <subcommand>`, with the files and identifiers named for the command. `iadd/follow-up.md` row 48 names the three spellings of the range command in the records, as G19 says.
3. **The environment and the files outside a repository take the product's name.** The variables, the heredoc delimiter, the pytest recorder, the git config key of a fixture, the opt-out file, the stamp's directories, the export's state file, the machine-local maps, the template's clone directory, the temporary prefixes, the eval harness's key and the loader ids take the values *Formats a script reads exactly* gives. The eval harness's key is renamed wherever it stands, subscripted as `run["iadd"]` and `result["iadd"]` or named in a docstring as *under `iadd`*. The loader ids include those in the lines whose alias phase 2 renamed, such as `AGENTIC = load_module(..., "iadd_under_test")`.
4. **The plugin is `agentic`.** The manifest's `name`, the marketplace `agenticseal` and its plugin entry `agentic`, the prefix `agentic:` of every agent and skill, the slash commands and the install spec take the product's name. Where `IADD` names the product, the text takes `agentic`, as *IADD where it names the product* lists. The display name, the titles and the description sentence take the values *Data & interfaces* gives, questions row Q1's answer (a). The locator rule's reason names the plugin's name beside the routing answer, as G18 says.
5. **What is the method's keeps `IADD`.** The method's name in prose, `IADD-Routing:`, the fence's info string `iadd` with every reader, case and fixture of it, `IADD core from`, the marker's word `IADD`, `docs/method/iadd.md` and the record vocabulary #1656 gave stay as they are. *What stays the method's* lists them.
6. **The definition states the three layers, and the release's notes state the names it ships.** `docs/method/iadd.md` *The names* is rewritten as *The names in docs/method/iadd.md* gives. #1656's `changelog.md` is rewritten in place where it states a product's or a place's name, and its other files stay byte for byte. This work item writes its own `changelog.md`.
7. **The keep file closes the work.** Each of phases 3, 4 and 5 closes on the acceptance command of *The keep file*, which prints nothing against that phase's keep file.

Out of scope:

- **Moving CodeChallenge and owlery's records.** #1658 *How it ships* and #1651 *Order* put CodeChallenge after the release, and owlery's at the comparison.
- **Renaming the repository `MichaelYcJo/AgenticSeal`.** #1651 *After this issue* weighs it later, and the marketplace keeps `agenticseal`.
- **The routing answer `agentic`.** #1658's table keeps it. A sentence that names both the answer and the plugin names each by its role, as *The three layers* says.
- **A shipped migration, and the marketplace's `renames` map.** #1651 *How the repositories move* keeps neither, and the one install is `agentic@agenticseal` (G10).
- **#1656's records other than its fragment.** Its `routing.md`, frame, trail, `gaps.md`, `pr.md` and `inspection.md` keep what they said, and G6 holds the first two to a byte-for-byte move.
- **`docs/experiments/`.** It holds no `iadd` (`executed`: `git grep -c -i iadd -- docs/experiments` printed nothing).
- **The version.** It is 0.40.0 in `.claude-plugin/plugin.json` at `801465cb`, and this work moves no version.
- **`TRADEMARKS.md`, `LICENSE` and the emblem's alternative text.** Questions row Q2's answer (a) leaves them as they are.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| The root is found under its new name alone | Given a repository whose `agentory/README.md` opens with `# What IADD keeps in agentory/`. When `bin/agentic mode` runs. Then it names that directory as the root. An `iadd/` whose README opens with `# What IADD keeps in iadd/` is no root, and the root of that repository is the local one | the cases of `tests/lib/test_optin.py` |
| This repository holds `agentory/` and no `iadd/` | When phase 1 has closed | `git ls-tree HEAD -- iadd` prints nothing, `git ls-tree -d HEAD -- agentory` prints one tree, and `bin/iadd mode --check` exits 0; from phase 2 on, `bin/agentic mode --check` |
| #1656's directory moves and declares nothing | When phase 1 has closed, and again when the last has | `git diff -M --name-status 801465cb HEAD -- iadd/threads/1795798115-the-plugin-is-named-for-the-seal agentory/threads/1795798115-the-plugin-is-named-for-the-seal` prints an `R100` line for each file, except `changelog.md` once phase 5 has closed; `python3 skills/code-review/scripts/chain_check.py --worktree` judges this work item alone |
| The command is `agentic` | When phase 2 has closed | `bin/agentic --help` prints `usage: agentic` and lists the subcommands; `git ls-files bin` lists no `iadd` |
| The plugin is `agentic` | When phase 4 has closed | `.claude-plugin/plugin.json`'s `name` is `agentic`, the marketplace's `name` is `agenticseal` and its one plugin entry `agentic`; `tests/behaviour/test_chain_hooks_hardening.py#test_the_marketplace_describes_the_plugin_in_the_manifests_words` |
| The product's and the place's `iadd` are gone, and every line that keeps the old name is one the keep file names | When phase 3, 4 or 5 has closed | the acceptance command of *The keep file*, run against that phase's keep file, prints nothing and exits 0; the file-name line prints `docs/method/iadd.md` alone from phase 3's close; the round reads each line the phase added to a keep file for its kind |
| The definition states the three layers | When the last phase has closed | `docs/method/iadd.md` *The names* holds the table *The names in docs/method/iadd.md* gives; `bin/agentic fold` exits 0 and `tests/behaviour/test_a_cited_section_stands_in_its_file.py` passes; the proofer reads each row against #1658 |
| The release's notes state what ships | When the last phase has closed | each line of #1656's rewritten `changelog.md` that holds the old name stands in `frame/keep.txt` under a kept kind; this work item's `changelog.md` exists and states the three layers |

## Data & interfaces

### The three layers

One sense, one layer, one spelling. The builder reads each occurrence for its sense before renaming it, and G12's old word gives the first reading.

| At `1790fab7` | Sense | Layer | After |
|---|---|---|---|
| IADD | Independent AI-Driven Development, *the IADD process*, its parties, its agents, its core, its definition, a repository that runs it | method | unchanged |
| IADD | the plugin: the thing installed, its page's title, its display name, its suite, its scripts, its releases | product | `agentic`, as *IADD where it names the product* lists |
| `iadd` | the plugin's `name`, the prefix of every agent and skill, the marketplace's plugin entry | product | `agentic` |
| `iadd` | the marketplace's name | product | `agenticseal`, as at 0.39.4 (G11) |
| `iadd` | the command, a subcommand's line, its wrapper, its script, its test file, its document | product | `agentic` |
| `IADD` | the test modules' alias for the dispatcher | product | `AGENTIC` |
| `IADD_` | a variable, a fixture's variable, the scaffolds' heredoc delimiter | product | `AGENTIC_` |
| `iadd-`, `iadd_`, `iadd.` | a file, directory, temporary prefix, loader id, JSON key or git config key named for the plugin | product | `agentic-`, `agentic_`, `agentic.` |
| `iadd/`, and `iadd` as a directory | the records root, shared or local, its template, its headings, a project's own directory of the root's name | place | `agentory/`, `agentory` |
| `iadd-<repo>-<date>.zip` | the export's archive of the root | place | `agentory-<repo>-<date>.zip` |
| `iadd_home`, `OWN_IADD` | a unit or a constant that names the root's place | place | `agentory_home`, `OWN_AGENTORY` |
| `iadd` after three backticks, `` `iadd` `` block | the info string of a block a script reads fields in | method | unchanged |
| `IADD-Routing:` | the commit trailer | method | unchanged |
| `IADD core from` | the first line the `SessionStart` hook prints | method | unchanged |
| `docs/method/iadd.md` | the definition | method | unchanged |
| `agentic` | the routing question's first answer, which leaves each item's route to the orchestrator | routing | unchanged |

The routing answer and the product share the word `agentic` by #1658's decision. A sentence that names both says *the answer `agentic`* or *under `agentic`* for the first, and *the plugin `agentic`* or *the command `agentic`* for the second, so each reads one way by `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*.

### Formats a script reads exactly

Each row is one spelling. No reader accepts the left column after this work.

| Format | At `1790fab7` | After | Layer | Read by |
|---|---|---|---|---|
| the root's directory, shared and local | `iadd` | `agentory` | place | `lib/optin.py#HOME` |
| the marker, the first line of the root's `README.md` | `# What IADD keeps in iadd/` | `# What IADD keeps in agentory/` | place, with the method's word | `lib/optin.py#MARKER`, pinned to the template by `tests/lib/test_optin.py` |
| the root's README template | `templates/setup/iadd-README.md` | `templates/setup/agentory-README.md` | place | `skills/implement/bootstrap.md`, the dispatcher's first setup |
| the root's headings | `docs/layout/the-record-layout.md` *iadd/* and *iadd/threads/<work-item-id>/*, `skills/agent-contract/SKILL.md` rule 11's heading | *agentory/* and *agentory/threads/<work-item-id>/*, rule 11 with `agentory/` | place | `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, which every citation of them meets |
| the records' prefix the censuses leave out | `iadd/threads/` | `agentory/threads/` | place | `tests/censuses.py#RECORDS` |
| the archive rule | `/iadd/ export-ignore` | `/agentory/ export-ignore` | place | `git archive`, which builds `dist` |
| the export's archive stem | `iadd-<repo>-<date>`, a literal | `agentory-<repo>-<date>`, built from `lib/optin.py#HOME` so that the stem has no spelling of its own | place | `skills/implement/scripts/iadd.py#zip_stem` |
| the units named for the root's place | `skills/settle/scripts/fold_check.py#iadd_home`, `skills/verify/scripts/broad_gate.py#iadd_home` | `#agentory_home` in each | place | their callers |
| the commit trailer's key | `IADD-Routing` | unchanged | method | `chain_check.py#TRAILER` |
| the block fence's info string | `iadd` | unchanged | method | `lib/fields.py#INFO` |
| the hook's first line | `IADD core from …` | unchanged | method | `lib/core.py#HEADER`, this repository's `CLAUDE.md` |
| the command and its dispatcher | `bin/iadd`, `bin/iadd.cmd`, `skills/implement/scripts/iadd.py`, `prog="iadd"` | `bin/agentic`, `bin/agentic.cmd`, `skills/implement/scripts/agentic.py`, `prog="agentic"` | product | Claude Code's `PATH` for a plugin's `bin/`, `lib/launch.py`, `templates/setup/hygiene.yml`, `.github/workflows/hygiene.yml` |
| the prefix of a line a subcommand prints | `iadd <subcommand>: ` | `agentic <subcommand>: ` | product | `.github/workflows/hygiene.yml`'s `sed` on `iadd rules: not read: ` |
| the gate's path to the dispatcher | `broad_gate.py#IADD_SCRIPT` | `#AGENTIC_SCRIPT`, renamed with the command in phase 2, since it names the dispatcher's path (*Scope* item 2) | product | `broad_gate.py`'s mode arm |
| the stamp's messages that name no subcommand | `iadd: the stamp for …`, `iadd: no stamp was queued for …` | `agentic: …`, renamed in phase 2 as the command's output, with the lines of `tests/skills/test_stamp.py` that pin them | product | `skills/verify/scripts/stamp.py` |
| the mutation document | `skills/verify/iadd-mutate.md` | `skills/verify/agentic-mutate.md` | product | `skills/verify/SKILL.md` |
| the plugin's name and display name | `iadd`, `IADD` | `agentic`, `agentic` | product | `.claude-plugin/plugin.json`, `lib/core.py#manifest`, the plugin directory check |
| the marketplace's name and its plugin entry | `iadd`, `iadd` | `agenticseal`, `agentic` | product | `.claude-plugin/marketplace.json` |
| the install spec and the marketplace's clone | `iadd@iadd`, `plugins/marketplaces/iadd` | `agentic@agenticseal`, `plugins/marketplaces/agenticseal` | product | `skills/update/SKILL.md`, `README.md` |
| the agent and skill prefix, the slash commands | `iadd:`, `/iadd:config`, `/iadd:update`, `/iadd:parity-setup` | `agentic:`, `/agentic:config`, `/agentic:update`, `/agentic:parity-setup` | product | the harness, from the plugin's name; `evals/scripts/behaviour.py` |
| the description sentence | `IADD, Independent AI-Driven Development: agents frame, build, review and inspect a change, no agent approves its own work, and it ends in an inspection bound to a commit.` | `The plugin that runs IADD, Independent AI-Driven Development: agents frame, build, review and inspect a change, no agent approves its own work, and the run ends in an inspection bound to a commit.` | product, naming the method | `tests/behaviour/test_chain_hooks_hardening.py`, which holds `README.md`'s paragraph under its title to it |
| the variables | `IADD_GATE_INVOKED_AS`, `IADD_RECORD_DIR`, `IADD_RECORD_KEY` | the same names opening `AGENTIC_` | product | `broad_gate.py#INVOKED_AS_VAR`, `#RECORD_DIR_VARIABLE`, `#RECORD_KEY_VARIABLE`, the recorder, `.github/workflows/publish-release.yml` |
| the fixtures' variables and the heredoc delimiter | `IADD_INHERITED`, `IADD_MODE`, `IADD_SETTLE_GH_STUB_HOME`, `IADD_EOF` | the same names opening `AGENTIC_` | product | their tests, and each `scaffold.sh` with `tests/evals/test_rule_cases.py#WRITTEN` |
| the pytest recorder | `skills/verify/scripts/pytest_record/iadd_pytest_record.py`, `-p iadd_pytest_record`, attribute `iadd_path` | `agentic_pytest_record.py`, `-p agentic_pytest_record`, `agentic_path` | product | `PYTEST_ADDOPTS` in the workflows and the gate |
| the opt-out file under the common git directory | `iadd-scratch` | `agentic-scratch` | product | `lib/optin.py#SCRATCH` |
| the stamp's two directories under the common git directory | `iadd-stamp`, `iadd-stamp-refused` | `agentic-stamp`, `agentic-stamp-refused` | product | `skills/verify/scripts/stamp.py#VALUES_DIR`, `#REFUSED_DIR` |
| the export's state file | `iadd-last-export.json` | `agentic-last-export.json` | product | the dispatcher's `#STATE` |
| the machine-local maps | `~/.claude/iadd/pact-paths.json`, `~/.claude/iadd/parity-paths.json` | the same files under `~/.claude/agentic/` | product | `pact_check.py#MAP_PARTS`, the parity setup |
| the template's clone directory | `$RUNNER_TEMP/iadd` | `$RUNNER_TEMP/agentic` | product | `templates/setup/hygiene.yml`, `tests/text/test_ci_gives_the_checks_what_they_need.py#CLONE` |
| the temporary prefixes | `iadd-gate-`, `iadd-gate-base-`, `iadd-layout-moved-`, `iadd-` and the suite's `iadd-…-` | the same opening `agentic-` | product | `broad_gate.py`, `test_layout.py`, `evals/scripts/noninferiority.py`, `tests/conftest.py`; the gate's line `outputs kept under agentic-gate-<random>/` |
| the eval harness's key | `"iadd"` in each run and result | `"agentic"` | product | `evals/scripts/noninferiority.py` |
| the fixture's git config key | `iadd.mode` | `agentic.mode` | product | `tests/lib/test_optin.py` |

A name this table does not give follows *The three layers*: a loader id `iadd_*_for_tests` becomes `agentic_*_for_tests`, a test named for the root, such as `test_the_iadd_readme_cites_the_marker_constant`, takes `agentory`, a test class named for a subcommand, such as `Test_iadd_rules`, takes `agentic`, and a test named for the fence, such as `test_refuses_to_name_a_fence_whose_first_word_is_not_iadd`, keeps `iadd`.

### IADD where it names the product

These lines of `1790fab7` name the product with `IADD`, and each takes `agentic` or a sentence that names the plugin, in the phase *Phases* gives: `.claude-plugin/plugin.json` lines 3 and 5, `.claude-plugin/marketplace.json` lines 3 and 11, `CLAUDE.md` line 1, `CONTRIBUTING.md` line 1, `README.md` lines 6, 8 and 14, `README.ko.md` lines 6, 8 and 14, `SECURITY.md` line 17, `bin/test` line 32, `bin/test.cmd` line 10, `tests/run_tests.py` line 541, `lib/launch.py` line 2, `docs/method/iadd.md` lines 67 to 77, `skills/settle/SKILL.md` lines 232 and 370, `tests/behaviour/test_chain_hooks_hardening.py` lines 187 and 207, `tests/behaviour/test_release_hygiene.py` lines 81, 124, 135, 140, 157, 169 and 178, and `tests/skills/test_broad_gate.py` lines 2181 and 2391. `skills/settle/SKILL.md` line 232 names the release that changed the trailer as the release that carries #1651.

### What stays the method's

The lines that keep the old name are the lines of `frame/keep.txt`, and each belongs to one of the kinds *The keep file* states with its reason. The fence's family is among them: `lib/fields.py#INFO` and every text that says *an `iadd` block*, every case, fixture, grader and generated scaffold line that builds or matches one, and the near misses `Iadd`, `IADD`, `iadds`, `python iadd`, `~~~iadd` and `iadd finding` that the cases of `tests/lib/test_fields.py`, `tests/lib/test_blocks.py`, `tests/skills/test_chain_check.py` and `tests/evals/test_rule_cases.py` refuse. So are `SpecIADD-Routing`, a near miss of the trailer in `tests/skills/test_chain_check.py`, and the method's name in `TRADEMARKS.md`, `README.md` and `README.ko.md`, which questions row Q2's answer (a) keeps. The verdict lines, the check states and the two mark keys hold no `iadd`.

### The keep file

`frame/keep.txt` holds, as `path:content` with no line number and sorted with `LC_ALL=C sort`, each line outside this work item's directory that holds `iadd` in any case once phase 5 has closed. Each line belongs to one kind, and each kind keeps the old name for one reason:

| Kind | Its lines | Why it keeps the old name |
|---|---|---|
| #1656's records | every line under `agentory/threads/1795798115-the-plugin-is-named-for-the-seal/` but its `changelog.md` | a record keeps what it said when it was written, and G6 holds its `routing.md` and `frame/design.md` to a byte-for-byte move |
| the fence | the fence's family, as *What stays the method's* names it | a block's info string is a record form, and the record forms are the method's (G14) |
| the trailer | `IADD-Routing` and its near miss `SpecIADD-Routing` | #1658 keeps the trailer |
| the hook's line | `IADD core from`, the messages that open `IADD core:`, and the lines that quote or pin them | the line names the method's core (G15) |
| the marker | `# What IADD keeps in agentory/` wherever it stands | #1658 gives the marker its word `IADD` |
| the definition | the path `docs/method/iadd.md` | the definition is the method's |
| the method's name | `IADD` where a line names the method: *the IADD process*, its parties and agents, a repository that runs it, the definition's own sentences, and the reserved name of questions row Q2 | the method is IADD, by the three layers |
| history | `agentory/follow-up.md` row 48 | it names `iadd range` as the spelling of #1656's records (G19) |

Two more files carry the lines the later phases own. `frame/keep-4.txt` is `frame/keep.txt` with the lines phase 5 owns, #1656's `changelog.md` and `docs/method/iadd.md` *The names*. `frame/keep-3.txt` is `frame/keep-4.txt` with the lines phase 4 owns. So the lines a phase owns are the lines its keep file holds and the next one does not.

The acceptance runs from the repository's root. `<keep>` is `keep-3.txt` at phase 3's close, `keep-4.txt` at phase 4's and `keep.txt` at phase 5's:

```
A   git grep -P '(?i)iadd' -- . ':!agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it' | LC_ALL=C sort | diff - agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/frame/<keep>
N   git ls-files -- . ':!agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it' | grep -i iadd
```

At each phase's close A prints nothing and exits 0, and from phase 3's close N prints `docs/method/iadd.md` alone. A line `<` is one the tree holds and the keep file does not: a name left behind, or a line the phase wrote that holds a kept kind. A line `>` is one the keep file holds and the tree does not: a kept line the phase changed. A runs no filter on a line's text and excludes no path but this work item's directory, so a line holding a kept kind and a product's `iadd` beside it is printed.

**A phase that writes or changes a line holding the old name of a kept kind writes the line into its own keep file and every later one, in the same commit.** Phase 4's description sentence, which names IADD, phase 5's rows of *The names* and the lines of #1656's rewritten fragment are such lines, and so is a kept line a formatter rewrapped. The phase record names each line the phase added or changed in a keep file and its kind, and the round reads each against the kinds above. A line that holds a product's or a place's `iadd` is no kind and goes into no keep file.

### The searches phases 1 and 2 closed on

Phases 1 and 2 closed on these, before the keep file. `W` is `:!agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it` and `P` is `:!agentory/threads/1795798115-the-plugin-is-named-for-the-seal`. No later phase runs them.

```
E1  git grep -n -P '(?<![\w.~$/-])iadd/|/iadd/|iadd-README|common-dir\)/iadd|\.git/iadd|, "iadd"\)|/ "iadd"|:/iadd|keeps in iadd/|iadd_home|OWN_IADD|iadd-<repo>|iadd-repo-|"iadd-\{' -- . W P | grep -v -E '\.claude/iadd/|RUNNER_TEMP/iadd/|marketplaces/iadd/|"marketplaces" / "iadd"'
E2  git grep -n -P 'bin/iadd|iadd\.(py|cmd)|[tT]est_iadd|iadd-mutate|(?<![\w/.-])iadd (gate|settle|cost|mutate|unverified|deferrals|fold|pact|payload|stamp|layout|rules|pr-body|pr-wait|range|mode|export|import|pr-checks|works)' -- . W P
D3  git grep -n -P '(?<![\w`-])IADD(?=\.\w|\s*=[^=]|\s*[,)\]])' -- '*.py' W P
```

### The names in docs/method/iadd.md

*The names* opens with the rule: **IADD is the method, and a product only expresses it.** No IADD name is chosen to pair with a product, and no product takes the method's name. The names fall into three layers, each with its one sentence:

| Name | Its one sentence |
|---|---|
| IADD | the method this document defines; *the IADD process* is what a product does with one issue, from the routing question to the final inspector's verdict |
| `agentic` | this plugin, one product that expresses IADD: its `name`, the prefix `agentic:` of every agent and skill, the command line `agentic` and the variables `AGENTIC_*`; its marketplace is `agenticseal` and its repository `MichaelYcJo/AgenticSeal` |
| `agentory/` | the place: the records root, visible beside `docs/`, and under the common git directory in local mode; where it stands in each mode is the opening paragraph of `skills/core/SKILL.md`. It is formed like *directory* and *repository*, the place where an agent's work is kept |

The rows for the thread, `agentory/threads/<id>/`, the agents, the inspection, the three states, the settle and `IADD-Routing:` follow, as at `1790fab7` with the root's new name. A row for the block fence `iadd` says it is the info string of every block a script reads fields in, a record form of the method's. A row for the routing answer says it shares the product's word and names the route left to the orchestrator. The sentence *Every identifier is lowercase with no separator, and `IADD` is written only where a person reads the brand* goes, since the three layers replace it.

## Rule changes

- nothing
  why: This work item's subject is the policy root's own text, the names every document states, so it edits `docs/` directly in its pull request as `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* states, and leaves the settle no decision to gather. The one unsettled design, #1656's, changes no rule (G4).

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the three exemptions from `root_name` | the comment above `lib/fields.py#INFO`, the comment above `prog=` in `skills/implement/scripts/iadd.py#main`, the comment above `skills/verify/scripts/pact_check.py#MAP_PARTS` | nothing owns them. Each excused a value equal to `HOME` that named no root, and once `HOME` is `agentory` none is equal, so `tests/censuses.py#_held` refuses each as excusing nothing (G8) |
| the sentence and the two rows that give every part the name `iadd` | `docs/method/iadd.md` *The names* | the three layers in the same section |
| the old spelling of each format | each row of *Formats a script reads exactly* whose *After* differs | the row's *After* cell. No reader keeps the old spelling, by G3 |
| the files named `iadd` for the product or the place | `bin/iadd`, `bin/iadd.cmd`, `skills/implement/scripts/iadd.py`, `skills/verify/iadd-mutate.md`, `skills/verify/scripts/pytest_record/iadd_pytest_record.py`, `templates/setup/iadd-README.md`, `tests/skills/test_iadd.py`, `tests/skills/test_iadd_pytest_record.py` | the same files under the names *Formats a script reads exactly* and *The three layers* give |
| this repository's `iadd/` | `iadd/` | `agentory/`, in the commit of *Scope* item 1 |
| the sentences of #1656's fragment that state a product's or a place's `iadd` | `agentory/threads/1795798115-the-plugin-is-named-for-the-seal/changelog.md` | the same fragment, rewritten in place with the names 0.40.0 ships (G16) |

This design adds no gate, check, hook, mark or rule.

Framed 2026-11-28 by framer, before the build.
