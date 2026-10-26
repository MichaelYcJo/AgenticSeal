"""Whether a change reaches outside the document roots, which the parity arm
asks at the pull request.

The rule is `docs/the-review-and-parity-arms.md` *Parity arm*: a change
confined to `docs/` and `seal/` owes no comparison with an original, because
nothing there can be compared against one. `skills/code-review/scripts/
chain_check.py#originals_of` loads this file by path and asks `touches_code`
of the paths the pull request changes.

The commit gate's arms, its refusal texts and its marks lived here until
#1027 removed every hook of this plugin that ran inside git.
"""

# `seal/` as a string rather than `optin.HOME` joined under anything: these
# classify paths as `git diff` prints them, repository-relative.
DOC_ROOTS = ("docs/", "seal/")


def touches_code(paths):
    """True when one of `paths` is outside the document roots, or when
    `paths` is None: a change git could not list is not a change confined to
    `docs/` and `seal/`, so the parity arm asks (#868)."""
    if paths is None:
        return True
    return any(not path.startswith(DOC_ROOTS) for path in paths)
