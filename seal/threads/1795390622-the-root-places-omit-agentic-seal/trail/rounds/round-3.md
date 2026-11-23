# Review round 3: 1795390622-the-root-places-omit-agentic-seal

```seal
target: f7e4f8aa3902c87cde7ef88390727944f7c245b6, fixes 69d2700cf..f7e4f8aa3
```

This is a verifying round. Its code bound is the diff from round 2's target
`69d2700cf` to `f7e4f8aa3`: the fix commits `e7f86c9f0` and `7f183aa14`,
the close blocks at `81342b386`, and the orchestrator's fold of
`frame/design.md` at `f7e4f8aa3`. Every hunk of it was read. Beside that
bound, `routing.md`, the three frame files, `gaps.md`, `changelog.md`,
`pr.md` and the three phase records were each read whole at `f7e4f8aa3`.
No `pr.<lang>.md` stands, and none is owed, since `seal/config.json` names
English for both language keys. No `seal/parity.json` is declared. The
chain check printed no notice at a line of `frame/design.md`.

Carried from rounds 1 and 2 and not searched again: the coordinates of
*Scope* items 1 to 10, the counts of the fragment's process rows 1 and 4,
which round 2 re-derived against `641b6bfb5`, and the quotes of `pr.md`.
No file `pr.md` quotes changed in the fix diff (executed, `git diff --stat
69d2700cf HEAD` names neither `routing.md` nor `frame/plan.md`).
Re-derived here: the class of statements of what an absent language key
does, by a search of this round's own (*Probes*), every hit read; the
coordinates the fix pass and the fold name, each opened at the commit it
states.

The fix pass's account, as the orchestrator relays it, says the class
list was built by `git grep` on the language keys' names, on `seal pr-body`
refusals and on English as what a missing key leaves, and calls the list a
sample. Contract rule 12 allows a sample where no method makes the list
whole, and the other statements of a rule across the tree are that case.
This round's search used other wordings ("refuses to compose", "never
refused", "until it says", "without them", "either key", "missing key" and
the like) over the same roots, `CLAUDE.md` and `seal/README.md`. It found
no member outside the six the memo names and the five the rounds removed.
`README.md:128` and its Korean pair at `README.ko.md:132` say who asks for
the keys, which is out of the class.

## Findings

### 1. The release note calls the template's paragraph the one statement of an absent language key and counts seven files, while five policy files state the refusal and stay

```seal
severity: should
location: `seal/threads/1795390622-the-root-places-omit-agentic-seal/changelog.md:5`, `seal/threads/1795390622-the-root-places-omit-agentic-seal/changelog.md:21`, `seal/threads/1795390622-the-root-places-omit-agentic-seal/frame/design.md:19`, `seal/threads/1795390622-the-root-places-omit-agentic-seal/frame/design.md:127`
evidence: executed `git grep -n -i -E` with the wordings named above over `skills`, `agents`, `templates`, `docs`, `CONTRIBUTING.md`, both READMEs, `CLAUDE.md` and `seal/README.md`, `git diff --stat 73a43735c HEAD` over the five policy files; read `docs/forms/the-guarantee.md:22`, `docs/layout/one-root-by-lifetime.md:232-237`, `docs/layout/one-root-by-lifetime.ko.md:221-226`, `docs/checks/the-pull-request-check.md:186-187`, `docs/running/what-a-script-gates.md:66`, `seal/threads/1795390622-the-root-places-omit-agentic-seal/gaps.md:16-24`, `git show 73a43735c:skills/commit-pr-convention/SKILL.md` lines 121-123
reopens: round-1#1
```

Why the close of round 1 finding 1 does not hold: its fix pass took the
class "every count and absence the fragment states" and corrected the
counts it found. Round 2 confirmed process row 2's count against G11,
which lacked members. Round 2's fix pass then rewrote the same count from
"five files" to "seven files" and left the same gap. The row still counts
only the files whose restatement left, and it still names the template's
paragraph as the one statement.

- **Claimed** at `changelog.md:21`, the Change cell: the paragraph opening
  "An absent language key is a refusal at the pull request body, and never
  at a commit" "is the one statement of an absent language key". The Why
  cell says "seven files and two sections of the template each stated part
  of what an absent key does".
