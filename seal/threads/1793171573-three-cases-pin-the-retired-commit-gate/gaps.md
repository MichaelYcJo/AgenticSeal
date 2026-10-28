# Overview: 1793171573-three-cases-pin-the-retired-commit-gate

## Scope confirmation

Delete the three cases of `tests/behaviour/test_the_hook_surface_git_offers.py` that #1039 names, with the `AUTHOR_DATE_LOG` hook they alone use and their three `.test_durations` entries, and rewrite the module docstring to state what the seven remaining cases pin for `docs/worktree-guard-spec.md`; no other file changes unless a citation of the three cases turns up outside this work item's records.

## Why this work exists

Three cases pinned facts that only the commit gate inside git needed, and
that gate left git in #1027, so they cost 16.3 s of the serial suite and
guarded no rule. The module now holds only the seven cases that the worktree
guard's two rules rest on, and its docstring says which case pins which rule.

## Where spec and implementation diverged

None. The issue's coordinates held at `27a6bb6d`, and the build followed it.

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check` on this branch, including `test_the_durations_file_prices_the_suite` against the three removed entries | the orchestrator, through `seal gate` |

## Not done

No `changelog.md` fragment is written. The change removes three cases from
this repository's own suite and changes nothing a plugin user installs, runs
or reads, so a release note would have nothing to tell them. The 0.22.4
settle's removal of caseless test files (#1028) has no entry in
`changelog/0.22.4.md` either.

`seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/design.md:172`
still names both removed markers. It is another work item's record of the
issue text at the time it was written, so it is left as written.

## Fed back into the spec

none
