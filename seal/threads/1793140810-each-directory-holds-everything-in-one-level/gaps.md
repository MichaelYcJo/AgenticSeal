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

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, through the tree's `bin/seal gate` after the review rounds settle |

## Not done

nothing

## Fed back into the spec

none
