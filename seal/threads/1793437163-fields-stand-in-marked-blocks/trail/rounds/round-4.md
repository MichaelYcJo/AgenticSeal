# Review round 4: 1793437163-fields-stand-in-marked-blocks

```seal
target: f885a3d9 against origin/release/v0.27.0
```

This round has two jobs. First, it answers round 3's two closes, `fixed b36c5d9e` and `fixed 8361d53a`, and the fix pass's extra commit `56f89f48`. The fix range is `38e6b964..f54a414f`. Second, it reviews phase 4, `f54a414f..a739cfa0`: the YAML splits in `946eedc6`, the changelog fragment in `5bc3f357`, and the phase records in `8f5b7508` and `a739cfa0`. It also reads the orchestrator's records commit `f885a3d9`, which closes a row of `gaps.md`. The work was done in a `git clone --no-local` under the session scratchpad at `f885a3d9`. The `v0.26.0` tag and `origin/release/v0.27.0` were fetched into the clone, and a `v0.26.0` worktree beside it served only to load that release's check.

Facts carried from round 3 without searching again: `command_forms` stands at `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:168-190`, and the only shipped line that invokes a script with no subcommand is `agents/proofer.md:57`. Every verdict below was reached again at `f885a3d9`. No `seal/parity.md` exists, so the round block holds no `original:` line.

## Findings

### 1. The changelog fragment does not tell a person that a `hygiene.yml` pinned to `v0.26.0` refuses every record the 0.27.0 agents write

```seal
severity: should
location: `seal/threads/1793437163-fields-stand-in-marked-blocks/changelog.md:12`
evidence: executed `bin/test tests/github/test_tmp_round4.py -q -s -p no:xdist`
```

Why it matters: in a user's repository, the pull-request check is not the installed plugin's. `seal pr-checks install` writes `.github/workflows/hygiene.yml` pinned to the release installed at that moment. The workflow clones the plugin at `v<version>` and runs that clone's `chain_check.py` (`templates/setup/hygiene.yml:8-11`, `:63-67`, `:76-78`). The pin moves only when a person edits it, or removes the file and installs it again. No command moves it on an upgrade.

So a person who upgrades to 0.27.0 and leaves the pin at `v0.26.0` meets a refusal on every pull request that carries a work item. The probe ran `v0.26.0`'s `round_of` over this item's `round-3.md`, a record in blocks. It returned 11 errors, among them "no `target:` line" at line 0, and "no `severity:` line" and "no `location:` line" at the first finding. It ran `v0.26.0`'s `verdicts_of` over a guarantee holding one verdict block, and that returned no verdict line. The other order fails as well: a pin moved to `v0.27.0` before the agents are upgraded refuses the labelled records the 0.26.0 agents still write. This tree's `round_of` refused this item's labelled round 1, as it stood before `aef89462`, with the `NO_ROUND_BLOCK` message alone.

The fragment's **Compatibility** bullet at `changelog.md:12` tells the person what an open work item and a released one meet. It says nothing about the pin, and neither does `frame/plan.md` *Operational impact*, which the bullet was built from. The release note is built from this fragment, and its reader is the person upgrading, so it is where they would learn that the pin and the plugin move together. `docs/the-review-and-parity-arms.md:146-148` already names the same hazard for #988's `original:` line: a pin older than the rule "runs a `chain-check` that reads no `original:` line, until a person moves the pin's `v<version>` to the installed release".

The fix is one more sentence in the **Compatibility** bullet, after the sentence about released work items:

```markdown
A repository whose `.github/workflows/hygiene.yml` pins `v0.26.0` or older runs that release's `chain-check`, which reads no field inside a `seal` block, so every round record and `guarantee.md` the 0.27.0 agents write is refused at the pull request until the pin's `v<version>` reads `v0.27.0`; move the pin in the same change that upgrades the plugin, since a pin moved first refuses the labelled records the older agents write. `seal pr-checks` reports the release a workflow pins.
```

