## Fixes

| # | Verdict | Commit or grounds |
|---|---|---|
| 1 | fixed | `d0541ae4` — the thirteen units, each read against its body and the callees it relies on (`merges`' caller, `_env_option`, `running`, `_ordered`, `top_units`, both `run_gh` callers, `is_header`); and the class closed by construction: every unit the three enumerations below selected was read against its own body, and 11 more lines that named a read their unit does not make were corrected |
| 2 | fixed | `d0541ae4` — `merges` `refused` (it only raises `Refused`), `parents` `passed` (a failure gives [] and the caller lists the merge as unjudged), `_ordered` `mixed` (it re-raises `NotADirectoryError` and gives [] on any other `OSError`), `parse_section` `guess` (its `strict_header=False` arm is `check_text`'s loose reading), each confirmed in the code first |
| 3 | fixed | `d0541ae4` — `sections` says a string heading is matched exactly and a pattern falls back after `## Not verified`; `flat` says it reads one field `describe` hands it, and the record's line and paragraph are gone from it |
| 4 | answered | corrected at `d0541ae4`: `plan.md`'s `Unit → units` bullet now names the unit that does the reading by what its body (or a same-file callee) does — the K1 call, the `open`, the `git` or `gh` command, the AST walk — never by position, says that where no one unit makes every read none does, gives each word a mechanical meaning, and carries round 1 ⬜ 4's decision with guard row 114 named |
| 5 | answered | corrected at `d0541ae4`: the `parse_section` row is gone from `survivors.md`, since its line no longer carries the quoted prose; `check_text`, which the row names first and whose line carries that prose with `guess`, has a row of its own already |

## The class, enumerated

The probe was `test_tmp_enumerate.py`, run from the scratchpad over the 189
units whose census line the build removed (`7608d82c`'s census less HEAD's),
then deleted. It selected:

- **(a) every unit not the first name in its inventory row's `Unit` cell:**
  71 units.
- **(b) every group of units sharing a byte-identical `Reads:` line:** 17
  groups, 40 units.
- **(c) every unit whose `Reads:` line or `What it reads, continued:`
  paragraph names a backticked identifier, path or command found neither in
  its body nor in the body of a same-file unit it calls:** 80 units.

The union is 127 units, and each was read against its body. None had to go
back to the census: every one could be read from its code. What they became:

- **Corrected, 27 units.** The reviewer's thirteen, `_ordered`, `sections`
  and `flat` (rows 1 to 3 above), and 11 the enumerations found:
  - `hooks/cmdline.py#_name_at` reads one name at an index, not `$NAME` in an
    operand; it gives `(None, i)` back, so `passed`, not `refused`.
  - `hooks/cmdline.py#_cd_target`'s paragraph: it returns kind `"unknown"`;
    the walk, not this unit, makes that `Unresolved`.
  - `skills/evidence-check/scripts/pact_check.py#near_miss` compares one name
    with the derived one and returns a bool, so `passed`, not `refused`.
  - `skills/implement/scripts/seal.py#resolve` never reads `SCRATCH`.
  - `skills/verify/scripts/broad_gate.py#Check` holds what `run` recorded and
    runs nothing itself.
  - `skills/code-review/scripts/round_record.py#parse_module`, `#signature`
    and `#return_arities` each read one module or one node, not "both ends".
  - `skills/verify/scripts/payload_meter.py#_ratio_from_baseline`, `#_spawn_of`
    and `#_same_spawn_over_other_bytes` each read one `ratios` entry and give
    None for anything else, so `passed`, not `mixed`.
- **Read and left as they stand, 100 units.** Each line is true of its own
  body or of a same-file callee the body relies on. Among them the ten groups
  still sharing a line after the fix (`below_floor` ×4, the two `parse_range`,
  the two `answer-*` hook `main`s, `_dedup`/`_directories`, `apply_chdir`/
  `compose`, the two heredoc wrappers, the two splitters, `is_ancestor`/
  `reachable`, the two module loaders, `decision_of`/`fired`), where the
  units of a group make the same read, or one reads through the other. After the fix the probe
  selects 71, 10 groups of 22 units, and 78.
- **Taken off and put back on the census: 0.**
