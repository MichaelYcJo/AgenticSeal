# Phase 2: 1793521558-the-record-decides-each-proposed-verifier

## What this phase found

This record decides C2, C11, C13 and C14 of `frame/design.md` *Scope* item 1. The tree is read at `813665f08eb48c63ae48dbdc17006491f3852410` (`813665f0`), the pull requests' own commits in a scratch clone with every `refs/pull/*/head` fetched on 2026-11-01, and the tracker on 2026-11-01. Each figure below is a figure at those moments unless its sentence names another. Each decision and the counts it stands on stand once, in the candidate's row of *The decisions*. The instances read one by one stand under *Instances*, and each command stands whole under *Commands*.

### Whether the frame holds

The frame holds, and the build follows it except where this list says. Each item is a departure or a reading the frame left open, with its grounds.

- **The pull requests' commits are read the way phase 1 read them.** C2, C11 and C14 read round records, merges and `target:` lines on each work item's branch, and most of those branches were settled away before `813665f0`. *Command C2* clones the worktree under the scratch directory, fetches `refs/pull/*/head` there, and reads each pull request's head, the method `trail/phases/phase-1.md` *Command C7* (b) used. The worktree was not written.
- **The window is the merged pull requests, bounded by two merges.** "Since 0.22.4" (C2) is read as the work-item pull requests merged after #1050, which shipped the merge route at `5daa931f` (PR #1050, merged 2026-10-27T02:18:01Z), through #1244, the last one merged into `release/v0.27.1` before `813665f0`. The pull requests that only settle a release or gather its fragments are left out, since they carry no work item's rounds. C14 reads the same window, as the next item says.
- **C14's window is narrower than its question.** *Scope* item 2 asks for findings "since the review axes became a floor". The sentence *The table is a floor, not a ceiling* stands in the repository's first commit, `716d8548` of 2026-08-31, so the question covers the whole history. *Command C14* reads C2's window of 57 pull requests, where the round records hold `target:`, `location:`, `regression:` and `reopens:` lines one script reads. Between `v0.22.4` and `813665f0` the axes table kept its ten rows, and two of its cells changed only the word `spec` (`git diff v0.22.4 813665f0 -- skills/code-review/SKILL.md`, executed). The rounds before the window are the open part, and the row says so.
- **"Lines an earlier round of the same work item read" is read as lines the branch had written by round 1's target.** No round record lists the lines it read. Round 1 reviews the branch's diff against its base, so a line the branch wrote by round 1's target, unchanged at round N's target, is a line round 1 had in front of it. Lines a fix wrote after round 1 and a later round read, and lines the branch never changed, are the open part of *Command C14*.
- **C11's "since #1148 shipped in 0.25.1" is read as the work items merged after #1148's own pull request.** #1148 merged as PR #1191 at 2026-10-30T21:52:18Z. Its own work item, `1793343707-each-document-serves-one-reader`, was framed and reviewed before its rules stood, so *Command C11* leaves it out. Its rounds hold 5 recurring findings of 14.
- **C11's split is by location, where #1020's 0.24.0 split was read one by one.** #1020's comment of 2026-10-29 sorted 0.24.0's 17 recurring findings "by where the defect stood". *Command C11* sorts each recurring finding by its `location:` paths: "records alone" where every path stands under the work item's directory, and "shipped text" where any path stands outside it. A finding located in a record and in a shipped file counts as shipped text, as #1020's comment counted its "4 reached shipped files as well as records". The two methods agree on that edge and are not otherwise the same method.
- **C2's decided-by sentence does not decide C2 literally.** *Scope* item 2 gives C2 "drop where the merge route cost nothing measurable". The route cost two verifying rounds in one work item (*Instances C2*), which is measurable. The row decides C2 under G1 and G14, and its *Grounds* cell gives the weighing.
- **Two merges took no verifying round that the merge route owed them.** The frame does not ask about this, and the record shows it. Of the three merges that resolved a conflict in a file outside the records, #1136's `2106d2e9` and #1202's `a8563a34` are their pull requests' heads. No round, broad run or sealer followed either merge, although `skills/code-review/orchestration.md` *A conflict with the base is integrated by merging the base into the branch, never by a rebase.* stood at `v0.22.4`, `v0.23.1` and `v0.25.1` (*Command C2*). `skills/implement/acts.md:75` at `813665f0` states the limit: "nothing gives a merge that resolved a conflict outside the records its verifying round, because the chain check reads no merge commit". CI passed on both pull requests (read: `gh pr checks 1136`, `gh pr checks 1202`). Each resolution keeps both sides' newer text (*Instances C2*), so no defect stands on either. Plan row A2 drafts a repair rather than making it, and *Scope* item 3 drafts an act only for a candidate's decision. So no draft is written, and `gaps.md` *Not done* names this.
- **No question of C2, C11, C13 or C14 waits on a paid run, and no row of `seal/follow-up.md` is this phase's.** Each is decided on the record. The two rows G12 names are C9's and C4's, which phase 3 decides (read).

### The decisions

