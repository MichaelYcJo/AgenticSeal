# Design: 1793966252-a-sentence-is-read-before-the-sealer

## Grounding

The tree as read at `1359abcb9`.

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against* | A script holds a gate only on a fact it reads exactly. Whether the body's first part is the committed `pr.md`, byte for byte, is such a fact, so `seal pr-body --check` may refuse on it. Whether a quote inside `pr.md` stands at its source is a reading of prose, so it stays the orchestrator's and the rounds' act and no script's (`frame/plan.md` *Alternatives considered*, the row on a quote script) |
| `skills/core/SKILL.md` *Each agent judges its own target, independently of the others* | The sealer judges a finished product. A sentence of a record that reaches it unread by a round is that round's miss, as #1415 *The cause* states as the owner's framing |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | This work item's subject is the code: the agents, the skills, the templates and `seal pr-body`. So each `docs/` sentence it changes is an operation of `## Rule changes`, and no phase edits `docs/` |
| `docs/releasing/branch-and-release.md` *Cutting a release* | The version moves in the first pull request into `release/vX.Y.Z`, in the commit that adds that work item's changelog fragment. It names the orchestrator as the party that moves it, and the `## Rule changes` operation on that file changes that |
| `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file* | A work item that changes an `agents/*.md` file or a `skills/*/orchestration.md` file ends its `changelog.md` with `### Process changes`. This one does both |
| `docs/layout/the-record-layout.md` *A fact of a work item has one record, and every other record cites it by path and heading* | A record holds no copy of another's fact. `pr.md` holds quotes for the reader of the pull request, so the `## Rule changes` operation on that sentence states it as the one exception |
| `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, the paragraph opening **You write the pull request body after** | At `1359abcb9` the orchestrator writes its part after `trail/gate.md` is committed, so after every round. Its part may hold "what no record holds" and a record's fact "with the record's coordinate". No round can read that part, which is how #1415 *What the sealer caught* happened |
| `skills/code-review/scripts/pr_body.py#_check` | Its docstring says "The part above it is the orchestrator's and is not read" (read). `pr_body.py#main` keeps that part from the body file as its bytes stood (read) |
| `agents/proofer.md` *Order of work* step 3 | A round reads `frame/design.md`, `frame/plan.md`, `gaps.md` and `trail/phases/`, and not `frame/questions.md`, `changelog.md` or `routing.md` (read). The two sentences of #1376 that the first sealer withheld on stood in two of the files it does not read |
| `agents/crafter.md` *Before you hand back, your range and the work item's records are read whole against HEAD* | #1415's item 3 is already this rule: the crafter reads the three frame files whole and names each statement HEAD contradicts in a file it does not write. It came in with #1327 (`git blame -L 162,181 agents/crafter.md`, executed: commit `5005355d8`), and the 0.32.6 copy that #1376's crafter ran under holds it (`git show v0.32.6:agents/crafter.md \| grep -c 'Read whole'`, executed: 1) |
| `skills/verify/orchestration.md` *Measure the segment, and feed the flow log*, the paragraph opening **When the run ends, one more reading is taken** | The run's comparison table "is not a third destination" and goes to the rolling log. It is taken when the run ends, after the sealer, so it cannot stand in a `pr.md` that every round reads |
| A thread's top-level files | No reader lists them: `git grep` for `listdir`, `scandir`, `glob` and `iterdir` in `lib/`, `skills/*/scripts/` and `.github/scripts/` finds only `trail/rounds/` listings and `pact_check.py`'s glob of `frame/design.md` (executed). So a new `pr.md` is refused by no reader and leaves with its directory at the settle |
| This design's `## Rule changes` | A probe in a `git clone --no-local` of the branch ran `rule_changes.py#parse` over this file and `rule_changes.py#apply_op` over each operation against the documents at `1359abcb9` (executed). The parse gave no error and no unread line, every operation was placed, and the added row landed as the last row of the file table in *seal/threads/<work-item-id>/* |
| The tickets | #1415's body as folded, and its comments as the orchestrator's line gives them: 6680032736 and 6680051546 folded into the body, 6684287207 recording the fold. #1401 has no comments. Both read with `gh issue view <N> --json body,comments` on 2026-11-06 (executed) |

## Scope

In:

1. **The party that builds the work item writes `changelog.md`, its `### Process changes` table included, and moves the version in the commit that adds it.** The version moves only where the pull request is the first into a release branch named for its version. Under `Implementation` `crafter`, that party is the last phase's crafter. `agents/crafter.md` *Job* names the version move as its write, where `frame/plan.md` *Operational impact* names one. `skills/implement/orchestration.md` *What the answer writes*, in the paragraph opening **Which branch the pull request lands on**, names the fragment's writer as the party that moves the version. The orchestrator still chooses which work item carries the move. The *Operational impact* placeholder of `templates/records/sdd-plan.md` names the version move and the phase that carries it. `skills/code-review/orchestration.md` already names the builder as the fragment's writer and keeps its text. The `docs/` sentences are the `## Rule changes` operations on `docs/releasing/branch-and-release.md` and on `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file*.
2. **The pull request body's first part is a committed record, `seal/threads/<work-item-id>/pr.md`.** The orchestrator writes it once the build's last phase has closed, before it spawns the first round. Where no round runs, it writes it before the broad run. It holds the `Closes` and `Part of` lines, quotes of the work item's records, and the attribution line. Each quote carries its coordinate: the record's path, then the heading, row, finding or line that holds it. It holds no sentence of the orchestrator's own account. Where a fix pass or a fold changes a sentence `pr.md` quotes, the orchestrator rewrites the quote and commits it before the next round's spawn. Before each spawn of the sealer, the orchestrator opens each quote's source at HEAD and finds the quote there verbatim, runs of whitespace collapsed. `pr.md` is in the language `Commit and pull request language` names. The rule is written in `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, in `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* item 2, in `skills/commit-pr-convention/SKILL.md` *Pull request bodies*, in the file table of `skills/implement/SKILL.md` *3. The SDD file set*, in `templates/setup/seal-README.md`'s tree, and in `agents/sealer.md` step 2. The `docs/` sentences are the other `## Rule changes` operations, each naming `pr.md`.
3. **`seal pr-body` writes `pr.md` as the body's first part, and `--check` reads it.** The command writes `pr.md`'s text, then the line `pr_body.py#HEADING` holds, then the copy, as *Data & interfaces* lays out. `--check` refuses each line above that line that is not `pr.md`'s, and refuses where `pr.md` is absent. The module docstring states the new first part. The sealer cases of `evals/scripts/rule_cases.py` write their `OWN_PART` into `pr.md`, and the cases under `evals/behaviour/sealer/` are written again from it.
4. **What the orchestrator wrote in its own words leaves the body.** The broad run's printed figures and a CI run taken after the rounds have no record and come after the last round, so they leave; the copy carries `trail/gate.md`'s `run:` line. The run's comparison table goes to the flow log's comment alone (`skills/verify/orchestration.md`, the paragraph opening **When the run ends**, and `skills/commit-pr-convention/SKILL.md` *Pull request bodies*). The orchestrator writes why the title takes its prefix as one row of `frame/plan.md` *Judgments of the run*, and `pr.md` quotes the row. The framer's judgment left after the exchange is quoted from its `frame/plan.md` *Alternatives considered* row (`skills/implement/orchestration.md` *The frame is read against the issue at the spawn*).
5. **Every round reads the work item's present-stating records whole against its target.** This holds for a finding round and a verifying round alike. The files are `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`. A frame section dated to the commit the framer read states that commit. Each sentence the target contradicts is a finding located in its file. So is each quote of `pr.md` that does not stand verbatim at its source. The read sits beside a verifying round's bound to the fix diff, which bounds the code it reviews. `agents/proofer.md` gains the rule and step 3's reading list. The *Target* row of the table in `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* names the read.
6. **#1415's item 3 changes no file.** The tree holds it (*Grounding*, the `agents/crafter.md` row). Its cost is weighed in `frame/plan.md` *Alternatives considered*, the row on a new crafter read.
7. **`agents/framer.md` says a frame states a count of a list once, beside the list, and cites it elsewhere.** It is one rule in `## Rules`. Every other sentence of the three frame files that needs the number cites the list by its coordinate. An item's own number, such as *Scope* item 3, is a coordinate and not a count.
8. **The last phase writes `changelog.md` and moves `.claude-plugin/plugin.json` from 0.33.0 to 0.33.1 in the same commit.** The changelog ends with `### Process changes`, one row for each of scope items 1, 2, 5 and 7.

Out:

- A script that checks each quote of `pr.md` against its source. Grounds: `frame/plan.md` *Alternatives considered*.
- A sealer verdict that names the round whose target held a withheld sentence. A round record's `target:` line already gives that commit, and `git show <target>:<path>` reads the sentence there. Grounds: `frame/plan.md` *Alternatives considered*.
- The orchestrator's fold rule in `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*. #1401 *Where the lesson belongs* says the copies came back after it stood, and scope item 7 removes their cause instead.
- `README.md`'s sentence that "the pull request body names it for you to overturn", and rung 4 of `docs/running/the-run.md` *The run*. A quote in `pr.md` and the copy's round records keep both true.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| The body opens with `pr.md` | Given a work item whose `pr.md` holds a `Closes` line and one quote, when `seal pr-body <item> --body <file>` runs, then the file holds `pr.md`'s text, then the heading line, then the copy | a new case in `tests/skills/test_pr_body.py`, seen red against `pr_body.py` at `1359abcb9` |
| A first part that is not `pr.md` is refused | Given a body file whose part above the heading differs from `pr.md` at one line, when `--check` runs, then it exits 1 and its `refused:` line names that line of the body | a new case in `tests/skills/test_pr_body.py`, seen red with the comparison of the first part removed |
| A work item with no `pr.md` is refused | Given no `pr.md` in the work item, when either form of the command runs, then it exits 1 and its `refused:` line names `pr.md` and the repair | a new case in `tests/skills/test_pr_body.py`, seen red against `1359abcb9` |
| The sealer's cases still hold | Given the sealer cases written again from `evals/scripts/rule_cases.py`, when the layout test reads them, then each case is what the script writes | `tests/behaviour/test_evals_layout.py` and `tests/behaviour/test_the_sealer_guarantees.py`, narrow runs |
| One party writes the fragment and moves the version | Given `agents/crafter.md`, `skills/code-review/orchestration.md` and `templates/records/sdd-plan.md`, when each is read for who writes `changelog.md` and moves the version, then each names the party that builds the work item | the phase record's census: `git grep` on "version" and "fragment" in `agents/`, `skills/` and `templates/` |
| A round reads the records | Given a round of any kind, when the proofer follows `agents/proofer.md`, then its record reads each file of *Scope* item 5 whole against its target | review reads the definition; the first run under the installed 0.33.1 shows it in a round record |
| #1415 *Done when*, the first line | Given a work item run under the installed 0.33.1, when the sealer audits it, then no withhold names a sentence of `changelog.md`, of `pr.md` or of the frame that HEAD contradicts, unless that sentence stood at a round's target | the milestone's paid run on the merged tree, read by the owner |
| #1401 *Done when*, the second line | Given the next settle, when it counts the findings located only in a work item's records that are stale counts, then it counts fewer than eight | the next settle's count, read by the owner |

## Data & interfaces

`seal/threads/<work-item-id>/pr.md`, written and committed by the orchestrator:

```
"<a record's sentence, as it stands>" (`<path>` *<heading>*)

Closes #<N>.

<the attribution line>
```

A quote stands on its own line, in a list item or in a table cell, with its coordinate after it. No sentence of the orchestrator's frames a quote or joins two, and no heading or bold lead-in of its own stands in the file.

`seal pr-body <item> --body <file>` writes the body file as `pr.md`'s bytes, then `pr_body.py#HEADING` on its own line, then the copy as `pr_body.py#compose` gives it at `1359abcb9`, the seal mark included. Whatever the body file held before is replaced. The exit codes are unchanged: 0 written or matching, 1 refused, 2 not a directory.

`seal pr-body <item> --body <file> --check` refuses in two new ways, each one `refused:` line in the form `pr_body.py#_place` writes. The first stands where `pr.md` is absent, and the writing form refuses the same way. The second stands at each line above the heading where the body and `pr.md` differ:

```
refused: <root>/threads/<id>/pr.md: is not there; the orchestrator writes it before the first round
refused: <body file>:<line>: reads `<text>`; pr.md gives `<text>`
```

## Rule changes

- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: The orchestrator moves it in the commit that adds the changelog
    fragment of the release's first work item, and every later pull request
    into the branch leaves it.
  to: The party that writes the changelog fragment of the release's first
    work item moves it in the commit that adds the fragment, which is the last
    phase's crafter where a crafter builds the work item, and every later pull
    request into the branch leaves it.
- change
  file: docs/layout/the-record-layout.md
  section: A change writes fragments, never a shared file
  from: The orchestrator writes it with the fragment.
  to: The party that writes the fragment writes it with the fragment, which is
    the last phase's crafter where a crafter builds the work item.
- add
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  to: | `pr.md` | what the pull request body opens with: the `Closes` lines and quotes of the other records, each with its coordinate, written before the first round so that every round reads it |
- change
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: (`gaps.md`, `changelog.md`, `guarantee.md`, and a `pr.*.md` where one
    was written)
  to: (`gaps.md`, `changelog.md`, `guarantee.md`, `pr.md`, and a `pr.*.md`
    where one was written)
