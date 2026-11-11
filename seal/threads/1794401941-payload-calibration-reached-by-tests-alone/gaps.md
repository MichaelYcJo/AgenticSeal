# Closing memo: 1794401941-payload-calibration-reached-by-tests-alone

## Not verified

| Item | Who must answer |
|---|---|
| the suite, the repository-wide lint and the format check beyond phase 1's boundary set | the orchestrator's broad gate |
| the suite, the repository-wide lint and the format check beyond phase 2's boundary set, the module test files that reach `lib/optin.py`, `lib/routing.py`, `lib/lines.py` or `seal_stamp.py` only through a script that loads them among it | the orchestrator's broad gate |

## Not done

Phase 1 kept two sentences that give the reason a token figure is labelled
an estimate by citing "the six calibration spawns": the `tokens` paragraph
of `skills/verify/scripts/payload_meter.py`'s module docstring, and the
second paragraph of `tests/skills/test_payload_meter.py`'s. Each states why
a bare token number is refused, which still holds, and recounts where the
numbers came from. `frame/design.md` *Out of scope* gives such history to
#1485.

`payload_meter.py#_fence_rule` keeps its name, though the meter now asks
`lib/blocks.py` only for its line split. Its docstring says so. A rename
is not part of the cut that `frame/design.md` *Scope* states.
