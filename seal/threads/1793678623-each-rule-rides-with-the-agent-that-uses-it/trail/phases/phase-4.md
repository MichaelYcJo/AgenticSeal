# Phase 4: 1793678623-each-rule-rides-with-the-agent-that-uses-it

## What this phase found

**The frame names the wrong flag for the tree at HEAD.** D6 and the plan's
*Verified by* cell write `release_report.py --against v0.30.0 --at <clone at
HEAD>`. The script's docstring says `--at` is the tag's tree and `--root` is
this one, and `main` reads `at` from `--at` and `now` from `--root` (read).
So the measurement ran with `--at` at the base and `--root` at HEAD. The
framer's base reading had both flags at one clone, and gave the same rows at
both sides. `v0.30.0` resolves to 0c68b9933 (`git rev-parse`, executed).
Judged against `.github/scripts/release_report.py`'s docstring and `main`.

**This phase moved the version, where the release document gives that to
the orchestrator.** `docs/releasing/branch-and-release.md` *The version moves
at the start of a release* says the orchestrator moves it in the commit that
adds the release's first changelog fragment (read). `frame/plan.md` phase 4's
*Delivers* cell and the spawn give the move to this phase. 08b43c65f adds
`changelog.md` and moves `.claude-plugin/plugin.json` from `0.30.0` to
`0.30.1` in one commit, as that section asks of the commit. No other tracked
file outside `seal/`, `CHANGELOG.md` and `.test_durations` names `0.30.0`
(`git grep`, executed, exit 1). `git show HEAD:.claude-plugin/plugin.json`
reads `"version": "0.30.1"` at 08b43c65f (executed). The fragment's `###
Process changes` table is also written here.
`docs/layout/the-record-layout.md` *A change writes fragments, never a shared
file* asks for it, since the diff changes `agents/*.md` and
`skills/implement/orchestration.md`. That section names the orchestrator as
its writer, so the orchestrator reads its three rows before the pull request.

**No agent's preload is larger than at v0.30.0.** The commands ran in two
`git clone --no-local` copies in the session scratchpad, one at 0c68b9933 and
one at 08b43c65f, both since removed. Each ran from the HEAD clone as `uv run
python .github/scripts/release_report.py --against v0.30.0 --at <base clone>
--root <clone>`, and each exited 0 (executed). With `--root` at the base
clone, every row read the frame's base reading, change +0 (executed). With
`--root` at the HEAD clone, the rows were these.

| What | v0.30.0 | Now | Change |
|---|---|---|---|
| preload `crafter` (bytes) | 33,081 | 31,510 | -1,571 (-4.7%) |
| preload `framer` (bytes) | 36,362 | 34,616 | -1,746 (-4.8%) |
| preload `proofer` (bytes) | 32,293 | 30,620 | -1,673 (-5.2%) |
| preload `sealer` (bytes) | 31,879 | 30,336 | -1,543 (-4.8%) |
| preload `tracer` (bytes) | 25,085 | 23,750 | -1,335 (-5.3%) |

The same rows came from a clone at 20e140537, before this phase's commit
(executed). 08b43c65f changes no file a preload sums. Each change is the sum
of the three phases' byte changes their records give. For the crafter that
is -441 - 830 - 300 = -1,571. For the tracer it is -441 - 896 + 2 = -1,335,
so phase 3's +2 is inside a fall. D5 estimated -1,500, -1,700, -1,500, -1,550
and -1,300. The proofer fell 173 bytes more than the estimate, and the sealer
7 bytes less. `skills/implement/SKILL.md` went from 25,406 to 26,127 bytes,
and `skills/verify/SKILL.md` from 15,097 to 15,208 (`git show <commit>:<path>
| wc -c`, executed). The contract went from 12,906 to 11,680.

**The census reproduces the base reading, and falls at HEAD.** The probe was
one file in the session scratchpad, written to D6's method, and since
deleted. It ran as `python3 -I test_tmp_census.py <base clone> <HEAD clone>`,
with the HEAD clone at 20e140537, and exited 0 (executed). It reads every
`git ls-files` `.md` and `.py` path outside `seal/` and `tests/`, lowercases
it, and takes runs of `[a-z0-9_/.'-]+`, each with `.` and `'` stripped from
both ends and empty ones dropped. Per target file, it counts the words inside
any ten-word run that another corpus file also holds. Its first run gave the
frame's base reading in every cell.

| File | 0c68b9933 | 20e140537 |
|---|---|---|
| `agents/crafter.md` | 245 of 1,683 | 198 of 1,632 |
| `agents/framer.md` | 185 of 2,263 | 137 of 2,181 |
| `agents/proofer.md` | 180 of 1,588 | 140 of 1,518 |
| `agents/sealer.md` | 77 of 1,505 | 49 of 1,455 |
| `agents/tracer.md` | 43 of 451 | 26 of 434 |
| `skills/agent-contract/SKILL.md` | 58 of 2,145 | 58 of 1,939 |
| `skills/core/SKILL.md` | 146 of 1,574 | 146 of 1,574 |
| all | 934 of 11,209 | 754 of 10,733 |

08b43c65f adds only files under `seal/` and `plugin.json`, and the corpus
holds neither, so the HEAD column stands for it by the method (read). The
probe ran a second time, with the same two trees and a pair breakdown added,
and every count above came out the same (executed). Each file's six top
partners came out the same too, except where two partners tie, since the
probe ranks ties in set order. The framer's sixth partner at 3 runs and the
proofer's sixth at 2 runs changed between the runs that way. Rule 7 asks
for one run, and the probe ran twice.

**Each D3 copy, named against its pair.** The pair breakdown counts the
distinct ten-word runs two files share, at the base and at HEAD, and prints
the text of each run that left (executed).

- **The plugin-path sentence left all ten pairs of definitions.**
  crafter~framer 65 -> 36, crafter~proofer 58 -> 38, crafter~sealer 25 -> 6,
  crafter~tracer 14 -> 6, framer~proofer 50 -> 30, framer~sealer 25 -> 6,
  framer~tracer 14 -> 6, proofer~sealer 25 -> 6, proofer~tracer 14 -> 6, and
  sealer~tracer 14 -> 6. In each pair the run that left is that sentence. In
  the tracer's pairs it is the shorter clause, "the plugin's at the root two
  directories above the base directory the harness printed with the
  contract".
- **The reference-root sentence left crafter~framer.** The run "a reference
  root templates/setup/config.md reference specs is read where the work
  touches what it describes and cited" left. Neither copy shared a ten-word
  run with `skills/implement/SKILL.md` at the base. The crafter's pair with it
  holds 4 runs at both trees, and the framer's 0. So the census sees this copy
  between the two definitions, and not against its kept side.
- **The proofer's parity sentence left its pair.** proofer~`skills/legacy-parity/SKILL.md`
  went 2 -> 0, and the run "where the pull request changes a path outside
  docs/ and seal/" left. The sealer's pair with that skill is 0 at both trees.
- **Four copies shared no ten-word run with their kept side at the base.**
  These are the sealer's parity sentences, the framer's reframe sentence, the
  preamble's two sentences, and rule 19's clause. The contract's pairs with
  the core, with `agents/crafter.md` and with `skills/verify/SKILL.md` are 0
  at both trees, and its pair with `skills/implement/SKILL.md` is 1 at both.
  The crafter~framer runs that left are the two above. So the census cannot
  name these copies gone. The `git grep` list below does, on their own words.
- **What the definitions still share is what the frame keeps.** Every pair
  keeps the opening sentence, pinned by
  `tests/text/test_every_agent_reads_the_contract.py#SENTENCE`. The
  crafter, the framer and the proofer keep the write bound (`#BOUNDS`) and
  the writing-style step (*Scope*, Out). crafter~framer keeps the
  reference-root *Never* line, pinned by
  `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`.
  crafter~proofer also keeps three runs from rules each of the two
  definitions holds for its own step: the crafter's *A new test starts from
  its group* against the proofer's *Each new test is read against its
  group*, the crafter's *Find the runner* against the proofer's *Runs are
  narrow*, and *The broad gate is not yours* in both. The frame's reading keeps all of them (`frame/design.md` *The
  reading: agent definitions*). The contract's 58 shared words and the core's 146 do not
  move. The core's do not because the core does not change (design, the
  core's row). The contract's top partners are
  `skills/implement/orchestration.md`, `skills/config/SKILL.md` and
  `docs/running/the-broad-gate.md`, which no D3 row names.

**Every D3 and D4 removal is gone.** Each search below ran at 20e140537 and
exited 1 with no lines (executed). 08b43c65f touches none of the searched
paths.

| Removal | Search |
|---|---|
| D4: rules 8 and 20's `Retired by` lines | `git grep -n "Retired by" -- skills/agent-contract/SKILL.md`; `git grep -n "Retired by #1027\|Retired by #1312" -- ':!seal/' ':!CHANGELOG.md'` |
| D2, D4: the sections of rules 8 and 20, and D1's rule 16 | `git grep -n -E "^## (8\|16\|20) " -- skills/agent-contract/SKILL.md` |
| D1: rule 16 cited by number | `git grep -n "contract rule 16" -- ':!seal/' ':!CHANGELOG.md'` |
| D1: the phase-boundary set in rule 2 | `git grep -n "phase boundary" -- skills/agent-contract/SKILL.md` |
| D3: the plugin-path sentence in five definitions | `git grep -n "two directories above" -- agents/` |
| D3: the reference-root step sentence | `git grep -n "Reference specs" -- agents/crafter.md agents/framer.md` |
| D3: the parity record's sentences | `git grep -n "original:\|Baseline commit\|raise an .unread" -- agents/proofer.md agents/sealer.md` |
| D3: the builder's act in the framer's reframe rule | `git grep -n "you are not spawned again\|A builder that finds the" -- agents/framer.md` |
| D3: the preamble's two copied sentences | `git grep -n "You received this file\|A role.s rules live" -- skills/agent-contract/SKILL.md` |
| D3: rule 19's restatement of the core | `git grep -n "A change rewrites the text it amends where that text stands" -- skills/agent-contract/SKILL.md` |

The same search for "two directories above" outside `seal/` and
`CHANGELOG.md` lists only `skills/agent-contract/SKILL.md:132`, contract rule
11, exit 0 (executed). The removed case's name
`test_the_retired_rule_keeps_its_number_and_none_of_its_shapes` is found
outside `seal/` only at `.test_durations:130`, exit 0 (executed). That file
prices cases for CI's shards. `CONTRIBUTING.md` says a contributor refreshes
it from a `tests` run's artifact, and that
`test_the_durations_file_prices_the_suite` fails only past one in twenty
(read). The entry is 0.0007 seconds. These searches cover each copy's own
words. A sentence that states the same fact in other words is outside them,
so that part of the class is a sample, left to review. Phases 1 to 3 say the
same of theirs.

**Nothing the issue keeps out moved (S9).** `git diff --stat 0c68b9933 HEAD
-- docs/ 'skills/*/orchestration.md'` lists only
`skills/implement/orchestration.md`, 2 insertions and 1 deletion (executed).
That is the re-pointed citation of rule 16, as D1 states.

**The phase-boundary set passed.** The set was 93 modules, listed by two
`git grep -l` searches over `tests/*.py` (executed). It holds every test
module that names `plugin.json`, `changelog.md`, `threads`, `gaps.md`,
`phases/`, `plan.md` or `Process changes`. It also holds every test module
that lists or walks the tree (`ls-files`, `os.walk`, `glob(`, `rglob` or
`censuses`). This phase adds two files under `seal/threads/` and changes
`plugin.json`, and those modules read both.
`tests/github/test_publish_release_note.py`,
`tests/behaviour/test_the_release_check_watches_what_ships.py` and
`tests/behaviour/test_chain_hooks_hardening.py` are among them. The command
was `bin/test <the 93 modules> -q`, run at 08b43c65f with this record,
`gaps.md`'s rows and the Status cell in the working tree. It exited 0, with
5021 passed and 12 skipped (executed).
