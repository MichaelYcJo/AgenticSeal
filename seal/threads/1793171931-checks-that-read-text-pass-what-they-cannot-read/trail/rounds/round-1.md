# Review round 1: 1793171931-checks-that-read-text-pass-what-they-cannot-read

target: 81a3dda6 against c825fd2c

This is the first round, so no earlier record named a coordinate and nothing
was carried; every fact below was opened or run in this round. The target is
the audit's records and its GitHub side: the 43 rows, issues #1121 to #1129
and comment 6464014816 on #956.

## Findings

### 1. R24 is left unfiled on the ground that its reader is gone, and at the release base the two near misses R24 measured still pass unread

severity: should
location: `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-5.md:52`, `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-5.md:93-95`, `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/gaps.md:15`
evidence: executed `PROBE_PART=2 python3 -I <scratch>/test_tmp_round1.py <clone> <scratch>/probe3 5287dd42`, `git show 5287dd42:skills/verify/scripts/pact_check.py`
verdict: open

R24 is one of the 16 `yes` rows. Its probe at `c825fd2c` found two
spellings of an anchor, `PACT:` and `pact: ` with a space, that `seal pact`
neither grades nor refuses (`trail/phases/phase-2.md:35`). Phase 5 claims
that #913, merged as `7da1a77e`, "refuses an inline `pact:` token at its
line", so "the reader R24 found passing near misses is gone at the base a
fix would build on" (`phase-5.md:95`). The row's `Fix` cell reads `none`,
and nothing is filed or sent to #1038.

The release base does not bear that out. At `5287dd42` the refusal is
`INLINE_TOKEN = re.compile(r"(?<![A-Za-z0-9_.@/-])pact:(?=\S)")`
(`skills/verify/scripts/pact_check.py:194` at that commit), which is
case-sensitive and needs a character that is not a space after the colon.
The probe fed it four lines. `pact:abc` was refused. `pact: abc`, `PACT:abc`
and `Pact:abc` were not read. So the two spellings R24 measured are still
neither graded nor refused at the base a fix would build on. A 0.23.x anchor
left in either spelling stays silent, and refusing such a leftover anchor is
the job `INLINE` (`:209-215` at that commit) gives the token. The comment at
`:190-193` there says the pattern "names no typo". That is a code comment,
which is no policy, and phase 5 does not cite it. The new anchor table's own
reader was not probed by phase 5 either, so R24's class at the release base
has no row and no home. A framer reading #956's comment takes R24 as closed
by #913.

This is the coordinate the crafter read (`gaps.md:15` cites `:194`). It is
not a reading of the new design as a whole: whether the table reader has
near misses of its own is a question this round leaves open.

The fix files R24 at the release base. One issue goes into
`release: 0.24.1` against `skills/verify/scripts/pact_check.py`, titled
like a commit. It names R24, the four token lines above, and a *Done when*
that has the inline token's near misses refused or stated as a limit, and
the table reader reprobed at its own base. Then the row's `Fix` cell, the
section *R24 was not filed* and `gaps.md:15` are corrected. The comment is
patched with the plan's command (`frame/plan.md`, *How the GitHub acts are
made*) so that S7 holds again. The cell, with the issue number
`gh issue create` prints in place of the placeholder:

```markdown
| R24 | `skills/verify/scripts/pact_check.py#check` with `coordinates.py#resolve_unit` (base versions; #913) | pact anchors in a signer's designs | `mixed`: an emphasised or code-span anchor is graded, a curly-quoted one refused; `PACT:` and `pact: ` with a space, neither | `yes`: a stale anchor written `PACT:` is never graded | eight anchors at one clause: the two near misses absent from the report | #<the number gh issue create prints>: at `5287dd42`, after #913, `INLINE_TOKEN` refuses `pact:` and reads neither `PACT:` nor `pact: ` |
```

answer:

### 2. R8's and R23's `limit` cells give a ground the design's definition of `limit` does not accept

severity: should
location: `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-1.md:34`, `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-2.md:34`, `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-5.md:36`, `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-5.md:51`, `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-5.md:73`
evidence: read `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/frame/design.md:272-274`, `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-1.md:34`, `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-2.md:34`, `docs/the-routing-check.md:113-117`, `skills/implement/orchestration.md:330`, `docs/worktree-guard-spec.md:589-603`
verdict: open

`frame/design.md` *The let-through words* (`:272-274`) defines `limit` as
"the shape cannot arise in the one-issue automation flow, and the cell says
why". Seven of the nine `limit` cells give that reason, for example R27's
"the release automation names both" and R41's "`compare` writes the cells".
Two give a different reason. R8's cell says that
`docs/the-routing-check.md:115-117` states the limit (`phase-1.md:34`).
R23's cell says that `docs/worktree-guard-spec.md` *Known limits* states it
(`phase-2.md:34`). A document stating a limit shows that the fix the
definition names already stands. It does not show that the shape cannot
arise, and the definition asks the cell to show that.

This matters because the closing paragraph's counts, 16 `yes` and 9
`limit` (`phase-5.md:73`), are what the owner reads for #923's Q9. For R8 a
reason exists that the cell does not give. A `Seal-Routing` trailer is
written only under `no work item` (`skills/implement/orchestration.md:330`),
and the one-issue automation flow never answers that. For R23 no such reason
is plain. The probe shows the guard silent on `G=git; $G switch feature` on
a dirty single-stream tree, which is what the guard exists to stop. The
commands come from the model in any session, the automation flow's
included, so by the design's words the row reads `yes` unless the crafter
can name why the flow cannot produce such a command.

For R8, the `Lets through` cell in `phase-1.md:34` and `phase-5.md:36`
becomes the block below. For R23, the crafter either names in
`phase-2.md:34` and `phase-5.md:51` why the one-issue flow cannot produce a
word the shell builds before git runs, or reads the row `yes`, keeps its
`Fix` cell as `none: the limit sentence stands`, and corrects the closing
paragraph (`phase-5.md:73`) to 17 `yes` and 8 `limit` with R23 in the list.
Either way the comment is patched with the plan's command so that S7 holds
again.

```markdown
`limit`: a `Seal-Routing` trailer is written only under `no work item` (`skills/implement/orchestration.md:330`), which the one-issue automation flow never answers, so a misspelt one cannot arise there; `docs/the-routing-check.md:115-117` states the cost
```

answer:

## Confirmations

confirms: none
S7 holds. Claimed: the comment equals `phase-5.md`'s comment section byte
for byte. Executed: `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6464014816`
returned the body, created and last updated at 2026-10-28T08:12:26Z. `cmp`
of that body against `phase-5.md:25-73` exited 0, at 14,910 bytes each.

confirms: none
S9 holds. Executed: `git diff --name-only c825fd2c..HEAD` with this work
item's directory excluded printed nothing, and `git status --porcelain` in
the worktree printed nothing before this record was written.

confirms: none
The counts hold. Claimed: 8 refuse, 3 pass, 7 skip and 24 mixed; 16 `yes`,
9 `limit` and 17 `no`. Executed: a count of the first word of each cell in
the 43 rows of `phase-5.md:29-71` gave those numbers, with R36 as "not
landed" in both columns. The same run compared each joined row's direction
and let-through with its family row in `phase-1.md` to `phase-4.md`, and no
row differed. The 16 `yes` rows it counted are the 16 the closing paragraph
lists.

confirms: none
The rows assigned to issues match the issues. Executed:
`gh issue view <N> --json title,milestone,state,body` for #1121 to #1129.
Each is open in `release: 0.24.1`, is titled with a commit prefix, names
its rows with their probes and the phase record holding them, and states
*Done when*. The rows each one names are the rows `phase-5.md:79-89` gives
it. Every row whose `Fix` cell names an issue number is named by that
issue. R10, R37 and R40 read `#1038`, with the reasons at `phase-5.md:91`.

confirms: none
R3, R11, R14 and R29 reproduce as recorded. Executed, by the probe in
`## Probes`, against the clone at `81a3dda6`, whose tree outside this
directory is `c825fd2c`. R3: an open finding inside a closed fence gave
`records()` no problem, and the same record unfenced gave one. R11:
`Round-2.md` and `round_2.md` holding an open finding gave no problem, and
`round-2.md` gave one. R14: a push-only `pytest` workflow keyed `on:` at two
spaces read `too late`, and keyed `"on":` or with `push:` at four spaces
read `answers (trigger unread)`. R29: `check: tests/exists.py` followed by
`  tests/missing_wrapped.py` gave no refusal.

