<!-- specseal:start -->
## Tooling
- Python: prefer uv · Node.js: prefer pnpm (always respect the project's existing manager).

## Safety
- **3+ Fix Rule** — same bug, 3 failed fix attempts → STOP. Re-examine the architecture, then ask.
- **Verification Gate** — no "done / fixed / passes" claim without running the check that proves it and reading its full output.
- **Verification Scope** — narrow and often, broad once. A slice runs what you just wrote; the handoff to review runs nothing broad; the full suite, lint, and typecheck run once, after the rounds settle. A broad run with an edit after it was spent, not banked.

## Session cost
- **Batch independent reads and runs** — every coordinate a task names in one call, every case from one file in one command. Round-trips are most of a round; cut the trips, never the investigation.

## Git
- Run lint/format/typecheck before committing.
- Worktrees only for concurrent sessions on the same tree — single-session work uses `git switch` (worktree-guard hook enforces this).
- **Routing, decided at the start** — **first, if this repository has `seal/` at neither `<repo>/seal/` nor `$(git rev-parse --git-common-dir)/seal/`: stop and follow the Bootstrap section of `skills/implement/orchestration.md`, the `implement` skill's orchestrator half.** Writing the file below is what CREATES that directory, creating it is what opts the repository in, and WHERE it lands — committed with the repository, or under the git directory and on this machine only — is the user's decision and not yours. Then, before the first edit, write `seal/specs/<work-item-id>/routing.md` from `templates/sdd-routing.md` and commit it — the write **in a command of its own**, never batched with the commit. The gate reads that file from the working tree, so a declaration on disk silences the very commit that adds it and no first-commit waiver is needed; but in a clone whose git hooks slot is somebody else's the gate is a `PreToolUse` hook that denies the WHOLE Bash call, so `write && git add && git commit` in one call writes nothing and the declaration the gate then reports missing is the file that was lost. Where this plugin's git hooks run, git judges the commit itself and the write goes through, so the separate command costs nothing there and is the one shape both readings accept. This is the one place the batching rule above misleads. **Ask question 1 alone; the boxes in a second call only under `per axis`.** Never one axis at a time: under `automation` or `no work item` the boxes mean nothing and are not shown, and under `per axis` the second call follows at once, before the first edit. Question 1, single-select: `automation` — every party runs and nothing stops to ask again · `per axis` — the boxes below are the answer · `no work item` — no frame, no review, no seal, no `routing.md`, this session writes the change, and every commit needs `[no-review]` in front of it. Question 2, a `multiSelect` of exactly four boxes, asked only under `per axis`, in this order: run end to end without stopping to ask (`Automation` = `yes`; unchecked is `no`, meaning this run may stop to ask, NOT that a person did it by hand) · implement with `smith` (unchecked, `the session` writes the code) · review with `warden` (`through the review chain`; unchecked, `straight to the PR`, and nothing reviews this code before the pull request) · open the pull request (unchecked, `stop before the pull request`, and the branch is handed back committed and unpushed). Four options is the cap and it is fully spent — a fifth box breaks the shape. What is checked is the answer, and each box is a row of that file; the file also records WHICH answer was pressed, because a pressed preset and four ticks by hand are otherwise the same bytes. You ask it whether or not a `framer` runs: a subagent in this harness has no `AskUserQuestion`, so a framer cannot ask and is told to report a missing declaration rather than write one. Asking the reviewer in the middle and the pull request at the end is three waits for one decision. The commit gate reads that file, so a declared work item commits silently for either review answer, and CI reads the same file at the pull request. For a change belonging to no work item, `[no-review]` still waives one command (`[no-parity]` too where a migration config is declared) — in front of the command, quotes included, `: '[no-review]'; git commit …`, because after `git commit` a bare word is a pathspec and git rejects it; `git -c specseal.waive=review commit …` is the same waiver in git's own spelling. Deciding at the commit is what stops a release mid-run.
<!-- specseal:end -->

<!-- Above: a generated copy of templates/claude-md-block.md, the block
     install.sh distributes. Edit the template, then
     `python3 .github/scripts/claude_block.py --write` regenerates this copy.
     Below: repo-local development rules for SpecSeal itself. -->

## The goal a design is chosen against — verification that runs unattended

**Verification through an automated workflow is this project's first goal.**
Between two designs that catch the same defect, the one that stops to ask a
person is the more expensive, and the difference has to be argued rather than
assumed. Time and stability are what the argument is being made for.

This is a goal, not a rule, which is why it sits above them: it decides
between options where no rule is broken either way.
`skills/implement/SKILL.md` §*1. Read the spec before the code* holds the rule
this goal produces for a session, with its reasoning: whatever needs a person
is asked once, together, before the first edit, and nothing comes back mid-run.

## The rule a mechanism is kept against — subtract before you add

**A mechanism stays only while its history shows what it caught against what
it costs**; existing is no reason to keep it. A rule's proof is the test or
behaviour eval its `check:` line names. A fact has one source, and every
other place links to it. A check gates only a fact it reads; a noisy reading,
or one guessed from words, is a report. Nothing is kept beside the tree to
stay in step with it, such as a stored count or coordinate. Do not avoid the
change a problem calls for: before a fix adapts to an existing structure, ask
whether the structure should change, and when fixes chase one mechanism's
edge cases, ask what it decides; what exists is a reference, not a
constraint. A thing is re-checked only when the diff or CI shows it
changed. A change rewrites the text it amends in place, and in the same
commit removes what stood on the old fact: a check, an exception, a comment,
a copy. History goes to git, the changelog and the work record.
`CONTRIBUTING.md` §*What a change to a gate must carry* is where a pull
request answers this rule and the goal above.

## Repo rule — the merge method is fixed per direction, and it is not a preference

A pull request into `release/vX.Y.Z` is squashed and one into `main` takes a
merge commit, whichever button a page offers first. The rule and its reasons
are `docs/branch-and-release.md` §*Work accumulates on a release branch*.

## Repo rule — no real identifiers in examples or fixtures

A domain in an example or fixture is `example.com` and a user path is
`/Users/x/`, never a real domain, path or organisation name
(`CONTRIBUTING.md` §*House rules*).

## Repo rule — a thing more than one party can have is named with whose

The concept and its format names stay bare — the Seal Test, a seal block —
and a reference to one instance says whose (`skills/writing-style/SKILL.md`
§*여럿이 가질 수 있는 것은 누구 것인지 밝힌다*).

`tests/test_one_word_one_meaning.py` is the check, one word per conversation
somebody had: writing the rule down is not the repair, the check is.

## Repo rule — commit early; on a declared branch it costs nothing

Both conditions `skills/implement/SKILL.md` §*2. Implement test-first, and
let each rule name its test* asks of a repository hold here: a feature branch
squashes into its release branch, and every work item commits its
`routing.md` before the first edit. So commit as soon as a step stands on its
own.

## Repo rule — a change writes fragments, never the shared file

Which file a change writes its changelog entry into is
`docs/the-record-layout.md` §*A change writes fragments, never a shared
file*. The release gathers the fragments with the command in
`docs/release-checklist.md` §*2. Gather, bump*.
