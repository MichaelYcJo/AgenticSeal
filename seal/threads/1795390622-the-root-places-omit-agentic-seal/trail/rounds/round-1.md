# Review round 1: 1795390622-the-root-places-omit-agentic-seal

```seal
target: 64059f40f90668083bde29770e04f51e88cbbc97 against release/v0.38.6
```

This is the first round, so no earlier record carries a coordinate and
every fact below was established here. The diff was read from the base
`641b6bfb5` (tag `v0.38.5`) to `64059f40f`, every file of it. `routing.md`,
the three frame files, `gaps.md`, `changelog.md`, `pr.md` and the three
phase records were each read whole at `64059f40f`. No `pr.<lang>.md`
stands, and none is owed: `seal/config.json` names English for both
language keys. No `seal/parity.json` is declared. The frame's `## Rule
changes` holds the no-change block, and the chain check printed no notice
of a test pin or a copy at a line of `frame/design.md`.

The three facts the spawn prompt handed over unopened were opened here.
`seal/README.md` is byte-identical to `templates/setup/seal-README.md`
(executed, `diff`, no output). `docs/forms/the-reader-registry.md` is
deleted and its row in `docs/README.md` with it (read, the diff; executed,
`git grep -n 'reader-registry' -- ':!seal/threads'` prints nothing). Of the
four sentences `gaps.md` *Not done* names as standing outside their owners,
three stand on the grounds it gives, and one does not (finding 3).

## Findings

### 1. The changelog's first item and its first process row miscount the files that spelt the root's places, and say no file spells the shared place

```seal
severity: should
location: `seal/threads/1795390622-the-root-places-omit-agentic-seal/changelog.md:3`, `seal/threads/1795390622-the-root-places-omit-agentic-seal/changelog.md:20`
evidence: executed `git grep -l -e '<repo>/seal' 641b6bfb5 -- skills agents templates docs seal/README.md ':!*.py'`, `git grep -n -e '<repo>/seal' -- skills agents templates docs ':!*.py' ':!seal/threads'`; read `skills/implement/bootstrap.md:37`, `skills/implement/bootstrap.md:58`, `docs/layout/one-root-by-lifetime.md:101`, `docs/layout/one-root-by-lifetime.md:124`
```

Why it matters: the fragment becomes the release note, which a person
reads for what changed. Two of its sentences state counts and one states
an absence, and the tree contradicts all three.

- **Claimed** at `changelog.md:3`: "Contract rule 11 and seven other files
  named the first and the last alone." **Found**: the same item then lists
  ten other files that now cite the core, and each of them spelt
  `<repo>/seal/` at the base. The search at `641b6bfb5` lists those ten
  beside the contract: `docs/layout/one-root-by-lifetime.md`, its `.ko.md`
  pair, `docs/layout/the-record-layout.md`,
  `skills/commit-pr-convention/SKILL.md`, `skills/config/SKILL.md`,
  `skills/implement/SKILL.md`, `skills/implement/bootstrap.md`,
  `skills/implement/orchestration.md`, `templates/setup/config.md` and
  `templates/setup/seal-README.md`, and `seal/README.md`, the template's
  byte-identical copy, which the item leaves out. The two files of
  the parity skills that also print are the shared mode's name, which the
  frame puts out of the class. "Seven" is the issue title's count, which
  the build's own list outgrew; the commit `222b5b5b5` says eleven files
  cite the core.
- **Claimed** at `changelog.md:3`: "none spells the shared place."
  **Found**: `skills/implement/bootstrap.md:37` and `:58` and
  `docs/layout/one-root-by-lifetime.md:101` and `:124` spell `<repo>/seal/`.
  They state where first setup creates the root and the mode table, which
  the frame keeps (`frame/design.md` *Scope* item 3). The sentence is true
  only of where the root is looked for.
- **Claimed** at `changelog.md:20`: "Eight files spelt two places".
  **Found**: the contract and the ten files above, eleven in all, twelve
  with `seal/README.md` counted beside its template.

```markdown
<!-- changelog.md:3, the second and the fifth sentences -->
Contract rule 11 and ten other files named the first and the last alone.
...
and none spells the shared place as where the root is looked for.