confirms: none
R7's joined `Probe` cell says `by Framer` is "refused as not the framer".
Phase 1's probe ran `frame_foot` alone and printed "read as `Framer`"
(`phase-1.md:33`), so the refusal is no probe's output. It holds by
reading: `chain_check.py#frame` compares the mark's name with
`routing.BY_FRAMER` (`skills/code-review/scripts/chain_check.py:1569`),
which is `"framer"` (`hooks/lib/routing.py:85`). Read, not executed.

confirms: none
The R16 divergence holds, by reading. `hooks/lib/config.py#hidden_lines`
reads a row under a comment nobody closed, and
`tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:180-185`
pins that. But `config_table` reads through the walker, which refuses a
table GitHub does not render (`hooks/lib/config.py:316-350`). So the
sentence at `docs/the-record-layout.md:158-162` describes `hidden_lines`
and not what decides. #1128 carries the correction.

confirms: none
The `## Not verified` row of `gaps.md:26` names this round as the
answerer for R13's base-side relaxations. Answered by reading, without the
`--baseline` probe the row asks for.
`skills/verify/scripts/unverified_check.py:880-889` relaxes three shapes
at a base revision only. Each lets the base's rows be counted where they
would otherwise be "not compared" (`:1598-1622`). So each relaxation adds a
comparison that can refuse a deleted row and removes none, and R13's
`refuses` on the working tree's side is unaffected.

confirms: none
S10 and `questions.md` Q3 hold. No `yes` row reaches either situation
`SECURITY.md:33-39` names. The fork-run checks R3, R9, R11, R25 and R29
turn a pull request's check green and reach no token, environment or
filesystem of the run. R5, R10 and R31 act on an untrusted local
repository's own records: a drawn stamp, an allowed question, and its own
directory removed. None of them touches anything outside it. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The probes of the 38 rows this round did not re-run; their cells were read against their phase records, not re-probed | `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-1.md` to `phase-4.md` | the sealer, by its sample |
| Whether the anchor table reader `pact_check.py` uses at `5287dd42` has near misses of its own; finding 1 names only the inline token | `skills/verify/scripts/pact_check.py` at `5287dd42` | the fix pass, through the issue finding 1 files |
| Whether GitHub creates a closing reference from `Closes #18` inside an HTML comment (R28, `gaps.md:24`) | GitHub | the orchestrator |
| How `claude plugin eval` reads a `not_contains` grader whose file is absent (R40, `gaps.md:23`) | `evals/behaviour/crafter/rule-crafter-count-words/graders/shape-no-probe-left.md` | the framer of #1038's R40 item |
| The full suite, the repository-wide lint and the typecheck over this branch | the branch | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6464014816`, then `cmp` of its body against `phase-5.md` lines 25 to 73 | exit 0 for both; 14,910 bytes each; created and updated at 2026-10-28T08:12:26Z |
| `git diff --name-only c825fd2c..HEAD -- . ':!seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read'`; `git status --porcelain` | both printed nothing; exit 0 |
| `gh issue view <N> --json title,milestone,state,body` for 1121 to 1129 | all nine open in `release: 0.24.1`, rows as `phase-5.md:79-89` |
| `python3 -I -` over `phase-1.md` to `phase-5.md`, counting each joined row's direction and let-through and comparing it with its family row | 24 mixed, 8 refuses, 7 skips, 3 passes; 16 yes, 9 limit, 18 no including R36's "not landed"; no row differed |
| `python3 -I <scratch>/test_tmp_round1.py <clone> <scratch>/probe 5287dd42`, first run | exit 1. R3: fenced 0 problems, unfenced 1. R11 stopped at its third scratch repository, whose name collided with the second's on a case-insensitive file system |
| `python3 -I <scratch>/test_tmp_round1.py <clone> <scratch>/probe2 5287dd42`, scratch names corrected | exit 1. R3 as above. R11: `Round-2.md` 0, `round_2.md` 0, `round-2.md` 1. R14 stopped on the probe's own kind name, `suite` for `tests` |
| `PROBE_PART=2 python3 -I <scratch>/test_tmp_round1.py <clone> <scratch>/probe3 5287dd42`, kind corrected, R3 and R11 skipped | exit 0. R14: two spaces `too late`; `"on":` and four spaces `answers (trigger unread)`. R29: `([], 1, 1)`, no refusal. R24 at `5287dd42`: `pact:abc` refused; `pact: abc`, `PACT:abc`, `Pact:abc` not read |

The probe file, its three output files, its three scratch folders and the
clone were deleted by their recorded paths before this record was handed
back.
