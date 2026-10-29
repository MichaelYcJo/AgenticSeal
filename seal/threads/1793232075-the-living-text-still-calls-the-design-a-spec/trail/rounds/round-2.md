# Review round 2: 1793232075-the-living-text-still-calls-the-design-a-spec

target: e2b93c49, fixes 2d8d8301..e2b93c49

This round verifies round 1's fixes. It read the diff `2d8d8301..e2b93c49`
and the lines that diff stands on, and nothing wider. Five commits make up
the range. `227ea366` is the crafter's fix pass. `7d7288bf`, `036b87ab` and
`e2b93c49` are the orchestrator's folds of the frame. `07c6d057` commits
round 1's record with the fix pass's two lines per finding, and the diff of
that record changes only the `verdict:` and `answer:` lines of both
findings (read).

Some facts are carried from round 1 and not established again here: the C1
to C6 enumeration and its reading against *Occurrences kept, and why*, the
reading of the moved pins, the nine rule changes against the policy root at
`475653e7`, and the changelog fragment's printed strings. No commit in the
range touches those lines. Round 1's `evidence: executed` lines were run
again where this round weighs their findings.

## Findings

### 1. The closing memo still says the frame counts twelve citations, after the folds removed that count from the frame

severity: should
location: `seal/threads/1793232075-the-living-text-still-calls-the-design-a-spec/gaps.md:19`
evidence: executed `git grep -n -i -E '\btwelve\b' e2b93c49 -- seal/threads/1793232075-the-living-text-still-calls-the-design-a-spec/frame`, `git diff 2d8d8301..e2b93c49`
verdict: open

`gaps.md:19` is the divergence row *The count of the step-1 heading's
citations*. It reads: "`frame/design.md` *Scope* item 5 and `plan.md`'s
phase-3 row say "twelve"". That held when phase 3 closed. It no longer
holds at `e2b93c49`. `036b87ab` rewrote *Scope* item 5 to "with each of its
citations" (`frame/design.md:74`). `e2b93c49` rewrote the plan's three
phrases, and the phase-3 row now reads "with all its citations"
(`frame/plan.md:88`). A search for `twelve` over the frame prints nothing
(executed). So the closing memo describes a frame that no longer exists.

This matters because the closing memo is read and acted on. The sealer
reads every party's account against the tree. A reader who opens the frame
to check this row finds no "twelve" and cannot tell whether the row or the
frame is wrong. `CLAUDE.md` *The rule a mechanism is kept against* says a
change removes, in the same commit, what stood on the old fact. The folds
removed the count and left this row standing on it.

The divergence itself is real: the build moved ten citations while the
frame said twelve. So the fix keeps the row and puts its frame claim in the
past, naming the commits that dropped the count. `gaps.md` is the crafter's
to edit in the fix pass.

```markdown
| The count of the step-1 heading's citations | `frame/design.md` *Scope* item 5 and `plan.md`'s phase-3 row said "twelve" when phase 3 was built. The frame's own list and `git grep -n -i 'Read the spec'` give ten, plus the heading. The orchestrator dropped the count from the frame at `036b87ab` and `e2b93c49` | the tree | All ten moved with the heading, and the grep prints nothing after `3816dfca` (`trail/phases/phase-3.md`) |
```

answer:

## Confirmations

confirms: round-1#1
The close holds. `skills/code-review/SKILL.md:22-25` at `e2b93c49` reads
round 1's paste-ready stage-1 sentence word for word, and the short line
"Look" is reflowed (read). Stage 1 now names its own set, "the ratified
documents above it", which is the word `skills/implement/SKILL.md:147-149`
uses for the line the ticket ranks below (read). `git grep -n -i outrank`
at `e2b93c49` finds the borrowed phrase nowhere outside `implement`'s step-1
heading and its citations (executed). The remaining hits are of three kinds.
Some are a different sentence, such as `agents/framer.md:55`, "outranks the
ticket and the code alike", which this branch did not change. Some are
other meanings in tests and hooks. The rest are history in
`trail/phases/phase-3.md:57` and in round 1's record. The fold `036b87ab`
also removed the phrase from `frame/design.md` *Scope* item 6, which round
1's answer had left to the orchestrator: line 76 now reads the stage's own
set (read). `frame/plan.md:77`, row A6a, names the same set and says why it
differs from step 1's (read). `tests/behaviour/test_docs_line_wrap.py`
passes over the reflowed paragraph in the run below (executed).

