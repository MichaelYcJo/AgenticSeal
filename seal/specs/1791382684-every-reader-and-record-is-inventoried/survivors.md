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
