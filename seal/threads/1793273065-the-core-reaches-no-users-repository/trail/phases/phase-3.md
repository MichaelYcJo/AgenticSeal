# Phase 3: 1793273065-the-core-reaches-no-users-repository

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | a7329570 |

## What this phase was asked

Phase 3 of `frame/plan.md`, and only that phase.
`skills/verify/scripts/payload_meter.py#composition` follows `@` lines as
`frame/design.md` *Scope* item 5 states. Then the before and after totals are
measured against a scratch home. Before is the block from
`templates/setup/claude-md-block.md` at `53f21b54`. After is the new block
beside a copy of the tree at `plugins/marketplaces/agenticseal`. Both totals
and the two commands go into this record, and the pull request body states
them, as the issue's Done-when asks. `tests/skills/test_payload_meter.py`
gains a case for each of these, each seen red first: an `@` line in each file
of the pair, a `~` path, a relative path, a symlink, a missing target, one
real path imported twice, and the fourth hop.
`tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` was to
pass if it reads the meter. Phase 4's changelog and version were not started.

## What this phase found

**The frame held.** `composition` stood where the plan's technical context
put it, and appended the pair as two flat rows.
`tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` does
not read the meter: `grep -n "meter\|payload"` over it prints nothing. It ran
in the phase-boundary set only because it reads `README.md`.

**How the design's rules were read where they left a choice.**

- `imports_of(path, home, depth, seen)` returns `(chain, real_path)` pairs.
  The design's sketch named `(display, real_path)`. `chain` is the tuple of
  each hop's path as written, so `composition` builds the row's name and its
  `via` from it without splitting a string at the arrow.
- "A quoted path is not an import" is read two ways at once. An `@` must
  stand at the start of a line or after whitespace, so `"@x"` and `` `@x` ``
  are not imports. A path that opens with a quote or a backtick is not one
  either, so `@"x"` is not an import. The installer test's `IMPORT` pattern
  refuses only the backtick.
- "One real path is counted once across the pair" also covers the pair's own
  files. Both are in `seen` before either file's imports are walked, so an
  import back to a file of the pair is no row.
- A nested import resolves against the real path of the file that holds it.
  Through a symlink, that is the target's directory. No probe says which
  directory the harness uses there, and no case pins it.
- Fences are not read. The memory docs say an import inside a code span or a
  code block is not evaluated, and *Scope* item 5 names no fence rule. A
  fenced `@path` line at the start of a line is counted. Neither block, the
  core, nor this repository's `CLAUDE.md` holds one: the after run shows one
  imported row and no other.

**`README.md` and `README.ko.md` said the meter reads "the two `CLAUDE.md`
files".** Each row now adds the files their `@` lines import. The meter's own
module docstring and the test module's docstring say the same. `git grep` on
"CLAUDE.md pair", "two \`CLAUDE.md\` files" and "seal payload" found no other
sentence that states what the meter reads.

**New cases, each seen red against the meter before the code.** In
`Test_measure`, beside the pair case:
`test_an_import_in_either_file_of_the_pair_is_a_harness_row_under_it`, which
also plants a backticked `@`, an address and `@"quoted.md"`;
`test_an_import_that_is_not_a_file_is_a_missing_row`, with a missing file and
a directory; and `test_one_real_path_imported_twice_is_one_row`. In a new
`Test_imports_of`: `test_a_tilde_path_expands_to_the_home_it_was_given`,
which points `HOME` elsewhere so `expanduser` would fail it;
`test_a_relative_path_resolves_against_the_importing_file`, with decoys
beside the top file and in the working directory;
`test_a_symlink_resolves_to_its_target`, through
`conftest.py#symlink_or_skip`; and `test_imports_stop_at_the_fourth_hop`, a
chain of five. The red run was the committed meter with only the cases
added. Seven failed, each on its own assertion or on the missing
`imports_of`. The module then passed 36 cases with no skip, the symlink case
included.

**`seal mutate`, one batch of twelve mutants over `payload_meter.py`, every
one red.** The mutants were: `@` anywhere, not only after whitespace; a
quoted or backticked path accepted; `expanduser` in place of the given home;
the working directory in place of the importer's; `abspath` in place of
`realpath`; five hops; the `seen` skip removed; the pair not seeded into
`seen`; no `via`; no sub-row in `render`; a missing target followed; and the
chain dropped from a nested import. The tree was clean afterwards.

**The before and after numbers.** Both runs use the meter at `a7329570`
against a scratch home that holds no user skill, so no row is shadowed.

Before. `<scratch>/base-tree` is `git archive 53f21b54`, and
`<scratch>/home-before/.claude/CLAUDE.md` is
`git show 53f21b54:templates/setup/claude-md-block.md`:

```
HOME=<scratch>/home-before bin/seal payload --root <scratch>/base-tree
```

After. The root is this tree at `a7329570`.
`<scratch>/home-after/.claude/CLAUDE.md` is
`git show a7329570:templates/setup/claude-md-block.md`, and
`<scratch>/home-after/.claude/plugins/marketplaces/agenticseal` is
`git archive a7329570`:

```
HOME=<scratch>/home-after bin/seal payload
```

Every token figure below is estimated at the meter's assumed 3.2 B/token,
because no transcript was calibrated.

| Agent | Before, bytes | After, bytes | Change | Before, tokens | After, tokens |
|---|---|---|---|---|---|
| crafter | 29,711 | 36,507 | +6,796 | 9,284 | 11,408 |
| framer | 32,373 | 39,169 | +6,796 | 10,115 | 12,240 |
| proofer | 29,304 | 36,100 | +6,796 | 9,156 | 11,281 |
| sealer | 29,070 | 35,866 | +6,796 | 9,083 | 11,208 |
| tracer | 22,790 | 29,586 | +6,796 | 7,121 | 9,245 |

The `CLAUDE.md` pair, the share a session in this repository reads at every
start, went from 7,618 B (2,380 tokens) to 7,666 B (2,396 tokens). The
repository's `CLAUDE.md` went from 5,832 to 856 B. The block went from 1,786
to 99 B, and the core it imports is 6,711 B. In a plugin user's repository
the share this change controls is `~/.claude/CLAUDE.md` with its imports. It
goes from 1,786 B to 6,810 B, which is +5,024 B, about +1,570 tokens.

**After this change every agent's prefix holds the core twice.** The +6,796 B
per agent is the core through `skills:` (6,711 B), the core again through the
block's import (6,711 B), less the 6,663 B the two files of the pair lost
(4,976 B from `CLAUDE.md`, 1,687 B from the block), plus 37 B more in each
definition's opening sentence. The meter counts the pair in every
agent's prefix. That rests on #292's calibration, as the meter's docstring
states, and was not measured here. If it holds, an agent on a machine with
the 0.25.0 block reads the core twice. That is about 2,100 tokens per spawn
at the assumed ratio. The issue's constraint "No session reads the core
twice" names sessions, and *Scope* item 3 gives the agents the core through
`skills:`, so neither the issue nor the frame decides it. This phase changes
neither carrier. The question is in the hand-back for the orchestrator.

**The phase-boundary set passed.** It was one `bin/test -q` command over 78
modules. They were `tests/skills/test_payload_meter.py`, every module that
names `payload_meter` or reads `README.md` or `README.ko.md`, and every
module that walks or globs `skills/`, `tests/` or a README. It passed 4,359
cases and skipped 10.
