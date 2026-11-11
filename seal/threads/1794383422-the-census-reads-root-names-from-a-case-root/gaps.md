# Closing memo: 1794383422-the-census-reads-root-names-from-a-case-root

## Scope confirmation

`tests/censuses.py#_root_names` reads `lib/optin.py` from the repository the census module stands in, not from `ROOT`, and the plugin's version moves to 0.37.4; nothing else changes.

## Not verified

- nothing
  why: the two cases were seen red alone in a fresh process (`bin/test tests/test_conftest.py -q -k Test_census_case -p no:xdist`, 2 failed) and green after the change, and `tests/test_conftest.py` passes whole (49 passed); the broad gate runs before the seal.

## Not done

nothing
