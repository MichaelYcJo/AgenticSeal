# Review round 2: 1793226631-every-release-ends-with-a-preparation-pull-request

target: bb0d2489, fixes 34f0d679..bb0d2489

## Findings

### 1. The frame and the plan still say the merge is the owner's one act at a release, which the step-5 rule change now qualifies as his one required act

severity: should
location: `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/frame/design.md:14`, `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/frame/design.md:136-137`, `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/frame/plan.md:11-14`
evidence: executed `git grep -n -i -E "one (required )?act|only act|single act|owner's (one|only)|no act of"`, `git grep -n -i -E "owner('s)? (merge|act)|his (one|only)|what is left at the end" -- seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request`
verdict: open

Round 1's finding 2 named the rule change for checklist step 5. The fix,
`78512510`, rewrote that rule change to say "the owner's one required act at
a release is its merge", and added that the reads and the boxes of step 6 are
reports that fail nothing. It did not rewrite the three other sentences of
this work item that state the same fact without the qualifier. Contract rule
19 asks the commit that amends a fact to correct every other sentence
stating it, found by `git grep` on its words. The grep finds three:

- `frame/design.md:14`, *Grounding*: "The owner's one act at a release is the merge of the release pull request with *Create a merge commit*."
- `frame/design.md:136-137`, the steps that cut 0.24.0: "The owner merges the release pull request with *Create a merge commit*. That is his one act at the release."
- `frame/plan.md:11-14`, *Summary*: "What is left at the end of a release is the release pull request, which the orchestrator opens, and the owner's merge of it."

Under `frame/questions.md` Q2's default (a), which this work builds on
(`trail/phases/phase-3.md:37`), the owner still reads the release table,
sweeps the modules that grew with `bin/seal mutate`, reads the plugin
directory's page and ticks the boxes of step 6. So each of the three
sentences is false as written. `frame/design.md:136-137` is the procedure the
orchestrator follows to cut 0.24.0, and the sealer reads the frame against
the issue, whose body asks the owner for nothing per release. An agent that
reads "That is his one act at the release" has no reason to tell the owner
about the acts Q2 leaves him. The frame now gives the fact in two wordings,
and a reader has to choose between them.

`frame/design.md:14` hedges in its next sentence, "Where a step the issue
does not name still asks the owner for something, it is `frame/questions.md`
Q2". `frame/plan.md:100-104` also names Q2. Neither sentence corrects the
one before it; each leaves the reader two facts. The round-1 close holds at
the two places finding 2 named (`## Confirmations`). This finding is the
rest of that class, so it carries no `reopens:` line.

```markdown
<!-- frame/design.md:14, the second cell's second sentence -->
The owner's one required act at a release is the merge of the release pull
request with *Create a merge commit*.

<!-- frame/design.md:136-137 -->
4. The owner merges the release pull request with *Create a merge commit*.
   That is his one required act at the release; the reads and boxes the
   checklist still gives him are `frame/questions.md` Q2's, and fail nothing.

<!-- frame/plan.md:11-14 -->
run. What is left at the end of a release is the release pull request, which
the orchestrator opens, and the owner's merge of it, his one required act.
0.24.0 is the first release cut this way: this work item's pull request
moves its version.
```

answer:

### 2. The 0.24.0 changelog fragment still reports the skill's sentence with the aside "as this one does", which `13b9d759` removed from the skill

severity: should
location: `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/changelog.md:4`, `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/frame/design.md:35-40`
evidence: read `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/changelog.md:4`, `skills/implement/orchestration.md:526-540`, `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/frame/design.md:35-40`
verdict: open

The fix for round 1's finding 1 rewrote the skill to read "as a branch named
`release/vX.Y.Z` does" (`skills/implement/orchestration.md:530`). Two other
sentences on this branch report what that skill says, and both keep the
aside the fix removed:

- `changelog.md:4`: "`skills/implement/orchestration.md` says that where a repository names the version when it cuts the release branch, as this one does, the orchestrator moves the version in the first pull request into the branch". This fragment becomes the text of the 0.24.0 GitHub Release (`changelog.md:3` and *Scope* item 4).
- `frame/design.md:35-40`, *Scope* item 1: the paragraph "is rewritten to say that where the repository names the version at the release branch's cut, as this repository does, the first pull request into the branch moves it."

Each sentence has two readings. In one, the aside is the writer's own remark
about this repository, which is true. In the other, the aside is part of what
the skill says. That second reading is the one the crafter took from the
frame, which produced round 1's finding 1. It is now also false, because the
skill no longer says it. The release note is read by people who install the
plugin into their own repositories, and the sealer reads the fragment and the
frame against the tree. Both would read a sentence that misreports the
skill. Contract rule 19 asks for both sentences to be corrected in the commit
that changed the skill.

The fix pass swept the lines this branch added under `skills/`, `agents/`,
`templates/`, `hooks/` and `bin/`, and found no other instance. This round
repeated that sweep and agrees (`## Confirmations`). The fragment and the
frame lie outside those roots, which is why the sweep missed them.

```markdown
<!-- changelog.md:4, the first sentence after the bold lead -->
`skills/implement/orchestration.md` says that where a repository names the
version when it cuts the release branch, as a branch named `release/vX.Y.Z`
does, the orchestrator moves the version in the first pull request into the
branch, and every later pull request into it leaves the version alone.

<!-- frame/design.md:38-40 -->
into the release branch leaves the version alone; it is rewritten to say
that where the repository names the version at the release branch's cut, as
a branch named `release/vX.Y.Z` does, the first pull request into the branch
moves it.
```

answer:

## Confirmations

confirms: round-1#1
`skills/implement/orchestration.md:528-533` now reads "as a branch named
`release/vX.Y.Z` does" and "that work item's changelog entry" (read, in the
`34f0d679..bb0d2489` diff). No longer naming the reader's repository, the
sentence reads the same in every repository that installs the plugin. The
class grep, `git grep -n -E "as this (one|repository) does"` over `skills`,
`agents`, `templates`, `hooks` and `bin`, exits 1 with no line (executed).
The fix pass claimed it swept every line the branch added to a shipped file.
This round grepped every added line under those roots and `.claude-plugin`,
from merge base `4134055a`, for "this one", "this repository", "this
project", "this plugin", "this tree", "here", "our" and the product names, and
found none (executed). This round also read each added line in
`agents/framer.md`, `skills/settle/SKILL.md` and `templates/records/process.md`.
The template's "what this work item changed" means the host's own work item,
which is the right reading. The fix pass also claimed 35 modules and 1059
cases passed. This round did not re-run that set; it ran the 17 modules its
prompt names (`## Probes`). Two sentences outside the swept roots still
carry the old aside; they are finding 2.

confirms: round-1#2
At `frame/design.md:261-280` the step-5 `to:` reads "the owner's one
required act at a release is its merge", followed by "The reads below and the
boxes of step 6 are reports that fail nothing". A second `change` operation
re-points the check line to "the owner before the release pull request's
merge". This round re-ran the parse through
`skills/settle/scripts/rule_changes.py#parse` over `frame/design.md` with
policy root `docs`. It returned 30 operations, no error and no nothing-block
(executed), which matches the orchestrator's claim. For both section-5
operations, `rule_changes.pattern` of the `from:` text matches inside the
section's span of `docs/release-checklist.md` (lines 174 to 225), so the
settle will find both (executed). The close holds at the two places the
finding named. The same fact stated elsewhere without "required" is
finding 1.

confirms: round-1#3
The #913 row stands at `changelog.md:16`, and `git show --stat 78512510`
shows the fragment changed by one line (executed). This round re-ran the
finding's executed lines. The `7da1a77e` diff of
`skills/implement/orchestration.md` still shows the signer's citation
becoming a `| Pact | Clause | Hash |` table row. `git grep` finds that header
at `skills/implement/orchestration.md:606`, `skills/verify/scripts/pact_check.py:11`
and `:212`, `templates/setup/config.md:417` and `templates/setup/pact.md:23`.
`gh issue view 913` returns the issue open, under the title that names the
retired map grammar (executed). The row's second clause matches
`skills/verify/scripts/pact_check.py:44-60`: the map is a Remote and Path
table, and every line the walk does not read is refused at exit 2 (read).
The row was placed before the #1041 row, and the finding asked for after it.
`7da1a77e` is dated 2026-10-28 16:54 +0900 and `fdfb20d5` 2026-10-28 22:44
+0900 (executed, `git log -1 --format=%ad`), so the placement is
chronological. The finding's placement was wrong, and the fix's is right.

