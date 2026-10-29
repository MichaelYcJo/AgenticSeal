# Review round 2: 1793240967-the-worktree-guard-was-never-weighed

target: f8447b30, fixes b30855a5..f8447b30

This is a verifying round. The diff read is `b30855a5..f8447b30`: the fix
commits 2bfa6459 and fddec67a (finding 1) and a82da960 (finding 2); e5c4c868,
the round-1 record, whose diff changes the two verdict lines and the two
answer lines and nothing else (read); 76c77c74, the frame fold; and
f8447b30, the `gaps.md` update. The fix pass's two answers, the commit
messages and the spawn prompt were read as claims. Each claim below says what
was claimed and what was found.

Carried from round 1 and not re-established: the merge base 1e82fd0a; the
17 `check:` lines of `docs/worktree-guard-spec.md` that name the five test
files this work deletes; `hooks/implementer-notice.py:112-116` as the one
reader of `hooks/lib/cmdline.py`'s outputs; `seal/parity.md` not declared,
so this round writes no `original:` line; no `Record language` row in
`seal/config.md`, so the record is in English. Re-established this round:
each close, by re-running round 1's `executed` lines in a
`git clone --no-local` at f8447b30.

## Findings

### 1. `seal rules --check` is described as reading the policy in force, and it excuses one shape of pending change under one root

severity: should
location: `.github/scripts/rules.py:28-33`, `skills/settle/scripts/rule_changes.py:253-264`, `skills/settle/SKILL.md:125-127`, `seal/threads/1793240967-the-worktree-guard-was-never-weighed/changelog.md:12`, `seal/threads/1793240967-the-worktree-guard-was-never-weighed/frame/design.md:104-108`, `seal/threads/1793240967-the-worktree-guard-was-never-weighed/frame/design.md:146`, `seal/threads/1793240967-the-worktree-guard-was-never-weighed/frame/plan.md:59`, `seal/threads/1793240967-the-worktree-guard-was-never-weighed/frame/questions.md:22`
evidence: read `skills/settle/scripts/rule_changes.py:253-264`, `.github/scripts/rules.py:312-319`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:306-326`, `docs/the-record-layout.md:42-47`, `tests/github/test_gather_changelog.py:9-16`, `hooks/lib/optin.py:167-200`
verdict: open
regression: round-1#1

The unit is `.github/scripts/rules.py#unresolved` with the excuse 2bfa6459
added, and the sentences that commit wrote about it. The frame, as 76c77c74
folded it from the fix (`frame/plan.md` phase 2 row, `frame/design.md`
*Scope* In 7 and S8), says the check "reads the policy in force" and then
that "a `remove` of another section, or one with a `from`, excuses
nothing". The fix built the second clause and wrote the first as what a
reader may rely on. The defect came from how the fix was written: round 1's
paste-ready fix called that one shape "the policy in force", and the fix
pass copied the phrase into the module docstring, the settle skill and the
changelog fragment.

The fix pass's answer claimed the check reads the policy in force, and so do
`.github/scripts/rules.py:28-33`, `skills/settle/SKILL.md:125-127` and the
changelog fragment's bullet heading at `changelog.md:12`.
`skills/settle/scripts/rule_changes.py:259` skips every item that is not a
`remove` with no `from`. The policy in force also loses a `check:` line where
a pending `change`, or a `remove` with a `from`, quotes the line in its
`from` and its `to` does not hold it. The tree holds that case now. Work item
1793188384's design (`frame/design.md:306-326`) changes
`docs/the-record-layout.md` *A change writes fragments, never a shared
file*. Its `from` holds the check line at `docs/the-record-layout.md:47`, and
its `to` names `tests/github/test_publish_release_note.py` instead. The check
still refuses that line once the two files it names are gone. That is why
`tests/github/test_gather_changelog.py:9-16` keeps a file with no case until
that settle, and its docstring says so.

The changelog fragment tells a person "its tests can go in the same pull
request", and the settle skill tells a session "It reads the policy in
force". A session that retires a mechanism through a `change` and trusts
either sentence deletes the tests and meets a refusal.

