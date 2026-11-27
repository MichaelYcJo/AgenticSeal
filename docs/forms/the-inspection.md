# The inspector's verdict

The inspector writes this verdict, and the orchestrator and the pull request
check read it.

## The inspection

**The inspector is the final, independent party to judge the work**, and what it verifies
against is `agents/inspector.md` *Job*'s. It runs after the changelog fragment is written, the
orchestrator's broad run has written `trail/gate.md`, and the pull request
body is written from the records, on both routing answers; it reads that
record and runs nothing broad, and its order of work is
`agents/inspector.md`'s.

**It checks a claim against the fact, and the parties against each other.**
The acts are `agents/inspector.md` step 3's and step 4's, and this section
names none of them, so the list has one home. Each act is one row of
`## Claims re-run` or `## The parties` in `inspection.md`. It does not
re-judge the design or the code's quality.
check: tests/behaviour/test_the_inspector_inspects.py

**The pull request body opens with the orchestrator's part, the work item's `pr.md`, and the records' copy follows it, the changelog fragment first and the rest in one fold; the inspector reads only the orchestrator's part.** `seal pr-body` writes above the line `skills/code-review/scripts/pr_body.py#HEADING` holds the work item's `pr.<lang>.md`, where `seal/config.json`'s `Commit and pull request language` and `Record language` keys name different languages, and then `pr.md`, each as its bytes stand; where the two keys name one language, `pr.md` comes first and any `pr.<lang>.md` follows it. Below that line it writes the copy of the work item's records: the changelog fragment first, whole and outside any fold, and then the rest inside one `<details>` block whose `<summary>` names the copy and is followed by a blank line, with nothing inside it folded again. What `pr.md` and `pr.<lang>.md` hold is stated in `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared*, and neither holds a sentence of the orchestrator's own account. The orchestrator commits them before the first round, so every round reads them. `seal pr-body` refuses where either language key is absent, so a body is composed only for a repository that declared its languages. A reader who stops after the first screen has the orchestrator's part, and the squash commit keeps the block's tags as text. The inspector runs `seal pr-body --check` on the body file before it compares the parties, and withholds where the part above the line is not what `pr.md` and, where the keys differ, `pr.<lang>.md` give, or the part below it is not what the records give. The copy then gives it nothing to compare: the records it copies are what the inspector audits.
check: tests/skills/test_pr_body.py tests/behaviour/test_the_inspector_inspects.py

**Its verdict is `inspection.md`, from `templates/records/sdd-inspection.md`**: the claims re-run and the parties compared, in tables for people, and one `seal` block per run of the inspector, appended below the blocks of earlier runs and never edited after its run. A verdict block holds `target: <sha> against <base>`, each one word, the `original:` line where `docs/checks/the-pull-request-check.md` *What the check reads at the pull request* owes one, and one `Verdict:` line, `cleared`, `withheld reason: <the claim, its party, its coordinate>` or `undecided question: <the question, for the owner>`, written exactly so. The last block is the newest run and the others are the earlier runs, which the stamp reads. An inspection with no verdict block, or with a line of a block that does not parse, is refused naming the file and the line. An undecided question is the owner's: the answer goes on a line below the newest block, and the inspector runs again at the new HEAD and appends its block.
check: tests/behaviour/test_the_inspector_inspects.py tests/skills/test_chain_check.py

**A ready pull request passes only where the newest verdict block of `inspection.md` names HEAD and reads `cleared`.** Only the closing records, `trail/gate.md` and `inspection.md`,
may follow the commit it names, since every other file on the branch is one
the inspector audited. A newest block reading `withheld` or `undecided`, an unfilled template, a block that does not parse or a lapsed inspection each fail naming the file; a draft prints them.
check: ready-needs-cleared

**How it errs.** It samples, so a false claim outside the sample passes, and
the sample is written in the file so the miss can be found afterwards.
Whether five stories agree is a judgment, so a disagreement it does not see
is missed.

**A pull request body carries the inspection mark only where the
repository turns it on and the work item is cleared at HEAD.**
`seal pr-body` writes the mark, the plugin's icon at the default
branch of the plugin's repository, as the first line under the line
`skills/code-review/scripts/pr_body.py#HEADING` holds. It writes it
where `seal/config.json`'s `Pull request inspection mark` key reads `yes` and
the newest verdict block of `inspection.md` reads `cleared` at a commit
that only the closing records follow, so the mark means what the stamp
means (`docs/checks/the-stamp.md` *The stamp*). It reads the row and HEAD in the work item's own
checkout, and, for a work item under the common git directory, in the
checkout the command runs in. A base the verdict block names that git
cannot resolve there, and a cleared commit that checkout's HEAD does not
hold, put no mark either, and are named, since whether the inspection has lapsed
cannot then be read. The key's other
values, and what the mark's address ties a body to, are
`templates/setup/config.md` *The inspection mark*'s. The inspector's
`seal pr-body --check` runs before its own verdict exists, so the copy
it checks carries no mark from that run. The orchestrator runs
`seal pr-body` once more after it commits a `cleared` inspection, and that
run changes no copied line, because the copy reads no `inspection.md`. The
pull request's check reads the body against what `seal pr-body` composes
at HEAD, so a body sent before that run fails a ready pull request on the
mark's line (`docs/checks/the-pull-request-check.md` *What the check reads
at the pull request*).
check: tests/skills/test_pr_body.py

**Where the body `seal pr-body` composes, counted in UTF-16 code units
with room for the inspection mark's line, would pass GitHub's limit of 65,536
characters, the sections of the records' copy after the
changelog's are folded, the longest first, until the body fits.** A folded
section keeps its heading, and a fixed line in place of its text names
the record that holds it, by its path in the work item. The changelog's
section is never folded, and a body that passes the limit with every
other section folded is refused, with nothing written, so `pr.md` or
`changelog.md` is shortened first. The fold leaves room for the inspection
mark's line whether or not the mark is written, so the run after a
`cleared` inspection folds what the inspector's check folded and changes no
copied line. GitHub refuses a longer body, and the pull request's check
reads the body as `seal pr-body` composes it, so without the fold a work
item whose records pass the limit has no body both accept (#1559).
check: tests/skills/test_pr_body.py

## The three states

**A work item's inspection is in one of three states, read from the
newest verdict block of `inspection.md`.** It is *cleared* where that
block reads `cleared` and names HEAD or a commit that only the closing
records follow. It has *lapsed* where that block reads `cleared` and a
commit that touches any other path follows the commit it names, and the
inspector runs again at HEAD. It is *not cleared* in every other case: no
`inspection.md`, a newest block reading `withheld` or `undecided`, a block
that does not parse, or a commit HEAD does not descend from. A ready pull
request passes, and a body carries the inspection mark, only where the
work item is cleared. A message of `chain_check.py`, `pr_body.py` or the
stamp that describes one of these states names it in these words.
check: tests/skills/test_chain_check.py tests/skills/test_pr_body.py tests/skills/test_stamp.py
