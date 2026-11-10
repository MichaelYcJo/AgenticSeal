# Review round 2: 1794271938-follow-up-holds-seven-owner-questions

```seal
target: f16fc5ca0, fixes 84142a881..f16fc5ca0
```

This is the verifying round over round 1's fix pass. The code reviewed is the diff `84142a881..f16fc5ca0`: `a5e6c5038`, `3a0054d24`, the close commit `c09538c6b` and `f16fc5ca0`. Its one code change is `argv_words` in `tests/github/test_close_issues_on_release.py:84-127`. The work item's present-state records were each read whole at `f16fc5ca0`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`. No `pr.<lang>.md` stands, and `Commit and pull request language` is English. The three phase records were read for their coordinates. `seal/parity.json` is not declared.

Carried from round 1 and not re-established: the six-module narrow run (170 passed), the narrow ruff run, and the confirmations of *Scope* items 2 to 6, none of which the fix diff touches. Re-opened at round 1's coordinates rather than searched again: `skills/code-review/scripts/chain_check.py:362-381`, `:495-506` and `:2085-2093`, the fold's search at `8657297d5:tests/github/test_release_completeness_check.py:571-574`, and #1493's body. Round 1's tuple probe was written again from its `## Probes` row and widened (`## Probes`).

`frame/plan.md:51` cites the closer case's docstring at `:1099-1124`, and `:61` cites a `docs/releasing/` citation at `:1128`. Both resolve at `eccf1bcb7`, the commit the plan's *Technical context* names as the framer's read, and phase 1 moved both lines down. They are read as dated to that read and are no finding.

## Findings

### 1. `argv_words`' docstring still says the reader closes every argv a fold of the source closed, and a first word written `f"gh"` or `b"gh"` passes the converted cases that refused it at the base

```seal
severity: should
location: `tests/github/test_close_issues_on_release.py:109-113`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/changelog.md:4`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/pr.md:4`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:31`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:42`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/plan.md:50`
evidence: executed `bin/test tests/github/test_tmp_round2.py -p no:xdist -q -s -p no:cacheprovider` in a clone at `f16fc5ca0`; read `8657297d5:tests/github/test_release_completeness_check.py:571-574`, `tests/github/test_close_issues_on_release.py:96-127`
reopens: round-1#1
```

Why the earlier close does not hold: round 1's finding was that the converted cases lost a catch the fold had, and that the docstring claimed the reader was strictly stronger than the fold. The close reads `ast.Tuple`, which ends the tuple loss. It also rewrote the claim as "this reader closes every argv a fold of the source closed, a list, a tuple and call arguments, and more" (`:109-111`). That sentence is still false. Round 1 named the class as the literal containers an argv can sit in. The class is wider: it is every argv the fold matched and the reader drops, and that also runs over how a word is spelt.

Why it matters: the fold searched the whitespace-folded source for the quoted words `"gh", "issue", "<verb>"` (`8657297d5:tests/github/test_release_completeness_check.py:571-574`). A first word written `f"gh"` or `b"gh"` still holds the text `"gh"`, so the fold matched it. `argv_words` keeps only an `ast.Constant` whose value is a `str` (`:120-127`). An f-string parses to an `ast.JoinedStr`, and a bytes literal is a `Constant` whose value is `bytes`, so both words are dropped and the first three words no longer start with `gh`. The probe read `subprocess.run([f"gh", "issue", "edit", "1"])` and `subprocess.run([b"gh", "issue", "edit", "1"])`: the fold matched both, and `argv_words` matched neither. Both are working argvs. `f"gh"` is a `str` at run time, and `subprocess` on POSIX accepts a `bytes` argument. So `test_the_gate_writes_nothing` and `test_the_script_only_ever_creates_a_label_and_adds_one` pass a forbidden argv they refused at `8657297d5`. `frame/design.md` *Scope* item 1 says each converted case "keeps every claim it made", and `frame/plan.md:50` says they "hold the same claims".

The release note is not clear about this either. `changelog.md:4` says an argv "that takes one of its first three words from anything but a string literal" still passes. Python's reference calls an f-string a formatted string literal, so a reader of the release note takes `f"gh"` as caught.

The class, listed from Python's grammar of string prefixes, a closed set. With no prefix, `r` or `u`, a word is a `str` constant and is read. With `f` or `fr`, it is a `JoinedStr`. With `b` or `br`, it is a `bytes` constant. Both are dropped, in either letter case. A `t` prefix gives no `str` and is no working argv, and the clone's interpreter is 3.13. Only the first word matters for the fold. Its pattern opens with `"gh"`, so a prefix on the verb broke the fold's match too, and the probe shows the fold missing `f"edit"`. Implicit concatenation, `"g" "h"`, is read by `argv_words` and was missed by the fold. So the lost catch is a first word with an `f` or `b` prefix, and nothing else.

The fix below changes words, not code. No release script writes a prefixed word. Reading `JoinedStr` and `bytes` would add two branches, and finding 2 shows that such a branch owes a case written for it. The fix pass may close it in code instead, and then the docstring sentence stands as it is.

The docstring's last paragraph, `tests/github/test_close_issues_on_release.py:109-113`:

```python
    So this reader closes every layout of an argv that a fold of the source
    closed, in a list, a tuple or call arguments, and more. It drops every
    word that is not a `str` constant. A name is dropped, and the fold was
    blind to a name too. A first word written as an f-string or a bytes
    literal, `f"gh"` or `b"gh"`, is dropped as well, and the fold matched it,
    since its text still holds `"gh"`. Closing the name means resolving
    module-level names before comparing, which is a different checker with
    its own false-positive argument to make. #1493 left the name open, and
    the prefixed first word with it, since no release script writes one.
