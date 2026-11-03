# Review round 2: 1793678623-each-rule-rides-with-the-agent-that-uses-it

```seal
target: d544e722b, fixes e045e7264..d544e722b
```

This is a verifying round. It reads the diff of the last fixes,
`git diff e045e7264 d544e722b`: 3a4d969b7, dbf25435e, 5aba6d616 and
d544e722b (executed). The branch's base is `release/v0.30.1` at 0c68b9933.
The repository tracks no `seal/parity.md` (`git ls-files seal/parity.md`,
executed, no output), so no `original:` line is owed. `seal/config.md` has no
`Record language` row, so the record is English. The runs took place in a
`git clone --no-local` at d544e722b in the session scratchpad, which has since
been removed.

Carried from round 1 and not re-established: each agent's `skills:` list is
`core` and `agent-contract`, so the contract reaches all five agents. Also
carried: `.github/scripts/release_report.py#preloads` sums the definition,
the core and the contract. Every verdict below was reached this round.

The fix pass's account was read as a claim. It claimed the new case was seen
red, the preloads at 3a4d969b7, and that three frame statements still said
only the builders commit. Each is checked below.

## Findings

### 1. Frame criterion S2 still says the contract holds no commit form, and rule 6 now holds it

```seal
severity: should
location: `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/frame/design.md:107`
evidence: read `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/frame/design.md:107`, `skills/agent-contract/SKILL.md:83-86`
regression: round-1#1
```

Unit: contract rule 6's commit sentence, which 3a4d969b7 added
(`skills/agent-contract/SKILL.md:83-86`). The frame's S2 says "the commit form
of old rule 16 stands in `skills/implement/SKILL.md` *2.* ... and the contract
holds neither", and phase 2's plan row is verified against S2. The fix put the
commit form back into rule 6: "writes the repository's absolute path after
`git -C` in a command of its own". The defect came from the fold at d544e722b,
which reached row 16, D1 and the plan's rule-16 row but not S2. The fix
pass's hand-back named only those three statements.

Why it matters: S2 is a success criterion the sealer reads against the tree.
At HEAD the contract holds the commit form, so S2 now states something false.
The sealer has to choose between the frame and the tree, or withhold on a
criterion the work no longer meets. S2's verification column also omits the
case that now pins the contract's sentence.

The snippet covers both of S2's cells. It reaches no other statement: row 16
and D1 already say rule 6 keeps one sentence (`frame/design.md:141`, `:235`,
read).

```markdown
In frame/design.md, row S2, the Given/when/then cell:

Given HEAD, when the crafter or the session builds a phase, then the commit
form of old rule 16 stands in `skills/implement/SKILL.md` *2.* and the
phase-boundary set in `skills/verify/SKILL.md`'s *Scope* table; the contract
holds no phase-boundary set, and of the commit rule only rule 6's one
sentence, which states the `git -C` form and cites implement's rule

In the same row, the verification cell:

`tests/behaviour/test_a_commit_names_its_repository.py`, retargeted at the new
home, with `test_the_contract_points_every_agents_commit_at_the_rule` reading
rule 6's sentence, and `tests/text/test_broad_gate_rule.py`, run narrow
```

```seal
verdict: fixed 6a0d36caf
answer: The finding holds, and 6a0d36caf closes it in `frame/design.md`, the path the finding names. S2's Given/when/then cell now says that the contract no longer holds the phase-boundary set. It also says that of the commit rule the contract holds only rule 6's sentence, which states the `git -C` form and points at implement's rule. Its verification cell names `test_the_contract_points_every_agents_commit_at_the_rule`. The tree bears both cells out (read at HEAD). Rule 6's sentence stands at `skills/agent-contract/SKILL.md:83-86`. `git grep -n "phase boundary" -- skills/agent-contract/SKILL.md` lists nothing (executed). The case passes in the narrow run. The orchestrator wrote the fold in its own words, and they say what the snippet says.
```

### 2. The changelog gives the census of the tree before the fix, and D6 sends the body to a preload table the fix made stale

```seal
severity: should
location: `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/changelog.md:6`, `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/frame/design.md:336-338`
evidence: executed `python3 -I test_tmp_census.py <clone> 0c68b9933 e045e7264 d544e722b`
regression: round-1#1
```

Unit: the changelog's last bullet, which 3a4d969b7 rewrote. D6 measures
preloads and the census "at HEAD" and puts both readings in the last phase
record (`frame/design.md:322-338`). The fix re-took the preloads at 3a4d969b7
but kept the census figure from e045e7264. The defect came from re-measuring
one of D6's two readings after the fix added 36 words to the contract.

