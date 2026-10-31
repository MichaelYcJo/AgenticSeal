# Review round 8: 1793411151-judgment-where-meaning-is-the-question

target: 27dcf020 against release/v0.26.0

This round reads phase 4 alone, the range `ce2bc211..27dcf020`, as
`frame/plan.md` *Phases* and the spawn prompt narrow it. The range holds
`7b70b22f` (the build: `skills/verify/scripts/deferral_check.py`,
`tests/skills/test_deferral_check.py`, `skills/verify/SKILL.md` *The answerer
has to exist*, `README.md` and `README.ko.md`) and `27dcf020` (its records).
It is the first finding round over phase 4, since a new phase in the plan
starts the count again. It reads `frame/design.md` *Scope* item 10, the two
`seal deferrals` scenarios of *User scenarios & acceptance*, the
`## Removes` row for the trigger reading, Table A's `seal deferrals` row and
the owner's comment 6489933002 on #1167. It reads nothing of phases 1, 2, 3
and 5.

Rounds 1 to 5 reviewed phases 1 and 2 and name no coordinate in
`deferral_check.py`, so no fact of this phase is carried from them; the
tool at `ce2bc211` was opened anew. Round 5 holds no finding, so nothing of
it is owed an answer here. Round 6 reads phase 3 at the same time and was
not read.

## Findings

### 1. `seal deferrals` prints a word from a YAML comment as a command line of its own where the comment holds U+2028 or one of seven other characters `str.splitlines` breaks at

severity: should
location: `skills/verify/scripts/deferral_check.py:94-109`, `tests/skills/test_deferral_check.py:115`, `seal/threads/1793411151-judgment-where-meaning-is-the-question/gaps.md:27-30`
evidence: executed `bin/test tests/skills/test_tmp_round7_probe.py -q -s -p no:xdist --basetemp=../basetemp`
verdict: fixed 7f69767f

Claimed, in `gaps.md` *Not done* and `trail/phases/phase-4.md` *Found and
not built*: `runners_in` still ends a line at U+2028; the frame keeps
`runners_in`; and the reader the trigger line sends to the file sees the
comment. Found: the probe wrote a workflow with `on: pull_request` and one
step, `- run: ./deploy.sh # see<U+2028>pytest`, which runs no tests. The
tool exited 0 with the header `tests: a runner in CI` and the line
`ci        .github/workflows/deploy.yml — pytest` (executed). The command
it printed is `pytest` alone. The class is every character
`str.splitlines` ends a line at and YAML 1.2 does not: U+2028, U+2029,
U+0085, U+000B, U+000C, U+001C, U+001D and U+001E. `runners_in` returned
`['pytest']` for each of the eight (executed). YAML ends a line at LF, CR
and CRLF only.

The stated limit does not hold, for three reasons:

- The trigger line sends the reader to the trigger, "open each ci file
  above for whether it runs before the change merges". Here the trigger is
  `on: pull_request`, so the reader's answer is yes. Nothing sends the
  reader to the step, and the tool has already printed `pytest` as the
  command it read.
- U+2028 shows as nothing, or as a line break, in most editors and in
  GitHub's file view. A reader who does open the step can see `pytest` on
  a line of its own.
- The frame's design for this tool is that it prints the command line it
  read and the reader judges it (`frame/design.md:53`, Table A's
  `seal deferrals` row). That works for a runner word after ` #` on the
  same line: the probe printed `echo hi # then pytest`, so the comment is
  in the output. It fails only where `splitlines` cut the line, because
  then the printed line is not the line YAML holds.

This is the owner's second misreading. Comment 6489933002 on #1167 says:
"`str.splitlines()` breaks a line at U+2028, so `on: pull_request` inside a
comment is read as a trigger and a push-only workflow answers."
`frame/design.md:53` closes it as moot because the scan that misread is
removed. The same mechanism still stands in `runners_in`, and `runners_in`
is now the only reading the exit code rests on. Reading lines at YAML's own
breaks is not a grammar rule added for one near miss. It is the format's
one definition of a line, and it closes all eight characters at once. The
repository's census already says `.splitlines(` ends a line where GFM does
not (`tests/censuses.py:688-691`). The exemption at `:97` names "YAML
keys", which this function does not read since phase 4 removed
`read_events`, and YAML does not break at these characters either. The
parametrised case at `tests/skills/test_deferral_check.py:115` holds
U+2028 on the `on:` line only. No case puts one inside a step (read).

