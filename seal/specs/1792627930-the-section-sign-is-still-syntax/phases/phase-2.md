# Phase 2: 1792627930-the-section-sign-is-still-syntax

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 0c8e94cf |

## What this phase was asked

Citations of another file's section. Every italic-heading citation drops the
sign, and every step-number citation names its heading text. `CITED_NUMBER`
goes, `CITED_TITLE` and `SECTION` lose their sign arms, and
`tracker_labels.py`'s `specified_by` and its test change together. Each
touched citation whose file exists names a heading of it, or the record lists
what it became (`spec.md` S4, S6, S7). The record recomputes its coordinates
at HEAD before the first edit.

Coordinates at HEAD 799e0664, before the first edit (executed):
`git grep -n -I -P '\x{00A7}\*' -- . ':!seal/specs/' ':!changelog/' ':!CHANGELOG.md' ':!evals/behaviour/'`
printed 268 lines in 100 files, and the numbered form of phase 1's command
printed the 20 lines phase 1's record lists, of which 18 cite a step of
`docs/release-checklist.md` or `skills/implement/SKILL.md`.

## What this phase found

**The rewrite.** Every `§*` became `*`, one `Edit` with `replace_all` per
file after the file's lines were read, and every step number became the
step's heading: `docs/release-checklist.md` steps 2 to 6 and
`skills/implement/SKILL.md` steps 1 and 3. 391 lines carried the sign before
the phase and 90 after (executed); phase 3 takes the 90.

**Citations that named no heading, Q4 (read, then executed by a scratch
probe that matched every path-and-italic citation on an added line against
the cited file's headings; the probe was deleted).**

| Where | Cited | Now |
|---|---|---|
| `agents/sealer.md` | `docs/the-review-record.md` *The broad run has one home* | *What the check reads at the pull request*, the section whose bold lead it is |
| `.github/scripts/tracker_labels.py` | `docs/issues-and-milestones.md` *A label answers what it is about, and survives the move* | unchanged words: the heading is `A label answers *what it is about*, and survives the move`, and a citation names it as it renders, its own emphasis dropped; the case reads headings the same way |
| `seal/follow-up.md` | `skills/code-review/orchestration.md` *A fix pass adds the unit that pins it, and that unit ships unreviewed* | no heading holds the depth rule now (`git grep` found none), so the row says in words what the rule was and that no heading holds it |
| `skills/verify/scripts/session_cost.py`, twice | `skills/verify/orchestration.md` *Measure the segment* | *Measure the segment, and feed the flow log* |
| `skills/verify/scripts/session_cost.py` | `CONTRIBUTING.md` *Hooks stay local and quiet* | *House rules*, with the bullet's bold lead named after it |
| `tests/test_the_release_seal_is_drawn.py` | `docs/branch-and-release.md` *Every act the release performs once it reaches `main`* | *Cutting a release*, with the paragraph's bold lead named after it |

**A reader without the sign arm reads more.** With `\s+§` gone, the
implement reader read a Python string split across two lines in
`tests/test_first_setup_asks_once.py` as a citation, and then the f-string
that replaced it. The assertion now builds its citation from the heading it
already holds. The S4 fixture is built the same way, so its own file cites
no missing heading.

**The `skill's` arm of `CITED_TITLE` stays.** It is not a section-sign arm,
and contract rule 11 cites `implement` that way.

**Printed text pinned (contract rule 14), each pin seen red against the old
text (executed) before the text changed:** the tracker label's
`specified_by`, the absent-row refusal of `broad_gate.py` (*The Seal Test*
and *The criterion for choosing a value*), the refusal for a row no walk
reads in its three shapes (*What is refused, and what stays allowed*), the
refusal of a row not as written (*Broad gate*), and `settle.py`'s readers
heading.

**Mutation-check, each killed (exit 0, executed):** `CITED_TITLE` given back
its sign arm, the dangling test in `dangling_implement_citations`, the cited
heading in `tracker_labels.py`, `SECTION_TOKEN` keeping the citation's
words, `settle.py`'s heading without italics, and each of the three
`broad_gate.py` messages without italics.

**The two link constants collapse.** `tests/test_the_rules_have_one_owner.py`
and `tests/test_a_reference_root_is_read_and_never_taken.py` held a cited
form with the sign and a second form with it stripped, for files not yet
rewritten. One form is left, and the `*_LINK` names are gone.

**Preload bytes after phase 2 (executed):** framer 25194 (-61 against the
base), smith 24668 (-78), warden 25300 (-70), sealer 23302 (-81), scribe
18486 (-59).
