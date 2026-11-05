# The sealer's verdict

The sealer writes this verdict, and the orchestrator and the pull request
check read it.

## The guarantee

**The sealer is the final, independent guarantor**, and what it verifies
against is `agents/sealer.md` *Job*'s. It runs after the changelog fragment is written, the
orchestrator's broad run has written `trail/gate.md`, and the pull request
body is written from the records, on both routing answers; it reads that
record and runs nothing broad, and its order of work is
`agents/sealer.md`'s.

**It checks a claim against the fact, and the parties against each other.**
The acts are `agents/sealer.md` step 3's and step 4's, and this section
names none of them, so the list has one home. Each act is one row of
`## Claims re-run` or `## The parties` in `guarantee.md`. It does not
re-judge the design or the code's quality.
check: tests/behaviour/test_the_sealer_guarantees.py

**The pull request body opens with the orchestrator's part, in the repository's language, and the records' copy follows it in one fold; the sealer reads only the orchestrator's part.** `seal pr-body` writes the part of the body below the line `skills/code-review/scripts/pr_body.py#HEADING` holds, copied from the work item's records inside one `<details>` block whose `<summary>` names the copy and is followed by a blank line, with nothing inside it folded again; the orchestrator writes above that line what no record holds, and states a record's fact only as that record's own sentence or with the coordinate of the row, heading, finding or line that holds it. A reader who stops after the first screen has the orchestrator's part, and the squash commit keeps the block's tags as text. The sealer runs `seal pr-body --check` on the body file before it compares the parties, and withholds where the part below the line is not what the records give. That part then gives it nothing to compare: the records it copies are what the sealer audits.
check: tests/skills/test_pr_body.py tests/behaviour/test_the_sealer_guarantees.py

**Its verdict is `guarantee.md`, from `templates/records/sdd-guarantee.md`**: the claims re-run and the parties compared, in tables for people, and one `seal` block per run of the sealer, appended below the blocks of earlier runs and never edited after its run. A verdict block holds `target: <sha> against <base>`, each one word, the `original:` line where `docs/checks/the-pull-request-check.md` *What the check reads at the pull request* owes one, and one `Verdict:` line, `sealed`, `withheld reason: <the claim, its party, its coordinate>` or `undecided question: <the question, for the owner>`, written exactly so. The last block is the newest run and the others are the earlier runs, which the stamp reads. A guarantee with no verdict block, or with a line of a block that does not parse, is refused naming the file and the line. An undecided question is the owner's: the answer goes on a line below the newest block, and the sealer runs again at the new HEAD and appends its block.
check: tests/behaviour/test_the_sealer_guarantees.py tests/skills/test_chain_check.py

**A ready pull request passes only where the newest verdict block of `guarantee.md` names HEAD and reads `sealed`.** Only the closing records, `trail/gate.md` and `guarantee.md`,
may follow the commit it names, since every other file on the branch is one
the sealer audited. A newest block reading `withheld` or `undecided`, an unfilled template, a block that does not parse or a stale commit each fail naming the file; a draft prints them.
check: ready-needs-sealed

**How it errs.** It samples, so a false claim outside the sample passes, and
the sample is written in the file so the miss can be found afterwards.
Whether five stories agree is a judgment, so a disagreement it does not see
is missed.

**A pull request body carries the seal mark only where the
repository turns it on and the work item is sealed at HEAD.**
`seal pr-body` writes the mark, the plugin's icon at the tag of the
plugin's version, as the first line under the line
`skills/code-review/scripts/pr_body.py#HEADING` holds. It writes it
where `seal/config.md`'s `Pull request seal mark` row reads `yes` and
the newest verdict block of `guarantee.md` reads `sealed` at a commit
that only the closing records follow, so the mark means what the stamp
means (`docs/checks/the-stamp.md` *The stamp*). It reads the row and HEAD in the work item's own
checkout, and, for a work item under the common git directory, in the
checkout the command runs in. A base the verdict block names that git
cannot resolve there, and a sealed commit that checkout's HEAD does not
hold, put no mark either, and are named, since whether the seal holds at
HEAD cannot then be read. The row's other
values, and what the mark's address ties a body to, are
`templates/setup/config.md` *The seal mark*'s. The sealer's
`seal pr-body --check` runs before its own verdict exists, so the copy
it checks carries no mark from that run. The orchestrator runs
`seal pr-body` once more after it commits a `sealed` guarantee, and that
run changes no copied line, because the copy reads no `guarantee.md`.
check: tests/skills/test_pr_body.py