The fix, in `skills/verify/scripts/deferral_check.py`. It assumes the text
was decoded as `read` decodes it, UTF-8 with `errors="replace"`, and has no
other precondition:

```python
# YAML 1.2 ends a line at LF, CR or CRLF and nowhere else. `str.splitlines`
# also ends one at U+2028, U+2029, U+0085, U+000B, U+000C and U+001C to
# U+001E, which YAML reads as text, so a runner word after one of them
# inside a comment would print as a command line of its own (#1167).
YAML_BREAK = re.compile(r"\r\n|\r|\n")


def runners_in(text, kind):
    """Command lines in `text` that run `kind`, deduped, in file order."""
    found = []
    for line in YAML_BREAK.split(text):
        stripped = line.strip().lstrip("-").strip()
        # exempt from heading_rule: a YAML or shell comment in a workflow's run lines
        if not stripped or stripped.startswith("#"):
            continue
        for pattern in RUNNERS[kind]:
            if re.search(pattern, stripped):
                cmd = re.sub(r"^(?:run|entry|script)\s*:\s*", "", stripped)
                if cmd not in found:
                    found.append(cmd)
                break
    return found
```

The case, in `tests/skills/test_deferral_check.py` under `Test_main`,
beside the parametrised trigger case. It is seen red against the tool at
`27dcf020`, which prints `pytest` alone:

```python
    @pytest.mark.parametrize(
        "char",
        ["\u2028", "\u2029", "\x85", "\x0b", "\x0c", "\x1c", "\x1d", "\x1e"],
        ids=["U+2028", "U+2029", "U+0085", "U+000B", "U+000C", "U+001C", "U+001D", "U+001E"],
    )
    def test_a_step_is_printed_whole_where_a_comment_holds_a_break_yaml_does_not_take(
        self, repo, char
    ):
        """#1167's second misreading: `str.splitlines` ends a line where YAML
        does not, which printed a word from a comment as a command. The step
        is printed as YAML holds it, comment and all, for its reader."""
        step = f"./deploy.sh # see{char}pytest"
        workflow(
            repo,
            "test.yml",
            "on: pull_request\njobs:\n  d:\n    steps:\n      - run: " + step + "\n",
        )
        r = run(["--kind", "tests", str(repo)])
        assert r.stdout == answered((TEST_YML, step)), r.stdout
```

The paragraph at `gaps.md:27-30` goes in the same commit, since the limit
it states no longer stands.

answer: The finding holds. The case was applied as written, and the splitter was not. Read against its grounds, the paste's `\r\n|\r|\n` has two dead arms. `read` opens each file in text mode with universal newlines, so CR and CRLF reach `runners_in` as LF. A first draft took the regex, and `seal mutate` showed it: dropping `\r`, or keeping `\n` alone, survived (executed). So `7f69767f` splits at `"\n"` alone, and the docstring says why: LF, CR and CRLF are YAML 1.2's line breaks and a Jenkinsfile's, `read` turns all three into LF, and `str.splitlines` also breaks at the eight characters. `test_a_line_ends_at_each_of_yamls_line_breaks` pins `read`'s half with a CRLF file and a CR file. It passes on both trees by design. Its mutant, `read` opened with `newline=""`, is red. `hooks/lib/blocks.py#gfm_lines` splits at the same three ends but was not reused, because its contract is markdown and record text. After the fix, the step still holds a runner word, so the tool still exits 0 and names the file. It now prints the whole step, `./deploy.sh # see<char>pytest`, so the reader sees the comment. That is the case's assertion. The eight rows were red at `2b7eef28` on a `ci` line of `pytest` alone (executed). `seal mutate` over the final splitter gave 5 red of 5 (executed): `splitlines` restored; a split at LF and U+2028; a split at LF and all eight characters; `read` without universal newlines; the stale `# exempt from splitlines: YAML keys` put back. The last is the census: it holds the LF split, and run alone it refuses the comment with "the exemption excuses nothing, because splitlines does not flag the line below it; remove the comment" (executed). The `gaps.md` paragraph left in the same commit. The narrow run then found that phase 4 had renamed `Test_main`'s one `test_accepts_` case, which `seal layout --check` refuses. `bce21a12` renames it back. Other statements, by `git grep` on "U+2028", "runners_in" and "splitlines" with "YAML", outside `docs/`: `trail/phases/phase-4.md`'s *Found and not built* paragraph, a phase record a fix pass does not edit; `frame/design.md` *Scope* item 10 and its `## Removes` row, which close both misreadings as moot with the scan; and `changelog.md:14`, which now holds as written. The hand-back names all three. Other instances of the cause, by the census's exemption lines that name YAML: `broad_gate.py#job_steps` and `payload_meter.py#frontmatter` read YAML through `str.splitlines`. Both read the plugin's own files, outside this finding and phase 4, and the hand-back names them.