- **Found**: five shipped policy files state what an absent key does, at
  the base and at the target alike, since no commit of this branch changed
  those lines (executed). `docs/forms/the-guarantee.md:22` says "`seal
  pr-body` refuses where either language key is absent".
  `docs/layout/one-root-by-lifetime.md:234-235` says it "refuses to
  compose a body without them" and `:236-237` "A commit is never refused
  for them", and the Korean pair says the same at `:223-226`.
  `docs/checks/the-pull-request-check.md:186-187` says "where either key is
  absent the check refuses on `seal/config.json`, as `seal pr-body` does".
  The `seal pr-body` row of `docs/running/what-a-script-gates.md:66` says
  it "refuses where a language key is absent". `gaps.md:16-24` names all
  five as standing, so the work item's own memo contradicts its release
  note. At the base, twelve files besides the template stated part of it,
  not seven.
- **Claimed** at `frame/design.md:19`, G11 as the fold at `f7e4f8aa3`
  left it: "this row's search missed the last four, which round 2 found".
  **Found**: at `73a43735c` the search also missed the five policy files
  above, whose lines read the same there (executed). Round 2's record named
  one of the four, `skills/implement/bootstrap.md:139-141`. Its fix pass
  found the other three. G11 and the *Removes* row at `:127` give
  `skills/commit-pr-convention/SKILL.md:121-122`, and at `73a43735c` that
  sentence runs to `:123` (executed, `git show`).

Why it matters: the fragment becomes the release note, and the settle
reads its process rows when it rewrites the guidance. A reader who
believes the template's paragraph is the one statement will change it and
leave the five policy sentences to drift. That is the defect this issue
measured. This round judges that the five may stay. Each policy file says
what one script, check or form does, and `docs/` outranks the template
that `docs/layout/one-root-by-lifetime.md` names as the home of each key's
meaning (G10). So the fix states the exception rather than removing the
sentences. Every statement the fix touches is in the work item's records.
The comment above `RULES` row 26 counts the same eight files and is named
below the findings.

```markdown
<!-- changelog.md:21, the Change cell's last clause -->
the paragraph of the same file opening "An absent language key is a refusal at the pull request body, and never at a commit" is the one statement of an absent language key that the skills and the template cite, and the five policy files that say `seal pr-body` refuses on one keep their sentences

<!-- changelog.md:21, the Why cell's last clause -->
and seven files and two sections of the template each restated part of what an absent key does

<!-- changelog.md:5, a sentence before "`seal pr-body`'s refusals do not change." -->
Five policy files say that `seal pr-body` refuses where a language key is absent, each about its own script, check or form, and keep the sentence: `docs/forms/the-guarantee.md`, `docs/layout/one-root-by-lifetime.md` with its Korean pair, `docs/checks/the-pull-request-check.md` and `docs/running/what-a-script-gates.md`.

<!-- frame/design.md:19, G11, from the commit skill's coordinates to the end of the sentence -->
`skills/commit-pr-convention/SKILL.md:121-123` and `:321-323`; this row's search missed the last four, which round 2 and its fix pass found. It also missed five policy files that say `seal pr-body` refuses on an absent key, each about its own script, check or form, which the work keeps (`gaps.md` *Not done*): `docs/forms/the-guarantee.md:22`, `docs/layout/one-root-by-lifetime.md:232-237` and its Korean pair at `:221-226`, `docs/checks/the-pull-request-check.md:186-187` and `docs/running/what-a-script-gates.md:66`.

<!-- frame/design.md:127, the Removes row's coordinate -->
`skills/commit-pr-convention/SKILL.md:121-123` and `:321-323`
```

```seal
verdict: fixed 6b2fa3a54
answer: The finding holds. The orchestrator applied the paste-ready text as given: `changelog.md` item 3 and process row 2 name the five policy files that keep their sentence, and `frame/design.md` G11 and the *Removes* row name them and the commit skill's `:121-123`. In the same commit `pr.md`'s two coordinates name the row on the title's prefix, since the run's stop row now shares its date. The fix touches the work item's records alone, so the sealer reads it.
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: `skills/implement/bootstrap.md:139-142` keeps the reason first
setup asks and cites the template's paragraph for what an absent key does.
The citation case reads that citation: `seal mutate` changed one word of it,
and `test_every_cited_section_stands_in_its_file` went red naming
`skills/implement/bootstrap.md:142` (executed). Restored, `git status
--short` printed nothing. `skills/implement/routing-question.md:157-158`
names "the refusal the paragraph cited above gives", and the one paragraph
cited above it in that paragraph is the template's, at `:142-143` (read).
`skills/commit-pr-convention/SKILL.md:117-119` cites the section at `:76`,
which cites the template. `:317-318` keeps the act and drops the refusal
(read). No case pinned an old or a new wording: `git grep -F` on each
wording over `tests`, `evals`, `lib`, the scripts and `hooks` printed only
docstrings of `lib/config.py:9` and `skills/code-review/scripts/pr_body.py:46`,
each about its own unit (executed). The memo's six coordinates and the two
lines the phase record calls out of the class each hold the text the memo
gives at HEAD (read). The changelog's count in item 3 and the fragment's
other statements on this fact are finding 1.

