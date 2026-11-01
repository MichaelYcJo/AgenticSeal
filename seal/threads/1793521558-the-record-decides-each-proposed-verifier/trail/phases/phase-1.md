# Phase 1: 1793521558-the-record-decides-each-proposed-verifier

## What this phase found

This record decides C1, C7 and C8 of `frame/design.md` *Scope* item 1. The tree is read at `813665f08eb48c63ae48dbdc17006491f3852410` (`813665f0`) and the tracker on 2026-11-01. Each figure below is a figure at those two moments unless its sentence names another. Each decision and the counts it stands on stand once, in the candidate's row of *The decisions*. The instances read one by one stand under *Instances*, and each command stands whole under *Commands*.

### Whether the frame holds

The frame holds, and the build follows it except where this list says. Each item is a departure or a reading the frame left open, with its grounds.

- **Nine guarantees stood at no release tag.** `frame/design.md` *Scope* item 2 asks C7 for the samples' sizes "from each `guarantee.md` *Claims re-run* at the release tags". The nine work items of 0.22.4 that wrote a `guarantee.md` were settled before `v0.22.4` was tagged, so no tag holds them. *Command C7* reads every `guarantee.md` that `813665f0`'s history adds, each at the last commit of that history that wrote it. For a file a tag holds, that reading gives the rows of the last tag that held it: the two readings were compared file by file and agree.
- **A withheld verdict was rewritten in place before 0.27.0.** Through 0.26.0 the next sealer run replaced a withheld block, so a final `guarantee.md` shows only its last verdict; #1044's body says the same of 0.22.x. The sealer's catches inside its sample therefore stand only in the pull requests' own commits. *Command C7* reads them in a `git clone --no-local` under the scratch directory, with `refs/pull/*/head` fetched from GitHub, the fetch plan *Technical context* places there. The worktree was not written.
- **The compare records stand under each work item's `evals/`, not under the top-level `evals/`.** *Scope* item 2 asks for "the compare records `git log --all` holds under `evals/`". They stand at `seal/specs/<item>/evals/*.md`. `--all` reads every ref of a clone, and this clone holds other sessions' branches, so *Command C8* reads `813665f0`'s history instead. That history holds 28 compare records and `false-rows.md`, which is not one. A 29th record, `seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/evals/971-warden-phase-3-864798a4.md`, stands only at `837ee9bc`, on a ref outside that history. It regrades sides another record of the same work item holds, reads `pass`, and adds no side and no fail.
- **C1's decided-by sentence covers only an absence.** *Scope* item 2 gives C1 "drop where no such defect and no recurring row stands". The record holds such defects and a recurring row (*Instances C1*), so that sentence does not decide C1. The row decides it under G1 and G2, and its *Grounds* cell gives the weighing.
- **C8's `narrow` is drafted as an issue, which *Scope* item 3 does not list.** Item 3 names a draft for a `build`, a `limit`, a kept issue and a dropped issue. C8 has no issue, and its decision changes `evals/README.md`. Plan row A2 drafts every change to the tree as an issue, so C8's act is `file D2`. Plan *Operational impact* step 1 creates the minor milestone only where a candidate other than C11 is `build`, so D2 names a home for the case where no phase decides a `build`.
- **No question of C1, C7 or C8 waits on a paid run.** Each is decided on the record, so `gaps.md` *Not verified* holds C5's question as *Scope* item 5 names it, and no other paid-run row.
- **No `seal/follow-up.md` row is this phase's.** The two rows G12 names, at `813665f0:seal/follow-up.md:49` and `:51`, are C9's and C4's, which phase 3 decides (read).

### The decisions