```

`changelog.md:4`, the last sentence of the *Changed* second item, and `pr.md:4`, which quotes it, are rewritten together:

```markdown
An argv that takes one of its first three words from anything but a plain string literal, such as a module-level name, an f-string or a bytes literal, still passes all three, and `argv_words`' docstring says so.
```

This snippet does not reach three frame sentences, and the orchestrator owes them. They are `frame/design.md:31`, *Scope* item 1's "keeps every claim it made", `frame/design.md:42`, the *Out* item that calls the escape "a name in one of an argv's first three positions", and `frame/plan.md:50`, "hold the same claims". Each should name the prefixed first word as a claim the conversion gave up.

```seal
verdict: fixed af63472e5
answer: The words changed and the reader did not, as the orchestrator directed. `argv_words`' docstring (`tests/github/test_close_issues_on_release.py:84-120`) now says the reader reads the plain string literals of a list, a tuple or a call's positional arguments, and nothing else. It says that an argv writing one of its first three words as a module-level name, an f-string or a bytes literal passes every case that reads through it, and that the fold matched `f"gh"` and `b"gh"` where this reader drops them. It no longer claims to close every argv the fold closed. The round's docstring snippet was read against the code and written in my own words. Two sentences outside it read an f-string as caught, so they changed too: the first line now says "plain string-literal words", and the middle paragraph says "a word that is not a plain string literal" and "`ast.Constant` values of type `str`". The parse was checked directly: `f"gh"` is an `ast.JoinedStr` and `b"gh"` is a `Constant` holding `bytes` (executed, `python3 -I -c` over `ast.parse`, interpreter 3.15.0). The changelog's *Changed* second item takes the round's sentence word for word (`changelog.md:4`). The three modules pass, 113 passed (executed). `frame/design.md:68` quotes the old first line of the docstring, and `pr.md:4` quotes the old changelog sentence. Both are for the orchestrator to fold.
```

### 2. `argv_words`' `ast.Tuple` half has no case, so removing it leaves every module green and round 1's defect can come back unseen

```seal
severity: should
location: `tests/github/test_close_issues_on_release.py:116-118`, `tests/github/test_close_issues_on_release.py:1077`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/gaps.md:12`
evidence: executed `bin/test tests/github/test_close_issues_on_release.py tests/github/test_release_completeness_check.py tests/github/test_label_merged_on_release_branch.py -q -p no:cacheprovider` in a clone at `f16fc5ca0`, before and after removing `ast.Tuple` at `:117`; read `seal/threads/1794271938-follow-up-holds-seven-owner-questions/gaps.md:12`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/plan.md:44`, `skills/verify/SKILL.md` *The narrow command still has to be able to fail*
regression: round-1#1
```

The unit is the `ast.Tuple` half of `argv_words`, `tests/github/test_close_issues_on_release.py:116-118`, which `3a0054d24` added. Phase 1's plan row (`frame/plan.md:44`) verifies the reader by plants that are reverted after their run, and `frame/design.md` *Scope* item 1 now rests on this half for the tuple claim. The fix showed the half red with six plants and reverted them. So the defect came from taking the plan row's plant-and-revert as the whole verification of a branch that no script exercises.

Why it matters: with `ast.Tuple` removed at `:117`, the three modules read 112 passed, exactly as they do at the target (executed). This is the crafter's own `SURVIVED`, reproduced. The change is the *Logic* row of `skills/verify/SKILL.md` *The narrow command still has to be able to fail*: the tests covering the file must be able to fail, and here none can. Round 1's finding 1 was that a reader of lists alone passes a tuple argv. Without a case, the next edit of `argv_words` can drop the half, and that finding returns with every case green.

`gaps.md:12` gives two grounds for leaving it. First, "a case would need a source written for it". That source is one line, and the case is below. Second, "the finding asks for the reader and its plants, not a case". Round 1's snippet did name no case. That was round 1's omission, and it does not limit what the change owes. The precedent `gaps.md:10` cites does not carry over. The `isinstance(a.value, str)` filter came over unchanged, so it is a guard of code the diff did not change. The `ast.Tuple` half is code the fix changed, and a *Scope* item states the behaviour it holds. That makes it the *Regression test* row's `should` in `skills/code-review/SKILL.md` *Probes and regression tests*.

The case goes in `Test_module`, after the closer's case, which ends at `tests/github/test_close_issues_on_release.py:1238`. It is shown red with only `ast.Tuple` removed at `:117` (contract rule 15). The probe shows both sources read with the half and missed without it.

```python
    def test_argv_words_reads_a_tuple_argv_as_it_reads_a_list(self):
        """No release script writes a tuple argv, so only a source written here
        holds the half of `argv_words` that reads one. A fold of the source
        refused both spellings below, and a reader of lists alone passed both,
        measured in round 1 of #1493."""
        for source in (
            'subprocess.run(("gh", "issue", "edit", str(n)))',
            'run(*("gh", "issue", "edit", str(n)))',
        ):
            prefixes = [words[:3] for words in argv_words(source)]
            assert ["gh", "issue", "edit"] in prefixes, source
