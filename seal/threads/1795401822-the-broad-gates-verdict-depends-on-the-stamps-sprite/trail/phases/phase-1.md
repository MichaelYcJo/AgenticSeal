# Phase 1: 1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite

## What this phase found

**The frame holds against the tree at `caa6ad47b`, except for the two
omissions the next two findings name.** The frame was read at `ee8a72583`, and `caa6ad47b` adds only this
work item's `frame/` (read, `git log --oneline -3`). The coordinates of
`frame/design.md` G5, G8, G9 and G16 held the text they name (read). The
gate calls none of `build`, `compose`, `stamp`, `disc_cells`, `drawn_from`
or `drawings` (executed, `grep -n -E '\.(build|compose|stamp|disc_cells|drawn_from|drawings)\(' skills/verify/scripts/broad_gate.py`
printed nothing and exited 1). The S4 search at `caa6ad47b` printed the
wrapper, its twelve callers and the three lines G8 names, as S4 lists them
(executed).

**The deferred row's rule stays, and `rounds_rows` catches a raising check
itself.** This departs from `frame/design.md` *Scope* item 4, which says
`rounds_rows` keeps its `except SystemExit`. Two documents state that the
deferred row never stops a run that passed: the comment in
`broad_gate.py#rounds_rows`, and the docstring of
`tests/skills/test_broad_gate.py#Test_rounds_rows.test_refuses_to_stop_a_run_where_the_check_will_not_load`,
whose `raises` case plants a `ValueError` in the check's load. G9 does not
list that case. The `ValueError` reached the old `except (Refused,
SystemExit)` only as the wrapper's `Refused`, so with `except SystemExit`
alone the case failed with `ValueError: planted` (executed, `seal mutate`
below). Removing the wrapper does not ask for that rule to go, and no
document says it should. So the arm is `except (Exception, SystemExit)`,
and the comment above it names a check that raises or exits. This is the
caller deciding what a raise means for its command, as `lib/sibling.py#load`'s
docstring leaves to every caller, and no exception becomes `Refused`. S4's
searches still print nothing. Judged against `skills/core/SKILL.md` *The
rule a mechanism is kept against*: the wrapper goes because its record is
the sprite alone, and the deferred row's rule has a case of its own.

**`write_gate_file`'s docstring named a refusal only the wrapper fed.** It
said `Refused` is raised where "the reader will not load", which held only
because `sibling_module(FIELDS_READER)` turned a raise into `Refused`.
G8 does not list it. The clause goes in the same commit. An absent
`lib/fields.py` is now the loader's `MISSING` at exit 2, and a raising one
a traceback, as `frame/design.md` *Data & interfaces* says of every other
load.

**`seal_stamp.py`'s module docstring now says nothing here reads a file at
import.** The paragraph that says the gate imports the text rules from
`seal_stamp.py` gains that sentence. `frame/plan.md` *Technical context*
names this paragraph as where a reviewer catches a later read at import,
and before this phase it did not say so.

**Each new case was seen red against the code at `caa6ad47b`, which is
`ee8a72583`'s code.** Each was run with the case written and the code not
yet changed (executed, `bin/test -q -p no:xdist`).

- `Test_main.test_a_malformed_sprite_leaves_the_verdict_and_the_report_as_they_were`
  in `tests/skills/test_broad_gate.py` (S1). The run with the shipped
  sprite passed. The run with the sprite cut to one line failed on
  `assert cut.returncode == 0`: it exited 2, and stderr held the wrapper's
  `will not load, so nothing ran: seal stamp: the disc's mark sprite ...
  (1 lines)`. That is the import-time read the case names.
- `Test_main.test_from_refuses_a_malformed_sprite_in_one_line_and_claims_nothing`
  in `tests/skills/test_seal_stamp.py` (S2). It failed on `assert 0 == 2`:
  `--from` drew from the sprite read at import and claimed the file.
- `Test_main.test_stop_draws_nothing_beside_a_malformed_sprite_and_claims_nothing`
  (S2). It failed on the `capsys` line: `--stop` printed a
  `systemMessage` holding the drawn stamp.