| Candidate | Command or coordinate | What the record shows | Decision | Grounds | Act |
|---|---|---|---|---|---|
| C1 a project-specific verifier that drives the real application | *Command C1*, executed on the tracker 2026-11-01 and over the tags `v0.0.1` to `v0.27.1`. The issue list is whole for the two labels; which of its issues describe such a defect is a `sample`, judged from the 182 titles read one by one and 13 bodies opened. An issue carrying neither label, and a user's repository, whose record is not in this tree, are the open part | Three defects merged or shipped past a green suite in what Claude Code showed a person, which no command or test of the time reached: #400, #717 and #911 (*Instances C1*). The owner found each at the first look, and each class was held by a case, a constant or a procedure once the platform's behaviour was known. None recurred, and no issue labelled `from-use` was opened after #911. Of 384 closed `## Not verified` rows at those tags, 31 concern a screen or a live harness. The owner answered 4 by looking at the stamp, at no cost the rows state beyond the look; 22 closed into a limit sentence and 5 by other means. The row that recurs is the stamp's look, held at `813665f0` by `docs/the-review-record.md` *The stamp*, `check: none reader: the owner on the first real run after a change here`, and it stood open once more at `v0.26.0` and `v0.27.0`. The tree's one driver of a session, the behaviour suite, grades what a run writes (`evals/README.md` *The behaviour suite*, read), and none of the three defects is something a run writes | drop | G1, "A mechanism stays only while its record of what it caught outweighs what it costs": each defect's class is held by what its fix wrote, and the recurring row is answered by a look the owner takes at every seal. G2: a verifier that drives an interactive session is a paid session per change, of the kind whose cost C8's row states | none |
| C7 the sealer reads every `executed` and `seen red` claim against the implementing agent's transcript | *Command C7*, executed at `813665f0`, in a scratch clone with every `refs/pull/*/head` fetched on 2026-11-01, and on the tracker 2026-11-01. The guarantees and their withheld verdicts are whole for `813665f0`'s history and the fetched pull request heads. The claims found false after a seal are a `sample`: six issue searches since 2026-10-16, and one search of every record at the tags `v0.22.0` to `v0.27.1` for another work item's phase record named beside a word of falsity. A claim found false in other words, or in no record, is the open part | 84 guarantees re-ran 1,255 claims, 263 of them on a seen-red or mutation claim. In the final files 4 rows did not hold, and none of the 4 is an `executed` or `seen red` claim. The pull request heads hold 52 distinct withheld verdicts. Two of them withheld on a crafter's claim that did not hold, a sweep and a mutation claim a later commit had disarmed, and both were repaired before the merge. Outside the samples, no search finds an `executed` or `seen red` claim that a later round, a later work item or use found false, and that includes #955's unsampled mutation claims, #1048's own example (*Instances C7*). At `813665f0` the labels are `executed`, `read` and `unverified` (`skills/verify/SKILL.md:233-241`), as #1148 left them | drop | *Scope* item 2 for C7: "drop where the record holds none; #1048 closes". G1: a proposed mechanism with no catch of its own is dropped. Plan row A8 weighs the sealer's sample for removal. The premise that keeps it, that it has catches of its own, holds: the two withheld verdicts above. Its cost is a share of one sealer segment, measured at 2.8 minutes and 30 tool calls for #1192's (#1195's comment, read) | close #1048 with D1 |
| C8 the behaviour suite as the proof of a preload rewrite | *Command C8*, executed at `813665f0`. Whole for the records that history holds; the one record outside it is named in *Whether the frame holds* | 28 compare records over 32 distinct sides, 544.17 USD and 24.4 hours of wall time as the records state them, where the two planted variants of `1791933022` record no spend. 15 read `fail`. One fail was a defect later confirmed: the rewritten warden left a finding's `verdict:` line out of 5 of 18 records, then 1 of 18, which rule 3's shape graders read. The fix had the warden read its record through `chain_check.py` before handing back, and the next side passed 18 of 18. At `813665f0`, `agents/proofer.md` step 7 holds that read, so a script now holds the class. One fail was acted on for bytes (rule 4), which a byte count answers with no run, and one measured a model and kept the Opus pin. Every other fail was read as run-to-run variation, or as a definition the contract contradicted, and none was acted on as a defect. Three of the 15 are regrades of sides already counted, and one is a planted variant (*Instances C8*). Since #1081 closed at the 0.22.4 settle, rewrites have shipped without the run by default, and no issue of *Command C1*'s list since then names a defect of a rewritten preload. 13 `check:` lines in 7 shipped files name a case of the suite | narrow | G1 and G2. What the suite caught is gross breakage of an agent's output, read by its shape graders, and that part stays as a smoke run. Recall, the false-finding rate and the token figures failed rewrites that no reading found worse, at the cost the row states. A pass does not judge a shift in meaning, which the proofer's reading of the diff judges (#1038's comment of 2026-10-30). Removal was weighed as an equal (plan row A8): it would leave 13 `check:` lines naming cases nothing keeps, while the one catch's class is already held by a check, so the narrowed run's own catches are what its next record weighs | file D2 |