<!-- changelog.md:20, the Why cell -->
Eleven files spelt two places and omitted the one the gates read second, and the core is the one file every agent and every session with a root already has
```

### 2. The owner paragraph calls a file that will not read an absent language key, and the paragraph after it says such a file is refused rather than read as absent

```seal
severity: should
location: `templates/setup/config.md:31-39`, `templates/setup/config.md:41-42`
evidence: read `templates/setup/config.md:31-58`, `skills/implement/routing-question.md:139-145`, `lib/config.py:196-205`
```

Why it matters: `frame/design.md` *Scope* item 5 makes the paragraph at
`templates/setup/config.md:31-39` the one statement of an absent language
key, and six files now send their readers to it. It says "A language key
is absent in four ways", and the fourth way is "a file that cannot be read
or does not parse as one JSON object, a key written twice or holding no
string among them". The next paragraph opens, at `:41-42`, "A key written
twice has no value, and a file that will not read is refused rather than
read as absent." Before this work the four ways stood in
`skills/commit-pr-convention/SKILL.md`, and the two statements were in
different files. The move put them in adjacent paragraphs of the one
owner, where they answer the same question two ways. A reader of
`skills/implement/routing-question.md:141-144` acts on the answer: the
batch asks for both keys "where either is absent in any of the four ways"
the paragraph names. A reader who takes the second paragraph's lead reads
a key written twice as not absent, and does not ask. The code takes the
first reading: `lib/config.py#declared_value` hands a refusal to every
caller, and `seal pr-body` refuses on it. This is the two-readings rule of
`skills/writing-style/SKILL.md`
*에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*.

The fix adds one sentence to the owner paragraph. It keeps the four
spellings `RULES` row 26 of `tests/text/test_the_rules_have_one_owner.py`
pins and the bold lead the six citations name, so no other file changes.

```markdown
**An absent language key is a refusal at the pull request body, and never
at a commit.** A language key is absent in four ways: no file, no such key,
an empty value, and a file that cannot be read or does not parse as one
JSON object, a key written twice or holding no string among them. The
fourth is the refusal the next paragraph gives, which for these two keys
counts as absent wherever this file or a skill speaks of an absent key. In
each, `seal pr-body` refuses with nothing written, naming the key, or
printing the refusal the next paragraph gives where the file or the key
will not read. A commit or a record is written in English, because a
config nobody can read must not stop the work. Who asks for the two keys is
*Commit and pull request language* below.
```

### 3. A restatement of what an absent key does stays in the commit skill on a frame coordinate that does not hold it

```seal
severity: should
location: `skills/commit-pr-convention/SKILL.md:87-89`, `seal/threads/1795390622-the-root-places-omit-agentic-seal/gaps.md:16-21`, `seal/threads/1795390622-the-root-places-omit-agentic-seal/trail/phases/phase-2.md:99-105`, `seal/threads/1795390622-the-root-places-omit-agentic-seal/frame/design.md:127`
evidence: executed `git show 73a43735c:skills/commit-pr-convention/SKILL.md | awk 'NR>=85 && NR<=92'`, `git show 73a43735c:templates/setup/config.md | awk 'NR>=86 && NR<=92'`; read `skills/commit-pr-convention/SKILL.md:82-89`, `seal/threads/1795390622-the-root-places-omit-agentic-seal/frame/design.md:59-79`
```

Why it matters: the closing memo tells the sealer the sentence stays on
grounds the frame gives, and the frame gives none.

- **Claimed** at `gaps.md:16-21` and `trail/phases/phase-2.md:99-105`:
  `skills/commit-pr-convention/SKILL.md:87-89`, "`seal pr-body` refuses to
  compose a pull request body where either key is absent in any of the four
  ways, because the body's language is the one the team reads", stays
  because "*Scope* names `:85-89` of `73a43735c` out of scope as the
  sentences on who asks." **Found**: at `73a43735c`, lines 85-89 of that
  file are the bold lead **Both keys are required all the same, and a
  commit is never refused for them.** and the two sentences on who asks,
  ending at the citation of `skills/implement/routing-question.md`. The
  `seal pr-body` sentence is lines 90-92. Phase 2 shortened the file by
  three lines and read the frame's coordinate against the new numbering.
- **What the frame says** of the sentence: nothing by coordinate. Its
  *Out of scope* bullet keeps who asks (`frame/design.md:79`). *Scope*
  item 5 makes "each restatement" of what an absent key does a citation of
  the template's paragraph. Its *Removes* row at `frame/design.md:127`
  lists "The ways a language key is absent, and what an absent one does,
  stated outside the template's paragraph". The sentence says both: the
  four ways, by count, and the refusal.
- **What the build did with the same sentence in the template**: at
  `73a43735c` `templates/setup/config.md:90-91` said "`seal pr-body`
  refuses to compose a pull request body without either", and phase 2
  removed it (`templates/setup/config.md:93-96` at HEAD).

The reason the sentence gives, that the body's language is the one the
team reads, is the template's, so the fix keeps it and drops the
restatement. The paragraph above it at `:76-80` already cites the owner for
the four ways and what each does. Rule 19 owes the memo and the phase
record the corrected ground in place.