- change
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: A record cites another's fact by its path and heading and does not
    restate it, so a template holds no section or cell that could hold only a
    copy.
  to: A record cites another's fact by its path and heading and does not
    restate it, so a template holds no section or cell that could hold only a
    copy. `pr.md` is the one exception, because the reader of the pull request
    reads it before the fold: it holds quotes of the other records, each
    found verbatim at its source, and no fact of its own.
- change
  file: docs/forms/the-guarantee.md
  section: The guarantee
  from: the orchestrator writes above that line what no record holds, and
    states a record's fact only as that record's own sentence or with the
    coordinate of the row, heading, finding or line that holds it.
  to: above that line it writes the work item's `pr.md`, the orchestrator's
    part, which holds the `Closes` lines and quotes of the records, each with
    its coordinate, and no sentence of the orchestrator's own account.
- change
  file: docs/forms/the-guarantee.md
  section: The guarantee
  from: and withholds where the part below the line is not what the records
    give.
  to: and withholds where the part above the line is not `pr.md` or the part
    below it is not what the records give.
- change
  file: docs/running/the-run.md
  section: The run
  from: and names it in one line of the pull request body, where the owner can
    overturn it.
  to: and quotes that row in the work item's `pr.md`, the pull request body's
    first part, where the owner can overturn it.
- change
  file: docs/layout/one-root-by-lifetime.md
  section: Naming
  from: and `routing.md`, `changelog.md`, `guarantee.md` and `gaps.md` at its
    top
  to: and `routing.md`, `changelog.md`, `guarantee.md`, `gaps.md` and `pr.md`
    at its top
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: 이름
  from: 맨 위에 `routing.md`, `changelog.md`, `guarantee.md`, `gaps.md` 를 둔다.
  to: 맨 위에 `routing.md`, `changelog.md`, `guarantee.md`, `gaps.md`, `pr.md` 를
    둔다.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The first part kept from the body file as its bytes stood | `skills/code-review/scripts/pr_body.py#main`, the `own = ... split(body)[0]` line | `pr.md`, which the command writes above the heading (*Scope* item 3) |
| The first part read by no check | `skills/code-review/scripts/pr_body.py#_check`, the docstring's "The part above it is the orchestrator's and is not read" | `_check` compares that part with `pr.md` |
| The orchestrator's part as "what no record holds", with the list of what it may hold, and a record's fact stated "with the record's coordinate" | `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, the paragraph opening **You write the pull request body after** | `pr.md`'s quotes and `Closes` lines (*Scope* item 2). The broad run's figures and a CI run after the rounds go with no home, since the copy carries `trail/gate.md` |
| The comparison table opening the orchestrator's part | `skills/commit-pr-convention/SKILL.md` *Pull request bodies*, the paragraph opening **Its chain section has one shape** | the flow log's comment, the table's one destination (`skills/verify/orchestration.md`, the paragraph opening **When the run ends**) |
| The pull request body's chain section as a place the run's table goes | `skills/verify/orchestration.md`, the paragraph opening **When the run ends** | the comment that carries the numbers, which that paragraph already names |
| The prefix's grounds as the orchestrator's sentence in the body | `skills/commit-pr-convention/SKILL.md` *Pull request bodies*, the paragraph opening **The orchestrator's part says in one sentence why the title takes its prefix** | a row of `frame/plan.md` *Judgments of the run*, which `pr.md` quotes |
| The framer's left judgment named by the orchestrator in its own words | `skills/implement/orchestration.md` *The frame is read against the issue at the spawn*, "which the orchestrator names in its part of the pull request body" | a quote in `pr.md` of the `frame/plan.md` *Alternatives considered* row |
| The orchestrator as the party that moves the version | `skills/implement/orchestration.md` *What the answer writes*, the paragraph opening **Which branch the pull request lands on** | the party that writes the fragment (*Scope* item 1) |
| Nothing goes for the rounds' records read | `agents/proofer.md` | The read adds a rule and no check. What it takes over is the sealer's place as the first reader of those sentences. Its catch record before it existed is #1415 *What the sealer caught*, each withhold a sealer re-run, and #1401 *The stale copies*, all found by a round or a sealer. The settle weighs it under `skills/core/SKILL.md` *The rule a mechanism is kept against* |

Framed 2026-11-06 by framer, before the build.
