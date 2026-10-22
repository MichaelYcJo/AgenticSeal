# Implementation Plan: #1005 the section sign is still syntax

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md holds HOW, in phases. It
is the Design Gate's artifact: where the work alters observable behaviour,
approval of this plan is the gate. -->

Approved <date> by <who>, when `smith` was spawned.

<!-- The line above is the record that the gate happened. The orchestrator
writes it when it spawns the build, in the shape and on the terms
`skills/implement/orchestration.md` *The plan is approved at the spawn*
states, including the shape where `routing.md` answers `Implementation`
with `the session`. A later session, a reviewer and CI all read the tree,
and a plan with nobody's name on it cannot be told from one nobody approved.
The line shares its shape with `templates/sdd-routing.md`'s `Answered <date>
by <who>, before the first edit.`: the verb, the date, who, and the moment.
The two are pinned against each other, so neither spelling can drift into a
second convention for one kind of fact. -->

## Summary

The section sign leaves every living file in three phases, one per kind of
citation, and each phase changes a reader in the same commit as the text it
reads. Phase 1 renumbers nothing: it rewrites the contract's headings and
every contract citation to a plain number. Phase 2 rewrites every citation of
another file's section to its heading text. Phase 3 adds the one case that
refuses the old spelling, rewrites what is left, and states the shape in the
writing rule. `spec.md` holds the spellings, the readers and the counts.

## Technical context

**The build starts after #988 and #1009 merge into `release/v0.22.3`.**
#988's branch at 77eef010 changes 27 files and #1009's at 001098c2 changes
23 (executed: `git diff --name-only eae7f0ad origin/<branch>`). Outside
`seal/specs/`, 14 and 7 of them carry a section sign at the branch's tip,
and the two diffs add 5 and 1 lines that carry one, records included
(executed). So no phase pins a coordinate. Each phase
starts with `git grep -n -I` for the section sign over the living files at
its own HEAD, and the list that command prints is the phase's work.

**Edits go through the `Edit` tool (contract rule 9), file by file.** The
smith uses `replace_all` where one token repeats in one file, and it reads
each line before it edits, because the same character means three things:
a contract rule, another file's section, and the seal's emblem.

**The contract citation spelling was chosen on rule 4.** A free simulation
at a16acb40 rewrote the contract and the five agent definitions in memory
and summed `noninferiority.py#preload_files` for each agent (executed; the
script was a scratch file outside the tree). Byte change against a16acb40:

| Heading shape | Citation outside, inside | framer | smith | warden | sealer | scribe |
|---|---|---|---|---|---|---|
| `## N title` | `contract rule N`, `rule N` | -18 | -30 | -31 | -38 | -23 |
| `## N. title` | `contract rule N`, `rule N` | +2 | -10 | -11 | -18 | -3 |
| `## N title` | `contract rule N` in both | +27 | +33 | +32 | -2 | +40 |
| `## N. title` | `contract rule N` in both | +47 | +53 | +52 | +18 | +60 |

Preloads at a16acb40 (executed): framer 25255 bytes, smith 24746, warden
25109, sealer 23383, scribe 18545. The simulation does not include the
preamble rewrite or rule 12's heading, so phase 1 measures the real figures.

