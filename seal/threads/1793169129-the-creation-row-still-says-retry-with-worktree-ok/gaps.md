# Overview: 1793169129-the-creation-row-still-says-retry-with-worktree-ok

## Why this work exists

Under the automation press, the single-stream creation deny in another clone told the model to get the user's confirmation and retry with `[worktree-ok]`, which led to a person's prompt in a run that promised none; it now ends with the press sentences instead, and the attended text is unchanged.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| How row 5's pressed ending is joined to the switch lines | `frame/design.md` *Data & interfaces*: "ends the reason with the switch command lines, then `"\n\n"`, then `press_sentence() + reissue_sentence()`". Code: `switch_lines(git) + "\n\n" + press_sentence() + reissue_sentence()`, where `switch_lines` ends on its last command line with no newline | the code, which matches the spec's exact reason | `frame/design.md` *In* quotes the reason word for word, with one blank line between the last switch line and the press sentence. The test helper `single_stream_deny` builds that text, and S1 compares the whole reason against it |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck, including whether `.test_durations` still prices the suite with this work's three new node ids unpriced | executed by the orchestrator's broad gate at `4a568c76` against `977b6613`, passed (`trail/gate.md`), `test_the_durations_file_prices_the_suite` among the suite it ran, and this repository declares no typecheck (`seal/config.md` *Broad gate*; #951 would add one) |

## Not done

Row 2's `ask` under the press is unchanged, on P1's default (a) in `frame/questions.md`. The owner has not answered P1, and the orchestrator reports the default.

`docs/worktree-guard-spec.md` is unchanged. `frame/design.md` *Rule changes* carries its two `change` items, and the settle writes them.

No `.test_durations` key was added for the three new cases, because a duration nobody measured on Windows would be a made-up number.

## Fed back into the spec

none
