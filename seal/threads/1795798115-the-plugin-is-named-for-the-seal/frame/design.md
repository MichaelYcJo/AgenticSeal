# Design: 1795798115-the-plugin-is-named-for-the-seal

## Grounding

The tree as read at `e904fbce`.

Each row is labelled `executed` where a command gave the fact and `read` where a file was opened. The framer ran no check of the repository's.

| Policy clause | What it fixes for this work |
|---|---|
| G1. #1651's body, as `gh issue view 1651 --json title,body,comments` printed it on 2026-11-27, and `gh issue view 1651 --json comments,state,milestone` on 2026-11-28: no comment, state `OPEN`, milestone `release: 0.40.0` (`executed`) | The issue is the source for what this work item is. Its table *The names* gives each rename, its *How the repositories move* rules out a shipped migration, and its *Order* puts CodeChallenge and owlery after the release. The orchestrator's line on the comments is that the issue has none, and the second command agrees |
| G2. `skills/core/SKILL.md` *The rule a mechanism is kept against*: a script holds a gate only on a line of the plugin's own forms in the one spelling the form gives it, and no script carries a list of the spellings a label is written in (`read`) | No reader accepts the old and the new spelling side by side. Each form in *Data & interfaces* has one spelling after this work |
| G3. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*: a work item whose subject is the policy root's own text edits the policy root directly (`read`) | This work rewrites the vocabulary of the policy documents, and a document left for the settle would cite files that no longer exist. The work edits `docs/` directly, and `## Rule changes` holds the no-change block. `seal/threads/` holds no other work item at `e904fbce` (`executed`: `ls seal/threads/`), so no unsettled design is re-pointed |
| G4. `lib/optin.py#home_at`, `#home_paths`, `#home_name_in`, `#HOME`, `#SECOND_HOME`, `#MARKER` (`read`) | The root is found by name and marker at three places. This work renames `HOME` and `MARKER` and removes `SECOND_HOME` and the second place |
| G5. `lib/fields.py#INFO`, `#SEALER_VERDICT`, `#SEALED`, `#WITHHELD`, `#UNDECIDED`, `#VERDICT_BLOCK` (`read`) | The block fence is the info string `seal`, and the verdict value reads `sealed`, `withheld reason: <reason>` or `undecided question: <question>`. `#verdict_word` takes the first word of the value, so each verdict word is one word |
| G6. `skills/code-review/scripts/chain_check.py#root_name`, `#guarantee`, `#CLOSING_RECORDS`, `#TRAILER`, `#_checked` (`read`) | The check reads the root's name from the marker at HEAD, the declarations from the `routing.md` files the pull request changes under `<root>/threads/`, the final record at `<item>/guarantee.md`, and the trailer `Seal-Routing` of commits that no declaration names |
| G7. `tests/` reads this repository's own root: sixteen lines in eight files join `ROOT` with `"seal"` (`executed`: `git grep -n -E 'ROOT, *"seal"\|ROOT */ *"seal"' e904fbce -- tests`) | A commit whose code names the root `iadd` and whose tree still holds `seal/` fails those cases. The root's name in the code and this repository's own root change in one commit |
| G8. `skills/verify/scripts/broad_gate.py#shipped_gate`, `#gate` lines 1946 to 1962, and `docs/running/the-broad-gate.md` *The gate that measures a tree is the copy that tree ships* (`read`) | A gate found on `PATH` hands its run to the tree's copy at `skills/verify/scripts/broad_gate.py`, and the tree's copy refuses a repository with no root. So the tree's own root has to be the one the tree's code names before the broad run, and that script keeps its path |
| G9. `which seal` on 2026-11-28 printed a path under the installed plugin's cache at release 0.39.3, and this repository's `CLAUDE.md` says an agent spawned here receives the installed plugin's copy (`executed`, `read`) | The agents and the `seal` command of the run are the installed release's. After the commit that moves the root they find no root in this checkout, and the forms they write are the old ones. `frame/plan.md` *Technical context* says how each later step reads the records |
| G10. `.github/workflows/hygiene.yml` lines 117 to 170 run `skills/code-review/scripts/chain_check.py`, `skills/implement/scripts/seal.py mode --check` and `skills/settle/scripts/rules.py --check` from the checkout, and line 181 reads the prefix `seal rules: not read: ` (`executed`: `grep -n` on the file) | This repository's own workflow pins no release. It follows the rename through the lines that name a script's path and that printed prefix |
| G11. `templates/setup/hygiene.yml` clones the plugin at `v<version>` into `$RUNNER_TEMP/agentic` and runs `chain_check.py` and `seal.py mode --check`; `skills/implement/scripts/seal.py#PLACEHOLDER` and `#PLUGIN_CLONE` hold the placeholder and the clone address (`read`) | The template follows through its clone directory and its script path. The placeholder and the clone address stay, since the repository keeps its name |
| G12. `skills/code-review/scripts/pr_body.py#MARK_KEY`, `#MARK_ALT`, `#_mark_line` (`read`) | The pull request's mark is the plugin's icon at `<repository>/raw/HEAD/<icon>`, written where the key `Pull request seal mark` reads `yes`. The address names no path that this work renames |
| G13. `docs/layout/one-root-by-lifetime.md` *Naming*, and *이름* in its `.ko.md` edition (`read`) | The policy root already holds the names and each one's sentence. The definition takes that section, so the names have one home |
| G14. `skills/writing-style/SKILL.md` *용어는 실물을 확인하고 고른다* and *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* (`read`) | A Korean name is chosen after opening what it names, avoids a word whose other sense comes first, and is the one word for its thing |
| G15. The Korean documents use `검사` for a check, `검증` for the verify skill, `승인` for an approval and `통과` for a check that passes; they hold no `검수`, `합격` or `효력` (`executed`: `git grep -c -F` for each word over `README.ko.md`, `docs/**/*.ko.md` and `skills/writing-style/*.md`) | `검사`, `검증`, `승인` and `통과` each fail the one-reading rule as a name for the inspection. `검수`, `합격` and `효력` are free |
| G16. `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` and `README.md` line 8 hold one description sentence, which names the proofer's step with the word `inspect` (`executed`: `git grep -n -i inspect`) | The word `inspector` is new, but `inspect` is not. The description sentence is rewritten so that `inspect` names the inspector's step alone |
| G17. `evals/behaviour/proofer/replay-*` and `evals/behaviour/proofer/seeded-*` fetch commits of this repository by SHA and name paths inside those trees, such as `seal/threads/<id>/trail/rounds/round-N.md` (`executed`: `git grep -h -o` over those directories; `read`: one `scaffold.sh`) | Those paths are claims about named commits and stay. The agent type those cases name changes with the plugin |
| G18. `seal/follow-up.md` (`read`) | No row waits on this work. Its rows name commands, files and verdict words of the plugin, which Scope items 2 to 7 rename in place |
| G19. The note of release `v0.39.3`, its `### Process changes` table (`executed`: `gh release view v0.39.3 --json body`); `gh release view` on 2026-11-28 named `v0.39.4`, whose note holds no such heading | The last process changes concern the orchestrator's drain, its judgment rows and `agents/sealer.md` step 1's listing command. None decides a name |
| G20. Searches A1 to A9 of *Data & interfaces*, run at `e904fbce` with the work item's directory excluded as `:!seal/threads/1795798115-the-plugin-is-named-for-the-seal` (`executed`) | A1 printed 606 lines in 111 files, A2 363 lines in 75 files, A3 1340 lines in 204 files, A4 1802 lines in 234 files, A5 4539 lines in 309 files, A6 306 lines in 79 files, A7 221 lines, A8 1137 lines in 154 files and A9 183 lines in 23 files. Each printed line is one that a Scope item from 1 to 7 renames or removes. The lines the design keeps are the ones each search excludes by pathspec or by its filter, named under the search |
| G22. `git grep -n -e '^## Naming' -e '^## 이름' e904fbce -- docs/layout` printed `docs/layout/one-root-by-lifetime.md:190` and `docs/layout/one-root-by-lifetime.ko.md:181` (`executed`) | Both lines are the headings the *Naming* row of `## Removes` takes out, so phase 8's search prints nothing once that phase has closed |
| G21. `seal/parity.json` is absent (`executed`: `ls seal/`) | No original stands between the ticket and the code |

