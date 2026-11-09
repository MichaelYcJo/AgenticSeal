# Phase 2: 1794200905-a-foreign-seal-dir-keeps-the-records-shared

## What this phase found

**The frame holds for this phase, with one reader it did not list and one
interface built simpler than it states.** The coordinates *Technical
context* gives for `lib/gate.py`, `lib/routing.py`, `chain_check.py` and
`seal_stamp.py` stood where it says at `93cec19e` (read). Two things in the
frame did not hold:

- `frame/design.md` G6 and *Scope* item 3 list the modules that spell the
  root's name, and they miss `skills/code-review/scripts/pr_body.py`. It
  spells the name through `OPTIN.HOME` at three places, the kind of reader
  `frame/plan.md` *Technical context* names in its failure scenario. One is
  a classifier: `_seal_at_head` asked `chain_check.py#follows` whether the
  commits after the sealed one touch only `seal/threads/<id>/`. In a
  repository whose root is `agentic-seal/`, the commit that adds
  `guarantee.md` read as outside the records, so `seal pr-body` never drew
  the seal mark there. The other two print a path: the refusal's place
  (`_place`) and the summary line of the copy (`SUMMARY`). This phase owns
  the case for `seal pr-body --check`, so it built all three. Judged against
  *Scope* item 3's rule that a path a person reads in a message is the real
  path, and contract rule 12.
- `frame/design.md` *Data & interfaces*, the paragraph on the root leaving,
  gives `chain_check.py` two names: HEAD's for the declarations it lists,
  and the merge base's for a deleted declaration and for the test that the
  root left. The first build had both, and `seal mutate` showed they are one
  name. Dropping either `changed_routing` call stayed green (8 mutants, 6
  red, 2 survived). With each name falling back to the other, the two differ
  only where both trees carry the marker under different names. That is the
  renamed root, a limit the frame's *Out* states. `chain_check.py#root_name`
  now gives one name: HEAD's, else the merge base's, else `optin.HOME`
  (`c6cdc0b6`). Judged against `skills/core/SKILL.md` *The rule a mechanism
  is kept against* and the *Out* item on a root renamed between commits.

**Departures, among them a removal `## Removes` did not name.**

- Where neither tree carries the marker, `root_name` gives `optin.HOME`,
  where *Data & interfaces* gives `""`. Every existing `chain_check.py`
  fixture commits `seal/threads/` with no marked `README.md`, for example
  `tests/skills/test_chain_check.py#_branch_template`. Read as `""`, none of
  them would declare anything. The check read `seal/threads/` before the
  marker decided the root, and it still does where no marker stands. Judged
  against S7, which lets existing cases change only where a signature
  changes.
- `tests/lib/test_routing.py::Test_module::test_the_pinned_checks_read_under_the_root_alone`
  is removed. It held `routing.WORK_ITEMS == "seal/threads"`, the constant
  *Removes* row 4 takes out, and *Removes* did not name the case. What it
  held, a walk of declarations that stays off a team's `specs/`, is held by
  `Test_declared_for_this_branch`'s decoy case, and `root_name` answers only
  the two names or `optin.HOME`. The two comments that cited the pin, in
  `tests/skills/test_settle.py` and
  `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`, now
  cite what stands.
- The existing cases changed only for a changed signature:
  `touches_code(paths, home)`, `originals_of(..., home, ...)`,
  `declared_for_this_branch(root, routing, work_items)`, and `SUMMARY`'s
  `{home}` field in `tests/skills/test_pr_body.py#unsourced`.
- `seal_stamp.py` reads no name from the resolver. Its guard no longer
  compares the root directory's name with `seal`. `written_root` already
  asks `optin.home_at` whether that directory is the root in force, so the
  resolver alone decides.

**Decisions made while building.**

- The unit names are `chain_check.py#root_name` and `pr_body.py#_in_tree`.
  `_in_tree` is private because no other module calls it. `seal layout
  --check` reports a public function without its class.
