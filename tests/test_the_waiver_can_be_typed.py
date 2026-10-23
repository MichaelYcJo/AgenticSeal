"""The gate names a way past itself, and that way has to actually run.

For three releases the prompt said to re-issue the command "with `[no-review]`
as a BARE WORD". Following it produced:

    error: pathspec '[no-review]' did not match any file(s) known to git

After `git commit`, a bare word is a pathspec. The marker was being READ
correctly and TYPED somewhere git would never accept, so the gate stopped the
commit, the escape it offered failed, and approving the prompt was left as the
only thing that worked — which is the outcome the wording exists to avoid
(issue #50).

The issue proposed a trailing `# [no-review]` comment. Measured, that is not
the fix either: it commits under bash and under `zsh -c`, and fails in an
INTERACTIVE zsh, whose default leaves `#` uncommented and then refuses
`[no-review]` as an unmatched glob before git is reached. That last case is
not automated — an interactive shell in CI sources a user's rc and needs a
tty — so it is recorded rather than run: `printf 'git commit -m x  #
[no-review]\\n' | zsh -i` gives `zsh: no matches found: [no-review]`.

The cases that run the form the gate now advises, in every non-interactive
shell available, against real git, are in `tests/test_commit_review_gate.py`'s
`Test_main` and `Test_module` (#942's phase 6).
`docs/the-review-and-parity-arms.md` names this file on a `check:` line until
the work item's rule change for it is settled, so the file stays with no case.
"""