## Scope

The plugin takes IADD's names. Nothing the chain does changes: the parties, their order, what each reads and writes, and what each check refuses stay as they are at `e904fbce`, except items 1 and 4's states.

In scope, by number:

1. **The fallback root goes.** `lib/optin.py#SECOND_HOME`, `home_name_in` and the second place of `home_paths` and `home_at` are removed, with each case and each sentence that states them. A repository whose own directory takes the root's name keeps its root in local mode.
2. **The final party is the inspector.** `agents/sealer.md` becomes `agents/inspector.md`, and the word `sealer` becomes `inspector` in every agent reference, identifier, file name and text, `evals/behaviour/sealer/` and the test files named for the sealer among them.
3. **The final record is the inspection.** `guarantee.md` becomes `inspection.md`, with its template, its form document, the verdict line for `cleared`, the flags `--sealing` and `--guarantee`, and the named checks, each as *Data & interfaces* *Formats a script reads exactly* gives it.
4. **The act, its states and its mark take the inspection's words.** Where a text or an identifier says *seal*, *sealed* or *guarantee* for the final party's act, record or verdict, it says *inspection*, *cleared* or *inspect*, as *The words* gives them. The three states of a work item's inspection, cleared, lapsed and not cleared, are stated once in the form document, and the messages of `chain_check.py`, `pr_body.py` and the stamp use those words where they describe one of the states. The stamp, the mark, the two config keys and the release's mark take the names *Formats a script reads exactly* gives.
5. **The plugin is `iadd`.** The product name AgenticSeal becomes IADD, the plugin, the marketplace and every agent and skill prefix become `iadd`, and each identifier, environment variable, file and directory named `agentic` takes `iadd`. The `renames` entry of `.claude-plugin/marketplace.json` is removed. The description sentence becomes the one *Data & interfaces* gives.
6. **The command is `iadd`.** `bin/seal` and `bin/seal.cmd` become `bin/iadd` and `bin/iadd.cmd`, the dispatcher becomes `skills/implement/scripts/iadd.py`, and every `seal <subcommand>` a text or a message names becomes `iadd <subcommand>`.
7. **The root is `iadd/`.** `lib/optin.py#HOME` and `#MARKER`, the root's README template, the local-mode root, the trailer, the block fence and `templates/setup/hygiene.yml` take the values *Formats a script reads exactly* gives. In the same commit this repository's own `seal/` moves to `iadd/`, the work item's directory with it, and `iadd/README.md` is written from the renamed template.
8. **The IADD definition is written in `docs/method/iadd.md`**, as *The definition* gives its sections, from this repository's own sources. `docs/README.md` gains the group `docs/method/`. The *Naming* section of `docs/layout/one-root-by-lifetime.md` and its `.ko.md` edition moves into the definition's *The names*.
9. **The Korean documents take the Korean names** of *The Korean names*, in `README.ko.md` and `docs/**/*.ko.md`, in the phase that renames the English word.
10. **The version moves, and the changelog fragment is written.** The last phase moves `.claude-plugin/plugin.json`'s `version` in the commit that adds `changelog.md`, and runs searches A1 to A9.

