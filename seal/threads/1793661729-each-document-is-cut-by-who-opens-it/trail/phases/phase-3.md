# Phase 3: 1793661729-each-document-is-cut-by-who-opens-it

## What this phase found

**The frame holds for this phase.** It was read against the tree at
cb98bb899 before the first edit (read). `skills/settle/SKILL.md` held every
section D5's first row names, at the headings it names. The three
citations of moved `settle` sections in `docs/` were `docs/README.md:6` and
`docs/the-reader-registry.md:12`, both *Rule changes*, and
`docs/the-record-layout.md:242`, *In local mode*. Each is re-pointed in
148e08b6d.

**What moved where.** `skills/settle/rule-changes.md` holds *Rule changes*,
*A rule has one shape* and *The index*. `skills/settle/local-mode.md`
holds *In local mode*, `skills/settle/draft.md` holds *What `--draft`
writes*, and `skills/settle/named-directories.md` holds the rest of
*Directories a person names*. Each file opens with a title in the shape the
plugin's other supporting files use, such as
`skills/implement/bootstrap.md`, and one sentence naming who opens it and
at which step. `SKILL.md` names each file at its step: the grammar in the
first paragraph, local mode where the intro sends a local root, the named
directories at the end of its own *Directories a person names*, and the
draft in step 4 of the procedure.

**Two decisions on what stays.**

- *Directories a person names* keeps its lead paragraph in `SKILL.md`
  beside the first question. D5 keeps "the first question" and moves "the
  rest". The lead says why the settle asks the first question at all, and
  every settle asks it at step 1. So the section's heading stands in both
  files: `SKILL.md` holds the lead, the first question and the pointer,
  and `named-directories.md` holds the rest under the same heading. Judged
  against D5's *Read by, at which step* cell.
- *A released work item with no `frame/design.md`* stays in `SKILL.md`. D5
  names it in neither column. It is four lines that `--apply` and the dry
  run act on at every settle.

**A departure: path-less cross-references in the moved text now carry a
path.** D7 gives phase 5 this rule for the policy root. The same case arose
here: a moved section named a section that now stands in another file. The
cases were *Rule changes* above, *The index*, *What `--apply` does* twice
and *What the dry run shows*. Each now names the file before the italics.
"Above" went with the first, since the section is no longer above. The
moved text is otherwise unchanged. The comparison below shows it. Judged
against D7's last bullet and S7, which allow exactly these differences.

**A departure: two readers of a skill's files read the files beside
`SKILL.md`.** Neither the frame nor the plan names them. Both were found
by listing the globs over `skills/` that the moved text would leave
(`git grep` for `skills/*/SKILL.md` and `"*", "SKILL.md"` over `tests/`,
`.github/`, `hooks/`, `bin/` and the scripts, executed). The list is a
sample by that method: a reader naming one file by literal path, such as
`tests/behaviour/test_docs_line_wrap.py#COVERED`, is not in it.

- `.github/scripts/rules.py#RULE_FILES` read `skills/*/SKILL.md` and
  `skills/*/orchestration.md`. *The index* ends with `check:
  tests/skills/test_fold_check.py`, so the move would leave that line
  unread by `seal rules --check`, with nothing refusing it. The two globs
  became `skills/*/*.md` in 8f18e72df, which also reads `acts.md`,
  `bootstrap.md`, `multi-repository.md` and
  `skills/writing-style/outside-the-review.md`. None of them holds a line
  that opens like a check line (`git grep`, executed).
- `tests/text/test_the_record_is_written_in_words.py#CORPUS` read every
  `skills/*/SKILL.md` for an emoji or a proof block. A framer reads
  `rule-changes.md` as instruction, so the census now reads
  `skills/*/*.md`. Every file it adds was clean at 8f18e72df (executed).

Judged against contract rule 19, which has a change remove or correct what
stood on the old fact in the same commit.

**S3, read.** `agents/framer.md` *A design states its rule changes* cites
`skills/settle/rule-changes.md` *Rule changes*. That file holds *Rule
changes*, *A rule has one shape* and *The index*, and nothing else a
settle needs: no step of the procedure, no dry run and no `--apply`. The
cited-section case resolves the citation (executed, below).

**The ceiling sentence.** It now reads "split by who opens each section and
at which step". It names no source. Phase 6 writes the core's rule, and a
citation of it here would name a section that is not there until then.
`fold_check.py`'s module docstring and `#past_ceiling_lines`' message say
the same. The message's pins in `tests/skills/test_fold_check.py` and
`tests/skills/test_settle.py` changed in a5b6a06eb, and so did the skill's
pin in `tests/text/test_a_document_has_room_for_the_next_fold.py`.
`git grep -n -i -e "own headings" -e "by topic"` outside `seal/` and
`CHANGELOG.md` then listed only `skills/settle/named-directories.md:37`,
"the document's own headings decide nothing", a different rule (executed).

**The old citations, as D7 asks (executed at 148e08b6d).** First, the
citation sites at cb98bb899:

```
$ git grep -n "settle/SKILL.md" -- ':!seal/'
```

It listed 27 files, the moved sections' citations among them. A one-line
search misses a citation wrapped across lines, so the check after the move
read every tracked file outside `seal/` whole. A read-only `python3` over
`git ls-files -z` matched each file's text against

