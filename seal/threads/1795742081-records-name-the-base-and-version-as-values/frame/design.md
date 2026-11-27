# Design: records name the base, the version and the tags as values

Issue: #1633, `fix: records name the base branch, the version and the tags as values, so a release's rename, merge or tag makes them false`.

## Grounding

The tree as read at `82169bfcc`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A fact has one source, and every other place links to it", and "Nothing is kept beside the tree to stay in step with it, such as a stored count or coordinate" (read) | A branch's name or tip, a tag and the version a release carries are facts that git, the tracker or the version file holds. A record sentence that states one as a present fact is a copy kept beside its source, and nothing brings the copy along when the source moves |
| G2. `skills/agent-contract/SKILL.md` rule 19, lines 193 to 217 (read; executed: its text is the same in the tree and in the installed 0.39.1 copy, by `diff` of the two sections) | Its second paragraph refuses a count or a universal "that a later change can make false without editing the sentence", lets one "stated of a named commit, a release or a dated measurement" stand as "a claim about that moment", and puts in its place the members or "the list, the section or the command that lists them". The issue's sentences are the same kind: they go false with no edit. What differs is the cause. There a later change makes the sentence false, and the first paragraph has that change search. Here a cut, a rename, a merge of another pull request or a tag does it, and none of them is a commit on the work item's branch, so no change searches and no round is owed. The remedy and the exemption are the ones rule 19 already states, so the rule this work adds stands in rule 19 |
| G3. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, the paragraph opening **Nothing else follows them, because there is nothing else.**, lines 98 to 112 (read) | A round record, a closed phase's Status cell, and the frame's *Grounding* and *Technical context* are claims about a named commit. A reader holds each other record sentence against HEAD. The state of the release is not in HEAD's tree, so a reader holds such a sentence against the refs and the tracker as they stand on the day it reads |
| G4. The issue's evidence (nobody's finding in this tree: the three Owlery records it quotes are in another repository, and the repository owner answers for them) | A `routing.md` named the base as `release/v0.0.5`, three frame sentences predicted what stands "once `release/v0.0.5` is deleted", and a plan said "moves no version" of a work item that later moved it. The issue says each was true when written |
| G5. What the class costs (nobody's finding in this tree; executed: `gh issue view 1632 --json comments` on 2026-11-27 prints the comment that holds the count, and the round records it counts are in another repository) | #1632's comment counts 12 of 120 findings of Owlery releases 0.0.5 and 0.1.0 as "stale after a release was renamed, merged or tagged" |
| G6. This tree's own findings of the class (read: `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/trail/rounds/round-4.md` lines 40 to 90, and `seal/threads/1795389517-three-github-scripts-ship-in-dist/trail/rounds/round-1.md` finding 2) | In the first, a plan row and a plan sentence said the work item merges first into `release/v0.37.3`, and another item's pull request merged first. In the second, a plan sentence said the release's other items were "none branched yet", and two were checked out beside it. The second finding's grounds say that *Overlap with the release* is not a section dated to a commit, so the sentence is held against the target. Each was fixed by a fold, in a commit that touched records alone |
| G7. Values this tree's routing records name (executed at `82169bfcc`: ``git grep -n -o -E 'cut from `origin/release/v[0-9.]+` at `[0-9a-f]+`' -- 'seal/threads/*/routing.md'``, and on 2026-11-27 `git for-each-ref 'refs/remotes/origin/release/*'` with `git ls-remote --heads origin 'release/*'`) | Each line the search prints says in the present tense that a branch "is cut from" a named release ref "at" a named commit. On 2026-11-27 each ref those lines name stands at another commit. Each sentence names the cut and the commit it was made at, so it states the ref of that moment, and clause R4 keeps it. A reader who takes the present tense "is cut" for today's state is the drift `frame/plan.md` *Technical context* names |
| G8. Who asks a record for these values (executed at `82169bfcc`: `git grep -n -i -E 'version moves\|moves the version\|the move' -- skills agents docs templates CONTRIBUTING.md .github tests` and `git grep -n -i -E 'version\|branch\|base\|tag\|release' -- templates/records`; read: `templates/records/sdd-routing.md`) | `templates/records/sdd-plan.md:31` asks *Operational impact* for "the move and the phase whose commit adding `changelog.md` carries it", and line 23 asks *Overlap with the release* for the other items "as the spawn names them and as their frames stand where committed". `templates/records/sdd-routing.md` asks the `Branch` row for the work item's own branch and *Why this way* for grounds. No line of a template or a skill asks `routing.md` for the base, a cut commit or a version number: the bullets that name them in G7's files follow no form |
| G9. What already answers a changed decision (read: `skills/implement/orchestration.md` lines 62 to 75 and 144 to 152, `skills/implement/merge-order.md`) | The version move is a decision the framer folds into the frame, and a merge out of the stated order owes a *Judgments of the run* row. So the plan that said "moves no version" (G4) and the plan row of G6's first finding were each owed a fold or a row under rules that stand. This work changes neither rule. It changes how a sentence is written so that fewer sentences depend on the state those rules follow |
| G10. The form lines a check reads by value (read: `lib/routing.py` lines 73 and 237 to 250; executed: the second search of G8 prints `templates/records/sdd-round.md:4` and `templates/records/sdd-guarantee.md:16`) | `lib/routing.py` reads the `Branch` row of `routing.md` as the work item's branch, and a round record and `guarantee.md` carry `target: <sha> against <base>` in a `seal` block. A role in one of these lines is a line the check does not read, so they keep their values |
| G11. Where rule 19 is cited (executed at `82169bfcc`: `git grep -n -E 'rule 19' -- ':!seal/threads'`; read: `tests/text/test_the_rules_have_one_owner.py` lines 345 to 362 and 404 to 420) | `skills/implement/fix-pass.md:48`, `skills/implement/fold-and-reframe.md:24` and `skills/code-review/orchestration.md:224` each cite "a count or a universal contract rule 19 refuses", `skills/implement/orchestration.md:35` binds the text the orchestrator's commits write to contract rule 19, and `RULES` row 30 holds those four citations. No template cites the rule: `git grep -n -F 'contract rule 19' -- templates/records` prints nothing and exits 1 (executed at `82169bfcc`) |
| G12. What the contract's cases pin (read: `tests/text/test_the_agent_contract_holds_the_universal_rules.py` lines 20 to 92 and 225 to 260) | `HEADING` reads `## <N> <title>`, and `FACTS` pins phrases of rules 1 and 21 alone. A reworded heading of rule 19 that keeps its number, and a paragraph added to its body, leave those cases green |
| G13. What reads the two templates this work edits (read: `tests/behaviour/test_the_set_a_work_item_always_has.py` lines 52 to 100, `tests/behaviour/test_waiver_decided_at_start.py` lines 192 to 204, 265 to 280 and 336 to 350) | The plan template's cases pin the header rows of its tables and that *Overlap with the release* stands immediately before *Operational impact*. The routing template's cases parse its rows with `lib/routing.py#parse` and pin the `Planning` placeholder row. None pins the placeholder text under `## Why this way` or the two plan placeholders this work rewords |
| G14. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* and `skills/settle/rule-changes.md` *Rule changes* (read); the unsettled operations on the same section (executed at `82169bfcc`: `git grep -n -A1 -E '^  file: docs/running/the-agent-set.md' -- 'seal/threads/*/frame/design.md'`) | This work's subject is the code: it edits `skills/`, `templates/` and `tests/`. The policy's account goes into `## Rule changes` as an `add` on `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each*, where #1613's design holds an unsettled `add` about rule 19's count clauses. `docs/README.md` lists no `.ko.md` edition of that document (read) |
| G15. `hooks/edit-leaves-copies.py` lines 1 to 70 and `hooks/hooks.json` (read) | The hook is matched on `Edit` alone, prints a note and never blocks, and by its docstring "writes nothing, starts no process and reaches no network". `frame/plan.md` *Alternatives considered* weighs widening it |
| G16. `seal/follow-up.md` (read whole) | Its rows for #1612 to #1615 and #1623 each send a measurement in a later release to the repository owner. None waits on this work. The row for #1613 measures findings "on a count or a universal", which the paragraph this work adds does not change. The issue's second *Done when* line is a measurement of the same kind, and *Scope* item 5 adds its row |
| G17. The issue's comments (executed: `gh issue view 1633 --json body,comments` on 2026-11-27 prints no comment) | The body is the request |
| G18. `routing.md` (read) | `Planning` framer, `Implementation` crafter, `Review` through the review chain, `Automation` yes. Its *Why this way* names the base by role, "the open release branch after #1620's pull request merged into it" |
| G19. The version (executed at `82169bfcc`: `grep -n version .claude-plugin/plugin.json` prints line 4, `0.39.2`; `git show 68bb3d5a9 --stat -- .claude-plugin/plugin.json` shows that commit changed the line; `git merge-base HEAD origin/release/v0.39.2` printed `68bb3d5a9` on 2026-11-27) | The release's version move was made at `68bb3d5a9`, which this branch descends from. This work item carries no move |
| G20. The latest release's `### Process changes` (executed: `gh release view --json body,tagName` on 2026-11-27 prints `v0.39.1` and one row, on the reading a fix pass owes) and the fragment of `1795569535-a-fix-writes-a-count-into-a-record` (read) | No row changes how a record names a value. The fragment's row for rule 19 is the shape *Scope* item 6 follows |
| G21. The mechanisms weighed for rule 19 before (read: `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/plan.md` *Alternatives considered*, the rows from the `PreToolUse` hook to the output style; each a claim of that frame, not probed here) | Those rows weighed a hook of each type, an agent-definition field, a `seal` subcommand, a workflow and the other components against a reader of record text. `frame/plan.md` cites them and argues again only what this class changes |
| G22. The parse of this design's `## Rule changes` (executed on 2026-11-27: a probe `test_tmp_parse_rule_changes.py` calling `skills/settle/scripts/rule_changes.py#parse` with `python3 -I`, from a `git clone --no-local` of `82169bfcc` under the framer's scratch directory, over a copy of this file as it stood before the words "a record from stating" and "The record states" of the `to` value became "a change from writing" and "The text states") | The section parses as one `add` on `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each*, with no error and no unread line |
| G23. The second *Done when* line has no row yet (executed at `82169bfcc`: `git grep -n -F '#1633' -- seal/follow-up.md` prints nothing and exits 1) | *Scope* item 5 adds the one row that search prints after the build |

## Scope

In:

1. `skills/agent-contract/SKILL.md` rule 19 keeps its number, takes the heading of *Data & interfaces*, and gains one paragraph after its second, holding clauses R1 to R6 of *Data & interfaces*. The sentence on a named moment is stated once for a count, a universal and a value alike, and the sentence on the rule's reach stays the rule's last.
2. `templates/records/sdd-routing.md`: the placeholder under `## Why this way` gains the sentence of *Data & interfaces*, which cites contract rule 19 for how the grounds name the base, the version move and the merge order.
3. `templates/records/sdd-plan.md`: the placeholders of *Overlap with the release* and *Operational impact* are reworded as *Data & interfaces* states, each citing contract rule 19. The table headers and the order of the sections stay.
4. `tests/text/test_the_rules_have_one_owner.py`: `RULES` gains a row, numbered after the highest key, whose owner is `skills/agent-contract/SKILL.md`, whose fact is the heading number `## 19 `, and whose carriers are the two templates of items 2 and 3, each linked by the citation `contract rule 19`. The row is seen red once per carrier with that carrier's citation removed (contract rule 15).
5. `seal/follow-up.md` gains one row for the issue's second *Done when* line, naming the repository owner: whether the next release of a repository that runs the chain counts fewer findings on a sentence that a rename, a merge or a tag made false than #1632's comment counted (G5), and that the text of rule 19's new paragraph goes to the weighing of `skills/core/SKILL.md` *The rule a mechanism is kept against*, beginning with the hook `frame/plan.md` *Alternatives considered* rejects, where the count does not fall.
6. The work item's `changelog.md`: a `### Fixed` entry for the rule and the templates, the sentence that the settle writes the policy's account from `## Rule changes`, and one `### Process changes` row in the shape of `templates/records/process.md`. It states no version move, because this work item carries none (G19).