Out of scope:

- **Moving CodeChallenge and owlery.** #1651 *How the repositories move* and *Order* put them after the release, each in its own commit with its pinned check.
- **Renaming the repository `MichaelYcJo/AgenticSeal`.** #1651 *After this issue* weighs it later. Every address that holds `MichaelYcJo/AgenticSeal` stays.
- **A shipped migration.** No `iadd migrate` command, no `renames` entry and no notice in the old plugin, as #1651 *How the repositories move* decides.
- **Committed trailers.** No commit is rewritten. `skills/settle/SKILL.md` names `Seal-Routing:` as the form of commits before the release that carries this work.
- **`docs/experiments/`.** Its documents are dated and are no policy. A citation there that a check of the repository reads is updated where the check fails, and nothing else in the group changes.
- **The drawings.** `assets/seals/` keeps its path and its words for the drawings. A line of `assets/seals/README.md` that names a script, a command or a key this work renames follows the rename. The phrases *wax seal*, *seal drawings* and *seal maker* stay where they describe the picture or the proofer's etymology. They name a drawing and a craft, not the plugin's record.
- **Paths inside replayed commits.** G17's paths stay as the named commits hold them.
- **Publishing the release, and opening the issue that holds the comparison with Owlery's definition.** #1651 *Done when* names both. The release is the release pull request's act, and an agent posts nothing, so the issue is the orchestrator's or the owner's to open.

