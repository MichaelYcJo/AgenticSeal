# Review round 1: 1793157214-the-pr-bodys-facts-come-from-the-records

target: 061d4e12 against release/v0.23.1

## Findings

### 1. A closing keyword in a copied record line closes an issue that no party claimed

severity: should
location: `skills/code-review/scripts/pr_body.py:388-412`, `tests/skills/test_pr_body.py:327`
evidence: executed `bin/seal pr-body <scratch>/h732/seal/specs/1791270162-the-worktree-guard-allows-a-listed-shape-and-asks-the-rest --body <scratch>/h732-body.md`, `python3 -I -c (close_issues_on_release.keywords_in over the part of <scratch>/h732-body.md above the heading)`
verdict: fixed 619ac510

The generated part is the text of the records. That text now reaches the
body, and two readers act on a closing keyword anywhere in the body:
GitHub, for a pull request into the default branch, and
`.github/scripts/close_issues_on_release.py`, which closes every issue a
merged feature body claims when the release ships. Before this change, the
orchestrator wrote every sentence of the body, so every claim in it was a
claim it chose to make.

The frame claims the opposite. `frame/questions.md:21-26` says "The `Closes`
line is the orchestrator's", and that `issue_claims_check.py` "reads the
whole body, so the line is read wherever it stands". The probe shows what
that leaves out. The changelog fragment at `3d78c220` of work item
`1791270162` holds the sentence `This closes #732, a git command inside a
string handed to a shell`. `seal pr-body` over that directory exited 0.
`keywords_in` over the part above `## Not from the records` returned
`['732']`. That claim happened to be intended. A record's prose does not
choose its words as a claim, though. For example, an `answer:` line saying
that a case `belongs to the work item that fixes #990` would close issue
990 when this pull request's release ships. Copied `answer:` paragraphs, `gaps.md`
rows and `frame/questions.md` rows are written as prose in the same way.

The generator already refuses a copied line that would break the body: a
copied line equal to `HEADING` (`pr_body.py:405-411`). A copied line that
makes a claim on the tracker is a second case of the same kind. The fix
refuses it at the record's line. The orchestrator then puts the number in
a code span in the record and writes its own `Closes` line under the heading.

```python
# skills/code-review/scripts/pr_body.py, inside the module's load `try:`,
# beside CHAIN and ROUTING. Precondition: the plugin ships from the
# repository root, so `.github/scripts/` stands three levels above HERE
# in a clone and in an installed copy alike (bin/test's comment says so).
    CLOSER = _load(
        os.path.join(HERE, "..", "..", "..", ".github", "scripts", "close_issues_on_release.py"),
        "agentic_closer_for_the_pr_body",
    )

# in _composed, after the `splits` refusal. `readable` blanks a fenced line,
# so a fenced example such as `Closes #88` in a record is not refused, and
# keywords_in masks the line's code spans, as GitHub does.
    claims = [
        (
            rel,
            line,
            f"claims #{number} with a closing keyword; a `Closes` line is "
            f"the orchestrator's, under `{HEADING}`",
        )
        for rel, line in (pair[1] for pair in above if pair[1])
        for number in CLOSER.keywords_in(READER.readable(texts[rel])[line - 1])
    ]
    if claims:
        raise Refused(claims)
```

The refusing case belongs in the parametrize of
`Test_compose::test_refuses_a_record_it_cannot_copy_faithfully`: a
changelog line reading `This closes #7.` is refused at `changelog.md:1`. The
same line with `#7` in a code span, or inside a fence, is accepted.

answer: fixed in 619ac510. `_composed` refuses a copied line where `close_issues_on_release.py#keywords_in` reads a closing keyword, at the record's line, beside the refusal of a copied line equal to `HEADING`. The module is loaded beside `chain_check.py`, and no second pattern was written. The line is read through the record's `readable` lines, so a fenced line and a code span claim nothing. The refusal names the issue, says that the `Closes` line is the orchestrator's alone and stands under `## Not from the records`, and says to put the number in a code span in the record. The new row of `Test_compose::test_refuses_a_record_it_cannot_copy_faithfully` holds a bare claim, a claim in a code span and a claim in a fence, and expects one cause, at `changelog.md:3`. It was seen red against the generator at 143fc233, which raised nothing. Run again over the changelog archived from 3d78c220, `--check` exits 1 at that changelog's line 42. The work item's `changelog.md` and a divergence row of `gaps.md` carry the change.

