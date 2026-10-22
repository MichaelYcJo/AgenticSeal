# Implementation Plan: #1005 the section sign is still syntax

Approved <date> by <who>, when `smith` was spawned.

## Summary

The section sign leaves every living file in three phases, one per kind of
citation, and each phase changes a reader in the same commit as the text it
reads. Phase 1 renumbers nothing: it rewrites the contract's headings and
every contract citation to a plain number. Phase 2 rewrites every citation of
another file's section to its heading text. Phase 3 adds the one case that
refuses the old spelling, rewrites what is left, and states the shape in the
writing rule.

The owner's widening of 2026-10-22 adds two phases. Phase 4 takes every
comment and every guidance sentence out of the record templates and lands
each sentence once, in what its writer reads. Phase 5 makes the fence rule
and the line split one copy. `spec.md` holds the spellings, the readers, the
homes and the counts.

## Technical context

**The build starts after #988 and #1009 merge into `release/v0.22.3`.**
#988's branch at 77eef010 changes 27 files and #1009's at 001098c2 changes
23 (executed: `git diff --name-only eae7f0ad origin/<branch>`). Outside
`seal/specs/`, 14 and 7 of them carry a section sign at the branch's tip,
and the two diffs add 5 and 1 lines that carry one, records included
(executed). #988 also changes `rule_changes.py`, `unverified_check.py` and
`chain_check.py`, the readers phase 5 touches (relayed by the
orchestrator, not opened). So no phase pins a coordinate. Each phase starts
with `git grep` at its own HEAD (for the section sign in phases 1 to 3, for
`<!--` and the template paths in phase 4, for the fence functions in phase
5), and the list that command prints is the phase's work.

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
Templates are not preloaded. Phase 4 adds to an agent definition only a
guidance sentence with no other home, and measures the five preloads again.

