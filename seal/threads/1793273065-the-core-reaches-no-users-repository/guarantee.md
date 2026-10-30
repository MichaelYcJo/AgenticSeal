# Guarantee: 1793273065-the-core-reaches-no-users-repository

| Field | Value |
|---|---|
| Target SHA | fbb9c018 against 53f21b54; earlier run: 3943873d sealed; earlier run: 0034a171 withheld |
| Broad gate | 11896fae against 53f21b54 |

The base `release/v0.25.0` resolved through `release/v0.25.0@{upstream}` to
`53f21b54` (executed). `trail/gate.md` names `11896fae`, an ancestor of HEAD
(`git merge-base --is-ancestor`, exit 0, executed). `git log --no-merges
--name-only 11896fae..HEAD ^53f21b54` names three commits: `2236c0a8`
(`trail/gate.md`), `0034a171` (`frame/plan.md`) and `fbb9c018` (`gaps.md`).
All three touch only the work item's directory (executed). `bin/seal pr-body
<item> --body <scratchpad>/pr-body-new.md --check` exits 0 at `fbb9c018`:
the body above `## Not from the records` is the records' text (executed).

The committed guarantee sealed the A1 build at `3943873d`, and every commit
since then is audited here. This audit's first pass, at `0034a171`, was
`withheld`: line 232 of the body file gave "about 1,390 tokens", where the
measurement gives about 1,425. That pass's guarantee was never committed.
`fbb9c018` changes only `gaps.md`'s S11 row (`git diff 0034a171 fbb9c018`,
executed). So the re-runs below were made at `0034a171`, and they bind
`fbb9c018`, whose code, tests and every other record are the same. PR #1186
is open at `fbb9c018`. Its `hygiene` check failed only because the
guarantee was behind HEAD (`gh run view 41008520033 --log-failed`,
executed). Every `tests` leg on `11896fae` passed (`gh run list`, executed).

## Claims re-run

Each `seen red` was re-run in a scratch clone at `0034a171`, with the unit
restored from the commit before its change, by `.venv/bin/python -m pytest
-q -p no:xdist -p no:cacheprovider <ids>`, and the clone hard-reset between
groups. The same ids first ran in that clone at `0034a171` unchanged: 516
passed, exit 0. The clone was removed afterwards.

