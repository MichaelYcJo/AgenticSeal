# settle, the rule-change grammar

Whoever writes or reviews a design's `## Rule changes` opens this file, and
so does the settling session before step 4 of `skills/settle/SKILL.md` *The
settling session's procedure*, where it reads each group's operations. It
holds the grammar of an operation, the shape of a rule and its check line,
and the index each `file:` is picked from.

## Rule changes

A work item whose subject is the code states the rules it changes in its
design's `## Rule changes` section, one item per operation; which work item
edits the policy root directly instead is `skills/implement/SKILL.md`
*Document layout — two roots, three lifetimes*'s. The operation's line
comes first, then one field per line, indented two spaces:

```
- change
  file: docs/forms/the-round-record.md
  section: The round record
  from: the sentence as it reads now.
  to: the sentence as it will read.
```

| Operation | Fields | What it says |
|---|---|---|
| `add` | `file`, `to`; `section` optional | `to` belongs at the end of the section's own text, before its first sub-heading. A `to` that is one table row belongs as the last row of the last table in that text. With no `section`, `to` is a new document, `file` |
| `change` | `file`, `section`, `from`, `to` | the text `from` quotes becomes `to` |
| `remove` | `file`, `section`; `from` optional | the text `from` quotes goes, or with no `from` the whole section, up to the next heading of its level or higher |
| `nothing` | `why` optional | changes no rule, and stands alone in the section |

- `file` is a `.md` file of the policy root, `seal/config.md`'s
  `Policy root` row (`docs` when absent), or of one of its groups:
  `<policy root>/<name>.md` or `<policy root>/<group>/<name>.md`, one group
  directory deep and no deeper, joined with `/` and holding no `\` or `:`,
  with no group named `.` or `..`. `section` is a heading's text at any
  level.
- **`from` is the text as the design's framer read it.** It locates the change
  for the settling session and for a reviewer, and it is not a
  precondition: a `from` the section no longer holds is history, and the dry
  run says so. The dry run compares it, and `to`, with runs of whitespace
  collapsed; every other character, emoji included, is matched as itself.
- A value continues on the lines below it indented four spaces, and lands
  with that indent removed. A code span closes on the line that opens it: a
  line that begins inside a span an earlier line opened is refused at its
  line.
- A design that changes no rule writes the no-change block in place of the
  items, `- nothing` with the reason in its one field `why:`, and the block
  is read in that one spelling. The reason is the proofer's to read: no
  script uses it, so none refuses a block that lacks it. A first line that
  opens like it and is not it, such as `nothing — <why>` or `- none`, is no
  block: the section is refused at that line as the items refuse any line
  outside them, and the reader names the line as one it did not read.
  `## Not verified` reads the block the same way.
- A block that does not match whole is refused at its line, and its design
  joins no group: the settling session reads it whole.
- The section's heading is `## Rule changes`, spelt exactly so, and no
  other heading is read as it. A heading whose letters, case folded, are
  those of `Rule changes`, that is not that heading and that stands outside
  the section, is another section: the reader names it, `chain-check`
  prints it at its line as one it did not read and refuses nothing for it,
  and the settle reads the design whole. Such a heading below level 2
  inside the section is a line of the section, refused as any line outside
  an item is. Whether a named heading meant the section is the judgment of
  whoever reads the design, the proofer at review among them.

`skills/settle/scripts/rule_changes.py` is the one reader.
`chain-check` asks the same reader at the pull request, for each work item
whose `routing.md` it judges and, on a pull request that declares at least
one work item, for every work item `frame/design.md` its own commits add or change
(`docs/checks/the-pull-request-check.md` *What the check reads at the pull
request*).

## A rule has one shape

**A rule has one shape: the rule, its grounds, and, where a case holds it,
the line naming that case.** A `to` value that states a rule opens with the
rule as one bold sentence and gives its grounds as prose. Where a case holds
the rule, the value ends with one check line, which stays English in every
edition. A rule no case holds carries no check line, and review reads it.

- A check line is a shown line of a rule file whose text, after any leading
  spaces, starts with `check: `, lowercase, one space after the colon.
- It names one or more targets separated by single spaces.
- A target is a file of the repository, an eval case directory
  `evals/behaviour/<agent>/<case>/` holding `case.yaml`, or a marker:
  lowercase letters, digits and hyphens, carried by at least one test as
  `@pytest.mark.rule("<marker>")`.
- A marker names the tests of a rule whose test drives a script that can
  refuse a commit or fail a required pull-request job. Every other rule names
  files.
- Only the exact shape above is read. A line that opens like a check line
  and is not one, the label in another case, under emphasis, behind
  Markdown block markup, with a space before the colon, in the plural or as
  the word `Enforced by`, is named at its line as not read and refused for
  nothing; whether it meant a check line is review's to judge.
- A check line is one line. A target wrapped onto the line below is not
  read, and nothing names it, since the line below is prose: a check line
  naming more targets than a wrapped line holds is written past the wrap.
- A check line is refused at its line for a value holding `::`, a comma or
  an em dash, a path that is no file of the repository, and a marker no
  test carries.

**What this plugin checks, and what it does not.** It ships `seal rules --check`
(`.github/scripts/rules.py`), which reads every check line in a rule file,
refuses one the grammar refuses and names one it did not read. At the pull
request, `chain-check` asks the same reader for each check line inside an
`add` or `change` `to` of a design, and refuses a line that reader refuses
at that line of the design. A refused
line inside a section that a
pending `remove` with no `from` takes out at the settle is printed as
excused, with the work item that removes it, and is no refusal. A pending
`change`, or a `remove` with a `from`, excuses nothing, and where the `seal/`
root is local no line is excused. Whether
a target really enforces its rule, whether a rule with no check line has a
case it should name, and whether two rules contradict each other, it cannot
read: that is review's, and it is review's to find.

## The index

**`<policy root>/README.md` is the index: one table row per topic, naming
its file.** A row names its documents as backticked paths, a `.ko.md`
edition on its English edition's row. A framer picks each `file:` from it.
A group of the policy root is a directory directly in it that a row names a
document of, as `<policy root>/<group>/<name>.md`; a directory no row names a
document of, and anything below a group, is not read. Where the index
exists, `seal fold` refuses a document of the policy root or of one of its
groups that no row names, one named on two rows, and a row that names none.
A settling session that creates the policy root writes the index with it,
and after the removals `--apply` names the row each new document is owed.
check: tests/skills/test_fold_check.py
