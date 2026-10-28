### Removed

- **`invocation_dir` on the broad gate recorder's `session` line, and `wasxfail` on its `test` lines (#1056).** `seal gate` read neither field. A record kept with `--keep-output` no longer carries them.
- **Guards that no input reached (#1056).** These go: the `if not session` return in `hooks/worktree_consent.py#main`, and three guards in `.github/scripts/issue_claims_check.py`. Those three are the segment-end bound and the skip of a segment with no claim in `read`, and the whitespace filter in `segments`. Two except clauses in `skills/implement/scripts/seal.py` no longer name an exception beside its own base class: `NotImplementedError` in `import_` and `UnicodeDecodeError` in `read_manifest`. No command, hook or script prints, writes or exits differently.
