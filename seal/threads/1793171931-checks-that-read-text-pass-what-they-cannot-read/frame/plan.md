# Implementation Plan: 1793171931-checks-that-read-text-pass-what-they-cannot-read

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 to 5.

## Summary

The crafter audits the 43 readers of `frame/design.md` *The readers to
audit*, one family per phase. For each reader it reads the code at
`c825fd2c`, feeds it a near miss through a probe it runs once and deletes,
and writes the reader's table row into that phase's record. Phase 5 joins
the four families into one table, files each fix the table names into
`release: 0.24.1` or marks it `#1038`, and posts the table as a comment on
#956. No file of the tree changes outside this work item's directory. The
owner pressed automation (`routing.md`), which authorizes the issues and the
comment this plan makes on GitHub, as it did for work item `1793163944`.

## Technical context

**Where the audit's judgments live.** A direction cell needs a probe that
was run (`frame/design.md` *Grounding*, the `CLAUDE.md` row), and a framer
runs no script. So the verdicts cannot sit in the frame the way work item
`1793163944`'s did: its verdicts were folds of issue text that reading
settles, and these are not. The frame holds the inventory and what the tree
already claims of each reader. Each phase record holds its family's rows,
each with its probe labelled executed, and the review reads them at their
commits. Phase 5's record holds the joined table and the closing paragraph,
and the comment on #956 is that text copied. While the work item lives, the
record is the reviewed text and the comment its copy (S7). After the settle
removes this directory, the comment is the one copy left standing.

**What the crafter reads.** The worktree at
`/Users/michael/Documents/GitHub/SpecSeal-worktrees/chore/956-checks-that-read-text-pass-what-they-cannot-read`
is `c825fd2c` plus this work item's records, so a file read there is the
base version. R16, R17 and R24 read files #913 changes on its own branch;
their rows say "base version; #913". No phase reads another branch's
worktree. Phase 4 alone may read `origin/release/v0.24.0` with `git fetch`
and `git show`, for R36 (`questions.md` Q2); neither moves HEAD.

**How a probe runs** (contract rule 7):

1. The probe is one file named `test_tmp_<phase>_<row>.py`, or one
   `test_tmp_<phase>.py` for the whole family, written through the `Write`
   tool into the crafter's scratch directory, outside the tree. It loads the
   reader by path with `importlib.util.spec_from_file_location`, as
   `chain_check.py#load` does, so nothing is installed and nothing in the tree
   is imported by a name a planted module could shadow.
2. It feeds the reader the near miss and prints the reader's answer: the
   value it returns, the refusal it names, or the exit code of the command.
   A hook is fed a payload on stdin; a CLI is run with `--root` pointed at a
   scratch copy holding the planted file where the reader needs a tree.
3. It runs once. Its exit code is read directly,
   `python3 <file> >/dev/null 2>&1; echo $?`, and its printed output is
   copied into the phase record with the command (contract rule 1).
4. It is deleted before the phase closes, with every scratch copy it used,
   by the paths the crafter recorded when it made them (contract rule 17).

Where a gate's own test file already holds a case that feeds the same near
miss (`SECURITY.md` *What is in scope* says each gate's test file holds its
fail-open cases), the crafter may run that one case by its node id instead,
which is a narrow run contract rule 2 allows, and record it the same way.
Reading such a case without running it makes the cell `read`, which S2
does not accept.

**How the GitHub acts are made** (phase 5). Each body goes to a file in the
scratch directory through the `Write` tool, then:

- an issue: `gh issue create --repo MichaelYcJo/AgenticSeal --milestone
  "release: 0.24.1" --title <title> --body-file <file>`;
- the comment: `gh issue comment 956 --repo MichaelYcJo/AgenticSeal
  --body-file <file>`, and its id from
  `gh api repos/MichaelYcJo/AgenticSeal/issues/956/comments --jq '.[-1].id'`;
- a later correction, by a fix pass: `gh api -X PATCH
  repos/MichaelYcJo/AgenticSeal/issues/comments/<id> -F body=@<file>`.

Each command's exit code is read directly, each result is read back with
`gh`, and each body file is removed when the phase closes.

**What the crafter does not run.** No test of the repository beyond the one
case a probe may run by node id, no lint, no suite: no tree file outside the
records changes, so nothing the suite reads moves. The broad gate is the
orchestrator's (contract rule 2).

