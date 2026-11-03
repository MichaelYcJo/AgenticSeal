# Design: 1793661729-each-document-is-cut-by-who-opens-it

Issue #1312, the one item of milestone `release: 0.30.0`; it absorbs #1311.
This design reads the issue body as it stood on 2026-11-03, after the owner's
directions were folded in (`gh issue view 1312 --json body`, executed by this
framer; no comments, executed). Those directions are: grouping, as item 4 of
*What changes*, and the paragraph after it, which has this pull request edit
the policy root directly because its subject is the policy root (D9). A third owner direction of the same day, that the cut
respects Claude Code's conventions for skills and agents, reached this framer
as the orchestrator's finding: a `claude-code-guide` agent read
https://code.claude.com/docs/en/skills.md,
https://code.claude.com/docs/en/sub-agents.md and
https://code.claude.com/docs/en/plugins-reference.md. Nobody in this frame
opened those pages, and the rows that rest on them say so.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | It says the policy root "is the baseline, and a pull request does not edit it". The owner's decision of 2026-11-03 (issue body, the paragraph after *What changes*) replaces that clause in this pull request with a boundary by subject (D9). A work item whose subject is the policy root edits it directly, as the settle does. A work item whose subject is the code states its rule changes for the settle. This work item is the first kind: its subject is the root's structure and its documents' text. The owner's grounds: restructuring the documents and the base rules is recurring work whose subject is the documents themselves, and work items running side by side on code must not each rewrite the same section. This work item is also the only unsettled design on `release/v0.30.0` (`ls seal/threads`, executed: one directory), so no other design's operation names a document it moves. The same section says the axis between the roots is "lifetime and authority, not audience". That axis stays between the roots, and the reader becomes the axis inside the policy root (D3) |
| `skills/settle/SKILL.md` *Rule changes* and *The index* (read) | `file:` is read only as a top-level `.md` of the policy root (`skills/settle/scripts/rule_changes.py:257-260`, read), and `seal fold` lists top-level documents only (`skills/settle/scripts/fold_check.py:128`, read). Grouping the policy root changes both readers before the root is grouped (D4) |
| `skills/settle/SKILL.md` *A document past its ceiling is split, never trimmed* (read) | It says a document past the ceiling is split "by topic along its own headings". The sentence is a skill's, so this pull request rewrites it to the reader rule |
| `templates/setup/config.md` *The fold's values* (read) | The estimate is UTF-8 bytes halved. `docs/the-review-record.md` is 50,774 bytes, about 25,387 tokens, past this repository's `Document token ceiling` of 25,000 (`wc -c`, executed; `seal/config.md`, read) |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "A fact has one source, and every other place links to it." Copies go before anything moves (D6). A mechanism this work adds names what it takes out in return (`## Removes`) |
| `skills/core/SKILL.md` *The first value* (read) | The core reaches every party on every spawn, so the new rule is a few sentences and its bytes are paid back inside the same preload (D1, D2) |
| `.github/scripts/release_report.py#preloads` (read) | An agent's preload is the bytes of `agents/<agent>.md` plus the core plus `skills/agent-contract/SKILL.md`. No agent's preload grows. #1254 settles how a preload rewrite is proved; this item claims only that none grows |
| `evals/README.md` *The behaviour suite* (read) | "Nothing in the tree makes a later edit owe a run." No paid eval run is taken here |
| `docs/measuring-a-run.md` *Where a reading goes* and the band paragraph (read) | The crafter of a work item that measures the process writes the reading and its weighing in the phase record (D8) |
| `skills/writing-style/SKILL.md` and `skills/writing-style/outside-the-review.md` (read: `SKILL.md:316-324`) | #265 already cut one skill by reader. That cut stands |
| Claude Code skills docs, `skills.md` (orchestrator's finding, not opened here) | A plugin skill is found at `skills/<name>/SKILL.md`; a category level `skills/<group>/<name>/` is not documented. Supporting files sit beside `SKILL.md` and enter context only when read after `SKILL.md` names them and says when; a `SKILL.md` under 500 lines is recommended |
| Claude Code sub-agents docs, `sub-agents.md` and `plugins-reference.md` (orchestrator's finding, not opened here) | A `skills:` list injects each skill's full `SKILL.md`; whether supporting files are injected is not documented, so what every spawn needs stays in the `core` and `agent-contract` bodies. `agents/` is scanned recursively and a subfolder becomes part of the agent's identifier, so grouping `agents/` would rename every agent |

### Measured on the tree at 2d38c75af (each executed by this framer, scripts under the scratch directory, since removed)

| What | Reading |
|---|---|
| Section bytes of `docs/the-review-record.md` | *The round record* 10,029; *What the check reads at the pull request* 13,825; *The guarantee* 5,218; *The stamp* 9,658; *The run* 8,065; *The handoff* 2,335 with *The per-segment bars* 1,354 inside it |
| Section bytes of `docs/the-record-layout.md` | *The fold, and what tells it from a deletion* 13,157; *The unverified record, and the baseline it is read against* 1,192; the whole file 28,884 |
| Agents' Read bytes in the 1,004 subagent transcripts under this repository's Claude Code project directory, `~/.claude/projects/<project>/*/subagents/`, for the agent types `crafter`, `framer`, `proofer`, `sealer` (JSON length of each Read result) | crafter, 78 spawns: `skills/implement/SKILL.md` 100 reads, 2,927,734 bytes. framer, 169 spawns: `skills/implement/SKILL.md` 42 reads, 586,744; `skills/settle/SKILL.md` 17 reads, 233,943; `docs/the-review-record.md` 6 reads, 74,538. proofer, 134 spawns: `skills/code-review/SKILL.md` 30 reads, 325,695; `docs/the-review-record.md` 6 reads, 75,294. sealer, 159 spawns: `docs/the-review-record.md` 2 reads, 21,103 |
| Ten-word runs `docs/the-review-record.md` shares with tracked `.md` and `.py` files outside `seal/` and `evals/` | 1,234 of 8,989 words by this framer's tokenizer; the orchestrator's 835 of 8,716 used another. The largest pairs: *The run* with `hooks/question-gate.py` (85 runs), *The stamp* with `skills/verify/scripts/seal_stamp.py` (60), *What the check reads at the pull request* with `skills/code-review/scripts/chain_check.py` (45), *The guarantee* with `skills/code-review/orchestration.md` (18) and `agents/sealer.md` (10) |
| Lines naming a `docs/<name>.md` path outside `seal/` | 708 lines in 151 files (`git grep -c`) |

The transcripts show where an agent's reading goes. The crafter reads
`skills/implement/SKILL.md` whole about once per spawn or more, and the framer
reads `skills/settle/SKILL.md` for one section. The agents rarely open
`docs/the-review-record.md`. An agent reads the plugin's installed copy of
every file, so all of this reaches agents with 0.30.0's release.

## Scope

In:

1. The core states the rule (D1), and the preload pays for it (D2).
2. The skills an agent reads whole are cut (D5): `skills/settle/SKILL.md`,
   `skills/implement/SKILL.md` and `skills/verify/SKILL.md`, each keeping in
   `SKILL.md` what every invocation needs.
3. The policy root's readers learn one level of group directories (D4), so
   the root can be grouped and a later design can name
   `docs/<group>/<name>.md`.
4. The policy root is cut and grouped in this pull request (D3):
   `docs/the-review-record.md` is cut into five documents by reader, two
   sections of `docs/the-record-layout.md` leave it, and every document moves
   into one of five groups. Each move leaves the wording unchanged.
   `skills/implement/SKILL.md` *Document layout* states the boundary that
   lets this pull request edit the root (D9).
5. Copies go before anything moves (D6). The pairs the ten-word census lists
   for `docs/the-review-record.md` are each kept on one side, the policy side
   included, edited in this pull request.
6. Every citation moves with its section, in the commit that moves it (D7).
   `tests/behaviour/test_a_cited_section_stands_in_its_file.py` holds each
   one.
7. The measurement (D8): a replay of existing transcripts against the tree at
   HEAD, with no paid run.

Out, each with its grounds:

- `agents/` is not grouped, and no agent's own rules leave its definition.
  Grouping renames every agent (sub-agents docs, orchestrator's finding), and
  the issue keeps an agent's own rules out of `agents/*.md` anyway.
- `skills/` gets no category level: a nested `skills/<group>/<name>/SKILL.md`
  is not documented as found (skills docs, orchestrator's finding).
- `skills/*/orchestration.md` (35, 29 and 24 KB) are not cut. One party, the
  orchestrator, reads each, in the one session that runs the work, so a cut
  by step turns one read into several in that context.
- `skills/writing-style/` stays as #265 cut it.
- `skills/code-review/SKILL.md`, `skills/commit-pr-convention/SKILL.md`,
  `skills/config/SKILL.md` and `skills/update/SKILL.md`: one party reads each
  at one step.
- The stamp's and the pull-request check's copies with their code are removed
  on the code side only (D6). Their documents go to the group no agent acts
  on.
- Any change to a rule's wording beyond D6's copies, the index and the
  sentences D3 and D5 name: the root is cut and grouped, and its rules are
  not rewritten.
- `.claude-plugin/plugin.json` moving to 0.30.0 is the orchestrator's, in the
  commit that adds the changelog fragment.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The core states the rule | Given any spawn, when it receives the core, then *The first value* holds the cut rule as D1 states it, in at most five sentences | the proofer reads `skills/core/SKILL.md` against D1 |
| S2 No preload grows | Given the base 2d38c75af and HEAD, when each agent's preload is computed as `.github/scripts/release_report.py#preloads` computes it, then no agent's bytes at HEAD exceed its bytes at the base. HEAD here is after phase 5, so the longer `docs/<group>/` citations are counted | `preloads` run on a clone at the base and on HEAD, executed by the crafter and pasted in the phase record |
| S3 The framer opens the settle grammar alone | Given a framer that needs the rule-change grammar, when it follows its citation, then the file it opens holds *Rule changes*, *A rule has one shape* and *The index*, and nothing a settle needs that a design's author does not | `agents/framer.md` cites `skills/settle/rule-changes.md`; the cited-section case resolves it |
| S4 The crafter's whole read of implement loses the orchestrator's text | Given a crafter reading `skills/implement/SKILL.md` whole, when it reads, then the batch question, the ladder and the row drain are not in it, and `skills/implement/orchestration.md` holds them under its own headings | the proofer reads both files; bytes before and after in the phase record |
| S5 A grouped policy root parses | Given a design whose `file:` is `docs/<group>/<name>.md`, when `rule_changes.py` parses it, then it is read; given `docs/a/b/c.md`, then it is refused at its line | new cases in the settle's test module, each seen red first |
| S6 `seal fold` and every other reader of the root read groups | Given a policy root whose index names `docs/g/x.md`, when `seal fold` runs, then `docs/g/x.md` is measured against the ceiling and held to one index row. A subdirectory the index names no document of, such as `docs/experiments/`, is not read. `rules.py` and `release_report.py` read the same documents | new cases in `tests/skills/test_fold_check.py` and the modules of the other readers, each seen red first |
| S7 A move leaves the wording unchanged | Given phase 1's commit and phase 5's commit, when each moved section and document is compared with its old text, then they are identical. The only differences allowed are the new documents' titles and reader sentences, the index, re-pointed citations, and the paths D7 gives to path-less cross-references | `git diff -M --stat` for the whole-document moves, and for each section move a comparison of the section's lines at the base with its lines at HEAD, executed by the crafter, commands and output in the phase record |
| S8 Every citation stands at its new place | Given phase 5's commit, when the cited-section case runs, then every citation resolves; and `git grep` of each old path outside `seal/` lists nothing | the cited-section case, run narrow; the `git grep` commands and their empty output in the phase record |
| S9 No document is past its ceiling | Given HEAD, when `seal fold` runs, then it names no document past 25,000 estimated tokens and the index names every document once | `seal fold`, executed by the crafter at phase 7 |
| S10 The reading is measured before and after | Given the transcripts the census read, when each spawn's Read calls are replayed against the tree at HEAD, then the phase record holds, per agent type, the bytes before and after, split into the cited sections and the rest | D8; the phase record |
| S11 The boundary is stated where the policy root's authority is | Given `skills/implement/SKILL.md` *Document layout*, when a framer reads the `docs/` row, then it says, as D9 states, which work item edits the policy root directly and which states rule changes for the settle, that whoever edits it directly re-points every unsettled design's operation naming a document or section it moved, and that the subject is the framer's judgment; "a pull request does not edit it" stands nowhere in the tree | the proofer reads the row against D9; `git grep -n "does not edit it"` outside `seal/`, executed by the crafter, lists nothing |
## Data & interfaces

### D1 The core's rule

One paragraph under *The first value*, after *Each agent judges its own
target*. The build may tighten this text and not lengthen it:

> **A document is cut by who opens it and at which step, so a party opens
> only what its step needs.** A party pays for every byte of each file it
> opens, on every spawn that opens it. A form two parties exchange has one
> home that both cite. Text no agent acts on, such as a hook's edge cases,
> stands in the code's docstring or in a document only a person opens. A
> skill's `SKILL.md` holds what every invocation needs and names each
> supporting file with the step that opens it.

About 560 bytes. It holds no list of documents, and no grounds beyond its
second sentence; the grounds are the issue and this design.

### D2 What pays for D1 in the preload

Every agent's preload carries the core and the contract, so the offsets come
from there first. Each applies D1's rule to the preload itself:

1. The core, *Asking a person is the most expensive step*: this sentence
   goes: "The routing question is one of that batch, and the orchestrating
   session puts the routing question as `skills/implement/orchestration.md`
   *Orchestrator: how the work is routed* states; in a repository opted in by
   its `seal/` root, `hooks/routing-edit-gate.py` refuses the first edit until
   the routing question is answered." Only the orchestrator acts on it. The
   table's first row holds the gate, and `orchestration.md` holds the act.
   About 330 bytes.
2. Contract rule 20 retires to one line, as the contract's numbering rule
   says a rule retires: "Retired by #1312: the core's *The rule a mechanism
   is kept against* states it, and a conclusion to keep a structure checks the
   premise that keeps it." Its first sentence restated the core's. About 220
   bytes saved.
3. `agents/sealer.md` loses the sentences the census finds it shares with
   *The guarantee*. For the rule that HEAD descends from the last record's
   commit, it cites `skills/code-review/scripts/chain_check.py#follows` in
   place of `docs/the-review-record.md` *What the check reads at the pull
   request*.

If S2 still fails after these, the crafter takes the next offset from preload
text that only the orchestrator acts on, names it in the phase record, and
never grows another file to do it.

### D3 The policy root, cut and grouped

Each group holds the documents one kind of reader opens at one kind of step.
The groups are the issue's four kinds. The orchestrator's kind is split into
the run and the release, and a fifth group holds the layout a repository is
set up with.

| Group | Who opens it, and at which step | Documents after phase 5 |
|---|---|---|
| `docs/forms/` | two parties that exchange a record: the one that writes it and the one that reads it | `the-round-record.md` (new), `the-guarantee.md` (new), `the-reader-registry.md` |
| `docs/running/` | the orchestrator while it runs a work item, and an agent that its definition, the contract or a skill it opens sends to one section | `the-run.md` (new: *The run*, *The handoff*, *The per-segment bars*), `the-agent-set.md`, `the-review-and-parity-arms.md`, `the-broad-gate.md`, `measuring-a-run.md`, `what-a-script-gates.md` |
| `docs/releasing/` | the orchestrator and the owner at a release and its settle | `branch-and-release.md`, `issues-and-milestones.md`, `release-checklist.md` |
| `docs/checks/` | a person who changes a hook or a script, and the settling session. No agent acts on these documents: where the contract or a skill an agent opens cites one, the citing text already states what the agent does, and the citation gives the reason | `the-pull-request-check.md` (new), `the-stamp.md` (new), `the-fold.md` (new), `the-unverified-record.md` (new), `the-session-hooks.md`, `the-routing-check.md` |
| `docs/layout/` | whoever sets a repository up, and the framer, the crafter and the orchestrator where they place or write a record | `one-root-by-lifetime.md`, `one-root-by-lifetime.ko.md`, `the-record-layout.md`, `the-pact.md` |

The new documents, each written with a title and one reader sentence and
then the sections moved into it unchanged, at their own heading level:

| New document | Title, and its reader sentence | Sections moved in, from |
|---|---|---|
| `docs/forms/the-round-record.md` | *What a review round leaves*. The proofer writes this record, the crafter closes its findings, and `skills/code-review/scripts/chain_check.py` reads it at the pull request | *The round record*, `docs/the-review-record.md` |
| `docs/forms/the-guarantee.md` | *The sealer's verdict*. The sealer writes this verdict, and the orchestrator and the pull request check read it | *The guarantee*, the same |
| `docs/checks/the-pull-request-check.md` | *The pull request check*. What `chain_check.py` reads at a pull request, for a person who changes it; the sealer cites its code | *What the check reads at the pull request*, the same |
| `docs/checks/the-stamp.md` | *The seal stamp*. What `hooks/sealer-stamp.py` and `skills/verify/scripts/seal_stamp.py` draw, for a person who changes them; no agent acts on it | *The stamp*, the same |
| `docs/running/the-run.md` | *The run and its handoffs*. The orchestrator's rules for the review chain's run and for what it hands each agent; an agent opens the section its definition cites | *The run* and *The handoff* (with *The per-segment bars*), the same |
| `docs/checks/the-fold.md` | *The fold*. What `seal settle` and `seal fold` read to tell a settle from a deletion, for a person who changes them and for the settling session | *The fold, and what tells it from a deletion*, `docs/the-record-layout.md` |
| `docs/checks/the-unverified-record.md` | *The unverified record*. What `skills/verify/scripts/unverified_check.py` reads, for a person who changes it | *The unverified record, and the baseline it is read against*, the same |

`docs/the-review-record.md` is deleted once its sections have left it. Its
title paragraph goes with it, and each new document's reader sentence takes
its place. The other fifteen documents move whole with `git mv`.

`docs/README.md` stays at the top. Its intro says the root is one directory
per group and one table per group, and cites `skills/settle/rule-changes.md`
*Rule changes*. It has one table per group, in the order of the table above.
Over each table stands the group's reader sentence as the table's
*Who opens it* cell gives it, so a group's reader is stated once, not at the
top of each document. Each row keeps the question its row answers today, and
the new documents' rows take their reader sentences. The line about
`docs/experiments/` stays. A moved document gets no reader line of its own,
which departs from the issue's "each states its reader at its top": fifteen
sentences naming one group's reader would be fifteen copies of one fact.

`docs/experiments/` stays where it is and is no group. The index names none
of its files, and S6 makes that what keeps a reader from reading it.

A reader of the cut root still reads two things whole: the index, which a
framer reads to pick each `file:`, and a group's documents, one at a time.

Each group's reader line was checked against every citation of a policy
document from the texts an agent receives or opens: `agents/*.md`, the core,
the contract, and the `SKILL.md` of `implement`, `verify`, `code-review`,
`legacy-parity`, `writing-style`, `confidence-check` and `feature-planner`.
The check was executed: a probe read each `` `docs/<name>.md` *section* ``
citation in those files, and `tr | grep -o` found the path-only ones. The
orchestrator's files name the orchestrator and need no check. The list was
made from what produces the readers, the files an agent reads, so it is whole
for citations in those two spellings. A mention in other words is not in it.

| Citation, from the agent side | Group after phase 5 | The line holds because |
|---|---|---|
| *The round record*: `agents/crafter.md`, `skills/implement/SKILL.md`, `skills/legacy-parity/SKILL.md`; *The guarantee*: `agents/sealer.md` | `forms/` | the writer and the reader of each record are its parties |
| *The run*: `agents/crafter.md`, `agents/framer.md`, `skills/implement/SKILL.md`; *The handoff*: `agents/crafter.md`, `agents/proofer.md`; *The per-segment bars*: contract rule 10; *One contract every agent receives, and one definition each*: `skills/implement/SKILL.md` | `running/` | each is an agent sent to one section |
| `docs/what-a-script-gates.md` *The checks*: `agents/proofer.md` step 7, which acts on it to judge a pin | `running/` | the proofer acts on it at review, so it leaves the group no agent acts on (the orchestrator's reading at 7849e7757, agreed) |
| `docs/the-routing-check.md` *The edit check*: contract rule 9; `docs/the-routing-check.md`: `skills/implement/SKILL.md` *2.* | `checks/` | rule 9 states the act, editing through the edit tools, and its citation gives the reason the shell is not seen. *2.* states that no gate stops a commit, and cites where the routing is checked |
| *The stamp*: `skills/verify/SKILL.md` *The hand-back's labels carry the claims, and the one seal is the sealer's* | `checks/` | the sentence states that the hooks draw the stamp, and no agent draws it |
| *What the check reads at the pull request*: `agents/sealer.md` step 1 | `checks/` | D2 item 3 repoints the sealer to `chain_check.py#follows` |
| *seal/* and *A commit after the build brings its changelog fragment along*: `skills/implement/SKILL.md`; *What the repository decides for itself, and how it is read*: the same | `layout/` | the framer and the crafter, writing a record. `docs/the-pact.md` is named by `skills/implement/multi-repository.md`, which the orchestrator opens for a work item spanning repositories (`git grep`, executed) |

No agent-side citation names a `releasing/` document.

### Which directories are grouped

The owner's criterion (issue item 4) sorts the directories. One whose
documents one party opens at one step, or that holds few files, stays as it
is. One where many documents read by different parties at different steps
stand side by side is grouped.

| Directory | Files now | Grouped | Grounds |
|---|---|---|---|
| `docs/` (the policy root) | 16 documents and the index (`ls`, executed); 22 after the cut | yes, into the five groups above | the orchestrator, four agents, the settling session and a person open its documents at different steps (the census above). The cost is D4's readers, paid once, and phase 5's moves and re-pointed citations. The gain is that a party opens one group and reads within it, and that a document's path shows its reader |
| `docs/experiments/` | 2 documents and 2 READMEs | no | one reader, a person checking whether something was measured, and no policy |
| `agents/` | 5 | no | few files, each read by the harness for one spawn. A subfolder becomes part of the agent's identifier and would rename `agentic:crafter` and every other agent that spawn prompts, hooks and tests name (sub-agents and plugins-reference docs, orchestrator's finding) |
| `skills/` | 17 skill directories | no | a category level `skills/<group>/<name>/SKILL.md` is not documented as found (skills docs, orchestrator's finding), so a grouped skill may stop loading |
| `skills/settle/`, `skills/implement/`, `skills/verify/` | after D5: 5, 5 and 4 Markdown files beside `scripts/` | no | few files, each named by its `SKILL.md` with the step that opens it. The docs place supporting files beside `SKILL.md` (skills docs, orchestrator's finding) |
| `skills/*/scripts/`, `hooks/`, `hooks/lib/`, `.github/scripts/` | 15, 15 and 15 files in the last three | no | one reader, a person changing the code, who reaches a file from the citation or import that names it. `hooks/hooks.json` and the imports name these paths |
| `templates/` | already `records/` and `setup/` | no change | already grouped by the step that copies a template |
| `tests/` | already grouped by area; `tests/text/` 36, `tests/behaviour/` 48 | no change | a test is opened from the `check:` line that names it, by whoever changes that rule, at that step. Regrouping would rename the targets of every `check:` line and every `.test_durations` key, for no reader who browses |
| `evals/behaviour/` | already one directory per agent | no change | already grouped by the agent its cases spawn |
| `seal/threads/<work-item-id>/` | fixed by the templates | no change | `skills/implement/SKILL.md` *3. The SDD file set* already groups it into `frame/` and `trail/` |

### D4 The policy root's readers learn groups

| Reader | Change |
|---|---|
| `skills/settle/scripts/rule_changes.py#parse` | `file` is `<policy root>/<name>.md` or `<policy root>/<group>/<name>.md`: one level and no deeper, with no `\` or `:` |
| `skills/settle/scripts/fold_check.py#documents`, `#index_problems` | a document is a top-level `.md` of the policy root, or a `.md` directly inside a subdirectory the index names at least one document of. Every such document is measured against the ceiling and held to one index row |
| `.github/scripts/rules.py`, `.github/scripts/release_report.py#DOCUMENTS`, and every other reader the build finds listing the policy root's documents, a test among them | they read the documents `fold_check.py#documents` reads |

The build lists the readers with two commands and pastes their output in the
phase record: `git grep -n "policy_root("` and `git grep -n "docs/\*"` over
the tree outside `seal/`. These are the producers of the list, since a reader
of the policy root's documents either resolves the root or globs it.

`skills/settle/SKILL.md` *Rule changes* (`skills/settle/rule-changes.md`
after phase 3), `templates/setup/config.md` *The fold's values* and
`skills/config/SKILL.md` say "a document of the policy root or of one of its
groups" where they now say "top-level document".

### D5 The skills cut

| Skill | `SKILL.md` keeps | Moves to | Read by, at which step |
|---|---|---|---|
| `settle` | *When it runs*, *What the dry run shows*, the procedure, *What `--apply` does*, *Answer every check that reads the corpus*, the ceiling rule, *A settle is not a work item*, *What this does not do*, and the first question of *Directories a person names* | `skills/settle/rule-changes.md`: *Rule changes*, *A rule has one shape*, *The index*. `skills/settle/local-mode.md`: *In local mode*. `skills/settle/named-directories.md`: the rest of *Directories a person names*. `skills/settle/draft.md`: *What `--draft` writes* | the framer writes rule changes, and the settle and `chain-check` read them. Local mode, named directories and the draft are taken by some settles only |
| `implement` | intro, *The language the records are written in*, *Document layout*, *1.* without the batch, *2.*, *3.* without the ladder, *4.*, *5.* | `skills/implement/orchestration.md`, under headings of its own: the batch and routing-wait paragraphs of *1.* (from "Collect what needs a person before the first edit" through "spends more."), the ladder of *3.* (from "When a work item is required" through "not a way out."), and *6. Drain the rows before the broad run, and keep the records* | the batch, the ladder and the drain are the orchestrator's acts. The crafter, which reads `SKILL.md` whole, and the framer never take them |
| `verify` | everything else | `skills/verify/seal-arms.md` and `skills/verify/seal-mutate.md`: the two `####` sections of those names | a party proving condition 2 of a module, or of one unit |

Each supporting file opens with one sentence naming who opens it and at which
step, and `SKILL.md` names each file where its step comes, with when to open
it.

`skills/implement/SKILL.md` *Document layout* also takes the sentence that
answers the axis question, after the axis paragraph, in phase 5: inside the
policy root, documents are grouped by who opens them and at which step, and
any party may open any group.

### D6 Copies, before anything moves

| Pair | Kept on | The other side |
|---|---|---|
| *The run*'s Automation paragraph and `hooks/question-gate.py`'s docstring | the docstring holds what the gate reads and each case it lets through. The document holds the rule the orchestrator acts on | in `docs/the-review-record.md` *The run*, edited in phase 1 under D9, the sentences from "The routing question put alone, single-select and with its text" through "and a row edited to `no` is in the diff the review reads." become: "The routing question put alone goes through until this session has answered it here, and what the gate reads and each case it lets through is `hooks/question-gate.py`'s docstring." The docstring gains the one fact only the document held: a row edited to `no` is in the diff the review reads |
| *The guarantee* and `skills/code-review/orchestration.md`, `agents/sealer.md` | the document | the skill and the definition link to it |
| *The stamp* and `skills/verify/scripts/seal_stamp.py`, `hooks/sealer-stamp.py` | the document | the docstrings link to it |
| *What the check reads at the pull request* and `skills/code-review/scripts/chain_check.py` | the document | the docstring and comments link to it |

The build re-runs the ten-word census in phase 1 and names its command in the
phase record. It calls its list a floor, since a restatement in other words
is not counted (contract rule 12).

### D7 Citations

Every citation of a section or a document that moves is re-pointed in the
commit that moves it. That includes a citation in a policy document, in a
test, in a hook's output and in `.test_durations`. Each edit goes through the
`Edit` tool, with `replace_all` for each old path in a file, never through a
script. `git mv` moves each whole document, so a missing source fails the
command.

- **Phase 3 and phase 4** re-point the skill sections they move, in every
  file, the three citations of moved `settle` sections in `docs/` among them.
- **Phase 5** re-points every policy path. Its list comes from `git grep` of
  each old path over the tree outside `seal/`, run before and after, and the
  after-run lists nothing (S8). The cited-section case holds every
  `` `path` *section* `` citation.
- **Path-less cross-references.** An italic cross-reference with no path
  inside a moved section, such as *What the check reads at the pull request*
  inside *The run*, names a section of another document after the move.
  Phase 5 reads each moved section for these, and gives each one that now
  crosses documents the path of the document it names. No case reads such a
  reference, so the proofer reads phase 5 for them.

### D8 The measurement

- **Before:** the Read calls of the crafter, framer, proofer and sealer spawns
  in the transcripts the census above read, taken while 0.29.0 or earlier was
  installed.
- **After:** the same calls replayed against the tree at HEAD. A whole-file
  read takes the bytes of the file that now holds the step's cited section. A
  ranged read takes the same range.
- **Comparable** means the same spawns and the same calls. A call whose path
  no longer exists is counted against the file its cited section moved into.
- **The split:** per agent type, the bytes of the sections the spawn's
  definition and prompt cite, and the rest.
- **The live reading** is the first run under the installed 0.30.0, which
  carries the skills and the policy root alike. `frame/questions.md` Q1
  holds it.

### D9 Which work item edits the policy root

The clause "and a pull request does not edit it" in the `docs/` row of
`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*
becomes the owner's boundary. Phase 1 writes it, since phase 1 is the first
to edit the root:

> A work item whose subject is the policy root itself, its structure or its
> documents' text, edits the policy root directly in its pull request, as the
> settle does, and re-points in that pull request every unsettled design's
> `## Rule changes` operation that names a document or a section it moved. A
> work item whose subject is the code states the rules its work changes in
> `## Rule changes`, for the settle, so that work items running side by side
> do not each rewrite the same section. Which subject a work item has is the
> framer's judgment, read by the proofer at review.

No script holds the boundary. `chain_check.py`, the hooks and the workflows
refuse no edit under `docs/` (`git grep -n -i "policy root"` over them,
executed: none refuses one), so the change needs no gate removed or added.

The same table row's sentence that a design states its changes in
`## Rule changes` stays true for the second kind. `docs/README.md`'s intro,
rewritten in phase 5, cites *Document layout* for which kind does which.
`git grep` found the clause in no other file (executed), and S11 holds that.

This work item is the first kind. Its subject is the root's structure, and
the text it changes there is the copy D6 removes, the index and the new
documents' reader sentences. Phase 5 re-points no other design's operation,
because no other design is unsettled (`ls seal/threads`, executed). The
phase still runs that `ls` at its commit and records what it lists.

## Rule changes

- nothing
  why: This work item's subject is the policy root's structure and text, so it edits `docs/` directly in its pull request under the boundary D9 writes into `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, and leaves the settle no decision to gather.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the core's sentence on who puts the routing question and which hook refuses the first edit | `skills/core/SKILL.md` *Asking a person is the most expensive step* | the invariant table's first row in the same file holds the gate, and `skills/implement/orchestration.md` *Orchestrator: how the work is routed* holds the act (D2) |
| contract rule 20's body | `skills/agent-contract/SKILL.md` *20 Do not avoid the change a problem calls for* | `skills/core/SKILL.md` *The rule a mechanism is kept against*, which every agent receives. The rule keeps its number as one retirement line |
| the sealer's restatement of the guarantee, and its citation of the check's section | `agents/sealer.md` | `docs/forms/the-guarantee.md` *The guarantee*, and `skills/code-review/scripts/chain_check.py#follows` |
| the restatements of *The guarantee*, *The stamp* and *What the check reads at the pull request* in code and in the orchestrator's skill | `skills/code-review/orchestration.md`, `skills/verify/scripts/seal_stamp.py`, `hooks/sealer-stamp.py`, `skills/code-review/scripts/chain_check.py` | the document each restates; each site links to it (D6) |
| the question gate's edge cases in the policy root | `docs/the-review-record.md` *The run* | `hooks/question-gate.py`'s docstring, in phase 1 (D6) |
| `docs/the-review-record.md` as one document, and its title paragraph | `docs/the-review-record.md` | five documents by reader, each with its own reader sentence (D3) |
| the flat policy root and the index's four subject tables | `docs/*.md`, `docs/README.md` | five group directories and one table per group (D3) |
| the rule that a pull request does not edit the policy root | `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | the owner's boundary in the same row: a work item whose subject is the policy root edits it directly, and one whose subject is the code states rule changes for the settle (D9) |
| the rule that a `file:` names a top-level document only | `skills/settle/scripts/rule_changes.py#parse`, `skills/settle/SKILL.md` *Rule changes* | one level of group directory (D4) |
| the settle's "split by topic" | `skills/settle/SKILL.md` *A document past its ceiling is split, never trimmed* | split by who opens each section and at which step, the core's rule |
| the orchestrator's batch, ladder and drain in the skill the crafter reads whole | `skills/implement/SKILL.md` *1.*, *3.*, *6.* | `skills/implement/orchestration.md` (D5) |

This work adds no mechanism. D4 widens what four readers read, and checks
nothing new.

Framed 2026-11-03 by framer, before the build.
