# Review round 2: 1795390622-the-root-places-omit-agentic-seal

```seal
target: 69d2700cff7126347ba1bcf7b7b5774e19cf9ee2, fixes 64059f40f..69d2700cf
```

This is a verifying round. Its code bound is the diff from round 1's target
`64059f40f` to `69d2700cf`: commits `93687f7f1`, `d6e1efa39`, `0d0963e88`
and the close blocks at `69d2700cf`. Every hunk of it was read. Beside that
bound, `routing.md`, the three frame files, `gaps.md`, `changelog.md`,
`pr.md` and the three phase records were each read whole at `69d2700cf`.
No `pr.<lang>.md` stands, and none is owed, since `seal/config.json` names
English for both language keys. No `seal/parity.json` is declared. The
chain check printed no notice at a line of `frame/design.md`.

Carried from round 1 and not searched again: the coordinates of *Scope*
items 1 to 10 that round 1 read at HEAD, and the list of narrow modules.
Re-derived here: every count the fragment states, by the search round 1
finding 1 names, re-run at `641b6bfb5`, and by reading the base statements
each count covers.

Each quote of `pr.md` stands word for word at its coordinate:
`frame/plan.md:59` twice and `routing.md:24` (executed, `grep -c -F` on
each quote, 1 each). No file `pr.md` quotes changed in the fix diff.

## Findings

### 1. The closing memo and phase 2's record say one sentence restates the body's refusal outside its owner, and the bootstrap holds a second

```seal
severity: should
location: `seal/threads/1795390622-the-root-places-omit-agentic-seal/gaps.md:16-19`, `seal/threads/1795390622-the-root-places-omit-agentic-seal/trail/phases/phase-2.md:96-110`, `skills/implement/bootstrap.md:138-141`
evidence: executed `git grep -n -i -e 'an absent key' -e 'is absent' -e 'absent in any' -e 'four ways' -- skills agents templates docs CONTRIBUTING.md ':!*.py'`, `git show 73a43735c:skills/implement/bootstrap.md | grep -n -B2 -A3 'either key is absent'`, `git diff 641b6bfb5 HEAD -- skills/implement/bootstrap.md | grep -n absent`; read `skills/implement/bootstrap.md:138-147`, `skills/commit-pr-convention/SKILL.md:82-89`, `docs/checks/the-pull-request-check.md:180-187`, `docs/running/what-a-script-gates.md:66`, `docs/forms/the-guarantee.md:22`
reopens: round-1#3
```

Why the close of round 1 finding 3 does not hold: the fix removed the one
restatement the finding located and rewrote the memo to say that one
sentence is left. The class the finding belongs to is every statement of
what an absent language key does outside the template's paragraph, the
*Removes* row at `frame/design.md:127`. A second member of it stands in the
bootstrap and stood there through every phase. The fix pass's answer names
no method that listed the class (contract rule 12).

- **Claimed** at `gaps.md:16-19`: "One sentence states part of what an
  absent language key does, beside a reason the template does not give:
  `docs/forms/the-guarantee.md:22`". `trail/phases/phase-2.md:96-110`
  says the same under **The statement this phase left standing, and
  why.**, and names the commit skill's sentence as the only other one.
- **Found** at `skills/implement/bootstrap.md:139-141`: "`seal pr-body`
  refuses to compose a pull request body where either key is absent, so
  first setup asks for both while the session is already stopped." It is
  the same shape as the commit skill's sentence round 1 finding 3 removed:
  the refusal, restated, beside the reason the orchestrator asks. The
  template does not give that reason. The sentence stood the same at
  `73a43735c` and no commit of this branch touched it (executed). No list
  of *Scope* item 5 names it, and neither does the memo.
- Two more hits state that `seal pr-body` refuses on an absent key:
  `docs/checks/the-pull-request-check.md:186-187` and the `seal pr-body` row
  of `docs/running/what-a-script-gates.md:66`. Each describes what one
  check or script gates, which is that document's subject, as the frame
  keeps a docstring that describes its own unit out of scope. They are no
  part of this finding. The search is line-bound, so it is a sample: a
  statement worded without "absent" stays outside it.

The memo is what the sealer reads for what was left, and it now tells the
sealer one sentence stands. The fix below treats the bootstrap sentence as
finding 3 treated the commit skill's: it keeps the reason and cites the
owner for the refusal. The memo then stays true as written. Phase 2's
record owes the corrected account in place (contract rule 19). Where the
fix pass judges the sentence should stay, the memo and the phase record
name it with the reason instead, and the bootstrap does not change.

```markdown
<!-- skills/implement/bootstrap.md:138-141; the file is held to 88 columns -->
   **The third and fourth questions are the two language keys, with the
   recent titles beside them.** First setup asks for both while the session
   is already stopped, since what an absent one does is
   `templates/setup/config.md` *An absent language key is a refusal at the
   pull request body, and never at a commit*. Beside the two questions the

<!-- trail/phases/phase-2.md, a paragraph after the one ending at :110 -->
Phase 2 also left `skills/implement/bootstrap.md:139-141`, "`seal pr-body`
refuses to compose a pull request body where either key is absent, so first
setup asks for both while the session is already stopped." No list of
*Scope* item 5 named it. Round 2 finding 1 named it, and its fix pass kept
the reason and made the refusal a citation of the template's paragraph.
```

### 2. The sentence that settles the fourth way of absence is pinned by no case, so the two readings round 1 found can come back unseen

```seal
severity: should
location: `tests/text/test_the_rules_have_one_owner.py:263-276`, `templates/setup/config.md:34-36`
evidence: read `templates/setup/config.md:31-41`, `tests/text/test_the_rules_have_one_owner.py:258-276`, `tests/conftest.py:830-837`, `skills/implement/routing-question.md:139-145`; executed `grep -n 'counts as absent' templates/setup/config.md`
reopens: round-1#2
```

