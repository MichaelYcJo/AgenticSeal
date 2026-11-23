# Implementation Plan: 1795411585-five-checks-block-on-a-reading-guessed-from-words

## Technical context

The tree as read at `22803718e`.

Each coordinate below is `frame/design.md` *Grounding*'s. The release publisher's two readers, `.github/scripts/publish_release_note.py#release_exists` (`:432-446`) and `.github/scripts/close_issues_on_release.py#_issue_api` (`:129-143`), already run `gh` through `lib/gitcmd.py#gh` since #1573, so a `gh` that gave no answer raises `gitcmd.Unrun` before any status is read, and that stays. `gh api -i` prints the status line, the headers, an empty line and the body to stdout, and exits 1 on any status outside 2xx (G10). `lib/closing.py` is the precedent for a `lib/` module that only `.github/scripts/` reads.

`skills/verify/scripts/deferral_check.py` imports only `argparse`, `os`, `re` and `sys`, and reads no file at import, so `session_cost.py` can load it through `lib/sibling.py#load` for `RUNNERS` without the import-time read #1582 removed from `seal_stamp.py`. `session_cost.py#family` searches each family's compiled pattern in order and charges the first that matches (`:745-757`); building the `test` and `lint/type` patterns from `RUNNERS` changes what each matches and not that order.

`pact_check.py`'s token loop is the only caller of `coordinates.py#unquoted` in the file, and `coordinates.py` keeps the function for its own readers. `test_a_cited_section_stands_in_its_file.py` already reports through `warnings.warn`, and pytest prints a warning under `-q` and exits 0 (G12).

