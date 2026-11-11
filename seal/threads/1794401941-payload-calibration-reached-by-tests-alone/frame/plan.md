# Implementation Plan: 1794401941-payload-calibration-reached-by-tests-alone

## Technical context

The tree as read at `918342dc0`.

`skills/verify/scripts/payload_meter.py` (1,203 lines) reads a plugin tree and prints one table for the session and one per agent. The composition half, `frontmatter`, `read`, `file_row`, `imports_of`, `user_dir`, `composition`, `pair_rows`, `session_composition` and `agents_in` (`:192-539`), is what `.github/scripts/release_report.py#preloads` and the tests that stay read. The transcript half (`:542-691`), the ratio and delta helpers (`:697-749`, `:902-957`) and the heading split (`:257-318`) are reached only through `--calibrate`, `--baseline` and `--sections` (design *Grounding* G6). `measure` (`:752-899`) and `render` (`:971-1084`) interleave both halves, so the cut runs through those two functions rather than around them.

`release_report.py` loads one meter, this tree's, and reads the tag's tree with it (design G4). So the `sections` parameter leaves `composition` and the one call at `release_report.py:148` loses its `False` in the same commit. The stand-in in `tests/github/test_release_report.py:96-108` takes the same four arguments.

`lib/lines.py:31-34` is one comment that names both `closed_fence_lines` and `payload_meter.py#heading_starts`. Phase 1 drops the second name and phase 2 the first, each where its unit goes.

The failure scenario of the chosen approach, six months on: a person wants the per-agent token figure measured again, as #292 and #329 measured it, for a model change or a preload cut. The meter now only divides bytes by 3.2. They read a spawn's first `usage` block in its subagent transcript and subtract a baseline spawn's by hand, the procedure the removed docstring described. The owner accepted that cost in the decision (design G1).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Remove the three flags the decision lists, and keep `--baseline` with `delta_against` | `--baseline` stays with no document or workflow calling it (design G3), so the first *Done when* line fails. Its ratio lending (`_ratio_from_baseline`, `_carried`, `_same_spawn_over_other_bytes`) keeps reading ratios that only an earlier calibrated run could have written, which is the calibration path under another flag. | Rejected. The issue's own line range and title put `--baseline` inside the cut (design G2). |
| Remove `--calibrate`, `--baseline-agent`, `--baseline` and `--sections`; keep `--root`, `--agent` and `--json`, and name the three in both READMEs' `seal payload` row | The scenario in *Technical context*. A person comparing two trees reads the release report's preload rows, or two `--json` outputs side by side. | Chosen. |
| Remove `--root`, `--agent` and `--json` too, so that no flag stands without a document | A person who measures their own plugin's definitions, which #292 shipped the meter for (`test_an_inline_skills_list_is_read`'s docstring, Q6), loses `--root` and can only measure the plugin's own tree. `tests/behaviour/test_every_shipped_agent_and_document_is_measured.py` reads the real tree through `--json` and is rewritten in process. Both go past the owner's decision, which names what is removed. | Rejected. Naming the three in the README row meets the *Done when* line at the cost of one cell per README. |
| Replace `seal payload` with the release report alone: move `agents_in`, `frontmatter` and `composition` into `release_report.py` or `lib/`, and delete the command | The session table, the `CLAUDE.md` pair with its imports and the core hook's bytes, has no other reader, and the command both READMEs list (`README.md:428`, `README.ko.md:424`) goes. `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py` loads `agents_in` and `frontmatter` from the meter and moves its loader. | Rejected. The premise that keeps the command is the owner's "keep the byte composition", and the command stands in both READMEs (read). |
| Keep `sections` in `composition`'s signature, ignored, so the report's five-argument call stands | A parameter that does nothing, and a docstring reason, the tag's tree loading this meter, that is false at the base (design G4). | Rejected. The call changes in the same commit. |
| Keep the two basis labels as they read | The agents' label says "nothing calibrated" and the session's says "no transcript calibrates a session". Both name a calibration the command no longer has, and a reader looks for the flag. | Rejected. One label for every row, *Scope* item 2. |
| Drop the token column, and print bytes and characters alone | `docs/running/the-agent-set.md` *What a spawn costs*, both READMEs and the help line (`seal.py:154-158`) name tokens, and the owner kept the composition as it reads. | Rejected. Out of scope. |
| Keep *Test_strip_ansi* beside the moved helper | The two cases would test a helper of the test file. The cases that call it, at `test_seal_stamp.py:825` and `:866`, fail when it strips nothing: the first compares lengths with the plain twin, and the second holds the widest line at 80 columns. | Rejected. |
| Keep the rider at `lib/optin.py:85-91` with `parity_config` struck from its count | The count it states is of the commit gate's calls, and #1027 removed that gate (design G10). A rider kept for a gate that is gone sends the next reader to measure nothing. | Rejected. `seal/follow-up.md` has the reader delete a spent rider. |
| Rename `strip_ansi` in the test file, so that `git grep -w strip_ansi` finds nothing | The issue's *Done when* names the move of `strip_ansi` into the tests, so the name in the test file is what that line expects. | Rejected. S4 reads the name in the test file as the move. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Design *Scope* items 1 to 7 | S1, S2, S3, S5, S6 and S7 executed, with the narrow run `bin/test tests/skills/test_payload_meter.py tests/github/test_release_report.py tests/behaviour/test_every_shipped_agent_and_document_is_measured.py tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q`; the suite beyond it `unverified`, answered by the orchestrator's broad gate | `2ec7b9776` |
| 2 | Design *Scope* items 8 to 12 | S4 and S6 executed, with the narrow run `bin/test tests/lib/test_routing.py tests/lib/test_optin.py tests/lib/test_lines.py tests/skills/test_seal_stamp.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q`; the suite beyond it `unverified`, answered by the orchestrator's broad gate | `1e3c11fb7` |