```seal
verdict: fixed 40b53b23
answer: The orchestrator closes this finding, which is located in the work item's records alone. 40b53b23 adds the round's sentence to the **Compatibility** bullet as given, and the same fact to `frame/plan.md` *Operational impact*, answering the round's `## Not judged` row on it. The sentence's last claim was read against the code: `skills/implement/scripts/seal.py#pinned` names the release a workflow's clone line pins, and `seal pr-checks` with no argument reports it and whether it differs from the installed release (`seal.py:1956-1966`).
location: `seal/threads/1793437163-fields-stand-in-marked-blocks/frame/plan.md`
```

### 2. `gaps.md` closes the round 1 rewrite row on a confirmation round 2 does not hold

```seal
severity: should
location: `seal/threads/1793437163-fields-stand-in-marked-blocks/gaps.md:12`
evidence: read `seal/threads/1793437163-fields-stand-in-marked-blocks/gaps.md:12`, `seal/threads/1793437163-fields-stand-in-marked-blocks/trail/rounds/round-2.md:7`, `seal/threads/1793437163-fields-stand-in-marked-blocks/trail/rounds/round-2.md:105-158`, `seal/threads/1793437163-fields-stand-in-marked-blocks/trail/rounds/round-2.md:179`
```

Why it matters: `f885a3d9` closes the row with "round 2 confirmed the rewritten record reads with the same targets and verdicts". Round 2 makes no such confirmation. It lists `aef89462` among the records-only commits of its range (`round-2.md:7`), and none of its confirmation blocks (`:105-158`) is about that rewrite. Its preflight probe (`:179`) shows only that the new reader read round 1 without `NO_ROUND_BLOCK`. That shows the record parses. It does not show that the targets and verdicts match the original. `seal pr-body` copies `gaps.md`'s `## Not verified` into the pull request body, and the sealer reads that row against the rounds as one party's account. A close that cites a confirmation the round does not hold is a disagreement the sealer has to find and weigh.

The claim itself holds, and this round re-derived it (the last confirmation block below). So the fix cites this round:

```markdown
| closed This work item's `trail/rounds/round-1.md` was in labelled lines, and the check refused it with `NO_ROUND_BLOCK` until it was rewritten into blocks | the orchestrator committed the rewrite in aef89462, a commit that touches only that record, after comparing it line by line with the original; round 4 confirmed that it only adds fences and that `v0.26.0`'s check over the original and this tree's over the rewrite read the same target, findings, verdicts and paths |
```

```seal
verdict: fixed 40c77f52
answer: The orchestrator closes this finding, which is located in the work item's records alone; 40c77f52 rewrites the row's answer cell to cite this round's confirmation, as given.
```

## Confirmations

```seal
confirms: round-3#1
```
What holds: the close holds (executed and read). The `evidence:` bullet at `skills/code-review/SKILL.md:141-144` now names `hooks/lib/fields.py` as where the forms of an `evidence:` value stand, and *The record* section holds no "row" or "table" pointing at a grammar. With `SKILL.md` checked out from `38e6b964`, the round-3 record commit before the fix, the new case `test_the_review_skill_sends_a_value_s_form_to_the_module_and_to_no_row` failed. Restored to HEAD, it passes. `git diff --stat 38e6b964 f54a414f` shows the fix pass touched only the two located files, the new case's module, and the round record.

```seal
confirms: round-3#2
```
What holds: the close holds (read and executed). The module docstring at `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:33-41` and the case's docstring now say the exemption holds for a script nobody is told to run without its repo-relative path. The failure message now lives in `no_command_form_message`, which names the third repair: writing the invocation with the script's path. `test_the_no_command_form_message_offers_every_repair_the_reader_accepts` pins each part of that message. `56f89f48` corrects the one more docstring of the same class, the planted-invocation case's. The class search reported by the close was re-run here with `grep` over `tests/`, `agents/`, `skills/` and `templates/` for "nobody is told", "no document tells" and "nobody being told". It found no other statement of the old premise, and the four hits outside this module are about other subjects. The module passes inside the run in *Probes*. A search for spellings is a sample, as the close says.

```seal
confirms: none
```
What matched: *Scope* item 10 holds (executed and read). `broad_gate.py#job_steps` at `skills/verify/scripts/broad_gate.py:2167` and `payload_meter.py#frontmatter` at `skills/verify/scripts/payload_meter.py:250` and `:256` turn CRLF and CR into LF and split at LF alone, which are YAML 1.2's three line breaks. The empty last element of the LF split is harmless. `job_steps` matches each line against `JOB_RE` and `STEP_RE`, and an empty line matches neither. `frontmatter` turns the line ends before `startswith("---")` and `find("\n---", 3)`, so a CR-only file finds its closing line. `git grep -n "exempt from splitlines: YAML"` outside `seal/` lists nothing (exit 1), and `tests/test_censuses.py` passes. With both scripts checked out from `f54a414f`, the two U+2028 cases failed and the four line-end cases passed, as the phase record says. Each line-end case pins the translation against a bare LF split, which is the mutant the phase record names. `uvx ruff check` over the four changed files exits 0. `bin/seal layout --pairs` over them names no pair, and the new `frontmatter` case stands in `Test_measure` beside the module's other `frontmatter` cases.

