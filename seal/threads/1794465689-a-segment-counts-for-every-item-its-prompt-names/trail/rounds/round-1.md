# Review round 1: 1794465689-a-segment-counts-for-every-item-its-prompt-names

```seal
target: 7510173d9 against release/v0.38.0
```

The range is `79f815a74..7510173d9`, the whole branch, read in the branch worktree the spawn named. The seen-red check ran in a `git clone --no-local` at `7510173d9` under the round's scratch directory. This is the first round, so no fact is carried from an earlier record: every coordinate below was opened this round. No `seal/parity.json` stands, so no original is compared. The records read whole at the target are `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md`. Both language keys of `seal/config.json` are English, so no `pr.<lang>.md` stands.

The round weighed the `OverflowError` arm the spawn named, at `skills/verify/scripts/session_cost.py:3142-3145`, and opens no finding on it. The crafter claimed the arm is there for the census alone (`trail/phases/phase-1.md:15`). The probe confirms that `int()` on the bytes a `cat-file` header ends with raises only `ValueError`, so the arm cannot run. Contract rule 18 forbids bending correct code to pass a check. Here the rewrite follows the module's own stated rule at `session_cost.py:1376-1378`: every site that converts to an `int` carries "a `try` catching both `OverflowError` and `ValueError`". The census message asks for the same shape. The phase record reports the false refusal, quoted, which is the other half of rule 18. The comment at `:3140-3141` does not say why `OverflowError` is caught, and a next editor meets the reason only in `token_thirds`' docstring. That comment only reads badly, so it is no finding.

Two gaps that change no behaviour the frame states are named here and not under `## Findings`. `work_item` keeps every walked transcript's spawn prompt in `prompts` (`session_cost.py:3381`), while `also` reads only the prompts of `named`. The old comprehension held none of them. A sibling directory name that holds a newline, or three backticks, would print inside the posted fence as a line of its own. That line could then take the `# <name>.jsonl` shape `posted_names` reads (`frame/design.md` G12). This needs a segment's prompt to name that exact directory, so the round opens no finding for it.

## Findings

### 1. In a partial clone, the branch read fetches other branches' `routing.md` from the remote, while the changelog says it reaches no network

```seal
severity: should
location: `skills/verify/scripts/session_cost.py:3082-3092`, `seal/threads/1794465689-a-segment-counts-for-every-item-its-prompt-names/changelog.md:4`, `seal/threads/1794465689-a-segment-counts-for-every-item-its-prompt-names/frame/plan.md:40`, `tests/skills/test_session_cost.py`
evidence: executed `sh test_tmp_lazy.sh` and `sh test_tmp_nolazy.sh` under the round's scratch directory (the `## Probes` rows); read `skills/verify/scripts/session_cost.py:3082-3150`, `README.md:399`, `CONTRIBUTING.md:493-496`
```

Why it matters: the build says three times that its git reads stay on the machine. `changelog.md:4` says "The four `git` commands it runs only read and reach no network". `frame/plan.md:40` says "All four only read, and none reaches the network". The `run_git` docstring says "Every call here only reads". `CONTRIBUTING.md:493-496` makes `README.md` *What runs on your machine* the place that names every command reaching a network. That table gives `seal cost` a row only for the `gh` calls.

The claims do not hold in a partial clone. `branch_declarations` asks `git cat-file --batch` for `<tree id>:routing.md` at the tip of every local branch (`session_cost.py:3128-3130`). A blobless clone (`git clone --filter=blob:none`) does not hold the blobs of a branch that was never checked out. For a missing blob, `cat-file` starts a fetch from the promisor remote, the remote the partial clone came from. The probe built such a clone, with a local branch `other` made from `origin/other` and never checked out. It then sent the exact request `branch_declarations` writes. `cat-file` printed the blob, and `GIT_TRACE` showed it ran `git fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin`. In a user's partial clone, that fetch goes to their real remote with their git credentials, from a command the table lists as reaching only issues through `gh`. Where the credentials are not cached, the fetch is likely to stop and ask for them in the middle of a run. This round did not run that case.

With `GIT_NO_LAZY_FETCH=1` in the environment, the same request in a fresh clone answered `<tree id>:routing.md missing` and ran no fetch (second probe). The parse at `:3140-3145` already reads a `missing` line as a directory with no `routing.md`. So an item whose `routing.md` the clone does not hold is not read, and the D3 count line shows the smaller reach, as `frame/plan.md` *Technical context* accepts for a deleted branch. Precondition: the fix relies on git reading the variable. git 2.50.1 read it in the probe. A git too old to know the variable ignores it and fetches as now. This round ran no older git.

Replace `skills/verify/scripts/session_cost.py:3082-3092` with:

```python
def run_git(cwd, args, stdin=None):
    """`git -C CWD` with ARGS, as `(exit code, stdout bytes)`, or `(None, b"")`
    where git could not start. Bytes, because `cat-file --batch` gives each
    object's size in bytes. Every call here only reads, and none fetches: in
    a partial clone `cat-file` would fetch a blob the clone lacks from its
    remote, and `GIT_NO_LAZY_FETCH` makes it answer `missing` instead, which
    `branch_declarations` reads as a directory with no `routing.md`."""
    try:
        done = subprocess.run(
            ["git", "-C", cwd, *args],
            input=stdin,
            capture_output=True,
            env={**os.environ, "GIT_NO_LAZY_FETCH": "1"},
        )
    except OSError:
        return None, b""
    return done.returncode, done.stdout
