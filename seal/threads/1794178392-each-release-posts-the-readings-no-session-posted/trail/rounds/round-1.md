# Review round 1: 1794178392-each-release-posts-the-readings-no-session-posted

```seal
target: 9bac36c0 against release/v0.36.0
```

This is the first round, so no earlier round's coordinates were carried; every
fact below was established in this round. The round read `routing.md`, the
three frame files, `gaps.md`, `changelog.md` and `pr.md` whole at `9bac36c0`,
then both phase records, then the diff of the branch against
`origin/release/v0.36.0` (`c7bb14ca`). `seal/parity.md` is not declared, and
`seal/config.md` has no `Record language` row, so the record is in English.

## Findings

### 1. `--work-item .` keys on the string `.` and takes every prompt that holds `./` or ` .`

```seal
severity: should
location: `skills/verify/scripts/session_cost.py:3135`, `tests/skills/test_session_cost.py:5236`
evidence: executed `bin/test tests/skills/test_tmp_1439_round1.py -q -p no:xdist` (probe, deleted); read `skills/verify/scripts/session_cost.py:3114`, `skills/verify/scripts/session_cost.py:3193`
```

Why it matters: *Scope* item 2 of `frame/design.md` says the mode matches
on "the directory's name". `work_item_keys` takes the name as
`os.path.basename(os.path.normpath(directory))`, and for the argument `.`
that is `.` and not the directory's name. `names_key` then matches `.`
wherever the character before it is outside `KEY_EDGE` (`A-Za-z0-9_-`), so
any prompt holding `./bin/test`, `(.` or ` .` counts as naming the work
item. The same holds for `..` given from a subdirectory such as `trail/`.
The probe built a work item, two agent transcripts from another repository
whose prompts were `Run ./bin/test in another repository.` and
`Fix the typo (see README.md) .`, and ran `--work-item . --post` from inside
the work item directory. It exited 0 and posted one comment. The comment
read `2 naming . or feat/12-a-work-item` and carried both rows under
`# agent-x.jsonl` and `# agent-y.jsonl`. With the absolute path, the same
fixture gave `0 naming`. The release checklist step passes
`seal/threads/<id>` paths, so the release step itself is not hit. A person
who runs the command from inside the directory posts other work items' and
other repositories' segment readings into the public log under a sentence
written for this one. No case in `Test_work_item` gives a relative
directory.

The fix takes the name from the absolute path. The docstring already says
"the directory's own name", so no other sentence changes:

```python
    name = os.path.basename(os.path.abspath(directory))
```

The case belongs in `Test_work_item`, beside
`test_a_prompt_naming_neither_whole_is_not_counted`:

```python
    def test_a_relative_directory_is_keyed_by_its_own_name(
        self, monkeypatch, capsys, tmp_path, item
    ):
        """`--work-item .` from inside the directory keys on the directory's
        name. Keyed on `.`, a prompt holding `./bin/test` would name it."""
        self.agent(tmp_path, "agent-x", "Run ./bin/test in another repository.")
        module = _cost()
        self.gh(monkeypatch, module, _listing((42, "OPEN")))
        monkeypatch.chdir(item)
        assert self.main(monkeypatch, tmp_path, module, ".") == 0
        out = capsys.readouterr().out
        assert f"0 naming {self.NAME} or {self.BRANCH}" in out, out
```

### 2. The *A real work item* scenario and the fold row give two transcripts where phase 2's second run found three

```seal
severity: should
location: `seal/threads/1794178392-each-release-posts-the-readings-no-session-posted/frame/design.md:182`, `seal/threads/1794178392-each-release-posts-the-readings-no-session-posted/frame/plan.md:81`
evidence: read `seal/threads/1794178392-each-release-posts-the-readings-no-session-posted/trail/phases/phase-2.md:158`, `seal/threads/1794178392-each-release-posts-the-readings-no-session-posted/trail/phases/phase-2.md:178`; executed `python3 skills/verify/scripts/session_cost.py --work-item seal/threads/1794178392-each-release-posts-the-readings-no-session-posted`
```

