# Review round 2: 1793240969-pre-rename-readings-outlived-their-release

target: 539a2a5a, fixes e593a385..539a2a5a

This is a verifying round. The diff it reads is `e593a385..539a2a5a`: the
fix commit 645c9c80, which changes the comment on one `KEPT_OLD_NAMES` item
in `tests/censuses.py`, and the round-1 record with the fix pass's `verdict:`
and `answer:` lines. Every fact below was established this round in a clone
of the branch at 539a2a5a, except where a paragraph says it was carried.

Carried from round 1, as coordinates and not as verdicts: the census item's
place at `tests/censuses.py:1007-1012`, the search that finding 1 rests on,
and the two commits finding 2 names, 6306f1f1 and 5b8fcd02. Each was opened
again. The search was run again, as finding 1's `evidence:` line names it.
The fix pass's account (its `answer:` lines, the commit messages and the
spawn prompt's run of `tests/test_censuses.py`) was read as claims.

## Findings

None. The fix diff adds no code unit: 645c9c80 rewrites a comment, and the
record change is the fix pass's two lines per finding.

## Confirmations

confirms: round-1#1
The close holds. Claimed (the `answer:` line): 645c9c80 names the two places
that spell the old trailer key and states no count. Found: the comment at
`tests/censuses.py:1007-1011` names the case in
`tests/skills/test_chain_check.py#Test_routing_trailers` that pins the key
as unread, and the sentence in `docs/the-routing-check.md` *At the pull
request*. It states no count. The search finding 1 rests on, run again,
prints four lines: `docs/the-routing-check.md:101`, and
`tests/skills/test_chain_check.py:2969`, `:2974` and `:2976`. All three test
lines stand inside one case,
`test_does_not_read_the_trailer_key_a_commit_before_0_23_0_carries`, which
opens at `:2965` in the class that starts at `:2928`. So the comment names
every place that spells the key, and it stays true however many lines the
case uses. `tests/test_censuses.py:776` and `:848` build the key from a
variable and do not spell it, so the search does not find them. A search for
the old wording, *Two living lines* and *living lines still*, finds no other
living line (rule 12). 645c9c80 touches `tests/censuses.py` alone, the path
the finding's `location:` names. `tests/test_censuses.py` passes whole, and
`ruff check` and `ruff format --check` on `tests/censuses.py` exit 0
(executed, the probe rows below).

confirms: round-1#2
The rejection holds. The `answer:` line agrees with the observation.
`skills/implement/orchestration.md:531-534` asks for the version move "in
the commit that adds that work item's changelog entry". `git show --stat`
shows `changelog.md` added at 6306f1f1 and `.claude-plugin/plugin.json`
changed alone at 5b8fcd02 (executed). The rejection rests on the rule that
forbids rewriting a work item's branch. `docs/release-checklist.md`
*0. Before starting* says at `:20-22` "Never rebase a work item's branch,
for any reason", because every round record names its branch's commits on
its `target:` line. `skills/code-review/orchestration.md:187-188`, inside
the range the answer cites, says the same of a conflict with the base.
Round 1's proposed `reset --soft` and amend would replace 5b8fcd02, the
commit named on round 1's own `target:` line. That orphans it just as a
rebase would, so the rule's reason covers the proposal although the
proposal is no rebase. The pull
request into `release/v0.24.1` is squashed (`CLAUDE.md`, the merge-method
rule), so the release branch receives the same tree whichever commit carried
the move. A `should` finding is fixed or answered with why not. This answer
says why not, and its reason is a rule that outranks the ordering sentence.

confirms: none
The fix pass wrote two lines per finding and nothing else in the record, as
`docs/the-review-record.md` *The round record* asks. In `round-1.md`,
`git diff e593a385..539a2a5a` changes four lines, two in each finding: the
verdict line and the answer line (executed). Claimed (the spawn
prompt): the orchestrator committed the record at 539a2a5a without changing
a line.
Found: the diff holds no other change to the record.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch, which `gaps.md` *Not verified* labels `unverified` | the branch at 539a2a5a | the orchestrator, through `seal gate` |
| Whether the ordering sentence can be followed when the crafter commits `changelog.md` before the orchestrator moves the version. `agents/crafter.md:19-20` lets the crafter write the entry, and the sentence puts the move in that same commit. Opened while weighing finding 2, and outside the fix diff | `skills/implement/orchestration.md:531-534` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `git grep -n SpecSeal-Routing -- :!seal/threads`, at 539a2a5a | exit 0; four lines: `docs/the-routing-check.md:101`, `tests/skills/test_chain_check.py:2969`, `:2974`, `:2976` |
| `git grep -n -e "Two living lines" -e "living lines still" -- :!seal/threads`, at 539a2a5a | no line printed |
| `bin/test tests/test_censuses.py -q`, in the round's clone | exit 0, 175 passed |
| `uvx ruff check tests/censuses.py` and `uvx ruff format --check tests/censuses.py`, in the clone | exit 0 each |
| `git show --stat 645c9c80 6306f1f1 5b8fcd02` | 645c9c80 changes `tests/censuses.py` alone; 6306f1f1 adds `changelog.md`; 5b8fcd02 changes `.claude-plugin/plugin.json` alone |
| `git diff e593a385..539a2a5a` | two files: `tests/censuses.py`, and the `verdict:` and `answer:` lines of the two findings in `round-1.md` |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.24.1 --root <the branch worktree> --worktree`, the plugin's copy | exit 0; nothing refused in this record; it reports no `trail/gate.md` and no `guarantee.md`, which are the orchestrator's and the sealer's to write |
