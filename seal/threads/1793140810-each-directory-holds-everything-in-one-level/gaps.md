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

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, through the tree's `bin/seal gate` after the review rounds settle |

## Not done

nothing

## Fed back into the spec

none
