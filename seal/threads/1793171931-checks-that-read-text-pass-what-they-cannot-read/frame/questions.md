# Questions for the planner: 1793171931-checks-that-read-text-pass-what-they-cannot-read

## Answered by the tree, not to be reopened

- **#956 edits no file of the tree.** Its body says the audit is "reported
  and not fixed here" and "the result is one table in this issue" (read).
  `frame/design.md` `## Rule changes` and `## Removes` both hold the no-change
  block.
- **The table is a comment on #956, not a fold of its body.**
  `docs/issues-and-milestones.md` *An issue is its body and its comments
  together*: measurements land as comments, and the body answers what the
  ticket asks.
- **A fix one work item carries goes into `release: 0.24.1`; a larger one is
  marked `#1038`.** #956 *The change* decides both, and #1038's body already
  reads #956's larger fixes, so #1038 is not edited. `frame/design.md` *Data &
  interfaces* defines which fixes one work item carries.
- **The verdicts live in the phase records, executed, and not in the frame.**
  A direction needs a probe that was run, and a framer runs none
  (`frame/plan.md` *Alternatives considered*, first row).
- **"33 of 311" is not re-read; R34 counts at `c825fd2c`.** #1005's records
  hold the two counts in one sentence and neither the resolver's command nor
  the 33 (`frame/design.md` *The citation reader, re-based*).
- **A reader whose direction the policy states is judged against that
  statement.** `docs/the-record-layout.md` *Whether a line is live is asked
  by what the line does* chooses a direction per kind of line, so a probe
  that contradicts it is a defect of the reader, not a new direction.
- **A file #913 changes is read at `c825fd2c`.** R16, R17 and R24 say "base
  version; #913"; the spawn prompt asks for the base version, and a branch
  not merged is no reader of record.

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does the sentence "a gate fails closed: input it cannot read is refused, never passed" go into `CLAUDE.md` *The rule a mechanism is kept against*? This is #923's Q9 (`8350c578:seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/questions.md:184`, read), and #956 *The change* says it "is decided with this table in hand". The tree cannot answer it: whether a repository-wide rule binds every check is the owner's choice. The tree does show the rule half-standing already, in `SECURITY.md` *What is in scope* ("a check that fails open is a security defect here") and in `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* (a line a check reads is read in one spelling and a near miss is refused at its line), and `docs/the-record-layout.md` *Whether a line is live is asked by what the line does* chooses not to refuse every kind of line ("No one rule serves all three kinds") | a person | (a) not in `CLAUDE.md` in this work: the comment's closing paragraph gives the counts per direction, every `yes` row, and the three places above, and the owner decides afterwards. (b) into `CLAUDE.md` in a commit of its own after this work merges, with the readers that fall short of it named in the issues the table files. Neither option changes what this work builds, since #956 edits no file | (a) | open |
| Q2 | Does #956's audit wait until #1043's tree-wide citation case lands, so that R36 audits a case that exists? #956 says the audit records how that case fails "once it lands". The milestone description of `release: 0.24.0` puts #1043 in the group before #956 (read, `gh api repos/MichaelYcJo/AgenticSeal/milestones/65`), and the orchestrator spawned both together. At this frame #1043's branch holds only its `routing.md` (executed, `git ls-tree` of `docs/1043-no-check-reads-a-citation-of-most-files`). The order of merges is the orchestrator's under the owner's milestone, not the tree's | a person | (a) no wait: phase 4 runs `git fetch` and reads `origin/release/v0.24.0`; where #1043's case is there, R36 is audited at that commit with `git show` and probed on a scratch copy outside the tree; where it is not, R36 reads "not landed at <sha>", and phase 5 files one issue into `release: 0.24.1` to add R36's row to the table once #1043 lands. (b) wait: the orchestrator holds phase 4 until #1043 merges into `release/v0.24.0`, and R36 is audited in this work | (a) | open |
| Q3 | Where does a row go whose let-through reaches one of `SECURITY.md`'s two situations, a fork's pull request in CI or an untrusted repository checked out locally? `SECURITY.md` *Reporting* asks that a suspected vulnerability not go into a public issue, and *What is in scope* counts a check that fails open as a security defect. #956 itself is public and names a reader that passes through emphasis. Most rows guard a work item's process against a model's misspelling, which crosses no privilege boundary (`SECURITY.md` *What this project is, and where its risk actually sits*, read), but the tree cannot say in advance whether a probe will find one that does. Whether to disclose is the owner's | a person | (a) a row that reaches either situation is written in the table as its row number, its reader and the words "held for a private report"; its input, its probe and its let-through go only into the crafter's hand-back to the orchestrator, which carries them to the owner for a private advisory; no committed record, comment or issue carries them. Every other row is public, as #956 is. (b) every row public. (c) the whole table private, and #956 closed with a pointer to the advisory | (a) | open |
| Q4 | How many of the 305 negative asserts read a tracked file's text, rather than a script's printed output? `for d in tests/text tests/behaviour tests/skills tests/github tests/hooks tests/evals; do grep -h -E 'assert \(?\s*"[^"]{12,}"\s*\)?\s+not in\b' -r $d \| wc -l; done` at `c825fd2c` printed 48, 120, 106, 13, 18 and 0 (executed). The pattern cannot tell what the asserted-against variable holds | a measurement | Phase 4 reads, for each match, whether the variable it tests was read from a tracked file or from a run's output, and records both counts with the command it ran. R37's row carries the first count; the sorting of each instance into the spelling of a repaired defect or a shape the check exists to stop is the fix R37 files | R37 carries 305 as an upper bound until phase 4 measures | open |