Why the close of round 1 finding 2 does not hold: the text fix holds, and
the close is early. `skills/code-review/SKILL.md` *The record*, under **A
finding is not closed too early.**, says "A claim a fix writes into a
document closes when a test pins the document, not when the sentence
lands." The fix pass's hand-back, as the orchestrator relays it, says the
new sentence takes no pin by contract rule 14. Rule 14 covers a message, a
verdict or a rendered line. The code-review rule covers a claim a fix
writes into a document, which this is.

What holds: `templates/setup/config.md:34-36` now reads "The fourth way is
the refusal the next paragraph gives, and for these two keys it counts as
absent wherever this file or a skill speaks of an absent key." That gives
the reader of `skills/implement/routing-question.md:141-144` one reading:
a key written twice or a file that will not read is absent, and the batch
asks. The bold lead of the next paragraph, "a file that will not read is
refused rather than read as absent", still reads as a rule for every key.
No file cites that lead (executed, `git grep` on its words prints only
`lib/config.py`), so a reader reaches it from the paragraph above it.

What is missing: row 26 of `RULES` pins four spellings of the paragraph,
and none of them is in the new sentence. Delete the sentence and the suite
stays green, and the two readings return. The frame pins every owner fact
of this paragraph (`frame/design.md` D1 row (c)), so this sentence's
classification is the same kind of fact. "for these two keys it counts as
absent" stands once in the file (executed), and `flat` collapses the line
break inside it (`tests/conftest.py:830-837`). The fix pass shows the case
red with the sentence taken out before it commits the line (contract
rule 15).

```python
            # The four ways a key is absent, which a reader of `config.json`
            # checks the file against.
            "no file, no such key, an empty value",
            "does not parse as one JSON object",
            # The fourth way counted as absent for the two language keys,
            # where the next paragraph's lead refuses it for every key.
            "for these two keys it counts as absent",
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `changelog.md:3` now says "Contract rule 11 and ten other files
named the first and the last alone", and adds "with its copy
`seal/README.md`" and "as where the root is looked for". `changelog.md:20`
says "Eleven files". The search round 1 named, re-run at `641b6bfb5`, lists
fourteen files (executed). They are the contract, the ten files the item
lists, `seal/README.md`, and the two parity skills, which name shared mode
and stay out of the class. The fix pass also corrected three more counts,
and each was checked against the base. Item 2's three lists that left out
the phase record hold against `frame/design.md` G8. Process row 2's six
files and its "five files and two sections of the template" hold against
G8 and G11. Process row 4's four files hold: at `641b6bfb5`,
`agents/sealer.md:42-46`, `skills/verify/orchestration.md:45-48`,
`docs/running/the-broad-gate.md:73-75` and
`skills/code-review/orchestration.md:464-466` each give the base order, and
the last leaves out the ref as given (read). The comment above `RULES`
row 24 now counts eleven files and says each names the core's paragraph.
Each of the eleven does (executed, a search for the core's path in each
file). The fragment was taken apart sentence by sentence again here, and no
other count or absence in it is contradicted by the tree (read).

```seal
confirms: round-1#4
```
What holds: in `93687f7f1`, the G18 cell of `frame/design.md:26` ends with
the sentence on `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:339-357`.
The frame names `tests/github/test_release_seal.py` only at G14
(`frame/design.md:22`), as a `REASONS` entry, and in the plan's phase 3
row (`frame/plan.md:39`), as a module that passes (executed, `grep` over
the frame files). Line 382 of the module is that `REASONS` entry (read).

What matched: round 1 finding 3's own coordinate.
`skills/commit-pr-convention/SKILL.md:82-89` keeps who asks and the
reason, and no longer restates the refusal (read). `gaps.md` and
`trail/phases/phase-2.md` no longer give the misread coordinate as a
ground. Finding 1 above is about the class, not this coordinate.

One gap of the kind `skills/code-review/SKILL.md` *The record* names, no
finding. The comment above `RULES` row 28
(`tests/text/test_the_rules_have_one_owner.py:292`) still says "three files
each gave the order the gate resolves its base in". The fix pass corrected
the same count to four in the fragment's process row 4 and left the
comment. Only whoever next edits the row reads that comment.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD, which `gaps.md` labels `unverified`. The label is honest: no party has run them | `seal/threads/1795390622-the-root-places-omit-agentic-seal/gaps.md:7` | the orchestrator, at the broad run |
| Whether a crafter's commit owes the `Seal-Routing:` trailer that `skills/commit-pr-convention/SKILL.md:193-195` asks of "a session's commit" at a shared root. The fix-pass commits `d6e1efa39` and `0d0963e88` carry none, and neither does any phase commit. `chain-check` does not judge a commit with no trailer, so nothing refuses it | `git log --format='%h %(trailers:key=Seal-Routing,valueonly)' 641b6bfb5..HEAD` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/text/test_the_settings_have_a_front_door.py tests/behaviour/test_no_document_names_the_old_roots.py -q` | exit 0, 250 passed, 5 warnings |
| `git grep -l -e '<repo>/seal' 641b6bfb5 -- skills agents templates docs seal/README.md ':!*.py'` | fourteen files, listed under the first confirmation |
| `python3 skills/code-review/scripts/chain_check.py --baseline 641b6bfb5 --root . --worktree`, before this record was written | exit 0. It named round 1's findings 1 to 3 as owing a verifying round, `trail/gate.md` and `guarantee.md` as not yet written, and no notice at a line of `frame/design.md` |
| the same command, with this record written | exit 0. Both findings are named as open for having no close block, which the fix pass appends, and nothing else in this record is refused |