Why it matters: the scenario says that at `7e4430b1` the run on this work
item's directory "finds this release's framer and crafter segments". Phase 2
quotes that run, and it found three transcripts: `aa0765332e9340577`
(#1439's framer), `aaca855c2bab4243e` (#1443's framer, whose prompt lists
#1439 as a sibling) and `ab8e8b8952399fc7d` (the crafter). The scenario
leaves out #1443's framer. That framer is the case the phase record names
as the behaviour to know about: a segment of another work item is posted
under the first work item whose command runs. The fold row in
`frame/plan.md` *Judgments of the run* says the scenario was rewritten to
give "the two transcripts each run found", which is also wrong for the
second run. The sealer reads the scenario against the phase record, so it
meets a count that disagrees with the quoted run. This round's own run at
`9bac36c0` found four: the three above and this round's proofer, whose
prompt names the directory.

The scenario's last clause becomes:

```markdown
and the second finds three: this release's framer of #1439, the framer of #1443, whose spawn prompt lists #1439 as a sibling, and this work item's crafter, phases 1 and 2
```

The fold row's clause becomes:

```markdown
the *A real work item* scenario gives the transcripts each run found
```

## Confirmations

What matched: *Scope* item 7. A posted plain reading carries no command
text. `report` prints command text in two places only, the `other` note at
`skills/verify/scripts/session_cost.py:2184` and the `slowest` list at
`skills/verify/scripts/session_cost.py:2192`. Both take `commands`, and
`main` passes `commands=not args.post` at
`skills/verify/scripts/session_cost.py:3554`. A search for every print of
`command`, `ran` and `unnamed` in the module found no third place
(executed, `grep`). The family a `slowest` row now names is a fixed family
name or a tool's name (`family`, `skills/verify/scripts/session_cost.py:731`),
never text from the command. The phase 1 claim that these "are the only
ones in the module that print a command" holds.

What matched: a `--work-item` body carries no command text, no
description and no path. Its rows are built with `"description": ""` and the
transcript's base name (`skills/verify/scripts/session_cost.py:3337`). The
`log_note` that can carry `gh`'s error text is printed only where nothing is
posted: under `--post`, comments that cannot be read exit 1 before the post,
and any other log state reaches `post`, which posts nothing for it. The
probe's posted body for the two-transcript fixture held the counts, the two
`# ` lines and the table, and nothing else (executed, probe).

What matched: the whole-token match does what *Data & interfaces* and the
changelog claim. `fix/12-a` is not found inside `fix/12-a-b`
(`test_a_prompt_naming_neither_whole_is_not_counted`, executed in the module
run). A key may touch `/`, a backtick, a full stop or a space. So the branch
is found inside a worktree path or `origin/<branch>`, and a directory name
inside `seal/threads/<id>/` (read, `skills/verify/scripts/session_cost.py:3114`).
The first user entry of a `fork` agent's transcript is its own directive and
not the parent's history: five fork transcripts on this machine were read, and
the opening of each was a prompt (executed, read-only `python3 -I`).

What matched: the comment reader reads what `emit` writes. The probe posted
a plain reading through `main`, fed the body to `posted_names`, and got
`{'t.jsonl'}`. The same body with CRLF line ends gave the same, because
`lib/blocks.py#gfm_lines` strips `\r\n`. A `--work-item` body, read back as a
comment, named both its transcripts, and a second `--work-item --post` over
that comment posted nothing and exited 0 (executed, probe). `log_comments`
decodes consecutive JSON arrays with `raw_decode`, so it reads `gh api
--paginate` output whether the pages arrive as one array or several
(read, `skills/verify/scripts/session_cost.py:3199`).

What matched: *Scope* items 4 and 5. The four log states end with `post`'s
exit codes and post nothing; a log found whose comments cannot be read exits
1 under `--post` and leaves nothing out without it; the five refused
combinations name both flags. The module's cases for each passed (executed,
`bin/test tests/skills/test_session_cost.py tests/text/test_a_segment_feeds_the_flow_log.py -q`,
289 passed, exit 0).