### Commands

Each command runs from the root of a worktree of this branch unless its heading says otherwise. A tag after `v0.27.1` would add rows to the tag loops, so each loop stops at `v0.27.1`.

#### Command C1

Executed on 2026-11-01.

```
gh issue list --search 'label:from-use,bug' --state all --limit 400 --json number,labels \
  --jq 'length, ([.[]|[.labels[].name|select(.=="bug" or .=="from-use")]|sort|join(",")]|group_by(.)|map("\(.[0]) \(length)")|join("; "))'
gh issue list --search 'label:from-use,bug' --state all --limit 400 --json number,title --jq '.[]|"\(.number) \(.title)"'
for n in 400 717 911; do gh issue view $n --json number,milestone,closedAt,labels --jq '"#\(.number) \(.milestone.title) closed \(.closedAt[:10]) \([.labels[].name]|join(","))"'; done
gh issue list --label from-use --state all --search 'created:>=2026-10-13' --json number --jq '[.[].number]'
for t in $(git tag -l 'v*' | sort -V | sed '/^v0\.27\.1$/q'); do git grep -h -E '^\| closed ' "$t" -- seal/; done | sort -u > closed.txt
wc -l < closed.txt
grep -iE 'screen|terminal|render|live (claude|session|harness)|real (claude|session)|claude code session|by eye' closed.txt > screen.txt
wc -l < screen.txt
git grep -n 'how the wax stamp looks in a real terminal' v0.26.0 v0.27.0 -- 'seal/threads/*/gaps.md' | cut -d: -f1-3
git show 813665f0:docs/the-review-record.md | sed -n '409,410p'
```

It printed `182` and `bug 130; bug,from-use 23; from-use 29`, then the 182 titles, then:

```
#400 release: 0.15.7 closed 2026-09-28 agents-skills,from-use,merged: 0.15.7
#717 release: 0.17.0 closed 2026-10-03 bug,hooks-gates,merged: 0.17.0
#911 release: 0.21.1 closed 2026-10-13 from-use,merged: 0.21.1
[911]
384
31
v0.26.0:seal/threads/1793401152-the-seal-draws-a-round-headed-little-owl/gaps.md:8
v0.27.0:seal/threads/1793401152-the-seal-draws-a-round-headed-little-owl/gaps.md:8
No case, hook or workflow can observe a screen.
check: none reader: the owner on the first real run after a change here
```

#911, opened on 2026-10-13, is the last issue labelled `from-use`. The 31 rows of `screen.txt` are judged under *Instances C1*.

#### Command C7

Executed at `813665f0` on 2026-11-01. Part (a) reads every guarantee's *Claims re-run*:

```
python3 -I - <<'EOF'
import re, subprocess

def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True).stdout

paths = sorted(set(git("log", "813665f0", "--diff-filter=A", "--name-only",
                       "--format=", "--", "seal/*guarantee.md").split()))
rows = red = 0
bad = []
for p in paths:
    last = git("log", "813665f0", "--full-history", "-n1", "--format=%h",
               "--diff-filter=AM", "--", p).strip()
    assert last, p
    text = git("show", f"{last}:{p}")
    m = re.search(r"^## Claims re-run\s*$(.*?)(?=^## |\Z)", text, flags=re.M | re.S)
    for r in (m.group(1).splitlines() if m else []):
        if not r.startswith("|") or r.startswith(("|---", "| Claim")):
            continue
        rows += 1
        if re.search(r"seen red|mutant|mutation|seal mutate|went red|goes red|go red", r, re.I):
            red += 1
        if re.search(r"\|\s*does not hold", r):
            bad.append((p.split("/")[2], r[:90]))
print(len(paths), "guarantees;", rows, "rows of Claims re-run;", red, "on a seen-red or mutation claim")
for b in bad:
    print("does not hold:", *b)
EOF
```

