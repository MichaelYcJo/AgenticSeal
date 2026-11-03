# Phase 1: 1793661729-each-document-is-cut-by-who-opens-it

## What this phase found

**The frame holds, with three corrections below.** It was read against the
tree at 52939d4f5 before the first edit: `skills/implement/SKILL.md:73` holds
the clause D9 replaces, `docs/the-review-record.md` *The run* holds the
sentences D6 names, and `hooks/question-gate.py`'s docstring holds every
fact of them but one (read).

**The version moved first, at the orchestrator's direction.** 8a68b6c05
moves `.claude-plugin/plugin.json` from `0.29.0` to `0.30.0`. The frame's
*Scope* put that move with the orchestrator, in the commit that adds the
changelog fragment. The spawn prompt moved it here: this is the first work
item pull request into `release/v0.30.0`, and `docs/branch-and-release.md`
has the branch's first pull request move `plugin.json` to the version named
at the cut. The row in `frame/plan.md` *Judgments of the run* is the
orchestrator's to write.

**D9 is written, and S11 holds.** 4d5e2049b replaces the clause in the
`docs/` row of `skills/implement/SKILL.md` *Document layout — two roots,
three lifetimes* with D9's text, word for word. The row's sentence that a
design states its changes in `## Rule changes` became D9's sentence for a
work item whose subject is the code, so the row states it once. S11's
command, at 4d5e2049b and again at 4c4925bff (executed):

```
git grep -n "does not edit it" -- ':!seal/'
```

It printed nothing and exited 1.

**Two places stood on the old clause, and the frame named neither.** Contract
rule 19 asks that they change in the same commit. A `git grep` for the
clause's words, and for statements that the policy root is written by the
settle alone, found these two (executed). That is a sample under contract
rule 12, since a restatement in other words is not matched.

- `agents/framer.md` *A design states its rule changes* told the framer that
  every rule a work item changes goes into `## Rule changes`. It now says the
  framer reads, from *Document layout*, which work item edits the policy root
  directly, and that a work item that does not states its rules there. The
  pinned citation in `tests/behaviour/test_waiver_decided_at_start.py#test_the_framer_writes_rule_changes_from_the_index`
  is unchanged. This adds 90 bytes to the framer's definition (`git diff`
  of the file, added minus removed line lengths, executed), which phase 6's
  S2 counts in its preload.
- `tests/text/test_the_handoff_before_round_one.py#test_the_bars_section_cites_the_run_level_tables_owner`
  carried a comment that `docs/` is not edited by a pull request, and on it
  accepted a second path, `skills/verify/SKILL.md`, until a settle applied
  #940's change. The settle #1310 applied it, and the section names
  `skills/verify/orchestration.md` alone (read). The comment went, and the
  case now asks for that one path. Seen red at 4d5e2049b (executed); the
  old case accepted that path, so it would have stayed green:

  ```
  seal mutate docs/the-review-record.md --replace "\`skills/verify/orchestration.md\` *Measure the segment" "\`skills/verify/SKILL.md\` *Measure the segment" --tests "bin/test -q -p no:xdist tests/text/test_the_handoff_before_round_one.py -k test_the_bars_section_cites_the_run_level_tables_owner"
  ```

  It printed `red: the cases failed against the mutation (exit 1)` and
  exited 0.

`docs/README.md`'s intro still says a design that finds a document wrong
states the correction in `## Rule changes`. That stays true for a work item
whose subject is the code, and D9 has phase 5 rewrite the intro to cite
*Document layout*, so phase 1 left it.

**D6's copies, at 4c4925bff.** Each pair was judged by reading both sides
against the census below.

- *The run* and `hooks/question-gate.py`: done as D6 states. The document's
  sentences from "The routing question put alone, single-select and with its
  text" through "and a row edited to `no` is in the diff the review reads."
  became D6's one sentence. The docstring gained the one fact: a row edited
  to `no` is in the diff the review reads. The docstring also lost its
  paragraph on a gate whose own reason says to ask with the question tool.
  That paragraph tells the session what to do, takes none of the question's
  ways and hands the stop back, which is the rule the document keeps.
  The document's last two sentences stay as D6 leaves them.
