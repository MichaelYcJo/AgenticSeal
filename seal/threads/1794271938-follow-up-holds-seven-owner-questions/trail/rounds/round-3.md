# Review round 3: 1794271938-follow-up-holds-seven-owner-questions

```seal
target: 96b61d748, fixes 8a914e9ae..96b61d748
```

This is the verifying round over round 2's fix pass. The code reviewed is the diff `8a914e9ae..96b61d748`: `b0c3ab23d`, `af63472e5`, the close commit `2a079203a`, `b76f00614` and `96b61d748`. Its one code change is in `tests/github/test_close_issues_on_release.py`: the docstring of `argv_words` (`:84-120`) and the new case `Test_module::test_argv_words_reads_a_tuple_argv_as_it_reads_a_list` (`:1246-1256`). The work item's present-state records were each read whole at `96b61d748`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`. No `pr.<lang>.md` stands, and `Commit and pull request language` is English. The three phase records were read for their coordinates. `seal/parity.json` is not declared.

Carried from rounds 1 and 2 and not re-established: the confirmations of *Scope* items 2 to 6, which the fix diff does not touch, and round 2's probe table of how `argv_words`, a reader of lists alone and the fold read nine spellings. Re-opened at round 2's coordinates rather than searched again: `8657297d5:tests/github/test_label_merged_on_release_branch.py:390-412`, the fold this work removed, and #1493's body. Round 2's two `evidence: executed` lines were run again: the three modules, and the same modules with `ast.Tuple` removed (`## Probes`).

The orchestrator's direction for this round was that the escapes are stated, not closed. This round does not argue for closing any escape. Both findings are about whether the text states the escapes truly.

`frame/plan.md:15`, *What breaks in six months*, names only the name escape. It stands in *Technical context*, which is dated to `eccf1bcb7`, the framer's read, and the target does not contradict it, so it is no finding. The fix pass removed a `## Not done` paragraph of `gaps.md` in `af63472e5`. It was a decision not to write a case, and the case now stands, so contract rule 19 asks for its removal. The `closed` marking that `skills/implement/SKILL.md` *4. The closing memo* requires covers rows of `## Not verified`, and no such row left.

## Findings

### 1. `argv_words`' docstring and the release note say an argv written with a name, an f-string or a bytes word passes every case, and a required argv so written turns its case red

