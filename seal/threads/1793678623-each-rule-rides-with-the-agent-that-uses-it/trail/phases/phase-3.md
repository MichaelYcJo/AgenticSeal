# Phase 3: 1793678623-each-rule-rides-with-the-agent-that-uses-it

## What this phase found

**The frame's coordinates for this phase hold.** HEAD before the phase was
ba96818fc (`git log --oneline -1`, executed). Each sentence D3 and this
phase's `## Removes` rows name stood where they say, shifted only by the
lines phases 1 and 2 changed (read). These were the plugin-path sentence at
`agents/crafter.md:29-33`, `agents/framer.md:44-47`, `agents/proofer.md:27-30`,
`agents/sealer.md:43-45` and `agents/tracer.md:27-29`. The reference-root
sentences were at crafter step 2 and framer step 4. The parity sentences
were at proofer step 5 and sealer step 5. The reframe rule's first sentence
and the preamble's two sentences stood as quoted. Phase 2's record said the
contract had 17 sections, and it still does after this phase.

**Each removed copy's kept side is a file its reader opens at that step.**
Each was checked as follows, all read.

- **The plugin-path sentence.** Kept in contract rule 11. Every definition's
  `skills:` list preloads the contract, and
  `tests/text/test_every_agent_reads_the_contract.py#PRELOADS` holds that.
- **The crafter's reference-root sentence.** Kept in
  `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*,
  at `:77-80`. That paragraph says a reference root is read where the work
  touches what it describes, cited in `frame/design.md`, and never written.
  Crafter step 1 opens that file whole.
- **The framer's reference-root sentence.** Kept in the same paragraph. The
  framer does not reach it through step 3, which reads only three sections
  of implement: the language, *1.* and *3.*. It reaches it through *A design
  states its rule changes*, which reads the policy in force as *Document
  layout* states it (`agents/framer.md:187-188` before this phase). Step 4
  cites that rule by name. D3's *Opened at that step* cell says the same.
- **The parity record.** Kept in `skills/legacy-parity/SKILL.md` *Recording
  the comparison*, at `:102-121`. It holds the `original:` line, the
  `Baseline commit` it names, and the condition of a path outside `docs/` and
  `seal/`. It also holds the table of who writes the line under each routing
  answer, the proofer's `unread` finding and the sealer's `withheld` verdict.
  Proofer step 5 and sealer step 5 each open that skill in the same sentence.
- **The reframe sentence.** Kept in `agents/crafter.md` *The frame is judged
  before it is built to*. That rule says a *no* goes to the phase record and
  the hand-back, never back to the framer.
- **The preamble's first sentence.** Kept in every definition's opening
  sentence, pinned by `tests/text/test_every_agent_reads_the_contract.py#SENTENCE`.
- **The preamble's "A role's rules live in that role's definition".** Kept in
  `skills/core/SKILL.md` *Each agent judges its own target*: "An agent's own
  rules live in its definition or in the document it reads at that step".
  The core is preloaded first.

**Q2, rule 11's half: the sentence and its place.** `frame/questions.md` Q2
gives the wording to the work. Rule 11 now opens with its own paragraph:
"Every `skills/`, `templates/`, `docs/` and `agents/` path here and in your
definition is the plugin's, at the root two directories above the base
directory the harness printed with this file; the repository you work in may
hold other files at those paths." It is 256 bytes, and the crafter's copy
it replaces was 310 (`wc -c`, executed). "with the contract"
became "with this file", since the sentence now stands in the contract.
"Here" matches the `seal/` sentence after it, which says "here and in the
skills". The `seal/` paragraph is unchanged, so both pinned spellings stay in
the rule's body. Q2's Status cell is not this crafter's write. The
orchestrator closes it.