**The record readers' states at a16acb40 (read).**
`unverified_check.py#readable` is `blank_fences(strip_comments(gfm_lines(text)))`,
and `strip_comments` walks `comment_scan`, which tracks a comment and a code
span. Its callers read records only: `chain_check.py` (round records, the
frame's foot, the routing table rows), `unverified_check.py#check_text`
(`overview.md`), `seal_stamp.py`, `noninferiority.py` and
`replay_targets.py`. `chain_check.py#unclosed` reports an unclosed comment
and an unclosed fence. `live_lines`, through `_liveness`, tracks a fence, a
comment and a code span under two span readings, and its callers read
release files, the policy root's index and policy documents as well as a
spec's `## Rule changes`. `hooks/blocks.py#walk` tracks fence blocks and
comment blocks by the block rule, for `hooks/config.py` and
`hooks/routing.py`.

**Failure scenario of the chosen approach.** In six months an agent
definition says "rule 4" meaning a rule of something else, such as the
behaviour suite's pass rules. The citation reader takes it for the
contract's rule 4 and passes it, because only a number above the contract's
last rule is refused. The reader's corpus and its bare-number homes are the
same as the section-sign reader's today, so the risk is not new; it moves
from one character to one word. For the templates: a guidance sentence a
writer needed is removed as "already stated" when its home states only part
of it. Phase 4's record lists every sentence and where it stands, so the
warden can read each one against its home.

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
| A9. One phase per kind of change, each reader with its text, coordinates from `git grep` at the phase's HEAD | A phase is large (phase 1 holds most of the 391 occurrences before a number). The merges of #988 and #1009 change nothing in the plan, because no coordinate is pinned | **chosen** |
| A10. A rewrite script committed to the tree, or run through the shell | A substitution through the shell does nothing and exits zero when it misses (contract rule 9), and a committed script is a mechanism with nothing left to do after one run | rejected |
| A11. Replace the changelog marker with a visible line, rewriting the 54 release files | `CONTRIBUTING.md` *House rules* gives `changelog/` to the branch based on `main`. The release note and the index would show an id line that each entry's own trailer already carries | rejected, by default (`questions.md` Q1) |
| A12. Keep the marker and refuse its near misses | 27 lines in 11 release files open a comment naming `seal/specs/` in an older convention (executed), so the refusal would fail on released lines this branch may not edit | rejected |
| A13. Keep the marker as it is | It is the needed case of the owner's direction: it must not render in the release note, and it is the only link back. The premise that keeps it, that it is read one way, holds: `gather_changelog.py#MARKER_LINE_RE` reads one spelling on a live line (read) | **chosen**, by default (`questions.md` Q1) |
| B1. Readers drop the fence state and rely on labelled lines never standing in a fence | No committed round record holds one (executed, 150 records), but #986's evaluation reports did, and a paste-ready fix to a record's own grammar can hold one: it would be read as the record's line | rejected |
| B2. Keep the fence state, as one copy in `hooks/blocks.py` that `unverified_check.py` imports | The premise that kept two copies is that a hook imports nothing from `skills/`. It holds, and the import goes the other way: the skill module already loads `hooks/config.py` by path (read). A hook-side change to the rule now changes the skill readers in the same commit, which is the point | **chosen** |
| B3. Keep both fence copies, held in step by the two tests | Two copies and two tests to keep one rule, the shape `CLAUDE.md` *The rule a mechanism is kept against* refuses | rejected |
| B4. Template guidance moves to the agent definitions | Every sentence moved there is paid on every spawn, and rule 4 is measured on exactly those bytes | rejected, except for a sentence with no other home |
| B5. Template guidance moves to the skill or orchestration file its writer opens, or goes where its owner already states it | A writer that does not open the skill misses the sentence. The framer opens `skills/implement/SKILL.md` *3. The SDD file set* at its step 3, and the orchestrator opens `skills/implement/orchestration.md` to route the work | **chosen** |
| B6. A template keeps a one-line comment pointing at its home | Still a comment in every record, and `skills/implement/SKILL.md` *3. The SDD file set* already maps each template to its writer | rejected |
| B7. The record readers lose the comment and code-span states in this item, with the old records stripped | The backlog settle reads a released spec at `origin/main`, where #941's no-change blocks arrive only when 0.22.3 merges, so the strip would rewrite records that settle is due to remove (relayed by the orchestrator from a dry run, not opened) | rejected by the owner, 2026-10-22 (`questions.md` Q6) |
| B8. The record readers keep the comment states until the backlog settle after 0.22.3 merges, and #1012 removes them right after it | Every reader keeps the states that caused #1000 and #988's round 2 for one more release | **chosen** by the owner, 2026-10-22 (`questions.md` Q6) |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The contract's numbering. The 20 headings become `## N title`, rule 12's heading loses its dash, and the preamble names the citation spelling. Every contract citation in a living file becomes `contract rule N`, or `rule N` in the contract and `agents/`. The heading reader becomes one, imported by the five modules that copied it. The citation reader reads the new spelling across a line break (`spec.md` S1, S2). The label `session_cost.py` prints for a spawn, and the sentence in `skills/verify/orchestration.md` that describes it, change with their pin. The phase record holds each agent's preload bytes at base and head. | The test modules that read the contract (the six that read its headings, `tests/test_edits_go_through_the_edit_tool.py`, `tests/test_every_agent_reads_the_contract.py`, `tests/test_session_cost.py`), the new cases seen red; `noninferiority.py#preload_bytes` for the five agents at base and head (S5) | |
| 2 | Citations of another file's section. Every italic-heading citation drops the sign, and every step-number citation names its heading text. `CITED_NUMBER` goes, `CITED_TITLE` and `SECTION` lose their sign arms, and `tracker_labels.py`'s `specified_by` and its test change together. Each touched citation whose file exists names a heading of it, or the phase record lists what it became (S4, S6, S7). | The modules of the readers changed and of every message whose pin changed, the new cases seen red | |
| 3 | The old spelling refused. The case of `spec.md` scope item 6 is written and run at the phase's HEAD, where it lists the residue (seen red), then every listed line is rewritten. The writing rule states the shape once and its `check:` line names the two modules. The phase record holds the preload bytes. | The new case at head (S3), `git diff --name-only <base>..HEAD` over the four record paths (S9), `noninferiority.py#preload_bytes` again (S5), the modules of every file the residue touched | |
| 4 | The record templates. Every comment and every guidance sentence leaves the eight `templates/sdd-*.md`; each sentence is removed where its owner already states it, or moved to the home `spec.md` names. Each case that pinned a template sentence pins it at its home. `tests/test_a_record_carries_no_comment.py` refuses a comment in a record template (S10). The phase record lists every sentence and where it now stands (S11), and the five preloads. | The new case seen red with one comment put back; the 17 modules that read `templates/sdd-*` at the phase's HEAD; `noninferiority.py#preload_bytes` (S5) | |
| 5 | One fence rule. `unverified_check.py` imports `fence_opener`, `fence_closes`, `GFM_LINE_RE` and `gfm_lines` from `hooks/blocks.py`, and its own copies and the two in-step cases go (S12). A labelled line in a closed fence is still not read, and an unclosed fence is still refused at its line. | `tests/test_chain_check.py`, `tests/test_unverified_rows_close.py`, `tests/test_the_hooks_hide_what_a_renderer_hides.py`, and the modules of every caller of the four names | |

## Out of scope

- Stripping the old records' comments and removing the record readers'
  comment and code-span states are #1012's, milestone 0.22.4, which runs
  right after the backlog settle that follows 0.22.3's merge to `main`
  (`questions.md` Q6; `spec.md` scope item 14).

## Operational impact

No migration, no new environment variable and no new dependency. Every
spawn's preload changes: the contract's headings and the agent definitions'
citations. A spawn prompt written before this release that cites a rule with
the section sign still names the same rule by the same number. A consuming
repository's own records keep their old citations and their comments, and
in this release the readers still read them. A new work item there,
framed after the upgrade, gets templates with no comment. The hooks change
in comments and docstrings, and `hooks/blocks.py` becomes the one fence
rule both the hooks and the skill readers ask. Once #1012 removes the
readers' comment state, a consuming repository's in-flight work item
framed under the old templates is refused at its first check after that
upgrade, until its records are stripped, and the release note that ships
#1012 has to say so.
