# Design: 1793240969-pre-rename-readings-outlived-their-release

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-routing-check.md` *At the pull request* (read) | The policy states the trailer arm, and one sentence of it says `chain-check` reads `SpecSeal-Routing:` as `Seal-Routing:` for the minor release of the rename. This work removes that reading, so the sentence is a `remove` in `## Rule changes` below |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | A pull request does not edit the policy root. The sentence above stands in `docs/` until the settle after this release writes the `remove`, so this pull request leaves `docs/the-routing-check.md` untouched |
| `CLAUDE.md` *The rule a mechanism is kept against* (read) | A mechanism stays only while it catches something. Each reading here reads an input that nothing open still holds (measured under *Scope*), so both readers go |
| `skills/agent-contract/SKILL.md` rule 12 (read) | The class is enumerated, not only the two coordinates the issue names. The other members, and why they are out of this work, are under *Scope* and in `questions.md` Q1 |
| `tests/censuses.py#old_names` (read) | A living line that spells an old name either has its spelling in `KEPT_OLD_NAMES` or carries `# exempt from old_names: <why>` on its own line above it. The build uses those two existing forms and adds no new one |

## Scope

**In.** The two readings that #1142 names, each with every line that states it:

- `skills/code-review/scripts/chain_check.py#OLD_TRAILER`. The constant, its
  comment, the second `key=` in `routing_trailers`' trailer format, and the
  words in `routing_trailers`' docstring and in the module docstring's
  `trailer` arm that say the old key is read.
- `hooks/lib/routing.py#OLD_BY_CRAFTER`. The constant, its comment, its
  `# exempt from old_names:` line, and the two lines in `parse` that turn the
  old answer into `crafter`.
- The two cases that pin those readings. Each is rewritten in place into the
  case that pins the opposite: the old input is read the way every other
  unknown input is read (S1 and S2 below).
- The sentence in `skills/implement/orchestration.md` *What the answer
  writes*, in the `Implementation` row, that describes the `smith` reading.
- The comment on the `SpecSeal-Routing` item of
  `tests/censuses.py#KEPT_OLD_NAMES`. The item stays, and its comment is
  rewritten to name the two readers that still spell the key: S1's case, and
  `docs/the-routing-check.md` *At the pull request* until the settle removes
  that sentence.

**What nothing open holds (executed, 2026-10-29, after `git fetch origin`).**
The remote holds two branches, `origin/main` and `origin/release/v0.24.1`,
and the clone holds seven local ones, the four sibling branches of this
milestone among them. No commit on any of them outside `origin/main` carries
`SpecSeal-Routing` in its message. No `seal/threads/*/routing.md` on any of
them answers `Implementation` with `smith`. All history together carries the key 358
times, every one of them in commits already on `origin/main`, which no pull
request judges again.

**Out, and why.**