**The heading departs from D3's.** D3 gives *Where the plugin's paths and
the `seal/` root resolve, and the language its records are written in*. With
`## 11 ` that is 104 columns. `tests/behaviour/test_docs_line_wrap.py` reads
the contract's headings as prose, and it was red at 104 against its limit of
88 (executed). The heading is now *Where the plugin's paths and the `seal/`
root resolve, and the record language*, at 84 columns. "Record language" is
the `config.md` row the rule's body names. No file cites the heading by its
words (`git grep` for the old heading's words outside `seal/`, executed).
Judged against `frame/design.md` D3 and that test.

**The sealer's step 5 keeps its condition for comparing.** D3 says the step
keeps the act and cites the section for the record. The old step compared
only where the routing answers `straight to the PR` and the diff changes a
path outside `docs/` and `seal/`. That condition decides whether the sealer
compares at all, so it stays in the step. What went was the record: the
`original: <sha>` line, its `Baseline commit`, and the `withheld` verdict
for a comparison not made. The step now says to record the comparison as
*Recording the comparison* states. The proofer's step compared wherever
`seal/parity.md` is declared, and that is unchanged. Judged against
`frame/design.md` D3, the parity row.

**Two rewordings the removals forced.** The preamble's next sentence opened
"Its rules", and the sentence that named the file had gone. It now opens
"This file's rules". The framer's reframe rule read "You are when the
orchestrator routes", and the sentence before it had gone. It now reads "You
are spawned again when the orchestrator routes". Neither changes a fact.

**Two neighbours of the removed copies stay.**

- `skills/legacy-parity/SKILL.md` *Recording the comparison* cites
  `agents/sealer.md` for the `withheld` verdict. Sealer step 5 still spells
  `Verdict: withheld reason: <reason>`, so the citation still names where
  the verdict's form is. It is not a copy.
- The contract's frontmatter `description:` says one agent's rules "live in
  `agents/<name>.md`". The harness injects the contract without its
  frontmatter: this crafter's own preload begins at the `# agent-contract`
  heading (read). So no spawn pays for that line, and D3 does not name it.
  The description is what a session reads in the skill listing.

**The retargeted case.** `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`
listed the framer's and the crafter's definitions among the readers whose
paragraph points at `templates/setup/config.md` *Reference specs*. Both
paragraphs are gone, so both left `READERS`. Implement's paragraph was
already a reader there, and the comment above `READERS` now says the two
definitions are told through it. The case still asserts each definition's
never-write line under `## Never`, in a loop of its own. No case was
written new and no `seal mutate` run was taken. A removed copy adds no
behaviour (`skills/verify/SKILL.md` *The narrow command still has to be able
to fail*, the *Names or places only* row).

**Every removed copy is gone, by `git grep` at 6455bc17a, each executed and
each exit 1 with no lines.**

- `git grep -n "two directories above" -- agents/`. The same search over the
  tree outside `seal/` and `CHANGELOG.md` lists only contract rule 11.
- `git grep -n "Reference specs" -- agents/crafter.md agents/framer.md`.
- `git grep -n "original:\|Baseline commit\|raise an .unread" -- agents/proofer.md agents/sealer.md`.
- `git grep -n "you are not spawned again\|A builder that finds the" -- agents/framer.md`.
- `git grep -n "You received this file\|A role's rules live" -- skills/agent-contract/SKILL.md`.

The searches cover the copies' own words. A sentence stating the same fact
in other words is outside them, so that part of the class is a sample, left
to review. A `git grep` for "harness printed" and "base directory" outside
`seal/`, `tests/` and `CHANGELOG.md` found no other statement of the
plugin-path fact (executed).

**Bytes after the phase** (`wc -c` at 6455bc17a, executed).

| File | ba96818fc | 6455bc17a | Change |
|---|---|---|---|
| `skills/agent-contract/SKILL.md` | 11,569 | 11,680 | +111 |
| `agents/crafter.md` | 11,018 | 10,607 | -411 |
| `agents/framer.md` | 14,233 | 13,713 | -520 |
| `agents/proofer.md` | 10,164 | 9,717 | -447 |
| `agents/sealer.md` | 9,750 | 9,433 | -317 |
| `agents/tracer.md` | 2,956 | 2,847 | -109 |

So this phase changes each preload by its definition's change plus the
contract's 111. The crafter's falls by 300 bytes, the framer's by 409, the
proofer's by 336 and the sealer's by 206. The tracer's rises by 2. The
tracer held a shorter clause than the others, and the plan foresaw about
+130 for it. Over the three phases its preload still falls, since phases 1 and 2
took 441 and 896 bytes from the contract. Phase 4 measures every preload
with `release_report.py`.

**The phase-boundary set passed.** The set was 97 modules, listed by
command (executed). It holds the plan row's four modules. It holds every
test module that names `agents`, `agent-contract` or one of the five agents.
It holds every module that lists or walks the tree (`ls-files`, `os.walk`,
`glob(`, `rglob` or `censuses`). It also holds every module that names the
changed test module. The command was `bin/test <the 97 modules> -q`, and it
exited 0: 4479 passed, 11 skipped (executed). It ran at 6455bc17a, before
this record. `ruff check` and `ruff format --check` on the changed test
module exited 0 (executed).

**What phase 4 needs.**

- The contract has 17 sections. Rule 11's heading changed, and no file cites
  it by its words.
- The tracer's preload rose 2 bytes in this phase, so phase 4's table should
  show the tracer against its v0.30.0 row, not against phase 2.
- D6's census names each D3 copy as gone from its pair. This phase removed
  the plugin-path sentence from the five definitions, the reference-root
  sentence from the crafter's and the framer's, the parity sentences from
  the proofer's and the sealer's, the framer's reframe sentence, and the
  preamble's two sentences. Which ten-word pairs those were is the census's
  to say. The pinned opening sentence and write bound stay shared.