```seal
confirms: round-2#2
```
What holds: `RULES` row 26 pins "for these two keys it counts as absent"
(`tests/text/test_the_rules_have_one_owner.py:273`), which stands once in
the template at `templates/setup/config.md:35-36`. Re-run here: `seal
mutate` replaced "it counts as absent wherever" with "it is refused
wherever", and `test_the_owner_states_the_rule[26 ...]` failed alone,
naming that spelling and nothing else (executed). Restored, `git status
--short` printed nothing.

What matched: the comment above `RULES` row 28 now says four files gave
the base order, as the fragment's process row 4 says, and names the
sealer's own steps. That closes the gap round 2 named in prose.

What matched: the fold at `f7e4f8aa3`, apart from what finding 1 names.
G11 and the *Removes* row give `skills/implement/bootstrap.md:139-141`,
`skills/implement/routing-question.md:156-157` and
`skills/commit-pr-convention/SKILL.md:321-323`, and each holds the
restatement at `73a43735c` (executed, `git show`).

What matched: the fix commits `e7f86c9f0` and `7f183aa14` and the fold
`f7e4f8aa3` each carry the `Seal-Routing:` trailer (executed, `git log`
with the trailer format), so round 2's second `## Not judged` row no longer
applies to the commits after it.

Two gaps, no finding. *Scope* item 5's list at `frame/design.md:53-60`
does not name the four restatements the fold added to G11 and *Removes*.
Its lead, "Each restatement becomes a citation of that paragraph", covers
them, and the *Removes* row names each, so no reader is sent wrong. The
comment above `RULES` row 26
(`tests/text/test_the_rules_have_one_owner.py:258-263`) says "eight files,
the template among them, each said how a language key is absent or what an
absent one does", the count finding 1 corrects in the fragment. Only
whoever next edits the row reads it. `trail/phases/phase-2.md:135` gives
`skills/commit-pr-convention/SKILL.md:317-319` where the sentence is
`:317-318`; the range holds it.

The writing-style step of the crafter, framer and proofer definitions
reads the Korean section where `Record language` is Korean. It names which
section to open and not what an absent key does, and `frame/plan.md`
*Overlap with the release* leaves it to #1579.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD, which `gaps.md` labels `unverified`. The label is honest: no party has run them. Once finding 1's fix lands, which touches the work item's records alone, the broad run and then the sealer come due | `seal/threads/1795390622-the-root-places-omit-agentic-seal/gaps.md:7` | the orchestrator, at the broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_waiver_decided_at_start.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_review_axes.py tests/text/test_the_chain_section_has_one_shape.py tests/text/test_the_settings_have_a_front_door.py -q` | exit 0, 528 passed, 5 warnings |
| `bin/seal mutate templates/setup/config.md --replace 'it counts as absent wherever' 'it is refused wherever' --tests 'bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k "owner_states_the_rule and 26"'` | red: 1 failed, naming `for these two keys it counts as absent` |
| `bin/seal mutate skills/implement/bootstrap.md --replace '*An absent language key is a refusal at the' '*An absent language key is a rejection at the' --tests 'bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist'` | red: 2 failed, each naming `skills/implement/bootstrap.md:142` |
| `git grep -n -i -E` over the shipped roots for the absent-key wordings named above | hits only in the memo's six, the rewritten five, `README.md:128` and `README.ko.md:132` on who asks, and lines on other subjects |
| `python3 skills/code-review/scripts/chain_check.py --baseline 641b6bfb5 --root . --worktree`, before this record was written | exit 0. It named round 2's two findings and the commit `e7f86c9f0` as owing a verifying round, `trail/gate.md` and `guarantee.md` as not yet written, and no notice at a line of `frame/design.md` |
| the same command, with this record written | exit 0. Finding 1 is named as open for having no close block, which the fix pass appends, and nothing else in this record is refused |
