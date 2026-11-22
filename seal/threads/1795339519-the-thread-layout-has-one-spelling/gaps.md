# Closing memo: 1795339519-the-thread-layout-has-one-spelling

## Scope confirmation

Eight scripts read a thread's file names from `lib/optin.py` (and `routing.md` from `lib/routing.py#FILENAME`) and the round records through `lib/routing.py#rounds`; `broad_gate.quote`, which had no caller, goes, and `seal_stamp.quote` keeps its reasons; both `plugin_version` functions read the manifest through `lib/core.py#manifest`; the plugin's version moves to 0.38.5. No verdict or output changes.

## Not verified

- nothing
  why: at the build commit's tree, `bin/test -q` over `tests/skills/test_broad_gate.py`, `test_chain_check.py`, `test_seal_stamp.py`, `test_seal.py`, `test_settle.py`, `test_rule_changes.py`, `test_pact_check.py`, `test_session_cost.py`, `test_unverified_check.py`, `test_pr_body.py`, `tests/lib/test_routing.py` and `tests/lib/test_core.py` passed (1983 passed, 1 skipped); after round 1's fix pass, `bin/test -q tests/text tests/behaviour` with the four test files of the modules it changed passed (2041 passed, 10 skipped); `Test_rounds`, moved to `tests/lib/test_routing.py`, was seen red with `lib/routing.py#_ordered` sorting by name (1 failed) and green after the revert; the broad gate runs before the seal.

## Not done

The class was listed by walking every string constant that is not a docstring in each tracked Python file outside `lib/`, `tests/` and `evals/`. Each constant was split into tokens on whitespace, backticks, quotes, brackets and punctuation, and each token on `/`, and a part equal to a thread's file or directory name `lib/optin.py` or `lib/routing.py` defines, or holding `round-`, was kept. The build's first search found only a constant whose whole value is the name; round 1 named the six it missed inside longer literals, and the fix pass reads each through its module. A name built at run time, such as by concatenation, is outside the walk. At the fix pass's tree, every constant the walk keeps is one of four kinds, and each stays: a sentence of a message or of help text that names a thread's file to a person, such as `settle.py`'s `no note read` sentences, which name `changelog.md`; a panel or table label, such as `rounds`; a key of `settle.py`'s own dictionary, `found["threads"]`; and a part of a finding's coordinate, such as `chain_check.py`'s `round-<N>#<n>`, which is `lib/fields.py`'s grammar and no file name. No script reads or joins a path through any of them. `evals/scripts/rule_cases.py` writes record files into fixture repositories by their names; it builds a corpus rather than reading one, so it stays.

`quote` stays in `seal_stamp.py` rather than moving under `lib/`, as the issue's *Done when* first said: `seal_stamp.py` is its one caller, so a module under `lib/` would hold one function for one reader.

`chain_check.py#changed_routing` reads `lib/routing.py#FILENAME` through `sibling.load` rather than taking `routing` as a parameter, so its signature and its two cases stay as they were.

The seven `git()` helpers with differing failure semantics are outside this work item, as the issue says.