```seal
severity: should
location: `tests/github/test_close_issues_on_release.py:109-119`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/changelog.md:4`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/pr.md:4`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:31`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/plan.md:50`
evidence: executed `python3 -B -c` in `tests/github/` of a clone at `96b61d748`, loading `argv_words` from the module's source and reading four one-line sources (`## Probes`); read `tests/github/test_label_merged_on_release_branch.py:400-402`, `tests/github/test_close_issues_on_release.py:1199-1231`, `8657297d5:tests/github/test_label_merged_on_release_branch.py:397-399`
regression: round-2#1
```

The unit is the last paragraph of `argv_words`' docstring, `tests/github/test_close_issues_on_release.py:109-119`, and the last sentence of `changelog.md`'s *Changed* second item, both rewritten by `af63472e5`. Phase 1's plan row (`frame/plan.md:44`) verifies the converted cases with forbidden-argv plants and with required argvs removed, and `frame/design.md` *Scope* item 1 lists both kinds of claim. The fix stated the escape for the forbidden claims alone and wrote it as true of every case. The defect came from round 2's finding 1, which framed the class as the catch the fold lost and did not name the red the parse adds.

Claimed: the docstring says that an argv writing one of its first three words "as a module-level name, an f-string or a bytes literal among others, passes every case that reads through it" (`:110-112`). The changelog says such an argv "still passes all three" (`changelog.md:4`), and `pr.md:4` quotes that sentence.

Found: the cases make two kinds of claim. A forbidden argv must be absent, and for that kind the sentence holds. A required argv must be present: the label case asserts `["gh", "label", "create"] in prefixes` (`tests/github/test_label_merged_on_release_branch.py:402`), and the closer's case asserts exactly one `gh issue close` and exactly one `gh issue edit` (`tests/github/test_close_issues_on_release.py:1219` and `:1234`). A required argv written that way does not pass. The parse does not see it, the case reads it as missing, and the case goes red with "the script stopped creating" while the script still creates. The probe read `run(f"gh", "label", "create", name)` and `run(b"gh", "label", "create", name)`: `argv_words` gave no `gh label create` prefix for either, and the fold at `8657297d5:tests/github/test_label_merged_on_release_branch.py:398` matched both. So for an f-string or bytes first word, the label case is red at the target where it was green at the base. A name was missed by the fold as well (`GH = "gh"` then `attempt(GH, "issue", "close", ...)`, missed by both), so the name's red is not new. `--add-label` is read from any word of any argv (`:403`), so a prefixed first word does not hide it.

Why it matters: the core calls a script that answers "these differ" where the meaning is the same the worst result it can give (`skills/core/SKILL.md` *The first value*). The text now records the false green and says nothing of this false red. An agent that moves the label script's `gh label create` onto a name or an f-string reads "passes every case" and then meets a red whose message says the script stopped creating. A reader of the release note takes "still passes all three" as the whole effect. No release script writes such a word today (executed, an `ast` scan of the three scripts: no module-level constant equal to `gh`, `issue` or `label`, no bytes constant, and the only f-strings that open with `gh` are error messages), so no case is red at the target.

The class is the claims of the three cases, a closed set, listed by reading each case whole. Absence claims: the five or six forbidden verbs in each case and `gh label delete`. Presence claims: `gh issue close` and `gh issue edit` in the closer's case, `gh label create` and `--add-label` in the label case. The gate case has no presence claim. The first-three-words escape reaches every presence claim except `--add-label`.

The docstring's last paragraph, `tests/github/test_close_issues_on_release.py:109-119`:

```python
    So this reader reads the plain string literals of a list, a tuple or a
    call's positional arguments, and nothing else. An argv that writes one of
    its first three words another way, as a module-level name, an f-string or
    a bytes literal among others, is invisible to every case that reads
    through it. A forbidden argv so written passes. A required one, such as
    the closer's `gh issue close` or the sibling's `gh label create`, reads
    as missing, and its case goes red while the script still makes the call.
    A fold of the source was blind to a name too. It matched a first word
    written `f"gh"` or `b"gh"`, since that text still holds `"gh"`, and this
    reader drops both, measured in rounds 2 and 3 of #1493. Closing the name
    means resolving module-level names before comparing, which is a different
    checker with its own false-positive argument to make. #1493 left the name
    open, and the f-string and bytes words with it, since no release script
    writes one.