Out:

- Rewriting the sentences of G6 and G7, or any other record under `seal/threads/`. Those records are other work items', the settle removes each directory after the release that ships it, and rule 19 binds what a change writes from here on.
- A script, a hook, a `seal` subcommand, a workflow or an agent-definition field that reads a record for a branch name, a tag or a version. `frame/plan.md` *Alternatives considered* weighs each and rejects it here.
- `skills/implement/fix-pass.md`, `skills/implement/fold-and-reframe.md` and `skills/code-review/orchestration.md`, whose citations name "a count or a universal contract rule 19 refuses". Each stays true, and the party that reads it preloads or has opened the contract. The frame of the work item for #1624, #1628 and #1629, committed at `762f284f7`, changes `skills/implement/fix-pass.md` and `skills/code-review/orchestration.md` (its *Scope* items 4 and 5), and does not name `skills/implement/fold-and-reframe.md`.
- `skills/implement/orchestration.md`. Step 1 of *Orchestrator: the order inside a ticket* already binds the text the orchestrator's commits write to contract rule 19, and `routing.md` is such a text.
- `skills/implement/SKILL.md` and a dated head line on *Overlap with the release*. `frame/plan.md` *Alternatives considered* holds why.
- The `Branch` row of `routing.md` and the `target:` lines (G10), which clause R5 keeps as they are. The issue proposes that the routing template's Branch line state the base by role. In this tree that row states the work item's own branch and no base, and the base stands in *Why this way*, which item 2 reaches.
- The fragment line "The version moves to" a number, in the `changelog.md` of a work item that carries the move. It states what its own commit writes to the version file, which is a state the work item's commits make, and clause R6 keeps it.
- `docs/releasing/branch-and-release.md`, which states where the version moves as a rule and names the branch by the pattern `release/vX.Y.Z`.
- An edit of the policy root. Its account of the rule is the `add` of `## Rule changes`, which the settle writes.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A1. The orchestrator writes `routing.md` | Given a new work item, when the orchestrator fills `templates/records/sdd-routing.md`, then the placeholder under `## Why this way` tells it to name the base, the version move and the merge order as contract rule 19 states | the `RULES` row of *Scope* item 4, carrier `templates/records/sdd-routing.md`; `bin/test -q tests/behaviour/test_waiver_decided_at_start.py tests/lib/test_routing.py` stays green, so the template still parses as a declaration |
| A2. A framer fills the plan | Given a release that holds other work items, when the framer fills *Overlap with the release* and *Operational impact*, then each placeholder tells it how a state of the release is stated and cites contract rule 19 | the `RULES` row, carrier `templates/records/sdd-plan.md`; `bin/test -q tests/behaviour/test_the_set_a_work_item_always_has.py` stays green |
| A3. The two templates are the rule's carriers under `templates/records/` | Given the build, when a reader searches the record templates for the citation, then it stands in the two templates of *Scope* items 2 and 3 | `git grep -n -F 'contract rule 19' -- templates/records` prints lines of `templates/records/sdd-plan.md` and `templates/records/sdd-routing.md` and of no other file. At `82169bfcc` it prints nothing (G11) |
| A4. Every agent receives the rule | Given any spawn, when the agent starts, then rule 19 with its new paragraph is in the contract its `skills:` list preloads | `bin/test -q tests/text/test_every_agent_reads_the_contract.py tests/text/test_the_agent_contract_holds_the_universal_rules.py`, both unchanged; the proofer reads rule 19's body against clauses R1 to R6 |
| A5. A value stated of a named moment stays | Given a record that says a branch was cut from a named ref at a named commit on a named date, when the ref later moves or is renamed, then the sentence is not false and no round raises it | the proofer reads clause R4 in rule 19's body |
| A6. A form line keeps its value | Given `routing.md`'s `Branch` row and a round record's `target:` line, when a party writes them under the new paragraph, then each holds the value its form gives it | the proofer reads clause R5; A1's two test files |
| A7. The second *Done when* line has an answerer | Given the build, when a reader opens `seal/follow-up.md`, then one row names #1633, what is counted and the repository owner | `git grep -n -F '#1633' -- seal/follow-up.md` prints that one row. At `82169bfcc` it prints nothing (G23) |
| A8. This work item's own records hold to the rule | Given the work item's records at the target, when the proofer reads them, then each sentence that names a release ref, a commit of the base or the version states it of a named commit or date, or names it by role | the proofer reads `routing.md`, the three frame files, `gaps.md` and `changelog.md` against clauses R1 to R6 |