| Candidate | Command or coordinate | What the record shows | Decision | Grounds | Act |
|---|---|---|---|---|---|
| C2 a verdict kept across a rebase where `git patch-id` shows the same patch | *Command C2*, executed at `813665f0` in a scratch clone with every `refs/pull/*/head` fetched, and on the tracker 2026-11-01. Whole for the 57 work-item pull requests merged from #1050 to #1244; a pull request outside that window is the open part | 12 merges of the base on 11 branches. 11 came after a review round, on 10 branches. 3 resolved a conflict in a file outside the records. One of the 3, #1159's `b9820880`, took its verifying round: round 5 read the merge and found one `should` the merge base already held, and round 6 verified its fix, about 14 minutes from the merge to the seal by the commit times. #1160's round 3 read its merge with round 2's fixes, so the merge added no round there. The other 2, #1136's and #1202's, took no round at all, as *Whether the frame holds* says. The 187 round records of the window name 447 commits on their `target:` lines, and every one is an ancestor of its pull request's head. No pull request created since 2026-10-26 was force-pushed. The repository's six force pushes stand on #558, #937 and #939, before the window (*Instances C2*) | drop | G1 and G14. A patch-id verdict is kept only where a rebased commit's patch is unchanged. The one merge that cost rounds resolved a conflict, which changes the patch of the commit that carries the resolution, so a rebase would have owed the same round. A rebase also moves HEAD, so the broad run and the sealer run again either way, by `skills/core/SKILL.md`'s invariant "No seal without the broad run at HEAD". Plan row A8 weighs the never-rebase rule for removal. The premise that keeps it holds at `813665f0`: the records arm of `skills/code-review/scripts/chain_check.py` requires HEAD to descend from the last record's commit, which a rewritten branch breaks. The rule costs no run, and #1038's body keeps it either way | none |
| C11 a check that reads recurrence across review rounds, or the mediated exchange at a finding's first `reopens:` | *Command C11*, executed at `813665f0` in the same clone. Whole for the 17 work items merged after #1191 through #1244 | 111 findings in those work items' rounds, 30 of them recurring, in 9 work items. 10 stand in the records alone and 20 reach shipped text, where #1020's comment of 2026-10-29 counted 12 and 5 of 0.24.0's 17. Four chains of three or more findings stand in shipped text, each on one rule or one function: #1201 on rule 12's wording, #1203 on the commit prefix rule, #1230 on how a generator answers a `--case` name, and #1241 on how a path walk reads `..`. #1230's fourth instance was deferred and reached a later work item: #1228, built as #1242. #1241's mechanism question was filed as #1240. In three of the four chains the orchestrator's judgments of the run took the structural question. #1201's plan holds no such section, and its chain ran four rounds (*Instances C11*) | build | #1020's comment of 2026-10-30, the decided-by sentence *Scope* item 2 gives C11: "where the records-alone count falls and recurrences remain in shipped text, the exchange is the case to make". The records-alone share fell, and recurrences in shipped text remain. G1: the instances that went on past one round, #1230's fourth among them, are what the candidate would have stopped and the verification the tree has did not. Plan row A8 weighs the existing judgment of the run as the alternative. It took the question in three of four chains, so whether the exchange or the check adds anything to it is #1020's frame to weigh, with these instances as its baseline | comment D3 on #1020 |
| C13 a check of a session's procedure rather than its commits | *Command C13*, executed at `813665f0` and on the tracker 2026-11-01. Whole for #27's seven rows | Every row has a catcher at `813665f0`. Three hooks watch the session, not a commit: `hooks/routing-edit-gate.py` refuses the first edit before the routing answer (rows 2 and 6), `hooks/question-gate.py` refuses a question under `Automation` `yes` (row 2), and `hooks/implementer-notice.py` says one line after a commit where the declared crafter left no mark (row 3). The pull request's routing trailer arm, `chain_check.py#routing_trailers`, reads row 6 again. The agent that reads the rule catches the rest: contract rules 2 and 3 for a prompt that widens the scope (row 1), rule 5 for a coordinate that does not land (row 4), `skills/commit-pr-convention/SKILL.md` *First, check the title against the history* for a title's prefix (row 5), and rule 12 for a shallow search (row 7). Rows 4, 5 and 7 are readings of meaning that no gate can make (*Instances C13*) | drop | *Scope* item 2 for C13: "drop where every row has a catcher or is a reading no gate can make; #27 closes on a drop". `skills/core/SKILL.md` *The first value*: "Whether two things mean the same or give the same result is the judgment the workflow delegates", and a script answers only what it reads exactly. The premise #27 stands on, "Every gate this plugin ships watches a commit", is stale, as #27's comment of 2026-10-31 says | close #27 with D4 |
| C14 a separate perspective pass in the review | *Command C14*, executed at `813665f0` in the same clone, and on the tracker 2026-11-01. Whole for the condition it states over C2's window. The rounds before that window, lines a fix wrote after round 1, lines the branch never changed, and findings located in the records are the open part, so the leak count is a `sample` of #6's question | 137 findings in rounds after the first. 5 carry no `regression:` or `reopens:` line and name lines outside the records that the branch wrote by round 1's target and that nothing changed after. One of the 5, #1140's round 2 finding 1, became wrong through a commit after round 1, so it is no miss. Of the other 4, three are of kinds the axes table names, *Inputs* and *Exclusions & boundaries*: two YAML spellings in #1171 and a link loop in #1241. One is of a kind no axis names: #1203's rule sentence a reader could read two ways. `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* names that kind, and the proofer reads by it. The sealer's withheld verdicts name records, the pull request body and claims (`trail/phases/phase-1.md` *Instances C7*), not a kind of code. The three issues labelled `bug` since 2026-10-27 are of kinds the table names, or concern CI (*Instances C14*) | drop | #6's own test: "Run three review rounds under the floor rule. If axes keep leaking, the pass has earned its place." The window held far more than three rounds, and one miss in 137 later findings is of a kind the table leaves out, which another rule the proofer reads names. Plan row A8 weighs the axes floor for removal. Its premise holds: the table names the kinds of three of the four misses, so the table is not what let them through, and the floor costs a paragraph and no run. #6's second question left with `skills/security-audit/SKILL.md`, removed at `e391ea04` (#1099), as #6's comment of 2026-10-31 says | close #6 with D5 |

### Commands