### 2. The sealer's withheld reason copies an absolute path into a committed `guarantee.md`

severity: should
location: `agents/sealer.md:66-71`, `skills/code-review/scripts/pr_body.py:487-489`, `tests/skills/test_pr_body.py:413`
evidence: executed `bin/seal pr-body <scratch>/owl/seal/threads/1793152332-the-stamps-mark-is-an-owl --body <scratch>/owl-tampered.md --check`
verdict: fixed 619ac510

Step 2 of `agents/sealer.md` says that on any exit but 0 the sealer writes a
withheld verdict whose reason is `<the first line the command printed>`. The
orchestrator commits that file (`skills/code-review/orchestration.md`
*Commit `guarantee.md`*). The first line `seal pr-body` prints names its
place through `_place` (`pr_body.py:487-489`). That function prints the body
file and the work item's directory as they were given on the command line.
`skills/code-review/orchestration.md:243` gives the body as
`<scratchpad>/<work-item-id>/pr-body.md`, which is an absolute path in the
session's temporary directory. So a `--check` refusal is the withhold this
check exists to produce, and its reason names a real machine path.

The probe confirmed it. With one changelog sentence changed in the body,
the command exited 1. Its first line opened `refused:` followed by the
absolute scratch path of the body file. That path holds this machine's
temporary directory and, inside the session's directory name, the owner's
home path written with dashes. `CONTRIBUTING.md` *House rules* keeps real
machine paths out of tracked files, because removing one means rewriting
history. The `real_identifiers` census (`tests/censuses.py:923`) matches
only a slash-separated home path under `/Users`, so it does not catch this dashed form. A withheld
`guarantee.md` is committed and can be pushed while the work item is being
built. A work item path given as an absolute path in the worktree prints in
the same way for a record's refusal.

The fix names each place without a path prefix: a record by its path under
the `seal/` root, and the body by its file name. The sealer's sentence can
then stay as it is.

```python
def _place(where, line, item, body):
    """Where a cause stands, with no machine path in it: the body file by
    its name, a record by its path under the `seal/` root. The sealer
    copies this line into a committed `guarantee.md`."""
    if where is None:
        path = os.path.basename(body)
    else:
        name = os.path.basename(os.path.normpath(os.path.abspath(item)))
        path = "/".join(p for p in (OPTIN.HOME, OPTIN.WORK_ITEMS, name, where) if p)
    return f"{path}:{line}" if line else path
```

Precondition: none at an OS boundary. `basename` and `abspath` read only
the strings they are given. `tests/skills/test_pr_body.py:413` pins
`refused: {body}:7: ` with the absolute temporary path and moves to
`refused: pr-body.md:7: `.

answer: fixed in 619ac510. `_place` names the body file by its name and a record by its path under the `seal/` root, as proposed, so the line the sealer copies into `guarantee.md` holds no machine path, and `agents/sealer.md` stays as it was. The pin at `tests/skills/test_pr_body.py:424` now reads `refused: pr-body.md:7: `. The new case `Test_main::test_refuses_naming_no_machine_path` hands the command absolute paths and expects `refused: seal/threads/<name>/trail/rounds/round-1.md:12: ` with no temporary path in the output. Both were seen red against the generator at 143fc233, which printed the absolute temporary path. Exit 2's line still prints `<item>` as it was given, or a module's installed path; the normal flow gives neither, and the module docstring states it as a limit. The work item's `changelog.md` says what the reason line now names.

### 3. The prose rule for the body's table says the phase records are already copied, and only their paths are

severity: should
location: `skills/writing-style/outside-the-review.md:63`
evidence: read `skills/writing-style/outside-the-review.md:63`, `skills/code-review/scripts/pr_body.py:276-292`, `skills/code-review/scripts/pr_body.py:295-333`
verdict: fixed 619ac510

The sentence the orchestrator reads before it writes its part of the body
says that the phase records, the round records, `trail/gate.md` and
`gaps.md`'s `## Not verified` "are already copied into the first part".
`_built` (`pr_body.py:276-292`) copies the plan's `## Phases` section and
writes one bullet per phase record naming its path. No line of a phase
record is copied. `_round` (`pr_body.py:295-333`) copies each round's
target line, the `## Findings` text before the first finding, each
finding's heading, and of each finding the lines labelled severity,
verdict, regression, reopens and answer. It does not copy the `## Confirmations`,
`## Not judged` or `## Probes` sections. The owl body this round generated
shows the same thing: under *How it was built* it holds the plan's table
and four lines naming `trail/phases/phase-1.md` to `phase-4.md`.