It printed `84 guarantees; 1255 rows of Claims re-run; 263 on a seen-red or mutation claim`, then four `does not hold:` lines, for `1792252400-the-sealer-reads-the-gate-the-orchestrator-ran`, `1792368015-every-finding-carries-an-evidence-line` and twice `1793457436-row-deletion-check-and-a-symlink`. `--full-history` matters: without it, `git log` simplifies away the side of a merge that wrote a file, and four of the paths then name no commit.

Part (b) reads the withheld verdicts, from an empty scratch directory with `W` set to this worktree's path:

```
git clone -q --no-local "$W" clone-1793521558
git -C clone-1793521558 remote set-url origin https://github.com/MichaelYcJo/AgenticSeal.git
git -C clone-1793521558 fetch -q origin '+refs/pull/*/head:refs/pull/*/head'
git -C clone-1793521558 log --no-merges -G '^Verdict: withheld' --format=%h \
  --glob='refs/pull/*/head' -- 'seal/*guarantee.md' > withheld-commits.txt
wc -l < withheld-commits.txt
while read h; do
  git -C clone-1793521558 show --format= "$h" -- 'seal/*guarantee.md' |
    grep -E '^\+Verdict: withheld'
done < withheld-commits.txt | sort -u > withheld.txt
wc -l < withheld.txt
grep -n -E "smith's|crafter's|does not hold at 00f95bb1" withheld.txt | cut -c1-110
```

It printed `96` commits and `52` distinct verdict lines, and six lines numbered 9, 14, 17, 24, 25 and 50. Line 25 names the orchestrator's sentence, not a crafter's, and *Instances C7* judges the other five.

Part (c) is the search for a claim found false after a seal:

```
for q in '"seen red"' mutant '"phase record"' claimed '"went red"' executed; do
  gh issue list --state all --limit 100 --search "$q created:>=2026-10-16" --json number --jq '.[].number'
done | sort -un | wc -l
for t in $(git tag -l 'v0.2[2-7].*' | sort -V | sed '/^v0\.27\.1$/q'); do
  git grep -h -E '[0-9]{10}-[a-z0-9-]+/(trail/)?phases/phase-[0-9]+\.md' "$t" -- 'seal/*.md'
done | grep -iE 'false|does not hold|did not hold|never (ran|went red)|survived|untrue|contradict' | sort -u | wc -l
git show 813665f0:skills/verify/SKILL.md | sed -n '233,241p'
gh issue view 1195 --json comments --jq '.comments[].body' | grep -A6 '#1192 sealer segment'
```

It printed `63` issues and `5` record lines, then the three labels of condition 4, then the #1192 sealer segment's table, whose *span* row reads `2.8m, 30 tool calls`. The titles of the 63 issues were read, and *Instances C7* names the bodies opened.

#### Command C8

Executed at `813665f0`:

```
python3 -I - <<'EOF'
import re, subprocess

def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True).stdout

paths = sorted(set(git("log", "813665f0", "--format=", "--name-only", "--",
                       "seal/**/evals/*.md").split()))
sides = {}
for p in paths:
    last = git("log", "813665f0", "--full-history", "-n1", "--format=%h",
               "--diff-filter=AM", "--", p).strip()
    assert last, p
    text = git("show", f"{last}:{p}")
    verdict = re.search(r"^Verdict: (\w+)", text, flags=re.M)
    tail = text[verdict.end():] if verdict else ""
    rules = sorted(set(re.findall(r"\(rule (\d)\)", tail)))
    def cell(k):
        m = re.search(r"^\| " + re.escape(k) + r" \| ([^|]+) \|", text, flags=re.M)
        return m.group(1).strip() if m else None
    for side in ("Baseline", "New"):
        run, spend, wall = cell(side + " run"), cell(side + " spend USD"), cell(side + " wall seconds")
        if run and spend:
            sides[run] = (float(spend), float(wall))
    print(last, p.split("/")[2][:10], p.rsplit("/", 1)[1],
          verdict.group(1) if verdict else "no verdict", "rules " + ",".join(rules) if rules else "")
print(len(sides), "distinct sides,", round(sum(s for s, _ in sides.values()), 2), "USD,",
      round(sum(w for _, w in sides.values()) / 3600, 1), "hours of wall time")
EOF
git grep -n -E '^check:.*evals/behaviour/' 813665f0 -- ':!seal/' | cut -d: -f2 | sort | uniq -c
```