- *The stamp*: `skills/verify/scripts/seal_stamp.py`'s comment over the
  queueing code and `#queue_for_written_guarantee`'s docstring lost the rule
  and its grounds, and cite the section. They keep the code's own facts: the
  values file's name, `sealed_before`, `refused_here`, and the conditions the
  function checks. `hooks/sealer-stamp.py`'s docstring lost the sentence on
  what the stamp means, and cites the section. `MESSAGE_LIMIT`'s comment
  stays: it is the measurement the section names the constant for.
  `skills/code-review/orchestration.md` lost the same grounds sentence; the
  clause `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py`
  pins is unchanged.
- *The guarantee*: `skills/code-review/orchestration.md` lost the seal
  mark's conditions and the fold's description, and cites the section.
  `agents/sealer.md` *The guarantee covers HEAD, and a re-run audits what came
  after* lost the form's facts: that the check refuses the file, which block
  the check and the stamp read, and that a line that does not parse is
  refused. It keeps the clause
  `tests/behaviour/test_the_sealer_guarantees.py#TestDefinition::test_the_guarantee_rule_exempts_only_the_closing_records`
  pins, since the sealer acts on it. Its `check:` line dropped
  `tests/skills/test_chain_check.py`, which held the refusal the paragraph
  no longer states.
- **A departure from D6's second row.** D6 keeps every *The guarantee* pair
  on the document's side. The opening of the section restated the sealer's
  job from `agents/sealer.md` *Job*: what it verifies, independently of whom,
  and its reference. The frame's *Scope* keeps an agent's own rules in its
  definition, and the sealer acts on that sentence at every step, so the
  definition keeps it and the document's opening now cites
  `agents/sealer.md` *Job*. Judged against `frame/design.md` *Scope* (Out,
  first item) and `skills/core/SKILL.md` *The rule a mechanism is kept
  against*.
- **D6's fourth row does not hold as written.** It has
  `skills/code-review/scripts/chain_check.py`'s docstring and comments link
  to *What the check reads at the pull request*. The docstring already
  linked to the document. Its eight shared runs, 122 words, are phrases
  inside text about the code: the arm list, a function's contract
  (`#records`), refusal messages a person reads, and one comment. None is a
  restated passage. The arm list also holds facts that section does not
  state: the frame arm's mark and `Reframed` lines, the closing records, the
  trailer's `no work item`, the four-word pin and the heading near
  `## Rule changes` (`grep -c` over the section, executed: 0 each). Cutting
  the arm list to a link would leave those facts with no home, so the
  docstring stays. Its link now names the sections it cites, which phase 5
  re-points.
- D2's third item has `agents/sealer.md` lose what it shares with *The
  guarantee*, in phase 6. The removal above is that act, taken here under
  D6. Phase 6 keeps the citation swap: step 1 cites *What the check reads
  at the pull request* beside `chain_check.py#follows`.

**The census, re-run.** The script was written for this phase and deleted
after it; this is its whole text, so the command can be run again.

```python
import re, subprocess, sys
from collections import defaultdict

WORD = re.compile(r"[a-z0-9]+(?:['-][a-z0-9]+)*")

def words(text):
    return WORD.findall(text.lower())

repo, doc, n = sys.argv[1], sys.argv[2], 10
files = subprocess.run(["git", "-C", repo, "ls-files", "*.md", "*.py"],
                       capture_output=True, text=True, check=True).stdout.split()
files = [f for f in files if not f.startswith(("seal/", "evals/")) and f != doc]
tagged, section = [], "(title)"
for line in open(f"{repo}/{doc}", encoding="utf-8"):
    if line.startswith(("## ", "### ")):
        section = line.strip("# \n")
    tagged += [(w, section) for w in words(line)]
doc_words = [w for w, _ in tagged]
shingles = defaultdict(list)
for i in range(len(doc_words) - n + 1):
    shingles[tuple(doc_words[i:i + n])].append(i)
covered_any, pairs = set(), defaultdict(lambda: [0, set()])
for f in files:
    try:
        other = words(open(f"{repo}/{f}", encoding="utf-8").read())
    except (OSError, UnicodeDecodeError):
        continue
    covered = set()
    for j in range(len(other) - n + 1):
        for i in shingles.get(tuple(other[j:j + n]), ()):
            covered.update(range(i, i + n))
    covered_any |= covered
    prev = None
    for pos in sorted(covered):
        if prev is None or pos != prev + 1 or tagged[pos][1] != tagged[prev][1]:
            pairs[(tagged[pos][1], f)][0] += 1
        pairs[(tagged[pos][1], f)][1].add(pos)
        prev = pos
print(f"{doc}: {len(covered_any)} of {len(doc_words)} words share a run of {n}+ words")
for (sec, f), (runs, cov) in sorted(pairs.items(), key=lambda kv: -len(kv[1][1])):
    print(f"{len(cov):5d} words {runs:3d} runs  {sec}  <->  {f}")
```

