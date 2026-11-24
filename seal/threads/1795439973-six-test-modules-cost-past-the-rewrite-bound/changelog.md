### Changed

- **Six test modules build their repositories once and read most commands without git (#1581).** On the Windows leg of `tests`, the six modules summed to 1,267 s in run 45181872904 and to 320 s in run 45256397846. Only test files changed, and no shipped file did.

  | Module | Run 45181872904 | Run 45256397846 |
  |---|---|---|
  | `tests/skills/test_chain_check.py` | 601 s | 132 s |
  | `tests/skills/test_settle.py` | 253 s | 75 s |
  | `tests/skills/test_seal.py` | 107 s | 48 s |
  | `tests/skills/test_test_layout.py` | 106 s | 17 s |
  | `tests/skills/test_broad_gate.py` | 105 s | 40 s |
  | `tests/github/test_release_seal.py` | 95 s | 8 s |

  Each module builds the repositories its classes need once per module. A case that writes takes a copy. A case whose fact is how a command reads its input calls the reader with that input in the process, or runs the command with the readers it does not test answered for it. A case whose fact is that the reading and git agree still runs git. Each command keeps at least one run of each arm over a real history with every reader real.
- **Two of the six stay above 60 s on the Windows leg, and a third may in a slow run.** Each record gives one verdict per case that costs more than 0.5 s. The case became a call. Or it runs the command with the readers it does not test answered, and the record names what of the command it holds. Or it kept real git, and the record names the answer of git it holds. The records are this work item's, under `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/`, and git history keeps them after the settle. The orchestrator's judgment of each module stands in that directory's `frame/plan.md` *Judgments of the run*.
  - `tests/skills/test_chain_check.py` read 132 s. `trail/phases/phase-9.md` gives the verdict of each of its 99 listed cases.
  - `tests/skills/test_settle.py` read 75 s. `trail/phases/phase-11.md` gives the verdict of each of its 88 listed cases. Its *Q2* puts about 21 s in one run per arm and in the classes of readers that ask git. It puts about 40 s in 50 cases that each hold an answer of git no other case holds.
  - `tests/skills/test_seal.py` read 52 s in run 45249520034 and 48 s in run 45256397846. Between phases 6 and 10 it read 50 s, 81 s and 70 s in three runs with nothing changed in it, so a slow run may put it above 60 s. `trail/phases/phase-10.md` *Q2* gives its floor.
- **Each module has its own seams for a new case.**
  - `test_settle.py`: `drawn` is a world with no history. `answered` answers `settle.py`'s ten readers that ask git from the disk, and `real` names the ones a case keeps. `at` runs `survey` at a ref and then `report`, or `apply` under `--apply`; a `--draft` case runs `settle.main`. The `gh` fixture answers in the process, and one case keeps a `gh` script on `PATH` (`gh_on_path`). `imported`, `committed` and `merged_history` write a history in one `git fast-import`.
  - `test_chain_check.py`: `reading` hands an arm its records. `answered` answers `read_record`, `tracked_files` and `follows` for a `main` run. `imported` and `born` write the templates.
  - `test_seal.py`: `at_top` gives a command the top of its copy. `guards_answered` answers a mode switch's guards. `beside_the_package` writes the package's files into a copy.
  - `test_broad_gate.py`: `history` writes a world in one process. `arms_answered` and `suite_alone` answer the arms a case does not test. `a_sealed_run` is one run of the gate that two cases read.
  - `test_test_layout.py`: `Test_moved` calls `moved` with texts from `WORLD`, and the cases that run `main --moved` stand in `Test_main`.
  - `test_release_seal.py`: `wired` records a ten-line suite whose counts differ from every other count in the header.
- **The names other test files import keep their behaviour.** These are `test_settle.unanswered` and `past_the_bound`, `test_seal.configured` and `tool`, `test_broad_gate.unquoted_flat` and `gate_module`, and `test_test_layout.layout`.

### Removed

- **`tests/skills/test_settle.py`'s own `git` and `commit` helpers, its `settled_repo` builder, and its `repo` and `local` fixtures.** Its cases reach `tests/conftest.py#git_out`, `#git` and `#commit_everything`, and module worlds copied per case.
- **`tests/skills/test_chain_check.py`'s per-case builders.** `bodied_with`, `reseal`, `direct_migrating`, `planted_spec` and `migrating` are gone. `Test_declared_for_this_branch::test_accepts_a_shared_root_and_tells_it_to_add_the_file` is cut too: `test_the_shared_sentence_says_what_it_searched_and_for_what` reads the same sentence over the same world and holds both of its assertions.
- **Two cases of `tests/skills/test_broad_gate.py`.** `Test_gate::test_accepts_a_failure_the_base_shares_as_failing_on_base_too` is cut, and `Test_gate::test_refuses_a_red_suite_an_act_after_the_run_loop_turned_to_exit_0` now asserts `failing on base too` over a red base. `Test_gate::test_accepts_a_green_suite_a_late_hook_exits_with_0` is cut, and `Test_read_record::test_accepts_a_green_session_a_late_hook_exits_with_0` holds its reading.
