# Phase 5: 1793174170-two-facts-kept-in-several-files-have-drifted

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | 53fbc4ff |

## What this phase was asked

Build `frame/plan.md`'s phase 5, the editions and the manifest. `pairs()`
reads every tracked pair (S11), the `CONTRIBUTING.md` sentence names every
pair (S12), and the plugin description case is added (S13). Write the
`changelog.md` fragment, and close `gaps.md`.

## What this phase found

- **The frame held at this tree.** `git ls-files "*.ko.md"` lists four
  files, and each has an `X.md` beside it: `README`,
  `docs/one-root-by-lifetime`, `docs/experiments/README` and
  `docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force`. The
  three `.claude-plugin/` descriptions were equal (read).
- **S11 and S12 seen red, then green.** With the new assertions and
  `pairs()` as it stood, the module failed two cases with exit 1: `pairs()`
  returned `['one-root-by-lifetime']` alone, and `CONTRIBUTING.md` still
  said "every top-level". After `pairs()` read git's listing and the
  sentence was rewritten in place, the module passed, 6 cases, exit 0. All
  four pairs agree on their outline, as the frame measured (executed).
- **`pairs()` now returns repository-relative names**, and `read` joins
  them under the root through `under_root`, which splits the name on `/`.
  The listing words stay at the call site, as `tests/conftest.py#git_listing`
  asks. The module's `DOCS` constant had no other reader and went.
- **S13 is a case that passes at the base**, because the three copies
  agree there. It was seen red by `seal mutate` on each copy in
  `marketplace.json`, the top-level description and the plugin entry's,
  each `red` with exit 0. The case sits in
  `tests/behaviour/test_chain_hooks_hardening.py`, which already reads
  `.claude-plugin/plugin.json` (executed).
- **Each new unit was mutated, and each went red.** `seal mutate` printed
  `red` with exit 0 for six mutants: a `## planted` heading added to
  `docs/experiments/README.ko.md`, which holds only its title heading, a
  heading level changed in `README.ko.md`, "every top-level" put back into
  `CONTRIBUTING.md`, the two `marketplace.json` copies, and the listing
  narrowed to `docs/*.ko.md`. A first try at the planted heading derived its
  old text from a `##` line the file does not have and was refused with
  exit 2 before anything was written (executed).
- **Every module that reads a file this phase changed ran green.** The
  readers of `CONTRIBUTING.md` and `marketplace.json`, the census module and
  the two changed modules, 31 modules, one per call, each exit 0. `uvx ruff
  check` and `uvx ruff format --check` passed over the two changed test
  files (exit 0, executed).