## Data & interfaces

No code interface changes. The units are text.

Rule 19's heading becomes `## 19 A change rewrites the text it amends in place, and writes nothing that goes stale unedited`, or words of the same meaning that keep the number. Its first two paragraphs keep their sentences, except that the sentence on a named moment and the sentence on the rule's reach move as *Scope* item 1 says. The crafter adds these clauses in its own words, each of them:

- R1. What a change writes states no value of a state outside the work item's branch that a later act can make false without a commit on that branch. The name or the tip of a branch, the base a pull request merges into, a tag, the version a release carries, and what another work item has branched, framed or been ordered to do are examples of such a state, and the text says they are examples. A prediction of such a state after a later act is held the same way.
- R2. The reason: a cut, a rename, another pull request's merge, a tag or a deleted branch changes the state and makes no commit on the work item's branch. So no change searches for the sentence as the rule's first paragraph asks, and no round is owed that would read it.
- R3. In its place the text states what the work item decided and names each thing by the role it plays, such as the release branch, the release's first pull request, or the item that carries the version move. Where a reader needs the value, the text names the file or the command that reads it at that time.
- R4. A value stated of a named moment is a claim about that moment and stays. The moments are the ones the rule's second paragraph names for a count and a universal, a named commit, a published release and a dated measurement, with a date and a cut the sentence names. A release still open is no moment. The sentence is stated once for the three.
- R5. A line of the plugin's forms that a check reads by value keeps the value its form gives it. The `Branch` row of `routing.md` and the `target:` line of a round record and of `guarantee.md` are such lines.
- R6. A value whose source is a file the work item's own commit has written is a state of its branch and not one outside it, and a sentence that states it stays. The example is the version that the work item carrying the move has written to the version file and states in its `changelog.md` (round 1, finding 2). Before that commit, the number is a prediction, which R1 holds (round 2, finding 1).