## Confirmations

confirms: none
*Scope* item 10's removals hold. `read_events`, `block_entries`,
`continued`, `unquoted`, `ON_KEY`, `EVENT_NAME` and `PRE_MERGE_EVENTS`
appear nowhere outside the work item's records (executed, `git grep -n -E`
over `skills`, `tests`, `hooks`, `agents`, `docs`, `templates`, `.github`,
both READMEs and `CONTRIBUTING.md`). `inspect` builds its verdict from
`in_ci` alone and reads no event (`deferral_check.py:155-183`, read). The
module's cases compare the whole output, and none names an event (read).

confirms: none
The first reading holds: a pre-commit hook alone still exits 1. Claimed:
"nothing holds a runner" means no CI file holds one. Found:
`inspect` returns false when `in_ci` is empty, whatever `local_only` holds
(`deferral_check.py:178-183`, read). The case at
`tests/skills/test_deferral_check.py:170` pins exit 1 and the whole output
for a hook alone, and a mutant that counted the hook as CI went red
(executed, `seal mutate`). This reading follows the policy and not only the
account. `skills/verify/SKILL.md` *The answerer has to exist* says a
pre-commit hook "runs on the committer's machine alone" and answers no
deferral to CI, and `## Removes` removes the trigger outcomes and nothing
about the local hook. The tool at `ce2bc211` exited 1 for this shape too.
`frame/design.md:53` still says "exits 1 only where nothing holds a
runner", which, read word for word, gives the other answer. Folding that
sentence is a row of `## Not judged`.

confirms: none
The second reading holds. The tool at `ce2bc211` counted a GitLab,
CircleCI, Jenkins, Azure, Drone, Travis or Buildkite file as answering
because "these systems run every pipeline on push by default", which is a
reading of when the file runs. At `27dcf020` those files are `ci` lines
under the same trigger line, and the exit code for them is unchanged
(`deferral_check.py:155-163`, read). `tests/skills/test_deferral_check.py:194`
pins the whole output for `.gitlab-ci.yml` with the trigger line (read).
That is what item 10's "reads no trigger" asks.

confirms: none
The third reading holds. `README.md:260` and `README.ko.md:255` listed the
five outcomes, so contract rule 19 asks that they be rewritten in the
commit that removed the outcomes. Both now name the three outcomes and say
the trigger is the reader's to open (read). A sweep for the old outcome
words and for `seal deferrals` and `deferral_check` found no other
statement of the five outcomes outside the records (executed, `git grep -n
-i -E`). Two places cite the removed code. The replay case
`evals/behaviour/proofer/replay-1791382684-r2` checks out `7ef6abbf`
(`scaffold.sh:4-6`, read), and its grader and the matching
`evals/scripts/recurred_truths.json` entry cite that commit's file. Both
stand.

confirms: none
`skills/verify/SKILL.md:357-373` names three outcomes and says exit 1 means
no CI file holds a runner. It says exit 0 does not make the row true and
that the reader opens each named file for its trigger. The removed
sentence, "It reads an event's name and not its filters", stated a fact
of the trigger reading and leaves with it (read).

