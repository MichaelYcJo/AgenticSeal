# Phase 3: 1793226631-every-release-ends-with-a-preparation-pull-request

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 7e0a2b48 |

## What this phase was asked

Build phase 3 of `frame/plan.md` against the frame at `7bead7e7`. The
version moves at the start of a release, and the rest of the preparation's
readers go. `PREPARATION_RE` and its case are removed. The paragraph at
`skills/implement/orchestration.md:526-533` is rewritten, along with
`skills/settle/SKILL.md:176` and the roll's docstring. The release hygiene
docstrings are rewritten, and the refusal message changes with its pin in
the same commit. The refusal pin is seen red against the old message. S11's
grep runs at the phase's close, and `bin/seal rules --check`'s exit code is
read directly (S12). This phase also writes the work item's `changelog.md`
and leaves its `### Process changes` table for the orchestrator. It does
not move `.claude-plugin/plugin.json`'s `version`.

## What this phase found

**The frame holds against the tree, and `## Removes` is short (read, at
`7bead7e7`).** Every phase 3 coordinate resolves. S11's grep at
`7bead7e7` also found `tests/text/test_the_direct_answer_owes_the_sealers_record.py:102`,
which `## Removes` does not list. Removing the filter turned two cases of
`tests/github/test_release_seal.py` red, because its `PULLS` fixture planted
a preparation pull request `#9`. Reading the same class turned up
`tests/behaviour/test_release_hygiene.py:564` and the pin's own failure
message at `:482`. `hygiene.yml`'s version step also said, in a comment and
in its skip line, that the version moves when the release branch merges to
`main`. Each is rewritten here, and `gaps.md` records each as a divergence.

**The defaults this phase built on.** Q1 (a): the orchestrator opens the
release pull request with this work item's pull request. This phase writes
nothing for it. Q2 (a): the checklist's other owner acts are untouched.
Q3 (a): no hygiene step is added, so no file #1111 owns is edited.

**How each removal and rewrite was seen red (executed).**
- With `PREPARATION_RE` and its filter removed, `bin/test
  tests/github/test_publish_release_note.py -q -p no:xdist` exited 1. Four
  cases failed: the type partition, the glance count, the `only the
  preparation` parameter and the sealed glance. Each read the preparation
  pull request `#9` as dropped. With `#9` and the parameter removed, the
  module passed.
- `tests/github/test_release_seal.py` then failed two cases on `3 pull
  requests` where it expected 2. With its `#9` removed, both passed.
- The refusal's pin, rewritten to the new halves, failed against the old
  message: `bin/test tests/behaviour/test_release_hygiene.py -q -p no:xdist`
  exited 1 with `the reason went`. With `refusal` rewritten, 33 passed.
- The new skip-line case failed against the old echo, exit 1, 1 failed and
  35 passed. With the echo rewritten, the module passed.

**The refusal's new text.** The timer now fires in the commit that moves the
version, at the start of the release, and not hours into its end. The old
cost, "after the broad gate has already run", no longer holds: the version
moves in the commit that adds the release's first fragment, before that
work item's broad run. So the message names that commit and a different
cost. It fires in a pull request whose own change did not write the line.

**S11 and S12 (executed, at `7e0a2b48`).** `git grep -n -i -E
'seal/process|preparation (commit|branch|pull request)|release-prep|PREPARATION_RE'
-- . ':!docs' ':!seal/threads'` found no line and exited 1. The commit-pr
convention's "release preparation" does not match the pattern, so the one
allowed hit is not a hit. `bin/seal rules --check` exited 0, and
`bin/seal layout --check` exited 0.

**What stands on purpose.** `tests/text/test_the_release_tail_does_not_end_at_the_tag.py:77`
and `:336` read `docs/release-checklist.md` *6. After the merge*, which
names the tag push until the settle. `tests/github/test_release_completeness_check.py:196`
says "a release preparation round", meaning a release being prepared, not
the preparation pull request. `.test_durations` keeps a stale entry for the
removed `only the preparation` parameter. That file is the runner's cache,
and the runner rewrites it.

**The fragment's process table is a placeholder.** `changelog.md` ends with
`### Process changes`, its header and delimiter rows, and the template's
placeholder row. If the placeholder is left in, the note lifts it, which a
reader sees at once. An empty table would publish nothing and hide the
omission. The orchestrator replaces the placeholder with this release's rows.

**No unit was added in this phase that a mutant could break.** The phase
removes a filter and rewrites text. The two pinned texts, the refusal and
the skip line, were each seen red by their pins above.
