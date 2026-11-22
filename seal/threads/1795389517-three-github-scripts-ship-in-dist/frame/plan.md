# Implementation Plan: 1795389517-three-github-scripts-ship-in-dist

## Technical context

The tree as read at `036e7d424`.

- **The closer.** `.github/scripts/close_issues_on_release.py` loads `lib/console.py` and `lib/gitcmd.py` through `lib/sibling.py` (:73-83). Its closing readers stand at :89-191 and its `run` at :194. `pr_body.py:183` loads the closer at import, inside a `try` that turns a load failure into exit 2 as a command (:182-193). `label_merged_on_release_branch.py:70` loads it for the readers and for `run`, `arrived`, `pull_request_body` and `issue_labels`. `release_completeness_check.py:104` reaches it as `signal.closer`.
- **The check-line reader.** `.github/scripts/rules.py` computes `ROOT` as `HERE/../..` (:69-70). It imports `sibling` lazily, at the first module asked for (:126-140), and reads `skills/settle/scripts/fold_check.py` and `rule_changes.py` through it. `seal.py#TOOLS` (:114-176) holds every other tool under `skills/<area>/scripts/`. `rules.py` is the one exception.
- **The suite runner.** `.github/scripts/run_tests.py` reaches `lib/` as `../../lib` (:78), reads `FLOOR` from `lib/launch.py` (:86), and names its repository `parent.parent.parent` (:170). `bin/test:30` and `bin/test.cmd:7` refuse with one sentence and exit 2 where the runner is absent. That is the path a `dist` copy takes once the runner leaves with `tests/`.
- **What ships.** `.gitattributes:31-44` marks `.github/` paths `export-ignore` one by one, and `git archive` builds each `dist` commit from that file (`docs/releasing/branch-and-release.md` *Cutting a release*). `hygiene.yml:88` is the watched list. `tests/behaviour/test_the_release_check_watches_what_ships.py:42-76` classifies top-level entries in two hand-kept sets. `tests/behaviour/test_a_cited_section_stands_in_its_file.py#archived` (:239) already lists the archive with `tarfile` and no `tar` binary, which the suite needs on `windows-latest`.
- **Constraints.** `lib/*.py` is linted at 3.9 (`ruff.toml:44`), so `lib/closing.py` keeps 3.9 syntax. `CONTRIBUTING.md` *The test layout* places each moved test file and asks for `seal layout --moved` or mutants. `seal rules --check` refuses a check line naming a missing file, so the check-line re-points go in the commit of the move.
- **Failure scenario of the chosen approach, six months on.** A new top-level directory is added, such as a loader's `output-styles/`, and nobody adds it to `.gitattributes` or to the pattern. The derived case fails and names it, so this is a stop at the suite, not a silent gap. The remaining exposure is a new top-level file that an installed loader reads, such as `.mcp.json`. The derived case refuses it until it is named among the files nothing installed reads, and whoever names it there has misjudged. Review reads that set.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the three scripts in `.github/scripts/` and widen the pattern with `\.github/scripts/(close_issues_on_release\|rules\|run_tests)\.py` | `.github/` stays half shipped, so a fourth script a shipped file loads ships unwatched until someone adds it to both lists. `.gitattributes` keeps a line per release script, and the issue's Done-when "No file under `.github/` is loaded by a file `dist` ships" stays false | Rejected |
| Move the closer whole into `lib/` | `lib/` would ship a script whose `main` closes issues and removes labels, so every installed copy carries a tracker writer it never runs. The release workflow would run a file from a shipped root. The issue's direction moves only the readers | Rejected |
| **Closing readers into `lib/closing.py`, with the closer keeping its release acts** | The closer and `label_merged_on_release_branch.py` then load two modules for one job. That is two `sibling.load` lines, and #1573 reworks the closer's `run` next | **Chosen** (*Scope* items 1-2) |
| `rules.py` into `skills/implement/scripts/`, beside `seal.py` | The implement skill does not own the check-line grammar, which is `skills/settle/rule-changes.md` *A rule has one shape*. The reader would stand apart from `fold_check.py` and `rule_changes.py`, the two modules it reads | Rejected |
| `rules.py` into `lib/` | `seal.py#TOOLS` runs commands from `skills/<area>/scripts/`, and `rules.py` has a command line of its own. In `lib/` it would be the one tool `seal` runs from a module directory | Rejected |
| **`rules.py` into `skills/settle/scripts/`** | `chain_check.py` loads a module from another skill's `scripts/`, which it already does for `rule_changes.py` | **Chosen** (*Scope* item 3) |
| `run_tests.py` into `lib/` | `dist` would ship a runner for a suite it does not hold, which is #1420's finding grown rather than reduced. A change to the runner alone would ask a version move that reaches no user | Rejected |
| `run_tests.py` stays in `.github/scripts/`, with `.github/` export-ignored whole | `bin/test`, a file `dist` holds, would still load a `.github/` file, against the issue's first Done-when line | Rejected |
| Move `bin/test` and `bin/test.cmd` out of `bin/` too | Every `bin/test` in the documents, in `seal/config.json`'s `Broad gate` key and in spawn prompts would be re-pointed, for a question #1420 owns and the owner holds | Rejected: out of scope |
| **`run_tests.py` into `tests/`** | `bin/test` in `dist` names a runner `dist` lacks and answers with its refusal. That is the state #1420 already records, now with the runner out of `dist` | **Chosen** (*Scope* item 4) |
| Keep the seven watched roots, with `docs/` classified as staying home | Contract rule 11 says installed agents open `docs/` at the plugin's root, so a release that changes only `docs/` reaches nobody, which is this issue's defect in a second root. The issue's second Done-when line names every root `dist` holds | Rejected |
| Derive the watched set in the step itself, from `git archive` of the base and of HEAD | The step gains a shell pipeline that only a run of bash in a fixture repository could test, and the suite avoids spawning shell tools since it runs on `windows-latest` (the test module's docstring). It would also ask a version move for a top-level file nothing installed reads | Rejected |
| Keep `SHIPS` and `STAYS_HOME` and add `docs` by hand | A third hand list beside `.gitattributes` and the pattern. Every one of the four places the issue counts already agreed with the others and disagreed with `dist`, because none was read from the archive | Rejected: the structure is replaced |
| Watch `assets/` too, as the first frame at `2e99c1ad6` did | A change to a drawing alone would move the version, though nothing installed reads `assets/` (`frame/design.md` *Grounding*). That is the reverse of the rule *Rule changes* item 1 writes for what `dist` holds unread. Proposed by the orchestrator against #1571 and agreed | Rejected |
| Mark `assets/` `export-ignore` | `README.md:175` and `README.ko.md:178` show `assets/seals/owl.png`, so the image would break wherever `dist` is rendered. Also, #1535 took out of `dist` only the files of a type the directory refuses, and a PNG is not one | Rejected |
| **The pattern lists every top-level directory the archive holds that an installed copy reads. The case derives the archive's directories and requires each to be watched or named in the set of entries held and read by nothing installed, where `assets` stands** | A new top-level file or directory an installed loader reads needs a person to decide it (*Technical context*), and a wrong entry in the set is review's to catch | **Chosen** (*Scope* items 8-9) |
| Pin "no shipped file loads `.github/`" by the archive alone (no path under `.github/`) | Installed copies come from `main`'s whole tree, so a shipped file that loads a `.github/` script works for users and passes the version check unwatched. The defect would return with nothing red | Rejected |
| Pin it by the literal paths handed to `sibling.load` | That misses `chain_check.py#CHECK_LINES_READER` and `seal.py#TOOLS`, two of the three loads this issue names (*Grounding*, the constants probe) | Rejected |
| **Pin it by every non-docstring string constant of a shipped `.py`, plus the archive holding no `.github/` path** | A shipped message that has to name a release script's path would be refused. No such message stands at `036e7d424` (the constants probe), and one that appears is a decision for review | **Chosen** (*Scope* item 10) |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1, 2, the `tests/lib/test_closing.py` part of item 5, item 6 for the closer's row, and item 11 for the closer's citations | The narrow modules: `tests/lib/test_closing.py`, `tests/github/test_close_issues_on_release.py`, `tests/github/test_issue_claims_check.py`, `tests/github/test_label_merged_on_release_branch.py`, `tests/github/test_publish_release_note.py`, `tests/github/test_release_completeness_check.py`, `tests/skills/test_pr_body.py`, `tests/skills/test_chain_check.py::Test_carried_by`, `tests/behaviour/test_every_entry_point_runs_at_the_floor.py`; the definitions search of `frame/design.md` *User scenarios* row 5; `bin/seal layout --moved 036e7d424` over the moved classes, or mutants in the phase record | d46e06d95 |
| 2 | *Scope* items 3, 4, the rest of item 5, item 6 for the moved rows, and item 11 for every other path | `tests/skills/test_rules.py`, `tests/test_run_tests.py`, the case of `tests/skills/test_seal.py` that holds `TOOLS` (`:3465`), the cases of `tests/skills/test_chain_check.py` that name the reader (`:1815`, `:1971`, `:1980`), `tests/behaviour/test_release_hygiene.py`, `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py`, `tests/behaviour/test_every_entry_point_runs_at_the_floor.py`, `tests/text/test_every_agent_reads_the_contract.py`; `bin/seal rules --check` exit 0; both searches of `frame/design.md` *User scenarios* row 4; `bin/seal layout --moved` over the moved files | |
| 3 | *Scope* items 7, 8, 9, 10, 12 | `tests/behaviour/test_the_release_check_watches_what_ships.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/github/test_dist_branch.py`; each new case seen red as `frame/design.md` *User scenarios* rows 2-4 state; `git archive HEAD \| tar -t \| grep '^\.github'` prints nothing | |

## Overlap with the release

The spawn names eleven other items of the release, none branched yet, and says they run one after another after this one merges. So this item merges first in every row, and each row names the new path the later framer reads.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1572 | `.github/scripts/close_issues_on_release.py` (its `:228` error-text test, which stays there, about 100 lines higher once the readers leave) and `tests/behaviour/test_a_cited_section_stands_in_its_file.py` (A7 and A8 here; `NEAR_CITATION` at `:1217` there) | #1571 | The spawn's order. #1572's coordinates in both files shift, and its framer reads them at the merged tree |
| #1573 | `.github/scripts/close_issues_on_release.py#run` and its `gitcmd`, which stay in the closer here. `label_merged_on_release_branch.py` and `release_completeness_check.py` keep loading the closer for them. `chain_check.py` and `seal.py`, whose runners #1573 rewrites, change here at `CHECK_LINES_READER`, `SQUASH_SUBJECT` and `TOOLS["rules"]` | #1571 | This item moves only readers, so #1573's runner work lands on a closer that holds release acts alone. `lib/closing.py` is a new `lib/` module that runs nothing |
| #1574 | `skills/code-review/scripts/chain_check.py` (here `:172`, `:237` and the messages; there `:657`) | #1571 | Different units of one file. `lib/closing.py` holds no table-row splitter |
| #1575 | `.github/scripts/run_tests.py:97-132` and `:587-594`, and `tests/github/test_run_tests.py`, which move to `tests/run_tests.py` and `tests/test_run_tests.py` here. Also `seal.py` (here `TOOLS`; there `:133`, `:401-432` and others) and `pr_body.py` (here `:172-193`, `:318-322`; there `:323-338`) | #1571 | #1575's framer reads the moved paths. Its pins and UTF-8 loop move unchanged |
| #1576 | `.github/scripts/tracker_labels.py`, whose `.gitattributes` line goes here in the one `/.github/` line, and `.github/workflows/hygiene.yml` (here `:88` and the rules step; there the `seal unverified` reference) | #1571 | After this merges, #1576 removes the script with no `.gitattributes` edit |
| #1579 | `skills/writing-style/SKILL.md:267`, one check line re-pointed here, if #1579's set of per-spawn files includes that skill | #1571 | A one-path edit, so its framer reads the merged line |
| #1581 | `tests/skills/test_chain_check.py`, whose reader messages at `:1815`, `:1971` and `:1980` change here | #1571 | #1581 splits or speeds the module, and it reads the merged cases |

No file this work changes is named by #1577 (`broad_gate.py`'s cmd.exe model, which reads the `Broad gate` string and not `bin/test`'s content), #1578 (`lib/optin.py` and the root's spellings), #1580 (tests copying facts, with no file of this work named in its body) or #1582 (the stamp's sprite). Each was read by its body's file names, and none meets this work.

## Operational impact

- **Version.** This work item is the first pull request into `release/v0.38.6`, so phase 3's crafter moves `.claude-plugin/plugin.json` from `0.38.5` to `0.38.6` in the commit that adds `changelog.md` (`docs/releasing/branch-and-release.md` *Cutting a release*).
- **A release that changes only `docs/` now moves the version.** Every pull request into `main` in the last sixty was a release branch (*Grounding*), and a release moves the version in its first pull request, so no correct pull request is newly refused. The change blocks more, and a wrong deny here is a release that forgot its version move.
- **No command changes for a user.** `seal rules`, `seal pr-body` and `chain-check` keep their arguments, output and exit codes. A user's installed copy updates with the version move.
- **`dist` changes.** `dist` loses `.github/` whole, the GitHub templates among it, and `tests/run_tests.py` never enters it. The plugin directory's listing is on hold, and no shipped file names the templates (*Grounding*).
- No new dependency, environment variable or migration.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