confirms: none
The phase's cases were seen red. This round checked out
`deferral_check.py` from `ce2bc211` in its clone and ran the module at
`27dcf020`: 10 failed and 6 passed, the split the phase record gives. The
tab-indented row and the U+2028 row were among the 10 (executed). Restored,
the module passed 16 of 16 (executed). `seal layout --pairs` names no pair
for the module (executed). Ruff check and format pass over the two changed
Python files, and `seal rules --check` holds 265 check lines in 54 rule
files (executed).

confirms: none
The two new `## Not verified` rows hold as written. The cases build the
printed path with `os.path.join` (`tests/skills/test_deferral_check.py:56`),
and the tool prints `os.path.relpath`, which uses the same separator on one
platform (read). The second row asks whether an agent writing an
`unverified` row opens each CI file the tool names. For this work item,
the one row that defers to CI is the Windows row. This round opened its
workflow: `.github/workflows/test.yml:3-12` triggers on `pull_request`,
and its Windows legs at `:105-108` run `pytest tests/` at `:158` (read).
So that deferral names an answerer that runs before the merge. The row
stays open for the later records that defer to CI.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and `seal gate` over the branch, labelled `unverified` in `gaps.md` | the branch at `27dcf020` | the orchestrator, by `seal gate --base release/v0.26.0 --record` after the rounds settle |
| The module on Windows, where the printed path takes a backslash | `tests/skills/test_deferral_check.py:56` | the orchestrator, at the Windows legs of the pull request's CI run |
| The crafter's `seal mutate` run (10 of 10 red) and its 94-module boundary run (4,541 passed), not re-run whole here; this round ran four mutants of its own | `skills/verify/scripts/deferral_check.py` and the modules the crafter named | the orchestrator's broad run |
| `frame/design.md:53` says the tool "exits 1 only where nothing holds a runner", and the build exits 1 where no CI file holds one, a reading this round confirms | `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:53` | the orchestrator, by folding the reading into the frame |
| Two arms of `runners_in` no case kills, the whole-line comment skip and the dedup, at `ce2bc211` as at `27dcf020`; the unit is outside phase 4's diff | `skills/verify/scripts/deferral_check.py:101`, `:105` | the orchestrator, to file or leave |
| The reason cell for `seal deferrals` says it "reads the pull request body and round records"; the tool reads CI files and `.pre-commit-config.yaml`; the file is outside phase 4's diff | `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py:64` | the orchestrator, to file or leave |
| Round 6 reads phase 3 at the same time and this record names none of its findings; a round 6 finding closed `fixed` or `rejected` is owed a `confirms:`, `reopens:` or `regression:` line in the record after round 6, which is the orchestrator's verifying round 7 | `trail/rounds/round-6.md` | the orchestrator, before it commits the records |
| Phases 1, 2, 3 and 5 and their Scope items, outside this round by `frame/plan.md` *Phases* | `frame/design.md` *Scope* items 1 to 9 and 11 to 14 | the rounds that read those phases |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_deferral_check.py -q -p no:xdist`, in a `git clone --no-local` at `27dcf020` under the scratchpad | 16 passed, exit 0 |
| The same, with `deferral_check.py` checked out from `ce2bc211`, then restored | 10 failed, 6 passed, exit 1 |
| `tests/skills/test_tmp_round7_probe.py`, one case, run once with `bin/test ... -q -s -p no:xdist --basetemp=../basetemp`, then deleted with its temp directory | `runners_in` returned `['pytest']` for each of the eight characters, and the YAML split returned the whole step; a same-line comment printed as `echo hi # then pytest`; a step name printed as `name: pytest later`; the tool over a `pull_request` workflow whose step is `./deploy.sh # see<U+2028>pytest` exited 0 with `ci ... — pytest` (finding 1) |
| `bin/seal mutate skills/verify/scripts/deferral_check.py` with four `--replace` pairs: the hook counted as CI, the trigger line dropped, the whole-line comment skip, the dedup | 2 red (the first two), 2 survived |
| The last two mutants with both files checked out from `ce2bc211`, then restored | 2 survived: the gap predates phase 4 |
| `uvx ruff check` and `uvx ruff format --check` over the two changed Python files | exit 0 and exit 0 |
| `bin/seal rules --check` | exit 0, 265 check lines in 54 rule files |
| `bin/seal layout --pairs`, filtered for `deferral` | no line |
