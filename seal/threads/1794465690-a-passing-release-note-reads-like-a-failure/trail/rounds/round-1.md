# Review round 1: 1794465690-a-passing-release-note-reads-like-a-failure

```seal
target: e18a067b0 against release/v0.38.0
```

The range is `release/v0.38.0..e18a067b0`, base `79f815a74`. No earlier round stands, so nothing is carried from one. Carried from the frame without re-running: the renderer probes of `frame/design.md` G9 to G12, which this round did not send to `gh api markdown` again, because the whole-string cases pin the built headers byte for byte to the shapes *Data & interfaces* gives and those probes read. Carried from the phase records without re-running: the mutation tables of `trail/phases/phase-1.md` and `trail/phases/phase-2.md`. The S6 red of phase 1 was re-derived by reading: with a bare `header`, the seal's `2 pull requests merged<br>2 issues closed` occurs once inside the note's longer line, so `body.count(header) == 1` and the seal replaces part of the line instead of refusing (`.github/scripts/release_seal.py:558-575`).

## Findings

### 1. Three of the five rule changes put a new sentence between a policy sentence and the sentence that leans on it, so the settled text reads with a wrong antecedent

```seal
severity: should
location: `seal/threads/1794465690-a-passing-release-note-reads-like-a-failure/frame/design.md:85`, `seal/threads/1794465690-a-passing-release-note-reads-like-a-failure/frame/design.md:90-91`, `seal/threads/1794465690-a-passing-release-note-reads-like-a-failure/frame/design.md:97`, `seal/threads/1794465690-a-passing-release-note-reads-like-a-failure/changelog.md:4`
evidence: read `docs/releasing/branch-and-release.md:75-99`, `seal/threads/1794465690-a-passing-release-note-reads-like-a-failure/frame/design.md:81-109`, `seal/threads/1794465690-a-passing-release-note-reads-like-a-failure/changelog.md:4`; executed a whitespace-collapsed count of each `from:` in `docs/releasing/branch-and-release.md` (each found once)
```

Why it matters: the settle writes each `to:` in place of its `from:` and leaves the next sentence of the policy bullet as it stands. Read that way, at the target:

- Operation 3 (`frame/design.md:97`) appends three colour sentences after "its alt text is that label and value in words". The policy's next sentence, `docs/releasing/branch-and-release.md:98-99`, is "So a reader whose client draws no image, or who opens the note while the service does not answer, still has every result." After the settle, that "So" follows "every other value is blue", and the consequence of the alt text reads as a consequence of the colours. An agent reading `docs/` takes the wrong cause.
- Operation 2 (`frame/design.md:91`) appends the border sentence after "as badges, one or two to a line". The policy's next sentence, `:92-95`, opens "They are the sealed version and commit, …". After the settle, "They" follows a sentence whose only nouns are the table, its cells, its border and the seal, so the list of results has no antecedent in the sentence before it.
- Operation 1 (`frame/design.md:85`) ends its new sentence on "never inside a longer line". The policy's next sentence, `:78`, is "The release's theme follows it". After the settle, "it" reads first as that longer line, not the header.
- Operations 4 and 5 hold: operation 4's `to:` carries the sentence after it inside its own value, and operation 5 ends on a semicolon whose clause after it names its own subject.

The list comes from taking `## Rule changes` apart: each of the five operations, read against the policy sentence that follows its `from:` at `docs/releasing/branch-and-release.md`. Operation 3 also says `SEALED`'s dark red stands "under" the bright red value. A Shields badge draws its label to the left of its value, so nothing stands under anything. `changelog.md:4` says the same, and the changelog becomes the release note a person reads. The fix below writes "beside" in both places.

The fix replaces the three operations. Operation 2's `from:` widens by one sentence so that the border sentence follows the list. Each `from:` below is in the policy once with whitespace collapsed, as the round's count shows for the current ones, and the added sentence is `docs/releasing/branch-and-release.md:92-95` word for word.

