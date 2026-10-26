# Review round 1: 1792973486-a-change-only-the-shell-makes-is-a-chore

target: 1d9c9b72 against 61a8455a

This is the first round, so no earlier record exists and no fact was carried
from one. Every fact below was opened or run in this round, in the checkout
of the branch at `1d9c9b72`.

## Findings

### 1. The sentence's own example, a rename made through the shell, is a change work items make every release

severity: should
location: `CLAUDE.md:19`, `seal/specs/1792973486-a-change-only-the-shell-makes-is-a-chore/spec.md:34-38`
evidence: executed `git log --diff-filter=R -M --format='%h %s' -6 61a8455a`, `grep -n -E 'Write|Edit|NotebookEdit|tool_name' hooks/routing-edit-gate.py`
verdict: fixed 8e656460

The new sentence names three examples of a change that would be routed
`no work item`: a formatter run, a dependency bump, and a rename made through
the shell. The third is not a chore. The `Write`, `Edit` and `NotebookEdit`
tools cannot move a file, so a work item that renames or moves a file does it
through the shell with `git mv`. The routing edit gate matches those three
tools alone (`hooks/routing-edit-gate.py:57`, `TOOLS = ("Write", "Edit",
"NotebookEdit")`). Work items do rename files: the `git log` run above lists
`b451e503` (#941) and `4b363e68` (#822) among the commits with renames, and
both were built under a work item.

So the example puts a change a work item owns into the class the sentence
exempts. A reviewer weighing a gap that a work item's `git mv` passes through,
which the routing check never sees, can cite this sentence to call that gap
not a weakness to close. `plan.md` *Technical context* names this exact
stretch as the failure scenario, "a session that writes a work item's files
through the shell", and says the sentence does not cover it. The example is
what makes it cover it.

The issue named the example differently: "a bulk rename through `sed`", a
text substitution across files. An agent may not edit through `sed`
(contract rule 9, `agents/smith.md:70`), so that example stays outside the
work a work item owns. The frame shortened it to "a rename made through the
shell" in `spec.md` *Scope* item 1, and the build copied it word for word.

The fix restores the issue's example in `CLAUDE.md` and in the spec's quote
of it. Where finding 2's fix is taken, its text already carries this change.

```markdown
work a work item owns. A change that would be routed `no work item`, such as
a formatter run, a dependency bump or an identifier renamed across files by
`sed`, is outside that work, so a gap in a gate or a check that
only such a change passes through is not a weakness to close. A rule's proof
```

answer: The finding holds. The orchestrator rewrote `spec.md` *Scope* item 1 in bb01b549 with the record's example, an identifier renamed across files by `sed`, and added a sentence saying a file renamed with `git mv` inside a work item is work the work item owns; the spec still parses, with the no-change block and no error (executed). The smith put the new sentences into `CLAUDE.md` in 8e656460, word for word; `git diff --word-diff 61a8455a -- CLAUDE.md` shows only added words (executed by the smith).

### 2. A gate or a check reaches the checks that run on every pull request, where the principle is false

severity: should
location: `CLAUDE.md:17-21`, `seal/specs/1792973486-a-change-only-the-shell-makes-is-a-chore/spec.md:34-38`, `seal/specs/1792973486-a-change-only-the-shell-makes-is-a-chore/questions.md:10-17`
evidence: read `CONTRIBUTING.md:53-64`, `.github/workflows/test.yml:3-11`, `.github/workflows/hygiene.yml:3-16`, `skills/agent-contract/SKILL.md:118-123`, `seal/specs/1792973486-a-change-only-the-shell-makes-is-a-chore/questions.md:10-17`
verdict: fixed 8e656460

The issue asks for a sentence saying "a gate guards the work the workflow
governs". The frame widened `A gate` to `A gate or a check`
(`questions.md:11-14`), on the ground that "the owner's ground covers any
mechanism and the section already speaks of checks". That ground is the
frame's own. The owner's ground in the issue is narrower: a gate that catches
only chores "adds a cost and a question with nothing to catch". A check that
runs on every pull request asks nobody anything, so the ground does not reach
it.

In this paragraph `check` has two readings. One is the routing check, which
contract rule 9 names (`skills/agent-contract/SKILL.md:118-123`). The other
is every check the paragraph's own sentence `A check gates only a fact it
reads` speaks of, which includes the CI checks. Under the second reading the
first new sentence, `A gate or a check guards the work a work item owns`, is
false of the repository. `CONTRIBUTING.md:55-64` says the CI checks run on
every pull request, including a contribution that opens no work item. It
names one that guards such a contribution: "a `check:` target the change
renamed or removed fails it". `test.yml` runs on every `pull_request`
(`.github/workflows/test.yml:3-11`), and `hygiene.yml` on every pull request
event it lists (`.github/workflows/hygiene.yml:3-16`). A dependency bump
from an outside contributor is a change no work item owns, and it passes
through all of them.

So the second sentence tells a reviewer that a gap in the suite or the
hygiene scan which only a dependency bump or a formatter run passes through
is not a weakness to close. Nobody asked for that, and the issue's *Done
when*, "no other file in the tree contradicts it", fails against
`CONTRIBUTING.md:61-64`.

The fix scopes the principle to the gates the owner's ground covers, those
that stop a session, and keeps the phrase `S2` greps for. It also carries
finding 1's example. `spec.md` *Scope* item 1 quotes the sentence exactly,
so its quote moves with it, and `questions.md` *Its wording* states the
reason for the scope. The fix pass reflows the paragraph as phase 1 did.

```markdown
it costs**; existing is no reason to keep it. A gate that stops a session,
the routing check among them, guards the work a work item owns. A change
that would be routed `no work item`, such as a formatter run, a dependency
bump or an identifier renamed across files by `sed`, is outside that work, so
a gap in that kind of gate which
only such a change passes through is not a weakness to close. A rule's proof
```

answer: The finding holds, and the record's direction is taken: the principle now names a gate that stops a session, the routing check among them. The owner's ground, given to the orchestrator in conversation, was SpecSeal stepping into a session, not the checks every pull request runs. The orchestrator rewrote `spec.md` *Scope* item 1 and the wording entry of `questions.md` in bb01b549, adding a sentence that the checks every pull request runs are not that kind of gate and are not exempted; the smith put the sentences into `CLAUDE.md` in 8e656460, with `only such a change passes through` on one line, which `git grep` outside `seal/specs/` finds at `CLAUDE.md:22` alone (executed by the smith).

### 3. The work item has no changelog fragment, and the repository records a CLAUDE.md rule change in the changelog

severity: should
location: `seal/specs/1792973486-a-change-only-the-shell-makes-is-a-chore/changelog.md`, `seal/specs/1792973486-a-change-only-the-shell-makes-is-a-chore/overview.md:21`
evidence: executed `for d in seal/specs/*/; do [ -f "$d/changelog.md" ] || echo "$d"; done`, `git grep -n 'changelog.md' -- skills/verify/scripts skills/code-review/scripts .github/scripts skills/implement/scripts agents/sealer.md docs/the-review-record.md`
verdict: fixed cc20b733

`overview.md:21` claims no fragment is owed because the change "is one
principle in this repository's own `CLAUDE.md`, which a consuming repository
never receives", and that `skills/implement/SKILL.md` and `plan.md` row 1
ask none. The tree does not hold that ground.

- `skills/code-review/orchestration.md:172-178` makes a fragment a condition
  of the broad run: the orchestrator takes it once "the work item's
  `changelog.md` states what the work item ships", and the party that builds
  the work item writes it. `phases/phase-1.md:20` read the same lines and
  left the decision to the orchestrator.
- The changelog records changes a consuming repository never receives. A
  rule added to this repository's `CLAUDE.md` was a changelog entry three
  times: `changelog/0.12.2.md:145-148`, `changelog/0.15.3.md:84-89` and
  `changelog/0.18.1.md:189-196` (#730, which notes "The block `install.sh`
  distributes is unchanged"). On this release branch, #841's fragment
  (`seal/specs/1791270165-the-windows-test-leg-is-measured-and-cut/changelog.md`)
  records a CI-only change, and #1005's records a citation convention.
- The loop above lists this work item alone among the 44 directories under
  `seal/specs/` without a `changelog.md`.
- `.github/scripts/publish_release_note.py:57-58` names the one kind of
  change that carries no fragment: an outside contribution, which carries no
  work item.
- `CLAUDE.md:32` says history goes to "git, the changelog and the work
  record".

No check refuses the missing file; the `git grep` above finds only the
gather reading fragments that exist. That is why the record catches it
rather than a gate. Without the fragment, release 0.22.4's note omits the
rule every later gate design is weighed against.

```markdown
### Changed

- **A gate is weighed by the work a work item owns (#1031).** This
  repository's `CLAUDE.md`, *The rule a mechanism is kept against*, now says
  that a change which would be routed `no work item`, such as a formatter
  run, a dependency bump or an identifier renamed across files by `sed`, is
  outside that work. A gap in a gate that only such a change passes through
  is not a weakness to close, so no gate is built to catch a change only the
  shell makes. Nothing the plugin installs into a consuming repository
  changes.
```

The fragment goes to `seal/specs/1792973486-a-change-only-the-shell-makes-is-a-chore/changelog.md`,
in the words the sentence holds once findings 1 and 2 are answered, and
`overview.md` *Not done* loses its first paragraph in the same commit.

answer: The finding holds; the orchestrator's reading that a `CLAUDE.md`-only change owes no fragment was wrong against the repository's practice the record cites. The smith wrote `changelog.md` in d1390952 from the record's draft, stating the narrowed principle and that nothing the plugin installs into a consuming repository changes; `tests/test_the_changelog_is_gathered_at_release.py` and the fragment's two other readers pass (executed by the smith). The orchestrator removed the no-fragment paragraph from `overview.md` *Not done* in cc20b733, a separate commit rather than the same one, because the smith's fix pass does not edit `overview.md`.

## Confirmations

confirms: none
The two sentences stand directly after `existing is no reason to keep it.`
at `CLAUDE.md:17`, word for word as `spec.md:34-38` quotes them, and no old
word of the section changed (`S1`). Executed: `git diff --word-diff
61a8455a..HEAD -- CLAUDE.md` shows `{+ +}` runs only and no `[- -]` run, and
a Python comparison with whitespace collapsed found the quote in the file
and found it starting right after the anchor sentence. The phase record's
claim of the same, `phases/phase-1.md:18`, holds.

confirms: none
`git grep -n 'only such a change passes through' -- ':!seal/specs/'` finds
`CLAUDE.md:21` alone (`S2`, executed). The placement and the reflow hold:
the widest line of the paragraph is 77 columns, as `phases/phase-1.md:16`
claims, and `CLAUDE.md:20` is 53 columns (executed, `awk` over lines 16 to
34). The short line is the price of keeping the `S2` phrase on one line,
because `git grep` matches within a line. Markdown renders the paragraph the
same whatever the breaks, no reader acts on a raw line break, and
`tests/test_docs_line_wrap.py` passed. So it is no finding. A later frame
that verifies a sentence by grep would leave the text's breaks free by
searching the whitespace-collapsed paragraph instead.

confirms: none
The modules that read `CLAUDE.md` pass (`S5`): `bin/test` over
`tests/test_rules.py`, `tests/test_the_rules_claude_md_names_have_one_home.py`,
`tests/test_no_passage_is_pasted_into_a_second_file.py`,
`tests/test_one_word_one_meaning.py`,
`tests/test_a_release_is_sized_by_a_criterion.py` and
`tests/test_docs_line_wrap.py` gave 148 passed at exit 0, the figure
`phases/phase-1.md:26` claims. `bin/rules --check` exited 0. Both executed,
and both are probes, not the broad gate.

confirms: none
Two defined terms keep their one meaning. `no work item` is the routing
answer of `skills/implement/orchestration.md:288`, written in backticks as
there. `owns` matches the existing uses at
`docs/commit-review-gate-spec.md:72` and
`docs/the-review-and-parity-arms.md:78`. The sentence says `gap` rather than
reusing `routed` for a path past a gate, as `questions.md:15-17` intends.
Read. Finding 2 is about `gate or a check`, the one term that does not keep
its meaning.

confirms: none
The frame's search holds against a wider one (`S4`). Beyond the paths
`spec.md` *Scope* item 3 searched, this round searched `hooks/`, `tests/`,
`.github/`, `changelog/`, `evals/`, `bin/` and every `plan.md` under
`seal/specs/` for `through the shell`, `shell write`, `shell edit`,
`shell substitution`, `through bash`, `bash call` and `git status after`
(executed). No hit calls the shell route a weakness to close or proposes a
mechanism to catch it. The one new kind of hit,
`tests/test_edits_go_through_the_edit_tool.py:46-59`, pins contract rule 9's
"an edit through the shell is invisible to it", the fact the frame's first
row keeps. The one contradiction this round found is a CI check, not a
sentence about the shell route, and it is finding 2.

confirms: none
`spec.md` *Rule changes* holds the no-change block correctly. `seal/config.md`
has no `Policy root` row, so the policy root is `docs`, and `CLAUDE.md` is
outside it (read, `seal/config.md:7-11`). `overview.md` *Where spec and
implementation diverged* says `none`, and the diff holds no change the frame
did not ask for: `git diff --stat 61a8455a..HEAD` names `CLAUDE.md` and the
work item's own files only (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at the branch head, labelled `unverified` in `overview.md` *Not verified*; that label is honest, since no party ran them | `1d9c9b72` | the orchestrator, through `broad-gate` once the rounds settle |
| The removal of the session memory file that held the principle, which lies outside the repository | outside the repository | the orchestrator, after the merge, as `spec.md` *Scope* item 4 says |

## Probes

| Command | Result |
|---|---|
| `git diff --word-diff 61a8455a..HEAD -- CLAUDE.md` | five `{+ +}` runs and no `[- -]` run |
| `python3 -I -c` comparing the whitespace-collapsed quote of `spec.md:34-38` with `CLAUDE.md` | both checks printed `True`: the quote stands in the file, directly after the anchor sentence |
| `git grep -n 'only such a change passes through' -- ':!seal/specs/'` | `CLAUDE.md:21` alone |
| `awk 'NR>=16 && NR<=34 {print NR, length($0)}' CLAUDE.md` | widest line 77 columns; line 20 is 53 |
| `bin/test` over the five `S5` modules and `tests/test_docs_line_wrap.py`, `-q` | 148 passed, exit 0 |
| `bin/rules --check` | exit 0 |
| `git log --diff-filter=R -M --format='%h %s' -6 61a8455a` | six commits with renames, `b451e503` (#941) and `4b363e68` (#822) among them |
| `grep -n -E 'Write\|Edit\|NotebookEdit\|tool_name' hooks/routing-edit-gate.py` | `TOOLS = ("Write", "Edit", "NotebookEdit")` at line 57; no other tool is matched |
| `for d in seal/specs/*/; do [ -f "$d/changelog.md" ] \|\| echo "$d"; done` | this work item's directory alone |
| `git grep -n 'changelog.md'` over the scripts that could require a fragment | the gather alone reads fragments; no check requires one |
| `git grep -n -i -E` for the shell-route phrases above, over the widened paths | no sentence calls the shell route a weakness to close |
