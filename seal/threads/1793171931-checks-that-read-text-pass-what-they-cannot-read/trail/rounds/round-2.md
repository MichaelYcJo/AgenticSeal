# Review round 2: 1793171931-checks-that-read-text-pass-what-they-cannot-read

target: 6adbca75, fixes b630569d..6adbca75

This round verifies the fix pass over round 1, commits `dd787d28` and
`6adbca75`, and stays inside that diff and the GitHub acts it names. Round 1
gave this round three coordinates: `INLINE_TOKEN` at
`skills/verify/scripts/pact_check.py:194` at `5287dd42`, the design's
definition of `limit` at `frame/design.md:272-274`, and comment 6464014816.
Each was opened again here. Every verdict below was reached again in this
round, and none was taken from round 1. `git ls-remote origin
refs/heads/release/v0.24.0` printed `5287dd42`, so the release tip is still
the commit round 1 and the fix pass read.

## Findings

### 1. R8's fix is sent to #1038, though it changes one module and the design files such a fix into `release: 0.24.1`

severity: should
location: `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-1.md:34`, `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-5.md:36`, `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-5.md:93`
evidence: read `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/frame/design.md:276-282`, `skills/code-review/scripts/chain_check.py:2084-2140`, `docs/the-routing-check.md:112-117`, `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-5.md:93`
verdict: fixed bedaa645
regression: round-1#2

The unit is R8's `Fix` cell, which `dd787d28` changed from `none` to
`#1038` in `phase-1.md:34` and `phase-5.md:36`, with its reason at
`phase-5.md:93`. The frame says where a fix goes. `frame/design.md:276-282`
files a fix into `release: 0.24.1` when it "changes only the reader's own
module and that module's test files, or writes sentences into documents, and
adds no module, no gate and no reader shared across modules". It sends to
#1038 only "a reader shared by several modules, a new gate, or a rule over
the tree like Q9's". The fix pass did something else: it sent R8 to #1038
because "judging this one is a rule change". The defect came from treating
a rule change as a #1038 cell by itself. The design does not do that, and
the row it copied, R10, was sent there for a different reason.

R8's reader is one function in one module.
`skills/code-review/scripts/chain_check.py#routing_trailers` (`:2084-2121`)
asks git for the `Seal-Routing` and `SpecSeal-Routing` keys and nothing
else. `#trailer_findings` (`:2123-2140`) judges the values it returns. A
near-miss key such as `SealRouting:` is refused by changing those two
functions and the module's tests. Where the change also needs a sentence in
`docs/the-routing-check.md`, that sentence is the kind the design says one
work item writes, through its `## Rule changes`. None of #1038's three
kinds applies. No second module reads the trailer: phase 4's pair list
names none for it (`phase-4.md:47-56`). No gate is added: `chain-check` is
the gate that runs today. No rule over the tree is needed either.

The reason at `phase-5.md:93` does not fit the fix. "`docs/the-routing-check.md:115-117` chooses to judge no commit without the trailer"
is about a commit that carries no trailer, such as a teammate's. Refusing a
misspelt key at its line, as `skills/writing-style/SKILL.md` asks of a line
a check reads, judges no such commit. R10 differs: its #1038 reason is that
failing closed changes the rule for "every reader of `routing.md`", which
are three readers across three modules (`phase-5.md:93`). That is the
shared-reader case.

Why it matters: the comment on #956 now tells #1038's framer that R8 is a
larger fix, and #1038 decides each of its candidates by build or drop. A fix
that one work item carries in one module can be dropped there. The design
would have built it in 0.24.1 beside R3, R9 and R11, which are the same
module's fixes in #1121.

