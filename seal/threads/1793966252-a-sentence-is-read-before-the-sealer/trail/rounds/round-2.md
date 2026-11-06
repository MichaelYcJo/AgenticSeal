# Review round 2: 1793966252-a-sentence-is-read-before-the-sealer

```seal
target: 457574049, fixes 96c77a7e8..457574049
```

This is a verifying round over the seven commits after round 1's record:
`d727b29c5`, `960fa60cb`, `13310a396`, `480ff41d8`, `c09c9ec71`, `0fbcbe352`
and `457574049` (executed: `git log 96c77a7e8..457574049`). Round 1 closed
four findings, each `fixed`, and each is answered below by a `confirms:`
line. The range also holds `13310a396`, which rewrites the paragraph round
1 left in `## Not judged`. The orchestrator folded that rewrite into the
frame at `d727b29c5` (`frame/plan.md` *Judgments of the run*, the last
row), and this round reviews it as code. It introduces no defect, so it
takes neither a `regression:` nor a `reopens:` line.

The round ran under the installed 0.33.0 proofer definition. The spawn
prompt asked for the read the branch's `agents/proofer.md` step 3 states.
So this round read `routing.md`, `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` whole at
`457574049`, and judged each sentence against the target. The sections
dated to `1359abcb9` (`frame/design.md` *Grounding*, `frame/plan.md`
*Technical context*) state that commit. No `seal/parity.md` is declared,
so `legacy-parity` does not apply.

Carried from round 1, not re-established: the coordinates of
`frame/plan.md` *Technical context* at `1359abcb9`; the count of each
`## Rule changes` `from:` in its `docs/` file, since the range changes no
file under `docs/` and no operation (executed: `git diff --stat
96c77a7e8..457574049`); the issue bodies of #1415 and #1401; and the remote
state the prefix row names. Re-established this round: the seven quotes of
`pr.md`, the four closes, the refusal forms of `seal pr-body`, the notice
`chain_check.py` prints on `frame/design.md`, and every verdict below.

Stage 1 axes: each close against the snippet its finding gave; each
sentence of the seven records against the target; what the range changes
in `gaps.md`; the `## Removes` row and the *Judgments of the run* row the
fold added; and the fragment's two changed items against the code and the
skill. Stage 2 axes: the new case against `read_own` and against its group
`Test_read_own`; the case seen red with the guard it names removed; the
rewritten paragraph against the gate's record writer and every other
statement in the tree of where the gate's printed lines go; and the tests
that pin that paragraph.

## Findings

None. No defect was found on any axis named above.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the *Grounding* row at
`seal/threads/1793966252-a-sentence-is-read-before-the-sealer/frame/design.md:20`
is round 1's snippet word for word. The case it names exists at
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:234`.
At `1359abcb9` its filter at `:262` reads `name.startswith("pr.") and
name.endswith(".md")`, which matches `pr.md`. At the target the filter at
`:264` adds `and name != "pr.md"`, as the row says phase 2 did. Executed:
`git show 1359abcb9:tests/behaviour/test_the_pull_request_language_is_the_repositorys.py | grep -n`
and `grep -n` of the same file at the target.

```seal
confirms: round-1#2
```
What holds: the Status cell of *Phases* row 3 at
`seal/threads/1793966252-a-sentence-is-read-before-the-sealer/frame/plan.md:37`
reads `eb0bd16b`. At that commit `.claude-plugin/plugin.json` reads 0.34.0,
and at `c64707f4` it reads 0.33.1 (executed: `git show <commit>:.claude-plugin/plugin.json | grep version`). The commits after
`eb0bd16b` up to round 1's target touch the work item's records alone:
`86183daa` the phase record, `5cb64676` the frame, `f98ac0c3` `gaps.md`
and `a817731d3` `pr.md` (executed: `git log --stat eb0bd16b~1..a817731d3`).
So `eb0bd16b` is the last commit phase 3 built. That matches phase 1's
precedent, where the Status cell names `91e05888`, the code commit, and not
the record commit `22d0599b`.

```seal
confirms: round-1#3
```
What holds: the *Alternatives considered* row at
`seal/threads/1793966252-a-sentence-is-read-before-the-sealer/frame/plan.md:20`
now ends "compares the body's lines above the heading with `pr.md`'s, line
ends aside". `pr_body.py#_first_part` compares `READER.gfm_lines` of each
part, which drops the line ends, so the sentence states what the check
compares (read). `frame/design.md:9` still says "byte for byte". It stands
in *Grounding*, dated to `1359abcb9`, and states why the fact may be
gated. Round 1's finding left it as it stands, and this round carries that
reading.

