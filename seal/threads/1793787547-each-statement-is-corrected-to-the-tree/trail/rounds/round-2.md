# Review round 2: 1793787547-each-statement-is-corrected-to-the-tree

```seal
target: 35e0c9af1, fixes a51f146a8..35e0c9af1
```

This verifying round reads the diff of round 1's fix pass,
`a51f146a8..35e0c9af1`: cc3c83283 (the fix), 485ce553e (a `gaps.md` row),
92498f713 (the four close blocks) and 35e0c9af1 (the orchestrator's fold of
`frame/design.md` *Out of scope* O2 and a row of `frame/plan.md`
*Judgments of the run*). The runs took place in a `git clone --no-local` at
35e0c9af1 in the session scratchpad, which has since been removed. The
repository declares no `seal/parity.md`, as round 1 found, so no `original:`
line is owed. `seal/config.md` has no `Record language` row, so this record
is English.

Carried from round 1, not re-established: the S1 to S11 confirmations, which
stand outside the fix diff; the census of `config.md`'s items over the
tracked markdown; and the path census of S5. Re-derived this round: every
verdict below, and each coordinate the fix diff touches, opened at
35e0c9af1. The close blocks, the commit messages, the spawn prompt and the
`gaps.md` row are the fix pass's account. Each claim in them was opened in
the tree, and the confirmations say what was claimed and what was found.

The axes for a diff of prose are these: whether each changed sentence holds
at 35e0c9af1, whether a citation reaches what it cites, and the reach of the
fix over its closed set (contract rule 12): its own diff, and each file of
the work item's directory that states the present. Inputs, authorization,
concurrency and security do not apply, because the diff changes no code,
only docstrings, documents and records (`git diff a51f146a8..35e0c9af1`,
executed, read whole).

## Findings

### 1. The frame still says the work item edits two `docs/` sentences directly, and the fix pass edited a third

```seal
severity: should
location: `seal/threads/1793787547-each-statement-is-corrected-to-the-tree/frame/design.md:258`, `seal/threads/1793787547-each-statement-is-corrected-to-the-tree/frame/design.md:24`
evidence: executed `git diff --stat origin/release/v0.31.2...35e0c9af1 -- docs`, `git diff a51f146a8..35e0c9af1 -- docs`, an `awk` over the `## Rule changes` section of every `frame/design.md` under `seal/threads/` for `one-root-by-lifetime`; read `seal/threads/1793787547-each-statement-is-corrected-to-the-tree/frame/design.md:24`, `seal/threads/1793787547-each-statement-is-corrected-to-the-tree/frame/design.md:255-258`, `docs/layout/one-root-by-lifetime.md:202-207`
regression: round-1#2
```

Why it matters: the unit is the direct edit of
`docs/layout/one-root-by-lifetime.md:206-207` and its Korean edition at
`:197-198`, which cc3c83283 made for finding 2. The frame's `## Rule
changes` block says this work item edits two `docs/` sentences directly,
the one in `docs/releasing/branch-and-release.md` and the one in the
copy-in-force experiment. The fix pass edited a third `docs/` sentence
directly, and the orchestrator's fold at 35e0c9af1 folded *Out of scope* O2
but did not fold the `why:` line or the *Grounding* row that make the same
count.

At 35e0c9af1 the branch changes five files under `docs/`: both editions of
the experiment, `docs/releasing/branch-and-release.md`, and both editions of
`docs/layout/one-root-by-lifetime.md` (executed). The `why:` at `:258` reads
"Its two `docs/` sentences, in `docs/releasing/branch-and-release.md` and
the copy-in-force experiment, state facts of the tree and a count, so it
edits them directly in its pull request". The *Grounding* row at `:24` says
the same: "It edits `docs/releasing/branch-and-release.md` and the
experiment document under `docs/experiments/` directly in its pull
request".

The direct edit itself is licensed. `skills/implement/SKILL.md` *Document
layout — two roots, three lifetimes* lets a work item whose subject is the
documents' text edit the policy root directly, and this item's subject is
that. No unsettled design's `## Rule changes` names
`docs/layout/one-root-by-lifetime.md` (executed, no output), so nothing
needs re-pointing. What is wrong is the frame's count. The sealer reads
every party's account against the tree, and this frame's account of which
policy documents the pull request edits directly leaves one out. That is a
count stating a closed set that the tree contradicts, the class this work
item corrects.

