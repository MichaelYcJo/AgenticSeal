# Design: a sha:path citation opens after the squash (#1270)

The issue's *Done when* asks for a weighing: build a check that each
`<commit>:<path>` citation resolves, with a case, or decide against it with
the grounds written where the decision lives. This frame builds it for every
tracked file outside a work item's `trail/` and `guarantee.md`, and decides
against reading bare SHAs. The weighing is in *Grounding* rows G1 to G4, and
the alternatives it was weighed against are in `plan.md` *Alternatives
considered*.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A mechanism stays only while its record of what it caught outweighs what it costs" | The record, executed by a read-only probe of the scoped check (*Probes* P2) at each release tag from `v0.24.0` to `v0.27.3`: three work items reached a release with a refused citation in their frame, each through a sealed chain. They are #1193 (`1793401152-the-seal-draws-a-round-headed-little-owl`, `frame/design.md:50`, its own branch's commit `efb91989`, at `v0.26.0` and `v0.27.0`), #1257 (`1793521558-the-record-decides-each-proposed-verifier`, `frame/design.md:60` and `frame/plan.md:13`, commit `79252e48`, at `v0.27.2` and at its merge `569780ef`) and #1235 (`1793538230-code-text-brought-to-the-tree`, `frame/design.md:18`, commit `79252e48`, at `v0.27.3` and still at HEAD). #1231's docstring and two frame lines were the fourth instance, and round 1 caught them at the cost of one finding, a fix pass and a second finding on the judgment row (G6). The cost: one test module, one `git for-each-ref` per distinct cited commit (12 at HEAD), and the full history that CI's pytest jobs already fetch (G9). No refusal in the ten revisions probed was anything but a dead commit (P2), so the measured false-positive count is 0. The rule's "Nothing is kept beside the tree" holds: the check stores no list and no count |
| G2. `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A script holds a gate only on a fact it reads exactly: an exit code, a parser's result, or a line of the plugin's own forms in the one spelling the form gives it", and "A reading that is noisy or guessed from words is reported, never used to block" | `<commit>:<path>` is this repository's own citation form (G7), and `tests/censuses.py#COMMIT_PATH` already reads it. The verdict comes from git: `for-each-ref --contains` lists a containing ref or fails. A bare SHA is a different case. Whether "at `79252e48`" says where a file was read is a reading of the sentence, and bare SHAs also fill the plan's Status cells and a round's `fixed <sha>` lines, which name the branch's own commits by rule (G8). So the bare-SHA half of the issue is decided against, and the proofer goes on reading it |
| G3. `skills/core/SKILL.md` *The first value: efficient development through the workflow*, paragraph *A judgment stands on a source document, and is written down with both* | The next session follows a frame's grounds, a plan's judgments, a changelog and a shipped file's citations to their source. Those are the files the check reads. A round record, a phase record and a guarantee record what a party ran, at the branch's own commits, and leave with the work item (G5) |
| G4. `skills/core/SKILL.md` *The rule a mechanism is kept against*: "ask whether the structure should change" | Two structures are weighed in `plan.md` *Alternatives considered*. The first is `tests/censuses.py#RECORDS`, which keeps `seal/threads/` out of the citation readers. This check departs from it for every file but `trail/` and `guarantee.md`, because a `<commit>:<path>` is pinned to a moment by its form and fails only when the commit dies. The second is the census framework, which the check stays out of (A6) |
| G5. `docs/one-root-by-lifetime.md` *The dependency rule*: "The coupling left is a round record's `target:` line, read while its pull request is open and gone with the record"; `docs/the-review-record.md` *`target:` names a commit, not a content anchor, because a round records a moment*: "A squash orphans the commit after the merge" | A round's evidence lines cite `<target>:<path>` for the commands it ran at its target, so they die at the squash with `target:` itself. P1 lists such citations in released work items at every tag from `v0.24.0` to `v0.27.3`, for example #1186's eight and #1146's five. Leaving `trail/` and `guarantee.md` unread keeps the check from refusing every later branch on those records. The sentence above names only `target:`, so the rule change rewrites it to name the trail's citations too (*Rule changes*, second and third items) |
| G6. #1231 round 1, finding 1, and round 2, finding 1 (`seal/threads/1793538229-each-passage-keeps-its-home/trail/rounds/round-1.md` and `round-2.md`) | Round 1 found the docstring citing a commit of #1237's branch, and it was fixed to the squash `48d035aa`. Round 2 counted the class for that one commit as a sample, and the orchestrator filed #1270 in place of a count of one (`frame/plan.md` *Judgments of the run*, row 2 of that work item). Round 2 also judged that `trail/phases/phase-1.md:7`, which records what phase 1 read at `79252e48`, stands as history. This frame keeps that judgment: the check does not read `trail/` |
| G7. `docs/the-record-layout.md` *seal/threads/<work-item-id>/*: "A document that still cites a record of it writes the path a commit holds, as `<commit>:<path>`, which `git show` opens as written" | This fixes the form, and the section is where the new rule lands (*Rule changes*, first item). No unsettled design changes this section. The unsettled changes to `docs/the-record-layout.md` name *seal/*, *The root records* and *The fold, and what tells it from a deletion* (read) |
| G8. `skills/implement/SKILL.md` *3. The SDD file set*: "Where feature branches squash, those commits stop resolving at the merge ... Nothing measures from the column, which is why that is tolerable" | A Status cell holds a bare commit and the check does not read it. That leaves the plan's Status column as the policy states it |
| G9. `.github/workflows/test.yml:118-120` (`fetch-depth: 0` on every pytest job) and `tests/text/test_ci_gives_the_checks_what_they_need.py`, which holds that depth | CI's checkout holds `refs/remotes/origin/main` and every `refs/remotes/origin/release/*` (read). The suite is not handed the base, so the check reads reachability from the main and release refs and not from "the base" as the issue words it. For a feature pull request the base is a release branch, and for the release pull request it is `main`, so both are covered |
| G10. `docs/branch-and-release.md` *Work accumulates on a release branch*: feature branches squash into the release branch, and a squashed feature branch can be deleted once its pull request merged | A feature branch's commits die at its squash, and deleting the branch removes the last ref a clone could fetch them by. The check therefore never counts a feature branch's ref as reaching a commit. It counts only `main` and `release/*`, the patterns the section's rulesets table names |
| G11. `tests/behaviour/test_a_cited_section_stands_in_its_file.py:66-69` and its module docstring, which computes its fixture's contract rule number when the case runs "so this file holds no dangling contract citation of its own" | This is the sibling reader. It reads no `<commit>:<path>` (comment at `:68`), so the two readers do not overlap. The new module follows its precedent: it builds every planted token at run time, so the module holds no `<commit>:<path>` of its own |
| G12. #1269, the 0.27.x settle (`14bfd992`) | It removed `1793521558`, so the seven citations #1257 merged are gone from the tree. Two of those seven sat in that work item's frame and are refused by P2 at `569780ef`. The other five sat in `trail/phases/phase-3.md`, which this check does not read (*Scope*, out) |
| G13. Issue #1270, body as folded, and the orchestrator's line that it has no comments (executed by the orchestrator: `gh issue view 1270 --json comments`, 2026-11-02T06:12Z; re-read here: `gh issue view 1270 --json title,body,comments`, executed, `comments: []`) | The scope's source. The milestone `release: 0.28.1` description calls #1270 "another reading that passes what it cannot read" (executed: `gh api .../milestones`) |
| G14. The orchestrator's instance, `skills/writing-style/SKILL.md:288`, which cites `0ed5dd3b:seal/specs/1792449518-settle-squashes-specs-into-docs-in-place/spec.md` | It resolves. `0ed5dd3b` is an ancestor of `origin/main` and of `origin/release/v0.28.1`, and `git cat-file -e` finds that path at it (executed). It is no instance, and P2 at HEAD does not refuse it |
| G15. The measure at `48d035aa` | In a fresh `git clone --no-local` of the worktree, `git cat-file -t 79252e48` exits 128. After fetching `refs/pull/1237/head` into that clone, `git diff --quiet 79252e48:<path> 48d035aa:<path>` exits 0 for both `phase-1.md` and `phase-2.md` of `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/` (executed). So `48d035aa:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md` holds what #1235's frame cites |

### Probes

| # | Command | Result |
|---|---|---|
| P1 | A probe script that lists every token of the form hex-colon-path in every tracked file at a revision and asks `git merge-base --is-ancestor` against `origin/main` and `origin/release/v0.28.1`, run at HEAD and at `v0.24.0`, `v0.25.0`, `v0.26.0`, `v0.27.0`, `v0.27.1`, `v0.27.2`, `v0.27.3` and `5f0cf7a7`, followed by `gh api repos/MichaelYcJo/AgenticSeal/commits/<sha>/pulls` for each dead commit | executed. At HEAD: 55 tokens and 19 commits. Three commits reach neither ref: `79252e48` (3 tokens), `2dfbc3fe` (#1275's own branch, cited in `1793541311` `trail/rounds/round-2.md:32`) and `e953d0a9` (#1278's own branch, cited in `1793542348` `trail/rounds/round-2.md:110`). At every tag, dead citations stand in `trail/` and `guarantee.md`, and all but three name a commit of the citing work item's own pull request. The three that do not are `79252e48` (#1237), `137d0a9c` (#1036, cited in `1793174169` `trail/rounds/round-5.md`) and `7ef6abbf` (#901, cited in `1793521562` `guarantee.md`) |
| P2 | The scoped check as this frame defines it: `tests/censuses.py#COMMIT_PATH` tokens, files outside `evals/behaviour/`, `seal/threads/*/trail/` and `seal/threads/*/guarantee.md`, refused where `git for-each-ref --contains <sha> 'refs/remotes/*/main' 'refs/remotes/*/release/*'` lists nothing or fails. Run with `git show <rev>:<file>` at HEAD, the seven tags above, `5f0cf7a7` and `569780ef` | executed. HEAD: 432 files read, 33 tokens, 12 commits, one refused (`1793538230` `frame/design.md:18`, `79252e48`). `v0.24.0`, `v0.25.0` and `v0.27.1`: none refused. `v0.26.0` and `v0.27.0`: `1793401152` `frame/design.md:50`. `v0.27.2`, `5f0cf7a7` and `569780ef`: `1793521558` `frame/design.md:60` and `frame/plan.md:13`. `v0.27.3`: `1793538230` `frame/design.md:18`. The probe took 5 to 7 seconds a revision, most of it one `git show` per file. The module reads the working tree instead, so its own time is not measured here |
| P3 | `git clone --no-local` of the worktree under the scratch directory, then the commands of G15 | executed, as G15 states |

Every probe ran under `<scratchpad>/1270-probe/`, committed nothing and ran
none of the repository's checks. The directory was removed before the
hand-back.

## Scope

In:

1. **The check.** A new module, `tests/text/test_a_cited_commit_outlives_the_squash.py`, holds one case over the tree. Each `<commit>:<path>` token, as `tests/censuses.py#COMMIT_PATH` reads it, in every tracked file that decodes as UTF-8 must name a commit that one of the reaching refs contains. Three kinds of file are left out: anything under `evals/behaviour/`, a work item's `seal/threads/<id>/trail/` and its `seal/threads/<id>/guarantee.md`. The reaching refs are every ref matching `refs/remotes/*/main`, `refs/remotes/*/release/*`, `refs/heads/main` or `refs/heads/release/*`. A commit the object store lacks is refused like one no reaching ref contains, because a fresh clone lacks every dead commit (G15).
2. **What a refusal says.** It names each citing file and line and the commit. It gives the repair: cite the squash commit on the release branch or on `main` that holds the same file, or the path at HEAD where the file is the branch's own. It adds that a local checkout whose `main` or release refs are older than the cited squash is answered by `git fetch`.
3. **No ref, no judgment.** Where no reaching ref stands in the checkout, the tree case skips, and its reason names the four patterns it found nothing for. Nothing is judged, and the skip is printed under `-rfEs` (G9).
4. **The behaviour cases.** Each case plants a repository under `tmp_path` and builds every token at run time, so the module holds no `<commit>:<path>` of its own (G11). They cover scenarios S2 to S7.
5. **The one instance at HEAD.** `seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md:18` cites the measure at `48d035aa`, at the same path, in place of the dead commit (G15). The row keeps the fact that issue #1235 cited `79252e48`, the head of #1237's branch, written bare.
6. **The class, as far as the release branch brings it.** After the orchestrator merges `release/v0.28.1` in, the tree case is run again. Any citation it refuses, in a sibling work item's frame or a shipped file, is corrected in this branch as item 5 was. Each correction is listed in the phase record, because contract rule 12 owes the fix to every instance.

Out:

- **Bare SHAs.** A commit written without `:<path>` is not read, on G2's grounds. The proofer goes on reading it.
- **`trail/` and `guarantee.md`.** Not read, on G3's and G5's grounds. P1 shows what stays open there. Five of #1257's seven sat in `trail/phases/phase-3.md`, and `137d0a9c` and `7ef6abbf` are two more cross-branch citations of the same kind. The rule change states this as part of the rule, and the proofer reads these files at review.
- **Issue bodies.** #1234, #1236, #1255 and #1256 are open and cite `79252e48` (executed: `gh issue view <N> --json state`, OPEN). A tree check reads no issue body. Round 2 of #1231 (*Not judged*, third row) left editing them to the orchestrator, and this frame leaves it there.
- **Whether the path exists at the commit.** Not checked. `COMMIT_PATH`'s path part `[\w./-]+` takes a sentence's closing period into the token (read), so a path check would refuse correct citations at the end of a sentence.
- **`chain_check.py` and the hygiene workflow.** Neither gains an arm (`plan.md` A5 and A7).
- **Citations whose path does not match `COMMIT_PATH`.** A path that opens with `…` or `<`, such as `efb91989:…/little-owl-wax-seal.svg`, is no token, so the commit is not read. This limit belongs to the form's one reader, and the module adds no second pattern.
- **A committed `pr.*.md`.** Such a file would copy the records' text, and the check would read it. None has ever been committed (executed: `git log --all --diff-filter=A -- 'seal/threads/*/pr.*.md'`, empty). That is a limit and no guard is built for it.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The tree holds no dead citation | Given this tree after *Scope* item 5 (and item 6 once the release branch is merged in), when the tree case runs with `origin/main` and `origin/release/*` present, then it passes. Before item 5, it fails naming `seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md:18` | `tests/text/test_a_cited_commit_outlives_the_squash.py`, the tree case. Seen red on the real instance before item 5's edit |
| S2 A citation of a feature branch's commit is refused | Given a planted repository with `main`, a `release/v9.9.9` branch and a feature branch commit that neither contains, and a tracked `.md` and a tracked `.py` each citing that commit with a path, when the reader runs, then it names both files, each line and the commit | the module, a case parametrised over the two extensions |
| S3 The squash is accepted | Given the same repository with the citation pointing at a commit `release/v9.9.9` contains, when the reader runs, then it names nothing | the module |
| S4 The scope's boundary | Given the dead citation in `seal/threads/<id>/trail/rounds/round-1.md`, in `seal/threads/<id>/trail/phases/phase-1.md`, in `seal/threads/<id>/guarantee.md` and in `evals/behaviour/<agent>/<case>/x.md`, when the reader runs, then it names none of them. Given the same citation in `seal/threads/<id>/frame/plan.md`, `seal/threads/<id>/changelog.md` and `seal/threads/<id>/gaps.md`, then it names each | the module, one case per side |
| S5 A commit no clone holds is refused | Given a token whose hex names no object in the repository, when the reader runs, then it names it as it names an unreached commit | the module |
| S6 No reaching ref, no judgment | Given a planted repository with no `main` and no `release/*` ref, local or remote, when the reader runs, then it returns the state that nothing was judged, and the tree case's skip reason names the four patterns | the module |
| S7 The refusal says the repair | Given S2's repository, when the tree check's assertion message is built, then it holds each file and line, the commit, the two ways to repair it and the `git fetch` sentence | the module, asserting the message's parts as values the case computes, not a pinned sentence |