Each command runs from an empty scratch directory with `W` set to this worktree's path, unless its heading says otherwise. A pull request merged after #1245 would add rows, so each window closes at `2026-11-01T09:19:59Z`, #1245's merge.

#### Command C2

Executed on 2026-11-01. The clone and the list of merged pull requests serve *Command C11* and *Command C14* too:

```
git clone -q --no-local "$W" clone-p2
git -C clone-p2 remote set-url origin https://github.com/MichaelYcJo/AgenticSeal.git
git -C clone-p2 fetch -q origin '+refs/pull/*/head:refs/pull/*/head'
gh pr list --repo MichaelYcJo/AgenticSeal --state merged --limit 300 --search 'merged:>=2026-10-27' \
  --json number,headRefName,baseRefName,headRefOid,mergeCommit,mergedAt > prs.json
python3 -I - prs.json clone-p2 <<'EOF'
import json, re, subprocess, sys

prs_file, clone = sys.argv[1], sys.argv[2]

def run(*a):
    return subprocess.run(["git", "-C", clone, *a], capture_output=True, text=True)

def git(*a):
    return run(*a).stdout

prs = [p for p in json.load(open(prs_file))
       if p["mergedAt"] > "2026-10-27T02:18:01Z" and p["mergedAt"] <= "2026-11-01T09:19:59Z" and p["baseRefName"] != "main"
       and not p["headRefName"].startswith(("chore/settle", "chore/the-fragments"))]
merges_total = after_round = outside = names = orphaned = records = 0
for p in sorted(prs, key=lambda p: p["mergedAt"]):
    head = p["headRefOid"]
    base = git("rev-parse", p["mergeCommit"]["oid"] + "^1").strip()
    added = git("diff", "--name-only", "--diff-filter=A", f"{base}...{head}", "--", "seal/").split()
    items = sorted({"/".join(x.split("/")[:3]) for x in added if x.endswith("/routing.md")})
    def rounds_at(c):
        return [x for it in items for x in git("ls-tree", "-r", "--name-only", c, "--", it).split()
                if re.search(r"/rounds/round-\d+\.md$", x)]
    rounds = rounds_at(head)
    for r in rounds:
        records += 1
        for line in re.findall(r"^target: (.*)$", git("show", f"{head}:{r}"), re.M):
            for sha in re.findall(r"\b[0-9a-f]{7,40}\b", line):
                names += 1
                if run("merge-base", "--is-ancestor", sha, head).returncode:
                    orphaned += 1
                    print("orphaned:", p["number"], r, sha)
    for m in git("rev-list", "--merges", "--first-parent", head, "^" + base).split():
        merges_total += 1
        before = rounds_at(m + "^1")
        after_round += bool(before)
        resolved = [f for f in git("show", "--remerge-diff", "--format=", "--name-only", m).split() if not f.startswith("seal/")]
        outside += bool(resolved)
        print(f"#{p['number']} merge {m[:8]}: {len(before)} of {len(rounds)} rounds before it; "
              f"resolved outside the records: {resolved or 'none'}")
print(f"{len(prs)} work-item pull requests; {merges_total} merges of the base, {after_round} after a round, "
      f"{outside} resolving a file outside the records; {records} round records name {names} commits "
      f"on target: lines, {orphaned} not an ancestor of the pull request's head")
EOF
gh api graphql --paginate -f query='query($endCursor:String){repository(owner:"MichaelYcJo",name:"AgenticSeal"){pullRequests(first:50,after:$endCursor){pageInfo{hasNextPage endCursor} nodes{number createdAt timelineItems(first:20,itemTypes:[HEAD_REF_FORCE_PUSHED_EVENT]){nodes{... on HeadRefForcePushedEvent{createdAt}}}}}}}' \
  --jq '.data.repository.pullRequests.nodes[]|select(.createdAt<="2026-11-01T09:19:59Z")|"\(.number) \(.createdAt[:10]) \(.timelineItems.nodes|length)"' |
  awk '$3>0{print "force-pushed:",$0; s+=$3} $2>="2026-10-26"{w++; ws+=$3} {n++} END{print n" PRs, "s+0" force pushes; "w" created since 2026-10-26, "ws+0" force pushes"}'
for t in v0.22.4 v0.23.1 v0.25.1; do git -C clone-p2 grep -c 'verifying round on that resolution' "$t" -- skills/code-review/orchestration.md; done
git -C clone-p2 show 813665f0:skills/implement/acts.md | sed -n 75p | grep -o 'nothing gives a merge[^,]*, because the chain check reads no merge commit'
```

It printed:

```
#1057 merge 95fa9fb7: 0 of 3 rounds before it; resolved outside the records: none
#1119 merge 8f9bff17: 3 of 4 rounds before it; resolved outside the records: none
#1131 merge 731df38a: 2 of 2 rounds before it; resolved outside the records: none
#1136 merge 2106d2e9: 4 of 4 rounds before it; resolved outside the records: ['tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py']
#1137 merge aa8b54cb: 4 of 8 rounds before it; resolved outside the records: none
#1140 merge 9477538d: 7 of 9 rounds before it; resolved outside the records: none
#1159 merge b9820880: 4 of 6 rounds before it; resolved outside the records: ['evals/scripts/rule_cases.py']
#1160 merge 6dbce088: 2 of 4 rounds before it; resolved outside the records: none
#1202 merge a8563a34: 11 of 11 rounds before it; resolved outside the records: ['skills/implement/acts.md']
#1203 merge a74827e8: 5 of 5 rounds before it; resolved outside the records: none
#1211 merge dfb49c8c: 2 of 5 rounds before it; resolved outside the records: none
#1211 merge 1a7d3ae3: 1 of 5 rounds before it; resolved outside the records: none
57 work-item pull requests; 12 merges of the base, 11 after a round, 3 resolving a file outside the records; 187 round records name 447 commits on target: lines, 0 not an ancestor of the pull request's head
force-pushed: 558 2026-09-24 1
force-pushed: 937 2026-10-13 2
force-pushed: 939 2026-10-13 3
306 PRs, 6 force pushes; 82 created since 2026-10-26, 0 force pushes
v0.22.4:skills/code-review/orchestration.md:1
v0.23.1:skills/code-review/orchestration.md:1
v0.25.1:skills/code-review/orchestration.md:1
nothing gives a merge that resolved a conflict outside the records its verifying round, because the chain check reads no merge commit
```