What matched: *Scope* item 6. `skills/verify/orchestration.md` replaces the
paragraph opening **The command does not make anybody run it.**, drops the
deadline and keeps "never as a question"; step 2 states the `# <file name>`
line. Both READMEs move together: the `seal cost --post` row's `Sends` and
`When` cells and the new `seal cost --work-item <dir>` row say the same in
`README.md` and `README.ko.md` (read, the diff).

What matched: the real reading. Run read-only from the tree's script on this
work item's directory, `--work-item` walked 1,792 transcripts and found the
three phase 2 names plus this round's own proofer, with 0 already in the
log (executed, exit 0).

What matched: each quote in `pr.md` stands word for word, with runs of
whitespace collapsed, at the source its coordinate names: five in
`changelog.md`, one in `frame/plan.md` and one in `gaps.md` (executed,
`python3 -I` comparison).

What matched: each new test covers something its group did not. The five
new `Test_emit` cases pin the `# <file name>` line for the plain reading,
`--spawns`, `--segments` and a resumed file, and the command-free body.
`Test_work_item` is a new class. `bin/seal layout --pairs` prints no pair
for either (executed).

The phases' mutation runs and seen-red runs were read, not re-run.

The `--spawns` description lines that `gaps.md` *Not done* names are
judged here as rightly outside *Scope* item 7. That item and its
*Grounding* row are about command text, and a spawn's `description` is a
label, not a command. The diff does not touch the line
(`skills/verify/scripts/session_cost.py:2433`). `--work-item`, the mode the
release step runs, posts no description. Whether a label may leave the
machine under `CONTRIBUTING.md` *House rules* ("repository contents, paths,
or prompts") is a policy question, and it stands in `## Not judged`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a spawn's `description` label, which the `--spawns` page posts on its `what each cycle spawned` lines, counts as a prompt or as repository contents that `CONTRIBUTING.md` *House rules* keeps off the network. The line predates this branch, and *Scope* item 7 covers command text only | `skills/verify/scripts/session_cost.py:2433`, `gaps.md` *Not done* | the repository owner |
| The full suite, the repository-wide lint and the format check at `9bac36c0`. Contract rule 2 gives them to the orchestrator; `gaps.md` labels them unverified and names the orchestrator, and that label is honest | the branch at `9bac36c0` | the orchestrator, at the broad gate |
| A real `--post` and a real multi-page `gh api --paginate` read against the tracker. This round posted nothing, and every case stubs `run_gh` | `gaps.md` *Not verified*, rows 2 and 4 | the orchestrator, at the 0.36.0 release step |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_1439_round1.py -q -s -p no:xdist` | First run: 3 passed. Its own capture hid two prints, and its `.` fixture's prompts held no `./`. So `names_key` was shown to accept a key followed by `.`, `/` or `+` and to refuse one inside `-b` or after `x` |
| `bin/test tests/skills/test_tmp_1439_round1.py -q -p no:xdist` | Second run, after the probe's own capture was corrected: 2 passed. `--work-item . --post` with prompts `Run ./bin/test ...` and `... README.md) .` posted one comment naming both transcripts under `2 naming . or feat/12-a-work-item`. `posted_names` read `{'t.jsonl'}` from a posted plain body, with LF and with CRLF. A `--work-item` body read back named both transcripts, and a second run over it posted nothing, exit 0. The file was then deleted, and `git status --short` was empty |
| `python3 skills/verify/scripts/session_cost.py --work-item seal/threads/1794178392-each-release-posts-the-readings-no-session-posted` | exit 0; 1,792 walked, 4 naming the work item, 0 already in the log |
| `python3 -I` over the `.meta.json` files under the config directory's `projects/` | 13 `fork` agent transcripts; the first user entry of each of the five read is the fork's own directive |
