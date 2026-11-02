# Design: 1793661729-each-document-is-cut-by-who-opens-it

Issue #1312, the one item of milestone `release: 0.30.0`; it absorbs #1311.
The issue body as it stood on 2026-11-03 after the owner's two grouping
directions were folded in as item 4 of *What changes* (`gh issue view 1312
--json body`, executed by this framer; no comments, executed). The owner's
third direction on 2026-11-03, that the cut respects Claude Code's own
conventions for skills and agents, reached this framer as the orchestrator's
finding: a `claude-code-guide` agent read
https://code.claude.com/docs/en/skills.md,
https://code.claude.com/docs/en/sub-agents.md and
https://code.claude.com/docs/en/plugins-reference.md. Nobody in this frame
opened those pages; the rows below that rest on them say so.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | The policy root is changed only through `## Rule changes`, which the settle after the release writes. Every `docs/` change below is a rule change; the core, the skills, the agent definitions, the scripts and the tests change in this pull request. The same section says the axis between the roots is "lifetime and authority, not audience". This work keeps that axis between the roots and adds a second axis inside the policy root, the reader (D3) |
| `skills/settle/SKILL.md` *Rule changes* and *The index* (read) | `file:` is read only as a top-level `.md` of the policy root (`skills/settle/scripts/rule_changes.py:257-260`, read), and `seal fold` lists top-level documents only (`skills/settle/scripts/fold_check.py:128`, read). Grouping the policy root changes both readers before any design can name a grouped file (D4) |
| `skills/settle/SKILL.md` *A document past its ceiling is split, never trimmed* (read) | It says a document past the ceiling is split "by topic along its own headings". That sentence is a skill's, so this pull request rewrites it to the reader rule |
| `templates/setup/config.md` *The fold's values* (read) | The estimate is UTF-8 bytes halved. `docs/the-review-record.md` is 50,774 bytes, so about 25,387 tokens, past this repository's `Document token ceiling` of 25,000 (`wc -c`, executed; `seal/config.md`, read) |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "A fact has one source, and every other place links to it." Copies go before anything moves (D6). A mechanism this work adds names what it takes out in return (`## Removes`) |
| `skills/core/SKILL.md` *The first value* (read) | The core reaches every party on every spawn, so the new rule is a few sentences and its bytes are paid back inside the same preload (D1) |
| `.github/scripts/release_report.py#preloads` (read) | An agent's preload is the bytes of `agents/<agent>.md` plus the core plus `skills/agent-contract/SKILL.md`. No agent's preload grows (#1254 is the item that settles how a preload rewrite is proved; this item claims only that none grows) |
| `evals/README.md` *The behaviour suite* (read) | "Nothing in the tree makes a later edit owe a run." No paid eval run is taken here |
| `docs/measuring-a-run.md` *Where a reading goes* and the band paragraph (read) | The crafter of a work item that measures the process writes the reading and its weighing in the phase record (D8) |
| `skills/writing-style/SKILL.md` and `skills/writing-style/outside-the-review.md` (read: `SKILL.md:316-324`) | #265 already cut one skill by reader. That cut stands and this work does not reopen it |
| Claude Code skills docs, `skills.md` (orchestrator's finding, not opened here) | A plugin skill is found at `skills/<name>/SKILL.md`; a category level `skills/<group>/<name>/` is not documented. Supporting files sit beside `SKILL.md` and enter context only when read after `SKILL.md` names them and says when; a `SKILL.md` under 500 lines is recommended |
| Claude Code sub-agents docs, `sub-agents.md` and `plugins-reference.md` (orchestrator's finding, not opened here) | A `skills:` list injects each skill's full `SKILL.md`; whether supporting files are injected is not documented, so what every spawn needs stays in the `core` and `agent-contract` bodies. `agents/` is scanned recursively and a subfolder becomes part of the agent's identifier, so grouping `agents/` would rename every agent |
| `git log`, executed by the orchestrator | The settle 0.27.3 to 0.29.0 (95cbd99a4, #1310) landed on `release/v0.30.0` before this item's routing commit. The settle after 0.30.0 is taken to land the same way, on `release/v0.31.0` before its first work item |

### Measured on the tree at 2d38c75af (each executed by this framer, scripts under the scratch directory, since removed)

| What | Reading |
|---|---|
| Section bytes of `docs/the-review-record.md` | *The round record* 10,029; *What the check reads at the pull request* 13,825; *The guarantee* 5,218; *The stamp* 9,658; *The run* 8,065; *The handoff* 2,335 with *The per-segment bars* 1,354 inside it |
| Which agent definitions cite which of its sections | crafter: *The handoff*, *The round record*, *The run*; framer: *The run*; proofer: *The handoff*; sealer: *The guarantee*, *What the check reads at the pull request*; contract rule 10: *The per-segment bars*. No agent cites *The stamp* |
| Agents' Read bytes in the 1,004 subagent transcripts under `~/.claude/projects/-Users-michael-Documents-GitHub-SpecSeal/*/subagents/`, for the agent types `crafter`, `framer`, `proofer`, `sealer` (JSON length of each Read result) | crafter, 78 spawns: `skills/implement/SKILL.md` 100 reads, 2,927,734 bytes. framer, 169 spawns: `skills/implement/SKILL.md` 42 reads, 586,744; `skills/settle/SKILL.md` 17 reads, 233,943; `docs/the-review-record.md` 6 reads, 74,538. proofer, 134 spawns: `skills/code-review/SKILL.md` 30 reads, 325,695; `docs/the-review-record.md` 6 reads, 75,294. sealer, 159 spawns: `docs/the-review-record.md` 2 reads, 21,103 |
| Ten-word runs `docs/the-review-record.md` shares with tracked `.md` and `.py` files outside `seal/` and `evals/` | 1,234 of 8,989 words by this framer's tokenizer (the orchestrator's 835 of 8,716 used another). The largest pairs: *The run* with `hooks/question-gate.py` (85 runs), *The stamp* with `skills/verify/scripts/seal_stamp.py` (60), *What the check reads at the pull request* with `skills/code-review/scripts/chain_check.py` (45), *The guarantee* with `skills/code-review/orchestration.md` (18) and `agents/sealer.md` (10) |
| Mentions of a `docs/<name>.md` path outside `seal/` | 708 lines in 151 files (`git grep -c`) |

The transcripts show where an agent's reading goes: the crafter reads
`skills/implement/SKILL.md` whole about once per spawn and more, and the
framer reads `skills/settle/SKILL.md` for one section. The agents rarely open
`docs/the-review-record.md` at all. The skills cut, which reaches agents with
0.30.0's release, is where most of the reading is saved; the policy-root cut
reaches them only with the release that carries the settle after 0.30.0.

## Scope

In:

1. The core states the rule (D1), and the preload pays for it (D2).
2. The skills an agent reads whole are cut in this pull request (D5):
   `skills/settle/SKILL.md`, `skills/implement/SKILL.md` and
   `skills/verify/SKILL.md`, each keeping in `SKILL.md` what every invocation
   needs.
3. The policy root's readers learn one level of group directories and a
   `move` operation (D4), in this pull request.
4. The policy root is cut and grouped through `## Rule changes` below (D3):
   `docs/the-review-record.md` is cut into five documents by reader, two
   sections of `docs/the-record-layout.md` leave it, and every document of the
   root moves into one of five groups. The settle after 0.30.0 writes it.
5. Copies go before anything moves (D6): the pairs the ten-word census lists
   for `docs/the-review-record.md`, each kept on one side.
6. Every citation moves with its section (D7):
   `tests/behaviour/test_a_cited_section_stands_in_its_file.py` holds each one,
   and its excuser learns to read a citation's path as well as its text.
7. The measurement (D8): a replay of existing transcripts against the new
   layout, with no paid run.

Out, each with its grounds:

- `agents/` is not grouped and no agent's own rules leave its definition:
  grouping renames every agent (sub-agents docs, orchestrator's finding), and
  the issue keeps an agent's own rules out of `agents/*.md` anyway.
- `skills/` gets no category level: a nested `skills/<group>/<name>/SKILL.md`
  is not documented as found (skills docs, orchestrator's finding).
- `skills/*/orchestration.md` (35, 29 and 24 KB) are not cut. One party, the
  orchestrator, reads each, and it reads them in the one session that runs
  the work, so a cut by step turns one read into several in that context.
- `skills/writing-style/` stays as #265 cut it.
- `skills/code-review/SKILL.md`, `skills/commit-pr-convention/SKILL.md`,
  `skills/config/SKILL.md` and `skills/update/SKILL.md`: one party reads each
  at one step.
- The copies of the stamp and of the pull-request check with their code are
  removed on the code side only (D6); their documents go to the group no
  agent opens, so no agent pays for them after the move.
- `.claude-plugin/plugin.json` moving to 0.30.0 is the orchestrator's, in the
  commit that adds the changelog fragment.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The core states the rule | Given any spawn, when it receives the core, then *The first value* holds the cut rule as D1 states it, in at most five sentences | the proofer reads `skills/core/SKILL.md` against D1 |
| S2 No preload grows | Given the base 2d38c75af and HEAD, when each agent's preload is computed as `.github/scripts/release_report.py#preloads` computes it, then no agent's bytes at HEAD exceed its bytes at the base | a run of `release_report.py --against` on a clone at the base, or of `preloads` on both trees, executed by the crafter and recorded in the last phase's record |
| S3 The framer opens the settle grammar alone | Given a framer that needs the rule-change grammar, when it follows its citation, then the file it opens holds *Rule changes*, *A rule has one shape* and *The index*, and nothing a settle with no design to read needs | `agents/framer.md` cites `skills/settle/rule-changes.md`; the cited-section case resolves it |
| S4 The crafter's whole read of implement loses the orchestrator's text | Given a crafter reading `skills/implement/SKILL.md` whole, when it reads, then the batch question, the ladder and the row drain are not in it, and `skills/implement/orchestration.md` holds them under its own headings | the proofer reads both files; byte count before and after in the phase record |
| S5 A grouped policy root parses | Given a design whose `file:` is `docs/<group>/<name>.md`, when `rule_changes.py` parses it, then it is read; given `docs/a/b/c.md`, then it is refused at its line | new cases in the settle's test module, each seen red first |
| S6 A `move` is placed | Given a `move` of a section into an existing document, when the draft places it, then the section leaves `file` with its sub-sections and stands at the end of `into` at its own level; given a `move` with no `section`, then the document is renamed; given an `into` that does not exist for a section move, or that exists for a document move, then it is not placed and the reason names the file | new cases, seen red first |
| S7 A move rewrites its one token | Given a placed `move`, when the draft writes it, then each backticked old path (a document move), or each backticked old path followed by the moved section's italic text (a section move), in a tracked UTF-8 file outside the records names the new path; a path in any other spelling is unchanged; and the draft prints each file it rewrote with its count | new cases, seen red first, one of them pinning that an unbackticked path is left |
| S8 `seal fold` reads groups | Given a policy root whose index names `docs/g/x.md`, when `seal fold` runs, then `docs/g/x.md` is measured against the ceiling and held to one index row; a subdirectory the index names no document of, such as `docs/experiments/`, is not read | new cases in `tests/skills/test_fold_check.py`, seen red first |
| S9 A citation whose path a pending change corrects is excused | Given a policy document citing `` `skills/settle/SKILL.md` *Rule changes* `` and a pending `change` whose `from` holds that citation and whose `to` holds the same text under another path, when the cited-section case runs, then the citation is excused, not dangling | a new fixture case in `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, seen red first |
| S10 After the settle no document is past its ceiling, and every citation resolves | Given a scratch clone of HEAD, when this design's operations are placed by the draft's placement code and `seal fold` runs there, then no document is past 25,000 estimated tokens, and the cited-section case passes there | executed by the crafter in the scratch clone, recorded in the last phase's record; the live reading is the settle after 0.30.0 |
| S11 The reading is measured before and after | Given the transcripts the framer's census read, when each spawn's Read calls are replayed against the HEAD tree and the scratch tree of S10, then the phase record holds, per agent type, the bytes before and after, split into the cited sections and the rest | D8; the phase record |

## Data & interfaces

### D1 The core's rule

One paragraph under *The first value*, after *Each agent judges its own
target*. The text, which the build may tighten and not lengthen:

> **A document is cut by who opens it and at which step, so a party opens
> only what its step needs.** A party pays for every byte of each file it
> opens, on every spawn that opens it. A form two parties exchange has one
> home that both cite. Text no agent acts on, such as a hook's edge cases,
> stands in the code's docstring or in a document only a person opens. A
> skill's `SKILL.md` holds what every invocation needs and names each
> supporting file with the step that opens it.

About 560 bytes. It holds no list of documents and no grounds beyond the
second sentence: the grounds are the issue and this design.

### D2 What pays for D1 in the preload

Every agent's preload carries the core and the contract, so the offsets are
taken there first, each the rule D1 states applied to the preload itself:

1. The core, *Asking a person is the most expensive step*: the sentence
   "The routing question is one of that batch, and the orchestrating session
   puts the routing question as `skills/implement/orchestration.md`
   *Orchestrator: how the work is routed* states; in a repository opted in by
   its `seal/` root, `hooks/routing-edit-gate.py` refuses the first edit until
   the routing question is answered." goes. Only the orchestrator acts on it,
   the table's first row holds the gate, and `orchestration.md` holds the act.
   About 330 bytes.
2. Contract rule 20 retires to one line, as the contract's numbering rule
   says a rule retires: "Retired by #1312: the core's *The rule a mechanism
   is kept against* states it, and a conclusion to keep a structure checks the
   premise that keeps it." Its first sentence restated the core's. About 220
   bytes saved.
3. `agents/sealer.md` loses the sentences the census finds it shares with
   *The guarantee*, and cites `skills/code-review/scripts/chain_check.py#follows`
   for the HEAD-descendant rule in place of `docs/the-review-record.md` *What
   the check reads at the pull request*.

Where S2 still fails after these, the crafter takes the next offset from text
in the preload that only the orchestrator acts on, names it in the phase
record, and never grows another file to do it. The citations the settle's
path rewrite lengthens in agent definitions (`docs/running/...` for
`docs/the-review-record.md`) are counted in S10's scratch tree, so S2 holds
after the settle too.

### D3 The policy root, cut and grouped

Each group holds the documents one kind of reader opens at one kind of step.
The groups are the issue's four kinds, with the orchestrator's split into the
run and the release, and a fifth for the layout a repository is set up with:

| Group | Who opens it, and at which step | Documents after the settle |
|---|---|---|
| `docs/forms/` | two parties that exchange a record: the one that writes it and the one that reads it | `the-round-record.md` (new), `the-guarantee.md` (new), `the-reader-registry.md` |
| `docs/running/` | the orchestrator while it runs a work item, and an agent that its definition, the contract or a skill it opens sends to one section | `the-run.md` (new: *The run*, *The handoff*, *The per-segment bars*), `the-agent-set.md`, `the-review-and-parity-arms.md`, `the-broad-gate.md`, `measuring-a-run.md`, `what-a-script-gates.md` |
| `docs/releasing/` | the orchestrator and the owner at a release and its settle | `branch-and-release.md`, `issues-and-milestones.md`, `release-checklist.md` |
| `docs/checks/` | a person who changes a hook or a script, and the settling session. No agent acts on them: where the contract or a skill an agent opens cites one, the citing text already states what the agent does, and the citation gives the reason | `the-pull-request-check.md` (new), `the-stamp.md` (new), `the-fold.md` (new), `the-unverified-record.md` (new), `the-session-hooks.md`, `the-routing-check.md` |
| `docs/layout/` | whoever sets a repository up, and the framer, the crafter and the orchestrator where they place or write a record | `one-root-by-lifetime.md`, `one-root-by-lifetime.ko.md`, `the-record-layout.md`, `the-pact.md` |

Each group's reader line is checked against every citation of a policy
document from the texts an agent receives or opens: `agents/*.md`, the core,
the contract, and the `SKILL.md` of `implement`, `verify`, `code-review`,
`legacy-parity`, `writing-style`, `confidence-check` and `feature-planner`
(executed: a probe reading each `` `docs/<name>.md` *section* `` citation in
those files, and `tr | grep -o` for the path-only ones; the orchestrator's
files name the orchestrator and need no check). The list was made from what
produces the readers, the files an agent reads, so it is whole for citations
in those two spellings; a mention in other words is not in it.

| Citation, from the agent side | Group after the settle | The line holds because |
|---|---|---|
| *The round record*: `agents/crafter.md`, `skills/implement/SKILL.md`, `skills/legacy-parity/SKILL.md`; *The guarantee*: `agents/sealer.md` | `forms/` | the writer and the reader of each record are its parties |
| *The run*: `agents/crafter.md`, `agents/framer.md`, `skills/implement/SKILL.md`; *The handoff*: `agents/crafter.md`, `agents/proofer.md`; *The per-segment bars*: contract rule 10; *One contract every agent receives, and one definition each*: `skills/implement/SKILL.md` | `running/` | an agent sent to one section |
| `docs/what-a-script-gates.md` *The checks*: `agents/proofer.md` step 7, which acts on it to judge a pin | `running/` | the proofer acts on it at review, so it leaves the group no agent acts on (orchestrator's reading at 7849e7757, agreed) |
| `docs/the-routing-check.md` *The edit check*: contract rule 9; `docs/the-routing-check.md`: `skills/implement/SKILL.md` *2.* | `checks/` | rule 9 states the act, editing through the edit tools, and the citation gives the reason the shell is not seen; *2.* states that no gate stops a commit and cites where the routing is checked |
| *The stamp*: `skills/verify/SKILL.md` *The hand-back's labels carry the claims, and the one seal is the sealer's* | `checks/` | the sentence states that the hooks draw the stamp, and no agent draws it |
| *What the check reads at the pull request*: `agents/sealer.md` step 1 | `checks/` | D2 item 3 repoints the sealer to `chain_check.py#follows` in this pull request |
| *seal/*, *A commit after the build brings its changelog fragment along*: `skills/implement/SKILL.md`; *What the repository decides for itself, and how it is read*: the same | `layout/` | the framer and the crafter, writing a record. `docs/the-pact.md` is named by `skills/implement/multi-repository.md`, which the orchestrator opens for a work item spanning repositories (`git grep`, executed) |

No agent-side citation names a `releasing/` document.

`docs/README.md` stays at the top, one table per group, and the group's
reader is stated once, in the sentence over its table, rather than at the top
of each of its documents. That departs from the issue's "each states its
reader at its top" for the documents that move whole: fifteen sentences
naming one group's reader would be fifteen copies of one fact. A new document
states its reader in its first paragraph, because it is written here.

`docs/experiments/` stays where it is and is no group: the index names none
of its files, and S8 makes that what keeps a reader from reading it.

A rule change's value holds no blank line, since the reader keeps a
section's non-blank lines only (`skills/verify/scripts/unverified_check.py#field_values`,
read). The new documents' titles and the index's group tables below are
therefore written without the blank lines Markdown wants between a heading,
a paragraph and a table, and the settling session writes them in. That is a
limit of the grammar this work leaves as it is.

### Which directories are grouped

Owner's criterion (issue item 4): a directory whose documents one party
opens at one step, or that holds few files, stays as it is; one where many
documents read by different parties at different steps stand side by side is
grouped.

| Directory | Files now | Grouped | Grounds |
|---|---|---|---|
| `docs/` (the policy root) | 16 documents and the index (`ls`, executed); 22 after the cut | yes, into the five groups above | its documents are opened by the orchestrator, four agents, the settling session and a person at different steps (the census above). The cost is D4's readers and one `move` per document at the settle, paid once; the gain is that a party opens one group and reads within it, and that a document's reader shows in its path |
| `docs/experiments/` | 2 documents and 2 READMEs | no | one reader, a person checking whether something was measured, and no policy |
| `agents/` | 5 | no | few files, each read by the harness for one spawn; a subfolder becomes part of the agent's identifier and would rename `agentic:crafter` and every other agent that spawn prompts, hooks and tests name (sub-agents and plugins-reference docs, orchestrator's finding) |
| `skills/` | 17 skill directories | no | a category level `skills/<group>/<name>/SKILL.md` is not documented as found (skills docs, orchestrator's finding), so a grouped skill may stop loading |
| `skills/settle/`, `skills/implement/`, `skills/verify/` | after D5: 5, 5 and 4 Markdown files beside `scripts/` | no | few files, each named by its `SKILL.md` with the step that opens it; the docs place supporting files beside `SKILL.md` (skills docs, orchestrator's finding) |
| `skills/*/scripts/`, `hooks/`, `hooks/lib/`, `.github/scripts/` | 15, 15 and 15 files in the last three | no | one reader, a person changing the code, who reaches a file from the citation or import that names it; `hooks/hooks.json` and the imports name these paths |
| `templates/` | already `records/` and `setup/` | no change | already grouped by the step that copies a template |
| `tests/` | already grouped by area; `tests/text/` 36, `tests/behaviour/` 48 | no change | a test is opened from the `check:` line that names it, by whoever changes that rule, at that step; regrouping would rename the targets of every `check:` line and every `.test_durations` key for no reader who browses |
| `evals/behaviour/` | already one directory per agent | no change | already grouped by the agent its cases spawn |
| `seal/threads/<work-item-id>/` | fixed by the templates | no change | `skills/implement/SKILL.md` *3. The SDD file set* already groups it into `frame/` and `trail/` |

What a reader of the cut root still reads whole: the index, which a framer
reads to pick each `file:`, and a group's documents one at a time. The
policy in force is still the documents plus the unsettled designs' rule
changes, read across every group.

### D4 The policy root's readers learn groups and `move`

| Reader | Change |
|---|---|
| `skills/settle/scripts/rule_changes.py#parse` | `file` is `<policy root>/<name>.md` or `<policy root>/<group>/<name>.md`, one level and no deeper, no `\` or `:`. A new kind `move`: fields `file`, `into`, and an optional `section`. `into` is held to the same path shape |
| `rule_changes.py#apply_op`, `#copies`, `#pins` | a `move` with a `section` cuts the section, from its heading to the next heading of its level or higher, out of `file` and appends it at the end of `into` at its own level, with one blank line before it; `into` must exist. A `move` with no `section` renames `file` to `into`, which must not exist. A move changes no wording, so it names no pin of wording and no copy |
| `skills/settle/scripts/settle.py`, the draft's placement | places a `move` in merge order like any operation |
| `skills/settle/scripts/settle.py`, the draft's path rewrite (its own phase, after the grammar and the readers) | **The draft rewrites one token, the moved path written whole between two backticks with nothing else inside them, in every tracked UTF-8 file outside the records, and prints each file it rewrote with its count; every other spelling of a moved path is left as it stands, for the cited-section case and the settle's broad run to name.** For a section move the token is rewritten only where the moved section's italic text follows it, so a citation of a section that stays is not touched. No list of spellings is kept: a path wrapped across lines, quoted without backticks or built at run time is one the suite names or nobody does, and the settling session answers each it names |
| `skills/settle/scripts/fold_check.py#documents`, `#index_problems` | a document is a top-level `.md` of the policy root, or a `.md` directly inside a subdirectory the index names at least one document of. Every such document is measured against the ceiling and held to one row |
| `.github/scripts/rules.py`, `.github/scripts/release_report.py#DOCUMENTS`, and every other reader the build finds listing the policy root's documents | read the documents `fold_check.py#documents` reads |
| `tests/behaviour/test_a_cited_section_stands_in_its_file.py#excuser` | a pending `change` excuses a citation where its `from` holds the citation's path and text together and its `to` does not hold that same pair (S9) |

The build enumerates the readers by two commands whose output it pastes in the
phase record, `git grep -n "policy_root("` and `git grep -n "docs/\*"` over
the tree outside `seal/`, as the producers of the list: a reader of the policy
root's documents either resolves the root or globs it.

The grammar's own text, the move's included, lands in
`skills/settle/rule-changes.md` (D5). `templates/setup/config.md` *The fold's
values* and `skills/config/SKILL.md` say "a document of the policy root or
of one of its groups" where they say "top-level document".

### D5 The skills cut in this pull request

| Skill | `SKILL.md` keeps | Moves to | Read by, at which step |
|---|---|---|---|
| `settle` | *When it runs*, *What the dry run shows*, the procedure, *What `--apply` does*, *Answer every check that reads the corpus*, the ceiling rule, *A settle is not a work item*, *What this does not do*, and the first question of *Directories a person names* | `skills/settle/rule-changes.md`: *Rule changes*, *A rule has one shape*, *The index*. `skills/settle/local-mode.md`: *In local mode*. `skills/settle/named-directories.md`: the rest of *Directories a person names*. `skills/settle/draft.md`: *What `--draft` writes* | the framer writes rule changes and the settle and `chain-check` read them; local mode, named directories and the draft are taken by some settles only |
| `implement` | intro, *The language the records are written in*, *Document layout*, *1.* without the batch, *2.*, *3.* without the ladder, *4.*, *5.* | `skills/implement/orchestration.md`, under headings of its own: the batch and routing-wait paragraphs of *1.* (from "Collect what needs a person before the first edit" through "spends more."), the ladder of *3.* (from "When a work item is required" through "not a way out."), and *6. Drain the rows before the broad run, and keep the records* | the batch, the ladder and the drain are the orchestrator's acts; the crafter, which reads `SKILL.md` whole, and the framer never take them |
| `verify` | everything else | `skills/verify/seal-arms.md` and `skills/verify/seal-mutate.md`: the two `####` sections of those names | a party proving condition 2 of a module, or of one unit |

Each supporting file opens with one sentence naming who opens it and at which
step; `SKILL.md` names each file where its step comes, with when to open it.
`skills/implement/SKILL.md` *Document layout* gains, in place of nothing it
removes, one sentence: inside the policy root, documents are grouped by who
opens them and at which step, and any party may open any group. That is where
the axis question is answered (D3).

### D6 Copies, before anything moves

| Pair | Kept on | The other side |
|---|---|---|
| *The run*'s Automation paragraph and `hooks/question-gate.py`'s docstring | the docstring holds what the gate reads and each case it lets through; the document holds the rule the orchestrator acts on | the document's sentences on the exemption, the transcript, the branch read and the forged row go by the first rule change below; the docstring gains the one fact only the document held, that a row edited to `no` is in the diff the review reads |
| *The guarantee* and `skills/code-review/orchestration.md`, `agents/sealer.md` | the document | the skill and the definition link to it in this pull request |
| *The stamp* and `skills/verify/scripts/seal_stamp.py`, `hooks/sealer-stamp.py` | the document | the docstrings link to it in this pull request |
| *What the check reads at the pull request* and `skills/code-review/scripts/chain_check.py` | the document | the docstring and comments link to it in this pull request |

The build re-runs the ten-word census at the phase that removes these, names
its command in the phase record, and calls its list a floor: a restatement in
other words is not counted (contract rule 12).

### D7 Citations

A citation of a skill section that moves in this pull request is rewritten
in the same commit, in every file but the policy root. A citation in the
policy root waits for its rule change below, and S9's excuser keeps the case
green until then. The policy root's own moves rewrite their citations at the
settle (D4). Inside a moved section, an italic cross-reference with no path
(such as *What the check reads at the pull request* inside *The run*) names a
section of another document after the move; the cited-section case does not
read it, and the settling session reads each moved section for one. That is
a limit, not a guard.

### D8 The measurement

Before: the Read calls of the crafter, framer, proofer and sealer spawns in
the transcripts the census above read, taken while 0.29.0 or earlier was
installed. After: the same calls replayed, a whole-file read taking the bytes
the file's successor holds for the step's cited section (the HEAD tree for
the skills, S10's scratch tree for the policy root), a ranged read taking the
same range. Comparable means the same spawns and the same calls; a call whose
path no longer exists is counted against the file its cited section moved
into. The reading is split per agent type into the bytes of the sections the
spawn's definition and prompt cite and the rest. The live reading is the
first run under the installed 0.30.0 for the skills, and the first run under
the release that carries the settle after 0.30.0 for the policy root;
`frame/questions.md` Q1 holds it.

## Rule changes

- change
  file: docs/the-review-record.md
  section: The run
  from: The routing
    question put alone, single-select and with its text, goes through
    while this session's transcript can be read and holds no answer to
    it from this clone, because a run resumed in a new session has to
    put question 1 again for the gates that read the press; once it is
    answered, it is refused like any other question. Any routing answer
    from this clone in the session spends the exemption, including one
    given for another work item, so a session that has already answered
    for another branch cannot put question 1 again; that is outside the
    one-issue flow. The declaration is read through `hooks/lib/routing.py` for the
    branch checked out where the session sits, and every way of not
    reading it is the attended answer. The file is written by the model,
    which is why no gate reads the `automation` press from it. It is read
    here only to refuse, so a row the model forged binds only the model,
    and a row edited to `no` is in the diff the review reads.
  to: The routing question put alone goes through until this session has
    answered it here, and what the gate reads and each case it lets through
    is `hooks/question-gate.py`'s docstring.
- change
  file: docs/the-reader-registry.md
  section: A frame names what its work removes
  from: removing nothing writes the no-change block of `skills/settle/SKILL.md`
    *Rule changes* in place of the table.
  to: removing nothing writes the no-change block of
    `skills/settle/rule-changes.md` *Rule changes* in place of the table.
- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: `skills/settle/SKILL.md` *In
    local mode* gives the states that leave a work item unreleased.
  to: `skills/settle/local-mode.md` *In local mode* gives the states that
    leave a work item unreleased.
- change
  file: docs/README.md
  section: docs/
  from: The standing policy, one row per topic and one table per subject. A `docs/`
    document outranks the work items' designs, and a design that finds one
    wrong states the correction in its `## Rule changes`
    (`skills/settle/SKILL.md` *Rule changes*).
  to: The standing policy, in one directory per group and one table per
    group, each group holding the documents one kind of reader opens at one
    kind of step. A `docs/` document outranks the work items' designs, and a
    design that finds one wrong states the correction in its
    `## Rule changes` (`skills/settle/rule-changes.md` *Rule changes*).
- change
  file: docs/the-record-layout.md
  section: docs/
  from: The standing policy. Its index is `docs/README.md`.
  to: The standing policy, grouped by reader into the directories its index,
    `docs/README.md`, names.
- add
  file: docs/forms/the-round-record.md
  to: # What a review round leaves
    The proofer writes this record, the crafter closes its findings, and
    `skills/code-review/scripts/chain_check.py` reads it at the pull request.
- move
  file: docs/the-review-record.md
  section: The round record
  into: docs/forms/the-round-record.md
- add
  file: docs/forms/the-guarantee.md
  to: # The sealer's verdict
    The sealer writes this verdict, and the orchestrator and the pull
    request check read it.
- move
  file: docs/the-review-record.md
  section: The guarantee
  into: docs/forms/the-guarantee.md
- add
  file: docs/checks/the-pull-request-check.md
  to: # The pull request check
    What `skills/code-review/scripts/chain_check.py` reads at a pull request,
    for a person who changes it; the sealer cites its code.
- move
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  into: docs/checks/the-pull-request-check.md
- add
  file: docs/checks/the-stamp.md
  to: # The seal stamp
    What `hooks/sealer-stamp.py` and `skills/verify/scripts/seal_stamp.py`
    draw, for a person who changes them; no agent acts on it.
- move
  file: docs/the-review-record.md
  section: The stamp
  into: docs/checks/the-stamp.md
- add
  file: docs/running/the-run.md
  to: # The run and its handoffs
    The orchestrator's rules for the review chain's run and for what it hands
    each agent; an agent opens the section its definition cites.
- move
  file: docs/the-review-record.md
  section: The run
  into: docs/running/the-run.md
- move
  file: docs/the-review-record.md
  section: The handoff
  into: docs/running/the-run.md
- remove
  file: docs/the-review-record.md
  section: The review record
- add
  file: docs/checks/the-fold.md
  to: # The fold
    What `seal settle` and `seal fold` read to tell a settle from a deletion,
    for a person who changes them and for the settling session.
- move
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  into: docs/checks/the-fold.md
- add
  file: docs/checks/the-unverified-record.md
  to: # The unverified record
    What `skills/verify/scripts/unverified_check.py` reads, for a person who
    changes it.
- move
  file: docs/the-record-layout.md
  section: The unverified record, and the baseline it is read against
  into: docs/checks/the-unverified-record.md
- move
  file: docs/the-reader-registry.md
  into: docs/forms/the-reader-registry.md
- move
  file: docs/the-agent-set.md
  into: docs/running/the-agent-set.md
- move
  file: docs/the-review-and-parity-arms.md
  into: docs/running/the-review-and-parity-arms.md
- move
  file: docs/the-broad-gate.md
  into: docs/running/the-broad-gate.md
- move
  file: docs/measuring-a-run.md
  into: docs/running/measuring-a-run.md
- move
  file: docs/branch-and-release.md
  into: docs/releasing/branch-and-release.md
- move
  file: docs/issues-and-milestones.md
  into: docs/releasing/issues-and-milestones.md
- move
  file: docs/release-checklist.md
  into: docs/releasing/release-checklist.md
- move
  file: docs/what-a-script-gates.md
  into: docs/running/what-a-script-gates.md
- move
  file: docs/the-session-hooks.md
  into: docs/checks/the-session-hooks.md
- move
  file: docs/the-routing-check.md
  into: docs/checks/the-routing-check.md
- move
  file: docs/one-root-by-lifetime.md
  into: docs/layout/one-root-by-lifetime.md
- move
  file: docs/one-root-by-lifetime.ko.md
  into: docs/layout/one-root-by-lifetime.ko.md
- move
  file: docs/the-record-layout.md
  into: docs/layout/the-record-layout.md
- move
  file: docs/the-pact.md
  into: docs/layout/the-pact.md
- remove
  file: docs/README.md
  section: The process
- remove
  file: docs/README.md
  section: The records
- remove
  file: docs/README.md
  section: The agents and the review
- remove
  file: docs/README.md
  section: The checks
- add
  file: docs/README.md
  section: docs/
  to: ## Forms two parties exchange
    Opened by the party that writes the record and the party that reads it.
    | File | The question it answers |
    |---|---|
    | `docs/forms/the-round-record.md` | what one review round leaves in the tree, and how a fix pass closes it |
    | `docs/forms/the-guarantee.md` | what the sealer's verdict covers, and how it errs |
    | `docs/forms/the-reader-registry.md` | how a frame names what its work removes |
- add
  file: docs/README.md
  section: docs/
  to: ## Running a work item
    Opened by the orchestrator while it runs a work item, and by an agent that its definition, the contract or a skill it opens sends to one section.
    | File | The question it answers |
    |---|---|
    | `docs/running/the-run.md` | how the review chain's run is bounded and ended, and what a spawn prompt hands an agent |
    | `docs/running/the-agent-set.md` | how the rules are split between the agents a work item spawns |
    | `docs/running/the-review-and-parity-arms.md` | what each routing answer owes at the pull request, and what the parity arm wants of a change in a migration |
    | `docs/running/the-broad-gate.md` | who takes the one broad run, what it runs, and what it may say |
    | `docs/running/measuring-a-run.md` | what a segment of a run measures, how a reading that moved is judged, and where the reading goes |
    | `docs/running/what-a-script-gates.md` | which gates a script holds and which an agent holds, what each script reads, and what it does with what it did not read |
- add
  file: docs/README.md
  section: docs/
  to: ## Releasing
    Opened by the orchestrator and the owner at a release and at its settle.
    | File | The question it answers |
    |---|---|
    | `docs/releasing/branch-and-release.md` | where a branch is cut from, how it merges back, and what carries the version |
    | `docs/releasing/issues-and-milestones.md` | what the issue tracker's fields mean here, and which of them anything reads |
    | `docs/releasing/release-checklist.md` | what to type on the day of a release, in order |
- add
  file: docs/README.md
  section: docs/
  to: ## The checks
    Opened by a person who changes a hook or a script, and by the settling session. No agent acts on them: where the contract or a skill an agent opens cites one, the citing text already states what the agent does, and the citation gives the reason.
    | File | The question it answers |
    |---|---|
    | `docs/checks/the-pull-request-check.md` | what the check reads of a work item's records at the pull request |
    | `docs/checks/the-stamp.md` | what the seal stamp draws, and for whom |
    | `docs/checks/the-fold.md` | what tells a settle from a deletion |
    | `docs/checks/the-unverified-record.md` | what the unverified record is read against |
    | `docs/checks/the-session-hooks.md` | how the hooks are registered, and what the implementer mark says |
    | `docs/checks/the-routing-check.md` | where a session's routing is checked: at its edit tools before the first edit, and at the pull request |
- add
  file: docs/README.md
  section: docs/
  to: ## The layout
    Opened by whoever sets a repository up, and by the framer, the crafter and the orchestrator where they place or write a record.
    | File | The question it answers |
    |---|---|
    | `docs/layout/one-root-by-lifetime.md` and `docs/layout/one-root-by-lifetime.ko.md` | where the plugin's one root is, what opts a repository in, what first setup asks, and what the repository's config rows decide |
    | `docs/layout/the-record-layout.md` | where each kind of record lives, which file a change writes, and when a later commit brings the changelog fragment along |
    | `docs/layout/the-pact.md` | where a contract several repositories keep together lives, how each knows about it, and what checks it |
    `docs/experiments/` holds dated scratch documents and is no policy; `settle` never writes there.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the core's sentence on who puts the routing question and which hook refuses the first edit | `skills/core/SKILL.md` *Asking a person is the most expensive step* | the invariant table's first row in the same file holds the gate, and `skills/implement/orchestration.md` *Orchestrator: how the work is routed* holds the act (D2) |
| contract rule 20's body | `skills/agent-contract/SKILL.md` *20 Do not avoid the change a problem calls for* | `skills/core/SKILL.md` *The rule a mechanism is kept against*, which every agent receives; the rule keeps its number as one retirement line |
| the sealer's restatement of the guarantee and its citation of the check's section | `agents/sealer.md` | `docs/the-review-record.md` *The guarantee*, and `skills/code-review/scripts/chain_check.py#follows` |
| the restatements of *The guarantee*, *The stamp* and *What the check reads at the pull request* in code and in the orchestrator's skill | `skills/code-review/orchestration.md`, `skills/verify/scripts/seal_stamp.py`, `hooks/sealer-stamp.py`, `skills/code-review/scripts/chain_check.py` | the document each restates; each site links to it (D6) |
| the question gate's edge cases in the policy root | `docs/the-review-record.md` *The run* | `hooks/question-gate.py`'s docstring, by the first rule change |
| `docs/the-review-record.md` as one document | `docs/the-review-record.md` | five documents by reader (D3), by the rule changes |
| the flat policy root and the index's four subject tables | `docs/*.md`, `docs/README.md` | five group directories and one table per group (D3) |
| the rule that a `file:` names a top-level document only | `skills/settle/scripts/rule_changes.py#parse`, `skills/settle/SKILL.md` *Rule changes* | one level of group directory (D4) |
| the settle's "split by topic" | `skills/settle/SKILL.md` *A document past its ceiling is split, never trimmed* | split by who opens each section and at which step, the core's rule |

The `move` operation is a mechanism this work adds, and nothing in the tree
goes in return for it. What it replaces is outside the tree: without it,
moving a document through `## Rule changes` is a `remove` of the old document
and an `add` whose `to` holds the document's whole text, so this design would
carry about 260 KB of the policy root verbatim, and the settle would have no
way to rewrite the 708 lines that name a moved path but by hand. A design
that moves nothing never writes it.

Framed 2026-11-03 by framer, before the build.
