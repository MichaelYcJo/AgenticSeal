# Review round 1: 1793787547-each-statement-is-corrected-to-the-tree

```seal
target: 7b9d7cbec against release/v0.31.2
```

This round reviews the branch at 7b9d7cbec against `origin/release/v0.31.2`,
which is 347853106. No earlier round exists, so no fact is carried, and every
fact below was opened this round. The repository declares no
`seal/parity.md` (`git ls-files seal/parity.md`, executed, no output), so no
`original:` line is owed. `seal/config.md` has no `Record language` row, so
this record is English. The runs took place in a `git clone --no-local` at
7b9d7cbec in the session scratchpad, which has since been removed.

Stage 1 read the diff against the bodies of #1346, #1338 and the ten issues
#1346 lists (`gh issue view <N> --json title,body`, executed). It also read
`frame/design.md`, `frame/plan.md`, `frame/questions.md`, the four phase
records, `gaps.md` and `changelog.md`. Stage 2 read each changed sentence
against the code or the file it names. The axes that apply to a diff of
prose are these: whether each claim holds at HEAD, whether a citation reaches
what it cites, the class of each corrected fact across the tree (contract
rules 12 and 19), and what the diff removes against `## Removes`. Inputs,
authorization, concurrency and security do not apply. Only
`evals/scripts/rule_cases.py#routing` changes a signature, and its one
caller passes the new argument (`evals/scripts/rule_cases.py:203-205`,
read).

Out of this round, as the spawn names: #1343, and the commit-gate sentences
under `tests/` that phase 3 lists in `gaps.md` *Not done*.

## Findings

### 1. The rewritten docstring's first line says no other file restates the rules, and the cases hold only the listed carriers

```seal
severity: should
location: `tests/text/test_the_rules_claude_md_names_have_one_home.py:1-2`
evidence: read `tests/text/test_the_rules_claude_md_names_have_one_home.py:1-2`, `tests/text/test_the_rules_claude_md_names_have_one_home.py:35-49`, `tests/text/test_the_rules_claude_md_names_have_one_home.py:153-165`, `tests/text/test_the_rules_claude_md_names_have_one_home.py:192-203`
```

Why it matters: #1335's *Done when* asks that the docstring state what the
module's cases hold at the commit that changes it. The first line now reads
"The rules `CLAUDE.md` once named have one home each, and no other file
restates them (#730)." `restated` checks only the eleven files in
`CARRIERS` (`:153-165`, `:192-203`). It looks only for each home's needles,
the sentences only the home writes. The docstring's own later paragraphs
say both things: "No carrier contains a needle" (`:37`), and "a carrier can
state a rule in its own words, with none of the home's needles" (`:44-45`).
So the first line claims a tree-wide absence that the cases do not hold, and
the paragraph below it contradicts the line. A file outside `CARRIERS` that
pastes a needle passes every case. This is the kind of statement the
work item exists to correct, in the docstring S4 rewrote. The changelog
bullet for #1335 already says "no carrier repeats it", which is right, so
the fragment needs no change.

```python
"""The rules `CLAUDE.md` once named have one home each, and no carrier this
module lists restates a home's own sentences (#730).
```

```seal
verdict: fixed cc3c83283
answer: The first line now reads "no carrier this module lists restates a home's own sentences", the paste-ready text, applied after reading it against `restated` and `CARRIERS`, which hold only that. The changelog bullet for #1335 already says "no carrier repeats it" and stays.
```

### 2. Three other places still say an absent `config.md` row has a default, the claim S1 removed from the README

```seal
severity: should
location: `docs/layout/one-root-by-lifetime.md:204-207`, `docs/layout/one-root-by-lifetime.ko.md:195-198`, `hooks/lib/config.py:4-8`
evidence: executed `git grep -n -E "absent row (has|takes|gets|means) (a|the) default|default .*absent row|no row (means|is) the default" -- ':!seal/threads' ':!evals/behaviour'`, `git grep -n -E "absent row has a default|exception that proves|행이 없을 때의 기본값" -- tests` (no output); read `templates/setup/config.md:11-29`
```

Why it matters: S1 removed the README entry's "no file and no row both mean
the default". `templates/setup/config.md:11-29` contradicts that sentence
for two items: `Mode` has no default, and an absent `Broad gate` is "a
refusal, not a prompt". Phase 1 searched for other statements of the
corrected claim by its old spellings and called the search a sample
(`trail/phases/phase-1.md`, *Other places that state the two corrected
claims*). This round's search, worded differently, found the same claim in
three places that phase 1's spellings did not reach:

- `docs/layout/one-root-by-lifetime.md:206-207`: "an absent row has a
  default that is stated there". The Korean edition says the same at
  `:197-198`. This is a policy document that agents and people read to learn
  what the repository decides for itself.
- `hooks/lib/config.py:4-8`: "every absent row has a default", with `Mode`
  as "the exception that proves it". `Broad gate` is a second exception, and
  the docstring does not name it.

No case pins any of the three sentences, because the second search printed
nothing. Contract rule 19 asks that a change remove every statement of the
old fact, at least those `git grep` finds on its words. Each fix below
states only what the template states. Where the fix pass judges these
sentences outside #1334's scope, the answer is a `deferred` close naming
where they go. Editing them in this branch also owes the `changelog.md`
bullet for #1334 a clause (`docs/layout/the-record-layout.md` *A commit
after the build brings its changelog fragment along*).