- **The other readings of the same promise** (rule 12's class). Each one's
  comment says the minor release after the rename removes it, and no issue
  schedules it (executed: `gh search issues` for `OLD_PLUGIN_CLONE`,
  `OLD_START` and `specseal:start` finds none open). They are:
  - the CLAUDE.md block markers that a release before the rename wrote, read
    by `install.sh` (`OLD_START`, `OLD_END`), `uninstall.sh` (the same two),
    and `skills/update/SKILL.md` *the table row for a block between the old
    markers*, pinned by
    `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py`;
  - the clone line of a workflow that a release before the rename wrote, read
    by `skills/implement/scripts/seal.py#OLD_PLUGIN_CLONE`, described in
    `templates/setup/hygiene.yml` and `README.md` *the paragraph on
    `seal pr-checks install` after the rename*, pinned by two cases of
    `tests/skills/test_seal.py`.

  These differ from the two in scope in what they read. `routing.md` and a
  commit trailer belong to work in flight, and that work is measured above.
  A CLAUDE.md block and a workflow file belong to a person's own install and
  stay as written until that person runs `install.sh`, `/agentic:update` or
  `seal pr-checks install`. A person who goes from a release before 0.23.0
  straight to one without the reading would get a second block appended to
  their CLAUDE.md, or a workflow `seal pr-checks` treats as somebody else's.
  How long that upgrade path is kept is a product decision, so it is
  `questions.md` Q1, and the build proceeds on Q1's default.
- **`SPECSEAL_LANG`** (`hooks/worktree-guard.py#_lang`, `README.md`,
  `.claude-plugin/plugin.json`). Its comments say it is read through 0.24.x,
  so its removal is due at 0.25.0 and is not overdue.
- **`hooks/root-migrate.py`**, the move of a 0.22.x layout. Its comments state
  no release that removes it.
- **`skills/verify/scripts/pact_check.py#INLINE_TOKEN`**. It refuses the
  0.23.x inline anchor and reads nothing, so it is not a reading kept for one
  release.
- **The edit to `docs/the-routing-check.md`**. That is the settle's, from
  `## Rule changes` below.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The old trailer key is not read | Given a ready pull request in a shared root whose own commit, committed by its author, carries `SpecSeal-Routing: <a work item no declaration names>` and a second commit carrying `SpecSeal-Routing: no work item`, and no `Seal-Routing` trailer on either. When `chain-check` runs. Then it exits 0, and neither commit's short SHA is in its output, the same as for a commit with any other trailer key | `tests/skills/test_chain_check.py#Test_routing_trailers`, the case that replaces `test_reads_the_trailer_a_commit_before_0_23_0_carries` at its place, seen red at 1e82fd0a before the reader changes |
| S2 The old Implementation answer is unanswered | Given a `routing.md` whose `Implementation` row reads `smith`. When `hooks/lib/routing.py#parse` reads it. Then the declaration parses, and its `implementation` is None, as for `whoever gets to it` | `tests/hooks/test_routing.py#Test_parse`, the case that replaces `test_accepts_the_answer_written_before_the_rename_as_the_crafter` at its place, seen red at 1e82fd0a before the reader changes |
| S3 `Seal-Routing` is judged as before | Given a commit carrying `Seal-Routing: <id>` or `Seal-Routing: no work item`. When `chain-check` runs. Then the problem and the notice are the ones they were at 1e82fd0a | the cases of `tests/skills/test_chain_check.py#Test_routing_trailers` that stand unchanged, `test_refuses_a_commit_naming_a_work_item_no_declaration_names` among them |
| S4 `crafter` and `the session` read as before | Given a `routing.md` whose `Implementation` row reads `crafter` or `the session`. When `parse` reads it. Then `implementation` is that answer | `tests/hooks/test_routing.py#Test_parse.test_accepts_the_third_axis_where_it_is_there`, unchanged |
| S5 No living file names a removed unit | Given the branch's head. When `git grep -n -e OLD_TRAILER -e OLD_BY_CRAFTER -- ':!seal/threads'` runs. Then it prints nothing; and every census passes over each file the build changed | the `git grep`, and the census cases that `tests/test_censuses.py` and each changed test module's `census_case` run |

## Data & interfaces

- `skills/code-review/scripts/chain_check.py#routing_trailers` asks git for
  one trailer key, `Seal-Routing`, and its return shape does not change.
- `hooks/lib/routing.py#parse` reads the `Implementation` row against
  `IMPLEMENTATION_ANSWERS`, `crafter` and `the session`, and nothing else.
- Two module names leave: `chain_check.OLD_TRAILER` and
  `routing.OLD_BY_CRAFTER`. Outside `seal/threads/`, only the two pinning
  cases import either (executed: `git grep`).
- What a person sees changes in one place. A `routing.md` answering `smith`
  no longer gets `hooks/implementer-notice.py`'s reminder, which fires only
  for an `implementation` equal to `crafter`. No message text changes.

## Rule changes

- remove
  file: docs/the-routing-check.md
  section: At the pull request
  from: A commit made
    before the plugin was renamed AgenticSeal carries `SpecSeal-Routing:`, which
    `chain-check` reads as the same trailer for the minor release of the rename;
    the next minor release removes that reading.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The old trailer key and its comment | `skills/code-review/scripts/chain_check.py#OLD_TRAILER` | No commit outside `origin/main` carries the key (executed, *Scope*). A commit that does is read as one with any other key: not judged |
| The second `key=` of the trailer format, and the docstring words *or `SpecSeal-Routing`* and *under either key* | `skills/code-review/scripts/chain_check.py#routing_trailers` | The same reason as the row above |
| The clause *or `SpecSeal-Routing` on one made before the rename* | `skills/code-review/scripts/chain_check.py`, the module docstring's `trailer` arm | The same reason as the row above |
| The old answer, its comment and its `# exempt from old_names:` line | `hooks/lib/routing.py#OLD_BY_CRAFTER` | No `routing.md` on any branch answers `smith` (executed, *Scope*). An answer outside `IMPLEMENTATION_ANSWERS` already reads as unanswered |
| The two lines that turn `smith` into `crafter` | `hooks/lib/routing.py#parse` | The same reason as the row above |
| The case that pins the old trailer read | `tests/skills/test_chain_check.py#Test_routing_trailers.test_reads_the_trailer_a_commit_before_0_23_0_carries` | Rewritten in place into S1's case |
| The case that pins the old answer read as `crafter` | `tests/hooks/test_routing.py#Test_parse.test_accepts_the_answer_written_before_the_rename_as_the_crafter` | Rewritten in place into S2's case |
| The sentence describing the `smith` reading | `skills/implement/orchestration.md` *What the answer writes*, the `Implementation` row | Nothing needs to own it: the row's vocabulary, `crafter` or `the session`, already says what reads |
| The sentence describing the old trailer read | `docs/the-routing-check.md` *At the pull request* | The settle after this release, from `## Rule changes`; this pull request does not edit it |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-29 by framer, before the build.