```seal
confirms: round-1#4
```
What holds: `Test_read_own::test_refuses_a_pr_md_that_is_not_utf_8` at
`tests/skills/test_pr_body.py:591-602` is round 1's snippet, with a
docstring that names how it was seen red. This round saw it red the same
way. `except (OSError, UnicodeDecodeError) as exc:` at
`skills/code-review/scripts/pr_body.py:366` was narrowed to `except OSError
as exc:`. The case then failed at `tests/skills/test_pr_body.py:599`,
`PR.read_own(str(item))`, on `UnicodeDecodeError: 'utf-8' codec can't decode
byte 0xff in position 11`. The other two cases of the group passed. The
file was restored, and `git diff --quiet` exits 0. Executed; see
`## Probes`. Read against its group, the case covers the decode branch,
which neither `test_accepts_pr_md_as_its_bytes_stand` nor
`test_refuses_a_line_equal_to_the_heading` reaches. `seal layout --pairs`
names no duplicate pair for `pr_body.py`.

What matched: the class of statements of what `seal pr-body` refuses at
`pr.md` names the decode refusal in each place that lists those refusals.
The list was built by `git grep` for the refusal's words and for "no
`pr.md`", and so it is a sample. `read_own`'s docstring at
`skills/code-review/scripts/pr_body.py:358` names it. So do
`frame/design.md:73` with its `refused:` line at `:77`, which matches the
message at `pr_body.py:368` placed by `_place` at `:829` with no line, and
`changelog.md:5`. The module docstring at `pr_body.py:33-38` names the
heading and the absent `pr.md`, and names no decode refusal of any file. It
claims no whole list, so it is no finding. Read.

What matched: `13310a396` rewrites the paragraph at
`skills/code-review/orchestration.md:450-457`. It now sends the three lines
only the gate prints to the orchestrator's report to the person and not to
the body. Its grounds hold. `broad_gate.py#write_gate_file` at
`skills/verify/scripts/broad_gate.py:2513` writes one line,
`run: <tree> against <base>`, with both as commits. So `trail/gate.md`
holds neither the moved-base line, nor the hand-off to the tree's copy, nor
the `outputs kept under` line that `:3121` writes to stderr (read). The
section's own end, at `:519-520`, puts "the lines worth quoting" in the
orchestrator's result text, which agrees with it. `git grep` for the three
lines' words and for "report to the person" across `docs/`, `skills/`,
`agents/`, `templates/` and both READMEs finds no other statement of where
they go (executed). That search is a sample. The two tests that pin the
paragraph still hold their phrase at the target:
`tests/behaviour/test_the_sealer_guarantees.py:271` and
`tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:104`.
Both docstrings say the orchestrator quotes the line, which stays true. The
narrow run of both modules passed (executed).

What matched: the fold of `13310a396` stands in the frame consistently. The
`## Removes` row at `frame/design.md:182` cites the paragraph by its bold
lead as it stands. The *Judgments of the run* row at `frame/plan.md:56`
names that row and the fix pass's rewrite, and both are in the range. The
fragment's sentence at `changelog.md:4` names two of the paragraph's three
lines with "such as". It sends them where the paragraph does (read). This
round weighed whether the change owes its own `### Process changes` row
under `docs/layout/the-record-layout.md` *A change writes fragments, never
a shared file*. Scope item 8 at `frame/design.md:35` fixes the rows at
items 1, 2, 5 and 7, and the change is an instance of item 4. Row 2 at
`changelog.md:17` states the practice it follows from: `pr.md` holds no
sentence of the orchestrator's own. So it is no finding.