```

`changelog.md:4`, the last sentence of the *Changed* second item, and `pr.md:4`, which quotes it, are rewritten together:

```markdown
An argv that takes one of its first three words from anything but a plain string literal, such as a module-level name, an f-string or a bytes literal, is invisible to all three: a forbidden one still passes, and a required one reads as missing and turns its case red. `argv_words`' docstring says so.
```

`pr.md:4` then quotes the first of those two sentences. This snippet does not reach two frame sentences, and the orchestrator owes them. `frame/design.md:31` says such an argv "passes the parse where the fold refused some of them", and `frame/plan.md:50` says an f-string or bytes first word "now passes". Each should add that a required argv so written reads as missing, and that for an f-string or bytes first word this is a red the fold did not give.

### 2. The frame's *Out* item says the issue keeps the f-string and bytes escapes open and that closing them needs a name-resolving checker, and neither holds

```seal
severity: should
location: `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:42`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/plan.md:69-71`
evidence: executed `gh issue view 1493 --json state,body,comments`; read `seal/threads/1794271938-follow-up-holds-seven-owner-questions/trail/rounds/round-2.md:30-32`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/trail/rounds/round-2.md:58`, `tests/github/test_close_issues_on_release.py:121-133`
regression: round-2#1
```

The unit is the first *Out* item of `frame/design.md`, line 42, which `b0c3ab23d` rewrote. Phase 1's plan row (`frame/plan.md:44`) and *Scope* item 1 build the reader for plain string literals, and the *Out* item is where the frame says why the rest stays open. The fold widened the item from the name to three escapes and kept the grounds that were written for the name alone. The defect came from that fold.

Claimed: "Closing the escapes of the `ast` reader: a module-level name, an f-string or a bytes literal in one of an argv's first three positions. The issue keeps it open, and closing it is a checker that resolves module-level names, with its own false-positive argument."

Found: #1493's row 7 says "The constant-valued escape stays open" and names nothing else (executed, `gh issue view 1493`; the issue is open and has no comments). The f-string and bytes words were found in round 2 of this review (`trail/rounds/round-2.md:30`), after the issue was written, so the issue does not keep them open. Closing them needs no name resolution. `argv_words` keeps a word where it is an `ast.Constant` of type `str` (`tests/github/test_close_issues_on_release.py:130`). Reading an `ast.JoinedStr` whose parts are all constants, and a `bytes` constant, adds two branches to that filter, as round 2 said (`trail/rounds/round-2.md:32`). The decision to leave them open was the orchestrator's: round 2's close of finding 1 says "as the orchestrator directed" (`trail/rounds/round-2.md:58`), and this round's spawn says the frame now records it. The frame records it under grounds that do not hold, and `frame/plan.md` *Judgments of the run* (`:69-71`) holds no row for it.

Why it matters: the sealer reads every party's account against the issue. It will find that the issue names one escape where the frame says it keeps three open, and it will find no recorded judgment for the other two. `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* asks for the decision, its grounds and the document it was judged against in the work item's records.

`frame/design.md:42`:

```markdown
- Closing the escapes of the `ast` reader: a module-level name, an f-string or a bytes literal in one of an argv's first three positions. The issue keeps the name open, and closing it is a checker that resolves module-level names, with its own false-positive argument. The f-string and bytes words were found in round 2 of the review, after the issue was written, and stay open by the orchestrator's judgment (`frame/plan.md` *Judgments of the run*).
```

A row for `frame/plan.md` *Judgments of the run*. The grounds are round 2's. The orchestrator confirms the *Judged against* cell, which names the document this round reads the decision against:

```markdown
| 2026-11-10 | The f-string and bytes first words `argv_words` drops stay open, and its docstring and the changelog state them | No release script writes one, and reading `ast.JoinedStr` and `bytes` adds two branches, each owing a case written for it, as the tuple half did (`trail/rounds/round-2.md`, findings 1 and 2) | `skills/core/SKILL.md` *The rule a mechanism is kept against* |
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: the docstring no longer says the reader closes every argv the fold closed. `tests/github/test_close_issues_on_release.py:109-119` says the reader reads plain string literals and nothing else, and that the fold matched `f"gh"` and `b"gh"` where the reader drops them. The first line (`:85`) says "plain string-literal words", and the middle paragraph says "`ast.Constant` values of type `str`" (`:100-101`), which is what `:130` keeps (read). `changelog.md:4` says "a plain string literal" and names the f-string and the bytes literal. `pr.md:4` quotes it word for word (executed, below). The three frame sentences round 2 said the orchestrator owed now name the prefixed first word: `frame/design.md:31`, `:42` and `frame/plan.md:50` (read). The probe confirms the docstring's measured claim again for `f"gh"` and `b"gh"` as first words (executed). Findings 1 and 2 above are new defects in the text the fix wrote. They are not the claim round 2 found false.

```seal
confirms: round-2#2
```
What holds: the case `test_argv_words_reads_a_tuple_argv_as_it_reads_a_list` stands at `tests/github/test_close_issues_on_release.py:1246-1256`, as round 2's snippet gave it. With `ast.Tuple` removed at `:123` through the `Edit` tool, and nothing else changed, the three modules read 1 failed, 112 passed. The one failure is this case, at `:1256`, on `subprocess.run(("gh", "issue", "edit", str(n)))` (executed). Restored, they read 113 passed (executed). So the case pins the tuple half, and contract rule 15's red, which the close showed with `seal mutate`, is reproduced. The `gaps.md` paragraph that stood on the missing case left in `af63472e5`. `bin/seal layout --pairs` names no pair involving the new case (executed). No other case of the three modules reads a tuple argv (read), so the case covers what its group did not.

What matched: `frame/design.md:68-69` gives the docstring's first line as `:85-87` holds it (read). The *Removes* closing sentence (`frame/design.md:114`) and the judgment row's grounds (`frame/plan.md:71`) both say the work adds one assertion and one case. The branch adds the `offered` assertion and the tuple case, and its other case changes replace the fold's assertions in place (read, `git diff 8a914e9ae..96b61d748`, and rounds 1 and 2 for the earlier range).

What matched: each of the ten quotes in `pr.md` stands word for word, with whitespace runs collapsed, in the source its coordinate names (executed, a `python3 -I` read of `pr.md`, `changelog.md` and `frame/plan.md`).

What matched: the docstring's "no release script writes one" holds at the target. An `ast` scan of the three scripts found no module-level constant equal to `gh`, `issue` or `label`, no bytes constant, and no argv whose first word is an f-string (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite and the repository-wide lint. They are `unverified` in this round, and `gaps.md:6` names the orchestrator's run and `trail/gate.md` as its record | `seal/config.json` `Broad gate` | the orchestrator |
| `changelog.md:9` says the measurements "are in #1493's body". At this round the body holds none (executed, `gh issue view 1493`), and the spawn says the text is appended when the pull request opens. The sentence is true from that moment | `seal/threads/1794271938-follow-up-holds-seven-owner-questions/changelog.md:9`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:84` | the orchestrator, who appends the text, and the sealer, who reads the body |
| The two `tests/test_conftest.py::Test_census_case` failures. The spawn says they fail on the base too and are filed as #1498. This round did not run them | `tests/test_conftest.py`, `tests/censuses.py` | the orchestrator, through #1498 |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_close_issues_on_release.py tests/github/test_release_completeness_check.py tests/github/test_label_merged_on_release_branch.py -q -p no:cacheprovider`, in a `git clone --no-local` at `96b61d748` under the round's scratch directory | exit 0, 113 passed |
| The same command after `(ast.List, ast.Tuple)` was replaced with `ast.List` at `tests/github/test_close_issues_on_release.py:123` through the `Edit` tool, restored with `git checkout` afterwards | exit 1, 1 failed, 112 passed. The failure is `Test_module::test_argv_words_reads_a_tuple_argv_as_it_reads_a_list` at `:1256` |
| `python3 -B -c` in the clone's `tests/github/`, compiling `argv_words` from the module's source and reading four sources, each also folded and searched as the base's label case searched | `run("gh", "label", "create", name)`: read, fold matched. `run(f"gh", "label", "create", name)`: not read, fold matched. `run(b"gh", "label", "create", name)`: not read, fold matched. `GH = "gh"` then `attempt(GH, "issue", "close", str(issue))`: not read, fold not matched |
| `python3 -B -I -c` over the three scripts in `.github/scripts/`, an `ast` scan for module-level constants equal to `gh`, `issue` or `label`, for bytes constants, and for f-strings opening with `gh` | no constants, no bytes. Three f-strings in `close_issues_on_release.py`, each an error message, none an argv word |
| `bin/seal layout --pairs` in the clone | exit 0, 131 lines, none naming the new case |
| `gh issue view 1493 --json state,body,comments` | open, no comments. Row 7 says "The constant-valued escape stays open" and names no other escape. The body holds no measurements yet |
