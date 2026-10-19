# 1792363231-a-local-mode-work-item-draws-no-stamp — review round 4

target: 40952942, fixes 3e28e664..40952942

## Findings

### 1. The changelog entry says none of its limits arises in this plugin's flow, then lists the foreign hooks slot among them

severity: should
location: `seal/specs/1792363231-a-local-mode-work-item-draws-no-stamp/changelog.md:44-50`
verdict: fixed f74b2f98

Why it matters. The fragment is what a user reads at the release. The
sentence "Three limits are stated, none of which arises in this plugin's
own flow" introduces round 3's three shapes. The next sentence opens with
the limit that stood before them: "A wrong row committed where the gate
does not run, under `--no-verify` or in a foreign hooks slot, or one an
amend folds into the commit it audited". So a reader takes the foreign
hooks slot as one of the limits that never arise. A foreign slot is a
user's own setup, such as `core.hooksPath` or a hook manager, and it does
arise: `docs/the-review-record.md` §*The stamp* and
`docs/the-commit-gate-inside-git.md` both state it as an ordinary place
where the stub does not run. The count also reads as three while the
listing holds four. The documents themselves state each shape truly
(confirmed below), so only the fragment misleads.

Read: `changelog.md:44-50` at 40952942, against
`docs/the-review-record.md:393-396` and
`docs/the-commit-gate-inside-git.md:127-131`.

```markdown
  A wrong row committed where the gate does not run, under `--no-verify` or
  in a foreign hooks slot, still leaves its work item with no stamp. Three
  more limits are stated, none of which arises in this plugin's own flow: a
  row an amend folds into the commit it audited leaves its work item with no
  stamp; a sealed item copied, in a second clone, onto a copy of its branch
  that lacks the audited commit draws a second stamp there; and a conflicted
  merge that brings in a side's `sealed` is refused, with `--no-verify` as
  its way on. `docs/the-review-record.md` §*The stamp* states each. On one
  machine,
```

answer: Fixed by the orchestrator after the last round, in the record it owns: the fragment now states the foreign-slot and `--no-verify` limit first, as one that does arise, then "Three more limits are stated, none of which arises in this plugin's own flow" over the amend, the second-clone copy and the conflicted merge, close to the round's rewrite.

## Confirmations

confirms: round-3#1
Each sentence states the copy shape truly. These are
`docs/the-review-record.md:302-306`, the unchecked paragraph's added
sentences at `:411-415`, and `seal_stamp.py`'s once comment at `:950-953`.
They name what happens: a `sealed` that drew in another clone is brought
onto a copy of its declared branch that does not hold its audited commit,
by hand, `checkout`, `cherry-pick -n` or `merge --squash`, and is refused
and recorded. They name the direction: doubled. They name the way on: the
new audit the refusal asks for is the step that draws again.

Executed in round 3's probe: the `checkout` and pruned `cherry-pick -n`
forms behaved exactly so. Read: `merge --squash` writes no `MERGE_HEAD` and
commits as a plain commit, so it meets the same refusal. The pin in
`test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does`
holds the sentence and asserts "copied here by hand" is gone. It passed in
the narrow run below (executed).

confirms: round-3#2
The merge shape is stated truly at
`docs/the-commit-gate-inside-git.md:110-115`, `docs/the-review-record.md`'s
"Likewise" sentence, and `seal_stamp.py`'s once comment. The concluding
commit is judged against `HEAD` alone, and a side's `sealed` over the side's
own commit is refused, as round 3's probe executed. Nothing is doubled or
missing beyond the refusal itself. The stated way on, `git commit
--no-verify`, holds (read): `reference-transaction` judges an unmarked
commit by the arms alone (`docs/the-commit-gate-inside-git.md:135-148`,
`hooks/commitgate.py:392-399`), and on the item's declared branch the arms
are quiet. The flow sentence is the owner's ruling and is not reopened. The
pin in `test_the_policy_states_the_guarantee_refusal_beside_the_arms` holds
both clauses, and it passed (executed).

confirms: round-3#3
The amend shape is stated truly at
`docs/the-commit-gate-inside-git.md:128-131` and
`docs/the-review-record.md:396-399`.

- **What happens:** the row lands through the stub, which runs with `HEAD`
  at the audited commit.
- **Direction:** missing. The work item draws no stamp, and its repair draws
  none, as round 3's probe executed.
- **Way on:** the pull request's check refuses the landed row as stale.

The pins in both policy tests hold the clause, and both passed (executed).

confirms: none
The fix pass changed no code. `git diff --stat 68a67d6b 40952942 -- hooks/`
printed nothing (executed). Its edits to `round-3.md` are each finding's
verdict and answer lines alone (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck. The suite stays `unverified` here | the branch at 40952942 | the orchestrator's `broad-gate --base <base> --record <item>`, after the rounds settle |
| `--no-verify` through the installed stubs, at a conflicted merge's concluding commit. Read here, not run | `docs/the-commit-gate-inside-git.md:110-115` | the orchestrator, if the shape is ever met |

## Probes

| Command | Result |
|---|---|
| `git diff --stat 68a67d6b 40952942 -- hooks/` | empty |
| `bin/test tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/test_the_commit_gate_decides_at_the_commit.py tests/test_docs_line_wrap.py -q -p no:xdist -k "policy or line_wrap or wrap or fits"` | exit 0, 46 passed, 280 deselected |