```

The snippet does not cover the other statements of the claim, and the fix pass owes them too. In `changelog.md:4`, the sentence becomes "The four `git` commands it runs only read and fetch nothing, so in a partial clone an item whose `routing.md` the clone does not hold is not read." In `frame/plan.md:40`, "All four only read, and none reaches the network" gains the same clause. The fix also owes a case in `Test_work_item` in `tests/skills/test_session_cost.py`. The case builds a source repository with `uploadpack.allowFilter` set and a second branch holding another item. It clones it with `--filter=blob:none` over `file://` and makes a local branch from the remote one without checking it out. It then asserts that the page does not name that item and that `git cat-file -e <blob>` still fails afterwards. Contract rule 15 has it seen red with the `env` line removed.

### 2. `README.md` *What runs on your machine* does not say the posted comment now names other work items, read from every local branch

```seal
severity: should
location: `README.md:399`, `README.ko.md:395`
evidence: read `README.md:399`, `README.ko.md:395`, `CONTRIBUTING.md:493-496`, `skills/verify/scripts/session_cost.py:3095-3185`, `skills/verify/scripts/session_cost.py:3317-3327`, `tests/skills/test_session_cost.py:5544-5573`, `seal/threads/1794465689-a-segment-counts-for-every-item-its-prompt-names/trail/phases/phase-1.md:49`
```

Why it matters: `CONTRIBUTING.md:493-496` makes this table the place that names "what each reaches, what it sends and when". Its `Sends` cell for `seal cost --post` lists what the comment holds: the orchestrator's sentence, the agent's numbers, and each transcript's file name, never its path. This work adds a new kind of content to the posted body. It is the directory name of each other work item a shared segment's prompt also names (`session_cost.py:3317-3327`, inside the fence, as the S1 case asserts at `tests/skills/test_session_cost.py:5570-5573`). The names come from the sibling directories and from the tip of every local branch (`session_cost.py:3095-3150`), so a branch that was never pushed is a source too. A person who reads the cell to learn what leaves their machine finds neither the names nor where they are read from.

The crafter claimed the cells "name no directory, which stood the same way before this work, when the comment already named the work item's own directory and branch" (`trail/phases/phase-1.md:49`). Reading the base confirms that the page's first line named the item's own directory and branch before this work. That name, though, travels with the pull request the same run opens. The names this work adds belong to other items, and come from branches that may stay local. `frame/design.md` G13 judges such a name to be the same kind of text as the item's own, and this round does not reopen that judgment. It asks only that the disclosure say it. The frame's *Scope* puts `README.md:423` and `README.ko.md:419` out, with a ground, and does not weigh these two rows.

In `README.md:399`, after "names each transcript the numbers were read from by its file name, never by its path.", insert:

```markdown
With `--work-item`, it also names the work item's directory and branch, and the directory of each other work item a segment's spawn prompt also names, read from the records directory and from every local branch, pushed or not.
```

In `README.ko.md:395`, after "수치를 읽은 트랜스크립트는 하나하나 경로가 아니라 파일 이름으로만 적힌다.", insert:

```markdown
`--work-item` 을 붙이면 작업 항목의 디렉터리와 브랜치도 적히고, 세그먼트를 띄운 프롬프트가 함께 적은 다른 작업 항목의 디렉터리 이름도 적힌다. 다른 작업 항목은 기록 디렉터리와, 푸시했든 하지 않았든 모든 로컬 브랜치에서 읽는다.
```

### 3. The changelog says a later run whose segments are all in the log still prints the shared segments, and a `--post` run prints none of them

```seal
severity: should
location: `seal/threads/1794465689-a-segment-counts-for-every-item-its-prompt-names/changelog.md:3`, `skills/verify/scripts/session_cost.py:3296-3299`
evidence: read `skills/verify/scripts/session_cost.py:3388-3394`, `skills/verify/scripts/session_cost.py:3296-3299`, `seal/threads/1794465689-a-segment-counts-for-every-item-its-prompt-names/frame/design.md:33`, `seal/threads/1794465689-a-segment-counts-for-every-item-its-prompt-names/frame/design.md:53`, `docs/releasing/release-checklist.md:216-220`
```

Why it matters: `changelog.md:3` says "The read without `--post` and the posted comment both carry these lines, inside the comment's fence. A later run whose segments are all in the log still prints them." The second sentence names no mode, after a sentence that names both. Under `--post`, `work_item` returns at `session_cost.py:3388-3394` when every counted segment is in the log. That return comes before `other_work_items` runs, and it prints only "every one of the N segment transcripts naming ... is already named on #N, so nothing was posted". The release runs exactly that form for each item it ships (`docs/releasing/release-checklist.md:216-220`). So a reader of the release note expects a line the release's own run never prints. The behaviour matches the frame: S2 (`frame/design.md:53`) restricts the line to "the read without `--post`", and the phase record states the early return (`trail/phases/phase-1.md:19`). Only the two texts overstate it. The `report_work_item` docstring at `:3296-3298` says the same of "a later run", and a next editor reads it as true of both modes.

In `changelog.md:3`, replace "A later run whose segments are all in the log still prints them." with:

```markdown
A later read without `--post` whose segments are all in the log still prints them; a `--post` run with nothing left to post prints only that nothing was posted.
```

Replace `skills/verify/scripts/session_cost.py:3296-3299` with:

```python
    **The lines on other work items print before either early return**, so
    a later read without `--post` whose segments are all in the log still
    shows the segment it shares with the run that posted it. With `--post`,
    `work_item` returns before this page when nothing is left to post. None
    of these lines is a `# <file name>` line, which `posted_names` would
    read as a posted segment.
```

## Confirmations

What matched: D1's two sources, as the fold at `c4ea14c83` states them, are what `other_work_items` and `branch_declarations` do (`session_cost.py:3095-3185`, read). The siblings on disk are read first. Every git command runs from the parent directory, and `rev-parse --show-toplevel` is the gate for a local-mode root. `for-each-ref` lists the tips, `ls-tree -z <tip>` lists each tip's entries, and one `cat-file --batch` reads `<tree id>:routing.md` per distinct tree id. The item's own name is left out, and a directory at several tips keeps every branch. That `ls-tree` run from a subdirectory lists that subdirectory's entries was executed: `git -C <worktree>/seal/threads ls-tree HEAD` listed the work item directories.

What matched: D2 and D3 hold at `session_cost.py:3395-3406` and `:3317-3327` (read). The count line prints under the log note, before both early returns of `report_work_item`, with or without a match. One line prints per shared segment, `already in the log` is marked from `in_log`, and no added line opens with `# ` (G12). Every exit path of `work_item` is unchanged (read, `:3345-3436`).

