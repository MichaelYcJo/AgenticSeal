# Survivors — every reader and record is inventoried

`survivor-check --range origin/release/v0.21.0...HEAD` names each place that
still carries wording this item's range removed. The one "sentence" the range
removed is `tests/undeclared_readers.txt` read as prose: its first block of
`path#unit@hash` lines, from which the build took 189 lines when their units
declared. The census is a list of coordinates, not a claim, and a line leaving
it says the unit declares now; it corrects nothing another record says. Each
row below was read at the branch's head.

| Path | Quote | Grounds |
|---|---|---|
| `seal/specs/1790815614-a-joined-projects-specs-is-read-and-never-taken/plan.md` | `skills/code-review/scripts/survivor_check.py#tracked` (436) | a past work item's plan naming the units it changed; the census line that left was the unit's undeclared state, and the unit is still there |
| `seal/specs/1790655302-every-reader-ends-a-line-where-gfm-does/spec.md` | Sites: `close_issues_on_release.py#arrived`, `release_completeness_check.py#subjects_since` | a past work item's list of the sites it read; those units stand, and none of them is said to be undeclared there |
| `seal/specs/1790260567-the-broad-gate-hands-cmd-a-forward-slash/spec.md` | nine modules: `skills/verify/scripts/session_cost.py#run_gh` | a past work item's reading of which code calls `gh`; a docstring line changes no call |
| `seal/specs/1790550714-a-git-call-after-cd-is-charged-to-git/spec.md` | `hooks/cmdline.py` `split_segments*` | a past work item naming the splitter it read; the units stand |
| `seal/specs/1791076832-the-broad-gate-re-runs-the-test-command-at-the-base/plan.md` | Split with `hooks/cmdline.py#split_segments_with_separators` | a past work item's plan naming the splitter its approach used; the unit stands |
| `seal/specs/1791382684-every-reader-and-record-is-inventoried/inventory/1-hooks-shell.md` | `type`, tool_use `id` and `name`, `isSidechain is False`, `tool_result.tool_use_id`, the entry's `cwd` mapped to its clone | round 1's fix took this row's prose off `_content` and `_clone_of`, which were named beside the reader it describes; the inventory is the reading of 5623d728 and stays as written |
| `seal/specs/1791382684-every-reader-and-record-is-inventoried/inventory/1-hooks-shell.md` | refused (a command that does not split gives True) | the same: round 1 took this paragraph off `_empties_the_environment`; the row stays as the inventory's reading |
| `seal/specs/1791382684-every-reader-and-record-is-inventoried/inventory/1-hooks-shell.md` | the cd kind and operand, and the previous directory | the same: round 1 took this off `_step`; the row stays |
| `seal/specs/1791382684-every-reader-and-record-is-inventoried/inventory/5-verify-bin-ci.md` | presence of six fixed CI paths + runner words | the same: round 1 took this off `other_ci_files`; the row stays |
| `seal/specs/1791382684-every-reader-and-record-is-inventoried/inventory/5-verify-bin-ci.md` | one exact `## Not verified`, exact header, 2-cell rows, ✅ prefix | the same: round 1 took this off `visible` and `sections`; the row stays |
| `hooks/cmdline.py` | Reads: guess — the cd kind and operand, and the previous directory | `_land`'s line, the row's lead: `_land` reads the cd kind and operand and returns `prev` for `cd -`, so the line is true of it |
| `skills/code-review/scripts/chain_check.py` | What it reads, continued: `for-each-ref --contains refs/remotes/pull/` | `reachable`'s paragraph: it calls `is_ancestor` and then `carried_by_a_pull_head`, so both reads are its own |
| `skills/code-review/scripts/chain_check.py` | Reads: owned — `FIX_RANGE_RE` ends resolved | `last_round_end`'s line, the row's lead: it takes the range's ends and, where the row says `none`, the last `Target SHA` |
| `skills/verify/scripts/deferral_check.py` | Reads: guess — presence of six fixed CI paths + runner words | `inspect`'s line, the row's lead: it reads runner words out of the files `other_ci_files` finds |
| `skills/verify/scripts/unverified_check.py` | Reads: guess — one exact `## Not verified`, exact header, 2-cell rows, ✅ prefix | `check_text`'s line: its strict reading is this shape, and its loose base reading makes it `guess`, `mixed` (phase 2's hand-read decision) |
| `seal/specs/1791382684-every-reader-and-record-is-inventoried/inventory/5-verify-bin-ci.md` | `gh issue list --json number,state` exit code and JSON | round 2 took this row's prose off `run_gh`, which runs whatever `args` its two callers hand it; the inventory is the reading of 5623d728 and stays as written |