Run as `python3 census.py <repository root> docs/the-review-record.md`. It
counts runs of ten or more words the document shares with tracked `.md` and
`.py` files outside `seal/` and `evals/`, by section and file. Its tokenizer
is a third one, beside the framer's and the orchestrator's. The list is a
floor, since a restatement in other words is not counted (contract rule 12).

At 52939d4f5 (executed) it printed `1312 of 8972 words`. D6's pairs stood
at: *The stamp* with `seal_stamp.py` 150 words in 10 runs; *The run* with
`hooks/question-gate.py` 130 in 5; *What the check reads at the pull
request* with `chain_check.py` 122 in 8; *The guarantee* with
`agents/sealer.md` 71 in 6 and with `skills/code-review/orchestration.md`
55 in 4; *The stamp* with `hooks/sealer-stamp.py` 34 in 3 and with
`skills/code-review/orchestration.md` 24 in 2.

On the tree 4c4925bff commits (executed), the whole list:

```
docs/the-review-record.md: 1055 of 8805 words share a run of 10+ words
  122 words   8 runs  What the check reads at the pull request  <->  skills/code-review/scripts/chain_check.py
   88 words   4 runs  The stamp  <->  tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py
   71 words   6 runs  The run  <->  skills/code-review/orchestration.md
   56 words   4 runs  The stamp  <->  skills/verify/scripts/seal_stamp.py
   52 words   5 runs  The guarantee  <->  templates/setup/config.md
   51 words   4 runs  The round record  <->  skills/code-review/SKILL.md
   46 words   4 runs  What the check reads at the pull request  <->  tests/skills/test_chain_check.py
   39 words   3 runs  The run  <->  agents/proofer.md
   37 words   3 runs  The guarantee  <->  skills/code-review/scripts/pr_body.py
   36 words   3 runs  The guarantee  <->  agents/sealer.md
   35 words   3 runs  What the check reads at the pull request  <->  docs/the-review-and-parity-arms.md
   34 words   2 runs  What the check reads at the pull request  <->  tests/text/test_review_axes.py
   33 words   3 runs  What the check reads at the pull request  <->  skills/verify/scripts/unverified_check.py
   32 words   3 runs  The run  <->  skills/implement/acts.md
   28 words   2 runs  The run  <->  tests/text/test_the_rules_have_one_owner.py
   27 words   2 runs  The guarantee  <->  skills/code-review/scripts/chain_check.py
   24 words   2 runs  What the check reads at the pull request  <->  skills/settle/SKILL.md
   23 words   2 runs  The run  <->  README.md
   23 words   2 runs  The stamp  <->  skills/code-review/orchestration.md
   22 words   2 runs  What the check reads at the pull request  <->  docs/the-record-layout.md
   22 words   2 runs  The stamp  <->  hooks/sealer-stamp.py
   22 words   2 runs  The per-segment bars  <->  skills/verify/scripts/session_cost.py
   22 words   2 runs  The guarantee  <->  tests/behaviour/test_the_sealer_guarantees.py
   22 words   2 runs  The per-segment bars  <->  tests/skills/test_session_cost.py
   21 words   2 runs  The guarantee  <->  skills/code-review/orchestration.md
   21 words   2 runs  The guarantee  <->  skills/implement/acts.md
   20 words   2 runs  The handoff  <->  agents/crafter.md
   20 words   2 runs  The handoff  <->  agents/framer.md
   20 words   2 runs  The round record  <->  skills/code-review/orchestration.md
   20 words   2 runs  The guarantee  <->  skills/commit-pr-convention/SKILL.md
   19 words   1 runs  The round record  <->  docs/the-pact.md
   19 words   1 runs  The round record  <->  docs/what-a-script-gates.md
   18 words   1 runs  The round record  <->  skills/code-review/scripts/chain_check.py
   18 words   1 runs  The round record  <->  skills/writing-style/SKILL.md
   17 words   1 runs  The run  <->  docs/release-checklist.md
   17 words   1 runs  The run  <->  skills/implement/orchestration.md
   17 words   1 runs  The run  <->  skills/settle/SKILL.md
   14 words   1 runs  The round record  <->  skills/core/SKILL.md
   14 words   1 runs  The run  <->  skills/implement/SKILL.md
   14 words   1 runs  What the check reads at the pull request  <->  skills/legacy-parity/SKILL.md
   13 words   1 runs  The round record  <->  agents/proofer.md
   13 words   1 runs  The stamp  <->  assets/seals/README.md
   13 words   1 runs  The run  <->  skills/core/SKILL.md
   13 words   1 runs  The round record  <->  templates/records/sdd-round.md
   13 words   1 runs  The stamp  <->  tests/hooks/test_sealer_stamp.py
   13 words   1 runs  The stamp  <->  tests/hooks/test_sealer_stamp_queue.py
   13 words   1 runs  The round record  <->  tests/skills/test_chain_check.py
   12 words   1 runs  What the check reads at the pull request  <->  docs/release-checklist.md
   12 words   1 runs  The run  <->  docs/the-record-layout.md
   12 words   1 runs  What the check reads at the pull request  <->  hooks/lib/config.py
   12 words   1 runs  What the check reads at the pull request  <->  hooks/lib/fields.py
   12 words   1 runs  The run  <->  hooks/question-gate.py
   12 words   1 runs  The per-segment bars  <->  skills/commit-pr-convention/SKILL.md
   12 words   1 runs  The per-segment bars  <->  skills/implement/acts.md
   12 words   1 runs  The per-segment bars  <->  skills/implement/orchestration.md
   12 words   1 runs  What the check reads at the pull request  <->  skills/settle/scripts/passages.py
   12 words   1 runs  What the check reads at the pull request  <->  skills/verify/scripts/coordinates.py
   12 words   1 runs  What the check reads at the pull request  <->  tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py
   12 words   1 runs  What the check reads at the pull request  <->  tests/behaviour/test_waiver_decided_at_start.py
   12 words   1 runs  What the check reads at the pull request  <->  tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py
   12 words   1 runs  What the check reads at the pull request  <->  tests/github/test_rules.py
   12 words   1 runs  What the check reads at the pull request  <->  tests/hooks/test_fields.py
   12 words   1 runs  What the check reads at the pull request  <->  tests/skills/test_passages.py
   12 words   1 runs  The round record  <->  tests/text/test_review_axes.py
   11 words   1 runs  What the check reads at the pull request  <->  .github/scripts/rules.py
   11 words   1 runs  The stamp  <->  README.md
   11 words   1 runs  The run  <->  docs/the-agent-set.md
   11 words   1 runs  What the check reads at the pull request  <->  skills/core/SKILL.md
   11 words   1 runs  The round record  <->  tests/text/test_a_rider_reaches_its_file.py
   10 words   1 runs  The guarantee  <->  README.md
   10 words   1 runs  The round record  <->  agents/crafter.md
   10 words   1 runs  The per-segment bars  <->  agents/crafter.md
   10 words   1 runs  The round record  <->  agents/framer.md
   10 words   1 runs  The run  <->  agents/framer.md
   10 words   1 runs  The per-segment bars  <->  agents/framer.md
   10 words   1 runs  The round record  <->  agents/tracer.md
   10 words   1 runs  The round record  <->  docs/branch-and-release.md
   10 words   1 runs  What the check reads at the pull request  <->  docs/what-a-script-gates.md
   10 words   1 runs  The round record  <->  skills/agent-contract/SKILL.md
   10 words   1 runs  The handoff  <->  skills/agent-contract/SKILL.md
   10 words   1 runs  The round record  <->  skills/implement/SKILL.md
   10 words   1 runs  The round record  <->  skills/legacy-parity/SKILL.md
   10 words   1 runs  The round record  <->  skills/settle/scripts/passages.py
   10 words   1 runs  What the check reads at the pull request  <->  skills/verify/scripts/broad_gate.py
   10 words   1 runs  The round record  <->  tests/behaviour/test_a_commit_names_its_repository.py
   10 words   1 runs  The round record  <->  tests/behaviour/test_the_pull_request_language_is_the_repositorys.py
   10 words   1 runs  The round record  <->  tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py
   10 words   1 runs  What the check reads at the pull request  <->  tests/skills/test_broad_gate.py
   10 words   1 runs  The round record  <->  tests/skills/test_passages.py
   10 words   1 runs  What the check reads at the pull request  <->  tests/skills/test_unverified_check.py
   10 words   1 runs  The round record  <->  tests/text/test_broad_gate_rule.py
   10 words   1 runs  The round record  <->  tests/text/test_edits_go_through_the_edit_tool.py
   10 words   1 runs  The round record  <->  tests/text/test_no_passage_is_pasted_into_a_second_file.py
   10 words   1 runs  The round record  <->  tests/text/test_the_rules_have_one_owner.py
```