The fix routes R8 with the other `chain_check.py` rows. The row's cell
becomes the block below, in `phase-5.md:36` and, as `#1121`, in
`phase-1.md:34`. R8 leaves the `#1038` sentence at `phase-5.md:93` and joins
#1121's row in the issues table at `phase-5.md:81`. #1121 gains R8 in a
comment carrying the probe from `phase-1.md:34` and a *Done when* line: a
trailer key that git reads as another key and that is a near miss of
`Seal-Routing` is refused at the pull request, naming the commit. The
comment on #956 is patched with the plan's command so that S7 holds again.
If the fix pass holds that the change does need a reader shared across
modules or a new gate, its answer names that reader or gate, and the cell
keeps `#1038` with that reason in place of the rule-change one.

```markdown
| R8 | `chain_check.py#routing_trailers`, `#trailer_findings` | `Seal-Routing` trailers of the pull request's commits | `mixed`: a value in another case is refused; a key git does not read is no trailer, and the commit is not judged | `yes`: a session's commit at a shared root carries the trailer (`skills/commit-pr-convention/SKILL.md:142`), so a misspelt key arises in the flow, and its undeclared work item is not judged | `SealRouting:` naming an undeclared work item: not read, not reported; `No work item` and `no work item.` refused | #1121 |
```

answer: The finding holds. The cited line is about a commit with no trailer; refusing a near-miss key judges no such commit and changes `chain_check.py#routing_trailers` and `#trailer_findings` and their tests alone, so no shared reader or new gate is needed. R8's `Fix` reads `#1121` in `phase-5.md:36` (`0.24.1 chain_check.py` in `phase-1.md:34`), #1121's row in the issues table names R8, the `#1038` sentence names R10, R37 and R40 alone, and *R8 and R23 after review round 1* says why, in `bedaa645`. R8 was added to #1121 by `gh issue comment 1121 --body-file <file>` (exit 0, issuecomment-6464431981) with its probe and a *Done when* line refusing a near-miss key at the pull request. The comment on #956 was patched with `gh api -X PATCH repos/MichaelYcJo/AgenticSeal/issues/comments/6464014816 -F body=@<file>` (exit 0, updated 2026-10-28T08:36:37Z, 15,378 bytes), and `cmp` of the stored body against `phase-5.md`'s comment section exited 0.

## Confirmations

confirms: round-1#1
The close holds. Claimed by the fix pass: at `5287dd42`, `PACT:abc`,
`pact: abc` and `Pact:abc` are not read, and the anchor table passes over a
lower-case header, a `Hashes` header, a `**Pact**` header and a `pakt`
remote. Executed: this round's probe ran `pact_check.check` from a clone at
`5287dd42`, which is still the release tip, over one pact and a signer
holding nine designs. The second run (see `## Probes` for why there were
two) gave `seal pact` exit 2. The exact table was graded `UNMATCHED`, and
`pact:abc` was refused at its line with `INLINE`. `PACT:abc`, `pact: abc`,
`Pact:abc`, `| pact | clause | hash |`, `| Pact | Clause | Hashes |`,
`| **Pact** | Clause | Hash |` and a row naming
`git@example.com:o/pakt.git` were each absent from the report. #1132 is open
in `release: 0.24.1` (executed, `gh issue view 1132`). It names R24 and
those probes, and its *Done when* covers the inline near misses, the header
near misses and the remote near miss, each seen red against `5287dd42`.
R24's `Fix` cell at `phase-5.md:52`, the issues-table row at `:90`, the
section at `:95-108` and `gaps.md:15` all name #1132 and the probe at the
release base.

confirms: round-1#2
The close holds for both cells' `Lets through` column. R23 reads `yes` in
`phase-2.md:34` and `phase-5.md:51`, on the ground that the model types the
command in any session. #1133 is open in `release: 0.24.1` (executed,
`gh issue view 1133`), names R23 with its probe, and states *Done when*.
R8's departure from round 1's proposed text holds on its grounds. Round 1
proposed that a trailer is written only under `no work item`, and that
premise was wrong. `skills/commit-pr-convention/SKILL.md:141-145` and
`docs/the-routing-check.md:98-100` have every session's commit at a shared
root end with one `Seal-Routing:` trailer naming its work item. So the
one-issue flow writes trailers, and a misspelt key can arise there. The
R8 probe cell now says the `SealRouting:` commit named an undeclared work
item and was not reported. By reading, that follows from the code:
`routing_trailers` asks git for the two keys alone
(`skills/code-review/scripts/chain_check.py:2104`), so that commit yields no
value for `trailer_findings` to judge. R8's `Fix` cell is finding 1 of this
round.

