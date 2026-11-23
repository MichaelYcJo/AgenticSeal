# Closing memo: 1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the build's last commit, after the base merge that brings in #1576 and #1572 | the orchestrator's broad run, after the review rounds settle |
| Phase 3 on Windows: the twelve entry points that now call `console.to_utf8()` at a cp1252 console, and `tests/skills/test_pact_check.py`'s Windows-joins case, whose join now differs by whether a path is absolute. Both were run on macOS alone | the `windows-latest` jobs of `.github/workflows/test.yml` on the pull request |

## Not done

`fold_check.py#declared` still opens `config.json` twice: once through `config_pairs` for the ceiling key, and once inside `lib/config.py#declared_policy_root`. The key is read once, which is what `frame/design.md` *Scope* item 2 asks. Reading the file once would need `declared_policy_root` to take the parsed pairs, and `frame/design.md` *Data & interfaces* gives it `home`. The second open costs one small file read per `seal fold` run, and it was so before this phase, through `policy_root`.

`broad_gate.py#rounds_rows` still loads `chain_check.py` inside `sibling.going_on()`, and still names an absent check in its own line and counts nothing for a check that raises. Since phase 2, `broad_gate.py#main` loads the check before any arm runs, so `seal gate` never reaches that block without the check. The block was not removed. Its two cases, `Test_rounds_rows::test_refuses_to_stop_a_run_where_the_check_will_not_load` and `test_names_the_absent_check_in_its_own_line_and_goes_on`, call `rounds_rows` directly, where the block still answers. #1572's branch adds two more callers of `sibling.going_on` and its own cases, so `lib/sibling.py#going_on` stays either way. Whether the block and its two cases go is the review round's to judge against `skills/core/SKILL.md` *The rule a mechanism is kept against*.