It printed:

```
8350c578 1791933022 q7-fence-deleted.md pass
8350c578 1791933022 q7-needs-a-fix-removed.md fail
2fc33333 1792126889 framer-phase-3.md fail rules 5
2fc33333 1792126889 sealer-phase-3.md fail rules 3,5
2fc33333 1792126889 smith-phase-3.md pass
2fc33333 1792126889 warden-phase-2-run-1.md fail rules 3
2fc33333 1792126889 warden-phase-2.md fail rules 3
2fc33333 1792126889 warden-phase-3.md pass
f6ae6db6 1792251842 framer-phase-4.md fail rules 5
f6ae6db6 1792251842 smith-phase-4.md pass
f6ae6db6 1792251842 warden-phase-4.md fail rules 5
4a6e24f6 1792252400 sealer-model.md fail rules 3,4,5
4a6e24f6 1792252400 sealer-phase-4.md pass
f1c9932d 1792311781 sealer-phase-4.md pass
8a100e13 1792363189 957-framer-phase-3.md fail rules 5
8a100e13 1792363189 957-sealer-phase-3.md fail rules 3,5
8a100e13 1792363189 957-smith-phase-3.md pass
8a100e13 1792363189 957-warden-phase-2-run-1.md fail rules 3
8a100e13 1792363189 957-warden-phase-2.md pass
8a100e13 1792363189 957-warden-phase-3.md pass
75502328 1792363231 sealer-phase-5.md pass
8db076f8 1792366315 971-warden-phase-3-11ebe8f4.md pass
8db076f8 1792366315 false-rows.md no verdict
b196fe9b 1792367880 sealer-phase-3.md fail rules 4
b196fe9b 1792367880 sealer-phase-3b.md fail rules 5
a1909096 1792368014 framer-phase-2.md pass
2ff7b963 1792368015 warden-phase-3.md fail
334189fd 1793273065 framer-phase-8.md fail rules 5
334189fd 1793273065 sealer-phase-8.md pass
32 distinct sides, 544.17 USD, 24.4 hours of wall time
   1 agents/framer.md
   1 agents/proofer.md
   4 agents/sealer.md
   1 docs/the-agent-set.md
   3 skills/agent-contract/SKILL.md
   2 skills/code-review/SKILL.md
   1 skills/verify/SKILL.md
```

`1792368015`'s record predates the `(rule N)` tags, and its two reasons name recall and the false-finding rate, rules 1 and 2.

### Instances

#### Instances C1

The bodies opened are #237, #249, #256, #400, #448, #475, #717, #720, #894, #896, #911, #1184 and #1185 (read: `gh issue view <n>`). Three describe a defect no command or test of the time reached:

- **#400**, fixed in 0.15.7. The stamp was drawn where only an agent could see it, and the owner raised it on 2026-09-15: "I have never once seen it printed". A tool call has no controlling terminal, so no command could see where the drawing landed. The fix draws the stamp in the orchestrator's session from a `Stop` hook. What a screen shows stays the limit sentence of `docs/the-review-record.md` *The stamp*.
- **#717**, fixed in 0.17.0 before its tag. The harness persists a hook's `systemMessage` past about 10,000 characters and shows a preview, and #666 had pushed the stamp past that, so every seal after #666's merge reached the owner as a preview. A headless `claude -p` probe then measured the limit, which `skills/verify/scripts/seal_stamp.py#MESSAGE_LIMIT` holds and `#admitted` applies, pinned by `tests/skills/test_seal_stamp.py` (read).
- **#911**, fixed in 0.21.1. `AskUserQuestion` shows every question of one call at once, so the routing question showed four boxes that mean nothing under `automation`. The owner met it at the start of most runs. The fix asks the second question in a call of its own.

