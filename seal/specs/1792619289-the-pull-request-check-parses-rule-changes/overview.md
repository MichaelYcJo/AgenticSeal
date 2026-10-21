# 1792619289-the-pull-request-check-parses-rule-changes — overview

## Why this work exists

A spec's `## Rule changes` section was first parsed at the owner's settle, after the release, where a section that does not parse applies nothing and no pull request is left to fix it in; `chain-check` now parses it at the pull request that carries the work item.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| S7's setting | `spec.md` S7: "Given S1's spec under a declaration whose `Planning` row reads `the session`", and "the `branch` fixture already declares `the session`". The case built declares `Planning` `framer`, with `plan.md` and the framer's mark, so the frame arm passes and the spec read is the one refusal | the case under `framer` | S1 already runs under `the session`, because the fixture declares it. A second case there covers nothing S1 does not, which `agents/smith.md` *A new test starts from its group* refuses. S7's title, "either planning answer", needs the other answer, which no case covered |
| What the exit-2 guard wraps | `spec.md` *Data & interfaces*: "Where the call raises, `main` prints `chain-check: the rule-changes reader would not load (<exception>)` to stderr and returns 2". The code wraps the whole `rule_changes_read` call, so a failure of `unverified_check.py#policy_root`, which loads `hooks/config.py` by path, prints the same line | the wider guard | `rule_changes_read(reader, root, item)` calls both the loader and `policy_root`, as *Data & interfaces* fixes its body. Both load a module by path, and the exception set is the one `main` already catches for `hooks/routing.py` |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck at this branch's HEAD | the orchestrator, through `broad-gate --base release/v0.22.3 --record seal/specs/1792619289-the-pull-request-check-parses-rule-changes` |
| S11: `hooks/commitgate.py`, `skills/verify/scripts/seal_stamp.py`, `skills/verify/scripts/broad_gate.py` and `.github/scripts/release_seal.py` load nothing new when they import `chain_check.py` | the warden, at review; the build adds no import-time load, and the reader is reached from `main` alone |

## Not done

Nothing.

## Fed back into the spec

None.
