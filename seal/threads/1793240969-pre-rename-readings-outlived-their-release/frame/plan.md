# Implementation Plan: 1793240969-pre-rename-readings-outlived-their-release

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 and 2.

## Summary

Two readings of names from before the rename to AgenticSeal go: the
`SpecSeal-Routing` trailer key that `chain-check` reads as `Seal-Routing`,
and the `smith` answer that `routing.parse` reads as `crafter`. Each goes with
its constant, its comment, its reader and the sentence that describes it. The
case that pinned each reading is rewritten in place into the case that pins
the opposite, seen red first. The policy sentence in
`docs/the-routing-check.md` goes through the design's `## Rule changes`, at
the settle. The other readings of the same promise stay out of this work on
`questions.md` Q1's default.

## Technical context

All coordinates are at 1e82fd0a (read).

- `skills/code-review/scripts/chain_check.py:2076-2082` holds `TRAILER` and
  `OLD_TRAILER` with the comment that promises the removal.
  `routing_trailers` (`:2101`) asks git for both keys at `:2121`
  (`key={TRAILER},key={OLD_TRAILER},valueonly,separator=%x1e`), and its
  docstring at `:2102-2103` and `:2107` says *or `SpecSeal-Routing`* and
  *under either key*. The module docstring's `trailer` arm at `:12-16` says
  *or `SpecSeal-Routing` on one made before the rename*. `trailer_findings`
  (`:2140`) reads values only, so it does not change.
- `hooks/lib/routing.py:72-78` holds `BY_CRAFTER`, the comment, the
  `# exempt from old_names:` line and `OLD_BY_CRAFTER`. `parse` (`:193`)
  turns the old answer into `BY_CRAFTER` at `:258-259`; the general path
  below it, `implementation if implementation in IMPLEMENTATION_ANSWERS else
  None`, is what reads `smith` once those two lines go.
- The one consumer of the parsed `implementation` is
  `hooks/implementer-notice.py#AXES`, which reminds only where it equals
  `crafter`.
- `tests/skills/test_chain_check.py:2965-2981` is the case that pins the old
  key; `tests/hooks/test_routing.py:128-136` is the case that pins the old
  answer. `tests/hooks/test_routing.py:265-277`
  (`test_refuses_an_unreadable_third_axis_as_an_answer_and_keeps_the_declaration`)
  and `tests/skills/test_chain_check.py:2994`
  (`test_a_teammates_commit_is_never_judged`) already pin the general paths
  the old inputs fall into.
- `tests/censuses.py:1006-1009` is the `KEPT_OLD_NAMES` item for the old key.
  `old_names` takes a kept spelling out of every line before it matches, so a
  line that spells the key needs no exemption while the item stands, and an
  exemption above such a line is refused as excusing nothing
  (`tests/censuses.py#_held`). `smith` is not kept: `OLD_NAME` matches it as
  a word (`:984`), so a test line that spells it needs
  `# exempt from old_names: <why>` on its own line above it.
- `tests/test_censuses.py:776` and `:848` use the kept key as their example
  of a kept spelling. They stand, because the item stands.
- `skills/implement/orchestration.md:398` is the `Implementation` row of
  *What the answer writes*. Sibling #1046 edits other sections of the same
  file in this milestone.