An orchestrator that trusts the sentence believes a reader of the body can
see the phase records' `executed` and `seen red` claims, but those claims
are not in the body. This work item's own `changelog.md` describes the copy
correctly ("the paths of the phase records"). The skill should agree with it.

```markdown
리뷰 체인을 거친 본문에서는 기록에 없는 검증만 이 표에 적는다. 앞부분에는 `frame/plan.md` 의 `## Phases` 표와 phase 기록의 경로, 회차 기록마다 `target:` 줄과 지적의 `severity:`·`verdict:`·`answer:` 줄, `trail/gate.md`, `gaps.md` 의 `## Not verified` 가 옮겨져 있다. phase 기록의 본문은 옮겨지지 않으므로, 그 기록의 사실이 필요하면 다시 쓰지 않고 그 경로를 적는다. 표에 남는 것은 광역 실행이 출력한 숫자, 회차가 끝난 뒤에 돌린 CI 결과처럼 어느 기록에도 없는 것이다.
```

answer: fixed in 619ac510. The sentence now says that the first part holds the plan's `## Phases` section and the phase records' paths, each round record's `target:` line, each finding's heading with its `severity:` line, `verdict:` line and `answer:` paragraph, the gate's table and `gaps.md`'s `## Not verified` section. It also says that a phase record's text is not copied, so a fact from one is named by its path. This is the proofer's text reworked rather than pasted: the middle dots it used as separators became words, the finding headings and the gate's table are named, and the sentence on the phase records follows `skills/code-review/orchestration.md`, where the orchestrator names a record's path rather than restating it.

## Confirmations

confirms: none
The generator copies text and does not compose it. `frame/design.md` S2 and
the docstring (`pr_body.py:15`) claim that it writes no count, summary or
rewording. This round ran `seal pr-body` over the owl thread, archived at
`74a680c1`, and over this thread. It then checked each non-blank line above
the heading against the thread's records with `grep -Fx`. Every line that is
not a record's line word for word is one of the `FIXED` templates
(`pr_body.py:120-165`) or a finding heading moved one level down, as
*Data & interfaces* specifies. No count, joined list or reworded heading
appears. Executed.

confirms: none
Phase 1 claims that it generated the owl body. The body this round
generated from `74a680c1` is byte for byte the body in the session's
scratchpad (`cmp` exit 0). Executed.

confirms: none
The check refuses an edited copy and leaves the orchestrator's part as it
was written. Over the owl thread, `--check` on the generated body with a
part of its own appended exited 0. With one changelog sentence changed,
it exited 1 at the body's line 9 and named `changelog.md:3`. A rewrite then
exited 0 and left the appended part as it was. Executed.

confirms: none
The orchestrator's order lets a body that follows it pass the check without
editing the generated part. `skills/code-review/orchestration.md:233-259`
gives this order: commit `trail/gate.md`, then run `seal pr-body`, then
spawn the sealer. It also runs the command again before every later spawn
of the sealer and before every `PATCH`. Four paths say so where they stand:
the merge from the base (`:184-189`), the platform repair (`:201-208`), a
repair touching only records or the orchestrator's part (`:278-285`) and a
repair outside the records (`:286-290`). The `undecided` answer and the
re-spawn after a stale guarantee rely on the bold general rule at `:255-258`.
The generated part does not copy `guarantee.md`, so committing the verdict
does not make the body stale. Read.

confirms: none
Step 2 of the sealer acts on every exit code, and the other parts of the
definition name the part the sealer may read. `agents/sealer.md:66-77`
withholds on any exit but 0 and reads the part above the heading as no
party's. Step 4 (`:84-89`) and *Never* (`:116-119`) name only the
orchestrator's part of the body. `git grep -n "list of changes" -- agents
skills` matches nothing, as plan row 2 asks. Read.

confirms: none
The heading has one spelling. The constant is `pr_body.py:92`. The sealer,
the orchestrator, `commit-pr-convention`, `outside-the-review.md` and
`templates/setup/config.md:87` cite it as
`skills/code-review/scripts/pr_body.py#HEADING`. The literal at
`templates/setup/config.md:145` is the no-row list item that
`_literal_strings` derives from the constant. `tests/skills/test_pr_body.py:348-353`
refuses the near miss `## Not from the records, really`, and `split` matches
only an exact line (`pr_body.py:429-432`). Read, and executed through the
`bin/test` run in `## Probes`.

