# 1792540458-on-demand-files-state-the-current-rule — phase 6

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | 5fa12c17 |


## What this phase was asked

The smaller skills rewritten to the current rule: `commit-pr-convention`,
`config`, `legacy-parity`, `gap-analysis`, `parity-setup`, `security-audit`,
`testing`, `feature-planner`, `confidence-check`, `learn`, `audit`, `debug`,
`build-fix`, `checkpoint` and `skills/writing-style/outside-the-review.md`.
The orchestrator added the rest of `skills/update/SKILL.md` and
`skills/preset-setup/SKILL.md`, whose copy sentences phase 3 had rewritten.
In `commit-pr-convention` *Branch names*, the issue-number rule of `spec.md`
Scope 5 in place, the `perf/403-…` example gone and the restated shape a
link. `skills/config/SKILL.md`'s criterion citation moves to the form without
a section sign, and `tests/test_the_rules_have_one_owner.py` follows it. Every
imperative sentence whose actor or condition the smith had to choose is listed
here for the warden.

## What this phase found

**The frame holds for this phase, with one note.** Scope 7 rewrites every
skill but five; `skills/evidence-check/` is in none of `plan.md`'s cells, and
it carries no Markdown file (executed `git ls-files`), so there is nothing of
it to rewrite.

**Two stored counts were false.** `skills/config/SKILL.md` told the session to
print "all nine" rows over a table of eight, and the case that pinned the
clause pinned the count with it; the sentence now says every row of the table
below. `commit-pr-convention` quoted `writing-style`'s description as
`NOT for: … branch/commit format`, a wording that description no longer has;
the opening now states the split between the two skills without the quote.

**"you" and "a session" in files more than one party opens.**
`commit-pr-convention` is read by the smith and by the orchestrator, so it
now names that reader **the writer** in its opening and uses the word
throughout. `legacy-parity` named the second writer of the parity mark "a
session where it compared without one"; the scribe, the smith and the warden
are each a session, so the sentence names the orchestrator. The command skills
a person invokes (`config`, `update`, `preset-setup`, `parity-setup`) are read
by the one session running the command, and their openings now say so;
`update` used "you" for both the session and the user, and now says "the
user" wherever the user is meant. Its printed output still addresses the user
as "you", because that is text the user reads.