**Each unit that adds behaviour was mutated after its commit, and every
mutant was red.** Each run was `seal mutate`, and `git status --short`
printed nothing after each one (executed).

- `seal_stamp.py#build`'s read made to ignore `SPRITE_PATH`, reading the
  path beside the file instead. Red under `-k malformed_sprite`, on the
  `--from` case's exit code. Run again under the `--stop` case alone, red on
  its `systemMessage`.
- A read at import put back, `SPRITE = read_sprite(SPRITE_PATH)` above
  `build`. Red under the S1 case: the cut run exited 1, the import's
  traceback with no wrapper to catch it. The S2 cases do not watch this
  mutant, because they patch `SPRITE_PATH` after the import. S1 is the one
  that does.
- `rounds_rows`' `except (Exception, SystemExit)` made `except SystemExit`.
  Red under `test_refuses_to_stop_a_run_where_the_check_will_not_load`, on
  `[raises]`, with `ValueError: planted`.

The wrapper's removal and the callers moved to `sibling.load` add no
behaviour, and are proved by the existing cases at the new call.
`test_refuses_a_copy_without_the_git_helper_in_a_sentence` passes
unchanged, and so does `Test_module.test_a_script_copied_alone_exits_2_and_names_what_it_misses`
(executed, in the phase boundary run).

**The census of the plan row's searches prints nothing at `385ee7e2f`**
(executed, each exiting 1): `git grep -n -w SPRITE -- skills tests`; S4's
`git grep -n -e sibling_module -e 'will not load' -e 'Refused, SystemExit' -- skills/verify/scripts/broad_gate.py`
and `git grep -n sibling_module -- tests`; and
`git grep -n seal-mark -- skills/verify/scripts/broad_gate.py`.

**`seal layout --pairs` names two pairs this phase made, and neither is a
duplicate** (executed). The `--stop` case calls `main(["--stop"])` as two
cases of `Test_main` already do. The world differs: here a stamp waits
beside a malformed sprite. `Test_main`'s docstring, which already named the
two worlds of the older pair, now names the third. In `Test_read_sprite`
both cases now call `read_sprite(stamp.SPRITE_PATH)`, as *Scope* item 1
asks of every case that read `stamp.SPRITE`. One asserts the shipped
sprite. The other reads it only to build the broken file it refuses.

**The phase boundary set ran in one command, and two tree-wide cases
failed, both on records** (executed, `bin/test -q` over
`tests/skills/test_broad_gate.py`, `tests/skills/test_seal_stamp.py`,
`tests/github/test_release_seal.py`, `tests/lib/test_optin.py`,
`tests/skills/test_agentic_pytest_record.py`, `tests/skills/test_seal.py`,
`tests/text` and `tests/behaviour`, at `0f2abef0c`: 2 failed, 2010 passed,
10 skipped). The four files beyond the two modules load `broad_gate.py` or
`seal_stamp.py`. `385ee7e2f` after it rewraps one docstring, and
`Test_module` and `Test_write_gate_file` passed over it (executed).
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`
failed because this work item had no `gaps.md`, which this phase's closing
commit writes. `tests/text/test_a_cited_commit_outlives_the_squash.py::test_every_cited_commit_outlives_the_squash`
failed on `frame/plan.md` *Operational impact*, which cites
`ee8a72583:.claude-plugin/plugin.json`, a commit no release ref holds. That
line is the framer's, and the hand-back names it for the orchestrator.

**The other places that state the reworded rules were searched, and the
list is a sample.** `git grep -n -i -e sprite -e 'will not load' -e 'cannot load' -e malformed -e seal-mark`
over `docs`, `skills`, `agents`, `templates`, `hooks`, `README.md` and
`CONTRIBUTING.md` found two prose hits that state the stamp's load limit:
`docs/checks/the-stamp.md:158`, which `frame/design.md` `## Rule changes`
amends for the settle, and `skills/code-review/orchestration.md:533`, which
*Scope*, *Out* leaves. Every other hit is about another script or the
sprite's shape. `assets/seals/README.md:53-55` says the module reads its
mark from `seal-mark.txt` beside it, which still holds. The search did not
reach `evals/`, `.github/` or test prose.
