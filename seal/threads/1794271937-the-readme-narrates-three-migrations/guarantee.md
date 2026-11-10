# Guarantee: 1794271937-the-readme-narrates-three-migrations

Audited on 2026-11-10 by the sealer, at `ee6a67128` against the base
`release/v0.37.1`, whose upstream resolved to `c5dad8d8c` (`executed`:
`git rev-parse --verify --quiet 'release/v0.37.1@{upstream}'`). The branch
forked at `8657297d5`, and the two commits on the base since then touch no
file this branch changes, so `git merge-tree --write-tree c5dad8d8c HEAD`
exits 0 (`executed`). The gate record `trail/gate.md` names
`run: 5258bd63c against c5dad8d8c`. `5258bd63c` is an ancestor of HEAD, and
the one commit after it, `ee6a67128`, touches only `trail/gate.md`
(`executed`: `git log --no-merges --name-only 5258bd63c..HEAD ^c5dad8d8c`).
`seal pr-body <item> --body <file> --check` exited 0 with both the
installed plugin's `seal` and the tree's `bin/seal` (`executed`). The
repository declares no `seal/parity.json` (`executed`: `ls seal/`), so no
comparison with an original is owed. `seal/config.json` names English for
both language keys, and no `pr.<lang>.md` stands.

The broad gate's pass is the orchestrator's account; the sealer read
`trail/gate.md` at HEAD and ran nothing broad (`read`, contract rule 2).

## Claims re-run

The sample is the phase record's `seen red` claims that neither round
re-ran (the Korean edition, the two `stamp.py` absence asserts, the citation
and record-path asserts, the wrap entry), plus the template exemption, on
which the route change rests. Each ran in a scratch clone at `ee6a67128`,
removed afterwards; the tree under audit was not changed.