The two phases touch no file in common but `lib/lines.py`, where each edits its own name in the comment at `:31-34`. Phase 2 can start from phase 1's commit or from the base; where it starts from the base, the orchestrator merges the two, never rebases.

## Overlap with the release

The spawn names two open items. #1489's branch was read at `7a2c58b2c`, its frame at that commit, in phase 3 of 8. #1485 has no branch and was read as an issue (executed: `gh issue view 1485`).

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1489 | `tests/skills/test_seal_stamp.py`: this work removes *Test_strip_ansi* and adds the helper; #1489's phase 4 moves the cases of `tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py` that run `seal_stamp.py` into it (read: #1489 design *The files*, the row for that file). `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py` (T1) and `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py` (T3): this work rewrites docstring and comment lines that cite `heading_starts` or `test_payload_meter.py`, and #1489's phase 6 adds a `# No TARGET:` line after each file's imports. `tests/behaviour/test_every_shipped_agent_and_document_is_measured.py` (T1) imports `run` and `write` from `tests/skills/test_payload_meter.py`, whose names this work keeps (design *Scope* item 5). No file of #1489's design *The files* names one of the four flags or the five symbols (#1489 plan, its row for #1484) | #1484 | #1489's plan states the same order. This diff is the smaller and is likelier to be sealed first. Its edits and #1489's land in different hunks of the same files: different cases of `test_seal_stamp.py`, and a docstring against a line after the imports. Whichever merges second keeps both sides. |
| #1485 | The docstrings and comments of `payload_meter.py`, `lib/routing.py`, `lib/optin.py`, `lib/lines.py` and `seal_stamp.py`. Its *Done when* counts lines that carry a `#NNN`, a date, "used to" or "measured", before and after | #1484 | #1485's body says it builds after this item. This work removes the docstring text that stood on the units it cuts, much of it calibration history full of `#292` and "measured", so #1485's before-count, taken after this merge, reads the docstrings that remain. A count taken before this merge would credit #1485 with this work's removals. |

## Operational impact

No migration, environment variable or dependency. `seal payload` refuses `--calibrate`, `--baseline-agent`, `--baseline` and `--sections` with argparse's usage error and exit 2, which is a break for anyone who typed them; no document or workflow names one (design G3). The JSON loses the keys design *Data & interfaces* lists. `release_report.py` prints the same table (S3). This pull request does not move the version: `.claude-plugin/plugin.json` already reads `0.37.4` (read).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