**The failure scenario of this approach, six months out.** The table names
readers by `path#unit` at `c825fd2c`, and readers move: #913 already changes
three of them on its own branch. A framer of a filed fix who trusts the row's
direction without reprobing builds on a reader that is no longer there. What
keeps that from mattering is contract rule 5, that every framer opens the
coordinates it is handed, and the comment's opening sentence, which names
the commit the audit read. A second risk is the class line: a reader the
inventory missed reads as audited by its absence. The enumeration method
stands in `frame/design.md` *The readers to audit* so a reader of the table
can re-run it, and each phase record names any reader it added or moved out.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| The frame writes the verdicts and the crafter only posts them, as work item `1793163944` did | A direction written from reading is the reading `CLAUDE.md` calls guessed from words. The record shows such readings were wrong: #905 (closed, read) found four `Reads:` lines saying `refused` where the code let an off-shape line pass, and #923's four misses each fell to the passing side of a reader built to refuse. A framer runs no probe, so every verdict would be one of those | Rejected. The frame holds the inventory; the phase records hold the executed verdicts (*Technical context*) |
| Each phase posts its own rows to #956 as it closes | Four comments, the table split by when it was built rather than by what a reader needs; #1111 and #1038 would read four partial tables, and a later fix pass would edit four. #956 asks for one table | Rejected; phase 5 posts once |
| The table is committed as a tree document, such as a dated file under `docs/experiments/` | A second copy beside the issue, which #956 names as the table's home, and nothing reads the two against each other. `docs/README.md` calls `docs/experiments/` dated scratch and no policy (read), so it would hold a record nobody is sent to | Rejected |
| The table is folded into #956's body | `docs/issues-and-milestones.md` *An issue is its body and its comments together*: measurements land as comments, and the body answers what the ticket asks. #1111 and #1038 read #956's body for what the audit is; a body holding the result changes that ask | Rejected; a comment |
| Fix each reader that passes what it cannot read, in this work | #956 *The change*: "reported and not fixed here". A pull request that changes a dozen readers across hooks, CI scripts and tests is a dozen work items under one review, and a larger fix built before #1038 reads its record is a mechanism with no history | Rejected |
| Replace the structure: build one shared reader that refuses everything outside one spelling, used by every check, instead of auditing readers one by one | The readers read different grammars: a table row, a trailer, a Bash command, a citation. A shared reader either guesses each grammar or becomes a dispatcher over the existing ones. And the policy chooses different directions for different kinds of line on purpose: `docs/the-record-layout.md` *Whether a line is live is asked by what the line does* reads a line that holds a claim on doubt and refuses to take a declaring line on doubt, and says "No one rule serves all three kinds" (`:183`, read). One direction everywhere would contradict ratified policy | Kept the per-reader structure for this work. The premise that keeps it, that the policy wants different directions per kind of line, was checked at `:145-185`. Where several rows show one miss, the table sends a shared reader to #1038 as a candidate |
| Audit from docstrings and existing cases, with no probe | Same failure as the first row: the claim and the code disagreed in #905 and #923 | Rejected; S2 requires an executed probe for every direction cell |
| Judge each of the 305 negative asserts one by one | The figure includes asserts on a script's printed output, which read no written text (`questions.md` Q4), and a per-assert sweep is a sorting task, which is a fix, not an audit | Rejected. R37 is one class row with its count, probed on the three instances `seal/follow-up.md` names; the sorting is filed as a fix |
| One umbrella issue for every fix | #956 files each fix where one work item carries it. An umbrella is several work items under one number, and `.github/scripts/release_completeness_check.py` can then not tell which part of it a release carries | Rejected; one issue per module, and one for the `limit` sentences |
| Wait to audit R36 until #1043 lands | The audit idles on another branch's merge, which is the orchestrator's sequencing; the owner's milestone order puts #1043 first, and the orchestrator spawned both together | Rejected as the default; `questions.md` Q2 holds the choice |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Family A, R1 to R15, and any pair for R43 met there: one table row per reader in `trail/phases/phase-1.md`, each with its probe | Each row's probe command, exit code and output in the record, labelled executed (S2, S3, S4); `git status --porcelain` lists no probe (S9) | a41783fd |
| 2 | Family B, R16 to R24: rows in `trail/phases/phase-2.md`, with "base version; #913" on R16, R17 and R24 | As phase 1 | 393df2cd |
| 3 | Family C, R25 to R31: rows in `trail/phases/phase-3.md` | As phase 1 | 234962eb |
| 4 | Family D, R32 to R43: rows in `trail/phases/phase-4.md`, the citation count and classification at `c825fd2c` (R34), the precision of #956's reader shape (R35), R36 under `questions.md` Q2, and the R37 measurement of `questions.md` Q4 | As phase 1, and S5: the R34 probe reports `.github/scripts/gather_changelog.py:43-44` before any classification | 06bada02 |
| 5 | The joined table and its closing paragraph in `trail/phases/phase-5.md`; each fix filed into `release: 0.24.1` with its number written into the table, or `#1038`; the comment posted on #956 | S6, for each filed issue; S7, `diff` of the fetched comment against the record, exit 0; S8, read; S10, read; S9, `git diff --name-only c825fd2c..HEAD -- . ':!seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read'` printing nothing | 1891adff |

Phases 1 to 4 share no reader and may be built in any order; phase 5
follows all four. Each phase writes `trail/phases/phase-N.md` from
`templates/records/sdd-phase.md` and commits it. A row that leaves the class,
a reader added to it, and a direction that contradicts what *The readers to
audit* says the tree claims each go to `gaps.md` as a divergence, with the
probe as its grounds.

## Operational impact

None in the tree. On GitHub: one comment on #956, or two where the table
passes the comment length limit (`frame/design.md` *Data & interfaces*), and
one issue per module that needs a fix, plus one for the `limit` sentences,
each in `release: 0.24.1`. Because
`.github/scripts/release_completeness_check.py` fails a release while its
milestone holds an open issue the release does not carry, each filed issue
is work 0.24.1 owes; none enters `release: 0.24.0`.
