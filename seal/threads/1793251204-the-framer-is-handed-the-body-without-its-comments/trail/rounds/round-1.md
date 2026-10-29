# Review round 1: 1793251204-the-framer-is-handed-the-body-without-its-comments

target: f3bb1308 against origin/release/v0.24.2

## Findings

### 1. The phase 3 record says no run called `gh issue view`, and side A's run 0 did

severity: should
location: `seal/threads/1793251204-the-framer-is-handed-the-body-without-its-comments/trail/phases/phase-3.md:67-72`
evidence: executed `grep -o 'gh issue view 106[^"]\{0,80\}' <scratchpad>/1158/sides/baseline-framer-generated-page.raw/traces/000.jsonl`, `python3 -I <scratchpad>/1158-r1/test_tmp_traces.py <the four traces under <scratchpad>/1158/sides/>`
verdict: fixed 122b609b

The sealer reads this record against the traces. The paragraph's point is
that the framer took the comment line from the spawn rather than from
`gh`, and that point rests on the false sentence.

Claimed, at `phase-3.md:69-71`: "No run on either side called
`gh issue view`." Found: side A's run 0 (`traces/000.jsonl` of the baseline
side) ran `gh issue view 106 --json body,comments` in the same Bash call as
`gh release view`. The call failed and asked for `gh auth login`. That
run's final `frame/design.md` says so at the foot of its *Scope*: "The
framer's own `gh issue view 106` failed with `gh auth login` required, so
the body and its comment-free state are unverified by the framer, and the
orchestrator answers for them." The sentence holds for side A's run 1 and
for both side B runs.

The paragraph also leaves out what side B did with the line, and that is
the new step 4 at work. Both side B framers saw `gh release view` ask for
authentication and called no `gh issue view`. Both wrote the line into
`## Grounding` as the orchestrator's finding. Run 0 wrote "comments: none,
the orchestrator's finding, executed by it on 2026-10-14 ... so the framer
did not open the issue itself". Run 1 wrote "the orchestrator's finding,
`executed` on 2026-10-14 ... no comments". This is what the issue's first
Done-when line means by "the case shows it". No grader reads it, so this
record is the only place where the result is written down.

```markdown
**The comment line reached the frame.** Both side B runs wrote the spawn's
line into `## Grounding` as the orchestrator's finding, after
`gh release view` asked for `gh auth login`, and neither called
`gh issue view`. That is step 4 of this work's definition where `gh` cannot
read the issue. On side A, run 0 called `gh issue view 106 --json
body,comments`, which failed asking for `gh auth login`, and its
`frame/design.md` *Scope* names the orchestrator as the answerer for the
relayed body. Run 1 wrote the spawn's line into `## Grounding`: "the
orchestrator executed `gh issue view 106 --json body,comments` on
2026-10-14 and found no comments". No run wrote a row about the issue's
comments. Every run called `gh release view`, as step 4 of both definitions
asks.
```

answer: The finding holds. A `grep -o` over the four saved traces shows a Bash call running `gh issue view 106 --json body,comments 2>&1 | head -20` in side A's run 0 alone, which `gh auth login` refused. Both side B traces carry the orchestrator's finding on their `## Grounding` lines. `phase-3.md`'s paragraph is replaced in place with the record's text. No other file states that no run called `gh issue view`.

### 2. The closing memo opens by saying the sixth case pins the no-row half, which its own *Not verified* row and phase 3 contradict

severity: should
location: `seal/threads/1793251204-the-framer-is-handed-the-body-without-its-comments/gaps.md:5`
evidence: read `seal/threads/1793251204-the-framer-is-handed-the-body-without-its-comments/gaps.md:5`, `seal/threads/1793251204-the-framer-is-handed-the-body-without-its-comments/gaps.md:18`, `seal/threads/1793251204-the-framer-is-handed-the-body-without-its-comments/trail/phases/phase-3.md:35-60`
verdict: fixed 122b609b