| Claim | Source | Command | Result |
|---|---|---|---|
| The cases of `tests/hooks/test_core.py` and `tests/hooks/test_core_start.py` were seen red against the tree with no `core.py`, no `core-start.py` and no group | `trail/phases/phase-5.md:74-77` | `hooks/lib/core.py` and `hooks/core-start.py` removed, `hooks/dispatch.py` and `hooks/hooks.json` from `ad8f09df`; both modules | holds: 22 failed, the matcher case `test_the_core_has_a_group_and_a_session_start_entry_of_its_own` among them; green at HEAD |
| `seal core`'s cases and the `core` rows of `tests/skills/test_seal.py` were seen red against `4d436388` | `trail/phases/phase-6.md:68-72` | `core_check.py` removed, `seal.py` from `4d436388`; `tests/skills/test_core_check.py`, then `tests/skills/test_seal.py -k core` | holds: 27 failed (the module has grown since, so it has more cases than the 24 the record counts); 2 failed in `test_seal.py`, `invalid choice: 'core'` |
| 8 of the 11 cases of the update module were red against `445b4dd4`, and the 3 moved ones passed | `trail/phases/phase-7.md:96-98` | `install.sh`, `uninstall.sh`, `skills/preset-setup`, update step 4, the template, both READMEs and `.gitignore` from `445b4dd4`; `tests/behaviour/test_the_old_block_leaves_through_update.py` | holds: 8 failed, 3 passed |
| Item 12: the hook prints the body below the frontmatter and `seal core` compares against it. The build crafter left no red run on record; round 6 mutated it | `trail/phases/phase-8.md:144-148`; `trail/rounds/round-6.md:328-335` | `hooks/lib/core.py` and `core_check.py` from `6ebfada5`; `Test_output::test_accepts_the_header_then_the_files_body_under_its_digest` and `Test_judge::test_accepts_the_body_below_the_frontmatter_and_refuses_the_whole_file` | holds: both red at `6ebfada5`, green at HEAD |
| The two CRLF cases were red before `72c1a3ee` | `trail/phases/phase-8.md:82-90` | `core_check.py` from `72c1a3ee^`; `-k "carriage_return_left or translating_stream"` | holds: 2 failed, 279 against 281 and 285 against 286 characters, exit 1 asserted 0 |
| The four session cases and the `core.py` parameter were red against the meter before phase 9 | `trail/phases/phase-9.md:108-114` | `payload_meter.py` from `9d861670^`; the record's `-k` expression | holds: 5 failed, four on `KeyError: 'session'`, 3 passed |
| Round 6#3: the routing assertion is red against the core at `6a925644` | `trail/rounds/round-6.md:174` | the core from `ccad9673^`; `test_review_axes.py::test_the_core_names_where_the_routing_question_is` | holds: red on "names its question by a pronoun", green at HEAD |
| Round 6#4: the slug case is red against the census without the slug arm | `trail/rounds/round-6.md:232` | `tests/censuses.py` from `e9008079^`; `-k projects_directorys_slug` | holds: red, the census refuses nothing (`[] == [line 1, line 4]`) |
| Round 7#1: the slug case is red against the dashed pattern, line 1 refused, line 4 not | `trail/rounds/round-7.md:146-150` | `tests/censuses.py` from `f1217ac9^`; same id | holds: line 1 refused by a match that keeps the dash after the name, and line 4, the home-directory slug, not refused |
| By hand: a `startup` payload through `dispatch.py session-core` names the clone's core inside it and the plugin's outside it, at the tree's digest | `trail/phases/phase-5.md:103-111` | the payload piped to `python3 hooks/dispatch.py session-core`, `CLAUDE_PLUGIN_ROOT` a scratch copy, `cwd` this clone, then a scratch directory; `shasum -a 256 skills/core/SKILL.md` | holds: exit 0 both times; the first line named `<clone>/skills/core/SKILL.md`, then `<scratch>/plug/skills/core/SKILL.md`, each with `plugin 0.25.0` and `c2fb26a9…96ae7`, the core's digest at HEAD |
| By hand: `core_check.py` in an agent's Bash reads the orchestrating session, started on 0.24.2, and exits 1 naming no core entry | `trail/phases/phase-6.md:108-113` | `python3 skills/verify/scripts/core_check.py` | holds: exit 1, "no core entry in this session's context", naming the clone's core to open once |
| S7: the hook's output stays under `CAP` | `frame/design.md:297` | `python3 -c` over `core.output('.', '.')` | holds: 6,301 characters, 6,347 B, `CAP` 10,000 |
| The payload table in the orchestrator's part of the body, measured at the gate's HEAD | the body, `## Not from the records` *The core's cost* | `HOME=<scratch>/home-before bin/seal payload --root <git archive 53f21b54>`, with `53f21b54`'s template (1,786 B) as the home's `CLAUDE.md`; `HOME=<scratch>/home-after bin/seal payload` at `0034a171`, which differs from `2236c0a8` by `frame/plan.md` alone | holds: session 7,618 → 7,490 B; crafter 29,711 → 30,126, framer 32,373 → 32,788, proofer 29,304 → 29,719, sealer 29,070 → 29,485 B; `CLAUDE.md` 5,832 → 1,143 B; the hook row 6,347 B, 1,983 tokens; each agent lists the core once and no hook row |
| "In a plugin user's repository, the block's 1,786 B gives way to the hook's output, 6,347 B here, about 1,425 tokens more per session", with the sentence that the first line's path is this clone's here and the version-cache path in a user's repository | the body file, line 232, the orchestrator's part, as rewritten after this audit's first pass | the two runs above: the hook row 6,347 B (1,983 tokens) and the block 1,786 B (558 tokens), at the meter's 3.2 B/token; `grep -n "1,390\|1,425"` on the body file | holds: 6,347 − 1,786 = 4,561 B, about 1,425 tokens. No "1,390" is left in the body. The first pass found phase 9's 1,390, from a 6,226 B output measured before `ccad9673` grew the core, and that figure now stands only in `trail/phases/phase-9.md:164-165`, the record of its own commit. The phase records are the only other place it appears (`git grep`, executed) |
| Every `## Removes` row stands nowhere in the tree | `frame/design.md:401-418` | `ls install.sh uninstall.sh skills/preset-setup tests/behaviour/test_the_installer_writes_the_block_from_its_template.py`; `cat templates/setup/claude-md-block.md`; `git grep` on the removed case names, `claude-md-block`, `install.sh`, `uninstall.sh`, `preset-setup`, "preset block" and "`@` line" outside `seal/`; `grep` on the core for `#1167` and *What a change to a gate must carry*; `.gitignore`; update step 4's heading | holds: the four paths are absent; the template is the two markers; the removed case names stand nowhere; the remaining hits are the update step that takes the block out, its README sentences naming the template, the module that holds the three files absent, the meter's import rows (plan D1) and docstrings that say the block was retired; `#1167` and the `CONTRIBUTING.md` sentence are out of the core, and the sentence stands in `CLAUDE.md:18`; `.gitignore` has no `install.sh` comment; step 4 is *Take out the preset block* |
| The removals the changelog names: the preset block, `install.sh`, `uninstall.sh`, `/agentic:preset-setup` | `changelog.md:3` | the row above | holds |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | A5, reframed after round 5: the core is `skills/core/SKILL.md`, preloaded by every agent and printed into every session by a `SessionStart` hook matched `startup\|clear\|compact`, the tree's copy in a clone of the plugin; `seal core` reads it back; the block, its installer, its uninstaller and `preset-setup` retire, and update step 4 takes an installed block out; the meter gains a session table; the core's prose is refactored (S11, S12); Q1 answered A5 by the owner, Q2 and Q3 open | #1177's *Update (owner, 2026-10-30)* and #1183's update (executed `gh issue view`); the tree at `hooks/hooks.json:79-80`, `dispatch.py#GROUPS`, `orchestration.md:27`, both READMEs, the template and every *Removes* row (read, rows above). Where it departs from the issue's words it gives grounds: `seal core` compares with the file the first line names, not `${CLAUDE_PLUGIN_ROOT}`, which an agent's Bash cannot read (*Grounding* row 44) | S11 asks all four agents' suites to pass, and they do not. The framer's compare record says `Verdict: fail` on rule 5 (`evals/framer-phase-8.md`). No proofer or crafter side ran. Both sides read the core at `769a1413` (`ad7d05bb…`), and `ccad9673` changed it after that. `gaps.md` *Not verified* and the body record this as the owner's decision of 2026-10-30. Since `fbb9c018`, the S11 row of `gaps.md` also answers the re-run question rounds 6 to 8 left with the orchestrator: no re-run, on its grounds that each change restores a reading the old core had or names a pronoun's noun. That matches rounds 7 and 8, which read the three sentences that way (read). Known, not contradicted |
| the build | phases 5 to 10 at `36b6b2b6`, `84cf2dd3`, `56861925`, `72c1a3ee`, `dd6f930a`, `3f458f83`; fix passes `ccad9673`, `e9008079`, `f1217ac9`; `.test_durations` from CI run 41006808781 (`e2fbae86`) | the diff (read); every sampled `seen red` and `executed` claim (rows above); `gaps.md` *Where spec and implementation diverged*, whose two later rows are folded into the design (`76d80d75`, `f0c4aff2`) | none |
| the last round | round 8 at `e2fbae86`: no finding. It confirms round 7#1 and the durations refresh, and leaves the S11 re-run with the orchestrator and the pushed history's real path with the owner | rounds 6 and 7 (read); this audit's re-runs of round 6#3, 6#4 and 7#1; `trail/gate.md` at `11896fae` | none |
| the changelog | the core arrives in every agent through `skills:` and in every session from the hook, at start, `/clear` and compaction; about 1,980 tokens; `! seal core` shows it; `/memory` no longer lists it; disabling the plugin's hooks turns it off; the block and the three retired names are gone; update empties then removes the old block; a project's block is named, not edited | the tree (read); the hook row's 6,347 B, 1,983 tokens (executed); the issue's *Done when*, "the release note says the core arrived" | none |
| the orchestrator's part of the pull request body | `Closes #1177`, `Closes #1183`; the payload table at the gate's HEAD; the leftovers in #1184, #1185, #1148 and #1038; how the run went | the re-measured table (executed); #1184 and #1185 open with matching titles, the #1148 comment of 2026-10-29T14:44:08Z, the #1038 comment 6514855011 (executed `gh`); its account of rounds 6 to 8 and of the Windows fix (read) | none. Its line 232 gave "about 1,390" at this audit's first pass, and it now gives about 1,425, which the table's own figures give (row above) |

The owner's open question stands outside this verdict. The real user path
that `4d436388` added to `frame/design.md:42` stays in the pushed history
of PR #1186 until the squash (round 8 *Not judged*). The tree no longer
holds it: the census over the tree refuses nothing, which round 8 executed
and this audit read.

Verdict: sealed