confirms: none
No commit has landed on the release branch since round 1, so *Scope* item 6
still names six way-of-working commits.
`git ls-remote origin refs/heads/release/v0.24.0` returns `4134055a`, which
is this branch's merge base (executed). The process table now carries rows
for #913, #1041, #1053 and #1117.

confirms: none
The 17 modules the prompt names pass. `bin/seal layout --check` and
`bin/seal rules --check` both exit 0, so S12 still holds at `bb0d2489`
(executed, `## Probes`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Facts carried from round 1 and not re-derived, because they lie outside the fix diff: its judgment that `822d75bb` (#1112), `5287dd42` (#1120) and `c825fd2c` (#1116) write no process row, its confirmations of `tag_release.py#decide` and the workflow's S8 behaviour, and its S11 grep. No commit in `34f0d679..bb0d2489` touches those paths | `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/trail/rounds/round-1.md` | the sealer, which reads the process table against `frame/design.md` *Scope* item 6 |
| Whether `gh api -X POST repos/<REPO>/git/refs` with the workflow's token creates `v0.24.0`, carried from round 1 unchanged | `frame/questions.md:31` (Q4), `.github/scripts/tag_release.py:153-179` | the orchestrator, reading `gh run list --workflow publish-release.yml --limit 1` and its log after 0.24.0's merge into `main` |
| Whether Q2's default (a) meets the owner's requirement that a release needs no act of his beyond the merge, carried from round 1 unchanged. Finding 1 asks only that the frame state the default consistently | `frame/questions.md:29` (Q2) | the owner, through Q2 |
| Whether the fix pass's hand-back labelled the full suite `unverified`. This round was not given that hand-back, and the round-1 record's `answer:` lines do not name the suite | `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/trail/rounds/round-1.md:55` | the orchestrator, who holds the hand-back and runs `seal gate` |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over the 17 `tests/` modules that `git grep -l -E "implement/orchestration\.md\|publish_release_note"` finds, plus `tests/behaviour/test_docs_line_wrap.py` | exit 0: 550 passed |
| `bin/seal layout --check` | exit 0: 161 files read, 0 refused |
| `bin/seal rules --check` | exit 0: all 266 check lines in 55 rule files hold |
| `python3 -I -c` importing `skills/settle/scripts/rule_changes.py`, running `parse` over `frame/design.md` with policy root `docs`, and searching each section-5 `from:` with `pattern` inside the span `section_lines` gives in `docs/release-checklist.md` | 30 operations, no error; both `from:` texts found in lines 174 to 225 |
| `git grep -n -E "as this (one\|repository) does"` over `skills`, `agents`, `templates`, `hooks` and `bin` | exit 1, no line |
| `git diff -U0 4134055a HEAD` over `skills`, `agents`, `templates`, `hooks`, `bin`, `commands` and `.claude-plugin`, its added lines grepped for self-referring phrases and product names | no line |
| `git grep` for the owner's one act, his only act and what is left at the end of a release, over the tree and over the work item | `frame/design.md:14`, `:137` and `frame/plan.md:12-13` unqualified (finding 1); the step-5 `to:` qualified |
| `git ls-remote origin refs/heads/release/v0.24.0` | `4134055a`, the merge base |
| `git show --format= 7da1a77e -- skills/implement/orchestration.md`, `git grep -n "Pact \| Clause \| Hash" -- skills templates`, `gh issue view 913 --repo MichaelYcJo/AgenticSeal --json title,state` | the table row form, five hits, the issue open |