**What stays on the list, and why.** Every pair of 30 words or more was
read with its runs printed. A pair under 30 words is one or two runs, and
each of those read was a cited path, a check line, a section title or one
clause; that is a sample, not every one.

- A file under `tests/` shares a run because the case pins the sentence;
  the pin is what holds the text, and stays.
- `seal_stamp.py`, `pr_body.py`, `chain_check.py` and
  `unverified_check.py` share a function's contract, a message a person
  reads, or a coordinate such as `skills/code-review/scripts/pr_body.py#HEADING`.
- `agents/sealer.md` keeps the pinned closing-records clause and two
  citations of `pr_body.py#HEADING`. `templates/setup/config.md`,
  `skills/code-review/SKILL.md` and `skills/implement/acts.md` share
  coordinates, check lines and short clauses.
- Two pairs are whole passages, outside D6, and `gaps.md` *Not done* names
  them. *The run*'s regression paragraph and the table in
  `skills/code-review/orchestration.md` *A regression is routed by comparing
  the fix with the frame* state the same three routes, 71 words. Both are the
  orchestrator's, and the design chose no side. `agents/proofer.md` *A
  verifying round answers the closed findings* states the regression line's
  rule as *The run* does, 39 words; the frame's *Scope* keeps an agent's own
  rules in its definition.