**Failure scenario of the chosen approach.** In six months an agent
definition says "rule 4" meaning a rule of something else, such as the
behaviour suite's pass rules. The citation reader takes it for the
contract's rule 4 and passes it, because only a number above the contract's
last rule is refused. The reader's corpus and its bare-number homes are the
same as the section-sign reader's today, so the risk is not new; it moves
from one character to one word.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Name the contract's rules by heading text | Every citation grows by its heading's length, so every preload grows and rule 4 fails for all five agents. A round record citing a rule by number, of which the records hold hundreds, stops meaning anything, against `docs/the-agent-set.md` *One contract every agent receives, and one definition each* | rejected |
| A2. `contract rule N` everywhere, the contract and the agent definitions included | One spelling with no bare form, but the simulation puts four of five preloads above their baseline (+27 to +60 bytes), so rule 4 fails | rejected |
| A3. `## N title`; `contract rule N` outside, `rule N` inside the contract and `agents/` | Two spellings, read by one reader rule that the section-sign reader already had: bare counts in the contract and `agents/`. Every preload falls by 18 to 38 bytes in the simulation | **chosen** |
| A4. A3 with `## N. title`, the shape of `skills/implement/SKILL.md`'s steps | The framer's preload grows by 2 bytes in the simulation, so rule 4 fails on one agent | rejected |
| A5. Keep the section sign and refuse only its near misses | The premise that keeps it is that a reader reads it one way. The owner's rule in `skills/writing-style/SKILL.md` names it as a symbol a reader trips on, so the premise is false | rejected |
| A6. Each reader refuses the old spelling in its own corpus | Five readers keep a section-sign arm forever, and the forms no reader parses (a lettered part, a named part, the emblem) stay unguarded | rejected |
| A7. One case refuses the section sign in every living file, at its line | A living file that needs the character, such as a fixture for this case, builds it with `"\N{SECTION SIGN}"`. The four record paths are exempt by name, so a fifth kind of record added later is refused until it is named | **chosen** |
| A8. A reader-first phase, then a rewrite phase | A reader that reads only the new spelling is red at its own commit while the text still holds the old one, and the issue asks for the reader and its text in one commit | rejected |
| A9. One phase per kind of citation, each reader with its text, coordinates from `git grep` at the phase's HEAD | A phase is large (phase 1 holds most of the 391 occurrences before a number). The merges of #988 and #1009 change nothing in the plan, because no coordinate is pinned | **chosen** |
| A10. A rewrite script committed to the tree, or run through the shell | A substitution through the shell does nothing and exits zero when it misses (contract rule 9), and a committed script is a mechanism with nothing left to do after one run | rejected |
| A11. Replace the changelog marker with a visible line, rewriting the 54 release files | `CONTRIBUTING.md` *House rules* gives `changelog/` to the branch based on `main`. The release note and the index would show an id line that each entry's own trailer already carries | rejected, by default (`questions.md` Q1) |
| A12. Keep the marker and refuse its near misses | 27 lines in 11 release files open a comment naming `seal/specs/` in an older convention (executed), so the refusal would fail on released lines this branch may not edit | rejected |
| A13. Keep the marker as it is | `docs/branch-and-release.md` *Work accumulates on a release branch* states it: an HTML comment, invisible to a reader, the only link back. The premise that keeps it, that it is read one way, holds: `gather_changelog.py#MARKER_LINE_RE` reads one spelling on a live line (read) | **chosen**, by default (`questions.md` Q1) |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The contract's numbering. The 20 headings become `## N title`, rule 12's heading loses its dash, and the preamble names the citation spelling. Every contract citation in a living file becomes `contract rule N`, or `rule N` in the contract and `agents/`. The heading reader becomes one, imported by the five modules that copied it. The citation reader reads the new spelling across a line break (`spec.md` S1, S2). The label `session_cost.py` prints for a spawn, and the sentence in `skills/verify/orchestration.md` that describes it, change with their pin. The phase record holds each agent's preload bytes at base and head. | The test modules that read the contract (the six that read its headings, `tests/test_edits_go_through_the_edit_tool.py`, `tests/test_every_agent_reads_the_contract.py`, `tests/test_session_cost.py`), the new cases seen red; `noninferiority.py#preload_bytes` for the five agents at base and head (S5) | |
| 2 | Citations of another file's section. Every italic-heading citation drops the sign, and every step-number citation names its heading text. `CITED_NUMBER` goes, `CITED_TITLE` and `SECTION` lose their sign arms, and `tracker_labels.py`'s `specified_by` and its test change together. Each touched citation whose file exists names a heading of it, or the phase record lists what it became (S4, S6, S7). | The modules of the readers changed and of every message whose pin changed, the new cases seen red | |
| 3 | The old spelling refused. The case of `spec.md` scope item 6 is written and run at the phase's HEAD, where it lists the residue (seen red), then every listed line is rewritten. The writing rule states the shape once and its `check:` line names the two modules. The phase record holds the final preload bytes. | The new case at head (S3), `git diff --name-only <base>..HEAD` over the four record paths (S9), `noninferiority.py#preload_bytes` again (S5), the modules of every file the residue touched | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past
one, which someone can open.

The party that builds a phase fills its cell as the phase closes, not at the
end. A phase reconstructed afterwards is reconstructed from the diff, which is
where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. The party that builds the phase
writes it to `seal/specs/<work-item-id>/phases/phase-N.md`, from
`templates/sdd-phase.md`, when the phase closes.

Where feature branches squash, these commits stop resolving at the merge, and
**a rebase during the work does the same thing earlier and more quietly**,
because the orphaned object still answers `git cat-file` in the worktree that
wrote it. **The party that rebases the branch re-reads this column after the
rebase**, or the column names commits that resolve in one clone and nowhere
else. Nothing measures from this column, which is why that is tolerable.

## Operational impact

No migration, no new environment variable and no new dependency. Every
spawn's preload changes: the contract's headings and the agent definitions'
citations. A spawn prompt written before this release that cites a rule with
the section sign still names the same rule by the same number. A consuming
repository's own records keep their old citations, because records of a
moment are not rewritten. The hooks change only in comments and docstrings.