This frame was drawn without reading MichaelYcJo/owlery#322. The independence #1651 asks of the definition is held by Scope item 8: each principle cites its source in this repository.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| The root is found under its new name alone | Given a repository whose `iadd/README.md` opens with `# What IADD keeps in iadd/`. When `iadd mode` runs. Then it names that directory as the root. A `seal/` whose README opens with the old marker, and a marked `agentic-seal/`, are no root | the cases of `tests/lib/test_optin.py` |
| A cleared inspection passes the ready pull request | Given a work item whose `inspection.md` ends in an `iadd` block holding `target: <sha> against <base>` and `Verdict: cleared` at HEAD. When `chain_check.py` runs for a ready pull request. Then the inspection arm refuses nothing. A block reading `Verdict: sealed` is refused at its line as a value that does not read whole | the cases of `tests/skills/test_chain_check.py` for the inspection arm |
| The three states read one way | Given the newest verdict block. Then the work item is cleared where it reads `cleared` at HEAD or at a commit that only the closing records follow, lapsed where it reads `cleared` and another path follows its commit, and not cleared in every other case | `docs/forms/the-inspection.md` states them once, and the cases of `tests/skills/test_chain_check.py` and `tests/skills/test_pr_body.py` pin the message for each |
| This repository holds `iadd/` and no `seal/` | When the last phase has closed. Then `git ls-tree HEAD -- seal` prints nothing, `git ls-tree HEAD -- iadd` prints one tree, and `bin/iadd mode --check` exits 0 | those three commands at HEAD |
| The party's old name is gone | When the last phase has closed | search A1 prints nothing |
| The record's old forms are gone | When the last phase has closed | search A2 prints nothing |
| The plugin's old identity is gone | When the last phase has closed | search A3 prints nothing. The lines it excludes are those holding `MichaelYcJo/AgenticSeal`, and `LICENSE`, which questions row Q1 holds |
| The old root, command, trailer and fence are gone | When the last phase has closed | search A4 prints the lines of `skills/settle/SKILL.md` that name `Seal-Routing:` as the trailer of commits before this release, and no other line |
| The word for the artifact is gone | When the last phase has closed | searches A5, A6, A7, A8 and A9 print nothing, except that A5 prints the lines of `tests/skills/test_chain_check.py` that hold the old verdict word as a near miss the check refuses, the lines of `tests/text/test_the_record_is_written_in_words.py` that hold an old line its check refuses, and the lines of `evals/scripts/noninferiority.py` and `tests/evals/test_noninferiority.py` that name the eval harness's `sealed` directory. A5's filter leaves out the lines that hold *wax seal*, *seal maker*, *seal drawings*, `Seal-Routing` or `assets/seals` |
| The definition is indexed and stands on this repository's sources | When phase 8 has closed. Then `docs/method/iadd.md` holds the four sections of *The definition*, `docs/README.md` names the group and the file, and each principle cites its source as a backticked path and an italic heading | `bin/iadd fold` and `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, which the broad run takes; the proofer reads each principle against the section it cites |
| The version is the release's | When the last phase has closed. Then `.claude-plugin/plugin.json`'s `version` is the version #1651's milestone names | `gh issue view 1651 --json milestone --jq .milestone.title` beside `python3 -c 'import json; print(json.load(open(".claude-plugin/plugin.json"))["version"])'` |

