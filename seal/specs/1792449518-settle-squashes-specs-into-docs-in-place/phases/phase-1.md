# 1792449518-settle-squashes-specs-into-docs-in-place — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 10aa4947 |

## What this phase was asked

Add the `## Rule changes` section to `templates/sdd-spec.md`. Write
`skills/settle/scripts/rule_changes.py`: the parser, an in-memory replay and
its refusals (S4, S7). Make `settle` with no flag the dry run (S8). Add the
section's vocabulary to `templates/config.md` §*What no row governs*, and its
grammar to `skills/settle/SKILL.md`. Mid-build the owner overturned Q1: no
symbol as syntax, plain field words one per line, the grammar stated once, a
block that does not match whole refused at its line, and no constant beyond
what the issue needs.

## What this phase found

- The grammar is an operation line (`- add`, `- change`, `- remove`) and
  fields indented two spaces (`file:`, `section:`, `from:`, `to:`). A value
  continues on lines indented four spaces. `rule_changes.GRAMMAR` is the one
  table in code, `skills/settle/SKILL.md` §*Rule changes* the one statement
  in prose, and a case parses the skill's example so the two cannot drift.
  The vocabulary case in `tests/test_the_pull_request_language_is_the_repositorys.py`
  derives the new literals from `GRAMMAR` and `HEADING`.
- Merge order lives in `rule_changes.order`, not in `settle.py`, because
  phase 3's predicate replays in merge order too. It reads
  `git log --full-history --topo-order --reverse --diff-filter=A` once. Two
  specs whose adding commits no ancestry orders, the same commit included,
  and that name one file and section, are a conflict.
- A spec refused at a place makes every later spec at that place wait.
  Otherwise the earlier spec would apply over the later one at the next
  settle, and the newer would not win.
- `replay` takes `held`, refusals decided before it runs: a parse error, an
  open record row (here or at the merge base, as the rule arm asks), a
  missing adding commit, a conflict. `settle.py#rule_plan` builds it.
  Nothing in phase 1 covers the open-row hold; phase 2's `--apply` cases do.
- Headings are found through `unverified_check.py#live_lines` and
  `#heading_level`, so a heading quoted in a fence is no place. Inside the
  section, a line is skipped when it is in an HTML comment; a fenced block
  inside a value is kept.
- `settle.main` handed `report` the `sys.stdout` bound when the module was
  imported, so a test's captured stdout never saw the report. `main` now
  passes `sys.stdout` at the call.
- For phase 2: the old report still lists marker folds, and `--retire` and
  `--retire-process` still run. Pre-model specs (no section) are the old
  *waiting for a fold* list for now.