#1057's work item keeps its rounds under `seal/specs/<item>/rounds/`, the layout before `trail/`, so each script reads a round record under either `rounds/` or `trail/rounds/`. Its merge came before its first round. Five pull requests of the window, #1100, #1112, #1168, #1169 and #1172, add no `routing.md` and hold no round. The `timelineItems` query lists the nodes, because its `totalCount` counts every item of the timeline and not only the filtered type. It counts the pull requests created by #1245's merge, so a pull request opened later changes no figure. The commits after each merge were listed with `git -C clone-p2 log --first-parent --reverse --format='%h %cI %s' <merge>..refs/pull/<n>/head`, and *Instances C2* reads them.

#### Command C11

Executed on 2026-11-01, in the scratch directory of *Command C2*:

```
python3 -I - prs.json clone-p2 <<'EOF'
import json, re, subprocess, sys

prs_file, clone = sys.argv[1], sys.argv[2]

def git(*a):
    return subprocess.run(["git", "-C", clone, *a], capture_output=True, text=True).stdout

prs = [p for p in json.load(open(prs_file))
       if p["mergedAt"] > "2026-10-30T21:52:59Z" and p["mergedAt"] <= "2026-11-01T09:19:59Z" and p["baseRefName"] != "main"
       and not p["headRefName"].startswith(("chore/settle", "chore/the-fragments"))]
findings = recurring = alone = 0
for p in sorted(prs, key=lambda p: p["mergedAt"]):
    head = p["headRefOid"]
    base = git("rev-parse", p["mergeCommit"]["oid"] + "^1").strip()
    added = git("diff", "--name-only", "--diff-filter=A", f"{base}...{head}", "--", "seal/").split()
    for it in sorted({"/".join(x.split("/")[:3]) for x in added if x.endswith("/routing.md")}):
        rounds = [x for x in git("ls-tree", "-r", "--name-only", head, "--", it).split()
                  if re.search(r"/rounds/round-\d+\.md$", x)]
        found = []
        for r in sorted(rounds, key=lambda x: int(re.search(r"round-(\d+)", x).group(1))):
            text = git("show", f"{head}:{r}")
            parts = re.split(r"^## Findings\s*$", text, flags=re.M)
            body = re.split(r"^## ", parts[1], flags=re.M)[0] if len(parts) > 1 else ""
            for sec in re.split(r"^### ", body, flags=re.M)[1:]:
                findings += 1
                refs = re.findall(r"^(regression|reopens): (\S+)", sec, re.M)
                if not refs:
                    continue
                locs = " ".join(re.findall(r"^location: (.*)$", sec, re.M))
                paths = [x.split(":")[0] for x in re.findall(r"`([^`]+)`", locs)]
                records_alone = all(x.startswith(it + "/") for x in paths)
                recurring += 1
                alone += records_alone
                n = re.search(r"round-(\d+)", r).group(1)
                found.append(f"  round-{n}#{sec.split('.', 1)[0]} {' '.join(':'.join(x) for x in refs)} "
                             f"{'records alone' if records_alone else 'shipped text'}")
        print(f"#{p['number']} {it.split('/')[-1]}: {len(rounds)} rounds, {len(found)} recurring")
        print("\n".join(found)) if found else None
print(f"{findings} findings, {recurring} recurring: {alone} in the records alone, {recurring - alone} reaching shipped text")
EOF
```

It printed:

```
#1193 1793401152-the-seal-draws-a-round-headed-little-owl: 2 rounds, 0 recurring
#1196 1793408293-less-text-means-nothing-said-twice: 2 rounds, 0 recurring
#1201 1793419351-project-rules-live-in-the-repository: 5 rounds, 4 recurring
  round-2#1 regression:round-1#3 shipped text
  round-2#2 regression:round-1#3 shipped text
  round-3#1 reopens:round-2#2 shipped text
  round-4#1 regression:round-2#1 shipped text
#1202 1793411151-judgment-where-meaning-is-the-question: 11 rounds, 2 recurring
  round-4#1 regression:round-3#1 shipped text
  round-10#1 regression:round-9#2 shipped text
#1203 1793419350-a-prefix-states-what-a-change-is: 5 rounds, 8 recurring
  round-2#1 reopens:round-1#1 shipped text
  round-2#2 regression:round-1#2 shipped text
  round-2#3 regression:round-1#1 records alone
  round-3#1 reopens:round-2#3 shipped text
  round-3#2 reopens:round-2#1 shipped text
  round-4#1 reopens:round-3#1 shipped text
  round-5#1 reopens:round-4#1 records alone
  round-5#2 regression:round-4#3 records alone
#1206 1793432602-a-feat-moves-to-the-minor-of-its-goal: 1 rounds, 0 recurring
#1209 1793438028-pre-0-23-upgrade-readings-removed: 2 rounds, 0 recurring
#1210 1793443708-settle-keeps-a-gaps-file-anywhere: 3 rounds, 1 recurring
  round-2#1 reopens:round-1#2 shipped text
#1211 1793437163-fields-stand-in-marked-blocks: 5 rounds, 1 recurring
  round-2#1 reopens:round-1#2 shipped text
#1226 1793457437-readers-state-the-shapes-they-pass: 2 rounds, 0 recurring
#1230 1793457435-replay-targets-reads-both-layouts: 5 rounds, 3 recurring
  round-2#1 regression:round-1#1 shipped text
  round-3#1 reopens:round-2#1 shipped text
  round-4#1 regression:round-3#1 shipped text
#1227 1793457436-row-deletion-check-and-a-symlink: 3 rounds, 0 recurring
#1237 1793490088-each-kind-of-restatement-is-measured: 4 rounds, 5 recurring
  round-2#1 regression:round-1#5 records alone
  round-2#2 reopens:round-1#5 records alone
  round-3#5 reopens:round-2#3 records alone
  round-4#1 regression:round-3#2 records alone
  round-4#2 regression:round-3#1 records alone
#1239 1793504230-replay-keeps-rounds-on-a-deleted-base: 2 rounds, 0 recurring
#1241 1793504229-a-linked-memo-named-as-the-argument: 7 rounds, 4 recurring
  round-2#1 regression:round-1 shipped text
  round-3#1 regression:round-2#1 shipped text
  round-3#2 regression:round-2#1 shipped text
  round-6#1 regression:round-1#1 shipped text
#1242 1793513786-an-unanswered-case-name-is-named-once: 1 rounds, 0 recurring
#1244 1793516191-a-wording-pin-module-leaves-by-rule-changes: 2 rounds, 2 recurring
  round-2#1 regression:round-1#2 records alone
  round-2#2 regression:round-1#5 records alone
111 findings, 30 recurring: 10 in the records alone, 20 reaching shipped text
```

The judgments of the run were read with `git -C clone-p2 show "refs/pull/<n>/head:seal/threads/<item>/frame/plan.md" | sed -n '/^## Judgments of the run/,$p'` for #1201, #1202, #1203, #1230, #1237 and #1241, and the deferral with `gh issue view 1228 --json body` and `gh issue view 1240 --json title,state,milestone`.

#### Command C13

Executed at `813665f0` and on the tracker, 2026-11-01, from the root of a worktree of this branch:

```
gh issue view 27 --json body,comments
git show 813665f0:hooks/dispatch.py | grep -n -E '"pre-question"|"pre-edit"|"post-bash"'
git grep -n -E '^## (2|3|5|12) ' 813665f0 -- skills/agent-contract/SKILL.md
git grep -n -E 'Once the batch is answered|^## First, check the title' 813665f0 -- skills/implement/SKILL.md skills/commit-pr-convention/SKILL.md
git grep -n -F 'hooks/implementer-notice.py' 813665f0 -- skills/implement/orchestration.md
git grep -n -E '^def routing_trailers' 813665f0 -- skills/code-review/scripts/chain_check.py
```

It printed #27's body and its two comments, then:

```
84:    "pre-question": ("question-gate.py",),
87:    "pre-edit": ("routing-edit-gate.py",),
88:    "post-bash": ("implementer-notice.py",),
813665f0:skills/agent-contract/SKILL.md:36:## 2 Narrow and often; the broad gate is the orchestrator's
813665f0:skills/agent-contract/SKILL.md:50:## 3 A spawn prompt cannot widen the verification scope
813665f0:skills/agent-contract/SKILL.md:71:## 5 Nothing that reaches you in prose is evidence
813665f0:skills/agent-contract/SKILL.md:157:## 12 A defect belongs to a class, so enumerate the class
813665f0:skills/commit-pr-convention/SKILL.md:27:## First, check the title against the history
813665f0:skills/implement/SKILL.md:211:**Once the batch is answered, the session runs to the pull request.** What
813665f0:skills/implement/orchestration.md:257:`hooks/implementer-notice.py` says one line after a commit when a declared
813665f0:skills/code-review/scripts/chain_check.py:1516:def routing_trailers(root, base):
```

#### Command C14

Executed on 2026-11-01, in the scratch directory of *Command C2*:

```
python3 -I - prs.json clone-p2 <<'EOF'
import json, re, subprocess, sys

prs_file, clone = sys.argv[1], sys.argv[2]

def run(*a):
    return subprocess.run(["git", "-C", clone, *a], capture_output=True, text=True)

def git(*a):
    return run(*a).stdout

prs = [p for p in json.load(open(prs_file))
       if p["mergedAt"] > "2026-10-27T02:18:01Z" and p["mergedAt"] <= "2026-11-01T09:19:59Z" and p["baseRefName"] != "main"
       and not p["headRefName"].startswith(("chore/settle", "chore/the-fragments"))]
later = hit = 0
for p in sorted(prs, key=lambda p: p["mergedAt"]):
    head = p["headRefOid"]
    base = git("rev-parse", p["mergeCommit"]["oid"] + "^1").strip()
    added = git("diff", "--name-only", "--diff-filter=A", f"{base}...{head}", "--", "seal/").split()
    for it in sorted({"/".join(x.split("/")[:3]) for x in added if x.endswith("/routing.md")}):
        rounds = {int(re.search(r"round-(\d+)", x).group(1)): x
                  for x in git("ls-tree", "-r", "--name-only", head, "--", it).split()
                  if re.search(r"/rounds/round-\d+\.md$", x)}
        if 1 not in rounds:
            continue
        def target(k):
            return re.search(r"^target: ([0-9a-f]{7,40})", git("show", f"{head}:{rounds[k]}"), re.M).group(1)
        t1 = target(1)
        branch_at_1 = set(git("rev-list", f"{git('merge-base', t1, base).strip()}..{t1}").split())
        for k in sorted(rounds)[1:]:
            tk = target(k)
            parts = re.split(r"^## Findings\s*$", git("show", f"{head}:{rounds[k]}"), flags=re.M)
            body = re.split(r"^## ", parts[1], flags=re.M)[0] if len(parts) > 1 else ""
            for sec in re.split(r"^### ", body, flags=re.M)[1:]:
                later += 1
                if re.search(r"^(regression|reopens): ", sec, re.M):
                    continue
                read_at_1 = []
                for loc in re.findall(r"`([^`]+:\d+(?:-\d+)?)`", " ".join(re.findall(r"^location: (.*)$", sec, re.M))):
                    path, lines = loc.rsplit(":", 1)
                    if path.startswith(it + "/"):
                        continue
                    a, _, b = lines.partition("-")
                    blame = run("blame", "-s", "-l", "-L", f"{a},{b or a}", tk, "--", path)
                    shas = {x.split()[0].lstrip("^") for x in blame.stdout.splitlines() if x.strip()}
                    if blame.returncode == 0 and shas and shas <= branch_at_1:
                        read_at_1.append(loc)
                if read_at_1:
                    hit += 1
                    print(f"#{p['number']} round-{k}#{sec.split('.', 1)[0]} {read_at_1} | {sec.splitlines()[0][3:110]}")
print(f"{later} findings in rounds after the first; {hit} carry no regression: or reopens: line and name lines "
      f"outside the records that the branch wrote by round 1's target and no commit changed after")
EOF
git -C clone-p2 merge-base --is-ancestor d60ca012 9f193554; echo $?
gh issue list --repo MichaelYcJo/AgenticSeal --state all --limit 100 --search 'label:bug created:2026-10-27..2026-11-01' --json number,title --jq '.[]|"\(.number) \(.title[:90])"'
git -C clone-p2 log -1 --format='%h %s' e391ea04 | cut -c1-90
git -C clone-p2 show --format= --numstat e391ea04 -- skills/security-audit/SKILL.md
```

It printed:

```
#1140 round-2#1 ['.github/scripts/publish_release_note.py:19-21'] | Six sentences still say the note reads every fragment the range added, and since `d60ca012` the reader skip
#1171 round-3#1 ['skills/verify/scripts/deferral_check.py:94'] | A colon with text glued to it is read as a key, so one event name GitHub runs nothing on answers a deferral
#1171 round-5#5 ['tests/skills/test_deferral_check.py:126-151'] | `splitlines()` breaks a line where YAML does not, so a comment's text is read as the trigger and a push-onl
#1203 round-3#5 ['skills/commit-pr-convention/SKILL.md:144-145'] | The test between `feat:` and `fix:` does not say which base a commit on a work item's branch opens, and thi
#1241 round-4#2 ['tests/skills/test_unverified_check.py:2527'] | A named link loop is kept as named, so the scan reads nothing under it, and the base's memo under its real 
137 findings in rounds after the first; 5 carry no regression: or reopens: line and name lines outside the records that the branch wrote by round 1's target and no commit changed after
1
1187 chore: a hung macOS pytest shard is cancelled at the job's 15-minute timeout with no log, 
1185 fix: seal payload follows an @ line inside a fenced code block, which Claude Code does not
1184 fix: /agentic:update reads ~/.claude where CLAUDE_CONFIG_DIR moves the plugins and the CLA
e391ea04b chore: templates/, hooks/ and tests/ each held two kinds of file in one level; e
0	85	skills/security-audit/SKILL.md
```

The `1` is `merge-base --is-ancestor`'s exit code: `d60ca012`, the commit #1140's finding names, is not an ancestor of round 1's target `9f193554`. Each finding's close was read with `git -C clone-p2 show refs/pull/<n>/head:<round record>`, and the axes table with `git show 813665f0:skills/code-review/SKILL.md | sed -n '/^## Comparison axes/,/^## Probes/p'`.

### Instances

#### Instances C2

The three merges that resolved a conflict outside the records, read with `git -C clone-p2 show --remerge-diff <merge> -- ':!seal/'`:

- **#1136's `2106d2e9`** (work item `1793174170-two-facts-kept-in-several-files-have-drifted`), in `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`'s `APPLIES_THE_SHARED_GUARD`. The resolution keeps the base's entry for #1043's `citations` and the branch's entry for #1055's `pairs`, and drops `#967`'s `cited_files` entry, which #1135 had removed on the base. The merge is the pull request's head. `trail/gate.md` names `9e34e9e5`, and `guarantee.md` reads `Verdict: sealed` at `7e57c7fd`, both before the merge.
- **#1159's `b9820880`** (work item `1793240966-the-framer-has-no-read-only-probe`), in `evals/scripts/rule_cases.py`'s docstring. The resolution keeps #1091's crafter lines and the branch's "five issues". Round 5 (`target: b9820880, fixes bd7ad2db..b9820880`) opens "This round verifies the merge `b9820880`". It confirmed the resolution and opened one `should` on the sealer paragraph's count, which the merge base `1e82fd0a` already read. Round 6 verified the fix `51859196`. The broad run and the sealer followed: the merge's commit time is 13:10:28 and the sealed verdict's `2b0baa48` 13:24:05 on 2026-10-29.
- **#1202's `a8563a34`** (work item `1793411151-judgment-where-meaning-is-the-question`), in three rows of `skills/implement/acts.md`. The resolution keeps the branch's two rows on the verifying round and the regression route, which name `frame/plan.md` *Judgments of the run*, and the base's row on the pull request's opening, which names `state` and `mergeable`. Each kept row is the newer text of its side. The merge is the pull request's head. `trail/gate.md` names `dae46f8d`, before the merge.

The eight other merges after a round resolved nothing outside the records. #1119, #1131 and #1203 then ran the broad gate and the sealer again, which a rebase would also have owed. #1137's merge preceded a reframe and round 5 targets it. #1140's preceded a phase 6. #1160's round 3 (`target: 6dbce088, fixes a3255131..6dbce088`) read round 2's fixes with the merge. #1211's two merges were followed by rounds 2 to 5.

The six force pushes outside the window stand on #558 (2026-09-24) and on #937 and #939 (2026-10-13). They are outside C2's question and were not read further.

#### Instances C11

The four chains of three or more findings that stand in shipped text, each read at its pull request's head:

- **#1201** (`1793419351-project-rules-live-in-the-repository`). `round-1#3` is followed by `round-2#1` and `round-2#2`, then `round-3#1` and `round-4#1`, all on the wording of contract rule 12 and the statements of it in `agents/crafter.md` and `skills/code-review/orchestration.md`. The first `reopens:` stands at round 3. The plan holds no `## Judgments of the run` section, so no judgment of the run is recorded.
- **#1203** (`1793419350-a-prefix-states-what-a-change-is`). `round-1#1` is followed by `round-2#1` and `round-2#3`, then `round-3#1`, `round-3#2`, `round-4#1` and `round-5#1`, on which prefix `skills/commit-pr-convention/SKILL.md` gives each kind of change. The first `reopens:` stands at round 2. The judgments route round 2's and round 3's findings to the framer, which reframed *Scope* item 1 twice (`fec2a3cc`, `ee035d00`).
- **#1230** (`1793457435-replay-targets-reads-both-layouts`). `round-1#1` is followed by `round-2#1`, `round-3#1` and `round-4#1`, on how `seed_defects.py` and `replay_targets.py` answer a `--case` name. The first `reopens:` stands at round 3. The judgment after round 3 says the run "goes on for one fix pass and one verifying round, and stops there". Round 4's finding reads `deferred #1228`, whose body says it was deferred "because it was the fourth finding in that run on how a generator answers a `--case` name". #1228 was built as PR #1242, whose one round opened nothing.
- **#1241** (`1793504229-a-linked-memo-named-as-the-argument`). Round 1 is followed by `round-2#1`, then `round-3#1` and `round-3#2`, and `round-1#1` by `round-6#1`, on how `unverified_check.py#absolute` reads `..` and links. Every link is a `regression:` line, so no `reopens:` stands. The judgments rewrite the `..` reading twice and file "the mechanism round 3 named" as #1240, open in `backlog: gates & hooks`.

The other recurring findings form chains of two: #1202's two regressions, #1210's and #1211's single reopenings, and #1203's `round-1#2` with `round-2#2`. The records-alone chain is #1237's, where the judgments sent the frame back to the framer after round 2 and stopped the run after round 4. #1244's two are each a single regression in the frame.

#### Instances C13

#27's seven rows, each with its catcher at `813665f0`:

| # | #27's row | Catcher at `813665f0` | Kind |
|---|---|---|---|
| 1 | a prompt ordered the full suite three times | contract rule 2 keeps the broad gate the orchestrator's, and rule 3 has the agent decline a prompt that widens the scope and name it in the hand-back, `check: none reader: the orchestrator at each hand-back`. #27's comment of 2026-08-31 moved this row to legacy `SpecSeal#29` | the agent that reads the rule |
| 2 | routing at the start, the reviewer in the middle, the pull request at the end | `hooks/routing-edit-gate.py` refuses the first edit before the routing answer, and `hooks/question-gate.py` refuses the question tool under `Automation` `yes`. Under another routing, `skills/implement/SKILL.md` *Once the batch is answered, the session runs to the pull request* is read by the orchestrator, since whether a later decision needs a person is a judgment | a gate where the fact is exact; otherwise a reading |
| 3 | the session implemented a work item itself | `hooks/implementer-notice.py`, registered `post-bash`, says one line after a commit where the declaration names the crafter and no crafter's mark stands (`skills/implement/orchestration.md:257`) | a hook, by path |
| 4 | five coordinates written, five wrong | contract rule 5: a fact with a coordinate is opened before it is built on; the proofer's `evidence:` line and the sealer's step 3 open them. The ledger the row names is gone from the tree | the agent that reads the rule; a reading |
| 5 | a pull request title with no prefix | `skills/commit-pr-convention/SKILL.md` *First, check the title against the history*, read by the orchestrator. `.github/scripts/release_completeness_check.py` reads one prefix, a `feat:` in a patch, and no other | the agent that reads the rule; which prefix fits is a reading of meaning |
| 6 | the declaration batched into a Bash call with a commit, so it was never created | `hooks/routing-edit-gate.py` refuses the first edit while no declaration names the branch, and `chain_check.py#routing_trailers` reads the routing at the pull request | a gate, by path |
| 7 | two claims from shallow greps | contract rule 12: a list names its method and calls a sample a sample, `check: none reader: the proofer at review`; and rule 5 | the agent that reads the rule; depth is a reading no gate can make |

#27's three checkboxes are answered by this table. The plugin gates a session's procedure where it reads a fact exactly, as rows 2, 3 and 6 show. The rest is caught by the agent that reads the rule. No row is caught by nobody.

#### Instances C14

The five findings of *Command C14*, each judged against the axes table at `813665f0`:

- **#1140 round 2 finding 1** (`.github/scripts/publish_release_note.py:19-21`). The six sentences were true at round 1's target. `d60ca012`, which made the reader skip a fragment, came after round 1's target, so the finding is a sentence a later change left stale, not a miss of round 1.
- **#1171 round 3 finding 1** (`skills/verify/scripts/deferral_check.py:94`). A colon glued to text is read as a key. Its kind is *Inputs* ("accepted ranges") and *Exclusions & boundaries*. It was fixed at `e8dc9313`.
- **#1171 round 5 finding 5** (`tests/skills/test_deferral_check.py:126-151`). `splitlines()` breaks a line where YAML does not. Its kind is *Inputs*. Its close reads `deferred #1167`: "the hand-written reader does not converge", which is a mechanism question and not an axis left out.
- **#1203 round 3 finding 5** (`skills/commit-pr-convention/SKILL.md:144-145`). The test between `feat:` and `fix:` does not say which base a commit opens. No axis of the table names a rule sentence with two readings. `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* names it. The close says phase 3's rewrite absorbed it (`b63534ef`).
- **#1241 round 4 finding 2** (`tests/skills/test_unverified_check.py:2527`). A named link loop is kept as named. Its kind is *Exclusions & boundaries*. It was fixed at `fa73cf34`.

Use: #1184 is a configuration path a variable moves and #1185 is an `@` line inside a fence, both kinds the table names under *Inputs*, and phase 1 read both as found by a crafter's reading (*Instances C1*). #1187 is a CI shard's timeout, which no review axis is for.

### Drafts

The orchestrator takes each act after the seal, as plan *Operational impact* orders them. Each draft cites this record at the sealed commit, written `<sealed>` below for the orchestrator to fill, and restates no figure its row holds.

#### D3

An evidence comment for #1020, which stays in `release: 0.29.0` (plan *Operational impact* step 3).

> #1038's reading keeps this issue: build. The record is `seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-2.md` at `<sealed>`, *The decisions* row C11, *Instances C11* and *Command C11*.
>
> This issue's comment of 2026-10-30 asked for #1148's measure: where the records-alone count falls and recurrences remain in shipped text, the exchange is the case to make. The work items merged after #1148's pull request show both. The row gives the counts beside this issue's 0.24.0 split, and *Instances C11* names each chain of three or more findings in shipped text and what the run did about it.
>
> Three things for this issue's frame to weigh, each at its instance. In three of the four chains, the orchestrator's judgments of the run already took the structural question: a reframe, a stop with a deferral, and a mechanism filed as its own issue. Whatever this issue builds is weighed against that judgment, which costs no new mechanism. One chain carries only `regression:` lines, so an exchange triggered at the first `reopens:` would not fire on it. And one chain ran four rounds in a plan with no judgment of the run recorded, which is the case the exchange or the check would have changed.
>
> The split between records and shipped text is by each finding's `location:` paths, which the row's grounds compare with this issue's own split.

Proposed home: `release: 0.29.0`, where it stands.

Answers: C11.

#### D4

A reason comment for #27, which then closes through `Closes #27` in this work item's pull request body (`frame/design.md` *Grounding* G10).

> #1038's reading decides this issue: drop. The record is `seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-2.md` at `<sealed>`, *The decisions* row C13 and *Instances C13*.
>
> This issue asks, for each of its seven rules, who could catch it: a gate, the agent that reads it, or nobody. *Instances C13* answers each row at `813665f0`. Three hooks now watch the session rather than a commit: the routing edit gate, the question gate and the implementer notice. The rows they do not reach are caught by the agent that reads the rule, through the agent contract's rules and the commit convention's title step, and those rows are readings of meaning that no gate can make. No row is left with nobody, so nothing is rewritten or dropped.
>
> The first checkbox is answered the same way. The plugin gates a session's procedure where it reads a fact exactly, and leaves the rest to the party that reads the rule.

Proposed home: `release: 0.27.2`, where it stands, so the release check's `M \ D` reports nothing once the pull request carries `Closes #27` (`frame/design.md` *Grounding* G9).

Answers: C13.

#### D5

A reason comment for #6, which then closes through `Closes #6` in this work item's pull request body (`frame/design.md` *Grounding* G10).

> #1038's reading decides this issue: drop. The record is `seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-2.md` at `<sealed>`, *The decisions* row C14, *Instances C14* and *Command C14*.
>
> This issue's test was to run three review rounds under the floor rule, and to build the pass if axes kept leaking. The record holds far more rounds than three. The row counts the later-round findings on lines an earlier round had in front of it, and *Instances C14* judges each against the axes table. One of them is of a kind the table leaves out, a rule sentence with two readings. The writing-style rule the proofer reads names that kind, so a pass that returns axis names would add nothing for it. The axes do not leak in the record, and the floor stays as `skills/code-review/SKILL.md` *The table is a floor, not a ceiling* states it.
>
> The list is a sample. The row names its open part, and a later leak reopens this question with that row as its baseline. The second question here, the `security-audit` heading, left with that skill at `e391ea04` (#1099).

Proposed home: `release: 0.27.2`, where it stands (`frame/design.md` *Grounding* G9).

Answers: C14.

### Phase-boundary run

`bin/test` is the repository's runner. Plan row 2's *Verified by* is "the same, for its rows", which is row 1's three modules. The citation case and the censuses read every tracked file, so they read this phase's files too, and the set ran as one command:

```
bin/test -q -p no:xdist tests/behaviour/test_unverified_rows_close.py tests/behaviour/test_a_phase_hands_the_next_one_a_record.py "tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview" tests/test_censuses.py tests/behaviour/test_a_cited_section_stands_in_its_file.py
```

With this record and `gaps.md` staged, so that `git ls-files` lists them, it exited 0 with 270 passed (executed). The phase changes prose alone, so no lint or format run reads it. `bin/seal unverified seal/threads/1793521558-the-record-decides-each-proposed-verifier` exited 0 and read `gaps.md` as 2 open and 0 closed (executed). Each `Command C<n>` was run again from this record's own text: the three scripts were cut from the record, run in the scratch directory, and their output compared with the blocks above, which they matched (executed). S4's `git diff --name-only 813665f0..HEAD` lists this work item's directory alone; the hand-back gives its output at the closing commit.
