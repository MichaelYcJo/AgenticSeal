# Closing memo: 1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the work item's last commit | the orchestrator, at the broad gate |
| Phase 1's S1 case, `tests/skills/test_broad_gate.py#Test_main.test_a_malformed_sprite_leaves_the_verdict_and_the_report_as_they_were`, on Windows. Phase 1 ran it on macOS alone | CI's `windows-latest` legs of `.github/workflows/test.yml`, on the pull request |
| `seal stamp` with no argument, and `seal stamp --guarantee`, beside a malformed sprite. Phase 1 read both from `seal_stamp.py#main` and `#queue_for_written_guarantee` and ran neither | the proofer, at round 1 |

## Not done

Phase 1 took nothing of phase 2 of `frame/plan.md` *Phases*, *Scope*
item 5, which a later crafter builds.

`skills/code-review/orchestration.md:533` still names a `python3` that
cannot load `seal_stamp.py` as the case where the `Stop` hook draws
nothing, and not a malformed sprite. `frame/design.md` *Scope*, *Out*
leaves it to #1579, which moves that paragraph in this release.