confirms: none
The counts after the fix hold. Executed: a count over the 43 rows of
`phase-5.md:29-71` gave 8 refuse, 3 pass, 7 skip, 24 mixed and R36 not
landed; and 18 `yes`, 7 `limit`, 17 `no` and R36. The 18 `yes` rows are
R3, R5, R8, R9, R10, R11, R14, R23, R24, R25, R29, R31, R33, R34, R35, R37,
R40 and R43, the list the closing paragraph at `phase-5.md:73` gives.

confirms: none
S7 holds after the patch. Executed:
`gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6464014816`
returned a body updated at 2026-10-28T08:28:17Z. `cmp` of it against
`phase-5.md:25-73` exited 0, at 15,462 bytes each.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether this branch's commits owe the `Seal-Routing` trailer. `git log --format=%(trailers:key=Seal-Routing,valueonly)` over `c825fd2c..HEAD` printed no value for any of its 13 commits, `dd787d28` and `6adbca75` among them. The root is shared (`seal/config.md`, `Mode` `shared`), and `skills/commit-pr-convention/SKILL.md:141-145` has a session's commit there end with one. By R8's own row, `chain-check` judges none of them | the branch's commit messages | the orchestrator |
| Whether a near-miss key refusal for R8 needs a reader shared across modules, which would keep it at #1038 | `skills/code-review/scripts/chain_check.py:2084-2140` | the fix pass, in finding 1's answer |
| The full suite, the repository-wide lint and the typecheck over this branch | the branch | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `git ls-remote origin refs/heads/release/v0.24.0` | `5287dd42`, the release tip |
| `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6464014816`, then `cmp` of its body against `phase-5.md` lines 25 to 73 | exit 0 for both; 15,462 bytes each; updated at 2026-10-28T08:28:17Z |
| `gh issue view 1132` and `gh issue view 1133` with `--json title,milestone,state,body` | both open in `release: 0.24.1`; rows, probes and *Done when* as the confirmations say |
| `python3 -I -c` over `phase-5.md`, counting each row's direction and let-through | 24 mixed, 8 refuses, 7 skips, 3 passes; 18 yes, 7 limit, 17 no; R36 not landed in both |
| `python3 -I <scratch>/test_tmp_round2.py <clone at 5287dd42> <scratch>/probe`, first run | exit 1 from `seal pact`. The exact table was `UNMATCHED` and nothing else was reported. The run measured nothing about the inline token: the probe named three designs `inline-pact`, `inline-PACT` and `inline-Pact`, and on a case-insensitive file system those are one directory, which ended up holding `Pact:abc`. The header and remote rows read as in the second run |
| `python3 -I -c` loading `pact_check.py` from the clone and reading the designs of the first run | the three inline names were one directory holding `Pact:abc`, and `INLINE_TOKEN` found no match there |
| `python3 -I <scratch>/test_tmp_round2.py <clone at 5287dd42> <scratch>/probe2`, design names made distinct | exit 2 from `seal pact`. Exact table `UNMATCHED`. `pact:abc` `REFUSED` with `INLINE`. `PACT:abc`, `pact: abc`, `Pact:abc`, the lower-case, `Hashes` and `**Pact**` headers, and the `pakt` remote: not in the report |
| `git log --format=%(trailers:key=Seal-Routing,valueonly) c825fd2c..HEAD` | no value on any of the branch's 13 commits |

The probe file, its two output files, its two scratch folders and the clone
were deleted by their recorded paths before this record was handed back.