**Failure scenario of the chosen approach.** A repository that installed a
release before 0.23.0 and still has a work item in flight from then, moved
by `hooks/root-migrate.py` with its `routing.md` copied byte for byte,
reads `Implementation | smith` as unanswered: the crafter reminder of
`hooks/implementer-notice.py` stays silent for it. A branch from then whose
commits carry only `SpecSeal-Routing:` has those commits passed over by the
trailer arm instead of judged. Both outcomes are the looser verdict, so no
session is stopped; what is lost is one reminder and one check on work that
began two minor releases ago. In this repository the count of such branches
and work items is zero (`frame/design.md` *Scope*, executed).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Keep both readings and rewrite each comment to name a later release, or no release | The comment promise is the shape that already failed once: the issue exists because no issue scheduled the 0.24.0 removal. The premise that would keep the readers is that something still writes or holds the old inputs. Checked: no open branch or work item does (executed, `frame/design.md` *Scope*) | rejected |
| B. Remove both readers, delete the two pinning cases, and add no case | Nothing shows that the old inputs now reach the general path. The issue's second acceptance line asks for that case, and `routing.md` *Why this way* says this work changes what the two readers accept, which is new behaviour under the run's rule that red-first cases are for new behaviour | rejected |
| C. Remove both readers, and rewrite each pinning case in place into the case that pins the opposite, seen red at 1e82fd0a | The rewritten trailer case spells the old key, so the census item for it stays with a rewritten comment, and the rewritten answer case carries one `# exempt from old_names:` line. Both are the census's existing forms | chosen |
| D. As C, and also remove the census item for the old key, as the issue's first acceptance line asks | `docs/the-routing-check.md:101` spells the key until the settle after this release writes the `remove`, and a pull request does not edit the policy root. Without the item, `old_names` flags that line on this pull request's own run. S1's case spells the key as well | rejected |
| E. As C, and also remove the other readings of the same promise: the CLAUDE.md block markers of `install.sh`, `uninstall.sh` and `skills/update/SKILL.md`, and `seal.py#OLD_PLUGIN_CLONE` | These read files a person's own install holds until that person reruns the installer. A person going from a release before 0.23.0 straight to this one would get a second CLAUDE.md block appended, or a workflow that `seal pr-checks` leaves as somebody else's. It also widens the files this work shares with the milestone's siblings, `seal.py` among them | `questions.md` Q1; out on its default |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The old trailer key is no longer read. In `skills/code-review/scripts/chain_check.py`: `OLD_TRAILER` and its comment go; `routing_trailers` asks for `key={TRAILER}` alone; the module docstring's `trailer` arm and `routing_trailers`' docstring drop the old key and *under either key*. `tests/skills/test_chain_check.py#Test_routing_trailers.test_reads_the_trailer_a_commit_before_0_23_0_carries` is rewritten in place into S1's case, under a name that says the old key is not read. The comment on the `KEPT_OLD_NAMES` item in `tests/censuses.py` is rewritten to name its two remaining readers: S1's case, and `docs/the-routing-check.md` *At the pull request* until the settle removes that sentence. The item's string is unchanged | S1's case seen red against the tree at 1e82fd0a with only the case rewritten, then green with the reader changed; the hand-back says how it was seen red. Then `tests/skills/test_chain_check.py` and `tests/test_censuses.py`, each run whole | e1fc252d |
| 2 | The old Implementation answer is no longer read. In `hooks/lib/routing.py`: `OLD_BY_CRAFTER`, its comment and its `# exempt from old_names:` line go, and the two lines of `parse` that turn it into `BY_CRAFTER` go. `tests/hooks/test_routing.py#Test_parse.test_accepts_the_answer_written_before_the_rename_as_the_crafter` is rewritten in place into S2's case, under a name that says the old answer reads as unanswered; the line that spells `smith` carries `# exempt from old_names: <why>` on its own line above it. In `skills/implement/orchestration.md` *What the answer writes*, the `Implementation` row keeps `crafter` or `the session`, OPTIONAL; absent reads as unanswered, and loses the sentence on the old answer | S2's case seen red at 1e82fd0a with only the case rewritten, then green; the hand-back says how. Then `tests/hooks/test_routing.py` and `tests/hooks/test_implementer_notice.py`, each run whole, and S5's `git grep` printing nothing | f4d3d4a3 |

## Operational impact

No migration, environment variable, dependency or setting changes. Two
behaviours change for input written before 0.23.0, both toward the looser
verdict: a commit whose only routing trailer is `SpecSeal-Routing:` is not
judged at the pull request, and a `routing.md` answering `Implementation`
with `smith` reads as unanswered, so `hooks/implementer-notice.py` gives it
no crafter reminder. `docs/the-routing-check.md` *At the pull request* keeps
the sentence on the old key until the settle after this release removes it.