```markdown
`seal/config.md` is the one file a repository writes about itself, one row
per item, read by the checkers and editable by hand. The rows that exist are
documented in `templates/setup/config.md`, which also states what an absent
row means, rather than leaving it to whoever reads the code.
```

```markdown
`seal/config.md` 는 저장소가 자기에 대해 적는 유일한 파일입니다. 항목마다 한
행이고, 검사기가 읽으며, 손으로 고칠 수 있습니다. 있는 행은
`templates/setup/config.md` 에 적혀 있고, 행이 없을 때 무엇을 뜻하는지도
코드를 읽는 사람에게 맡기지 않고 거기에 적혀 있습니다.
```

```python
`config.md` sits in the root `hooks/lib/optin.py` resolves, in the same shape as
`parity.md` -- a markdown table of `| Item | Value |`. Every row in it is
optional, and every absent row but two has a default, which is what every
repository got before that row existed. An absent `Broad gate` is the first
exception: `seal gate` names the row and runs nothing.

`Mode` is the second, and it is why this module exists. What
```

The last line of the Python snippet joins the paragraph that already
continues at `hooks/lib/config.py:8` ("every repository got before that row
was *the folder decides*").

```seal
verdict: fixed cc3c83283
answer: Both editions of `docs/layout/one-root-by-lifetime.md` take the paste-ready text. `hooks/lib/config.py`'s docstring is in my own words: "The file is optional, and every absent row but two has a default", then "An absent `Broad gate` is one exception: `seal gate` names the row and exits 2 with nothing run", which is `templates/setup/config.md:27-29` and `broad_gate.py#missing_row` raised as `Refused`; the paste-ready "Every row in it is optional" would contradict the template's two exceptions, and "runs nothing" left out the exit. The class search by wording found a fourth instance the finding does not list, `skills/config/SKILL.md:9-10`, "Every row has a default", which now names `Mode` and `Broad gate` as the two rows with no default and the table below as what each absent row means. The `changelog.md` bullet for #1334 names all four. `frame/design.md` *Out of scope* O2 lists `hooks/lib/config.py` as out for #1342; this edit is #1334's class and changes the docstring alone, which the hand-back names for the orchestrator.
```

### 3. The plugin-name check and its case still say a literal would be the second place the name is written

```seal
severity: should
location: `.github/scripts/plugin_directory_check.py:143-144`, `tests/github/test_plugin_directory_check.py:395-396`
evidence: executed `git grep -n -i -E "second place|one place the name|name is written|spells (the|its) name|the name lives|where the name" -- ':!seal/threads'`; read `.github/scripts/plugin_directory_check.py:140-150`, `tests/github/test_plugin_directory_check.py:394-405`, `docs/releasing/branch-and-release.md:200-205`
```

Why it matters: #1341's drifted fact is that `.claude-plugin/plugin.json`
holds the plugin's one name. S9 corrected the paragraph in
`docs/releasing/branch-and-release.md`, and the paragraph now makes no claim
about the other files that spell the name. Two docstrings state the same
fact in other words. `plugin_name` says "A literal here would be a second
place the name is written down" (`plugin_directory_check.py:143`), and its
case says "A literal would be a second place the name is written down"
(`test_plugin_directory_check.py:395`). "Second" presupposes that one place
holds the name today. `.claude-plugin/marketplace.json` and both READMEs'
install lines also spell it, which is what #1341 measured. Phase 4 called its
search for other statements a sample that matches the old wordings
(`gaps.md` *Not verified*, row 6), and these two lines are outside it. The
reason each docstring gives, that a literal is a copy that can drift, holds
without the count.

```python
    """This plugin's name, from its own manifest rather than a literal.

    A literal here would be one more place the name is written down, and the
```

```python
        """A literal would be one more place the name is written down, and the
```

```seal
verdict: fixed cc3c83283
answer: Both docstrings now say "one more place", the paste-ready text, applied after reading `plugin_name` and its case; the reason each gives, that a literal is a copy that can drift, stands without the count. The `changelog.md` bullet for #1341 names both.
```

### 4. The front-door module's docstring says three `config.md` rows exist, and `gaps.md` keeps it on the grounds that it names its moment

```seal
severity: should
location: `tests/text/test_the_settings_have_a_front_door.py:3-4`, `seal/threads/1793787547-each-statement-is-corrected-to-the-tree/gaps.md:17-26`
evidence: read `tests/text/test_the_settings_have_a_front_door.py:1-12`, `tests/text/test_the_settings_have_a_front_door.py:24-40`, `skills/config/SKILL.md:38-49`, `seal/threads/1793787547-each-statement-is-corrected-to-the-tree/gaps.md:17-26`
```

Why it matters: the spawn asked this round to judge whether the sentence
states the present. It does. "Issue #105. Three rows exist and the only way
to see them was to open a file nobody has a reason to open." "Three rows
exist" and "nobody has a reason" are in the present tense. "Issue #105." is
a citation before the sentence. It does not put the sentence in the past, and
only "was" is in the past tense. The module's own `ROWS` lists ten items
(`:24-40`), and `skills/config/SKILL.md:38-49` tables ten. So the sentence
is a count of `config.md`'s rows that the tree contradicts. That is #1334's
class, a sentence stating the file's items as a closed set.

#1334's *Done when* accepts such a sentence when it is "corrected or named".
`gaps.md` *Not done* names it, so the *Done when* holds. But the grounds
`gaps.md` gives for leaving it do not hold. It says the sentence "names its
moment, the kind of sentence `frame/design.md` *Out of scope* O2 keeps out
for #1344". A reader of the record is told that the sentence is history,
and it is not. The correction is one clause, and the PR ships the false
count without it. When the fix pass corrects the sentence, the `gaps.md`
paragraph at `:17-26` goes, and the `changelog.md` bullet for #1334 gains
the module.

```python
Issue #105. Three rows existed then, and the only way to see them was to open
a file nobody had a reason to open. The skill is instructions rather than a
```

```seal
verdict: fixed cc3c83283
answer: The sentence now reads "Three rows existed when this module was written (#113), and the only way to see them was to open a file nobody had a reason to open", in my own words. #105's body counts two rows "exist or are arriving", and the commit that added the module, b644a6c00 (#113), says three, so "then" after "Issue #105" would date the count to the wrong issue. The paragraph of `gaps.md` *Not done* that kept the sentence is gone, and the `changelog.md` bullet for #1334 names the module.
```

## Confirmations

What matched: S1 (#1334). The README entry lists no item and makes no claim
about an absent row. It names `templates/setup/config.md` in the plugin, and
contract rule 11 resolves that path to the plugin's root in a user's
repository (`templates/setup/seal-README.md:85-87`, read). The two copies
are identical (`cmp seal/README.md templates/setup/seal-README.md`, executed,
exit 0). The `ROW_READERS` entry for the README went with the file's only
`Record language`, and no other reader of the README asserts the removed
words (`git grep -n seal-README -- tests`, executed, and each case read).
The account claims this census is a sample, and it is one. This round
widened it: `git grep -l "Record language"` over the tracked markdown,
counting each file's item names, found no further closed list of the items
beyond those phase 1 lists (executed). The same search found the absent-row
statements of finding 2 and, by reading, the count of finding 4.

What matched: S2 (#1342). The comment says no hook or command of the plugin
asks for the row. `git grep` for the row's name over `hooks`, `bin`,
`skills`, `*.py` and `*.sh` outside `tests/` lists only the skills' prose
(executed). The cases of the module parse the row through
`hooks/lib/config.py#config_rows` (`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:369`,
`hooks/lib/config.py:351`, read).