## Data & interfaces

### The searches

Each runs at HEAD after the last phase. `W` is `:!iadd/threads/1795798115-the-plugin-is-named-for-the-seal`, the work item's directory, whose records quote the old names. `X` is `:!docs/experiments`. `R` is the two pathspecs `:!evals/behaviour/proofer/replay-*` and `:!evals/behaviour/proofer/seeded-*`.

```
A1  git grep -n -i -e sealer -- . W X
A2  git grep -n -e 'guarantee\.md' -e 'sdd-guarantee' -e 'the-guarantee' -e 'Verdict: sealed' -e '--sealing' -e '--guarantee' -- . W X
A3  git grep -n -i -e agentic -- . W X ':!LICENSE' | grep -v -F 'MichaelYcJo/AgenticSeal'
A4  git grep -n -e 'seal/' -e 'Seal-Routing' -e '```seal' -e 'bin/seal' -e 'seal\.py' -e 'seal\.cmd' -- . W X R
A5  git grep -n -i -w -e seal -e seals -e sealed -e sealing -e unsealed -- . W X R ':!assets/seals' | grep -v -i -E 'wax seal|seal maker|seal drawings|Seal-Routing|assets/seals'
A6  git grep -n -e 'seal_' -e '_seal' -- . W X ':!assets/seals'
A7  git grep -n -i -e 'seal mark' -e 'seal_stamp' -e 'seal-mark' -e 'Seal Test' -e 'release_seal' -e 'SEAL_PNG' -e 'seal\.png' -- . W X
A8  git grep -n -E 'seal (gate|settle|cost|mutate|unverified|deferrals|fold|pact|payload|stamp|layout|rules|pr-body|pr-wait|range|mode|export|import|pr-checks|--help)' -- . W X
A9  git grep -n -F -e 'agentic-seal' -- . W X
```

A7, A8 and A9 each print nothing once the phase that `frame/plan.md` names for it has closed. A8 also matches `unseal mutate`, a made-up word in one case of `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`, which follows the command's name.

A3 hides a line that holds the repository's address and a second use of the old name, and A5 hides a line that holds a kept phrase and a second use of the word. The round that reads the diff reads those lines.

### The words

One sense, one word. The builder reads each occurrence for its sense before it renames it.

| At `e904fbce` | Sense | After |
|---|---|---|
| AgenticSeal; the AgenticSeal process | the product; the method from the routing question to the final verdict | IADD; the IADD process |
| `agentic` | the plugin's identifier | `iadd` |
| sealer | the final party | inspector, *the final inspector* where the text introduces it |
| the seal; the guarantee | the final party's record and its act | the inspection |
| to seal; to guarantee | what the final party does to a commit | to inspect, and to clear where the verdict is meant |
| sealed | the verdict word, and the state it gives | cleared |
| a seal behind HEAD, a stale guarantee | a cleared verdict whose commit another path follows | lapsed |
| no seal, withheld, undecided, no guarantee | every other state | not cleared, with `withheld` and `undecided` kept as verdict words |
| the Seal Test | the verify skill's evidence protocol | the Inspection Test |
| seal mark | the picture a pull request body or a release note carries | inspection mark |
| `seal` | the command | `iadd` |
| `seal/` | the records root | `iadd/` |
| a `seal` block | the fenced block a script reads fields in | an `iadd` block |
| guarantee, in *a platform guarantee* and other plain uses | the ordinary English word | unchanged |
| wax seal, seal drawings, seal maker | the drawing, and the proofer's etymology | unchanged |

The verdict lines are these three, written exactly so:

```
Verdict: cleared
Verdict: withheld reason: <reason>
Verdict: undecided question: <question>
```

The description sentence of `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` and `README.md` is: `IADD, Independent AI-Driven Development: agents frame, build, review and inspect a change, no agent approves its own work, and it ends in an inspection bound to a commit.`

### The Korean names

| English | Korean | Grounds |
|---|---|---|
| inspector | 검수자, and 최종 검수자 for *the final inspector* | 검수 is the inspection of delivered work before it is accepted, which is what the party does. 검사 already names a check (G15) |
| inspection | 검수 | the same word for the act and for the record; the file is named `inspection.md` |
| cleared | 합격 | 통과 already names a check that passes (G15) |
| lapsed | 효력을 잃음 | 실효 is read as either of two words, 失效 and 實效, so the plain phrase is used |
| not cleared | 합격 아님 | it covers a withheld verdict, an undecided one and no inspection, which 불합격 does not |

A Korean document writes the Korean name with the English identifier in parentheses at its first use, as `검수자(inspector)`. The agent type, the file names, the verdict words of a `Verdict:` line and every word a script prints stay English.

### Formats a script reads exactly

Each row is one spelling. No reader accepts the left column after this work.

| Format | At `e904fbce` | After | Read by |
|---|---|---|---|
| the root's directory, shared and local | `seal` | `iadd` | `lib/optin.py#HOME` |
| the second shared root | `agentic-seal` | removed | `lib/optin.py#SECOND_HOME` |
| the marker, the first line of the root's `README.md` | `# What AgenticSeal maintains in seal/` | `# What IADD keeps in iadd/` | `lib/optin.py#MARKER`, pinned to the template by `tests/lib/test_optin.py` |
| the root's README template | `templates/setup/seal-README.md` | `templates/setup/iadd-README.md` | the first setup of `skills/implement/bootstrap.md`, and the dispatcher's install |
| the opt-out file under the common git directory | `agentic-scratch` | `iadd-scratch` | `lib/optin.py#SCRATCH` |
| the commit trailer's key | `Seal-Routing` | `IADD-Routing`, its value `no work item` unchanged | `skills/code-review/scripts/chain_check.py#TRAILER` |
| the block fence's info string | `seal` | `iadd` | `lib/fields.py#INFO` |
| the final record's file | `guarantee.md` | `inspection.md` | `lib/optin.py#GUARANTEE`, which becomes `INSPECTION`, and `chain_check.py#CLOSING_RECORDS` |
| the final record's template and its title line | `templates/records/sdd-guarantee.md`, `# Guarantee: <work-item-id>` | `templates/records/sdd-inspection.md`, `# Inspection: <work-item-id>` | the inspector, step 5 of its definition |
| the first verdict word | `sealed` | `cleared` | `lib/fields.py#SEALED`, which becomes `CLEARED`, in `#VERDICT_BLOCK`'s pattern |
| the key `Verdict:`, and the words `withheld` and `undecided` | as spelled | unchanged | `lib/fields.py#SEALER_VERDICT`, which becomes `INSPECTOR_VERDICT` |
| the check's flag for the run before the verdict | `--sealing` | `--inspecting` | `chain_check.py#INSPECTING` |
| the stamp's flag naming the record | `--guarantee <path>` | `--inspection <path>` | the stamp script |
| the stamp script, its sprite and its title row | `skills/verify/scripts/seal_stamp.py`, `seal-mark.txt`, `SEALED` | `skills/verify/scripts/stamp.py`, `stamp-mark.txt`, `CLEARED` | `hooks/hooks.json`'s `Stop` command, `#SPRITE_PATH`, `#TITLE_ROW` |
| the stamp's two directories under the common git directory | `agentic-stamp`, `agentic-stamp-refused` | `iadd-stamp`, `iadd-stamp-refused` | the stamp script's `#VALUES_DIR` and `#REFUSED_DIR` |
| the mark's alternative text | `Sealed` | `Cleared` | `skills/code-review/scripts/pr_body.py#MARK_ALT` |
| the two config keys of the mark | `Pull request seal mark`, `Release note seal mark` | `Pull request inspection mark`, `Release note inspection mark` | `pr_body.py#MARK_KEY`, the release's mark script, `lib/config.py`, `templates/setup/config.md` |
| the release's mark script, its job, its dry-run variable and its image | `.github/scripts/release_seal.py`, job `seal`, `SEAL_PNG`, `seal.png` | `.github/scripts/release_mark.py`, job `mark`, `MARK_PNG`, `mark.png` | `.github/workflows/publish-release.yml` |
| the command and its dispatcher | `bin/seal`, `bin/seal.cmd`, `skills/implement/scripts/seal.py` | `bin/iadd`, `bin/iadd.cmd`, `skills/implement/scripts/iadd.py` | Claude Code's `PATH` for a plugin's `bin/`, `templates/setup/hygiene.yml`, `.github/workflows/hygiene.yml`, `broad_gate.py#SEAL_SCRIPT` |
| the prefix of a line a command prints | `seal <subcommand>: ` | `iadd <subcommand>: ` | `.github/workflows/hygiene.yml` line 181 reads `seal rules: not read: ` |
| the gate's script | `skills/verify/scripts/broad_gate.py` | unchanged, by G8 | `broad_gate.py#GATE_REL` of an installed copy |
| the plugin's name and display name | `agentic`, `AgenticSeal` | `iadd`, `IADD` | `.claude-plugin/plugin.json`, read by `lib/core.py#manifest` |
| the marketplace's name, its plugin entry and its `renames` map | `agenticseal`, `agentic`, `{"specseal": "agentic"}` | `iadd`, `iadd`, removed | `.claude-plugin/marketplace.json` |
| the agent and skill prefix | `agentic:` | `iadd:` | the harness, from the plugin's name |
| the first line the `SessionStart` hook prints | opens `AgenticSeal core from` | opens `IADD core from` | `lib/core.py`, and this repository's `CLAUDE.md` |
| the gate's variable, the pytest recorder's two variables, and `AGENTIC_INHERITED` | `AGENTIC_GATE_INVOKED_AS`, `AGENTIC_RECORD_DIR`, `AGENTIC_RECORD_KEY` | the same names opening `IADD_` | `broad_gate.py#INVOKED_AS_VAR`, the recorder, `.github/workflows/publish-release.yml` |
| the pytest recorder's module | `skills/verify/scripts/pytest_record/agentic_pytest_record.py`, loaded with `-p agentic_pytest_record` | `iadd_pytest_record.py`, `-p iadd_pytest_record` | `PYTEST_ADDOPTS` in the workflows |
| the export's state file and its archive stem | `agentic-last-export.json`, `seal-repo-` | `iadd-last-export.json`, `iadd-repo-` | the dispatcher's `#STATE` and `#zip_stem` |
| the machine-local maps | `~/.claude/agentic/pact-paths.json`, `~/.claude/agentic/parity-paths.json` | the same files under `~/.claude/iadd/` | the pact check and the parity setup |
| the clone directory of the pull request check's template | `$RUNNER_TEMP/agentic` | `$RUNNER_TEMP/iadd` | `templates/setup/hygiene.yml` |
| the named checks | `ready-needs-sealed`, `refused-sealed-leaves-a-record`, `parity-in-the-guarantee` | `ready-needs-cleared`, `refused-cleared-leaves-a-record`, `parity-in-the-inspection` | the `check:` lines' reader, `skills/settle/scripts/rules.py` |
| the heredoc delimiter of the eval scaffolds | `AGENTIC_EOF` | `IADD_EOF` | each `scaffold.sh` |
| the verify skill's protocol name | *Seal Test* | *Inspection Test* | the texts that cite it |

