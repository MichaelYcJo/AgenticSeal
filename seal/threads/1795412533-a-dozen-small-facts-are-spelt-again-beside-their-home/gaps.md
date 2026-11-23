# Closing memo: 1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the build's last commit, after the base merge that brings in #1576. `8b8b434b5` merged #1572 and #1574 | the orchestrator's broad run, after the review rounds settle |
| Phase 3 on Windows: the fourteen entry points given a call of `console.to_utf8()`, thirteen by phase 3, `tests/run_tests.py` among them, and `skills/verify/scripts/session_cost.py` by round 1's fix pass, at a cp1252 console, and `tests/skills/test_pact_check.py`'s Windows-joins case, whose join now differs by whether a path is absolute. Both were run on macOS alone | the `windows-latest` jobs of `.github/workflows/test.yml` on the pull request |
| Phase 4's install lines: `pip install -r tests/requirements.txt pytest-split==0.11.0` in every leg of `.github/workflows/test.yml`, and the `pip install -r` fallback of `CONTRIBUTING.md` *Running the checks*. Neither was run; the `uvx --with-requirements` fallback was run on macOS and installed the file's packages | the `pytest` and `pytest-wide` jobs of `.github/workflows/test.yml` on the pull request |
| The `seal` job of `.github/workflows/publish-release.yml` installing `-r tests/requirements.txt` from the checkout of the tag. It runs only when a release is published | the `publish-release` run of the release that ships this work |

## Not done

`fold_check.py#declared` still opens `config.json` twice: once through `config_pairs` for the ceiling key, and once inside `lib/config.py#declared_policy_root`. The key is read once, which is what `frame/design.md` *Scope* item 2 asks. Reading the file once would need `declared_policy_root` to take the parsed pairs, and `frame/design.md` *Data & interfaces* gives it `home`. The second open costs one small file read per `seal fold` run, and it was so before this phase, through `policy_root`.

`tests/behaviour/test_every_entry_point_runs_at_the_floor.py#loaded_by` still leaves out every path under `tests/`. The runner's `PINS` named its pins' test modules by tracked path, and since phase 4 no line of the runner names one. The exclusion stays, because the reason its docstring gives does not rest on `PINS`: `tests/` holds no module of the plugin, and pytest imports a test module at the virtualenv's floor. `test_a_script_reaches_no_module_under_tests` holds it on a fixture. Whether a guard no tracked script now reaches stays is the review round's to judge against `skills/core/SKILL.md` *The rule a mechanism is kept against*.
