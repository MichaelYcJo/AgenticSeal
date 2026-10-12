# Round 1 report — 1791779434, under automation the guard asks nobody (#894)

Target `c0fbf89c`, base `origin/release/v0.21.0` at `c38f97d7`. Reviewed by
the warden in a `git clone --no-local` of the worktree at the target. The
clone, its virtualenv and the one-file test_tmp probe were deleted before this
report was written.

## The shape of what was found

The change does what it says. The attended `ask` is byte-identical to the
base, the press is read where the stop reads it, and every way on the deny
names passes the guard. Those were run, not read.

What is wrong sits in the deny's own text and in one ledger row:

1. Way 1 of the deny, *commit here first*, is wrong for the one switch whose
   purpose is to carry the changes along: `git switch -c <new>`. Under the
   press that switch now meets the deny, and way 1 leaves the commit on the
   branch being left (🟡 1).
2. The same way 1 tells the model, in every repository the plugin runs in,
   that a feature branch squashes at the merge. That is this repository's
   convention, and `skills/implement/SKILL.md` §2 says to read it off the
   repository before leaning on it (🟡 2).
3. 0.15.6 W9 was re-stamped as holding while its *asks* now holds only
   attended. The smith named this in `overview.md` and left it. It is a
   record correction (⬜ 3).
4. Two smaller text gaps: the resume paragraph leaves out the same-clone
   condition (⬜ 4), and the deny's premise is false for a switch that
   discards or merges the changes (⬜ 5).

## The seven questions, in the order asked

**1. The attended path is byte-identical.** Executed. A differential probe
loaded the base's `hooks/worktree-guard.py` beside the head's and fed both
the same payloads with no press reaching the row. Twenty cells, all
`identical=True`: English and Korean, single-stream, `[shared-tree-ok]` from
only-idle and from detection-unusable, `git -C <repo> switch` from outside the
repository, `git switch -c`, each with the session holding a press given in
an unrelated clone and with a session that has no transcript. The fixture
held a force-added ignored file, so the phantom note was in every reason.
Read: the diff inserts one `if` block before the untouched `respond("ask", …)`
and changes no line of the `ask`.