A file or an identifier named for the seal that this table does not name follows *The words*: `tests/skills/test_seal.py` becomes `tests/skills/test_iadd.py`, `skills/verify/seal-mutate.md` becomes `skills/verify/iadd-mutate.md`, and a test file named for the sealer or the guarantee takes *inspector* or *inspection*.

### The definition

`docs/method/iadd.md` holds four sections. `docs/README.md` names the group's reader: a person who wants to know what IADD is opens it, and so does the owner when this plugin's definition is set beside another tool's. No agent acts on it.

1. **What IADD is.** IADD is Independent AI-Driven Development. Its line is *Zero Self-Approval: no AI approves its own work.* One paragraph says what the method does with one issue.
2. **The principles.** Each is one sentence and the source it stands on, cited and not restated at length:
   - no party approves its own work: `skills/core/SKILL.md` *Each agent judges its own target, independently of the others*, and `docs/running/the-agent-set.md` *The party that draws a contract is not the party that executes it*;
   - judgment where meaning is the question, and a script for the rest: `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*;
   - a judgment stands on a source document and is written down with it: `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both*;
   - the inspection is bound to one commit: `docs/forms/the-inspection.md`;
   - a person is asked once, before the first edit: `skills/core/SKILL.md` *Asking a person is the most expensive step*;
   - four invariants hold the chain: the table of `skills/core/SKILL.md` *Judgment is not licence to skip a party*;
   - a mechanism stays only while what it caught outweighs its cost: `skills/core/SKILL.md` *The rule a mechanism is kept against*;
   - a document is cut by who opens it: `skills/core/SKILL.md` *A document is cut by who opens it and at which step, so a party opens only what its step needs*.
