# 1791384157-the-hooks-read-the-session-waiver-and-creation-one-way — phase 11

| Field | Value |
|---|---|
| Phase | 11 |
| Commit | 63a518a8 |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

The second reframe, built on `questions.md` P2's default, delete (S25–S28,
In 6). Merge `origin/release/v0.21.0` at `ad447367` first, never a rebase.
Then take out every unit `spec.md` In 6 lists for this phase: the guard's
brace test and quoting reader, every `braced` parameter and arm, the union of
`-C` trees, the brace stop text and `main`'s brace read, with `_finding_tree`
the one tree lookup `main` calls. Remove the thirteen brace cases, their
three constants and the two brace policy pins. Invert the braced half of
`test_no_listed_form_moves_head_under_git`, add
`test_a_shell_built_word_is_the_named_limit`, and show both red at
`52c72bbe`. Name the limit once in §*Known limits*, give
`docs/the-commit-gate-inside-git.md` the rebase sentence with its pin and the
hook-surface case its `rebase main other` parameter, and rewrite the
changelog's brace bullet.

## What this phase found

**The merge was clean.** `ad447367` touched none of this phase's files:
`git diff 52c72bbe HEAD -- hooks/worktree-guard.py docs/worktree-guard-spec.md
docs/the-commit-gate-inside-git.md` and the three test modules were empty
after it, so a case red against the tree before this phase's edits is red at
`52c72bbe` (merge `048506e7`).

**Red at `52c72bbe`, executed** before any code left the tree. Nine failed:

- the braced half of `test_no_listed_form_moves_head_under_git`, naming all
  four forms (`rebase {main,feature/x}`, `rebase --ro{,} feature/x`, `stash
  {branch,} y`, `worktree {add,} ../wt62 feature/x`);
- six of the eight parameters of `test_a_shell_built_word_is_the_named_limit`,
  the four #856 forms and `cat {a,b}` and `echo {a,b}`; the two quoted forms
  were silent there too;
- `test_the_guard_policy_names_the_shell_built_word_limit` and the extended
  `test_the_policy_names_the_one_session_reader`, each on its first missing
  sentence.

**The inverted half asks `main` too.** Read off `shape_of` alone it was green
at `52c72bbe`, because `shape_of` defaulted to no brace there and only
`main` passed the command's brace read. So the half asserts both: the guard
reads each form as listed, and `main` is silent on it in an ACTIVE tree. The
case takes `monkeypatch` and `capsys` for that.

**S28 on git 2.50.1, executed.** `git rebase main other` reaches
`reference-transaction` the way `switch` and `checkout` do; the parameter
passes beside them, the tree on `other` and the line naming
`refs/heads/other`. The CI floor leg answers for 2.34–2.43.

**Where the frame does not hold, and what was built instead.**

- S27 says the hidden-spelling bullet keeps its `{add,}` example. That
  bullet says such a creation is an unrecognised shape. With the reader gone,
  `git worktree {add,} ../wt f` is listed. Keeping the example would state
  something the tree no longer does. The bullet goes back to 0.20.0's
  wording, and the new limit bullet names `{add,}`.
- In 5 keeps `_rebase_names_a_branch`'s docstring as phase 3 corrected it.
  Its last clause said a brace segment "is unrecognised before this is
  asked", which stopped being true. The clause now points at the limit
  comment, and phase 3's `_plain_words` sentence stands.
- `_two_trees` (NAME NOT IN TREE since this phase), a helper In 6 does not list, served only removed cases. It
  went with them.
- The guard grep finds three lines, not one: the limit comment (two lines)
  and line 404, 0.20.0's note that `cmdline.understood` refuses a brace
  group. That note is about a `{ …; }` group, not an expansion, and stays.

**W5's answer.** Retired: the thirteen cases and three constants In 6 lists,
and `_two_trees` (NAME NOT IN TREE since this phase). Inverted: the braced half of the git-binding case. New:
`test_a_shell_built_word_is_the_named_limit` and
`test_the_guard_policy_names_the_shell_built_word_limit`.

**Verified by, executed at `63a518a8`:** the five modules the plan names
(the result is in the plan's Status row); `uvx ruff check hooks/ tests/`, all
checks passed; `grep -n 'brace\|_BRACE\|braced' hooks/worktree-guard.py`,
the three lines above; the text checks `tests/test_docs_line_wrap.py`,
`tests/test_release_hygiene.py` and
`tests/test_every_reader_ends_a_line_where_gfm_does.py`, 242 passed.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| `_BRACE` and `_unquoted_brace` in `hooks/worktree-guard.py` — NAME NOT IN TREE since this phase | nowhere: the limit comment above `Finding` and §*Known limits* say why nothing reads the brace |
| the `braced` parameter of `_git_finding`, `_segment_finding`, `shape_of`, `_merged_findings` and `_first_finding_in`, and each brace arm | nowhere |
| `_finding_trees` — NAME NOT IN TREE since this phase | `_finding_tree`, which `main` calls for every unrecognised shape, as at 0.20.0 |
| the `brace` branch of `_described`, both languages | nowhere: no stop names a brace |
| `BRACE_SHAPES`, `BRACE_EN`, `BRACE_KO` and `_two_trees` in `tests/test_worktree_guard.py` — NAME NOT IN TREE since this phase | nowhere |
| thirteen brace cases in `tests/test_worktree_guard.py`, listed by name in `spec.md` In 6's fence | `test_a_shell_built_word_is_the_named_limit` and the inverted half of `test_no_listed_form_moves_head_under_git` pin the limit |
| the two brace policy pins in `tests/test_guard_resolves_the_tree_it_judges.py`, named in In 6's fence | `test_the_guard_policy_names_the_shell_built_word_limit` |
| §A's brace paragraphs (In 6 counts four; the text held three, from "A brace expansion is unrecognised (#856)" to the line before "A creation is §B's"), the brace sentence of *The failure direction*, the brace-hidden `-C` sentence of the `sh -c` bullet, the `{add,}` example of the hidden-spelling bullet, and every `Enforced by:` entry naming a removed case | the limit bullet in §*Known limits* |