Why it matters: the fragment becomes the release notes, and it would ship
"754 of 10,733" for a tree that reads otherwise. The probe ran D6's method
over three commits. It reproduced 934 of 11,209 at 0c68b9933 and 754 of
10,733 at e045e7264. At d544e722b it read 766 of 10,769, and the contract
alone went from 58 of 1,939 to 70 of 1,975. Every other file's count is
unchanged. The same run summed the preloads at d544e722b: crafter 31,730,
framer 34,836, proofer 30,840, sealer 30,556 and tracer 23,970. These match
the bullet, so its preload half holds.

The phase 4 table itself is no defect. It names the commits it measured,
08b43c65f and 20e140537 (`trail/phases/phase-4.md:30-36`, `:59`, read), and a
phase record states its own reading. But D6 still says "The pull request body
copies the preload table from there" (`frame/design.md:337-338`). An
orchestrator who follows it would copy figures 220 bytes below HEAD for each
agent. `seal pr-body` copies the changelog fragment and only the phase
records' paths (`skills/code-review/scripts/pr_body.py:9-17`, read), so the
fragment is the copy that carries HEAD.

The snippet covers both statements. Phase 4's table and round 1's census row
stay as they are, since each names the commit it read.

```markdown
In changelog.md, the last bullet:

... the words inside a ten-word run that another tracked file outside `seal/`
and `tests/` also holds fall from 934 of 11,209 to 766 of 10,769. ...

In frame/design.md, D6, the last bullet's last sentence:

The pull request body copies the preload figures from `changelog.md`, which
gives them at HEAD.
```

```seal
verdict: fixed d90b20d83
answer: The finding holds. In d90b20d83 the changelog's census figure reads "766 of 10,769". It was re-taken at HEAD, not worked out from the old figure. A new one-file probe written to D6's method ran over clones at 0c68b9933 and 6a0d36caf, whose tree outside `seal/` equals d544e722b's. It gave 934 of 11,209 at the base, the frame's reading in every cell, and 766 of 10,769 at HEAD, with the contract at 70 of 1,975 (executed; the probe and clones are removed). Every other figure in `changelog.md` and `gaps.md` was re-taken the same way, and each still holds. The five preloads came from `release_report.py --against v0.30.0 --at <base clone> --root <HEAD clone>`, exit 0, and from each agent's `wc -c` sum: 31,730, 34,836, 30,840, 30,556 and 23,970 (executed). `skills/implement/SKILL.md` +721 and `skills/verify/SKILL.md` +111 came from `git show <commit>:<path> | wc -c` (executed). The `.test_durations` entry `gaps.md` *Not done* names is still there (executed). The frame half, D6's sentence on the body's copy, is 6a0d36caf's, read at HEAD: the body now copies the figures from the changelog. The same commit also corrects two docstrings and a changelog clause. Each said that the agents that commit without opening implement's *2.* read part of that file, and each now says that no step of theirs opens *2.*.
location: `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/changelog.md:3`, `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/changelog.md:6`, `tests/behaviour/test_a_commit_names_its_repository.py:10-18`, `tests/behaviour/test_a_probe_that_commits_says_so.py:9-14`
```

### 3. The new gaps row hands the framer's and the probes' commits to a measurement that counts crafter transcripts only

```seal
severity: should
location: `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/gaps.md:14`, `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/frame/questions.md:16`
evidence: read `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/gaps.md:14`, `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/frame/questions.md:16`
regression: round-1#1
```

Unit: the `## Not verified` row 3a4d969b7 added (`gaps.md:14`). The frame's
Q1 asks whether "a crafter spawn" finds the commit form in implement *2.*. Its
measurement is "a count, over the first 0.30.1 crafter transcripts, of
phase-boundary runs and commits in the `git -C` form" (`frame/questions.md:16`).
The fix's row asks the opposite case: whether the framer, or an agent whose
probe commits, commits in that form from rule 6's sentence. It names "Q1's
measurement" as the answerer. The defect came from pointing the new row at
the existing question without widening that question.

Why it matters: contract rule 4 asks that an `unverified` row name who
answers it. Q1's answerer, reading Q1, counts crafter transcripts and never
opens a framer, proofer, sealer or tracer transcript. So the row's question
has no answerer, and a full answer to Q1 as written leaves this row open.

The snippet widens Q1, which the gaps row already cites. The row can then
stand as written. The fix pass may instead name another answerer in the
row's second cell.

```markdown
In frame/questions.md, Q1's question cell, after "*2.*?":

And does an agent that commits without opening *2.*, the framer where a spawn
prompt asks and a proofer's, sealer's or tracer's probe, commit in that form
from contract rule 6's sentence?

In the same row's options cell, after "commits in the `git -C` form":

; and, over the first 0.30.1 framer, proofer, sealer and tracer transcripts,
each commit and whether it is in that form
```