- `pr_body.py#_in_tree` gives `optin.home_name(root)`, and `optin.HOME`
  where the root is local or absent. That second case is the name the text
  gives the root, since no path in the tree holds it.
- `pr_body.py#compose` and `#_composed` take `home` with `optin.HOME` as
  the default. `compose` has no tree to read, and its callers are the cases.

**Seen red at the phase's parent.** The first seven cases ran against
`93cec19e`'s code, with only the behaviour module changed (executed:
`bin/test tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py
-q -p no:xdist -k "s3_ or s4_ or s5_"`, 6 failed, 1 passed). The one that
passed is the `records` parameter of the package case, the side that owes
no comparison. The failing lines were read:

- The two judged cases printed "declared neither way" and "Nothing git
  carries under `seal/threads/`".
- The package case found no `agentic-seal/parity.md` line.
- The deletion case printed the same "declared neither way" and no
  root-left line.
- `seal stamp --guarantee` printed nothing.
- The `seal pr-body` body had no mark: it read `<details` where the mark's
  `<img` was expected.

These are S3's three cases the plan row names: the judged declaration, the
change to the package, and the deletion. The cases added after that run were
not run at the parent: the edited design, the pull request that adds
`agentic-seal/`, the message naming the place to declare, the deletion under
`--worktree`, and the refusal in write mode. Each was seen red by a mutant
of its own guard below. For the `there` fallback of the first build, the
failing line was read, and it names the guard: "no top-level `seal` entry".
For the other batched runs, only each mutant's red verdict was read.

**Every unit that adds behaviour went red under `seal mutate`** (executed,
one command per unit, after `c6cdc0b6`):

| Unit | Mutants | Cases run | Result |
|---|---|---|---|
| `lib/gate.py#touches_code` | 3 | `tests/lib/test_gate.py` | 3 red |
| `chain_check.py#root_name` | 4 | the behaviour module `-k s3_`, and `test_chain_check.py`'s `Test_declared_for_this_branch` and root-leaving cases | 4 red |
| `chain_check.py#main`, each use of the name | 7 | the behaviour module `-k s3_` | 7 red |
| `chain_check.py#originals_of` | 2 | `-k package_reaches` | 2 red |
| `chain_check.py#tracked_declarations` and `#declared_for_this_branch` | 3 | `-k s3_` | 3 red |
| `chain_check.py#edited_work_items` | 2 | `-k design_the_pull` | 1 red, 1 survived |
| `seal_stamp.py#queue_for_written_guarantee`, the root's name compared again | 1 | `-k s4_` | red |
| `pr_body.py`: `_in_tree`, `_seal_at_head`, `_composed`, `compared`, `_place`, both `main` calls | 8 | `-k s5_` | 8 red |

The survivor computes `edited_work_items`'s `depth` from `seal/threads`.
`seal/threads` and `agentic-seal/threads` have the same number of parts, so
the mutant is equivalent and no input tells it apart.

**For the next phases.** `chain_check.py#root_name` and
`pr_body.py#_in_tree` fall back to `optin.HOME` by design. *Scope* item 4's
text case refuses string constants, so neither needs an allowlist entry.
`pr_body.py` is done, and phase 3 need not take it up. The behaviour module
imports its `seal pr-body` and stamp fixtures from
`tests/skills/test_pr_body.py` and `tests/skills/test_seal_stamp.py`, as
phase 1 imported from `tests/skills/test_seal.py`.

**The phase boundary.** The *Phase boundary* row's set ran as one command
(executed, at `c6cdc0b6`'s code: 5225 passed, 9 skipped). It covered the
plan row's files, each test file the phase changed, and `tests/lib`,
`tests/skills`, `tests/text` and `tests/behaviour`. It also covered the
files outside those that load a changed module: `tests/e2e/teammate`,
`tests/github/test_release_seal.py`, `tests/github/test_finding_counts.py`,
`tests/evals/test_replay_targets.py`, `tests/evals/test_rule_cases.py`,
`tests/test_censuses.py` and `tests/test_conftest.py`.