The other ten are read as not this kind. #237 is a prompt per worktree creation, a cost of the guard's design that a case reaches. #249 asks for a progress readout, which is a feature. #256 and #894 are a guard reading a transcript or a process table, which a case reaches through a fixture, though none had been written for those shapes. #896 is a prompt line contradicting its header, a string a case reads. #448 is Windows `cmd.exe`, which CI's Windows leg caught. #475 is the gate resolving to the installed copy, which the sealer found with `command -v`. #720 is a wide character's columns, found by a review round's reproduction. #1184 and #1185 were found by a crafter's reading, with no wrong result yet.

The 31 rows of *Command C1*'s `screen.txt`:

- The owner answered 4 by looking: S17 of `1790562543-the-stamp-reaches-the-person-it-is-drawn-for`, "seen on the owner's screen 2026-09-28", and three rows of `1791270164-the-release-seal-is-drawn-in-curves`, where the owner compared renders and printed `specseal-stamp-14.ans` and `specseal-stamp-28.ans` on 2026-10-07. No row states a cost beyond the look.
- 22 closed into a limit sentence: `docs/the-review-record.md` *The stamp*, `docs/commit-review-gate-spec.md` *Registration*, `docs/branch-and-release.md` *Cutting a release*, `docs/worktree-guard-spec.md` *Known limits*, and `docs/the-commit-gate-inside-git.md` *Known limits of the commit gate inside git*, which left the tree with that gate.
- 5 closed by other means: 3 because their subject left the tree, 1 executed by a warden's probe, and 1 by a build whose image was looked at once.

The row stood open once more as `1793401152-the-seal-draws-a-round-headed-little-owl/gaps.md:8` at `v0.26.0` and `v0.27.0`, "how the wax stamp looks in a real terminal", answered by "the owner, at the first `sealed` stamp drawn after the merge".

#### Instances C7

The four rows that did not hold in the final files (*Command C7* (a)):

- `1792252400-the-sealer-reads-the-gate-the-orchestrator-ran`: a `## Removes` row of the frame, kept as a recorded departure.
- `1792368015-every-finding-carries-an-evidence-line`: the spawn prompt's claim that the base's advance touched none of the branch's files.
- `1793457436-row-deletion-check-and-a-symlink`, twice: a crafter's `read` claim that `seal/follow-up.md` is absent, and the design's citation of a section that does not state the rule. The sealer withheld on both.

The withheld verdicts that name a crafter's claim (*Command C7* (b)):

- Line 14, at `527afede` in PR #977, work item `1792311781-the-stamp-is-drawn-from-the-sealers-verdict` (#975). The smith claimed a sweep had reworded every sentence calling the broad gate's run a stamp (`phases/phase-3.md:42-46`), and `assets/seals/README.md` still said it. This is an `executed` claim that did not hold.
- Line 9, at `245502810` in PR #1004, work item `1792533444-automation-refuses-mid-run-questions`. A fix pass's "Each new condition was mutated red" was true at `067a37a8`, and a later commit, `c4aa0c8b`, left the cases pinning none of the conditions. The sealer's re-run found each mutant surviving. This is a mutation claim that no longer held at the sealed commit.
- Lines 17, 24 and 50 name a crafter's record sentence that the tree contradicted: a `questions.md` status left open, a `gaps.md` paragraph a later commit made stale, and the `read` claim above. None is an `executed` or `seen red` claim.

Most of the other 47 lines name the orchestrator's pull request body. Several of those overstate what the records said, such as a body's "the other three were fixed" where its phase record reads "1 and 2 deferred to the frame, 3 and 4 fixed".

Outside the samples, the issue bodies opened are #1017, #1058, #1077 and #1109 (read). #1058's cases passed where they ran and failed in a `pull_request` environment that no earlier run had, so the claims were true as made. #1077 is a case that its own work item recorded as never seen failing on a paid side, a claim recorded as unverified. #1017 lists gaps the old tests already had, and #1109 a substitution the old-name census was not built to see. None is an `executed` or `seen red` claim found false. The five record lines of part (c) are a mutation tool's description, a citation, a regrade's credits, a plan alternative and a `## Not verified` row, and none reports such a claim false.