```markdown
- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: The note opens with a header, an HTML table whose one cell holds the release's counts as text, one per line: the pull requests merged, the issues they closed, and the outside contributors where there are any.
  to: The note opens with a header, one HTML paragraph holding the release's counts as text, one per line: the pull requests merged, the issues they closed, and the outside contributors where there are any. The paragraph's opening and closing tags keep the seal from matching a longer line of counts, so the seal finds only the whole header.

- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: It runs the suite at the tag and replaces the note's header with a table whose last cell holds the results the stamp states, as badges, one or two to a line. They are the sealed version and commit, the pull requests merged, the issues closed, the outside contributors where there are any, the suite's counts, the work items and their review rounds, how many were capped, and the issues deferred.
  to: It runs the suite at the tag and replaces the note's header with a paragraph holding the results the stamp states, as badges, one or two to a line. They are the sealed version and commit, the pull requests merged, the issues closed, the outside contributors where there are any, the suite's counts, the work items and their review rounds, how many were capped, and the issues deferred. The header holds no table: GitHub draws a border around every table cell whatever the note's HTML asks, and in dark mode that border frames the seal in grey.

- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: A badge is a static image from the Shields badge service showing a label and a value in two of the seal's reds, and its alt text is that label and value in words.
  to: A badge is a static image from the Shields badge service showing a label and a value in colours read by its label from one table, so that a passing result does not read like a failure. Every label is grey except `SEALED`'s, which keeps the seal's dark red beside the seal's bright red value. The suite's passed count is green, the skipped, capped and deferred counts are grey, and every other value is blue. A badge's alt text is that label and value in words.
```

In `changelog.md:4`, the one sentence changes:

```markdown
Now every label is grey except `SEALED`'s, which keeps the seal's dark red beside its bright red value.
```

The snippet does not reach the case names `frame/design.md` gives the operations, since no `to:` changes the facts a case holds. Nothing else in the work item quotes these three `to:` values (read: `pr.md`, `gaps.md`, the two phase records).

### 2. The new colour case's docstring says it was seen red against the old `badge`, and its `SEALED` parameter passed against it

```seal
severity: should
location: `tests/github/test_publish_release_note.py:1078-1079`
evidence: read `tests/github/test_publish_release_note.py:1043-1087`, `seal/threads/1794465690-a-passing-release-note-reads-like-a-failure/trail/phases/phase-2.md:13-23`, `.github/scripts/publish_release_note.py:681`
```

Why it matters: the claim is "Seen red against the `badge` that coloured every label with the seal's two reds." `trail/phases/phase-2.md:17` records that this run failed eleven of the twelve parameters and that "The `SEALED` parameter passed, because `SEALED` keeps the two reds the old pair gave every label. Its red came from the mutation run below", which is the row "the `SEALED` entry removed, so it takes the default" at `:23`. Reading agrees: the old pair was `d42420` on `8e0c12`, and the `SEALED` entry at `.github/scripts/publish_release_note.py:681` is the same pair. So a person who reverts `badge` to check the docstring sees one parameter stay green and cannot tell from the docstring whether it pins anything. The skill counts a false seen-red claim as a finding (`skills/code-review/SKILL.md` *The record*), and contract rule 15 asks that a case name the guard its red was read for. The phase record is accurate. Only the docstring overstates.

```python
        label with no colours of its own is the case above. Seen red against
        the `badge` that coloured every label with the seal's two reds, at
        every parameter but `SEALED`, whose two reds that `badge` already
        gave; `SEALED`'s was seen red with its entry removed."""
```

## Confirmations

What matched: `frame/design.md` *Scope* item 1. `publish_release_note.py#header` returns `paragraph([...escaped counts])`, one line of `<p>`, the counts parted by `<br>`, and `</p>` (`.github/scripts/publish_release_note.py:643-665`, read). The publisher's source holds `<table>` nowhere else: the `### Process changes` table is a pipe table (`:304-323`, read). The changelog's "no longer an HTML table" therefore holds for the note's source.

What matched: *Scope* item 2 and *Data & interfaces*. `sealed_header` passes the floated `<img … width="W" align="left">` as `before` and `<br clear="left">` as `after`, and with no image it passes neither (`:734-762`, read). S2's and S3's whole-string cases compare the exact shapes, the escaped case among them (`tests/github/test_publish_release_note.py:926-1015`, read; executed in the narrow run below).

