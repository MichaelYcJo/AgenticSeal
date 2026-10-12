## Fixes

| # | Verdict | Commit or grounds |
|---|---|---|
| 1 | answered | corrected on the pull request by the orchestrator: PR #901's title and body are the orchestrator's to edit, and nothing in the tree changes for them |
| 2 | fixed | `4d2c56c6` — `docs/the-reader-registry.md` §*The four classes and the line that declares one* now says the direction is where an input the unit does not understand ends, read through to the decision its value feeds, and that a helper's direction is read at its callers; read first against the inventory's key (part 6: a presence pin is `refused` because a rewording fails it) and #835's spec ("The direction is the inventory's"). The fold marker and the `Enforced by:` line are untouched. The edit drifted #835's live row D1, which was read and re-executed (`bin/fold-check --root .` exit 0, 19 documents, none over the ceiling) and re-stamped in place by `evidence-check --reverify --checked 2026-10-12 --ledger` that fragment. `overview.md` §*Fed back into the spec* and §*Not done* point at `docs/`, and `9ceba9a3` names the sentence in the changelog fragment, under `### Added`, which stays the fragment's one heading |
| 3 | answered | corrected at `4d2c56c6`: `plan.md`'s alternative row now rests on round 1's recall (it read all 189 bodies and caught about 37 of at least 65 distinct multi-unit false lines, about 57%), counts at most 65 distinct false lines among the 125, and states round 1's 83 / 97 / 9 matching beside the framer's 64 / 125; `spec.md` says round 1 read every line and 94 were opened by no later round; `overview.md` says 71 findings, at most 68 distinct lines |
| 4 | answered | corrected at `4d2c56c6`: `overview.md` and `spec.md` §*Removes* say the branch's code is the release branch's; the census acceptance row says it equals the release branch's, 1,583 at 34fc36e9 after #894 declared `hooks/worktree-guard.py#main`; the record-checks row runs `survivor-check` with no exemption file; the sealer's row reads "at the head"; `Not done` says every column of the inventory stays |
| 5 | answered | corrected at `4d2c56c6`: `handoff.md`'s state row for #834 names PR #901, the build, the reframe, phases 4–5 and the owner's choice of withdrawal, and decision 2 carries a dated line saying the reframe and the owner's answer superseded it for #834, its own text unchanged |
| 6 | answered | corrected at `4d2c56c6`: the changelog fragment names the inventory's full path and says it is read at the `v0.21.0` tag once `settle --retire` removes the directory |

The ❓ is answered by the owner in the session on 2026-10-12: withdraw
everything, and 0.21.0 ships the inventory and no backfill. `questions.md` Q1's
Status now carries that answer, asked by the orchestrating session, and
#835's `questions.md` Q7 the same: no bulk shrink, the census shrinks only as
units change and declare (`4d2c56c6`).