confirms: none
Each part of the body follows its own language row.
`templates/setup/config.md:85-89`, `skills/commit-pr-convention/SKILL.md:65-67`
and `:181-188`, and `skills/writing-style/outside-the-review.md:21-29` all
give the same rule. The generated part is in `Record language` and nobody
translates it. The orchestrator's part is in
`Commit and pull request language`. Read.

confirms: none
Each departure in `gaps.md` was checked against the code. The two extra
fixed lines are at `pr_body.py:137-138`. The refusal of a second section is
at `:254-257`. Only a copied line equal to `HEADING` is refused, at
`:405-411`. Round files are numbered by `routing.round_number` at `:220`.
A missing body under `--check` exits 1, at `:465-468`. The check is the
first act of step 2, at `agents/sealer.md:66`. The fixture body is composed
before its placeholders are filled, and the filled body is held equal by
`tests/evals/test_rule_cases.py:204-221`. Read.

confirms: none
`gaps.md` *Not verified* names the Windows shards of the `tests` workflow as
the answerer for Windows behaviour. The prompt's CI run 40630397480 is at
head `061d4e12`. Every pytest job on Windows, macOS and Ubuntu, and the lint
job, ended `success`. Executed (`gh run view`).

No earlier round exists, so no fact is carried from one.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Issue #1044 lists the phase records as a source of the generated part, which "covers what changed, how it was verified". The frame copies the plan's `## Phases` table and only the paths of the phase records. `frame/questions.md:9-13` treats this as answered by the tree instead of asking it as a question. Whether this narrowing matches the owner's decision is the owner's question | `frame/design.md:186-195` | the owner |
| Whether the five paid sealer evals still grade as before, now that the sealer runs `seal pr-body --check` first | `frame/questions.md` Q4 | the owner, at the next paid run |
| The full suite, the repository-wide lint and the typecheck over this branch. This round's spawn prompt and contract rule 2 keep them out of the round | `trail/gate.md` | the orchestrator, through `seal gate` after the rounds settle |
| Whether the installed plugin's `seal` and the tree's `bin/seal` produce the same part when this repository's own sealer checks a body generated by the tree's command | `frame/plan.md:101-108` | the orchestrator of this work item, at the sealer's spawn |

## Probes

| Command | Result |
|---|---|
| `bin/seal pr-body <scratch>/owl/seal/threads/1793152332-the-stamps-mark-is-an-owl --body <scratch>/owl-body.md`, the thread archived from `74a680c1` | exit 0. `cmp` against the body phase 1 generated exited 0 |
| `bin/seal pr-body seal/threads/1793157214-the-pr-bodys-facts-come-from-the-records --body <scratch>/self-body.md` | exit 0. The fixed lines name the absent `trail/rounds/` and `trail/gate.md` |
| `grep -Fx` of each non-blank generated line against the item's records, under `bash -c`, for both bodies | the only lines that are not a record's are `FIXED` templates and demoted finding headings |
| `bin/seal pr-body <owl item> --body <scratch>/owl-body.md --check`, with a part of its own appended | exit 0 |
| the same `--check` on a copy with one changelog sentence changed | exit 1. One `refused:` line names the body's line 9 and `changelog.md:3`, and it opens with the body file's absolute path |
| `bin/seal pr-body <owl item> --body <scratch>/owl-body.md` again | exit 0. The appended part is unchanged |
| `bin/seal pr-body` over `3d78c220:seal/specs/1791270162-the-worktree-guard-allows-a-listed-shape-and-asks-the-rest/`, then `close_issues_on_release.keywords_in` over the part above the heading | exit 0, then `['732']` |
| `bin/test tests/skills/test_pr_body.py tests/behaviour/test_the_sealer_guarantees.py tests/evals/test_rule_cases.py -q` | exit 0, 48 passed |
| `bin/seal layout --check` | exit 0, 159 files read, 0 refused |
| `bin/seal rules --check` | exit 0, 265 check lines in 55 rule files hold |
| `gh run view 40630397480 -R MichaelYcJo/AgenticSeal --json headSha,conclusion,jobs` | head `061d4e12`, conclusion `success` on every job but `release-report`, which was skipped |
