# Phase 5: 1793171931-checks-that-read-text-pass-what-they-cannot-read

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | the commit that adds this file; `frame/plan.md`'s Status cell for phase 5 names it |

## What this phase was asked

Merge the four families' rows into one table here, file the fix issues into
`release: 0.24.1` as the plan says (one per module, and the `limit` sentences
as one), and post the table on #956 as a comment. The owner pressed
automation, which authorizes these GitHub acts. Under `questions.md` Q1's
default the comment's last paragraph carries the counts by direction, every
`yes` row and the three places the frame names, and no sentence enters
`CLAUDE.md`. Under Q3's default a row whose let-through reaches one of
`SECURITY.md`'s two situations is held for a private report.

## What this phase found

### The comment on #956

The text between this heading and the next is the comment, byte for byte.

This is the audit #956 asks for, read at `c825fd2c` by work item `1793171931-checks-that-read-text-pass-what-they-cannot-read`, whose `trail/phases/phase-1.md` to `phase-4.md` hold each probe's input, command and output.

| Row | Reader | Reads and decides | On input it cannot read | Lets through | Probe | Fix |
|---|---|---|---|---|---|---|
| R1 | `hooks/lib/blocks.py#walk_text` | which markdown lines a renderer hides, for R10 and R16; no verdict of its own | `mixed`: a closed fence or comment block hides its lines; one nobody closed, or one inside a list item, leaves the lines uncertain for the caller | `no`: it decides nothing | a row under an unclosed fence: live and uncertain; under a closed fence: hidden | none |
| R2 | `skills/code-review/scripts/chain_check.py#grammar` | the two tables of `docs/the-review-record.md` *The round record*; exit 2 where unreadable | `mixed`: an unreadable cell is refused; a blank line ends a table, and the rows after it are dropped unless one is a row the check reads | `limit`: a dropped old-spelling row lets that spelling through as prose; the settle writes the tables | a blank line before `fix of a fix:`: the grammar loads, and a finding line in that spelling reads as prose | #1128 |
| R3 | `chain_check.py#findings`, `#record_lines`, `#confirmations`, `#round_of` | `trail/rounds/round-N.md`; a ready pull request fails on a line it cannot read or an open finding | `mixed`: a label in another case, under emphasis or with a homoglyph is refused; a finding inside a closed fence is skipped | `yes`: an open finding inside a closed fence | finding 2 at `verdict: open` in a closed fence, finding 1 deferred: `records()` named no problem | #1121 |
| R4 | `chain_check.py#verdicts_of`, `#verdict_word` | the `Verdict:` line of `guarantee.md`; a ready pull request needs `Verdict: sealed` | `refuses` | `no` | emphasis, another case, a trailing mark, a blockquote, an indent, a homoglyph: no word or no line, refused | none |
| R5 | `skills/verify/scripts/seal_stamp.py#queue_for_written_guarantee`, `#sealed_before` | the same line at the guarantee's write; queues the stamp | `mixed`: an unreadable verdict queues nothing; a fence nobody closed is not looked for | `yes`: the stamp is queued for a guarantee the pull request refuses (R43) | `Verdict: sealed`, an unclosed fence, `Verdict: withheld ...`: queued, and `guarantee` refused the file | #1122 |
| R6 | `chain_check.py#target_row`, `#target_of`, `#earlier_verdicts` | the `Target SHA` row of `guarantee.md` | `refuses` | `no` | a backticked or emphasised SHA, no `against`, `Earlier run`: each refused at the row | none |
| R7 | `chain_check.py#frame_foot` | the framer's mark at the foot of `frame/design.md` | `refuses` | `no` | emphasis, no period, a comment line after it: no mark, refused; `by Framer`: refused as not the framer | none |
| R8 | `chain_check.py#routing_trailers`, `#trailer_findings` | `Seal-Routing` trailers of the pull request's commits | `mixed`: a value in another case is refused; a key git does not read is no trailer, and the commit is not judged | `limit`: `docs/the-routing-check.md:115-117` states it | `SealRouting:` not read; `No work item` and `no work item.` refused | none |
| R9 | `chain_check.py#original_of`, `#originals_of` | `original:` lines, in a migration repository | `mixed`: misspelt in a round record, refused; misspelt in a guarantee, counted as present and not read | `yes`: a guarantee naming another baseline as `Original: 0000000` | `Original:`, `**original:**`, `original:0000000`: both arms passed; `original: 0000000`: refused | #1121 |
| R10 | `hooks/lib/routing.py#parse`, `#shown`, `#table_rows`, with the edit gate, the question gate and `chain_check.py` | `routing.md` | `mixed`: an unreadable `Review`, `Destination` or `Branch` is no declaration, and the edit gate denies; an unreadable `Automation` is unanswered | `yes`: with `Automation` reading `Yes` the question gate allows a question | `yes`: deny; `Yes` and `**yes**`: no output | #1038 |
| R11 | `routing.py#rounds`, `#rounds_unreadable`, `#stray_rounds`, `chain_check.py#round_records` | the file names under `trail/rounds/` | `skips`: a name other than `round-<N>.md` is no record | `yes`: `Round-2.md` holding an open finding | `Round-2.md`, `round_2.md`, `round-2.MD`: `records()` named no problem | #1121 |
| R12 | `skills/settle/scripts/rule_changes.py#parse` | `## Rule changes` of `frame/design.md` | `mixed`: a heading with the same letters and every off-shape item line are refused; a heading with other letters is no section | `no`: `seal settle` lists such a design to be read whole | `## Rule Changes`, `- Change`, a backticked file: refused; `## Rule change`: no section | none |
| R13 | `skills/verify/scripts/unverified_check.py#check_text` and its helpers | `## Not verified` of `gaps.md` | `refuses`; a row opening `**closed**` reads as open | `no`: an unread closing word errs toward open | heading near misses, `Closed`, `closed:`, three cells, prose after the table: refused | none |
| R14 | `skills/verify/scripts/deferral_check.py#inspect`, `#read_events` | CI workflows, for whether a deferral has an answerer | `passes`: an unreadable `on:` block counts as answering | `yes`: a push-only test run answers the deferral | `"on":` and a `push:` at four spaces: `answers (trigger unread)`, exit 0; `on:`: `too late` | #1123 |
| R15 | `skills/code-review/scripts/pr_body.py#_check`, `#split` | a pull request body against the records | `refuses` | `no` | a trailing space, added emphasis, the heading with a trailing space: refused | none |
| R16 | `hooks/lib/config.py`, its table and row readers (base version; #913) | `seal/config.md`; a value or a refusal per item | `mixed`: an unknown `Mode` value; a refusal for a doubled row or a refused table; the default for a misspelt optional item | `no`: R18 and R30 carry what callers do | `**Mode**`: no row; a table under an unclosed `<!--`: refused, where `docs/the-record-layout.md:158-162` says it still declares | none; the sentence is #1128's |
| R17 | `config.py#gfm_table`, `#read_table`, `#pact_declaration`, `#pact_signers`, `#baseline_commit` (base version; #913) | the pact's tables and the `Baseline commit` row | `mixed`: a baseline or signer near miss is refused; a misspelt `Pact` item is no pact | `no`: `seal pact` refuses a signer whose config names no pact | `abcdef1` with no backticks, capitals: refused; `pact` in lower case: no pact | none |
| R18 | `hooks/mode-gate.py#undeclared`, `#decide` | the `Mode` row | `mixed`: an unreadable value or item denies; a doubled row or a refused table is silent | `limit`: a root with no `Mode` row and a refused table is silent; the bootstrap writes the row | no `Mode` and a readable table: deny; a refused table: silent | #1128 |
| R19 | `hooks/lib/optin.py` `MARKER` | the first line of `seal/README.md` | `skips`: no root, and every gate is silent | `limit`: setup writes the README | a trailing space, a byte order mark, a blank first line: not marked | #1128 |
| R20 | `hooks/stub-remove.py#is_stub` | the second line of each git hook file | `mixed`: a stub with an indented or later marker stays; a file whose second line only begins with the marker is removed | `limit`: no hook manager writes that line | a person's hook with `# specseal-git-hook-like` on line 2: removed | #1128 |
| R21 | `hooks/lib/tokens.py#given` | consent tokens in a Bash command | `mixed`: a misspelt token is not read; a whole quoted token is read | `no`: a token is an audit trail, not an authorization | `[Worktree-ok]`, `[worktree_ok]`: not read; `-m "[worktree-ok]"`: read | none |
| R22 | `hooks/lib/one_heredoc.py#reduce` | one heredoc shape | `skips`: the caller reads the command as written | `no`: the wider reader takes the body out too | four near misses: None, and no token read from the body | none |
| R23 | `hooks/lib/cmdline.py`, `hooks/lib/cmdline_base.py`, through `hooks/worktree-guard.py` | Bash commands, for a switch or a creation | `mixed`: a git in a string, in `eval` or with a backslash is judged; one spelled by a substitution, a parameter or a brace is not | `limit`: `docs/worktree-guard-spec.md` *Known limits* states it | a dirty single-stream tree: `git switch`: ask; `$G switch`, `$(echo git) switch`, `git rebase {main,feature}`: silent | none |
| R24 | `skills/verify/scripts/pact_check.py#check` with `coordinates.py#resolve_unit` (base versions; #913) | pact anchors in a signer's designs | `mixed`: an emphasised or code-span anchor is graded, a curly-quoted one refused; `PACT:` and `pact: ` with a space, neither | `yes`: a stale anchor written `PACT:` is never graded | eight anchors at one clause: the two near misses absent from the report | none: #913 replaced the inline anchor with a table row at `7da1a77e` |
| R25 | `.github/scripts/gather_changelog.py`, `--check` | fragments and the release files' markers | `mixed`: an unread marker leaves its fragment ungathered, and the check fails; a fragment at another path is none | `yes`: `frame/changelog.md` passes as gathered | marker near misses: exit 1; `frame/changelog.md`, `changelog.markdown`: exit 0 | #1124 |
| R26 | `.github/scripts/issue_claims_check.py#read` | the pull request body; reports what it claims | `passes`: every body exits 0 | `no`: a report, so it leaves the class | `Closes: #14 and #15`: exit 0, "claimed: none" | none |
| R27 | `.github/scripts/release_completeness_check.py#judge` | the range's closing keywords against `release: X.Y.Z` | `mixed`: an unread keyword fails the release; another milestone title or branch name is judged as nothing, at exit 0 | `limit`: the release automation names both | `**Closes** #15`: M \ D fails; `release/v9.9.9`: no milestone, exit 0 | #1128 |
| R28 | the closing keyword as R26, R27, `close_issues_on_release.py#keywords_in` and `pr_body.py#_claims` read it | pull request bodies | `refuses`: the four agree, and an unread keyword fails R27 | `no` | twelve bodies, each read alike by all four | none |
| R29 | `.github/scripts/rules.py#check_lines`, `#parse` | `check:` lines | `mixed`: near misses of the label are refused; a target wrapped onto the next line is not read | `yes`: a missing target on a wrapped line | `Check:`, `check:x`, `**check:**`: refused; the wrapped target: unread | #1125 |
| R30 | `skills/settle/scripts/fold_check.py#index_problems`, `#config_rows` | the policy root's index | `mixed`: index near misses are refused; a misspelt `Policy root` reads `docs` | `limit`: setup writes the row | `Policy root`: exit 1; `Policy Root`: exit 0 over `docs/` | #1128 |
| R31 | `skills/settle/scripts/settle.py#open_rows`, with `--apply` | released work items' open rows | `mixed`: an unreadable section keeps the directory; a `gaps.md` elsewhere is no record | `yes`: an open row in `trail/gaps.md` is removed with its directory | six work items: `trail/gaps.md` removed, the unreadable ones kept | #1126 |
| R32 | the `Reads:` lines #905 names | none stand | `skips`: gone at `af9c924b` | `no` | `git grep` at `c825fd2c`: exit 1, nothing | none |
| R33 | the `implement` citation case, the contract-rule resolver, the broad gate pin | citations in the tree | `skips`: a wrap across `#`, a string split or bold is not read; the contract case reads six trees | `yes`: a dangling citation wrapped across `#` | `*9. No such step*` wrapped across `#`: not found | #1127, and #1043 for the `implement` case |
| R34 | each `` `<path>.md` *<section>* `` citation at `c825fd2c` | the tree's text files | `skips`: no case reads them | `yes`: the miss at `gather_changelog.py:43` stands | 411 recognised, 55 unresolved, 1 real miss | none: #1043 |
| R35 | #956's reader shape | the same | `mixed`: it refuses at least 13 correct wrapped citations, and misses the possessive and 3 of the `implement` case's 24 | `yes`: it is blind to the one real miss | 388 recognised, 59 unresolved | none: #1129 carries it to #1043's row |
| R36 | #1043's tree-wide case | the same | not landed at `5287dd42` | not landed | `git log c825fd2c..origin/release/v0.24.0`: #1118, #1119, #1120 | #1129 |
| R37 | negative pins, as a class | documents and source read as text | `passes`: every spelling but the literal | `yes`: `gh issue close` planted across a comment leaves `test_the_gate_writes_nothing` green | 305 asserts: 123 read a file, 41 an output, 10 both, 131 neither word list | #1038 |
| R38 | positive phrase pins, as a class | documents | `refuses`: a rewording turns the case red | `no` | a sentence reworded to the same meaning: red | none: #1111 |
| R39 | `tests/censuses.py#_exempted`, `#_held`, `#_trailing` | exemption comments | `refuses` | `no` | no reason, capitals, another name, two names: the flagged line stays flagged | none |
| R40 | the eval graders, through `claude plugin eval` and `noninferiority.py#grade` | what the agent under test wrote | `mixed`: a `contains` grader fails a near miss; a `not_contains` grader passes every other spelling | `yes`: a leftover `tmp_test_x.py` passes "No probe file is left behind" | `test_tmp_` over four leftovers: one matched | #1038 |
| R41 | `evals/scripts/noninferiority.py#check` | a comparison record | `mixed`: an unread `cut short` cell is no result; an unread number cell is 0 | `limit`: `compare` writes the cells | a failing record edited to `pass`, with a number cell spaced off: exit 0 | #1128 |
| R42 | `evals/scripts/replay_targets.py#labelled_round`, `#confirmed` | round records, for the replay cases' truths | `skips`: a refused record or an unread `confirms:` adds no truth | `no`: fewer truths measure less | `Confirms: round-1#1`: nothing confirmed | none |
| R43 | the readers that read one line twice | the line both read | `mixed`: R4 and R5 disagree on an unclosed fence; every other pair reads through one function | `yes`: R5 | R5's and R28's probes | #1122 |

For #923's Q9, the counts and where the rule already stands. By what a reader does with input it cannot read: 8 refuse, 3 pass, 7 skip, 24 are mixed, and R36 has not landed. By whether that lets through what the check exists to stop: 16 yes, 9 limit and 17 no. The yes rows are R3, R5, R9, R10, R11, R14, R24, R25, R29, R31, R33, R34, R35, R37, R40 and R43. The rule Q9 would write stands in part in three places already: `SECURITY.md` *What is in scope* counts a check that fails open as a security defect; `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* has a line a check reads read in one spelling and a near miss refused at its line; and `docs/the-record-layout.md` *Whether a line is live is asked by what the line does* chooses one direction per kind of line, which R10's and R18's let-throughs follow for a declaring line. No row was held for a private report: no let-through reaches either situation `SECURITY.md` *What this project is, and where its risk actually sits* names.

### The issues filed

Each was created with `gh issue create --repo MichaelYcJo/AgenticSeal --milestone "release: 0.24.1"`, its exit read directly as 0, and read back with `gh issue view`, which named `release: 0.24.1` for every one.

| Issue | Module | Rows |
|---|---|---|
| #1121 | `skills/code-review/scripts/chain_check.py` | R3, R9, R11 |
| #1122 | `skills/verify/scripts/seal_stamp.py` | R5, R43 |
| #1123 | `skills/verify/scripts/deferral_check.py` | R14 |
| #1124 | `.github/scripts/gather_changelog.py` | R25 |
| #1125 | `.github/scripts/rules.py` | R29 |
| #1126 | `skills/settle/scripts/settle.py` | R31 |
| #1127 | `tests/text/test_the_agent_contract_holds_the_universal_rules.py` | R33 |
| #1128 | the limit sentences, and the one policy sentence R16 contradicts | R2, R16, R18, R19, R20, R27, R30, R41 |
| #1129 | the row R36 owes once #1043 lands (`questions.md` Q2's default) | R34, R35, R36 |

R10, R37 and R40 read `#1038`: R10's fix would take a declaring line on doubt, which `docs/the-record-layout.md:153-172` decides against for every reader of `routing.md`, and R37 and R40 are one class across a dozen modules and every eval case.

### R24 was not filed

#913 merged into `release/v0.24.0` as `7da1a77e` (#1119) while this audit ran. It replaced the inline `pact:` anchor R24 probed with a table row the one walker reads, and refuses an inline `pact:` token at its line (read, `git show origin/release/v0.24.0:skills/verify/scripts/pact_check.py`, `INLINE_TOKEN` at `:194`). So the reader R24 found passing near misses is gone at the base a fix would build on, and filing it would send a framer to a unit that no longer stands. The plan let phase 4 alone read `origin/release/v0.24.0`, for R36; this read was made to decide the filing, and `gaps.md` records it.

### The comment, and the checks the plan names

- The comment is https://github.com/MichaelYcJo/AgenticSeal/issues/956#issuecomment-6464014816,
  id `6464014816`, posted with `gh issue comment 956 --repo MichaelYcJo/AgenticSeal --body-file <scratch>/c956/comment.md`
  at exit 0. At 14,910 bytes it is one comment.
- S7: the body file was first compared with this record's section above,
  `diff` exit 0. The posted body, read from
  `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6464014816` as JSON,
  equals both byte for byte (executed, exit 0). The plan's
  `--jq .body` form prints one newline more than the body holds, so a
  `diff` of its output against the file differs by that newline alone.
- S9: `git diff --name-only c825fd2c..HEAD -- . ':!seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read'`
  printed nothing, and `git status --porcelain` listed this work item's
  records alone.
- S8 and S10: read against the closing paragraph above, which counts the
  rows by both columns, names every `yes` row and the three places, and
  says no row was held.

### Where the frame does not hold

The phase 1 to phase 4 records each name what they found; `gaps.md` holds the divergences. This phase adds R24's above.
