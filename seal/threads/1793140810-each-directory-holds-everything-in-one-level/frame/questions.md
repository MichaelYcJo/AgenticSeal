# Questions for the planner: 1793140810-each-directory-holds-everything-in-one-level

What the ticket left open and the tree answered, so nobody reopens it. Each
answer's grounds are in `frame/design.md` or in `plan.md` *Alternatives
considered*:

- **Whether `skills/` can be split by kind.** Claude Code loads
  `skills/<name>/SKILL.md` one level deep, and a nested directory loads only
  through the manifest's `skills` key (`https://code.claude.com/docs/en/plugins-reference`,
  read 2026-10-28). `skills/` keeps one level, and after the removal it holds
  only the workflow's skills.
- **Which files stay at the top of `hooks/`.** What `hooks/hooks.json` and
  `hooks/dispatch.py#GROUPS` run: `hooks.json`, `dispatch.py` and 15 gates.
  `worktree_consent.py` is a gate and stays; `launch.py` is run by `bin/`
  and moves to `hooks/lib/`.
- **Whether `hooks/cmdline_base.py` can move.** It can. The freeze hashes
  the bytes from `START` on, the rider above it may change, and the readers
  case reads `hooks/` recursively.
- **The two directories of `templates/`.** `templates/records/` for the
  shapes of the records a work item and a release write, `templates/setup/`
  for the files written into a repository. Each file keeps its name.
- **Packages or the import mode for `tests/`.** pytest's default `prepend`
  mode with no `__init__.py`: the other two break `from conftest import` in
  134 files. A case refuses two test files of one name.
- **Where the area directories come from.** The first segment of a module
  test file's `TARGET`, a leading dot dropped. The files whose `TARGET` is
  under `tests/` stay at `tests/` beside what they test.
- **How a test file finds the repository root.** From `tests/conftest.py#ROOT`,
  one source, so the next move costs no edit per file.
- **`bin/`.** It stays: #1060 says it follows #1051, and `bin/` is what
  Claude Code puts on PATH.
- **Where `.test_durations` comes from.** The `test-durations` artifact of
  a `tests` run dispatched on this branch after phase 4, committed by the
  orchestrator.
- **The Korean editions.** `docs/one-root-by-lifetime.ko.md` and the two
  under `docs/experiments/` do not move, because no document moves; their
  citations of moved paths are rewritten with the English ones.
- **Whether an installed repository needs a migration.** It does not; what
  was checked is `plan.md` *Operational impact*.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Do the policy documents move into subject directories under `docs/`, as #1060 proposes, or stay at the top of `docs/` with `docs/README.md` grouped by subject? The tree cannot answer it because #1060 proposes the move and three readers of the tree refuse it: `skills/settle/scripts/rule_changes.py` accepts only a top-level `docs/<file>.md` as a `## Rule changes` `file`, `seal fold` reads only the top level of the policy root, and `docs/README.md` says a subdirectory of `docs/` is no policy and `settle` never writes there. Choosing between the ticket and those rules is a decision about the product | a person | **Flat, index by subject**: `docs/` keeps its 17 top-level files where they are, `docs/README.md` holds one table per subject (the process, the records, the agents and the review, the checks, as #1060 groups them, with `the-routing-check.md` and `the-session-hooks.md` placed by phase 1), and no reader changes. **Subject directories**: the documents move with their Korean edition, `rule_changes.py` and `fold_check.py` learn which subdirectories are policy and which, like `experiments/`, are not, `skills/settle/SKILL.md` *Rule changes* and `docs/README.md` restate the rule, and every repository that installs the plugin gets the wider grammar. It adds one phase with new cases seen red, and it is a change of behaviour inside a release #1060 calls a change of place | Flat, index by subject. Phase 1 builds it | open |
| Q2 | Are the eight general skills no record shows used (`debug`, `build-fix`, `checkpoint`, `gap-analysis`, `security-audit`, `testing`, `learn`, `audit`) removed, moved out to a plugin of their own, or kept? #1060 decides it "from whether anything in the record shows it used", and the record shows no use of any of them. The tree cannot settle it because the instrument is blind on one side: a session that loads a skill writes no record of loading it, so a use that happened leaves nothing in the tree. `audit` is not on #1060's list and is put here by the same criterion | a person | **Removed**: phase 5 removes them, `/agentic:security-audit` and `/agentic:testing` stop existing for a user who types them, a repository's `.claude/audit-rules/*.md` has no reader, and git history holds each skill for a later restore. **Moved out**: a second plugin in this repository's marketplace, with its own manifest, version and install line, which phase 5 builds instead and README.md *Install* names. **Kept**: phase 5 is dropped and `skills/` keeps both kinds, one level deep | Removed. Phase 5 builds it, alone, so another answer replaces that phase and nothing else | open |
| Q3 | Does an installed repository updated to 0.23.1 run its first session with its hooks firing as before? The tree cannot run a session under an installed plugin; it can only show that `hooks/hooks.json` is unchanged, that every gate loads in a fresh interpreter, and that the dispatch cases pass | a measurement | **Read in the first session after `/agentic:update`**: a session in any opted-in repository after the update, where `dispatch.py`'s failure report (`hooks/dispatch.py#LABEL`) prints nothing at the end of the first turn. **Left to the tree's cases**: the fresh-interpreter case and `tests/hooks/test_dispatch.py` stand for it | The tree's cases stand for it, and the owner's first session after the release is the reading | open |