What matched: S3 (#1336). The generator at 7b9d7cbec, run in the clone,
exits 0 and leaves `git status --porcelain` empty, so the 17 cases are its
output byte for byte. `git grep` for the three old forms under `evals/`
prints nothing (both executed). Each record the generator writes opens with
its template's title, including the plan, the phase record and the closing
memo, which were already right. Each heading it writes is the template's
(`evals/scripts/rule_cases.py:132-160`, `:265-272`, `:766-815`, against
`templates/records/*.md`, read). The gate record's title is
`broad_gate.py#write_gate_file`'s own, `# {name} — broad gate`
(`skills/verify/scripts/broad_gate.py:2502`, read). `RECORD_LINES` holds the
heading in its new spelling, and its comment no longer says the heading
lacks ` *(mandatory)*`.

What matched: S4 (#1335) apart from finding 1. The docstring names no
`CLAUDE.md` row as standing and no removed module. The comment above
`LINKED` gives #940, #1169 and #1177 as the issues that took the rows out
(`:137-143`, read). The sentence on `LINKED` matches `unlinked`, which holds
each linked file to the home's path and section (`:206-215`, read). The
module keeps its name, as *Alternatives considered* A8 and A9 decide. The
claim that `git diff` touches the docstring alone holds
(`git diff origin/release/v0.31.2...HEAD -- tests/text/test_the_rules_claude_md_names_have_one_home.py`,
executed).

What matched: S5 (#1344). Each of the eleven statements now cites what HEAD
holds, cites a commit, or drops the citation, as phase 3 lists them. Each
cited commit is on `origin/main` and holds the cited file and name.
`f975ea66a` is the parent of 5b1f6faea, and its two modules hold
`_derives_a_path_list` at `:1277` and
`test_no_document_describes_the_lenient_reader_alone` at `:398`.
`cdfdfedd8` is the parent of 8350c5788, and
`tests/test_handoff_outlives_the_merge.py` holds
`test_the_documents_that_instruct_never_name_the_old_directory` at `:174`
(executed: `git branch -r --contains`, `git rev-parse`, `git show | grep -n`).
`tests/hooks/test_routing_edit_gate.py` pins root resolution, both shared and
local (`:189`, `:307-314`, `:375-377`, read). The induced `os.path.relpath`
raise that the new `test_question_gate.py` docstring names is the case's
monkeypatch (`tests/hooks/test_question_gate.py:376-379`, read). The
dropped clause in `test_review_axes.py` was false, because the tree's
`skills/core/SKILL.md` names neither the section nor "routing question"
(`git grep`, executed, exit 1). The account claims that both censuses miss a
module cited by its old path while its basename stands. This round ran that
census: every `tests/…py` or `evals/…py` path that a `tests/*.py` file cites
and HEAD lacks, intersected with the paths `git log --diff-filter=D` lists.
It gives 32 lines, and no path among them has its basename standing
elsewhere. Each of the 32 is a citation at a commit, or a sentence naming
its moment ("The cases come from … (#942's phase 6)"), or an S5 statement
(executed, and each line read). So the account's own gap holds no instance
at HEAD.

What matched: S6 (#1337). `aa687d357` is the parent of f51e634d2 and is on
`origin/main`. Its `spec.md` holds *The sharp question — where an untracked
declaration lands* at line 43, and the section states the row's argument
about answer B (`git show aa687d357:… | sed -n 43,75p`, executed). The
table under *Schedulable items with nowhere else to go* has no blank line
between its rows (`sed -n 36,50p seal/follow-up.md`, executed).

What matched: S7 to S11. The template's comment cites the section and lists
none of its items (`.github/PULL_REQUEST_TEMPLATE.md:29-32`, read).
`floor_syntax` refuses through `newer_than`, which parses with
`feature_version` and flags `zip(..., strict=...)` and `datetime.UTC`, and
`test_launch.py`'s case says it holds the set to the table
(`tests/censuses.py:776-798`, `:823-842`, `tests/hooks/test_launch.py:203-214`,
read). `plugin_name` reads `.claude-plugin/plugin.json`
(`.github/scripts/plugin_directory_check.py:140-150`, read). The Results
table holds four marketplace-clone runs in both editions, and both now count
four (read). `gh label list` lists `hooks-gates` (executed).

What matched: the version move and the fragment. `.claude-plugin/plugin.json`
moves from `0.31.1`, which the base holds, to `0.31.2`. No other tracked
file holds `0.31.1` (`git grep -F`, executed). This is the release's first
pull request, which `docs/releasing/branch-and-release.md:248-250` says moves
the version. No template for `changelog.md` exists, and the fragment follows
the shape of the fragments on `main`: one heading, and one bold-led bullet
per issue (`git show a2deb4e04`, `git show 0cb6014d1`, read). It carries no
`### Process changes` table, and the diff touches none of the files that
`docs/layout/the-record-layout.md:52` names (read).

What matched: `## Removes` against the diff. Each of the six rows is a
removal in the diff. Every other removal is a citation that S5 or S4 drops,
and its phase record names each one. The diff adds no test, check, hook or
rule (A12, read).

The diff leaves one comment line at 101 columns in a block that wraps at
78: `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:39`
(executed: `awk` over the line lengths). It tells nobody anything wrong, so
it is no finding. The fix pass may rewrap it when it next touches the
module.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD; the suite is `unverified` | `seal/config.md` *Broad gate* | the orchestrator, at the broad gate after the rounds settle |
| The pull request body names the paid runs that #1107, #1178 and #1266 wait on as grading the changed cases (#1336 *Done when*), and names the census method (#1344 *Done when*) | the pull request body, not yet written | the orchestrator, then the sealer |
| How the agents under test behave on the 17 regenerated cases | `evals/behaviour/` | the paid runs #1107, #1178 and #1266 wait on |
| Whether a contributor opens `CONTRIBUTING.md` *What a change to a gate must carry* from the template's citation | `.github/PULL_REQUEST_TEMPLATE.md:29-32` | the repository owner; it can be read and not measured |

## Probes

| Command | Result |
|---|---|
| `python3 evals/scripts/rule_cases.py` then `git status --porcelain`, in the clone at 7b9d7cbec | exit 0, nothing changed |
| `git grep -n -E 'Feature Specification\|— review round 1\|^# routing$' -- evals/` | no output, exit 1 |
| the census by path: `git grep -n -o -E '(tests\|evals)/[A-Za-z0-9_/]+\.py' -- 'tests/*.py'`, kept where HEAD lacks the path, intersected with `git log --diff-filter=D --name-only -- 'tests/*.py' 'evals/*.py'` | 307 cited paths absent at HEAD, 32 of them removed modules; none has its basename elsewhere in the tree |
| `bin/test` over the 13 changed test modules with `test_evals_layout.py`, `test_rule_cases.py`, `test_a_rider_reaches_its_file.py` and `test_a_cited_commit_outlives_the_squash.py`, `-q`, in the clone | 326 passed, exit 0 |
| `gh label list --limit 200 --json name --jq '.[].name' \| grep -x hooks-gates` | `hooks-gates`, exit 0 |