| Claim | Source | Command | Result |
|---|---|---|---|
| The plan's narrow modules pass at HEAD | `frame/plan.md` *Phases*, row 1; `trail/phases/phase-1.md`, its last paragraph | `bin/test -q` over the seven modules of plan row 1 and `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` | Holds. 270 passed, exit 0 (`executed`) |
| `README.ko.md`'s new launcher sentence assert is red against the old Korean text | `trail/phases/phase-1.md`, the `seen red` table, row 3 | `README.ko.md` restored from `c5dad8d8c`, then `bin/test -p no:xdist` on `test_both_readmes_say_what_the_stamp_hook_writes_and_leaves` | Holds. Exit 1, failing at `:367` on the `said` assert for `('README.ko.md', '0.33.0 부터 0.34.1 까지의 … wrote*).')` (`executed`) |
| *The stamp* cites step 4b, red against the old policy text | `trail/phases/phase-1.md`, the `seen red` table, row 5 | `docs/checks/the-stamp.md` restored from `c5dad8d8c`, then `bin/test -p no:xdist` on `test_the_policy_names_the_command_the_marker_and_the_command_to_draw` | Holds. Exit 1, failing on the citation assert (`executed`) |
| `README.md` no longer holds "a launcher, `stamp.py`" (absence) | `trail/phases/phase-1.md`, the `seen red` table, row 2 | `bin/seal mutate README.md`, that phrase added before "No session stops another", the stamp-README case alone | Holds. `red`; the failing line is the `gone` assert at `:369`, `('README.md', 'a launcher, \`stamp.py\`')` (`executed`) |
| `README.ko.md` no longer holds "실행기 `stamp.py`" (absence) | `trail/phases/phase-1.md`, the `seen red` table, row 4 | `bin/seal mutate README.ko.md`, that phrase added before "다른 세션이 쓰고 있는", the same case | Holds. `red`; the failing line is `('README.ko.md', '실행기 \`stamp.py\`')` (`executed`) |
| `${CLAUDE_PLUGIN_DATA}/stamp.py` is gone from *The stamp* (absence) | `trail/phases/phase-1.md`, the `seen red` table, row 7 | `bin/seal mutate docs/checks/the-stamp.md`, a sentence naming it added after "claims the file first.", the policy case alone | Holds. `red`; the failing line is the absence assert at `:199` (`executed`) |
| The measurement clause cites the `docs/experiments/` record | `trail/phases/phase-1.md`, the `seen red` table, row 9 | `bin/seal mutate docs/checks/the-stamp.md`, the record's path replaced by "the owner's record says", the policy case alone | Holds. `red`; the failing line is `` assert "`docs/experiments/2026-11-06-" in unchecked `` (`executed`) |
| The wrap list covers the new record | `trail/phases/phase-1.md`, the `seen red` table, row 10; `frame/design.md` *Scope* item 5 | A 105-column line appended to the record, `bin/test -p no:xdist tests/behaviour/test_docs_line_wrap.py`; then the same with the list entry removed | Holds. With the entry: exit 1, `…plugin-hook.md:71 is 105 columns (limit 88)`. Without it: 46 passed, exit 0, so the entry is what makes the line red (`executed`) |
| The template exemption is what keeps the case green | `trail/phases/phase-1.md`, the `seen red` table, row 11; `routing.md` *Why this way*, the Review row | `bin/seal mutate` with `READ_BY_AN_EARLIER_RELEASE = ()`, `test_every_template_is_named_by_a_document_that_ships` alone | Holds. `red`, naming `['templates/setup/claude-md-block.md']` (`executed`) |
| Acceptance row 1: neither README names `agentic:start`, `claude-md-block` or `` `stamp.py` `` | `frame/design.md` *User scenarios & acceptance*, row 1 | ``git grep -n -e 'agentic:start' -e 'claude-md-block' -e '`stamp.py`' -- README.md README.ko.md`` | Holds. No output, exit 1 (`executed`) |
| Acceptance row 2: `seal mode` stands in *Updating* and *업데이트* | `frame/design.md` *User scenarios & acceptance*, row 2 | `git grep -n 'seal mode' -- README.md README.ko.md` | Holds. `README.md:99` and `README.ko.md:104`, besides the command listings (`executed`) |
| The experiment record transcribes issue #1376's comment 6675898172 | `frame/design.md` *Scope* item 5; `changelog.md` *Changed*, the second item | `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6675898172` | Holds. The comment is the owner's, of 2026-11-06; its *The terminal stamp* names Claude Code 2.1.319 and a scratch plugin, and its four facts, their marks and the seven surfaces match the record's *What it established* and *Results* (`executed`, then `read`) |
| The removal date is 90 days after 0.37.0, and the span each path covers | `frame/design.md` G6 and *Scope* item 7; `changelog.md`, the *Updating* line | `gh release view` for `v0.37.0`, `v0.35.0`, `v0.25.0`; `git tag -l` for the 0.23, 0.24, 0.33, 0.34 and 0.36 tags | Holds. 0.37.0 was published 2026-11-09, and 90 days later is 2027-02-07; 0.35.0 on 2026-11-08, 0.25.0 on 2026-10-30; the last 0.24 tag is `v0.24.2` and the last 0.34 tag `v0.34.1` (`executed`) |
| The README's old `config.md` paragraph copied the 0.37.0 note | `changelog.md` *Changed*, the first item; `frame/design.md` G3 | `gh release view v0.37.0 --json body` | Holds. Line 77 of the note holds the exit-2 / exits-1 / defaults account the README held (`executed`) |
| Each quote of `pr.md` stands in its source | `pr.md` | Each quote, whitespace collapsed, searched in the file it names | Holds. Seven of seven found (`executed`) |

The `## Removes` rows, each checked against the tree at HEAD:

| Removes row | Command | Result |
|---|---|---|
| The `CLAUDE.md` block paragraph, its markers, the empty marker pair, the template's name | `git grep -n -F -e 'agentic:start' -e 'agentic:end' -e 'claude-md-block' -e 'empty marker' -e '빈 표시' -- README.md README.ko.md` | Gone. No output, exit 1 (`executed`) |
| The `config.md` paragraph's account of which commands exit 2, refuse or read defaults | `git grep` for `exit 2`, `exits 2`, `exits 1`, `종료 코드`, `mode --check` over both READMEs, and a read of *Updating* and *업데이트* | Gone. The only hits are the `seal mode --check` lines of the command listings, which the account did not hold (`executed`, `read`) |
| The launcher's description in both READMEs | `git grep` for `stamp.py`, the `Stop` entry, "names both", "이 둘을" over both READMEs | Gone. The only hits are `seal_stamp.py --stop`, the plugin's own hook (`executed`) |
| The launcher's description in `docs/checks/the-stamp.md` | `git grep -F` for `CLAUDE_PLUGIN_DATA}/stamp.py` and "until the person removes" | Gone (`executed`) |
| "the owner's spike of 2026-11-06" | `git grep -F` for "owner's spike" and "spike" in `docs/checks/the-stamp.md` | Gone (`executed`) |
| The old pins on the launcher sentence | `git grep -F` for "names both for you to take out by hand" and "이 둘을 알려 주면" over `tests/` | Gone (`executed`) |
| The issue's *Done when*: the launcher described in `skills/update/SKILL.md` alone | `git grep -n -i` for `launcher`, `stamp-hooks`, `/stamp.py`, `0.33.0` outside `tests/` and `seal/threads/`, and for `stamp.py` not preceded by `_` | Holds. The description stands only in `skills/update/SKILL.md:215-233`; the READMEs and `the-stamp.md` cite step 4b; the other `launcher` hits are `lib/launch.py`'s interpreter launcher (`executed`) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | One *Updating* paragraph that names what `/agentic:update` does for an earlier release and links to the update skill, keeping the `seal mode` line and the three hand-rewritten files; one linking sentence for the launcher in each edition; `the-stamp.md` cites step 4b and a dated `docs/experiments/` record; the cases change in place; every compatibility path leaves in the first release cut on or after 2027-02-07; seven `## Removes` rows | The issue's *Change* and *Done when*; the diff; the removal checks above | none |
| the build | Phase 1 delivers *Scope* items 1 to 6 and the changelog's *Updating* sentence, closing at `11ea31d92`; it names three frame claims that did not hold and the exemption it added, each with grounds; `phase-1.md` stands for phase 1, the one phase whose Status holds a commit (`routing.md` answers `crafter`) | The design as folded; the diff; every `seen red` sampled above | none. Its line "Its *Method* carries a re-run outline and says it is the comment's account" states the record at the phase's commit; round 1 finding 2 corrected the record and round 2 read the line as such |
| the last round | Round 2, at `5d834a711`: no findings; it confirms each of round 1's three closes. Only `round-2.md` and `trail/gate.md` follow its target | The diff at HEAD (both READMEs, the experiment record's *Method*, `frame/plan.md` *Technical context*); the acceptance greps re-run above | none |
| the changelog | *Changed*: the READMEs send a person to `/agentic:update` and keep the `seal mode` line and the three files; each edition carries one launcher sentence with a link to step 4b; `the-stamp.md` cites step 4b and the dated record. *Updating*: the three paths leave together in the first release cut on or after 2027-02-07 | The diff; the comment; the release dates and tags; the 0.37.0 note; `lib/config.py#unconverted_config` and `#unconverted_parity` | none |
| the orchestrator's part of the pull request body | Seven quotes of `changelog.md`, `frame/design.md`, `routing.md` and `frame/plan.md`, and `Closes #1492.` | Each quote stands at the coordinate it names | none |
| `routing.md` *Why this way* (the orchestrator's grounds under `agentic`) | Framer and crafter; the review changed after phase 1 to the review chain because the build exempted a template in a check | The diff: outside `seal/threads/` it changes the two READMEs, `docs/checks/the-stamp.md`, the new record, the wrap list, the stamp cases and the one exemption the grounds name, which the plan's *Technical context* lists whole | none |

The 2027-02-07 date is a default the frame states as the owner's to set at
the pull request (`frame/design.md` *Scope* item 7, `frame/questions.md`);
the sealer guarantees that every record states it the same way, not that
90 days is right.

```seal
target: ee6a6712875efb9275e67eb91487d5fa6fa67fb6 against c5dad8d8ccdb82ac166e0087f3094b3e440da386
Verdict: sealed
```
