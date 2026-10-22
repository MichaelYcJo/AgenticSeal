# Questions for the planner: #1005 the section sign is still syntax

**What the issue and the owner's widening left open, and the tree
answered.** Nobody reopens these; the grounds are in `spec.md` and `plan.md`.

- **Number or heading text for the contract's rules: number.**
  `docs/the-agent-set.md` *One contract every agent receives, and one
  definition each* makes the numbers stable and cited, and a heading-text
  citation grows every preload (`plan.md` A1).
- **The spelling: `contract rule N`, and `rule N` inside the contract and
  `agents/`.** The free simulation in `plan.md` *Technical context* is the
  only spelling of four that lowers every preload (executed).
- **The records of a moment are not rewritten for the section sign.**
  `seal/specs/`, `changelog/`, `CHANGELOG.md` and `evals/behaviour/`: a
  record states what was true when written, `CONTRIBUTING.md` *House rules*
  gives `changelog/` to the branch based on `main`, and `evals/README.md`
  says the cases are generated and never edited by hand.
- **The old spelling is refused by one case, not by each reader.** One fact
  read in one place (`plan.md` A6, A7).
- **`skills/verify/scripts/coordinates.py` needs no reader change for the
  section sign.** At a16acb40 it carries one, in a docstring, and its grammar
  reads none (executed). Its `#` and `>` are Q2.
- **The dash in the release heading `## X.Y.Z — <date>` is not this item's.**
  Neither the issue nor #941's Q2 names it (`spec.md` *Scope*).
- **No comment in a record template is anything but guidance.** All eight
  `templates/sdd-*.md` were read: their 23 comments explain how to write the
  record, and no reader reads one. The comments outside those templates that
  are needed, the two `specseal` block markers and the changelog marker,
  stay (`spec.md` *Scope*).
- **The fence state stays, as one copy.** A finding's fix stays fenced, and
  a fix to a record's own grammar can hold a line shaped like a label
  (`plan.md` B1, B2).
- **The guidance goes to what its writer opens, not to the preloaded agent
  definitions** (`plan.md` B4, B5).
- **`live_lines` and the config reader keep their comment states.** They
  read files that are not records (`spec.md` *Scope*).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Do the changelog markers `<!-- specs/<id> -->` change? The issue lists them as left over, #941's Q2 called them syntax a check reads, and the owner's direction of 2026-10-22 is to write a comment only where it is truly needed. **Why the tree cannot answer:** `docs/branch-and-release.md` *Work accumulates on a release branch* states the comment and why it is invisible, so changing it changes a docs rule, and whether the owner counts the marker as needed is the owner's to say | a person | (a) **Unchanged**: the marker is the needed case, invisible in the release note and the only link back; `gather_changelog.py` loses only its two section signs. (b) **A visible line**: a docs rule change, and a rewrite of the markers in 54 release files, which only the branch based on `main` may make, so it lands at a release and not here; the release note shows each id twice, once in the line and once in the entry's own trailer. (c) **Near misses refused**: fails on 27 lines of an older convention in 11 release files (executed), which this branch may not edit | (a). The build proceeds on it; `plan.md` A11 to A13 hold the grounds | open |
| Q2 | Does this item also take the coordinate grammar's `#` and `>` and the pact anchors `skills/verify/scripts/coordinates.py` reads? `seal/specs/1792540458-on-demand-files-state-the-current-rule/spec.md` scope item 8 named them for "a later item", and #1005 is that item, but the issue's text names only the section sign and the changelog markers, and the owner's widening names comments and fences. **Why the tree cannot answer:** which of the texts sets the scope is the owner's, and a pact anchor is written in another repository's tree | a person | (a) **Not here**: a later item takes them, with the cross-repository migration a pact anchor needs, and `templates/pact.md`'s comment with them. (b) **Here**: a new phase that changes `coordinates.py`'s grammar, `pact_check.py`, `chain_check.py`'s anchor reading, `templates/sdd-spec.md`'s `## Removes` hint and the pact clauses in other repositories | (a) | open |
| Q3 | Is the paid non-inferiority run made? The issue says #923's proof is owed, because the contract and the five definitions are preloaded. **Why the tree cannot answer:** the spend is the owner's. The price, read from #941's Q1: about 65 USD and 3.2 hours a side for framer, smith, sealer and warden (framer about 15, smith 6, sealer 4, warden 40); scribe has no cases | a person | (a) **Both sides, four agents**, after the last phase: about 130 USD and 6.4 hours serial, and rules 1, 2, 3 and 5 read. (b) **The new side only**, against the newest recorded sides: about 65 USD, but those sides were taken on preloads that have changed since, and `evals/README.md` refuses a warden pair taken across #986's squash. (c) **Not run**: rule 4 is read for free at phases 1, 3 and 4; the preload change is the spelling of citations and any guidance sentence phase 4 moves into a definition, with no rule added or removed, and the precedent is #941's Q1, answered (c) by the owner on 2026-10-20 | (c). The build proceeds without a run, and the pull request body names the departure from the issue. A run not made can still be ordered at the pull request | open |
| Q4 | What does a touched citation become where its file has no such heading? Two are known (`spec.md` scope item 9); the rest are known only when each line is read. **Why the tree cannot answer now:** it needs each citation read against the rule it points at | the work | The phase that meets one names the heading that now holds the rule, or, where none does, rewrites the pointer in words | The heading that holds the rule; each one listed in the phase record | open |
| Q5 | Is every agent's preload below its baseline at the end, measured against the base this branch has once #988 and #1009 merge? #988 changes `agents/warden.md`, and phase 4 may move a guidance sentence into `agents/sealer.md`. **Why the tree cannot answer now:** the base is not cut yet, and phase 4's moves are not known | a measurement | `noninferiority.py#preload_bytes` for the five agents at the base and at head, run by the smith at phases 1, 3 and 4 | The simulation's figures: every preload falls by 18 to 38 bytes (`plan.md` *Technical context*); a phase 4 sentence that would lift a preload above its baseline goes to `docs/the-review-record.md` through a further `## Rule changes` item instead | open |
| Q6 | Are the old records stripped of their comments now? 611 record files across all 125 work items carry a comment, about 12,240 lines (executed; regex count). `seal/specs/` holds what was true at the time, so rewriting it is the owner's choice. **Why the tree cannot answer:** whether a record of a moment may be rewritten, and when the readers drop a state consuming repositories still need, are the owner's | a person | (a) **Strip now**: phase 6 is built. One commit rewrites 611 files that the owner's settle after 0.22.3 is due to remove anyway; `comment_scan`, `strip_comments` and the comment half of `unclosed` go, and a record line beginning `<!--` is refused. A consuming repository's in-flight work item framed under the old templates is refused after it upgrades, until its records are stripped, and the release note must say so. (b) **Keep reading comments until the backlog is settled**: phase 6 is not built. The records stay as written; the record readers keep the comment and code-span states that #1000 and #988's round 2 tripped on, for one more release; a later item removes them once settle has retired this repository's backlog, and consuming repositories get a release in which new records carry no comment before any reader stops reading one | (b). The build proceeds without phase 6, and the pull request body names the later item's work | open |
| Q7 | Where does each guidance sentence of the templates land? The homes are named per template (`spec.md` *Data & interfaces*), but whether a home already states a sentence is known only by reading the two side by side. **Why the tree cannot answer now:** 23 comments and two bodies of guidance, read one sentence at a time | the work | Phase 4 removes a sentence its owner already states and moves the rest to the named home, listing each in its record | The named home; an agent definition only where no other home fits (Q5) | open |
