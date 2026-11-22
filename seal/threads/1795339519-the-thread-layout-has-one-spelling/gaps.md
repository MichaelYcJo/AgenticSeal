# Closing memo: 1795339519-the-thread-layout-has-one-spelling

## Scope confirmation

Eight scripts read a thread's file names from `lib/optin.py` (and `routing.md` from `lib/routing.py#FILENAME`) and the round records through `lib/routing.py#rounds`; `broad_gate.quote`, which had no caller, goes, and `seal_stamp.quote` keeps its reasons; both `plugin_version` functions read the manifest through `lib/core.py#manifest`; the plugin's version moves to 0.38.5. No verdict or output changes.

## Not verified

- nothing
  why: the narrow suites of every touched module and of `lib/routing.py` and `lib/core.py` pass (`bin/test -q` over twelve files, 1983 passed, 1 skipped, at the build commit's tree); `Test_rounds`, moved to `tests/lib/test_routing.py`, was seen red with `lib/routing.py#_ordered` sorting by name (1 failed) and green after the revert; the broad gate runs before the seal.

## Not done

The class was listed by a search over every script outside `lib/`, `tests/` and `evals/` for each name `lib/optin.py` and `lib/routing.py` define as a code literal, then for the round-record pattern. A name built another way, such as by concatenation, is outside what that search reaches. `evals/scripts/rule_cases.py` writes record files into fixture repositories by their names; it builds a corpus rather than reading one, so it stays.

`quote` stays in `seal_stamp.py` rather than moving under `lib/`, as the issue's *Done when* first said: `seal_stamp.py` is its one caller, so a module under `lib/` would hold one function for one reader.

`chain_check.py#changed_routing` reads `lib/routing.py#FILENAME` through `sibling.load` rather than taking `routing` as a parameter, so its signature and its two cases stay as they were.

The seven `git()` helpers with differing failure semantics are outside this work item, as the issue says.