- `docs/the-review-and-parity-arms.md` shares 35 words with *What the check
  reads at the pull request*. Both are policy documents, and phase 5 moves
  both.

**The frame's own record trips a census.** `frame/design.md:39` names the
transcript directory with a real user path, and
`tests/test_censuses.py::Test_module::test_every_file_no_module_file_declares_meets_every_census`
fails on it (executed, at 4c4925bff). Phase 1 did not touch that file, and
the crafter does not write the frame: `git diff 52939d4f5 --
seal/threads/1793661729-each-document-is-cut-by-who-opens-it/frame/design.md`
prints nothing (executed), so the line stands as the framer committed it.

**Narrow runs (executed).** The modules that read a changed path, name it,
import it or walk a directory holding one: 103 modules, listed by a
`git grep -l` over `tests/` for each changed file's name and for directory
walks. At 4c4925bff before this record, 5093 passed, 12 skipped and 2
failed: the census above, and
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which this record's `gaps.md` answers. The phase-boundary run, the same
103 modules in one `bin/test -q` command with this record, `gaps.md` and
the Status cell written: 5094 passed, 12 skipped, and 1 failed, the census
on `frame/design.md:39`.

**Mutation.** The phase adds one behaviour: the narrowed case above, run
under `seal mutate`. D9's sentence is held by S11's `git grep` and by the
proofer's reading. The rest of the phase removes copies, adds one fact to a
docstring and one clause to the framer's definition; no script's behaviour
changed.