**Symbols.** Every dash used as a separator in a heading, a description or a
sentence, every arrow (including the parity skills' `↔` and the output
templates' `→` and `↳`), every middle dot and every slash between
alternatives became words, across all seventeen files. Two dashes stay, each
inside the name of a heading another file owns: `templates/config.md`
*Choosing a value — the criterion* (phase 7's file) and `writing-style`'s
「먼저 — 무엇을 쓰는 글인가」 (out of scope). No file of this phase holds a section
sign (S8, executed `grep`).

**No heading another file cites changed.** The titles of the seventeen files
lost their dashes and no file cites a title (S14, executed `git grep` for each
old title outside `seal/`, `changelog/` and `docs/`).

**Census (S11): what left, and why it could go.**

| What left | Grounds |
|---|---|
| `commit-pr-convention`: the quoted `NOT for` line of `writing-style` | stale; the split between the two skills is stated directly |
| *In one session the prefix rule and the language rule were each broken once* | anecdote; the reason stays: a list on screen is not a comparison made |
| *which is how two headings went missing from it once already* | history; the rule that a hand-copied list drifts stays |
| *This file used to require English of everyone* | history; what a repository says in one row stays |
| *a skill that only said "follow the log" would have nothing to offer there* | reasoning restated by the clause before it |
| the hosted document's *One was tried and failed three ways at once* | the three reasons stay, stated as properties of a hosted document |
| *`writing-style` has the reasoning and the incident* | the incident; the pointer stays |
| *Branch names stay ASCII* — `<prefix>/<kebab-case-slug>` — | the restated shape; the bullet links *Branch names* (Scope 5) |
| `perf/403-repositories-built-one-git-call-at-a-time` | its number reads as an issue under the rule (Scope 5); the example is this work item's own branch |
| `fix/issue-88` as the bad example | a near miss of the new shape; `fix/88`, a number with no slug, is the bad example |
| `config`: *until now the only way to see any of it was to open a file nobody has a reason to open* | history |
| *that example used to be the table every gate read, and the broad run ran its command (#429)* | history; the rule stays in the conditional |
| *this bullet used to carry the third of them on its own* | history |
| the pipe sentence restating `templates/config.md` | the template's *What is refused, and what stays allowed* states it; the skill links it |
| the copy instruction's wording shared with the bootstrap in `skills/implement/orchestration.md` | reworded at the config skill's own act; both acts keep their instruction |
| `update`: *Running only the second reports* | reworded to "Run alone, the second reports"; no content left |
| `outside-the-review.md`: *`skills/writing-style/SKILL.md` 이 담고 있던 세 절이다* and `(#265)` | history; who opens the file stays |
| the account of a PR body sent back as too hard, given twice | anecdote; the reason the rule is repeated at each section's head stays once |
| `legacy-parity`, `gap-analysis`, `parity-setup`: *both measured* in the two bare-marker cases, *These are the useful part and they stay* | anecdote and history |
| `confidence-check`: the account of the old weighted score summing to 85 | history; why no score is kept stays in the present |
| `feature-planner` and `confidence-check`: the shared stand-down wording | reworded in `feature-planner` so the pair shares no run; both still name the framer as the party that calls them |

**Cases rewritten or added** (each seen red after 5fa12c17 by `mutation-check`
on the new text, executed):

| Case | What changed |
|---|---|
| new: `tests/test_the_pull_request_language_is_the_repositorys.py#test_branch_names_state_the_issue_number_rule_once` | holds the four shapes in *Branch names*, the exclusion bullet's link, no second shape, and no `perf/403`. Red under four mutations: the release-branch line deleted, `perf/403-…` put back as an example, the shape restated in the bullet, the issue-number shape replaced |
| `tests/test_the_settings_have_a_front_door.py#test_the_skill_shows_rows_that_are_absent` | holds the clause without the count; red with "all nine" put back |
| `tests/test_the_rules_have_one_owner.py`, rule 12 | `skills/config/SKILL.md` names the criterion in the form without a section sign (`CRITERION_LINK`); red with the section sign put back |
| `tests/test_review_axes.py#test_the_record_of_a_comparison_names_its_writer` | holds the orchestrator as the second writer; red with "a session" put back |

**Imperative sentences whose actor or condition the smith chose.**

| Sentence | What was chosen |
|---|---|
| `commit-pr-convention`: *This skill is read by whoever writes a commit, a pull request or a branch name: the smith, and the orchestrator, which also writes the code where `routing.md` answers `Implementation` with `the session`. Below, that party is the writer.* | one defined term for the actor of every instruction in the file |
| *the writer makes the comparison in one line before opening anything* | the moment: before opening anything, as the old text had it |
| *the writer meeting any of these writes English and carries on rather than asking* | the actor, which was "a session" |
| *The writer invents none* | the actor, which was a bare imperative |
| *the writer puts it in the repository as a file and links it from the body* | the actor of the mirror |
| `config`: *A person runs this command to see every row and to change one; the session running it follows the procedure below* | the two parties of a command a person invokes |
| *print every row of the table below with its current value* | the count gone; the table is the list |
| *copy from `templates/config.md` the row with its `## Broad gate` section, stopping where its `### What is refused, and what stays allowed` subsection starts* | the boundary named by the two headings |
| `legacy-parity`: *the warden in a review round, and the orchestrator where it compared with no review round* | the party, which was "a session" |
| `update`, `preset-setup`, `parity-setup`: *The user runs this command; the session running it …* | the two parties; "the user" wherever the person is meant |
| `update`: *a directory whose `.in_use/` names a live PID is never deleted* | stated as a rule on the directory, which was an imperative to an unnamed reader |
| `feature-planner`, `confidence-check`: *NOT for: loading unasked while the framer is driving a work item, since the framer calls it …* | the framer named as the caller; the phrase `framer is driving` stays, as `tests/test_chain_hooks_hardening.py` reads it |

**Restatement pairs of these files** (Scope 10, measured at 5fa12c17 with the
module's own `shared_counts`, executed):

| Pair | Measured | `BASELINE` | Whose the residue is |
|---|---|---|---|
| `skills/confidence-check/SKILL.md`, `skills/feature-planner/SKILL.md` | 0 | 6 | drained; phase 9 removes the entry |
| `skills/config/SKILL.md`, `skills/implement/orchestration.md` | 0 | 5 | drained; phase 9 removes the entry |
| `skills/config/SKILL.md`, `templates/config.md` | 0 | 2 | drained; phase 9 removes the entry |
| `skills/config/SKILL.md`, `skills/implement/SKILL.md` | 0 | 1 | drained; phase 9 removes the entry |
| `skills/commit-pr-convention/SKILL.md`, `templates/config.md` | 0 | 9 | drained; phase 9 removes the entry |
| `skills/implement/SKILL.md`, `skills/legacy-parity/SKILL.md` | 0 | 1 | drained; phase 9 removes the entry |
| `skills/writing-style/SKILL.md`, `skills/writing-style/outside-the-review.md` | 0 | 3 | drained; phase 9 removes the entry |
| `README.md`, `skills/update/SKILL.md` | 0 | 9 | drained; phase 9 removes the entry |
| `README.md`, `skills/config/SKILL.md` | 22 | 22 | the README's: its paragraph on switching to shared restates the skill's *Before switching to shared, say what cannot be undone*, and the README is outside this item beyond its block rows |
| `README.md`, `skills/parity-setup/SKILL.md` | 1 | 1 | the README's, the waiver's pathspec clause |

**Bytes, for S13** (executed `wc -c`, b3154f43 and 5fa12c17): the framer's
`confidence-check` 3,150 to 3,067 and `feature-planner` 2,400 to 2,465; the
smith's and the warden's `legacy-parity` 5,369 to 5,402. Words in place of
symbols and a named actor make the shortest files a few bytes longer. Phase 9
reads each agent's whole set against b3154f43. The warden's set
(`skills/code-review/SKILL.md`, `writing-style`, `templates/sdd-round.md`,
`legacy-parity`, `templates/config.md`) has gained phase 1's writing section
and these 33 bytes, and none of its files is shortened before phases 7 and 9,
so that reading is the one that says whether S13 holds for the warden.
The other files: `commit-pr-convention` 10,866 to 10,808, `config` 10,380 to
10,330, `gap-analysis` 5,496 to 5,325, `parity-setup` 3,797 to 3,922,
`update` 9,774 to 9,690, `preset-setup` 2,776 to 2,704,
`outside-the-review.md` 7,861 to 7,638.