confirms: round-1#2
The close holds. `gaps.md:34-41` is round 1's *Not done* paragraph as
written, with `<N>` read as #1150 (read). `gh issue view 1150` shows it
open, titled as round 1 proposed, in the milestone `release: 0.24.2`
(executed, a read with no write). Round 1's evidence was run again.
`python3 evals/scripts/replay_targets.py --list` prints nothing and exits 0.
`git ls-tree` gives 0 round records under `seal/specs/` and 7 under
`seal/threads/*/trail/rounds/` at both `v0.23.0` and `v0.23.1`, which are
still the two highest release tags (executed). `last_tags` at
`evals/scripts/replay_targets.py:107-117` takes two tags by default, and
`:132` still reads `seal/specs` (read). `trail/phases/phase-2.md:64-73`
now says the same as the closing memo and names #1150 (read). The fix pass
corrected that phase record in place, against round 1's line that it stay.
Its answer says so and names the orchestrator's instruction. Round 1's
finding named that file among its locations, so the fix touched a named
path.

confirms: none
The folds change no fact the build stands on. `036b87ab` changes only
*Scope* items 5 and 6 of `frame/design.md`. `e2b93c49` changes only three
"twelve citations" phrases of `frame/plan.md`, at `:31`, `:74` and `:88`.
`7d7288bf` changes only row A6a (read, `git diff 2d8d8301..e2b93c49`).
*Scope* item 6 now matches `skills/code-review/SKILL.md:22-24` (read). S6,
S7, `## Rule changes` and the *Living occurrences* rows did not change.
The phase-3 row's Status cell, `3816dfca`, did not change either. The
changelog fragment says the stage checks "the code against the policy and
the work item's SDD set", which agrees with the new sentence (read).
`bin/seal rules --check` and `bin/seal layout --check` exit 0 (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck. The crafter labels the suite `unverified`, and the label is honest: this round ran only the modules below | `seal/threads/1793232075-the-living-text-still-calls-the-design-a-spec/gaps.md` | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `git grep -n -i outrank e2b93c49` | the phrase stands in `implement`'s heading, its citations, `frame/design.md:74`, `frame/plan.md:77` and `:88`, `gaps.md:10`, the round-1 record and `trail/phases/phase-3.md:57`; every other hit is another sentence or meaning |
| `git grep -n -i -E '\btwelve\b\|\bten citations' e2b93c49` over the work item's `frame/`, `gaps.md` and `trail/phases/` | no line in `frame/`; the phase-3 record holds its moment's "ten citations, not twelve" |
| `python3 evals/scripts/replay_targets.py --list` | nothing printed, exit 0 |
| `git ls-tree -r --name-only <tag> seal/specs` and `seal/threads`, for `v0.23.0` and `v0.23.1` | round records under `seal/specs/`: 0 and 0; under `seal/threads/*/trail/rounds/`: 7 and 7 |
| `gh issue view 1150 --json number,title,state,milestone` | open, in `release: 0.24.2`, titled as round 1 proposed |
| `bin/test -q` over the 7 modules `git grep -l` finds under `tests/` naming `code-review/SKILL.md`, plus `tests/hooks/test_review_skill_gate.py`, `tests/behaviour/test_chain_hooks_hardening.py` and `tests/skills/test_unverified_check.py` | 1006 passed, exit 0 |
| `bin/seal layout --check` | exit 0 |
| `bin/seal rules --check` | exit 0, all 266 check lines in 55 rule files hold |