```seal
verdict: fixed 6a0d36caf
answer: The finding holds, and 6a0d36caf closes it in `frame/questions.md`, a path the finding names. The fix was written in the orchestrator's words, not the snippet's. Q1 now also asks whether "a framer or a probe of any agent that commits under it" writes the `git -C` form contract rule 6 states. Its measurement now counts "over the first 0.30.1 transcripts of every agent, of commits in the `git -C` form" (read at HEAD). `gaps.md:14` asks whether such an agent under 0.30.1 commits in the `git -C` form from that sentence. That is the same question, so the row stands as written and names Q1's measurement as its answerer. `gaps.md:10`, the crafter's commit form and phase-boundary runs, and `gaps.md:15`, the installed preload, also cite Q1 and match its first two parts. Every row of `gaps.md` was read whole against HEAD, and none was changed for this finding.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the close `fixed 3a4d969b7` holds for the defect round 1 found.
Rule 6 now states the `git -C` form and cites implement's rule in the file
all five agents preload (`skills/agent-contract/SKILL.md:83-86`, read). Rule
11 resolves its `skills/` path at the plugin's root
(`skills/agent-contract/SKILL.md:134-137`, read). The cited lead stands at
`skills/implement/SKILL.md:193` (read), and
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` passed in the
narrow run (executed). The fix pass claimed it chose the contract over code
review *Probes* and `agents/framer.md` because only the contract reaches the
sealer's and the tracer's probes. That holds: `agents/sealer.md` and
`agents/tracer.md` name neither `skills/code-review/SKILL.md` nor
`agents/framer.md` (`grep`, executed, no lines). The preloads at d544e722b match the
changelog's figures, and each is still below its v0.30.0 figure (executed,
the census probe). Findings 1 to 3 are statements this fix left behind, not
a failure of the fix itself.

```seal
confirms: none
```
What matched: the new case `test_the_contract_points_every_agents_commit_at_the_rule`
(`tests/behaviour/test_a_commit_names_its_repository.py:71-83`, read). Its
group is the module's other cases, which read implement's rule and the
orchestration's citation. No case reads the contract's sentence, and the
cited-section case checks that a citation resolves but not that this one
exists. So the case covers something its group does not. It pins the form an
agent types and the place it is sent. Both are facts a reader acts on, not
wording, by `docs/running/what-a-script-gates.md` *The checks* (read). The
fix pass claimed the case was seen red against the contract before the edit.
At e045e7264 the contract holds neither pinned phrase, since a search for
`git -C` and the cited lead found no line (executed, exit 1). So both
assertions fail there.

```seal
confirms: none
```
What matched: the two docstrings in the fix diff. The one in
`tests/behaviour/test_a_commit_names_its_repository.py:10-19` and the one in
`tests/behaviour/test_a_probe_that_commits_says_so.py:9-14` say what rule 6
now states (read). Their new lines run to 102 and 109 characters. `ruff.toml`
selects no `E501` and sets `line-length = 88` for the formatter, which leaves
docstrings alone (read). That is a line that reads badly, not a defect.

```seal
confirms: none
```
What matched: the orchestrator's fold at d544e722b. Row 16 and D1 of
`frame/design.md` and the rule-16 row of `frame/plan.md` *Alternatives
considered* now say that rule 6 sends every other agent's commit to
implement's rule, which is what HEAD does (read). The new row of *Judgments of
the run* names its grounds and the document it was judged against. Finding 1
names the one statement of the same fact that the fold missed.

```seal
confirms: none
```
What matched: the changed and dependent modules pass at HEAD. One `bin/test`
command over ten modules exited 0 with 341 passed (executed). It covered the
commit and probe modules, the contract-shape, every-agent, cited-section,
pasted-passage, sealer-seal, moved-rule, one-owner and pact-signer modules.
The last one reads the multi-repository `git -C` sentence.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, lint and typecheck at HEAD: the suite is `unverified` here | the repository's `Broad gate` row | the orchestrator, at the broad run after the rounds settle; with no finding left open, the sealer's spawn follows it |
| Whether an agent spawned under 0.30.1 commits in the `git -C` form from rule 6's sentence | `frame/questions.md` Q1, once finding 3 widens it | the Q1 measurement on the first 0.30.1 transcripts |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_census.py <clone> 0c68b9933 e045e7264 d544e722b`, one file written this round to D6's method, which reads each commit through `git show` and also sums each agent's definition, core and contract | exit 0; 934 of 11,209, 754 of 10,733 and 766 of 10,769; preloads at d544e722b of 31,730, 34,836, 30,840, 30,556 and 23,970; the file, its output and the clone were deleted |
| `bin/test` over the ten modules named above, `-q`, in the scratch clone at d544e722b | exit 0, 341 passed |
| `git show e045e7264:skills/agent-contract/SKILL.md`, whitespace folded, searched for `git -C` and the cited lead | exit 1, no lines |
| `grep -n -E "code-review/SKILL\|agents/framer" agents/sealer.md agents/tracer.md` | no lines |