#955's guarantee (`fa7d1374:seal/specs/1793051803-settle-runs-in-local-mode/guarantee.md`, *Claims re-run*, last row) says "The other 23 rest on the phase record (unverified by this audit; the sample is named so a miss can be traced)". No later record found one of them false.

Before the seal, the proofer catches the same kind of claim. `1792624592-the-release-seal-is-drawn-from-the-stamps-cells` round 1 finding 1 (`v0.22.3`) shows a frame's "seen red against a copy of the colours" not held, and `1793251201-a-push-only-workflow-answers-a-deferral` round 5 finding 2 (`v0.24.2`) a new case never seen red. Both were fixed before the merge.

#### Instances C8

The 15 fails of *Command C8*, each with what its work item did, read at the tag or commit *Command C8* prints:

1. `1791933022` `q7-needs-a-fix-removed.md`: a planted variant of S10, built to fail (`overview.md:39` at `v0.22.3`). It is a probe and not a catch. Its pair `q7-fence-deleted.md`, also planted, reads `pass`.
2. `1792126889` `framer-phase-3.md`, rule 5: carried to #968, "the regression is carried, not dropped" (`overview.md:30` at `v0.22.2`).
3. `1792126889` `sealer-phase-3.md`, rules 3 and 5: "Not to be read as the sealer's result", since it measured a definition the new contract contradicted (`phases/phase-3.md:199-204` at `v0.22.2`).
4. and 5. `1792126889` `warden-phase-2-run-1.md` and `warden-phase-2.md`, rule 3: the catch. Five of 18 records, then one of 18, carried no `verdict:` line, and the rewrite had stopped naming that line (`phases/phase-2.md:91-102` at `v0.22.2`). Phase 3 had the warden read its record through `chain_check.py` before the hand-back, and it did so in 18 of 18 runs (`overview.md:39`). At `813665f0` the same read stands in `agents/proofer.md` step 7 (read).
6. and 7. `1792251842` `framer-phase-4.md` and `warden-phase-4.md`, rule 5: the framer's carried to #968, the warden's "recorded as it reads and not rerun" (`overview.md:52-62` at `v0.22.3`).
8. `1792252400` `sealer-model.md`, rules 3, 4 and 5: a comparison of two models. The Opus pin was kept as the measurement decided (`overview.md:27` at `v0.22.3`).
9. to 11. `1792363189` `957-framer-phase-3.md`, `957-sealer-phase-3.md` and `957-warden-phase-2-run-1.md`: regrades of 2, 3 and 4 under the new rule 3, with no new run. The work item exists because rule 3 had failed rewrites on one run of one grader (`overview.md:11` at `v0.22.3`).
12. `1792367880` `sealer-phase-3.md`, rule 4: a preload 117 bytes longer. A fix pass removed three restatements, and the next side passed rule 4 (`overview.md:22` at `v0.22.3`).
13. `1792367880` `sealer-phase-3b.md`, rule 5 by 0.9%: shipped under the owner's rule for a fail on rule 5 alone (`overview.md:29`).
14. `1792368015` `warden-phase-3.md`, rules 1 and 2: the owner's answer of 2026-10-19, "노이즈로 기록하고 출시" (record it as noise and ship), grounded in the phase's diagnosis (`overview.md:21` at `v0.22.3`).
15. `1793273065` `framer-phase-8.md`, rule 5: diagnosed from the raw sides with no re-run, as variation in what the framer opened (`gaps.md:30-31` at `v0.27.0`, and #1038's comment of 2026-10-30).

#1081 holds the two 0.22.3 work items that rewrote what agents read and took no run. It was closed at the 0.22.4 settle: "no failure on record asks for this measurement, and taking it costs more than the record shows it would catch" (read: `gh issue view 1081 --json comments`).

### Drafts

The orchestrator takes each act after the seal, as plan *Operational impact* orders them. Each draft cites this record at the sealed commit, written `<sealed>` below for the orchestrator to fill, and restates no figure its row holds.

#### D1

A reason comment for #1048, which then closes through `Closes #1048` in this work item's pull request body (`frame/design.md` *Grounding* G10).

> #1038's reading decides this issue: drop. The record is `seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-1.md` at `<sealed>`, *The decisions* row C7, *Instances C7* and *Command C7*.
>
> This issue proposes that the sealer read every `executed` and `seen red` claim against the implementing agent's transcript, because it re-runs a sample and leaves the rest on the crafter's word. The record holds no claim left on that word that a later round, a later work item or use found false, and #955's unsampled mutation claims are among those read. The sample's own catches stand in the pull requests' commits, each repaired before its merge, so the sample stays as `agents/sealer.md` step 3 states it, and the labels stay as `skills/verify/SKILL.md` *4. Each claim labelled executed, read or unverified* states them.
>
> The list of claims found false is a sample built from searches, and the row names its open part. A claim found false later reopens this question, with that row as its baseline.

Proposed home: `release: 0.27.2`, into which plan *Operational impact* step 4 moves it from `backlog: review chain & agents`, so the release check's `D \ M` reports nothing for it (`frame/design.md` *Grounding* G9).

Answers: C7.

#### D2

Title: `refactor: the behaviour suite is stated as the proof that a preload rewrite is not worse, and its record's only catch is a breakage of an agent's record that a check now reads at the hand-back; it narrows to a smoke run for gross breakage and judges no rewrite not worse`

Body:

> The measure is `seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-1.md` at `<sealed>`, *The decisions* row C8, *Instances C8* and *Command C8*.
>
> **What changes.** `evals/README.md` *The behaviour suite* opens: "A rewrite of an agent's preload is proved not worse by running this suite on the old tree and on the new one". The record does not bear that sentence out. The fail it shows as a defect was an agent's output broken in a way its shape graders read, and each fail on recall, the false-finding rate or tokens was read as variation and shipped. The suite narrows to a smoke run for gross breakage: the new side's shape and reach graders, read against a recorded baseline. Recall, the false-finding rate and the token figures are recorded and judge nothing, and the preload's bytes are read with no run.
>
> **What stays.** The cases under `evals/behaviour/`, which `check:` lines of shipped rules name, and the sentence that nothing in the tree makes a later edit owe a run.
>
> **Done when.** The section's lead and its pass rules state the smoke run. `evals/scripts/noninferiority.py#verdict` judges what the section states, and `tests/evals/test_noninferiority.py` pins it, each changed case seen red first. Every other sentence that calls the suite the proof of a rewrite is rewritten in place, found by a method the hand-back names, and a sentence of `docs/` among them changes through this work item's `## Rule changes`.
>
> **Out of scope.** Any paid run.

Proposed milestone: the minor milestone `frame/questions.md` Q1 names, by plan *Operational impact* step 2. Where no phase of this work item decides a `build`, step 1 creates no such milestone, and D2 goes to `backlog: review chain & agents`, whose description covers the agents that run the chain.

Answers: C8, and the question of #1038's comment of 2026-10-30.

### Phase-boundary run

`bin/test` is the repository's runner. Before `gaps.md` existed, `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview` failed on this work item (executed: 1 failed, 50 passed with the plan's other two modules). After it, with both new files staged so that `git ls-files` lists them, the phase-boundary set ran as one command:

```
bin/test -q -p no:xdist tests/behaviour/test_unverified_rows_close.py tests/behaviour/test_a_phase_hands_the_next_one_a_record.py "tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview" tests/test_censuses.py tests/behaviour/test_a_cited_section_stands_in_its_file.py
```

It exited 0 with 270 passed (executed). The first three are plan row 1's. The last two read every tracked file, so they read this phase's two files: the censuses read them, and the citation case leaves them out as records (`tests/censuses.py#RECORDS`). The phase changes prose alone, so no lint or format run reads it. `bin/seal unverified seal/threads/1793521558-the-record-decides-each-proposed-verifier` exited 0 and read `gaps.md` as 2 open and 0 closed (executed). S4's `git diff --name-only 813665f0..HEAD` lists this work item's directory alone; the hand-back gives its output at the closing commit.
