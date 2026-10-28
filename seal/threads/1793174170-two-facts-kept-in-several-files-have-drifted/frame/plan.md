# Implementation Plan: 1793174170-two-facts-kept-in-several-files-have-drifted

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 to 5.

## Summary

Issue #1055 lists seven facts that the tree keeps in more than one file. The
work gives each fact one source, and makes every other place link to it or be
derived from it by a case that fails on a difference. Counts in prose go, and
cases read the lists the counts stood for. The gate table is derived from
`hooks/dispatch.py#GROUPS`, and the skills row from the skills' frontmatter.
The way back before the commit to shared is told once, in
`skills/config/SKILL.md`. The shipped workflow is the one source of the two
steps it shares with the repository's workflow. The outline case reads every
edition pair. The two pasted passages leave `BASELINE`, and the plugin's
description is derived from `plugin.json`. One rule is added to the policy
through `## Rule changes`: `docs/the-session-hooks.md` *Registration* says
that the gate table is derived from `GROUPS`.

## Technical context

What the work builds on. Each coordinate was read at `5287dd42`:

- `hooks/dispatch.py:81-105`, `GROUPS`: nine groups naming 15 distinct
  scripts. `worktree-guard.py` and `session-lease.py` each stand in two
  groups, and `worktree_consent.py` in two (read).
- `README.md:172-184` and `README.ko.md:166-178`: the gate tables, 13 rows
  each. Their first cells are the script names without `.py`, which
  `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:391`
  already reads that way (read).
- `tests/behaviour/test_chain_hooks_hardening.py:237-421`: the three
  README-skills cases. `test_every_shipped_skill_is_named_in_both_readmes`
  (`:297`) derives membership. The other two derive counts and spell them
  through `NUMBER_WORDS` and a `spellings` table (read).
- `skills/config/SKILL.md:163-176`: the section on switching to shared. It
  is pinned by `tests/text/test_the_settings_have_a_front_door.py:111-119` on
  "point of no return", "before running the command" and
  "git reset -- :/seal" (read).
- `skills/implement/scripts/seal.py#indexed` (`:1755-1800`) refuses a switch
  over a staged edit. That is the claim the README's reason sentence makes,
  and it moves into the skill section (read).
- `templates/setup/hygiene.yml:1-96` and `.github/workflows/hygiene.yml:1-162`.
  The repository's file runs the two shared steps from the tree, and the
  template runs them from a clone at `"$RUNNER_TEMP/agentic"` (`:52-56`).
  `tests/text/test_ci_gives_the_checks_what_they_need.py#read` reads
  `.github/workflows/` only (read). `tests/e2e/teammate/test_teammate_flow.py`
  targets the template and must stay green with the two added keys.
- `tests/behaviour/test_both_editions_carry_the_same_folds.py:60-72`:
  `pairs` and `read` join under `docs/` (read).
- `tests/text/test_no_passage_is_pasted_into_a_second_file.py:189-221`:
  `BASELINE`, with the two entries at `:213` and `:219` (read).
- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`: one
  sentence, three times, equal today (read).

The chosen approach's failure scenario, six months on: a hook is added to
`GROUPS` and its pull request does not touch either README. S1's case goes
red on that pull request, which is the intent. The cost is one table row in
each edition for every hook. A contributor who reads the red as noise could
add a row with an empty Does cell. The case reads names, not content, so it
would not see that. The proofer reads the row's content, and nothing else
does.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Gate list: keep the gate table, drop the count and the lists of names in prose, and derive the table's rows from `GROUPS` by a case | Covered under *Technical context*: the case sees a row's name and not its content | Chosen |
| Gate list: keep "Nine of the thirteen", and add a case that compares the number with `GROUPS` | The case needs a table of number words in two languages, a stored list beside the tree that `CLAUDE.md` forbids. A count that matches can still hide a missing row, which is the state today: 13 rows and 15 scripts | Rejected |
| Gate list: replace the table with a link to `hooks/dispatch.py` (the structure removed) | The table is the one place a person learns when each gate fires, what it does and where it acts. `GROUPS` names files and events and says none of that. A link moves the reader into Python to learn what runs on their machine | Rejected. The premise that keeps the table was checked: no other document holds Fires, Does and Where for every gate. `docs/the-session-hooks.md` covers registration and two hooks only (read, `:1-60`) |
| `worktree_consent` and `root-migrate`: give each a row | Two rows to write in two languages, and #1102 rewrites them later | Chosen. Both scripts write to disk on a person's machine: `<git-common-dir>/agentic-worktree-consent/`, and staged moves in the tree (read, the two docstrings) |
| `worktree_consent` and `root-migrate`: an exemption list in the case | A second list of hook names beside `GROUPS`, kept by hand, and the inventory keeps omitting two scripts that write | Rejected |
| Skill counts: drop the numbers, and replace the two count cases with one membership case | The membership case can be satisfied by a row that lists the right names in the wrong sentence. The case reads the on-demand sentence, as the count case reads its phrase today | Chosen |
| Skill counts: keep the numbers and `NUMBER_WORDS` | Every release that ships a skill at a new count edits a spelling table in a test, which is the stored count the issue names | Rejected |
| The way back before the commit to shared: `skills/config/SKILL.md` is the home, and the READMEs link to it | A person reading the README needs one more click to see the command. `seal mode shared` prints the command at the moment of the switch, so the person meets it there anyway (`seal.py:2546-2556`) | Chosen. The skill is where the warning is said before the act, and its case already pins the command |
| The way back: the README is the home, and the skill links to it | #1102 rewrites the README last in the milestone, so the home would move under a rewrite. An agent would also have to open the README at the moment of acting | Rejected |
| The way back: `docs/one-root-by-lifetime.md` *Shared or local* is the home, through a `change` in `## Rule changes` | The policy has a Korean edition, so the command would stand twice again. Until the settle after the release, the policy would not hold the command, and the skill would link to text that is not there | Rejected. The policy keeps the rule, and the skill section cites it |
| Shared workflow steps: the template is the source of comments and steps, and a case compares the `run:` bodies | A step added to the template alone is not seen as missing from the repository's file unless the case pairs by the template's names. It does | Chosen |
| Shared workflow steps: the repository's workflow calls the template as a reusable workflow, replacing the structure | The template clones the plugin at a released tag (`templates/setup/hygiene.yml:52-56`). The repository's pull requests would then be checked by the last release's `chain_check.py`, not the branch's, so a change to the checker would ship unchecked by itself | Rejected. Keeping two files was weighed and holds on this premise: the repository has to run the checker from its own tree |
| Shared workflow steps: generate `.github/workflows/hygiene.yml` from the template | A generator is a second mechanism to keep, and the repository's file carries steps the template does not have (release steps, the issue-claims report) | Rejected |
| Template: add `permissions: contents: read` only, as the issue's item 3 names | The template's runs are not cancelled when a newer push supersedes them, against the reason `test_ci_gives_the_checks_what_they_need.py` states for every pull-request workflow | Rejected |
| Template: add `permissions: contents: read` and `concurrency` | An installed copy changes only when the person reinstalls it (template header `:11-12`), so existing users do not get the keys until then | Chosen |
| Plugin description: a case that fails when a `marketplace.json` description differs from `plugin.json`'s | Three copies stay in the tree, held by a case | Chosen |
| Plugin description: delete the two `marketplace.json` copies | How the marketplace listing renders without them is not visible from this tree, and no case here can see it | Rejected |
| Edition pairs: `pairs()` lists every tracked `X.ko.md` beside an `X.md` | A `.ko.md` added under `seal/` or `changelog/` would be read too. None exists (executed, `git ls-files "*.ko.md"`: four files) | Chosen |
| Edition pairs: a list of pairs kept in the case | A stored list beside the tree, which is how `docs/experiments/` went unread | Rejected |
| The workflow step "both READMEs move together": remove it | A sentence edited in one edition only would pass every check, because the outline case reads headings and nothing reads content across two languages | Rejected. Keeping it was weighed on its premise: it reads the diff, which no case does, and it fails nothing, so its cost is one warning line (read, `.github/workflows/hygiene.yml:151-162`) |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The gate inventory. Both READMEs' gate tables gain the `worktree_consent` and `root-migrate` rows. The count and the lists of gate names leave *First run* and the `seal/` row, in both editions, and point at the Where column. S1's case is added, and `test_both_readmes_list_the_stamp_hook` is re-pointed to S2's absence pins | S1 and S2 cases, each seen red as the design says. `tests/behaviour/test_chain_hooks_hardening.py` and `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py` run green | a1f7a177 |
| 2 | Counts in prose. The always-on heading and the CLAUDE.md block row (S3), the hooks that reach the network in both READMEs and `CONTRIBUTING.md` (S4), and the skills row (S5). `NUMBER_WORDS` and the two count cases leave, and S5's membership case replaces them | S3, S4 and S5 cases, each seen red. `tests/behaviour/test_chain_hooks_hardening.py` runs green | e61cd169 |
| 3 | One home for each pasted passage. The way back before the commit to shared is told in `skills/config/SKILL.md` only, and both READMEs link to it (S6). `skills/implement/SKILL.md:355-359` links to `docs/the-agent-set.md` (S7). Both `BASELINE` entries are removed | S6 and S7, each seen red. `tests/behaviour/test_first_setup_asks_once.py`, `tests/text/test_the_settings_have_a_front_door.py` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py` run green | |
| 4 | The shipped workflow as the one source. The template gains `permissions` and `concurrency` (S8). Its chain-step comment names the review record's section instead of listing refusals (S10). The repository's two shared steps lose their comments to a pointer, and the case comparing the steps is added (S9) | S8, S9 and S10, each seen red. `tests/text/test_ci_gives_the_checks_what_they_need.py`, `tests/e2e/teammate/test_teammate_flow.py` and the cases of `tests/skills/test_seal.py` that install the template run green | |
| 5 | Editions and the manifest. `pairs()` reads every tracked pair (S11), the `CONTRIBUTING.md` sentence names every pair (S12), and the plugin description case is added (S13) | S11, S12 and S13, each seen red. `tests/behaviour/test_both_editions_carry_the_same_folds.py` and the module S13 lands in run green | |

## Operational impact

- A repository that already installed the workflow keeps its copy of
  `.github/workflows/hygiene.yml` without `permissions` or `concurrency`.
  `seal pr-checks install` never overwrites an existing file (template header,
  `:7-12`), so the keys reach it only through `seal pr-checks remove` and then
  `seal pr-checks install`. The changelog fragment should say so.
- `permissions: contents: read` narrows the token of the template's job. The
  job's steps check out the repository, clone the public plugin repository,
  and run two scripts that read files and `git`. No step writes and none calls
  `gh` (read, `templates/setup/hygiene.yml:38-96`).
- No migration, no new environment variable, no new dependency.