The fix pass's class account in `gaps.md` names its searches by wording as
a sample, and that holds for the open class across the tree. The work
item's own directory is a closed set, though (contract rule 12), and the
`why:` line and the *Grounding* row are two statements in it that the
account missed.

The snippet below covers both statements. No other line of the frame
counts the `docs/` edits: *Scope* S9 and S10 name their own sentences, and
the plan row at `frame/plan.md:107` names `skills/config/SKILL.md` and no
`docs/` file.

```markdown
  why: This work item corrects statements of documents, templates, a config comment and test docstrings to the tree, and no rule says anything different afterwards. Its three `docs/` sentences, in `docs/releasing/branch-and-release.md`, the copy-in-force experiment and `docs/layout/one-root-by-lifetime.md` *What the repository decides for itself, and how it is read*, state facts of the tree and a count, so it edits them directly in its pull request under `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*. No section moves, so no unsettled design's operation is re-pointed.
```

In the *Grounding* row at `:24`, the third cell's third sentence becomes:

```markdown
It edits `docs/releasing/branch-and-release.md`, the experiment document under `docs/experiments/` and, from round 1's fix pass, `docs/layout/one-root-by-lifetime.md` directly in its pull request, as 1793750411 and 1793756609 did for their `docs/` text (read: their `## Rule changes`).
```

```seal
verdict: fixed baebc9ef8
answer: The finding is located in `frame/design.md`, which the crafter does not write, so the orchestrator folded it, as `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* gives the frame's statements to the orchestrator. Both statements take the round's paste-ready text: the `why:` line of `## Rule changes` and the third sentence of the *Grounding* row now count three `docs/` sentences. The commit touches the work item's records alone, so the sealer is this fix's reader.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the fix pass claimed it applied the paste-ready first line. The
docstring of `tests/text/test_the_rules_claude_md_names_have_one_home.py:1-2`
now reads "no carrier this module lists restates a home's own sentences"
(read). The diff of cc3c83283 touches those two lines and nothing else in
the module, so `restated` and `CARRIERS` are unchanged and the line states
what they hold (`git diff a51f146a8..35e0c9af1`, executed). The module
passes (`bin/test`, executed, in the narrow run below).