```
settle/SKILL\.md`(?:'s)?\s+\*(Rule\s+changes|A\s+rule\s+has\s+one\s+shape|The\s+index|In\s+local\s+mode|What\s+`--draft`\s+writes)\*
```

and printed nothing, exit 0. A citation of *Directories a person names*
stays valid in `SKILL.md`, which keeps that heading.

**The moved text against its old text (executed).** Each section was cut
out of `git show 8f18e72df:skills/settle/SKILL.md` and out of its new file
with one `awk` from its heading to the next `## `, and the two were put
through `diff`. *Rule changes* and *A rule has one shape* gave no
difference. *The index*, *What `--draft` writes* and *In local mode* lost
only the blank line that ended them, since each now ends its file. The
other differences are the re-pointed cross-references above:

```
=== draft.md ## What `--draft` writes
< in the working tree, where *Rule changes* above places its kind. The designs
> in the working tree, where `skills/settle/rule-changes.md` *Rule changes*
> places its kind. The designs
=== local-mode.md ## In local mode
<   would remove gets as far as a version tag (*What `--apply` does*).
>   would remove gets as far as a version tag (`skills/settle/SKILL.md` *What
>   `--apply` does*).
<   that holds a row, with the exit codes *What `--apply` does* states. It
>   that holds a row, with the exit codes `skills/settle/SKILL.md` *What
>   `--apply` does* states. It
<   it is absent (*The index*).
>   it is absent (`skills/settle/rule-changes.md` *The index*).
=== named-directories.md ## Directories a person names
< about one file, as *What the dry run shows* gives them: its path, its two
> about one file, as `skills/settle/SKILL.md` *What the dry run shows* gives
> them: its path, its two
< - **The place** is named as an operation of *Rule changes* names one: a
<   `file` picked from the index (*The index*) and a `section`. It names an
> - **The place** is named as an operation of `skills/settle/rule-changes.md`
>   *Rule changes* names one: a `file` picked from the index
>   (`skills/settle/rule-changes.md` *The index*) and a `section`. It names an
< by its repository path, as the paragraph on reference roots under *What
< `--apply` does* asks of a statement a settle writes.
> by its repository path, as the paragraph on reference roots under
> `skills/settle/SKILL.md` *What `--apply` does* asks of a statement a settle
> writes.
```

The *Directories a person names* diff also lists the lead and the
first-question paragraphs as absent from the new file, because they stayed
in `SKILL.md`.

**Bytes (executed, `wc -c`).** `skills/settle/SKILL.md` was 43,620 bytes and
729 lines at cb98bb899. At a5b6a06eb it is 26,511 bytes and 444 lines.
`rule-changes.md` is 7,383 bytes, `local-mode.md` 4,483,
`named-directories.md` 4,408 and `draft.md` 2,939. A framer that follows
its citation opens 7,383 bytes where it opened 43,620.

**Mutation (executed),** each `seal mutate <file> --replace … --tests
"bin/test -q -p no:xdist <module> -k <cases>"`:

| Unit | Mutation | Verdict |
|---|---|---|
| `rules.py#RULE_FILES` | `skills/*/*.md` back to `skills/*/SKILL.md` | red: `test_a_check_line_in_a_skills_supporting_file_is_read` |
| `fold_check.py#past_ceiling_lines` | the old message back | red: the fold's and the settle's ceiling cases |
| `skills/settle/SKILL.md`, the ceiling sentence | the old sentence back | red: `test_settle_owns_the_placement_rule` |
| `test_the_record_is_written_in_words.py#CORPUS` | an emoji planted in `rule-changes.md`'s title | red: the emoji census |
| the cited-section case over the new files | `rule-changes.md`'s `## The index` renamed | red: `local-mode.md:63` and `named-directories.md:34` dangle |

The new case in `tests/github/test_rules.py` was also seen red before the
glob changed: "seal rules: all 0 check lines in 0 rule files hold", exit 0
where 1 was asserted (executed). The section moves add no behaviour, so no
case was written for them. The cases that already read them, re-pointed in
148e08b6d, are their proof: the cited-section case,
`test_settle_applies_rule_changes_in_place.py`,
`test_the_rules_command_reads_each_rule_off_its_test.py` and the
local-mode case in `tests/text/test_settle_reads_before_it_removes.py`.

**Narrow runs (executed).** The phase-boundary set is the test modules that
name, import or walk a path this phase changed. One `git grep -l` over
`tests/*.py` and `tests/**/*.py` listed them, with the changed files' names,
`ls-files`, `os.walk`, `rglob`, `glob(`, `RULE_FILES` and `agents` as the
pattern: 107 modules. At 148e08b6d, `bin/test -q` over the 107 gave 5101
passed and 12 skipped.

**For the next phases.**

- `agents/framer.md` changed in 148e08b6d. `docs/the-record-layout.md`
  has a work item whose diff changes an `agents/*.md` file end its
  `changelog.md` with `### Process changes`, so the changelog phase names
  it.
- Phase 4 cuts `skills/implement/SKILL.md` and `skills/verify/SKILL.md`.
  `seal rules --check` and the emoji census already read every `.md` beside
  a `SKILL.md`, so a section moved there keeps its check line read.
  `tests/behaviour/test_docs_line_wrap.py#COVERED` names its files one by
  one, and each new file goes in by name.
- Phase 6 writes the core's rule. The ceiling sentence in `SKILL.md` and
  the fold's message state the same rule, and name no source.
