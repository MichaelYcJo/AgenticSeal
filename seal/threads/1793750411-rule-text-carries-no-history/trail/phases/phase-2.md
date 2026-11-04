# Phase 2: 1793750411-rule-text-carries-no-history

## What this phase found

**The frame holds for this phase's files.** The two `## Removes` rows on
`skills/` outside phase 1's files open the sentences they name at
3bd60d29f: `skills/code-review/SKILL.md:198-200` and
`skills/implement/SKILL.md:291-293` (read). Phase 1 changed none of this
phase's files (`git diff --stat 3bd60d29f 8b30ef79b` over them prints
nothing, executed), so each base line below is also the line at 8b30ef79b.
The phase's files are the 21 that `git ls-files 'skills/**/*.md'` lists
outside `skills/core/SKILL.md`, `skills/agent-contract/SKILL.md`,
`skills/implement/acts.md` (O2) and the three orchestration files. Each was
read whole (rule 12's second method), so the list of removals below is
whole for these files. The paraphrases among them are a sample (Q2).

**The statements phase 1 cited stand.** The bold sentence that opens
`skills/implement/SKILL.md`, which `skills/code-review/orchestration.md` now
cites, keeps its reason: the contract "reaches it by being opened rather
than by arriving". *3. The SDD file set* still says the spawn is the
approval, and *Document layout — two roots, three lifetimes* still says
where a `seal/…` path resolves (read at 1392479e2).

**Removals.** Each line number is at 3bd60d29f.

| File | Base line | Class | What went, and its grounds |
|---|---|---|---|
| `skills/implement/SKILL.md` | 25-26 | D2 | "#107's headline failure is an orchestrator breaking a rule it had put into every prompt it sent." It tells how the rule was found. The bold sentence and the reason after it state the rule in the present tense |
| `skills/implement/SKILL.md` | 291-293 | D2 | the clause "which is what every work item here did before the framer shipped, and what nothing in the set could say was wrong". This is the `## Removes` row. The sentence's first half states the effect |
| `skills/code-review/SKILL.md` | 198-200 | D2 | "The judgment rows of 0.26.0 to 0.29.0 trace nine regressions in seven work items to a paste-ready fix applied as given whose reach was one coordinate." This is the `## Removes` row. The paragraph's reason stands in the present tense before it: each statement a snippet leaves "returns as the next round's `regression:` or `reopens:` finding" |
| `skills/settle/SKILL.md` | 136-137 | D2 | the clause "so a run with no earlier settle prints what it printed before". It compares the output with the script's output before the section existed. "The section is printed only where it holds a row or a line not read" states the rule |
| `skills/settle/SKILL.md` | 350 | D2, borderline (Q1) | "goes as before" is now "goes, in each of these cases". "As before" refers to the behaviour before the note check existed. The cases after the colon state when a directory goes, and `skills/settle/scripts/settle.py`'s module docstring states the same act as "A directory with no note to read goes" |
| `skills/writing-style/SKILL.md` | 242-243 | D2 | "실제로 `seal` 은 세 가지를 동시에 가리켰다…" and the rest of that paragraph. It is a past event. The table above it gives the same three owners as its *좋음* cell, so the example stays in the present tense |
| `skills/writing-style/SKILL.md` | 245 | D2 | "규칙을 적어 두고도 다시 깨진 사례가 일곱 건이다." It is a count of past breaks. The bold "이 문장은 보장이 아니다." stays, and the sentences after it say in the present tense who finds such a sentence and why |
| `skills/writing-style/SKILL.md` | 269-270 | D2 | "사례는 `plan.md` 의 승인 줄이다…" It is a past event, and it names a line `plan.md` no longer carries: `skills/implement/SKILL.md` *3. The SDD file set* says the spawn is the approval "and no line records it". The rule before it stands alone |
| `skills/writing-style/SKILL.md` | 284-288 | D2 | "사례는 셋이다." and its three bullets: two past misreadings with #953 and a commit coordinate, and a third the paragraph already states in the present ("그 파일에서 "the session" 은 둘 중 누구로도 읽힌다"). The rule's reason stands before them: a sentence that drops the actor or the condition "절약이 아니라 결함이다" |
| `skills/writing-style/SKILL.md` | 302-303 | D2, repair (O7) | in the HTML comment, "읽기 시작해 표가 전부인 줄 알았기 때문이다" is now "읽기 시작하면 표가 전부인 줄 알기 때문이다". The past event was the comment's only stated grounds for repeating the header, so the grounds are restated in the present tense |
| `skills/writing-style/SKILL.md` | 321 | D2, repair (O7) | "도착할 이유가 없었다 (#265)" is now "도착할 이유가 없다". The issue that split the file goes with its past tense. The reason stays in the present tense |

The commit 1392479e2 rewraps the two paragraphs the removals shortened,
in `skills/settle/SKILL.md` and `skills/writing-style/SKILL.md`. It changes
no word.

**What stood on a removed sentence (S3, contract rule 19).** I ran `git
grep -n -F` over the whole tree, without `seal/threads/`, on the words of
each removal: "headline failure", "#107", "before the framer shipped",
"nothing in the set could say", "nine regressions", "0.26.0 to 0.29.0",
"printed before", "goes as before", "세 가지를 동시에", "일곱 건",
"승인 줄", "#953", "1792449518-settle-squashes", "사례는 셋", "PR 본문
쓰려고", "#265" and "도착할 이유가" (executed). No test, `KNOWN_PROSE`
entry, citation or Korean edition states a removed sentence. The other
hits are docstrings and comments of `.py` files that tell their own
history (O5), and `docs/checks/the-pull-request-check.md`'s "in 0.22.1 to
0.22.4", which is phase 3's `## Removes` row. No Korean edition covers
these files.

**Judged against D2 and D3 and kept, with the case that holds each.**

- `skills/code-review/SKILL.md:86-87`, "Contract rule 7 is about leavings,
  not files: …". It is a paraphrase of contract rule 7 in a file whose
  table row already says "everything else it made goes with it". It stays
  because
  `tests/behaviour/test_a_probe_that_commits_says_so.py#test_the_procedure_a_reviewer_follows_cites_contract_rule_7`
  pins it as the citation that row's qualifier needs (contract rule 14).
- `skills/verify/SKILL.md:121-124`, "The edit hook writes the values it is
  drawn from at the file's write, under either root, and the `Stop` hook
  draws them in the orchestrator's session". It restates
  `docs/checks/the-stamp.md` *The stamp*, which it cites. It stays because
  `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py#test_the_form_bullet_says_what_draws_the_final_seal`
  pins it as text the sealer and the crafter read in the **Form** bullet.
- `skills/commit-pr-convention/SKILL.md:52-56` and
  `skills/config/SKILL.md:17-21` both say where the `seal/` root resolves,
  which is contract rule 11 and `skills/implement/SKILL.md` *Document
  layout — two roots, three lifetimes*. They share a 12-word run. Both stay,
  on the ground #1313's D3 used for `skills/implement/SKILL.md`'s copy of
  contract rule 9. A session that invokes either skill directly, and the
  session a person runs `/agentic:config` in, is not preloaded with the
  contract, so the home is a file that reader does not open at that step.
- `skills/implement/SKILL.md:390`, "Never record something as passing that
  you did not run.", a 10-word run shared with contract rule 4. It stays on
  the same #1313 ground: a session that builds where `Implementation` is
  `the session` reads this skill without the contract.
- `skills/commit-pr-convention/SKILL.md:33-35`, "Everything below was read
  off a repository's log, and repositories differ." It tells how the table
  was found, but it is the rule's only stated grounds for letting a
  repository's own log outrank the table. O7 keeps a rule's only grounds.
- Version boundaries the reader acts on (D2):
  - `skills/code-review/SKILL.md:110-111`, a record written before the
    `evidence:` field "lacks the line, and that is no finding".
  - `skills/settle/SKILL.md:333-335` and `:343`, the HTML comment that the
    notes published before entries linked their pull requests carry.
  - `skills/update/SKILL.md:122-130` and `:198`, the preset block earlier
    releases wrote into `CLAUDE.md`, which step 4 takes out.

**Marker-probe sentences kept in these files**, three at 7b6e4858f:

| File | Sentence | Keep case (D2) |
|---|---|---|
| `skills/commit-pr-convention/SKILL.md` | "The work item is its directory's name under `seal/threads/`, … where the session ran `seal no-work-item` on the branch." | no history: the regex matched "work item … ran" |
| `skills/parity-setup/SKILL.md` | "Present what was found with what each one is, …" | no history: the regex matched "was found" in an instruction |
| `skills/update/SKILL.md` | the *Move* table, whose **measured** row cites "Run 6 of `docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.md`" | a coordinate a reader opens, and a definition that names its source: the row tells the user what a reload is known to do, and on what evidence |

Every other base marker sentence in these files was removed above.

**Census passages kept in these files, with the D3 ground for each**, read
from the ten-word census at 7b6e4858f. Shared wording is two files naming
one thing in the same words, and it stays. Phase 3 judges each `docs/`
side.

- `skills/code-review/SKILL.md`:
  - with `agents/proofer.md` (O1): "finding the round before closed
    `fixed <commit>` or `rejected` is answered" and "a case that holds no
    fact the frame states is". This skill is the procedure's home, and the
    other side is O1.
  - with `docs/forms/the-round-record.md`: the `seal` block's opening line,
    the bar "a wrong sentence an agent reads and acts on is `should`", and
    the `## Not judged` row. They are the form's words naming the same
    thing. The proofer writes the record from this section at that step,
    and the section does not send it to the `docs/` file.
- `skills/commit-pr-convention/SKILL.md`:
  - with `skills/config/SKILL.md`: the root resolution, kept above.
  - with `skills/config/SKILL.md` and `templates/setup/config.md`: "the
    commit subject and body, the pull request title and body". D3 gives
    it as its example of shared wording.
  - with `templates/setup/config.md` (O5): the exclusions. This skill is
    their home, and it says so ("That file repeats the exclusions below").
  - with `docs/releasing/issues-and-milestones.md`: an issue's title takes
    the prefix of the pull request that closes it. This skill ships the
    rule to every repository.
  - with `docs/checks/the-routing-check.md`: "a session's commit in a
    repository whose root is shared". That file names this skill as
    "where a session reads it".
- `skills/config/SKILL.md`:
  - with `skills/agent-contract/SKILL.md` and
    `skills/commit-pr-convention/SKILL.md`: the root resolution, kept above.
  - with `skills/implement/SKILL.md`: "no file, no such row, an empty value,
    a file that cannot be read". Each file states its own rows' default
    for its own reader.
  - with `skills/settle/rule-changes.md` and `templates/setup/config.md`:
    "a document of the policy root or of one of its groups". This is shared
    wording.
  - with `templates/setup/config.md` (O5): the rows' *What it governs*
    cells, the `Broad gate` refusal, "The table is read the way GitHub
    shows it, or refused" and the refused forms. Step 1 prints each row
    with its default and step 3 reads the refusals to the person, so these
    are the acts this skill's session takes. The other side is O5.
- `skills/implement/SKILL.md`:
  - with `templates/setup/config.md` and `templates/setup/seal-README.md`
    (O5): "A translated field name is not a translation…", and the
    sentence on where `seal/` lives. Only the in-scope side could change,
    and both are this skill's reader's act.
  - with `skills/settle/rule-changes.md`: "a work item whose subject is the
    code states the rules". Each file cites the other for the case it does
    not hold.
  - with `docs/checks/the-fold.md`: "writes each section as the latest
    decision the released designs state". This is shared wording naming
    the settle's act.
  - with `agents/sealer.md` and `skills/verify/SKILL.md`: "asserting that
    something is not named, counted, read or let through". This is the
    name of contract rule 15's class.
  - with `docs/layout/the-record-layout.md`: "each with its grounds and the
    document it stands on" and "and who answers it, and what was within
    reach". This skill's *3. The SDD file set* and *4. The closing memo*
    are where the builder reads the file set.
  - with `docs/running/the-agent-set.md`: "the party that draws a contract
    is not the party that executes it" (14 words), a citation phrase that
    names what the cited home says. Also "is a decision the orchestrator
    folds into the plan before the spawn". In *3. The SDD file set* it is
    the builder's reason the phase record copies no spawn scope, which is
    the act this skill's reader takes when it writes the record.
  - with `templates/records/sdd-gaps.md` (O5): the closing memo's second
    kind.
  - with `skills/code-review/orchestration.md`: the fix pass's close blocks
    and the changelog brought along. Phase 1 judged them kept.
- `skills/implement/bootstrap.md`, with `skills/implement/orchestration.md`
  and `skills/code-review/orchestration.md`: phase 1 judged both runs kept.
- `skills/implement/multi-repository.md`, with `docs/layout/the-pact.md` and
  `templates/setup/pact.md`: the definition "a sentence is contract when
  another repository's code would be wrong if it changed", the reason no
  check reads a twice-minted id, and what `seal pact` reads. The
  orchestrator decides at this step whether the repositories sign a pact.
  The section points at `docs/layout/the-pact.md` for the model and not
  for the decision.
- `skills/legacy-parity/SKILL.md`:
  - with `agents/tracer.md` (O1): the three section names.
  - with `docs/checks/the-pull-request-check.md`: what a proofer that could
    not resolve the original writes. *Recording the comparison* is that
    rule's home, and `skills/parity-setup/SKILL.md` cites it.
- `skills/settle/SKILL.md` and `skills/settle/local-mode.md`:
  - with `docs/checks/the-fold.md`: four runs, the named directories'
    commits, "the rest of the document stays as it was", the first-fit
    order of the row kinds, and the local `--apply`.
  - with `docs/releasing/release-checklist.md`: what `--apply` removes.
  - These sides are the settling session's procedure, which it follows at
    each step, and phase 3 judges the `docs/` sides.
- `skills/settle/rule-changes.md`:
  - with `skills/implement/SKILL.md`: kept above.
  - with `docs/checks/the-pull-request-check.md`: two check-line phrases.
    This file is the grammar's home.
  - with `skills/config/SKILL.md` and `templates/setup/config.md`: shared
    wording, kept above.

**Census readings at 7b6e4858f**, by phase 1's probe rewritten to D4 under
the session's scratch directory as one file, `test_tmp_census.py`, run in a
`git clone --no-local` and deleted after its runs (executed). The base
reading at 3bd60d29f, run again first, equals `frame/design.md`
*Grounding*: 2,078 of 88,708 words, 80 pairs, 264 runs, and 58 marker
sentences in 22 files. At 7b6e4858f it read 1,977 of 88,240 words, 80
pairs, 255 runs, and 49 marker sentences in 19 files. 1392479e2 changes no
word. The ten-word figures equal phase 1's reading at 19f0ceafe except the
word total, because no removal of this phase sat in a shared run. These
readings are context, and the HEAD reading of record is phase 3's.

**Narrow runs (executed, through `bin/test`).**

- The phase-boundary set (`skills/verify/SKILL.md` *Scope: cheap and often,
  broad and once*) was 57 modules in one command. They are every test
  module that names one of the four changed files, by path or by
  `"<skill>", "SKILL.md"`, and every module that walks, globs or lists a
  tree holding `skills/`, listed by `git grep -l`. Among them are
  `tests/text/test_no_passage_is_pasted_into_a_second_file.py`,
  `tests/behaviour/test_docs_line_wrap.py`,
  `tests/behaviour/test_a_probe_that_commits_says_so.py` and
  `tests/text/test_a_language_section_of_writing_style_opens_alone.py`.
  `bin/test -q -p no:randomly <the 57>` exited 0 with 3,133 passed and 11
  skipped, once before the commit 7b6e4858f and once at 1392479e2.
- No unit adds behaviour, so no case was written new and no `seal mutate`
  ran (`skills/verify/SKILL.md` *The narrow command still has to be able to
  fail*, the prose row). The suite stays `unverified` until the
  orchestrator's broad gate.

**Q2: the paraphrases this phase met are a sample.** Reading each file
whole found two restatements of another file. The rule 7 gloss in
`skills/code-review/SKILL.md` and the stamp mechanism in
`skills/verify/SKILL.md` were both kept above, each held by a case. A
restatement in other words shares no ten-word run, so no probe lists one.
Judged against `frame/questions.md` Q2's default.

**For phase 3.**

- The `docs/` sides of the pairs above are phase 3's to judge. They are
  `docs/running/the-agent-set.md`, `docs/forms/the-round-record.md`,
  `docs/layout/the-pact.md`, `docs/checks/the-fold.md`,
  `docs/layout/the-record-layout.md`,
  `docs/checks/the-pull-request-check.md`,
  `docs/releasing/issues-and-milestones.md`,
  `docs/checks/the-routing-check.md` and
  `docs/releasing/release-checklist.md`. Where this record names a skill
  as the home, the `docs/` side is the copy under D3.
- `docs/running/the-agent-set.md:104-106` states "a decision the
  orchestrator folds into the plan before the spawn" and cites
  `skills/implement/orchestration.md` *Orchestrator: the order inside a
  ticket* for it. `skills/implement/SKILL.md` *3. The SDD file set* keeps
  its own statement as the builder's reason, so whatever phase 3 does
  with the `docs/` side, that sentence stays.