```seal
confirms: none
```
What matched: apart from finding 1, the fragment tells a person what phases 1 to 3 shipped (read). `### Added` describes the block, its kinds, the near-opener notice and the two templates as `hooks/lib/fields.py` and Table F give them. `### Changed` matches the reader (a finding with no close block is open, and a block inside the fix's fence is refused for lacking its finding block), `seal gate --record`'s append and same-run read-back, `seal pr-body`'s copy, and the instruction files phase 3 changed. Its **Compatibility** bullet says what *Scope* item 9 and *Operational impact* give for an open and a released work item, and the eval sides that stop comparing. `### Fixed` names #1122 as the design's grounding states it. The YAML entry names `seal gate` and `seal payload`, whose scripts call `job_steps` and `frontmatter` (`broad_gate.py:2308-2386`, `payload_meter.py:400`, `:484`), and `seal deferrals`. Each of the three is a key of `skills/implement/scripts/seal.py#TOOLS` (`:128`, `:152`, `:164`). The four `### Process changes` rows each match an instruction change phase 3 made. The crafter's grounds for leaving out *Operational impact*'s third and fourth lines hold for those lines: the third is about this repository's own agents in a window that has closed by the tag, and the fourth is nothing a person meets. *Scope* item 11 holds: `.claude-plugin/plugin.json` reads `0.27.0` at `origin/release/v0.27.0`, and the branch does not change it.

```seal
confirms: none
```
What matched: the substance of `f885a3d9`'s close holds (executed), and finding 2 is only about whom it cites. Against its parent, `aef89462` adds 14 opening and 14 closing fences to `trail/rounds/round-1.md` and removes no line. `v0.26.0`'s `round_of` over the original and this tree's over the rewrite returned no errors on either side. They returned the same target `968f5ac4`, the same three findings closed `fixed e6c81213`, `fixed 3e51b9a1` and `fixed 5d5a1813` with the same paths, and the same held numbers.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck. This round ran narrow module sets and a lint of four files only, and the suite stays `unverified` | the branch at the head the rounds settle on | the orchestrator, by `seal gate --base <base> --record <item>` once the rounds settle |
| The crafter's boundary run of 65 modules and 4143 passes, and its `seal mutate` runs over the two scripts. This round re-ran the U+2028 cases against the old scripts and none of the mutants | `trail/phases/phase-4.md` | the sealer, at the guarantee (contract rule 15) |
| Whether *Operational impact* in `frame/plan.md` should also carry the pin of finding 1. It is the frame's record of the cost, and this round's finding asks only for the note | `frame/plan.md` *Operational impact* | the orchestrator, folding it in place where it judges the frame owes it |
| Round 3's *Not judged* rows on the *Not done* item's home and on an item merged into the base after this pull request opens. This round's range does not answer them | `trail/rounds/round-3.md` *Not judged* | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_broad_gate.py tests/skills/test_payload_meter.py tests/skills/test_chain_check.py -q -k "only_where_yaml or sends_a_value_s_form"` with both scripts checked out from `f54a414f`, then restored | 2 failed (the two U+2028 cases), 4 passed |
| `bin/test tests/skills/test_chain_check.py -q -k sends_a_value_s_form` with `skills/code-review/SKILL.md` checked out from `38e6b964`, then restored | 1 failed |
| `tests/github/test_tmp_round4.py`, one file run once with `-s` and then deleted: a line count and `round_of` of `v0.26.0` and of this tree over `aef89462`'s parent and the rewrite; `v0.26.0`'s `round_of` over this item's `round-3.md`; `v0.26.0`'s `verdicts_of` over a guarantee holding one verdict block; this tree's `round_of` over the labelled round 1 | 14 fence pairs added, none removed, the same reading on both sides; 11 errors over `round-3.md`, the first "no `target:` line"; no verdict line; `NO_ROUND_BLOCK` alone |
| `bin/test` over the 13 modules a `git grep` for `changelog.md`, `payload_meter` and `job_steps` lists under `tests/`, with `tests/test_censuses.py`, `tests/skills/test_chain_check.py`, the script-reach module, `tests/text/test_the_record_is_written_in_words.py`, `tests/text/test_a_record_carries_no_comment.py` and `tests/hooks/test_fields.py`, `-q` | 1454 passed, 11 skipped |
| `uvx ruff check` over the two scripts and their two test modules | exit 0 |
| `bin/seal layout --pairs` over `tests/skills/test_broad_gate.py`, `tests/skills/test_payload_meter.py`, `tests/skills/test_chain_check.py` and the script-reach module | 4 files read, 0 pairs |
| `git grep -n "exempt from splitlines: YAML"` outside `seal/` | no line, exit 1 |