**2. Where the press is read.** Executed and read. The row calls
`automation_pressed(repo_paths(cwd)[0], …)`, the call the stop makes at
`hooks/worktree-guard.py:2956`. `hooks/worktree_consent.py#automation_answered`
then requires the press's own `cwd` to sit in the same clone as that root
(its condition 4). A switch into a second dirty clone through `git -C`
denies under the press given in the session's clone and names the second
clone in every command (the smith's case, which passed in the module run). A
session whose shell sits outside any repository reads no press, so the same
`git -C` switch asks (probe). That is the stop's behaviour too, and it fails
toward a question, not toward a silent switch. Reading the session's root is
right: the question the press answers is whether anybody is at the keyboard,
and that belongs to the session, not to the tree the command names.

**3. The deny's ways on.** Executed. Under the press, in a dirty tree, each of
these is silent: `git branch --show-current`, `git branch keep`, `git add
-A`, `git commit -m x`, `git commit -am x`, `git stash`, `git stash push -m
x`, `git stash pop`, and the phantom note's `git -C <top> restore --staged
<path>`. From a detached HEAD the switch meets the deny, `git branch
--show-current` prints the empty string, and both `git branch` forms stay
silent. The text says each step is its own command, says what `pop` applies
to, and the detached-HEAD check is correct git. A compound `git stash && git
switch x` meets the deny (pinned by the smith's S5). What does not hold is
way 1 for a creating switch, which is 🟡 1.

**4. No loop.** Read and executed. The deny ends with *Re-issuing this command
unchanged meets this same refusal*, and its text holds no `AskUserQuestion`
(pinned by S1 in both languages). The stop's rewrite reaches this deny, and
this deny's ways reach a clean tree, so nothing cycles back to a question.
Whether a model loops anyway is M3, which stays the next run's measurement.

**5. S8.** Executed: `git diff --stat origin/release/v0.21.0...c0fbf89c --
hooks/commit-review-gate.py hooks/worktree_consent.py hooks/cmdline_base.py`
printed nothing and exited 0.

**6. The three `Corrected ·` rows and the re-stamps.** Read. A4, S2 and S6 each
state what the code at the head does: no consent makes a switch silent, the
ladder's only new branch is the press inside the tracked-changes row, and
the plain retry in a dirty tree is the deny under the press and the `ask`
without it. The re-read rows in `1791384154` and `1791384160` cite the
code-review orchestration headings, whose claims the new sentence does not
touch. Of the `1791384157` re-stamps onto `hooks/worktree-guard.py#main`,
only W4 and W9 speak about the tracked-changes row's verdict. W4 got a note
in this item's fragment that says it holds with the press absent. W9 got
none, which is ⬜ 3.

**7. The resume paragraph and M2.** Read and executed. The paragraph matches
conditions 1 to 3 of `automation_answered`: a harness-written result, in this
session's own main transcript, of the routing question, and a typed answer
does not count. It leaves out condition 4 (⬜ 4). M2 reproduces on this
machine: 115 main transcripts, 20 compaction boundaries each under its own
file's id, 8 files written by more than one CLI version, and no file holding
another session's id. I added one check the smith did not run: no transcript
begins with an entry whose parent lives in another file, which is what a
resume that forked into a new file would leave. So the claim stands at the
confidence of an inference from transcript signatures. Nobody has run a
`--resume` and watched the guard read the press. The orchestration paragraph
says it was read off transcripts. The §*Known limits* bullet states it flatly,
and that is acceptable given the reproduction.

## Findings

### 🟡 1 — Under the press, `git switch -c <new>` meets the deny, and way 1 misplaces the commit

`hooks/worktree-guard.py:3296` (English) and `:3319` (Korean).

Executed: under the press in a dirty tree, `git switch -c newb` and `git
switch -c newb main` both answer the deny with the full text. Attended, both
answered the `ask`, and approving it was the right answer, because carrying
the changes to the new branch is what `-c` is for.

Way 1 tells the model to commit here first and re-issue the switch. Read
from git's semantics, not executed:

- For `git switch -c newb`, the commit lands on the branch being left, and
  `newb` starts from it. The work now sits on two branches, one of them the
  wrong one.
- For `git switch -c newb main`, the commit stays on the branch being left
  and `newb` starts from `main` without it. The change never reaches the
  branch the model was making for it.

Way 2 is correct for both. The text gives no hint which way fits, and way 1
is listed first. Why it matters: a smith that starts its work on a release
branch checkout and branches off with `-c` follows way 1 and commits onto the
release branch. Where that branch has no `routing.md`, the commit gate stops
it. Where it has one, the commit goes through silently.

The fix is in the text. A sentence in way 1 says it keeps the changes on the
branch checked out now, so a switch that creates its branch to carry them
takes way 2. A case pins `-c` under the press and runs way 2 with real git.

### 🟡 2 — The deny tells every repository that a feature branch squashes at the merge

`hooks/worktree-guard.py:3299` and `:3321`.

The guard ships with the plugin and runs in every repository that opts in.
The sentence *a feature branch squashes at the merge* is true here
(`docs/branch-and-release.md`), and it is the first of the two conditions
`skills/implement/SKILL.md` §*2. Implement* tells a reader to "read both off
the repository before leaning on them". In a repository that merges without
squashing, the deny tells the model something false about what its
intermediate commit costs, and it says so as the reason to take way 1.

The fix drops the clause. The `routing.md` sentence beside it is true in
every opted-in repository, so it stays.

### ⬜ 3 — 0.15.6 W9 is re-stamped as holding, and its *asks* now holds only attended

`seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md:31`.

W9 says *a dirty repository reached from elsewhere asks and names its own
changes*. Under the press, read from the session's root, that switch is the
deny (the smith's W2 case shows it). The re-read row's Result column says
*the cited row's claim holds*, at `main@c6554e10`, dated 2026-10-12, with no
note. W4, the sibling claim, got a note in this item's fragment. The smith
named the gap in `overview.md` §*Not done* and left it to whoever wants it
exact.

This is a record correction under `docs/review-chain-spec.md` §*A finding
located in a record is a correction, not a round*. `Needs a fix` does not
count it. A `Corrected ·` row in this item's fragment, or a note like W4's,
closes it.

### ⬜ 4 — The resume paragraph leaves out the same-clone condition

`skills/implement/orchestration.md:291`.

The paragraph says the gates read a harness-written result in this session's
own transcript and nothing else. `automation_answered` also requires the
result's own `cwd` to resolve to the same clone as the root the gate reads
from, and the guard reads from the session's own root. A resumed session
started outside the run's clone, for example in a parent folder or in
another working directory, can put question 1 exactly as the paragraph says
and hold no press anywhere the guard looks. That is the #894 failure again,
one step removed. One clause closes it.

### ⬜ 5 — For a switch that discards or merges the changes, the deny's premise is false

`hooks/worktree-guard.py:3288`.

Executed: `git switch --discard-changes feature/x`, `git switch -f
feature/x` and `git switch -m feature/x` each meet the deny, which opens by
saying the changes *would follow it onto the target branch*. With
`--discard-changes` and `-f` they are thrown away, and with `-m` they are
merged. The attended `ask` at the base says the same (*They will follow you
onto the target branch*), so the premise is inherited. Under the press it is
now the only text the model gets, and the deny offers no way to discard on
purpose. `git restore`, which §*Never guarded* lists, would do it. Blocking
is the right direction here. Only the sentence is wrong. Noted for whoever
next touches the row's text, #21 included.

## Axes walked

- **Spec compliance.** In 2 and S1 to S11: met as written. In 3: met, with
  ⬜ 4. §*The class*: the enumeration matches `main`, where
  `automation_pressed` is called at 2956 (the stop) and 3282 (the row) and
  nowhere else in the switch direction.
- **Failure direction.** Read and executed: one verdict moves, from `ask` to
  `deny`, in one state. A wrong press costs the model a turn. No path is
  made more permissive.
- **Security.** The press is the one input the model cannot write, and here it
  can only tighten a verdict. The deny's commands quote the root through
  `git_at`, whose quoting is unchanged. Nothing new is read from the tree or
  the payload.
- **Concurrency.** The row reads the tree before the line runs, as before,
  and the text tells the model so. No new shared state, marker or lock. The
  ACTIVE row still comes first, so the press never crosses another
  session's tree (A4's cases passed in the module run).
- **Efficiency.** One more transcript scan per dirty switch where the stop did
  not fire. The stop exits whenever it reads the press, so one command never
  scans twice (W2). `automation_answered` measured 0.09 s on a 17.3 MB
  transcript, per its docstring (read, not re-measured).
- **This change's own axes.** Byte-identity attended (executed, 20 cells).
  The ways on pass the guard, including from a detached HEAD (executed).
  The press's locality (executed). The text's truth for every switch shape
  that reaches the row (executed: 🟡 1 and ⬜ 5). The text's truth in every
  repository that runs it (read: 🟡 2).

## Regression tests to plant

- `tests/test_the_guard_asks_once_per_session.py`: under the press in a dirty
  tree, `git switch -c newb` meets the deny, the reason names way 2 for a
  creating switch, and `git stash`, `git switch -c newb`, `git stash pop`
  each pass the guard and leave `M f.txt` on `newb` (🟡 1). Seen red by
  deleting the new sentence from the text.
- Same file: from a detached HEAD in a dirty tree under the press, `git
  branch --show-current` and `git branch <name>` are silent. The probe ran
  this once and nothing pins it. Without it, a later change to the shape
  list can turn the deny's detached-HEAD advice into a second deny.

## Facts for the evidence ledger

- M2, reproduced on 2026-10-12 on the same machine: 115 main transcripts
  under `~/.claude/projects/`, 20 compaction boundaries none of them under a
  foreign id, 8 files written by more than one CLI version, 0 files holding
  another session's id, and 0 transcripts whose first entry's parent lives in
  another file. Executed, read-only, counts only.
- The attended `ask` of the tracked-changes row is byte-identical to
  `c38f97d7`'s in 20 cells, including the phantom note. Executed through a
  differential probe. S2's ledger row cites a captured-text assertion, and
  this probe is independent of it.

## Not verified

| Item | Who answers it |
|---|---|
| The full suite, the repository-wide lint and the typecheck: `unverified`. The broad run is the sealer's, once, after the rounds settle | the orchestrator, by spawning the sealer once nothing is open |
| That `claude --resume` keeps the press in a live run. The evidence is transcript signatures, reproduced above, and nobody has resumed a session and watched the guard read it | the orchestrator, at the next resumed `automation` run, from its transcript |
| Windows: the row is reached there only under `[shared-tree-ok]` from detection-unusable. Read from the code, S3 covers it with the count stubbed | the Windows CI leg at the pull request |

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | Under the press, `git switch -c <new>` in a dirty tree meets the deny, and way 1 (commit here first) puts the commit on the branch being left, or leaves it off the new branch when a start point is named | `hooks/worktree-guard.py:3296` | open | Executed: both `-c` forms answer the deny under the press, and the base asked. Read: git's semantics for a commit before `switch -c` |
| 🟡 2 | The deny tells the model, in every opted-in repository, that a feature branch squashes at the merge | `hooks/worktree-guard.py:3299` | open | Read: `skills/implement/SKILL.md` §2 makes squashing a property to read off each repository. The hook ships to all of them |
| ⬜ 3 | 0.15.6 W9 re-stamped as holding at `main@c6554e10` with no note, while its *asks* holds only without the press | `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md:31` | open | Read: the W2 case shows the deny for the same switch under the press. A record correction, so `Needs a fix` does not count it |
| ⬜ 4 | The resume paragraph omits `automation_answered`'s same-clone condition, so a resumed session started outside the clone can press and still hold no press the guard reads | `skills/implement/orchestration.md:291` | open | Read: `hooks/worktree_consent.py#automation_answered`, condition 4 |
| ⬜ 5 | For `--discard-changes`, `-f` and `-m`, the deny says the changes would follow, which is false. Inherited from the base's `ask` | `hooks/worktree-guard.py:3288` | open | Executed: all three meet the deny under the press |
| 🟢 | The attended path is byte-identical to the base in both languages and every state that reaches the row | `hooks/worktree-guard.py:3282` | confirmed | Executed: base and head differential, 20 of 20 cells identical |
| 🟢 | The press is read from the session's own root, as the stop reads it, and that is the right root | `hooks/worktree-guard.py:3282` | confirmed | Executed: the W2 case passes, and a shell outside any repository asks. Read: the stop's call at line 2956 |
| 🟢 | Every way on the deny names passes the guard, including from a detached HEAD, and the detached-HEAD check is correct | `hooks/worktree-guard.py:3292` | confirmed | Executed: probe over 9 commands in a dirty tree and 3 from a detached HEAD |
| 🟢 | No loop: the re-issue sentence is present and no question tool is named | `hooks/worktree-guard.py:3308` | confirmed | Read, and S1 pins the whole text in both languages |
| 🟢 | S8: the three hooks are byte-identical to the base | `hooks/commit-review-gate.py` | confirmed | Executed: `git diff --stat` printed nothing, exit 0 |
| 🟢 | The `Corrected ·` rows for 0.20.0 S2 and S6 and 0.15.5 A4 state what the head does | `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md:9` | confirmed | Read against `main`. Their cases passed in the module run |
| 🟢 | M2's claim reproduces at the confidence the orchestration paragraph states | `skills/implement/orchestration.md:301` | confirmed | Executed: the same counts, plus no transcript continuing another file's chain |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_the_guard_asks_once_per_session.py tests/test_worktree_guard.py -q` in the clone at `c0fbf89c` | exit 0, 228 passed |
| Base and head differential: the base's `hooks/worktree-guard.py` loaded beside the head's, the same payloads with no press reaching the row, through a one-file test_tmp probe (deleted) | 20 of 20 cells `identical=True`, all `ask` |
| Under the press, dirty tree: the guard over 18 commands, the ways on and the switch shapes | ways on all silent. `git switch` with `feature/x`, `-c newb`, `-c newb main`, `-`, `--discard-changes`, `-f` and `-m` all deny with the row's text. `git checkout -b newb` meets the stop |
| Under the press, detached HEAD, dirty tree | `git branch --show-current` silent and prints the empty string. `git branch keep` silent. `git switch feature/x` denies |
| Under the press given in the repository, shell outside any repository, `git -C <repo> switch feature/x` | `ask` |
| `git diff --stat origin/release/v0.21.0...c0fbf89c` on the three S8 hooks | no output, exit 0 |
| Read-only count over `~/.claude/projects/*/*.jsonl` | 115 files, 8 with more than one version, 20 compaction boundaries, 0 foreign ids, 0 first entries parented in another file |
| The full suite, the repository-wide lint and the typecheck | not yet. Unverified. The sealer runs them once, after the rounds settle |

## Paste-ready fixes

### 🟡 1 and 🟡 2 — way 1 of the deny, both languages

One edit closes both. It replaces the way-1 lines in the English half
(`hooks/worktree-guard.py:3296` to `:3302`):

```python
                    f"  1. Commit the changes here first (`{git} commit …`), then "
                    "re-issue the switch. This keeps them on the branch checked "
                    "out now, so where the switch creates its branch (`-c`) to "
                    "carry them there, take way 2. On a branch a `routing.md` "
                    "declares, the commit gate is silent for that commit. Where "
                    f"HEAD is detached (`{git} branch --show-current` prints "
                    "nothing), the commit lands on no branch: name it with "
                    f"`{git} branch <name>` before the switch, or take way 2.\n"
```

And in the Korean half (`:3319` to `:3326`):

```python
                    f"  1. 먼저 여기서 변경을 커밋하고(`{git} commit …`) 전환을 "
                    "다시 실행합니다. 이 방법은 변경을 지금 체크아웃된 브랜치에 "
                    "남기므로, 브랜치를 새로 만들어(`-c`) 변경을 그쪽으로 옮기려는 "
                    "전환이면 2번을 택하세요. `routing.md` 가 선언한 브랜치에서는 "
                    "커밋 게이트가 이 커밋을 막지 않습니다. HEAD 가 분리되어 "
                    f"있으면(`{git} branch --show-current` 가 아무것도 출력하지 "
                    "않으면) 커밋이 어느 브랜치에도 남지 않습니다. 전환 전에 "
                    f"`{git} branch <name>` 으로 이름을 붙이거나 2번을 "
                    "택하세요.\n"
```

`dirty_deny` in `tests/test_the_guard_asks_once_per_session.py` takes the same
two sentences, and the new case pins the `-c` shape:

```python
def test_a_creating_switch_under_the_press_takes_the_stash_way(
    monkeypatch, capsys, projects, repo
):
    """Round 1, yellow 1. `-c` meets the deny, the reason sends a creating
    switch to way 2, and way 2 carries the change onto the new branch."""
    write_transcript(projects, "me", ask_entries(repo))
    dirty(repo)
    decision, reason = decide(monkeypatch, capsys, repo, "git switch -c newb")
    assert decision == "deny", reason
    assert "creates its branch (`-c`)" in reason, reason
    assert "squashes" not in reason, reason
    for command in ("git stash", "git switch -c newb", "git stash pop"):
        assert decide(monkeypatch, capsys, repo, command) == ("silent", ""), command
        git_in(repo, *command.split()[1:])
    assert git_in(repo, "branch", "--show-current") == "newb"
    assert git_in(repo, "status", "--porcelain") == "M f.txt"
```

### ⬜ 3 — 0.15.6 W9, narrowed in this item's fragment

Let `bin/evidence-check` compute the anchor's hash. The row's words:

```
| Corrected · W9 · the switch ladder's tracked-changes row lists the changes of the tree the switch acts on — the `git -C` or `cd` target every row above it judged — and runs its force-staged check at that tree's root, not in the shell's starting directory and not in a subdirectory it was reached through. Without the `automation` press a dirty repository reached from elsewhere asks and names its own changes; under the press, read from the session's own root, it is the `deny` to the model naming the same changes; a clean clone switched from a dirty session tree says nothing; an anchored ignore pattern is named from a subdirectory | `seal/releases/0.15.6.md#"### 1790550712-the-worktree-guard-judges-a-switch-after-a-creation">"W9 · the switch ladder's"@<hash>`, `tests/test_guard_resolves_the_tree_it_judges.py::test_the_dirty_tree_row_reads_the_tree_the_switch_is_in`, `tests/test_the_guard_asks_once_per_session.py::test_the_press_is_read_from_the_sessions_own_root` | **Executed** <date>: both cases pass at the head | <date> | Corrected <date> by work item 1791779434-under-automation-the-guard-asks-nobody (#894): W9 said a dirty repository reached from elsewhere asks, and under the press it is the deny |
```

### ⬜ 4 — the resume paragraph names where the session stands

In `skills/implement/orchestration.md`, after *and `routing.md` is not read*:

```markdown
The session puts it from a directory inside the clone the run works in: the
readers keep the answer only where the result's own directory and the
gate's root are the same clone (`docs/worktree-guard-spec.md` §*Creation
consent*, rule 4).
```

Needs a fix: yes — 🟡 1 (way 1 misplaces the commit for `git switch -c`) and 🟡 2 (the squash claim sent to every repository)

Loses a record or crashes: no

## Proof block

Files opened at `c0fbf89c`:

- `hooks/worktree-guard.py`: `main` from the walk through the ladder's end,
  `automation_pressed`, `repo_paths`, `respond`
- `hooks/worktree_consent.py`: `transcript_for`, `_routing_preset`,
  `_routing_answer`, `automation_answered`, `consent`
- `tests/test_the_guard_asks_once_per_session.py`: the header, `decide`,
  `ask_entries`, `write_transcript`, `projects`, `dirty`, and the #894 cases
- `tests/test_worktree_guard.py`: the S2 assertion and its constants
- `tests/conftest.py`: `load_hook_module`, `run_hook`, `repo`
- `docs/worktree-guard-spec.md`: §A and its new paragraphs, §*Creation
  consent*'s ordering table and property, §*Choice sites* on the token,
  §*Known limits*
- `skills/implement/orchestration.md` and `skills/code-review/orchestration.md`:
  the changed paragraphs
- `skills/implement/SKILL.md`: §2's two conditions
- `docs/the-evidence-ledger.md`: §*A citation that does not hold is named* and
  the `--reverify --into` paragraph
- `docs/review-chain-spec.md`: §*A finding located in a record is a correction*
- `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` whole,
  and the changed rows of `1791384154`, `1791384157` and `1791384160`
- `seal/releases/0.15.6.md` W2, W4, W7, W9; `seal/releases/0.20.0.md` S2, S3,
  S6, S8, S12, F1, Corrected R6, Corrected W1; `seal/releases/0.15.5.md` A4,
  A5; `seal/releases/0.9.1.md`, the writer-property row
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/`: `spec.md`,
  `overview.md`, `changelog.md`, `questions.md`, `routing.md`, and
  `phases/phase-2.md`'s M2 paragraph
- the round brief the orchestrator wrote for this round