What matched: *Scope* item 3 and S5 to S7. `seal_release` keeps `body.count(header) != 1` and `body.replace(header, replacement)`, with `table` renamed `header` and nothing else changed (`.github/scripts/release_seal.py:558-577`, read). Both S6 parameters change one thing each: the seal's pull request list loses its outside author, or the note's count gains a digit (`tests/github/test_release_seal.py:959-963`, read). They refuse with the existing reason. The second-run and hand-edit cases still meet the new header (`:858-879`, `:1016-1031`, read), and every case passes (executed). Moving to one line removes the earlier header's internal newlines, so a body that came back with CRLF line endings could no longer split it. That is no new failure path. `seal_release` adds no refusal, and its message is unchanged.

What matched: *Scope* item 4 against the owner's C3 in issue #1496 (executed: `gh issue view 1496 --json title,body,comments,milestone`). `SEALED` is `d42420` on `8e0c12`. `suite` is `2ea44f`. `skipped`, `capped` and `deferred` are `6e7781`. Every other label falls to `BADGE_DEFAULT_COLOURS`, `0969da`, and every label but `SEALED`'s is on `555555` (`.github/scripts/publish_release_note.py:667-687`, `:711`, read). The suite's green never stands on a failed or unread suite: `release_seal.py#suite_counts` raises where the counts hold a failure or an error, and `release_rows` writes `suite` from numbers alone (`.github/scripts/release_seal.py:137-175`, `:229-250`, read).

What matched: *Scope* item 5. Each docstring and comment it names was rewritten. `git grep` over both scripts for `cell`, `table`, `red`, `reds`, `beside` and `colour` found no other statement of the old shape: the hits left are the `### Process changes` table, `release_seal.py:303` on a round record's shape, and `:240` on a red suite (executed). This is a sample, built from words.

What matched: *Scope* item 7. The diff leaves `docs/` as it is (executed: `git diff --stat release/v0.38.0..e18a067b0`). Each of the five `from:` values is found once in `docs/releasing/branch-and-release.md`, whitespace collapsed (executed). Those five cover every sentence of the bullet that states a table, a cell or the two reds, lines 75-76, 91, 97, 102-103 and 105-106 (read). G18 left a question to this round: should the bullet carry a check line? The bullet had none before this work, and no operation rewrites the bullet's bold rule sentence. So the question is not this work's, and no finding is opened for it.

What matched: the new test against its group. `test_a_badge_takes_its_two_colours_from_its_label` is read against `badge`'s group: the spelling case and the whole-string cases of both files. `tests/github/test_release_seal.py#BADGE_LINES` already pins every label's colours under `RESULTS`' values. What the new case adds is the `not read` value under every label: a `badge` that greyed a value it could not read would pass every whole string, since only `capped` carries `not read` there and `capped` is grey anyway. Phase 2's account names the group as the publisher's file alone, and that is narrower than the group is. Its conclusion holds by the `not read` value. `seal layout --pairs` named no pair (carried from `trail/phases/phase-2.md:9`, not re-run).

What matched: the records against the target. `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` were read whole at `e18a067b0`. Every `pr.md` quote stands word for word at its coordinate: `frame/questions.md:12` *Default until answered* and *Options & what each implies*, and `frame/plan.md:66`. `Commit and pull request language` is English, so no `pr.<lang>.md` is owed. `trail/phases/phase-1.md:5` names `publish_release_note.py:86-92` in *Scope* item 5. That was the frame at `c368121de`, which the record dates (executed: `git show c368121de:…/frame/design.md`), so the target does not contradict it. Apart from finding 1, no sentence of the work item's records that states what the work does is contradicted by the target.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the release page draws the one-line headers as GitHub's `/markdown` endpoint did: the seal floated, one line's badges side by side, the float cleared before the theme | `frame/questions.md` Q1, open at its default | the orchestrator, by the measurement Q1 names, or the owner on the 0.38.0 note after its seal job runs |
| The broad gate: the full suite, the repository-wide lint. The suite stays `unverified` | `seal/config.json` `Broad gate` | the orchestrator's broad run, after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_publish_release_note.py tests/github/test_release_seal.py -q -p no:xdist` | exit 0, 125 passed |
| `uvx ruff check` and `uvx ruff format --check` over the two scripts and the two test files | exit 0 each |
| `python3 -c` counting each `from:` of `frame/design.md` in `docs/releasing/branch-and-release.md`, whitespace collapsed | 1 for each of the five |
| `python3 skills/code-review/scripts/chain_check.py --baseline 79f815a74 --root <the worktree> --worktree`, before this record | exit 0; it named no round record, no gate record and no guarantee, and printed no notice at `frame/design.md` |