```markdown
<!-- skills/commit-pr-convention/SKILL.md:87-89 -->
The refusal stands at the pull request body because the body's language is
the one the team reads. Nothing reads the keys at a commit.

<!-- gaps.md:16-21 -->
Phase 2 left one sentence that states part of what an absent language key
does, beside a reason the template does not give:
`docs/forms/the-guarantee.md:22`, a policy document outside the list
*Scope* item 5 names. `trail/phases/phase-2.md` gives the grounds.

<!-- trail/phases/phase-2.md:99-105: the bullet goes, or reads -->
- `skills/commit-pr-convention/SKILL.md:87-89` kept a restatement of the
  refusal on a misread coordinate; round 1 finding 3 corrected it.
```

### 4. The frame's G18 still says `tests/github/test_release_seal.py:382` holds a sentence of *The broad gate*, which the fold of G14 says it does not

```seal
severity: should
location: `seal/threads/1795390622-the-root-places-omit-agentic-seal/frame/design.md:26`
evidence: read `seal/threads/1795390622-the-root-places-omit-agentic-seal/frame/design.md:22`, `tests/github/test_release_seal.py:376-382`, `skills/verify/orchestration.md:95-97`; executed `git diff 30a0b05ef HEAD -- seal/threads/1795390622-the-root-places-omit-agentic-seal/frame/design.md`, `git diff --stat 641b6bfb5 HEAD`
```

Why it matters: a later framer, the sealer and the settle read the
frame's *Grounding* as the tree at `73a43735c`. Two of its rows now say
opposite things about one line.

The orchestrator's fold at `95344f189` corrected G14 to say
`tests/github/test_release_seal.py:382` "is an entry of that case's
`REASONS` table, a reason the release workflow prints, and pins no
sentence of `skills/verify/orchestration.md`". That is what the line
holds: `"a line of the record did not parse": "did not parse as the
recorder's"`, a key and the reason the release workflow prints. G18's
last sentence, at `frame/design.md:26`, still reads
"`tests/github/test_release_seal.py:382` holds *The broad gate*'s
unparsed-line sentence." The file is not in the diff, so the line held the
same at `73a43735c`, and G18's sentence was false at the commit it states.
The fold reached one of the two statements of the fact (contract rule 19).

```markdown
<!-- frame/design.md:26, G18, the last sentence of the cell goes; the cell ends -->
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:339-357` holds the crafter's paragraph naming `` `failing on base too` ``, `` `new?` `` and rule 2.
```

## Confirmations

What matched: *Scope* item 1. `skills/core/SKILL.md:23-29` names
`<repo>/seal/`, then `agentic-seal/` beside it, then
`$(git rev-parse --git-common-dir)/seal/`, the order `lib/optin.py#home_at`
(`lib/optin.py:280-319`) reads through `#home_paths`
(`lib/optin.py:153-199`), and names `agentic-seal/` on one line, line 25
(read; executed, `git grep -n 'agentic-seal'` over the scanned roots prints
that line alone).

What matched: *Scope* item 2. Contract rule 11
(`skills/agent-contract/SKILL.md:121-131`) spells no place, cites the core's
opening paragraph and the template's two sections, and the sentence "A
repository with both is shared" is gone (read).

What matched: *Scope* item 3, every coordinate of its list, each read at
HEAD: `skills/implement/SKILL.md:85-96`, `skills/implement/orchestration.md:9-12`,
`skills/implement/bootstrap.md:3-5`, `:79-82` and `:203-205`,
`skills/commit-pr-convention/SKILL.md:51-55`, `skills/config/SKILL.md:19-29`,
`templates/setup/config.md:7-10` and `:186-189`,
`docs/layout/one-root-by-lifetime.md:27-28` and `:64-70`, its `.ko.md` pair
at `:27-28` and `:61-66`, which renders the English edit,
`docs/layout/the-record-layout.md:84-86`, and the README pair. The class
was re-listed with `git grep -n -e '<repo>/seal' -e 'common-dir)/seal' -e
'two places' -e 'either place' -e 'one of two places' -e 'git-common-dir'`
over `skills`, `agents`, `templates`, `docs`, `seal/README.md`, both READMEs,
`CONTRIBUTING.md` and `CLAUDE.md`, every hit read (executed). Contract rule
12 calls the list a sample: a sentence in other words stays outside it.
The hits that still say "either place" or "two places" are
`skills/implement/multi-repository.md:16`, `skills/implement/fix-pass.md:36`,
`skills/implement/bootstrap.md:33`, `docs/layout/one-root-by-lifetime.md:88`
and `:111` with the `.ko.md` pair, `templates/setup/config.md:180` and
`:364`, and the `Mode` row of `skills/config/SKILL.md:43`. Each counts the
shared and the local root, the framing G3 takes from `#home_paths`, and
none spells the shared place, so none is a finding. Phase 1 reworded
`skills/config/SKILL.md`'s "either" because the sentence above it now cites
three places. `skills/implement/multi-repository.md:16` sits beside a
citation of rule 11, which names no count, so that ground does not reach it.

