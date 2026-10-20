# 1791852617-a-docstring-left-short-is-reflowed — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. Facts that must outlive this work item go to the
evidence ledger, not here. -->

📋 implement applied
· spec:     issue #844; `routing.md`; round 3's report of work item 1791270163 at `25a05c68` (§*Paste-ready fixes*, ⬜ 1); `docs/the-record-layout.md` §*A change writes fragments, never a shared file* and §*A commit after the build brings its changelog fragment along*; `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*; `seal/config.md`
· evidence: `seal/ledger/1791852617-a-docstring-left-short-is-reflowed.md` — one `Re-read ·` row citing `seal/releases/0.19.0.md` R6, written by `evidence-check --reverify --into`
· verified: executed — the word-sequence comparison of the docstring, `bin/test tests/test_one_word_one_meaning.py`, ruff on that file, `bin/evidence-check --strict`; the broad gate is unverified, the sealer's

## Scope confirmation

Rewrap the last six lines of `tests/test_one_word_one_meaning.py#without_the_policy_span`'s docstring into five, to round 3's fence, change no word and no code, and re-read the one ledger family the rewrap drifts.

## Why this work exists

Round 2 of #831 inserted three sentences into the docstring and left `continuation line stays inside,` as a short line of its own; the paragraph now runs to one width, so it no longer reads as a break that is not there.

## Where spec and implementation diverged

Nothing. The issue's coordinate (line 741 at `eea27ad0`) still named the short line at this branch's base, and round 3's fence matches the rewrapped text byte for byte.

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, lint and typecheck over the merged tree | #912, merged with lint and the suite green on the ubuntu, macOS and Windows legs; the repository configures no typecheck |

## Not done

No changelog fragment. The rewrap changes nothing a release note states — no
verdict, no output, no instruction — and `docs/the-record-layout.md` says a
commit that changes nothing a release note states owes the fragment nothing.
Work items with no fragment already stand in the tree, such as
`1791090072-the-three-wave-one-items-read-each-other-after-the-squash`.

No phase record. Below the rung that draws a `plan.md` there are no numbered
phases to record; the scope confirmation above stands in for the plan.

## Fed back into the spec

none