```

`gaps.md:12` then states a gap that no longer stands, and it leaves in the same commit.

```seal
verdict: fixed af63472e5
answer: The round's case was added word for word as `Test_module::test_argv_words_reads_a_tuple_argv_as_it_reads_a_list` (`tests/github/test_close_issues_on_release.py:1246-1256`), after the closer's case. It was shown red with only the `ast.Tuple` half removed: `seal mutate` replaced `isinstance(node, (ast.List, ast.Tuple))` with `isinstance(node, ast.List)`, and the case failed on its assertion for `subprocess.run(("gh", "issue", "edit", str(n)))`, with `argv_words` returning `[[], []]`. The verdict was red, exit 0, and the tree was clean after the restore (executed). The `gaps.md` *Not done* paragraph on the missing case left in the same commit. The paragraph on the `isinstance(a.value, str)` filter stays, because the new case does not exercise that filter. The three modules pass, 113 passed, and `bin/seal layout --pairs` names no pair involving the new case (executed). `frame/design.md` *Removes* closes with "This work adds one assertion to an existing case", and HEAD now also adds this case. That sentence is for the orchestrator to fold.
```

## Confirmations

```seal
confirms: round-1#2
```
What holds: `changelog.md:9` carries round 1's snippet word for word. #1493's *Decided* names the owner for row 2 and "orchestrator's default, reported to the owner" for row 5 (executed, `gh issue view 1493`). `frame/questions.md:16` and `routing.md:21` now say the same. The `--worktree` sentence holds at the target (read). `tracked_declarations` (`skills/code-review/scripts/chain_check.py:1875-1891`) lists declarations through `git ls-tree -r HEAD`, so a root under the common git directory is never among them. Where none matches, `:1915-1923` reports local mode and says the check examined nothing. `pr.md:7` and `pr.md:8` quote the rewritten sentences.

What matched: the close's claims about spreads (executed, the probe). A tuple spread whole, `run(*("gh", "issue", "edit", "1"))`, is read by `argv_words` at the target and missed by a reader of lists alone. A mixed spread, `run("gh", *("issue", "edit", "1"))`, is missed by both `argv_words` and the fold, as the close says. The six `seal mutate` plants the close names were not re-run. The probe shows the same reading on source text.

What matched: the three converted modules pass at the target, 112 passed, exit 0 (executed).

What matched: each of the ten quotes in `pr.md` stands word for word, with whitespace runs collapsed, in the source its coordinate names (executed, a `python3 -I` read of `pr.md`, `changelog.md` and `frame/plan.md`).

What matched: `frame/design.md:67-72` states the docstring's first sentence and the three node kinds as `argv_words` holds them at `:84-127` (read). *Scope* item 8 and the *Removes* first row put the measurements in #1493's body, which the issue's *Done when* allows: "move to the issue body or the commit message where the row is closed" (executed, `gh issue view 1493`).

What matched: `gaps.md:6` names fix pass 1's close blocks as where its runs are recorded, and they are there (read, `trail/rounds/round-1.md:51` and `:82`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite and the repository-wide lint. They are `unverified` in this round, and `gaps.md:6` names the orchestrator's run and `trail/gate.md` as its record | `seal/config.json` `Broad gate` | the orchestrator |
| `changelog.md:9` says the measurements "are in #1493's body". At this round the body holds no measurements (executed, `gh issue view 1493`), and the spawn says the text is appended when the pull request opens. The sentence is true from that moment | `seal/threads/1794271938-follow-up-holds-seven-owner-questions/changelog.md:9`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:84` | the orchestrator, who appends the text, and the sealer, who reads the body |
| The two `tests/test_conftest.py::Test_census_case` failures. The spawn says they fail on the base too and are filed as #1498, and this round did not run them | `tests/test_conftest.py`, `tests/censuses.py` | the orchestrator, through #1498 |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_tmp_round2.py -p no:xdist -q -s -p no:cacheprovider`, in a `git clone --no-local` at `f16fc5ca0` under the round's scratch directory. The probe file was deleted after its one run | 1 passed. It printed, as `argv_words` / a reader of lists alone / the fold: plain list True/True/True; tuple True/False/True; whole spread tuple True/False/True; mixed spread False/False/False; f-string first word False/False/True; f-string verb False/False/False; bytes first word False/False/True; raw string True/True/True; implicit concatenation True/True/False |
| `bin/test tests/github/test_close_issues_on_release.py tests/github/test_release_completeness_check.py tests/github/test_label_merged_on_release_branch.py -q -p no:cacheprovider`, in the same clone | exit 0, 112 passed |
| The same command after `ast.Tuple` was removed at `tests/github/test_close_issues_on_release.py:117` through the `Edit` tool, restored with `git checkout` afterwards | exit 0, 112 passed: no case pins the half |
| `gh issue view 1493 --json state,body,comments` | open, no comments. *Decided* names row 2 as the owner's and row 5 as the orchestrator's default reported to the owner. The body holds no measurements yet |