## Data & interfaces

The module holds these units. The names are the build's to choose:

- `cited(root)`: `[(rel, line, commit)]` for each `COMMIT_PATH` token in the
  files *Scope* item 1 reads, from `git ls-files -z` and the working tree,
  as `tests/behaviour/test_a_cited_section_stands_in_its_file.py#corpus`
  reads them.
- `reaching(root)`: the refs matching the four patterns, from one
  `git for-each-ref` call.
- `unreached(root)`: `None` where `reaching` is empty, else the subset of
  `cited` whose commit no reaching ref contains or whose object is missing.
  It makes one `git for-each-ref --contains <commit> <refs>` call per
  distinct commit and reads the exit code and the output.

`COMMIT_PATH` is imported from `tests/censuses.py` and is not copied. No
shipped file changes. `hooks/`, `skills/`, `agents/`, `templates/` and
`.github/` are untouched.

## Rule changes

- add
  file: docs/the-record-layout.md
  section: seal/threads/<work-item-id>/
  to: **A `<commit>:<path>` citation names a commit that `main` or a release
    branch reaches, except in a work item's `trail/` and its
    `guarantee.md`.** A feature branch squashes into its release branch, and
    the squash discards every commit the branch wrote, so a citation of one
    opens in no clone after the merge, and a reader sent to it finds no
    source. The commit to cite is the squash that holds the same file, or
    the path at HEAD where the file is the branch's own. A round record, a
    phase record and a guarantee cite what a party ran at the branch's own
    commits, which the squash orphans as it orphans the round's `target:`
    line, and they leave with the work item. A bare commit is not read: a
    plan's Status cell and a round's `fixed` line name the branch's own
    commits by rule, and whether a sentence cites a bare commit as where a
    file was read is the reviewer's reading. Where the checkout holds no
    `main` or release branch ref, nothing is judged.
    check: tests/text/test_a_cited_commit_outlives_the_squash.py