The owner decides at the pull request whether `Closes #1158` stands. In
the closing memo, the first paragraph that reader meets says the opposite
of the row that asks the question.

Claimed, at `gaps.md:5`: "a sixth framer case pins that a question a run
answers is answered in `## Grounding` with no row left to a measurement."
Found: in the side file for `c48cd5e3`, `shape-no-measurement-row` passed
2 of 2. In the traces, neither old framer wrote an `a measurement` row.
Run 0 wrote no row. Run 1 wrote one `the work` row, about how a test
imports the generator.

The grader that separated the definitions is `shape-answers-by-run`. It
failed 2 of 2 on side A and passed 2 of 2 on side B. Like
`shape-answers-by-probe` in the sharp-s case, it reads where the answer is
written, not whether a row was left. It therefore pins the same half of
#1047's rule as before, on a second kind of question. The no-row half rests
on a grader that has never been seen red on any definition, as
`gaps.md:18` and `phase-3.md:35-53` say. This answers the handoff's
question: `shape-answers-by-run` is a second pin of the half
`rule-framer-sharp-s` already pins. It does not pin the half the issue's
last Done-when line asks for. The changelog's second bullet states the
result plainly already, and this sentence is the only record that does not.

```markdown
The framer was handed an issue's body without its comments and asked whether they changed the request; it is now handed the request whole. A sixth framer case, on a question only running the fixture's generator answers, tells the definitions apart by where the answer is written, in `## Grounding` labelled `executed`; its grader for a row left to a measurement passed on both definitions, so the no-row half of #1047's rule is still not seen pinned (*Not verified*).
```

answer: The finding holds. `gaps.md:5` contradicted its own row at `:18` and phase 3's side table, and the line is replaced in place with the record's sentence. Every other sentence on the same fact stands. `changelog.md`'s second bullet already says the row grader passed both runs before #1047 and is kept with nothing yet showing it red. `evals/scripts/rule_cases.py:27` describes what the sixth case's graders read, not what they were seen to separate. `frame/plan.md:21` and `routing.md:17` state the framer's and the orchestrator's intent before the build, and neither file is the crafter's to write.

## Confirmations

confirms: none
The framer cases are the generator's output. In a `git clone --no-local`
at `f3bb1308`, `python3 evals/scripts/rule_cases.py --out <scratch>/cases`
exited 0, and `diff -r` against `evals/behaviour/framer` exited 0
(executed). All six prompts, the sharp-s one among them
(`evals/behaviour/framer/rule-framer-sharp-s/prompt.md:5`), carry the
comment line before the body. That is the issue's second Done-when line.

confirms: none
The three new `Test_framer_case` cases are red against the old generator
and green at the target (executed). With `evals/scripts/rule_cases.py` at
`c1240e0b` in the clone, they failed with `AssertionError: loud-flag` and
twice with `KeyError: 'rule-framer-generated-page'`, and the two earlier
cases passed. At `f3bb1308`, six modules ran in one `bin/test` command:
the generator's test module, the evaluated-words module, the pasted-passage
module, the one-owner module, `tests/github/test_rules.py` and the evals
layout module. They exited 0 with 138 passed. `bin/seal layout --pairs`
names no pair for `tests/evals/test_rule_cases.py` (executed). Read
against its group, the page-case test adds the generator's run, the page
it changes and the revision taken from that run. Its section and label
checks repeat what the sharp-s case already holds for `grounding_answer`,
so the test adds coverage and is not a duplicate.

confirms: none
The side files say what phase 3 says (executed: a JSON read of both files
under `evals/`). Side A at `c48cd5e3` cost 5.0003 USD. On both runs,
`shape-answers-by-run` failed and every other grader passed. Side B at
`df003309` cost 4.5597 USD, and every grader passed on both runs. Both
files record `cut_short` false, the model `claude-fable-5-1`, Claude
version 2.1.312 and the suite at `df003309`. That makes 9.56 USD of the
15 USD cap. The trace readings in `phase-3.md:35-66` hold except for the
sentence in finding 1. Both old framers reached `Revision d8cac16f`, run
0 through its own `python3 -I -c` copy of the generator's logic and run 1
by running the script in a `$TMPDIR` copy, and neither wrote it on an
`executed` line of `## Grounding`. Both new framers ran the script in a
`git clone --no-local` under `$TMPDIR/1790000026-generated-page/frame/`
and wrote it there. No side B `frame/questions.md` holds a row.

