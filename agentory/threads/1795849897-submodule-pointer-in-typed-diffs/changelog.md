### Fixed

- **A diff a party reads by hand now shows a commit that only moves a submodule's pointer (#1648).** The inspector's `git diff <base>...HEAD`, and the `git log … -p` and `git show <merge>` a round types after a merge of the base, now carry `--ignore-submodules=none`. Before, a repository whose `diff.ignoreSubmodules` read `all`, or whose `.gitmodules` entry read `ignore = all`, hid the moved pointer from all three, so a pull request could move a submodule with no round and no inspector seeing it. The scripts already carried the flag.