Every `## Rule changes` operation of the design was parsed and applied to the policy text in a clone at `22803718e` (executed: `test_tmp_rules.py` and `test_tmp_apply.py` in the framer's scratch directory call `skills/settle/scripts/rule_changes.py#parse` and `#apply_op`; no refusal, and each `from` is found).

The failure scenario of the chosen approach, six months on. A repository whose CI runs its suite through a script no runner word names reads `seal deferrals` at exit 0 with a line saying nothing matched, and a session that reads the exit code alone and skips the line writes `CI covers it` unchecked. The line, the limit it prints and `skills/verify/SKILL.md` *The answerer has to exist* are what stand against that, which is the judgment of the agent that writes the row (`docs/running/what-a-script-gates.md` *The checks*). A second: a later `gh` prints its status line in another shape, `http_answer` reads no status, and `release_exists` stops the publish job. That direction publishes nothing twice and names gh's stderr in the job log.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Release publisher: read the status line of `gh api -i` through one reader, `lib/gitcmd.py#http_answer` | A `gh` that printed no status line stops the run (Technical context) | **Chosen.** The status line is what the HTTP answer carries, as gh prints it (G10), and one reader serves both scripts, as `lib/closing.py` serves the closing keywords |
| Release publisher: keep `gh api` and its stderr match (keeping the structure) | A 403 whose message holds `Not Found`, or a gh that rewords its error line, reads as no release, and a second Release is published at the tag (G8) | Rejected. The premise that would keep it, that gh's error line is a form, does not hold: gh documents no stable wording, and the match reads a word anywhere in the line |
| Release publisher: read the `status` field of the JSON error body, without `-i` | An endpoint whose error body has no `status` field reads every failure as another failure, and one whose field is absent on success needs a second rule | Rejected. The field is the body's, not HTTP's; the probe saw it on one endpoint (G10) |
| Release publisher: each script parses its own `-i` answer | Two copies of one parse drift, and a fix lands in one | Rejected (`skills/core/SKILL.md` *The rule a mechanism is kept against*: a fact has one source) |
| Release publisher: `publish_release_note.py` loads `close_issues_on_release.py` for its `_issue_api` parse | The publisher's run depends on the closer's import, its `lib/closing.py` load among it, for one parse | Rejected. `lib/gitcmd.py` already owns the `gh` run both make |
| `seal deferrals`: report and exit 0 on whatever it read | Technical context's first scenario | **Chosen.** The issue's direction, and the core's: a guessed reading is reported, never used to block |
| `seal deferrals`: keep exit 1 and reword `skills/verify/SKILL.md` to call it a guess | A session reads exit 1 as "the row is not true" anyway, as the skill read it until now, and a CI that runs its suite through a script keeps refusing a true row | Rejected. *Done when* asks that no reading guessed from words exits non-zero |
| `seal deferrals`: retire the command and send the agent to open each workflow (replacing the structure) | A repository with many workflows costs the agent one read per file where one call names the files that matter | Rejected. The premise that keeps the command, checked: `skills/verify/SKILL.md:212-218` sends a session to it before every row that defers to CI, and the report names the matching files and lines in one call |
| `seal deferrals`: drop the runner words and print every command line of every CI file | The report of a repository with many steps is every step, and the local-only and no-match outcomes are lost | Rejected. The words still help a reader find the line, which is the issue's ground for a report |
| One runner list in `deferral_check.py#RUNNERS`, loaded by `session_cost.py` | A later edit makes `deferral_check.py` read a file at import, and `session_cost.py` inherits it, as `broad_gate.py` inherited `seal_stamp.py`'s sprite read (#1582) | **Chosen.** The comment over `RUNNERS` names its second reader. The list's command already owns the fact, and no new shipped module or test file is needed for one constant |
| One runner list in a new `lib/runners.py` | A shipped module and its test file exist for one constant, which each script's cases already pin | Rejected on cost; it would be the right home if a third reader appeared |
| Two runner lists kept (keeping the structure) | A runner added to one list is missed by the other, as G7 lists today in both directions | Rejected. The premise that would keep them, that the two read different facts, does not hold: both ask which command words run a kind of check |
| `seal pact`: remove the token reading | A signer that never settled a 0.23.x frame reads that frame as citing nothing, and its `READ` line counts no anchor there without naming the token | **Chosen.** No release since `v0.24.0` reads the inline anchor, and frames leave at the settle (G4). The `READ` line's count is what shows the person a frame citing nothing |
| `seal pact`: keep the token pattern as a `NOT READ` line in no exit class | The pattern stays a guess over prose, `pact:x` anywhere, kept for a form no release writes | Rejected. The core names a line as not read where it looks like one of the form's lines, and a token in prose is not a line of the anchor table |
| Near-miss citations: warn and pass | A warning in the suite's summary is not read, and a near miss stands | **Chosen.** The issue's direction; the module's other two reports take the same channel (G11), and the proofer reads prose for meaning |
| Near-miss citations: remove the reader | A citation written `Contract Rule 99` is read by no case at all, since `CITATION` does not read it as a citation | Rejected. The reading still helps the reader find a citation the dangling check cannot see |
| Batch sweep: remove it | A definition later tells an agent to collect a person's answers, and no case reads it | **Chosen.** No definition holds a batch phrase (G13), the sweep's own comments record its false refusals, and `test_waiver_decided_at_start.py` holds the measured instance exactly |
| Batch sweep: turn it into a warning | A report over a phrase the tree does not hold, which keeps every constant and its case | Rejected. The issue's direction removes it, and a report that can only fire on new text is the proofer's reading of that text |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* item 1 | `bin/test -q tests/lib/test_gitcmd.py tests/github/test_publish_release_note.py tests/github/test_close_issues_on_release.py tests/github/test_label_merged_on_release_branch.py tests/github/test_release_completeness_check.py` passes; S2's cases are each seen red against `22803718e`, and S1, S3 and S4 hold; search 4 prints nothing | |
| 2 | `frame/design.md` *Scope* items 2, 3 and 4 | `bin/test -q tests/skills/test_deferral_check.py tests/skills/test_session_cost.py tests/skills/test_payload_meter.py` passes; S5's case and S6's two cases are each seen red against `22803718e`; search 5 prints nothing | |
| 3 | `frame/design.md` *Scope* item 5 | `bin/test -q tests/skills/test_pact_check.py tests/skills/test_coordinates.py` passes; S7's case is seen red against `22803718e`; searches 1 and 2 print what S10 states | |
| 4 | `frame/design.md` *Scope* items 6, 7 and 8 | `bin/test -q tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_waiver_decided_at_start.py tests/test_censuses.py` passes; S8's case is seen red against `22803718e`; search 3 prints nothing | |

The searches are `frame/design.md` *User scenarios & acceptance*'s. The broad gate is the orchestrator's, after the rounds settle (contract rule 2); every phase hands over the suite as `unverified`.

## Overlap with the release

The spawn names #1574 and #1576. #1574's frame was read at its branch's head, `9603d3fed`, with its diff against `74ba63423`; its branch log closes its three phases and round 1's findings, and commits its broad gate's record (executed: `git log 74ba63423..fix/1574-lib-routing-splits-a-row-on-an-escaped-pipe`). #1576's frame was read at its branch's head, `24aee6a21`, with its diff against `74ba63423`; its phase 1 is closed at `7403ea0bc`. Neither item adds a check that reads the whole tree, and neither does this one: the near-miss warning reads the tree and blocks nothing.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1574, one row splitter and one line split in `lib/` | `skills/verify/scripts/pact_check.py`: #1574 changes `#near_headers` and `#first_table` at `:330-365`; this work removes `:57-61`, `:117`, `:241-278` and `:813-816`. `tests/skills/test_pact_check.py`: #1574 parametrizes `test_grades_the_exact_table_and_names_a_near_one_beside_it` (`:956-974`) and adds a row and an id to the second-table cases (`:1026-1093`); this work rewrites `test_refuses_the_inline_anchor_naming_the_row_to_write` (`:975-1007`), the case between them | #1574 | Its phases and its round 1 are closed and its broad run is recorded, so it is likelier to be sealed first. The test file's hunks touch adjacent cases, so any textual conflict falls in this item's merge of the base, inside the broad run it takes anyway |
| #1576, code, comments and tests stand on facts that no longer hold | `.github/scripts/close_issues_on_release.py`: #1576's closed phase 1 rewrote the comment over `SPENT_ON_CLOSE` (`:180-185`); this work's phase 1 rewrites `#_issue_api` (`:129-143`). `tests/github/test_close_issues_on_release.py`: #1576 removes the `Tracker` double's label arms (`:180-230`) and the `import json` at `:53`, which only those arms use; this work's phase 1 rewrites `Test__issue_api` and `_gh_answers` (`:451-475`), and a case that builds a JSON body needs that import. `tests/behaviour/test_chain_hooks_hardening.py`: #1576's phase 5 removes the cases at `:215` and `:299`; this work's phase 4 removes `:568-935` | #1576 | Its phase 1 is closed and it was framed first. The hunks are apart in each file. The one point both touch is the `json` import: git merges its removal and a new use without a conflict, and the suite then fails on the name, so whichever merges second keeps `import json` where its cases use it. That falls in its merge of the base, inside the broad run it takes anyway |

## Operational impact

No migration, environment variable or dependency. `.claude-plugin/plugin.json` reads `0.38.6` on the release branch already, so this pull request moves no version. `seal deferrals` exits 0 where it exited 1; nothing in the tree reads its exit code (design search 5 and G6). The release publisher stops on one answer it read as no release before, a status other than 404 whose stderr held `Not Found` or `404`. `session_cost.py` charges the commands the union adds to `test` and `lint/type`, so a reading of a transcript that ran them moves between families against an earlier release's reading. A signer's frame holding a `pact:` token is no longer refused. The build's last phase writes `changelog.md` (design *Scope* item 8).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