The placeholder under `## Why this way` of `templates/records/sdd-routing.md` keeps its present sentence and gains one that says, in these or like words: the grounds name the base, the version move and the merge order by what was decided and by role, and state a branch name, a commit or a version number only of a named moment, as contract rule 19 states.

The two placeholders of `templates/records/sdd-plan.md` keep what they ask for and change as follows:

| Placeholder | Reads at `82169bfcc` | Changes to say |
|---|---|---|
| *Overlap with the release* | "each other open work item of the release that this work meets, as the spawn names them and as their frames stand where committed" | the same, and that what another item has branched, framed or merged is stated with the date or the commit it was read at, as contract rule 19 states. The *Merges first* cell stays this work's conclusion, with no date |
| *Operational impact* | "where this pull request moves the version, the move and the phase whose commit adding `changelog.md` carries it" | where this pull request carries the release's version move: that it does, the phase whose commit adding `changelog.md` carries it, and the file or the command that phase reads the version from, with a version number stated only of a named moment, as contract rule 19 states |

Where each party that writes a record receives the rule, the parties being the agents `ls agents/` lists and the orchestrator:

| Party | The record it writes | Receives rule 19 | Meets it at the step it writes |
|---|---|---|---|
| orchestrator | `routing.md`, `pr.md`, *Judgments of the run* rows, a fold of what a crafter names | step 1 of `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* | the placeholder of `templates/records/sdd-routing.md` (*Scope* item 2) |
| framer | the three frame files | preload | the two placeholders of `templates/records/sdd-plan.md` (*Scope* item 3) |
| crafter | `gaps.md`, phase records, `changelog.md`, close blocks | preload | none added: G4 and G6 name no sentence a crafter wrote |
| proofer | round records and paste-ready fixes | preload | none added: a round record's base is its `target:` line (R5) |
| sealer | `guarantee.md` | preload | none added |
| tracer | facts with coordinates | preload | none added |

## Rule changes

- add
  file: docs/running/the-agent-set.md
  section: One contract every agent receives, and one definition each
  to: **Contract rule 19 keeps a change from writing, as a present fact, a
    state outside the work item's branch that a later act makes false, and
    nothing reads a sentence for one.** The name or the tip of a branch, the
    base a pull request merges into, a tag and the version a release carries
    change at a cut, a rename, another pull request's merge or a tag, and
    none of those acts is a commit on the work item's branch. So no change
    searches for the sentence and no round is owed that would read it, and
    it stands false until a later round or a later release meets it (#1633).
    The text states what the work item decided and names each thing by its
    role, names the file or the command that reads a value a reader needs,
    and may state a value of a named commit or date. A form line that a
    check reads by value keeps its value, and so does a value whose source
    is a file the work item's own commit has written, such as the version
    that the item carrying the move has written to the version file. The
    placeholders of
    `templates/records/sdd-routing.md` and `templates/records/sdd-plan.md`
    cite the rule where the orchestrator and the framer write the release's
    state. Whether a sentence states today's state or a named moment's is
    the reader's judgment, so no script reads for one.
    check: tests/text/test_the_rules_have_one_owner.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| a rule sentence: the heading words "and writes no count that goes stale" | `skills/agent-contract/SKILL.md` rule 19, its heading | Rewritten in place by *Scope* item 1 to the heading of *Data & interfaces*, which covers a count, a universal and a value |
| a rule sentence: the exemption scoped to a count and a universal, "A count or a universal stated of a named commit, a release or a dated measurement is a claim about that moment and stays." | `skills/agent-contract/SKILL.md` rule 19, its second paragraph | Rewritten in place by *Scope* item 1 as clause R4, stated once for a count, a universal and a value |
| a template clause: "where this pull request moves the version, the move and the phase whose commit adding `changelog.md` carries it" | `templates/records/sdd-plan.md` *Operational impact*, its placeholder | Rewritten in place by *Scope* item 3, which asks for the decision, the phase and where the phase reads the version |

Nothing goes in return for the paragraph rule 19 gains. No text of the tree asks a record for a branch name, a cut commit, a tag or a version number, other than the template clause above: G8's searches print that one line, and the bullets of G7 follow no form. The count clauses of rule 19 stay, because `seal/follow-up.md`'s row for #1613 still waits on their measurement (G16). The work adds no gate, check, hook or mark: the `RULES` row of *Scope* item 4 holds two citations, as row 30 holds the citations of the count clauses.

Framed 2026-11-27 by framer, before the build.