There is a second limit that nothing states. `rule_changes.pending` reads
`<root>/seal/threads/`, and `unresolved` reads the policy root from
`<root>/seal`. In local mode the `seal/` root sits under the common git
directory (`hooks/lib/optin.py#home_paths`), so no design is read and no line
is excused. A CI checkout of such a repository holds no design either. So
reading `optin.home_at` instead would make a local run excuse a line that CI
refuses. The limit belongs in a sentence, not in a different reader.

The fix writes each sentence to say what is read. The frame lines at
`frame/design.md:104` and `:146`, `frame/plan.md:59` and
`frame/questions.md:22` take the same words in the orchestrator's fold. The
fix pass may instead widen `rule_changes.removed_by` into a reader that also
excuses a refused line a pending item's `from` holds and its `to` does not,
as the first arm of the S9 excuser
(`tests/behaviour/test_a_cited_section_stands_in_its_file.py:157-162`) does
for a citation. Then the phrase "reads the policy in force" holds for `check:`
lines in a shared root, and a case in `tests/github/test_rules.py` plants a
`change` whose `from` holds the line, seen red first. In either case the text
and the reader must say the same thing.

`.github/scripts/rules.py`, the module docstring, in place of lines 28-33:

```python
`seal rules --check` excuses one shape of a pending rule change: a refused
line inside a section that an unsettled design's `remove` with no `from`
takes out at the settle is printed as `seal rules: excused: path:line:
heading: why; <work item> removes this section at the settle`, and is no
refusal. The designs are read through
`skills/settle/scripts/rule_changes.py#pending`, under `<root>/seal/threads/`.
A pending `change`, or a `remove` with a `from`, whose `from` holds the line
excuses nothing, so the test the line names stays until the settle
(`tests/github/test_gather_changelog.py`). In local mode the designs sit under
the common git directory, which a CI checkout does not hold, so no line is
excused there.
```

`skills/settle/SKILL.md`, the sentence at lines 125-127:

```markdown
refuses one the grammar refuses. A refused line inside a section that a
pending `remove` with no `from` takes out at the settle is printed as
excused, with the work item that removes it, and is no refusal. A pending
`change`, or a `remove` with a `from`, excuses nothing, and where the `seal/`
root is local no line is excused. Whether
```

The changelog fragment, the bullet at line 12:

```markdown
- **`seal rules --check` excuses a line whose section a pending `remove` takes out (#1049).** A `check:` line it refuses inside a section that an unsettled design's `remove` with no `from` takes out at the settle is printed as `seal rules: excused: <path>:<line>: <heading>: <why>; <work item> removes this section at the settle`, and does not fail the check. The summary then reads `<n> excused in <lines> check lines of <files> rule files, and every other line holds.` A pull request that retires a mechanism by removing its policy sections whole leaves the document to the settle, as the layout rule says, and its tests can go in the same pull request. A pending `change` that rewrites a `check:` line excuses nothing, and where the `seal/` root is local no line is excused. `skills/settle/scripts/rule_changes.py` reads the pending designs for both this check and the suite case that excuses a citation a pending rule change corrects.
```

answer:

## Confirmations

confirms: round-1#1
The close holds. The fix pass claimed the document, its index row and the
`2.50.1` exemption are restored. `docs/worktree-guard-spec.md`,
`docs/README.md` and `tests/behaviour/test_release_hygiene.py` are
byte-identical to 1e82fd0a (executed, `git diff --quiet`, exit 0). Round 1's
`executed` lines, re-run at f8447b30:
`python3 .github/scripts/rules.py --check --root .` exits 0. It prints "17
excused in 266 check lines of 55 rule files, and every other line holds".
Each excused line names one of the five deleted test files and this work
item. `python3 skills/settle/scripts/fold_check.py --root .` exits 0. So the
layout rule at `skills/implement/SKILL.md:75` and the tree agree, and no
exception was written into it. The fix pass also claimed one reader holds the
remove fact. `tests/behaviour/test_a_cited_section_stands_in_its_file.py:146`
reads the designs through `rule_changes.pending`, and `:163` reads the remove
arm through `rule_changes.removed_by`. Its `from` arm stays at `:157-162`,
which reads a different fact, a citation in `from` and not in `to` (read).
`tests/github/test_rules.py`, that module and `tests/skills/test_rule_changes.py`
give 141 passed (executed, exit 0). The red-first runs the answer reports,
against the old check and under fddec67a's mutant, were read and not re-run.
Finding 1 above stands in the excuse this fix added and leaves the close in
place.

confirms: round-1#2
The close holds. Round 1's `executed` line, re-run:
`git grep -n -E "command_word\(|strip_subshell\(|_git_options\(|chdirs|split_segments_with_separators" -- hooks skills tests`
finds the three functions' definitions and calls inside
`hooks/lib/cmdline.py` alone. It also finds three unrelated case names in
`tests/skills/test_session_cost.py`, and `chdirs` only in the rider test's
docstring (executed, exit 0). `parse_git` returns `(subcommand, args)`,
`command_word` the segment, `strip_subshell` the tokens and `_git_options`
the index. `split_segments` holds the scan with no operator kept
(`hooks/lib/cmdline.py:541-603`, `:677-844`, read).
`hooks/implementer-notice.py:112-116` still reads `parse_git(tokens)[0]`
alone. `WRAPPED` maps a name to its command (`tests/hooks/test_cmdline.py:31-77`).
The rider tuple no longer holds `hooks/lib/cmdline.py`
(`tests/text/test_a_rider_reaches_its_file.py:114-118`). `.test_durations`
loses the four `Test_split_segments_with_separators` keys (read, the diff).
The unclosed-quote case that left with that class still stands for
`split_segments` at `tests/hooks/test_cmdline.py:126`. The rider test's
docstring at `:111-113` names the worktree guard across a line break, which
the S7 sweep cannot match. It states that the guard left, so *Scope* In 4
holds (executed, a scan for `worktree` at a line's end followed by `guard`,
one hit). `tests/hooks/test_cmdline.py`, `tests/hooks/test_implementer_notice.py`,
`tests/hooks/test_dispatch.py` and `tests/text/test_a_rider_reaches_its_file.py`
give 102 passed (executed, exit 0).

confirms: none
The frame fold agrees with the tree. The S7 sweep of `frame/design.md`
*Data & interfaces* prints 485 lines (executed, exit 0). Outside
`seal/threads/`, the replay eval and `docs/worktree-guard-spec.md` it prints
five: `docs/README.md:41`, `docs/the-review-record.md:633`,
`docs/the-routing-check.md:81`, `tests/behaviour/test_release_hygiene.py:129`
and `tests/hooks/test_root_migrate.py:927`. These are exactly the lines S7
lists. *Scope* In 3, the *Removes* row for `hooks/lib/cmdline.py` and the
phase 3 row of `frame/plan.md` name the outputs a82da960 removed. *Scope*
In 6 names the restored bytes (read).

confirms: none
`README.md:149` and `README.ko.md:143` need no qualifier, and neither do
`README.md:19`, `README.ko.md:20`, `CONTRIBUTING.md:61-64` or
`agents/proofer.md:102`. Each one says what the check does for a rule a
policy document states. A line the excuse covers stands in a section that the
policy in force no longer states. Each sentence errs in one direction only: a
reader expects a refusal and gets an excuse, which costs nothing. The
qualifier is stated in the command tables at `README.md:263` and
`README.ko.md:258` and in the module docstring. Writing it into the six
general sentences would state the excuse in eight places (read). The
qualifier's own wording is finding 1's.

confirms: none
`gaps.md`'s claim that no check refuses a dead key of
`VERSIONS_OF_ANOTHER_PRODUCT` holds. `tests/behaviour/test_release_hygiene.py:266-269`
looks a key up and never checks that its file exists (read).

confirms: none
The changed files pass `uvx ruff check` and `uvx ruff format --check`. The
files are `hooks/lib/cmdline.py`, `.github/scripts/rules.py`,
`skills/settle/scripts/rule_changes.py`, `tests/github/test_rules.py`,
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`,
`tests/hooks/test_cmdline.py`, `tests/text/test_a_rider_reaches_its_file.py`
and `tests/behaviour/test_release_hygiene.py` (executed, each exit 0).
`tests/behaviour/test_release_hygiene.py`, `tests/skills/test_fold_check.py`
and `tests/skills/test_settle.py` give 141 passed (executed, exit 0).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over f8447b30: unverified | the whole tree | the orchestrator, at the broad gate |
| Whether `.test_durations`, with 30 unpriced cases (`gaps.md` *Not done*), stays under `test_the_durations_file_prices_the_suite`'s shares: unverified, because that case belongs to the broad run | `.test_durations` | the orchestrator, at the broad gate |
| Whether the settling session will find the `2.50.1` key. `gaps.md` *Not done* hands its removal to that session in prose. The settle's dry run lists the open `## Not verified` rows (`skills/settle/scripts/settle.py:39-41`) and not a `## Not done` paragraph, so only a `git grep` for the document's path reaches the key | `seal/threads/1793240967-the-worktree-guard-was-never-weighed/gaps.md`, `tests/behaviour/test_release_hygiene.py:129` | the orchestrator |
| Whether the phase 2 and phase 3 rows of `frame/plan.md` should name the fix commits. 76c77c74 rewrote their *Delivers* cells to include what 2bfa6459 and a82da960 built, and the *Status* cells still name only f528f7a1 and 4c9abc11, which `skills/implement/orchestration.md` *Where a work item stands* gives as where the state is read | `seal/threads/1793240967-the-worktree-guard-was-never-weighed/frame/plan.md` | the orchestrator |
| The red-first runs of `tests/github/test_rules.py#Test_main::test_a_refusal_in_a_section_a_pending_remove_takes_out_is_excused_and_named`, against the old check and under fddec67a's mutant: read in the fix pass's answer, not re-run | `tests/github/test_rules.py` | the sealer |

## Probes

| Command | Result |
|---|---|
| `git diff --quiet 1e82fd0a f8447b30 -- docs/worktree-guard-spec.md docs/README.md` | exit 0 |
| `git diff --quiet 1e82fd0a f8447b30 -- tests/behaviour/test_release_hygiene.py` | exit 0 |
| `bin/seal rules --check` | exit 0, 17 excused in 266 check lines of 55 rule files |
| `python3 .github/scripts/rules.py --check --root .` | exit 0, the same summary |
| `python3 skills/settle/scripts/fold_check.py --root .` | exit 0, "the index docs/README.md names every document" |
| `bin/test tests/github/test_rules.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/skills/test_rule_changes.py -q -p no:randomly` | exit 0, 141 passed |
| `bin/test tests/hooks/test_cmdline.py tests/hooks/test_implementer_notice.py tests/hooks/test_dispatch.py tests/text/test_a_rider_reaches_its_file.py -q` | exit 0, 102 passed |
| `bin/test tests/behaviour/test_release_hygiene.py tests/skills/test_fold_check.py tests/skills/test_settle.py -q` | exit 0, 141 passed |
| `uvx ruff check` and `uvx ruff format --check` over the eight changed Python files | exit 0 each |
| Round 1's finding 2 `git grep -n -E` for the five names, over `hooks`, `skills` and `tests` | exit 0, hits inside `hooks/lib/cmdline.py`, three unrelated case names, and the rider test's docstring |
| The S7 sweep of `frame/design.md` *Data & interfaces* | exit 0, 485 lines, five outside the threads, the replay eval and the guard's document, each listed by S7 |
| `git grep` for a line ending in `worktree` outside the threads, the replay eval and the guard's document, with the next line read for `guard` | exit 0, one hit, `tests/text/test_a_rider_reaches_its_file.py:112` |