What matched: `457574049` adds the decode refusal to `frame/design.md`
*Data & interfaces*, in the sentence at `:73` and as the `refused:` line at
`:77`. The *Judgments of the run* row at `frame/plan.md:53` still says the
phase 2 fold gave "five forms". That row records the fold at `b64b70e3`,
whose block holds five `refused:` lines, and the block now holds six
(executed: `grep -c '^refused:'` of `frame/design.md` at each commit that
changed it). The row is a dated record of an act. Round 1 read the same row
that way, so it is no finding.

What matched: what the range changes in `gaps.md`
(`git diff 96c77a7e8..457574049`). The first `## Not verified` row is
closed in place: its Item cell now opens with `closed` and keeps its item.
Its second cell names round 1's *Confirmations*, which hold what it says.
The cell's clause that the crafter ran "with the move named in its spawn
prompt" stands in `trail/phases/phase-3.md:5`. That is the crafter's own
account, which the cell does not cite, and the clause is why the new row 8
stays open. Row 8 is new, open, and names its answerer. No row and no memo
left. *Not done*'s fourth paragraph holds: `agents/crafter.md` names no
`pr.md` (executed: `grep -n "pr.md" agents/crafter.md`, no line).

What matched: each of the seven quotes in `pr.md` stands word for word at
the source its coordinate names, at the target. Quote 1 is
`changelog.md:3`, the first item's bold lead without the bold markers.
Quotes 2 to 4 are the bold leads of `changelog.md:6`, `:7` and `:8`, the
fourth, fifth and sixth items. Quote 5 is `frame/plan.md:55`, the prefix
row. Quote 6 is `frame/questions.md:14`, option (a). Quote 7 is
`frame/questions.md:15`, the *Default until answered* cell. The range
changes the second and third items of `changelog.md`. `pr.md` quotes
neither, so no quote went stale and `pr.md` was rightly left as committed
(read).

What matched: no other sentence of `routing.md`, the three frame files,
`gaps.md` or `changelog.md` is contradicted by the target. Two sentences
were checked against the tree: *Scope* item 8's four process rows, which
are `changelog.md:16-19`, and *Operational impact*'s two version commits,
`fe8df522a` and `eb0bd16b7` (read).

What matched: `chain_check.py --worktree` printed one notice on the frame.
"seal/threads/1793966252-a-sentence-is-read-before-the-sealer/frame/design.md:143
a test pins text this operation takes out of `docs/forms/the-guarantee.md`:
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:134`
holds "in the repository's language", and the `to` does not" (executed).
This is round 1's notice, one line lower. That case reads
`skills/commit-pr-convention/SKILL.md`, which it names at `:30`. The file
names `the-guarantee` nowhere (executed: `grep -n`). So the notice names no
pin of this operation's wording and no copy, and it is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the lint and the format check. This round ran four narrow modules, so the suite stands `unverified` | `seal/config.md` *Broad gate* | the orchestrator, at its broad run after the rounds settle |
| Whether the sealer evals and `evals/behaviour/proofer/rule-proofer-one-finding/` still reach their verdicts. No paid eval ran | `seal/threads/1793966252-a-sentence-is-read-before-the-sealer/gaps.md:10`, `seal/threads/1793966252-a-sentence-is-read-before-the-sealer/gaps.md:13` | the owner, at the milestone's paid run |

Nothing stays open from this round. What comes due is the orchestrator's
broad run, then the sealer's spawn.

## Probes

The probe was an edit of `skills/code-review/scripts/pr_body.py` in the
clone, made through the edit tool and restored by `git checkout` of that
file. No probe file was written.

| Command | Result |
|---|---|
| `bin/test tests/skills/test_pr_body.py tests/behaviour/test_the_sealer_guarantees.py tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py -q` | exit 0, `177 passed` |
| `bin/test "tests/skills/test_pr_body.py::Test_read_own" -q`, with `except (OSError, UnicodeDecodeError)` at `pr_body.py:366` narrowed to `except OSError` | exit 1, `1 failed, 2 passed`; the new case failed at `tests/skills/test_pr_body.py:599` on `UnicodeDecodeError` |
| `git checkout -- skills/code-review/scripts/pr_body.py; git diff --quiet` | exit 0 |
| `grep -c '^refused:'` of `frame/design.md` at each commit of the branch that changed it | 2 up to `cf4c05e0`, 5 from `b64b70e3`, 6 at `457574049` |