3. **The names.** The table that *Naming* held, for IADD: the product, `iadd`, `iadd/`, `iadd/threads/<id>/`, the agents, the inspection and its three states, the thread, the settle and `IADD-Routing:`, each with its one sentence.
4. **The record forms.** One row per record of a work item, with the document that owns its form: `docs/forms/the-round-record.md`, `docs/forms/the-inspection.md` and `docs/layout/the-record-layout.md`.

## Rule changes

- nothing
  why: This work item's subject is the policy root's own text, the names every document states, so it edits `docs/` directly in its pull request as `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* states, and leaves the settle no decision to gather.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the second shared root, its name and the second place of the root's discovery | `lib/optin.py#SECOND_HOME`, `lib/optin.py#home_paths`, `lib/optin.py#home_name_in`, `lib/optin.py#home_at` | nothing owns it. It existed because `seal` is a common directory name, and #1651 decides `iadd` is not |
| the cases and the sentences that state the second root | `tests/lib/test_optin.py`, and each file search A3 prints for `agentic-seal` at `e904fbce` | they go with the unit they pin |
| the `renames` map | `.claude-plugin/marketplace.json` | nothing owns it. #1651 *How the repositories move* keeps no rename entry |
| the *Naming* section, in both editions | `docs/layout/one-root-by-lifetime.md` *Naming*, `docs/layout/one-root-by-lifetime.ko.md` *이름* | `docs/method/iadd.md` *The names*; the Korean names stand where `README.ko.md` introduces the process |
| the old spelling of each form | each row of *Formats a script reads exactly* | the row's *After* cell. No reader keeps the old spelling, by G2 |
| the files named for the sealer and the guarantee | `agents/sealer.md`, `docs/forms/the-guarantee.md`, `templates/records/sdd-guarantee.md`, `evals/behaviour/sealer/` | `agents/inspector.md`, `docs/forms/the-inspection.md`, `templates/records/sdd-inspection.md`, `evals/behaviour/inspector/` |
| this repository's own `seal/` | `seal/` | `iadd/`, in the commit of Scope item 7 |

This design adds no gate, check, hook, mark or rule. It adds one document, `docs/method/iadd.md`, and one group of the policy root, and takes the *Naming* section out in return.

Framed 2026-11-28 by framer, before the build.
