# Overview: 1793140810-each-directory-holds-everything-in-one-level

## Why this work exists

`templates/`, `hooks/` and `tests/` each held two kinds of file in one level, so a reader found a file by reading the whole listing; each now holds its kinds in their own directories, and `docs/README.md` groups the policy documents by subject.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Three readers globbed `templates/` one level deep | `frame/plan.md` row 1's reader list names the code joins, `install.sh`, the `$CLAUDE_PLUGIN_ROOT` paths, the gate messages and the citations; `.github/scripts/rules.py#RULE_FILES`, `tests/test_the_record_is_written_in_words.py#CORPUS` and `tests/test_a_record_carries_no_comment.py` read `templates/*.md` and matched nothing after the move | each reads `templates/*/*.md`, or `templates/records/*.md` for the record-comment case | a glob that matches nothing passes silently, and `RULE_FILES` would have stopped reading any `check:` line a template later carries |
| Where the census `vacated_paths` reads | `frame/design.md` *Data & interfaces*: "each tracked file" | it lists the moved-into subdirectories on disk, so its cases need no git, like the other censuses' cases | an untracked file in such a directory vacates its old spelling too |
| A vacated spelling inside a longer path | `frame/design.md`: a spelling inside a longer path is not refused | a spelling after a shell variable, `$CLAUDE_PLUGIN_ROOT/templates/...`, is refused; `skills/update/SKILL.md`'s `marketplaces/agenticseal/templates/` path was rewritten | `frame/plan.md` row 1 names the `$CLAUDE_PLUGIN_ROOT` paths as readers of the move |
| The census's `KEPT_FILES` | `frame/design.md`: the census passes the files of its own `KEPT_FILES` | phase 1 adds no such constant; phase 2 creates it with `hooks/lib/cmdline_base.py` | no file keeps a vacated `templates/` spelling |
| The gates that import `worktree_consent` | `frame/design.md`: each gate inserts `os.path.join(..., "lib")` where it inserted its own directory | `question-gate.py`, `routing-edit-gate.py` and `worktree-guard.py` keep their own-directory insert and add the `lib` insert after it; the twelve others replace theirs | `worktree_consent.py` is a gate and stays at the top of `hooks/` |
| The census's kept-files constant | `frame/design.md`: the census passes "its own `KEPT_FILES`" | `tests/censuses.py#VACATED_KEPT_FILES` holds `hooks/lib/cmdline_base.py` | `KEPT_FILES` is `old_names`' constant |
| A fourth reader that lists `hooks/` one level deep | `frame/plan.md` row 2 names three such readers | `tests/test_the_root_migrates_itself.py#test_no_hook_names_the_0_3_x_roots` lists `hooks/` and `hooks/lib/` | after the move it would have checked no module |
| A historical line that names a vacated path | `frame/design.md` keeps records at their old paths | five living lines that state a past fact name the path as `<commit>:<path>`, and two keep `hooks/blocks.py` under a `vacated_paths` exemption because the replay reads commits cut before the move | a living line naming the old path is refused by the census; a commit-tied path is the form `docs/the-record-layout.md` states |
| Imports between test files in different directories | `frame/design.md` *Data & interfaces*: "the other helper imports keep working from every subdirectory" | `tests/conftest.py` puts every directory under `tests/` that holds a test file on `sys.path` when it loads | three top-level files that import from a moved file failed with `ModuleNotFoundError` when collected alone, and passed in a full run only by the order in which directories sort |
| Readers that listed `tests/` one level deep | `frame/plan.md` row 3 names `test_layout.py --check` and the `check:` lines | `test_layout.py#_moved_main`, `tests/skills/test_arm_check.py#selects_this_module`, `tests/test_one_word_one_meaning.py` and the session-cost segment join read the areas, the first two with a case seen red | each would have read no file under an area |
| `tests/evals/test_seed_defects.py` after phase 2 | phase 2's narrow run did not include it, and its scaffold copied every `CHECK_FILES` entry from the working tree, `hooks/blocks.py` among them | the scaffold skips an entry the tree does not hold | `hooks/blocks.py` is a spelling `CHECK_FILES` keeps for commits cut before the move |
| `CONTRIBUTING.md` *The test layout* | `frame/plan.md` row 3 rewrites it in place | phase 3 states the area rule; the rule that a test file takes its root from `conftest.ROOT` is phase 4's, with its case | the root rule's case is phase 4's |
| Where the nine edge files stand | `frame/design.md` *Data & interfaces* counts 43 behaviour files and 48 text files | 52 and 39: nine files that run shipped code through a helper imported from a module test file stand in `tests/behaviour/` | the criterion's own words, "loads or runs shipped code", send them there |
| What the root case reads | `frame/plan.md` row 4: no file under `tests/` but `conftest.py` computes the root from `__file__` | the case reads `test_*.py` files only; `tests/censuses.py` keeps its own root | `evals/scripts/noninferiority.py` loads `censuses.py` by path without pytest |
| What the name case reads | `frame/plan.md` row 4: no two test files share a name | the case reads `.py` files under `tests/` | only Python files are imported by name, and a `.DS_Store` may stand in several directories |
| Where the two cases stand | `frame/plan.md` row 4 names `tests/test_conftest.py` | both stand in `Test_module` | the tree's `seal layout --check` refuses a class that names no top-level definition of `tests/conftest.py` |
| Two cases that named a removed skill | `frame/design.md` *Removes* names the eight skills and their README rows, and *Scope* says the only mentions are the READMEs and the skills' own `NOT for` clauses | `test_migrated_commands_stay_user_invoked` checks `preset-setup` alone, and `test_installer_prints_commands_a_user_can_actually_type` reads `preset-setup` and `parity-setup` | each case named `security-audit` and `testing` as shipped commands, and the first asserted their `SKILL.md` exists |
| The changelog fragment's template | the spawn prompt for phase 5 names `templates/records/sdd-changelog.md` | the fragment takes the shape of the 0.23.0 fragment at `ab14194b:seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/changelog.md` | no such template exists in the tree |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, through the tree's `bin/seal gate` after the review rounds settle |

## Not done

nothing

## Fed back into the spec

none
