# Implementation Plan: 1793457437-readers-state-the-shapes-they-pass

## Technical context

No reader changes. The work writes three sentences in place and pins each one, puts one marker on two existing cases for the rule `## Rule changes` adds, and leaves the two `docs/` items to the settle. Each reader was probed at `a92c358b` (`frame/design.md` *Grounding*).

- `templates/setup/seal-README.md` and `seal/README.md`, the paragraph *The first line of this file is the marker*. `tests/behaviour/test_first_setup_asks_once.py` holds the two byte-identical, so one edit lands in both. `hooks/lib/optin.py#marked`, lines 191-212, compares the first line with `\r\n` stripped and nothing else.
- `templates/setup/config.md`, the paragraph **This file is optional, and an absent row is not an error, with two exceptions** at lines 11-15. `hooks/lib/config.py#value_of`, line 529, compares `found == item`.
- `evals/README.md`, the paragraph that ends `Nothing in the tree makes a later edit owe a run.` at line 62. `evals/scripts/noninferiority.py#header_field`, line 1058, matches `^\| <name> \| (?P<v>[^|]*) \|$`, and `parse_record`, line 1066, reads each of the four row counts with `or 0`.
- `tests/github/test_release_completeness_check.py`: the parametrized case ending at line 327 and `test_a_milestone_that_does_not_exist_says_it_verified_nothing` at line 330 already hold the R27 rule. The module carries `@pytest.mark.rule("a-patch-carries-no-feat")` on other cases, and `.github/scripts/rules.py#markers` is what a check line's marker is read against.
- Test modules that read a changed path, for the phase's narrow run: `tests/hooks/test_optin.py`, `tests/hooks/test_config.py`, `tests/evals/test_noninferiority.py`, `tests/github/test_release_completeness_check.py`, `tests/behaviour/test_first_setup_asks_once.py`, `tests/behaviour/test_the_set_a_work_item_always_has.py`, `tests/text/test_the_records_can_be_carried_out_and_in.py`, and every module `git grep -l` finds naming `templates/setup/config.md`, `seal-README` or `evals/README` (ten and more, among them `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_one_word_one_meaning.py` and `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py`). That list is a sample from three searches, and the crafter makes it whole by the method contract rule 2 names.

**The failure scenario of the chosen approach, six months on.** A writer starts producing one of these shapes, for example a release script that cuts `release/X.Y.Z` without the `v`. The sentence states the limit, and nothing refuses the shape, so the release check exits 0 with its one line as the only trace. The other direction is the one the pins are for: a reader made tolerant, such as `marked` stripping spaces, turns its case red, and whoever made the reader tolerant rewrites the sentence in the same change.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Replace each limit with a guard: each reader refuses or names the near miss it now passes. | Five readers grow code and cases for shapes no writer of the one-issue flow produces. `skills/core/SKILL.md` *The rule a mechanism is kept against* keeps a mechanism by what it caught, and #956's audit classed all five `limit` with no catch to show. | Rejected. The premise that keeps the readers was checked: setup writes the README from the template (`tests/hooks/test_optin.py#test_the_template_opens_with_the_marker`), `seal mode` writes `config.md`, `compare` renders the record, and the release automation names the branch and the milestone. |
| R2: write the sentence in `docs/the-review-record.md` *The round record*, as the ticket asks. | The sentence would describe `chain_check.py#grammar`, which `7a8899d5` removed with the two tables it read. `hooks/lib/fields.py#BLANK` now refuses a blank line in a block, so the sentence would state a direction no reader takes. | Rejected. The row is closed with its coordinates in `frame/design.md` *Grounding*. |
| R20: write the sentence in `docs/the-routing-check.md`, as the ticket asks. | `hooks/stub-remove.py` was removed in `5560c742` and the section is gone, so the sentence would have no reader and no home. | Rejected, closed the same way. |
| R18: a sentence in `skills/implement/bootstrap.md` *Orchestrator: Bootstrap*, as the ticket asks (the bootstrap moved there from `skills/implement/orchestration.md`). | The bootstrap writes `config.md` through `seal mode`, which never writes a refused table, so the orchestrator reading that step never meets the shape. `templates/setup/config.md` *Repository config* already says a refused table is a refusal and the mode gate is silent on one, so the bootstrap's sentence would be a second copy of that fact. | Rejected. The template is the one source, and the person who hand-edits `config.md` reads it. |
| R19: a sentence in `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, as the ticket asks. | That section is read by sessions and agents, and none of them edits the README's first line. The person who does reads `Leave the line as it is.` in the README itself, and nothing tells them a trailing space breaks it. | Rejected for `templates/setup/seal-README.md` and its byte-identical copy `seal/README.md`, where that person acts. |
| R19: a `## Rule changes` item in `docs/one-root-by-lifetime.md` *The opt-in signal is the root itself*, the policy home of the opt-in rule. | The document has a Korean edition that must carry the same folds, so it costs two items and a translated sentence. The reader who acts still meets the sentence only in the README. | Rejected. The policy says the README opens with the marker, and the README's own paragraph says what counts as opening with it. |
| R30: the sentence in `templates/setup/config.md` *The fold's values*, for `Policy root` alone, as the ticket asks. | `hooks/lib/config.py#value_of` compares every item exactly, so `record language` or `Broad Gate` reads as absent the same way. A sentence for one row leaves the rest of the class unwritten, which contract rule 12 forbids. | Rejected for one sentence in the file's opening paragraph on absent rows, which covers every item. |
| Name `check: none reader:` for the new sentences, or no case at all, since the ticket says *No code changes*. | `skills/implement/SKILL.md` *2.* keeps `check: none` for a rule no case can hold, and a case holds each of these. Without one, a reader made tolerant leaves the sentence false and nothing turns red. | Rejected. The ticket's *No code changes* is read as no reader changes, which its own body says (*a limit sentence ..., not a guard*). Cases and a marker are tests, not readers. |
| R27's check line names `tests/github/test_release_completeness_check.py`, a file. | `skills/settle/SKILL.md` *A rule has one shape* gives a marker to a rule whose test drives a script that can fail a required pull-request job, and the release check is one, as `a-patch-carries-no-feat` already shows. | Rejected for the marker `a-release-is-judged-under-its-two-names` on the two existing cases. |
| R16: correct only the `config.md` clause and leave `Those rows are the places a line nobody wrote live declares something`. | After the correction the `config.md` row declares nothing, and `Those rows` would still read as counting it. | Rejected. The one `change` item also narrows that sentence to `Those routing.md rows`. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2, 3 and 4 | The narrow run, in one command, of the test modules that read a changed path (*Technical context*). Each new id or case is seen red before it is committed, by a mutation of its reader in a scratch clone: `marked` comparing a stripped line (item 1), `value_of` folding case (item 2), `header_field` accepting any spacing (item 3). The phase record names each mutation and its red. `.github/scripts/rules.py#markers` lists `a-release-is-judged-under-its-two-names` on exactly the two cases (item 4). | 805a97c8 |

## Operational impact

None. No reader, hook, command or config row changes, and nothing a deployer runs is new.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-01 | *Scope* items 1 and 3 are folded to the sentences round 1's fix pass wrote (fd549f8e, b5a4d754): the marker sentence names the root under the git directory, and the count sentence names the row shape `header_field` reads | Both findings were the frame's own wording carried into the build; the next crafter and the verifying round read the frame | `skills/code-review/orchestration.md` *The fix pass then finds what the fixes left standing* |