What matched: S6 and D4. `skills/verify/orchestration.md:166-176` keeps the sentence D4 names and adds that a segment whose prompt also names another work item is counted for each and named with those items. It says the `--says` sentence judges the run it belongs to (read). The usage line, the comment above `POSTED_NAME`, the docstrings of `work_item` and `report_work_item`, and the `--work-item` help say the same (read), apart from finding 3's docstring sentence.

What matched: the phase record's claim of contract rule 15. The six new cases of `Test_work_item` failed against the base module, and the 21 existing cases passed (executed, the `## Probes` row). The whole module passed at the target (executed). The new cases were read against their group. Each holds a fact no other case holds: the sibling match on both pages and in the posted fence (S1), the `already in the log` mark above the every-segment sentence (S2), the branch read with two items and a directory with no `routing.md` (S3), the count line with no match (S5), the local-mode gate, and the `OSError` arm. The mutation run of 17 breaks was not re-run, and the round carries it as the crafter's claim.

What matched: the operation under `## Rule changes` is placed (G18). `rule_changes.parse` read this design and `1794312072-the-cost-comment-is-posted-per-segment`'s with no error and no unread line. `apply_op` placed `1794312072`'s four operations on `docs/running/measuring-a-run.md` and then this one, and the document then holds the `to` (executed, the `## Probes` row).

What matched: both quotes of `pr.md` stand word for word at their coordinates, `frame/plan.md:40` and the title row at `frame/plan.md:46` (read). `changelog.md` carries the `### Process changes` row *Scope* item 6 asks for (read). The `gaps.md` rows name answerers that exist: `seal gate --record`, the orchestrator's S7 read, and the `test` workflow, whose matrix at the target holds ubuntu, macOS and Windows legs (`.github/workflows/test.yml:52-79`, read).

What matched: the frame puts `README.md:423` and `README.ko.md:419` out of *Scope*, saying each "gives one row per segment found by its spawn prompt naming the item's directory or branch, which stays true". It still holds at the target (read). The spawn's question on `README.md:399` and `README.ko.md:395` is answered by finding 2.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the work item's HEAD; this round ran one module and labels the suite `unverified` | `seal/config.json` `Broad gate` | the orchestrator, by `seal gate --record` |
| S7: the page over this machine's four framer transcripts of release 0.38.0 | `frame/design.md:58` | the orchestrator, at the run's read, before the post |
| The new cases on Linux and Windows, where the branch read runs `git -C` and the cases build a repository with `git` | `tests/skills/test_session_cost.py:5599-5712` | the `test` workflow at the pull request |
| The mutation run of 17 breaks the phase record reports | `trail/phases/phase-1.md:27-47` | the crafter's claim, carried; no party re-runs it unless a fix touches `branch_declarations` or `report_work_item` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_session_cost.py -q`, in the branch worktree at `7510173d9` | exit 0, 275 passed |
| `bin/test tests/skills/test_session_cost.py -q -p no:xdist -k Test_work_item`, in a `git clone --no-local` at `7510173d9` with `skills/verify/scripts/session_cost.py` checked out from `79f815a74` | exit 1, 6 failed and 21 passed; the six failures are the six new cases |
| `python3 test_tmp_round1.py <worktree>`: `rule_changes.parse` over both designs, then `apply_op` of each operation on `docs/running/measuring-a-run.md` in order; then `int()` over `b"missing"`, `b""`, 5,000 digits, `b"inf"`, `b"nan"` and `b"12"` | exit 0; no error, no unread line, all five operations placed, and the document holds this design's `to`; every `int()` raised `ValueError` except `b"12"`, which gave 12, and none raised `OverflowError` |
| `sh test_tmp_lazy.sh`: a blobless `file://` clone with a local branch `other` never checked out, then `cat-file --batch` with `<tree id>:routing.md` from inside `seal/threads`, under `GIT_TRACE=1`, on git 2.50.1 | exit 0; the blob printed, and the trace shows `cat-file` ran `git fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` |
| `sh test_tmp_nolazy.sh`: the same request in a fresh blobless clone, with `GIT_NO_LAZY_FETCH=1` | exit 0; `<tree id>:routing.md missing`, and no fetch line in the trace |
