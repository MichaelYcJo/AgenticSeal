# Review round 2: 1794271935-the-releasing-documents-describe-the-note-twice

```seal
target: 9c00157f6, fixes 4b10dd960..9c00157f6
```

This is the verifying round over round 1's one finding. The code reviewed
is the fix diff, `c15f827f2`, and the close that `9c00157f6` appends to
`trail/rounds/round-1.md`. `routing.md`, the three frame files, `gaps.md`,
`changelog.md` and `pr.md` were each read whole at `9c00157f6`. No
`pr.<lang>.md` stands, and none is owed, since `seal/config.json` names
English for both language keys. No `seal/parity.json` is declared.

Carried from round 1 and not re-established: that `53f21b542` removed the
checklist's step 3; that `skills/settle/scripts/settle.py:1854` removes each
directory with `shutil.rmtree`; that the other "step N" hits in
`tests/behaviour/test_release_hygiene.py:1064-1115` name the steps of
`skills/update/SKILL.md`. Each was re-opened at its coordinate and still
reads as round 1 says. Round 1's sweeps were run again at the target (see
`## Probes`).

## Findings

None.

## Confirmations

```seal
confirms: round-1#1
```
What holds: neither docstring cites a checklist step any more, and the
closing memo no longer keeps a stale step as not done.

- `tests/conftest.py:213-216` takes round 1's proposed text. It cites
  `docs/releasing/release-checklist.md` *Settle what earlier releases left
  behind*, and that section holds the sentence the claim stands on at
  `docs/releasing/release-checklist.md:109-111`, "`--apply` deletes each
  directory from the working tree and stages nothing" (read). The close
  claims the census pins that citation. I re-ran its `bin/seal mutate`
  line with `--tests` naming the census. It came back `red`, and the
  census's tree reading failed on `tests/conftest.py:215` and nothing else
  (executed, see `## Probes`).
- `tests/behaviour/test_release_hygiene.py:1372-1382` is in the fix pass's
  own words, and the close gives its grounds. The close claims the sweep
  lists only the `LOADED` prefixes and that `seal settle --apply` deletes
  only under `seal/threads/`, so "`seal settle --apply` deletes ..., so the
  index can list paths the disk does not have" would say the sweep meets
  those deletions. Found: `LOADED` at `tests/behaviour/test_release_hygiene.py:45-53`
  holds `skills`, `agents`, `docs`, `templates` and three top-level files,
  and no `seal` prefix, and the case passes `*LOADED` to `tracked` at line
  1391 (read). So the proposed sentence would have tied the sweep to an act
  that never reaches it, and the fix pass's rewrite is the more accurate
  one. The new first sentence says the checklist names the module on its
  `check:` lines; they stand at `docs/releasing/release-checklist.md:241`
  and `:344` (executed, `grep -n`). The new second sentence states the
  class as #432 states it: "Any change that deletes a tracked text file
  reaches it the same way" (executed, `gh issue view 432`). The case body
  builds that state, with `docs/folded.md` deleted under `docs`, and
  asserts the sweep reads past it (lines 1383-1397, read).
- `gaps.md` *Not done* loses the paragraph on the hygiene docstring. It sat
  under `## Not done`, which holds decisions in prose, not a
  `## Not verified` row that is closed by marking it
  (`skills/implement/SKILL.md` *4. The closing memo*). The decision it
  recorded, leaving the sentence, was reversed by the same commit, so
  keeping the paragraph would state something false about the present. Its
  removal is no finding.
- `trail/phases/phase-2.md:86-88, 90-95, 105-106` stay as they stand. The
  close names each of them, and says that the "whole for those two
  spellings" was untrue at `c44121bff` and that two step numbers stood
  where the record counts one. Round 1's fix allowed this: "the fix pass
  names that in its close or corrects the sentence in place". A fix pass
  writes no phase record, so the close is where the correction stands for
  the sealer and the settle.

What matched: the fix diff touches only the two docstrings and `gaps.md`
(executed, `git show --stat c15f827f2`), and `9c00157f6` only appends the
close block to `trail/rounds/round-1.md`. No line of code runs differently.

What matched: the records that state the present still hold at the
target. `pr.md`'s seven quotes each stand word for word, with whitespace
collapsed, in the `changelog.md` items and `frame/plan.md` rows they name
(executed, a whitespace-collapsing substring check of each quote against
its source). The fix changes nothing that `changelog.md` or the frame
states. `gaps.md` `## Not verified` still reads `nothing`, and its `why:`
holds for the fix pass too, since the close labels each claim it makes
`executed` or read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at `9c00157f6`: the suite stands `unverified` here, and the narrow runs of `## Probes` are not it | `seal/config.json` `Broad gate` | the orchestrator, by its broad run before the sealer's spawn |
| The two `Test_census_case` failures of `tests/test_conftest.py`, which the orchestrator reports as failing on base too and filed as #1498; this round did not run the base | `tests/test_conftest.py` | the orchestrator, through #1498 |

Nothing this round found is open. What comes due is the orchestrator's
broad run, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `bin/seal mutate tests/conftest.py --replace '*Settle what earlier' '*Settle what older' --tests "bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist -k every_cited_section"` in a clone at `9c00157f6` | `red`; `test_every_cited_section_stands_in_its_file` failed with "tests/conftest.py:215 cites `docs/releasing/release-checklist.md` *Settle what older releases left behind*" and no other dangling citation; the file was restored and `git status --short` printed nothing |
| `bin/test tests/behaviour/test_release_hygiene.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py -q` in the clone | 143 passed, exit 0 |
| `bin/test tests/test_conftest.py -q` in the clone | 47 passed, 2 failed, exit 1; the two failures are the `Test_census_case` cases the orchestrator filed as #1498 |
| `uvx ruff check` and `uvx ruff format --check` on `tests/conftest.py` and `tests/behaviour/test_release_hygiene.py` in the clone | exit 0 each |
| Round 1's sweeps at the target: `git grep -n 'release-checklist' -- . ':!seal/threads'` filtered to "step", the `-P` numbered-step grep filtered to checklist and release, and the scenario S4 grep | the first lists only `docs/releasing/branch-and-release.md:9`, "in the order the steps run", which cites no step; the second lists only steps of `skills/update/SKILL.md`, `agents/sealer.md` and `agents/framer.md`; S4 finds nothing |