- change
  file: docs/one-root-by-lifetime.md
  section: The dependency rule
  from: The coupling left is a round record's `target:` line, read while
    its pull request is open and gone with the record.
  to: The coupling left is a record of what a party ran at the branch's own
    commits: a round record's `target:` line, and a `<commit>:<path>` that a
    work item's `trail/` or `guarantee.md` cites at such a commit. Both are
    read while the pull request is open and go with the record. Every other
    `<commit>:<path>` names a commit `main` or a release branch reaches
    (`docs/the-record-layout.md` *seal/threads/<work-item-id>/*).
- change
  file: docs/one-root-by-lifetime.ko.md
  section: 종속 규칙
  from: 남은 묶임은 라운드 기록의 `target:` 줄 하나이고, 그 PR 이 열려 있는
    동안 읽히고 기록과 함께 사라집니다.
  to: 남은 묶임은 당사자가 브랜치 자신의 커밋에서 실행한 것의 기록입니다.
    라운드 기록의 `target:` 줄, 그리고 작업 항목의 `trail/` 이나
    `guarantee.md` 가 그런 커밋에서 인용한 `<commit>:<path>` 가 그것입니다.
    둘 다 PR 이 열려 있는 동안 읽히고 기록과 함께 사라집니다. 그 밖의
    `<commit>:<path>` 는 `main` 이나 릴리스 브랜치가 닿는 커밋을 가리킵니다
    (`docs/the-record-layout.md` *seal/threads/<work-item-id>/*).

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The citation of the measure at `79252e48`, a commit of #1237's branch that no clone holds | `seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md` *Grounding*, the issue row (line 18) | The same row cites the measure at the squash `48d035aa`, which holds the file byte for byte (G15). The issue's own citation stays as a bare `79252e48` |

The check is a new mechanism, and nothing comes out in return for it. No
file instructs anyone to check that a `<commit>:<path>` opens (executed:
`git grep -n -i 'orphan\|stops resolving\|<commit>:<path>'` outside
`seal/threads/`). The class had no reader but a reviewer's own axis, which
#1231's round 1 walked on its own initiative. That reading stays, because
the check leaves bare SHAs, `trail/` and `guarantee.md` to it (*Scope*,
out). The sibling reader's comment at
`tests/behaviour/test_a_cited_section_stands_in_its_file.py:68` stays true,
because that reader still skips a `<commit>:<path>`. The check was not
added at a blocked step. It answers a class that G1's record shows reaching
three releases.

Framed 2026-11-02 by framer, before the build.
