# Implementation Plan: 1795798115-the-plugin-is-named-for-the-seal

## Technical context

The tree as read at `e904fbce`.

**What the work builds on.** The names stand in a few constants and in the texts that state them. The root's name, the second root, the marker and the record file names are `lib/optin.py` lines 41 to 82. The block fence, the verdict key and the verdict words are `lib/fields.py` lines 69 to 92, and the verdict's pattern is `lib/fields.py` lines 195 to 212. The trailer's key is `skills/code-review/scripts/chain_check.py` line 1994, the check's read of the root's name is `#root_name` at line 1860, and its read of the final record is `#guarantee` at line 1711. The command's table of subcommands is `skills/implement/scripts/seal.py#TOOLS` at line 115. `tests/censuses.py` holds the list of agents and refuses a literal root name outside `lib/optin.py`, so each phase moves the census with the name it renames.

**The approach.** The rename is cut by name family, one family a phase. A family is one name with every constant, reader, test, fixture, template and text that states it, so each phase's commit leaves code, tests and texts agreeing on that name. `frame/design.md` *The words* gives the word for each sense, and *Formats a script reads exactly* gives each spelling a script reads. The word *seal* has six senses at `e904fbce`: the root, the command, the fence, the final party's act and record, the mark, and the drawing. A phase renames the occurrences of its own sense and leaves the others to their phase.

**Where the root moves.** Phase 7 changes `lib/optin.py#HOME` and `#MARKER` and moves this repository's `seal/` to `iadd/` in one commit, the work item's directory with it. Before that commit the tree's code and the installed release both read `seal/`. After it the tree's code reads `iadd/`, and the installed release finds no root in this checkout (`frame/design.md` G9). The phase stands as late as the build allows, so that phases 1 to 6 run with every installed tool reading the records.

**How each step reads the work item's records from phase 7's commit on.** The work item's directory is then `iadd/threads/1795798115-the-plugin-is-named-for-the-seal`, and the tree is the plugin whose forms its own checks read.

| Step | What reads or writes the records | How |
|---|---|---|
| phases 8 and 9 | the crafter | its prompt names the directory, and each `seal <subcommand>` its definition names is run as `bin/iadd <subcommand>` from this checkout. The phase record and `gaps.md` hold no fenced block, so their form does not change |
| a review round | the proofer | it writes the round record from the tree's `templates/records/sdd-round.md`, whose fence is `iadd`. The orchestrator reads `python3 skills/code-review/scripts/chain_check.py --worktree` from this checkout |
| a fix pass | the crafter | it closes findings inside the blocks the round record already holds |
| the broad run | the tree's gate | `bin/iadd gate --base <base> --record <the directory>`. An installed `seal gate` hands the run to the same script (`frame/design.md` G8) |
| the body | the tree's composer | `bin/iadd pr-body` |
| the inspection | the inspector | it follows the tree's `agents/inspector.md` and writes `inspection.md` from the tree's `templates/records/sdd-inspection.md` |
| the stamp | the tree's stamp script | `bin/iadd stamp --inspection <path>` queues it. The `Stop` hook of the session is the installed release's and reads the old directory, so the orchestrator draws with `bin/iadd stamp --from <path>` |
| the pull request's check | this repository's `.github/workflows/hygiene.yml` | it runs the checkout's scripts, which read `iadd/` |

The proofer and the inspector each write a record whose form this work changes. The installed definitions name the old template, the old file and the old verdict line, and the installed final party's definition names `guarantee.md` as its only write. So from phase 7's commit on, the prompt that spawns either party names the tree's `agents/<name>.md`, `skills/core/SKILL.md` and `skills/agent-contract/SKILL.md` as the files that bind it. Which agent type carries that prompt is the orchestrator's choice. A commit made before phase 7's ends with the trailer `Seal-Routing:`, as the installed convention writes it, and a commit from phase 7's on ends with `IADD-Routing:`.