What matched: *Scope* items 4 and 5. `templates/setup/config.md` *Record
language* (`:98-103`) lists `trail/phases/phase-N.md`, and every list the
item names cites it. The paragraph at `:31-39` holds the four ways, and the
six citations its bold lead takes resolve (executed, the narrow run below,
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` among it).
S4's search prints `templates/setup/config.md:32` and `:209` (executed).

What matched: *Scope* items 6 and 7. `skills/code-review/orchestration.md:115-119`
and `:132-137` cite *The run* for the count, the reset, the verifying round
a regression is owed and the judgment row. `docs/running/the-run.md:8-21`
states each (read). S5's search prints the four lines S5 names (executed).

What matched: *Scope* item 8. The three bullets of
`skills/verify/orchestration.md:70-80` open with the words
`skills/verify/scripts/broad_gate.py:187` and `:1466` hold, and cite them.
`agents/crafter.md:147-151` gives the act at each word and no meaning
(read).

What matched: *Scope* item 9. `docs/running/the-broad-gate.md:74-76` spells
`<base>@{upstream}`, `origin/<base>` and the ref as given, the order
`skills/verify/scripts/broad_gate.py#resolve_base` tries (read).
The two orchestration files cite it and spell no ref, apart from
`skills/code-review/orchestration.md:477-481`, the sealer's clone, which
`gaps.md` names with the out-of-scope `agents/sealer.md:42-48`, and which
holds (read).

What matched: *Scope* item 10. The agent-set paragraph
(`docs/running/the-agent-set.md:120-125`) holds the no-change block's
clause, and `CONTRIBUTING.md:408-409`, `agents/framer.md:222-224`,
`skills/implement/SKILL.md:287` and `:313-314` and the docstring at
`tests/behaviour/test_a_phase_hands_the_next_one_a_record.py:118` cite it
(read). S8's search prints nothing (executed).

What matched: `gaps.md:16-29`, the other three sentences outside their
owners. `docs/forms/the-guarantee.md:22` is a policy reason outside
*Scope* item 5's list. `skills/code-review/orchestration.md:477-481` is the
sealer's resolution. `docs/running/what-a-script-gates.md:57` names the
three words and says only that they are reported (read).

What matched: `pr.md`. Each of its three quotes stands word for word at
its coordinate: `frame/plan.md:59` twice, the Judgment cell and the Grounds
cell, and `routing.md:24` (read).

What matched: the tests. The modules the plan's three rows name, with the
contract module and the records module, pass at HEAD (executed, the narrow
run under *Probes*). Of the cases this diff changes,
`test_moving_a_sentence_to_another_section_is_caught` now moves rule 21
under the rule before it, and the deleted cases are the ones G18 names,
each replaced by the `RULES` link D1 gives or rewritten to its citation
(read).

Three gaps of the kind `skills/code-review/SKILL.md` *The record* names,
none a finding. `RULES` row 24's fact `` `agentic-seal/` ``
(`tests/text/test_the_rules_have_one_owner.py:229`) is held already by
`tests/behaviour/test_no_document_names_the_old_roots.py:78-83`, which
fails on a count other than one. Row 27's fact `` `new?` `` (`:287`) is
held already by the sealer case's `readers` entry `` **`new?`** ``
(`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:221`). D1
asks for both facts, and each row's other facts pin what nothing else
does. The comment above row 24 (`:217-222`) says six files spelt the
places, where ten did, and six is the count of the links.

The core's opening paragraph does not name the opt-out file that
`lib/optin.py#home_at` reads first. `docs/layout/one-root-by-lifetime.md:91-93`
states it, and a repository that opted out has no root, so no hook prints
the core there. That is judged no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD, which `gaps.md` labels `unverified`; the label is honest, since no party has run them | `seal/threads/1795390622-the-root-places-omit-agentic-seal/gaps.md:7` | the orchestrator, at the broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_no_document_names_the_old_roots.py tests/behaviour/test_first_setup_asks_once.py tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/text/test_the_settings_have_a_front_door.py tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_a_phase_hands_the_next_one_a_record.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py tests/text/test_the_records_can_be_carried_out_and_in.py -q` | exit 0, 329 passed, 5 warnings, none of them about a file this diff changes |
| `diff seal/README.md templates/setup/seal-README.md` | no output, exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline 641b6bfb5 --root . --worktree`, before this record was written | exit 0; no record under `trail/rounds/`, no `trail/gate.md` and no `guarantee.md` named, and no notice at a line of `frame/design.md` |
| the same command, with this record written | exit 0; each of the four findings named as open for having no close block, which the fix pass appends, and nothing else refused in the record |