confirms: none
The definition and the orchestration say what the frame asks (read).
`agents/framer.md:69-77` cites `skills/implement/orchestration.md`
*Orchestrator: the order inside a ticket* for what the line holds, and
does not restate it. It sends a line `gh` cannot open into `## Grounding`
and forbids a row about comments. `skills/implement/orchestration.md:47-50`
adds the sentence after the folding paragraph's last pinned phrase, and
the acts row at `:455` names the limit. The `## Rule changes` item's
`from:` text is the sentence at `docs/issues-and-milestones.md:297-300`
word for word. `git grep` for "spawns the framer", "framer is handed" and
"hands the framer" over `agents`, `skills`, `docs` and `templates` finds
only the new sentence, so no other sentence still states the old fact
(executed).

confirms: none
The crafter's handoff labels the full suite, the repository-wide lint and
the typecheck `unverified`, with the orchestrator as the answerer, and no
phase record claims any of them ran (read: `phase-1.md`, `phase-2.md` and
`phase-3.md`, each *The phase boundary*). The label is honest.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The issue's last Done-when line is not met. No case is seen red for leaving a row on the definition before #1047, and `shape-answers-by-run` pins the half the sharp-s case already pins (finding 2). Two things stay open: whether `Closes #1158` stands, and whether `shape-no-measurement-row` stays in the tree with no red on any definition (`frame/questions.md` Q2 (a) against Q2 (c)) | `seal/threads/1793251204-the-framer-is-handed-the-body-without-its-comments/gaps.md:18`, `evals/behaviour/framer/rule-framer-generated-page/graders/shape-no-measurement-row.md` | the owner, at the pull request |
| Step 4's branch where `gh` can read the issue: no paid run had `gh` authenticated, so no run opened the comments itself | `agents/framer.md:72-74` | the orchestrator, at each framer spawn (`gaps.md` S1 row) |
| The full suite, the repository-wide lint and the typecheck | the branch at `f3bb1308` | the orchestrator, at `seal gate` |

## Probes

| Command | Result |
|---|---|
| `python3 evals/scripts/rule_cases.py --out <scratch>/cases`, then `diff -r` of each agent's cases against `evals/behaviour/`, in a clone at `f3bb1308` | generator exit 0; framer, crafter and sealer diff exit 0; proofer differs only by the replay and seeded directories the generator does not write, none of which the branch touches |
| `bin/test` over the six modules named in the second confirmation, `-q` | exit 0, 138 passed |
| `git checkout c1240e0b -- evals/scripts/rule_cases.py` in the clone, then `bin/test tests/evals/test_rule_cases.py -q -p no:xdist -k Test_framer_case`, then the file restored to `f3bb1308` | exit 1: three failed, two passed; `git status --short` empty after the restore |
| `python3 -I test_tmp_traces.py` over the four saved traces, printing every Bash call and every Write and Edit of the frame files | side A run 0 ran `gh issue view 106`; no other run did; the readings in the third confirmation |
| `grep -o` for `gh issue view 106` over side A's `traces/000.jsonl` | one Bash call, one auth failure, and the frame's own sentence naming it |
| a JSON read of both committed side files | the costs, grader results, model and revisions in the third confirmation |
| `bin/seal layout --pairs`, searched for `test_rule_cases` | no pair (grep exit 1) |