**The failure scenario of the chosen approach.** A phase misreads a sense: it renames the plain word *guarantee* in `skills/agent-contract/SKILL.md` rule 13, or leaves *sealed* where a text means the verdict. The searches of `frame/design.md` *The searches* find a word that stayed and cannot find a word that was renamed wrongly, so a wrong rename is found only by the round that reads the diff. In six months the likelier break is in a repository that moves later: one that renames its root and leaves the key `Pull request seal mark` in its `config.json` loses its mark and is told nothing, because an absent key writes no mark and says nothing (`skills/code-review/scripts/pr_body.py#seal_mark`). *Operational impact* names the key for that reason.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| One phase per name family, the root last among the renames, and the parties after the move bound by the tree's definitions | a sense misread in one phase is found only at review; the parties after phase 7 are spawned by a prompt and not by the installed agent type alone | chosen |
| One sweep in one commit | the searches of `frame/design.md` G20 print several thousand lines over six senses of one word. One spawn cannot read each for its sense, and a sweep by pattern renames *a platform guarantee* and the drawings with the rest | rejected |
| Phases cut by directory: the code, then the tests, then the documents | a commit whose constants and whose cases disagree fails its narrow tests, and the text cases under `tests/text/` hold documents to the code, so no phase but the last would close green | rejected |
| Move this repository's root in the first phase | every build phase would then run with the installed hooks silent and the installed command blind to the records, where the chosen order leaves phases 8 and 9 so | rejected |
| Leave this repository's root for a commit after the release, as #1651 *Order* step 3 reads | the tree's gate refuses a repository with no root (`skills/verify/scripts/broad_gate.py` lines 1953 to 1962), an installed gate hands every run to the tree's copy, and the lines of `tests/` that `frame/design.md` G7 lists read the root under the name the code gives it (G8 holds the gate's part). The broad run could record nothing, and the final party's step 1 would withhold | rejected |
| Read both spellings for one release, so the installed agents could finish this run in the old forms | #1651 *How the repositories move* says a form has one spelling, and `skills/core/SKILL.md` *The rule a mechanism is kept against* refuses a script that carries a list of spellings. The second reader would be a mechanism kept for one run | rejected |
| Keep the marker and the discovery by name and marker, with the second place removed | none found. The premise that keeps it is #1651's table, which gives the new marker and so decides that a marker stays; checked in the issue body (`frame/design.md` G1) | chosen |
| Replace the marker by the directory's name alone, since `iadd` is not a common directory name | a repository that holds an `iadd/` of its own would opt in by accident | rejected |
| Keep the fence's info string `seal` | each record a party writes would open its fields with the word #1651 takes out of the vocabulary, and a reader of a round record would meet *seal* where no inspection is meant | rejected; the fence takes the plugin's name, as the root, the command and the trailer do |
| Spell the second verdict `Verdict: not cleared reason: <reason>` | the value's first word is the verdict (`lib/fields.py#verdict_word`), and *not cleared* is the state that also covers `undecided` and no inspection, so one word would name two things | rejected; `withheld` and `undecided` keep their one sense, and *not cleared* names the state |
| Spawn the final party as the installed agent type with a prompt that names the new file | the installed definition names `guarantee.md` as its only write and says that a write not named there is one it does not make, so a party that keeps its definition declines | rejected for the inspector; the orchestrator's choice for the other parties |
| Write the definition as a section of `docs/layout/one-root-by-lifetime.md`, beside *Naming* | that document's reader is whoever sets a repository up, and the definition's reader is a person asking what IADD is and the owner at the comparison. One document would be opened by two readers for different parts, which `skills/core/SKILL.md` *A document is cut by who opens it and at which step* refuses | rejected; the definition is `docs/method/iadd.md` and takes *Naming* |
| Korean names `검사자` and `검사`, or the English words alone | `검사` names a check throughout the Korean documents (`frame/design.md` G15), and #1651 asks for Korean names | rejected |
| Rename `assets/seals/` and the words for the drawings | the picture is a wax seal and stays one. `README.md`, `README.ko.md` and `TRADEMARKS.md` link the directory, and nothing there names the plugin's record | rejected |

## Phases

