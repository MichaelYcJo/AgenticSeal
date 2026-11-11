"""Whether a change reaches outside the document roots, which the parity arm
asks at the pull request.

The rule is `docs/running/the-review-and-parity-arms.md` *Parity arm*: a change
confined to `docs/` and `seal/` owes no comparison with an original, because
nothing there can be compared against one. `skills/code-review/scripts/
chain_check.py#originals_of` loads this file through `lib/sibling.py` and
asks `touches_code` of the paths the pull request changes, with the name of
the root in force at HEAD, which a project's own `seal/` changes.
"""


def touches_code(paths, home):
    """True when one of `paths` is outside the document roots, or when
    `paths` is None: a change git could not list is not a change confined to
    them, so the parity arm asks. The roots are `docs/` and `<home>/`,
    HOME the root's repository-relative name as `lib/optin.py#home_name`
    gives it, and `docs/` alone where HOME is "". PATHS are as `git diff`
    prints them, repository-relative and `/`-joined."""
    if paths is None:
        return True
    roots = ("docs/", f"{home}/") if home else ("docs/",)
    return any(not path.startswith(roots) for path in paths)