```seal
confirms: round-1#2
```
What holds: the fix pass claimed both editions of
`docs/layout/one-root-by-lifetime.md` take the paste-ready text, and they do
(`docs/layout/one-root-by-lifetime.md:206-207`,
`docs/layout/one-root-by-lifetime.ko.md:197-198`, read). It claimed its own
wording for `hooks/lib/config.py:4-9`, on the grounds that round 1's "Every
row in it is optional" contradicts the template's two exceptions. That
ground holds: `templates/setup/config.md:11-12` says the file is optional
and an absent row is not an error "with two exceptions: `Mode` and `Broad
gate`" (read). The new docstring says what the template says. "The file is
optional, and every absent row but two has a default" matches `:11-14`.
"`seal gate` names the row and exits 2 with nothing run" matches `:26-28`
and the code: `broad_gate.py` raises `Refused(missing_row(home))` when the
command is absent (`skills/verify/scripts/broad_gate.py:2956-2957`, read),
and `main` returns 2 on `Refused` (`:3165-3167`, read). "`Mode` is the
other" leads into the paragraph that already said an absent `Mode` has no
default (`hooks/lib/config.py:9-12`, read). No line of `tests/` or the tree
outside the records still says every row or every absent row has a default
(`git grep -n -i -E "row has a default|absent row is not an error|every absent row|absent row has"`,
executed: only the new docstring's "every absent row but two", the
template's own sentence and the records). The one exception is the frame's
count of `docs/` edits, which is finding 1.

```seal
confirms: round-1#3
```
What holds: both docstrings say "one more place" instead of "a second
place" (`.github/scripts/plugin_directory_check.py:143`,
`tests/github/test_plugin_directory_check.py:395`, read), as the fix pass
claimed. The diff touches only those two lines. Both modules pass ruff
check and ruff format (`uvx ruff check`, `uvx ruff format --check` on the
five changed Python files, executed, exit 0 each). The test module passes
(`bin/test`, executed, in the narrow run).

```seal
confirms: round-1#4
```
What holds: the fix pass claimed its own wording, "Three rows existed when
this module was written (#113)", on the grounds that #105 counts two rows and
the commit that added the module counts three. Both grounds hold. #105's
body reads "Two rows exist or are arriving" (`gh issue view 105`,
executed). The module's first commit is b644a6c00
(`git log --follow --diff-filter=A`, executed), and its subject says "three
rows decide what a repository does with nothing to show them (#113)"
(read). #113 is a closed pull request (`gh api .../issues/113`, executed).
The paragraph of `gaps.md` *Not done* that kept the sentence is gone (read).
The `changelog.md` bullet for #1334 names the module and says three rows
existed when it was written (read).

What matched: the fix pass's new unit `skills/config/SKILL.md:9-11`, the
fourth instance its search found. The sentence "Every row but `Mode` and
`Broad gate` has a default, and the table below says what each absent row
means" agrees with `templates/setup/config.md:11-14`. It also agrees with
the skill's own table at `:39-50`, whose `Mode` cell is "*the folder
decides*" and whose `Broad gate` cell is "*none: `seal gate` refuses
without it*", and with the paragraph at `:52-56` (read). The modules that
read the skill pass: `tests/text/test_the_settings_have_a_front_door.py`,
`tests/text/test_the_mode_is_a_row_and_a_command.py` and
`tests/text/test_no_passage_is_pasted_into_a_second_file.py` (executed, in
the narrow run).

What matched: the `changelog.md` bullets for #1334 and #1341. The new
sentences name the four places and the two docstrings that cc3c83283
changes, and each says what the place now states (read against the diff).

What matched: the `gaps.md` row 485ce553e adds. It says the fix pass's
searches match spellings and are a sample, and that it found and corrected
`skills/config/SKILL.md`. Both hold (read). The class across the tree is
open, so the sample is the account's, and what it did not reach is not this
round's share (contract rule 12).

What matched: the orchestrator's fold at 35e0c9af1. O2 now keeps only
`hooks/lib/config.py`'s code out for #1342 and says round 1's fix pass
corrected the module docstring as #1334's class. #1342's body puts
`hooks/lib/config.py` out of #1342's scope (`gh issue view 1342`,
executed), and #1334's *Done when* reaches every sentence that states the
file's items as a closed set. So the docstring edit is #1334's, and the
fold says so. The fix diff changes `hooks/lib/config.py` only in lines 1-12
of its docstring (executed). The new row of *Judgments of the run* cites
`skills/implement/orchestration.md` *Orchestrator: drain the rows before
the broad run, and keep the records*, first row, and that row stands at
`skills/implement/orchestration.md:465` (read). Its claim that each fix
changes no assertion holds: no line the diff changes is code (executed).

The fix leaves one docstring line at 114 columns where the block wraps at
78: `tests/text/test_the_settings_have_a_front_door.py:7` (executed: `awk`
over the line lengths). Ruff does not select E501 here (`ruff.toml:56`,
read), and the line tells nobody anything wrong, so it is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD; the suite is `unverified` | `seal/config.md` *Broad gate* | the orchestrator, at the broad gate after the rounds settle |
| The part of the classes of round 1's findings 2, 3 and 4 across the tree that the fix pass's wording searches did not reach; each class is open | `gaps.md` *Not verified*, the row for round 1's fix pass | the fix pass's account names it as a sample; the orchestrator decides whether it needs a home |

## Probes

| Command | Result |
|---|---|
| `bin/test` over `tests/text/test_the_settings_have_a_front_door.py`, `tests/text/test_the_rules_claude_md_names_have_one_home.py`, `tests/github/test_plugin_directory_check.py`, `tests/hooks/test_config.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/text/test_the_mode_is_a_row_and_a_command.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/text/test_the_rules_have_one_owner.py` and `tests/text/test_a_document_has_room_for_the_next_fold.py`, `-q`, in the clone at 35e0c9af1 | 374 passed, exit 0 |
| `bin/test tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_first_setup_asks_once.py -q`, in the clone | 89 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` on the five Python files the fix changes | exit 0 each |
| `git grep -n -i -E "row has a default\|absent row is not an error\|every absent row\|absent row has"` | `hooks/lib/config.py:5`, `templates/setup/config.md:11` and lines of this work item's records; nothing else |
| `awk` over the `## Rule changes` section of each `seal/threads/*/frame/design.md`, matching `one-root-by-lifetime\|skills/config` | no output |