Each phase renames in the Korean documents the words of its own family (Scope item 9), updates the rows of this repository's own root that state its names, and is one crafter spawn. The searches are those of `frame/design.md` *The searches*, and until phase 7 closes the work item's directory in each is `:!seal/threads/1795798115-the-plugin-is-named-for-the-seal`.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope item 1 | the cases of `tests/lib/test_optin.py`, `tests/skills/test_chain_check.py` and `tests/skills/test_seal.py` that hold the root's discovery, search A9 prints nothing | 1d72f657 |
| 2 | Scope item 2 | the cases of `tests/test_censuses.py` and of the test files the phase renames; search A1 prints nothing | 8fabf95e |
| 3 | Scope item 3 | the cases of `tests/lib/test_fields.py`, `tests/skills/test_chain_check.py`, `tests/skills/test_pr_body.py` and `tests/skills/test_seal_stamp.py`, the case that refuses `Verdict: sealed` shown red first; search A2 prints nothing | |
| 4 | Scope item 4 | the cases for the stamp, the mark and the two config keys in `tests/skills/`, `tests/lib/test_config.py` and `tests/github/`, each message for a state pinned by a case shown red first; search A7 prints nothing | |
| 5 | Scope item 5 | the cases of `tests/lib/test_core.py`, `tests/lib/test_optin.py` and `tests/test_censuses.py`, and the cases that read the manifest and the marketplace entry; search A3 prints nothing | |
| 6 | Scope item 6 | the cases of the renamed `tests/skills/test_iadd.py` and of `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`; `bin/iadd --help` lists the subcommands; search A8 prints nothing | |
| 7 | Scope item 7 | the cases of `tests/lib/test_optin.py`, `tests/skills/test_chain_check.py` and the files of `frame/design.md` G7; `git ls-tree HEAD -- seal` prints nothing; `bin/iadd mode --check` exits 0; search A4 prints the lines of `skills/settle/SKILL.md` that name `Seal-Routing:` as the trailer of commits before this release, and no other line | |
| 8 | Scope item 8 | `bin/iadd fold` exits 0; the cases of `tests/behaviour/test_a_cited_section_stands_in_its_file.py`; `git grep -n -e '^## Naming' -e '^## 이름' -- docs/layout` prints nothing | |
| 9 | Scope item 10 | searches A1 to A9 give the results the acceptance table of `frame/design.md` states; `.claude-plugin/plugin.json`'s `version` is the one the command of *Operational impact* prints | |

## Overlap with the release

The spawn names no other open work item of the release, so this work meets none.

## Operational impact

- **The plugin is registered anew.** The marketplace and the plugin are both named `iadd`, and the `renames` map is gone, so an installed `agentic` does not update into `iadd`. A deployer adds the marketplace again, installs `iadd`, and removes the old plugin by hand.
- **Each repository that runs the plugin moves in one commit of its own**, outside this work item: `seal/` to `iadd/` with the new marker as the first line of its `README.md`, `guarantee.md` to `inspection.md`, each fence to `iadd`, `Verdict: sealed` to `Verdict: cleared`, the keys `Pull request seal mark` and `Release note seal mark` to their new names in `config.json`, and the tag its `hygiene.yml` pins to the release that carries this work. A key left under its old name turns the mark off without a message.
- **Files outside any repository keep their old names until moved by hand.** They are `~/.claude/agentic/pact-paths.json` and `~/.claude/agentic/parity-paths.json`, the opt-out file `agentic-scratch` and the stamp's two directories under a clone's common git directory, and `agentic-last-export.json`. Each is read under `iadd` after this work.
- **The workflows' names change.** `publish-release.yml`'s job `seal` becomes `mark`, and the variables that open `AGENTIC_` open `IADD_`. A release note already published keeps the image `seal.png` it attached.
- **This pull request carries the release's version move.** Phase 9 moves `version` in `.claude-plugin/plugin.json` in the commit that adds `changelog.md`. It reads the version from the milestone of #1651, with `gh issue view 1651 --json milestone --jq .milestone.title`, which printed `release: 0.40.0` on 2026-11-28.
- **This run, from phase 7's commit on**, reads the records as the table of *Technical context* gives it. The installed hooks find no root and stay silent for the rest of the run, the one that refuses a question under automation among them.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-28 | From phase 7's commit on, the proofer and the inspector are spawned as the harness's general-purpose agent type, with a prompt that names the tree's `agents/<name>.md`, `skills/core/SKILL.md` and `skills/agent-contract/SKILL.md` as the files that bind them (questions row Q5) | The installed definitions are the last release's, and the final party's names `guarantee.md` as its only write. A party bound by the tree's definitions writes the forms the tree's checks read | `frame/plan.md` *Technical context*, and `skills/core/SKILL.md` *Each agent judges its own target, independently of the others* |
