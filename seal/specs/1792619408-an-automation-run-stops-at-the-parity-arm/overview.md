# 1792619408-an-automation-run-stops-at-the-parity-arm — overview

## Why this work exists

In a repository that declares `seal/parity.md`, an `automation` run stopped at the smith's first code commit, because the parity arm's only satisfying event, the warden's comparison, comes after that commit; a branch declaring the review chain now meets the parity arm at the pull request, where every round record carries an `original:` line naming the baseline it compared against.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The loader paragraph under the grammar table | `spec.md` *Data & interfaces*: the `original:` row "is edited into `docs/the-review-record.md` in the build commit that adds its reader, not through `## Rule changes`". The build also added `original:` to `chain_check.py#READ_ROWS`, at `at most one` alone, and edited the paragraph under the table that names each row the loader reads a meaning from, adding "and `original:` stands there and is `at most one`" | the row in `READ_ROWS`, and the paragraph edited in the same commit | Without the entry, a table that moved the row into a finding or dropped its `(?P<commit>…)` part would end the check in a traceback where it owes exit 2. With the entry, the paragraph's sentence "Every other row may take any `Where` and `How many`" reads false for `original:` until a settle, and no `## Rule changes` operation of this spec touches that paragraph. Contract §19 asks for the text the change amends to be rewritten in the same commit |
| The template's `original:` line | `plan.md` *What the build touches*: "an `original:` placeholder line with one comment saying when it is owed". The build wrote the example line inside the comment, so a copied template carries no live `original:` line | the line inside the comment | Most repositories declare no `seal/parity.md`. A live placeholder that a warden forgets to delete there is a record naming a comparison nobody made, and no check sees it. A placeholder kept in the comment and forgotten in a migration repository is a missing line, which `chain_check.py#original_of` refuses at the pull request |
| S11 through `main` | `spec.md` S11: "when the diff against the base cannot be read, then the refusal stands". `chain_check.py#main` exits 2 at `chain-check: cannot diff against <base>` before any arm runs, so no run of the command reaches the parity arm with an unreadable diff | S11 pinned at `originals_of` with `paths` None | The refusal stands in both readings: exit 2 at the command, and an owed line at the function, which `hooks/gate.py#touches_code` decides for paths git could not list |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck at this branch's HEAD | the orchestrator's broad run, `broad-gate --base release/v0.22.3 --record seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm` |

## Not done

Nothing.

## Fed back into the spec

None.
