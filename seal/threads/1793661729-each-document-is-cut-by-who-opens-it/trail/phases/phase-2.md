# Phase 2: 1793661729-each-document-is-cut-by-who-opens-it

## What this phase found

**The frame holds for this phase.** It was read against the tree at
384e4f1f3 before the first edit (read). `rule_changes.py#parse` held the
top-level check D4 names. `fold_check.py#documents` and `#index_problems`
read the policy root's top level alone. `.github/scripts/rules.py` globbed
`docs/*.md` in `RULE_FILES`, and `.github/scripts/release_report.py` did
the same in `DOCUMENTS`. The owner's decision of 2026-11-03 removed the
`move` operation and the path rewrite, and this phase adds neither.

**The reader list, as D4 asks.** Both commands ran over the tree at
0ef30af9b, after the readers changed (executed). The first:

```
$ git grep -n "policy_root(" -- ':!seal/'
.github/scripts/release_report.py:198:    policy = config.policy_root(os.path.join(root, "seal"))
.github/scripts/rules.py:240:    policy = sibling("config").policy_root(os.path.join(root, "seal"))
.github/scripts/rules.py:390:    policy = sibling("config").policy_root(os.path.join(root, "seal"))
hooks/lib/config.py:683:def policy_root(home):
skills/code-review/scripts/chain_check.py:1319:    parsed = reader.rule_changes().parse(text, reader.policy_root(root))
skills/settle/scripts/fold_check.py:351:    return ceiling, reader.policy_root(home)
skills/settle/scripts/settle.py:1214:    policy = reader.policy_root(root)
skills/settle/scripts/settle.py:1730:    policy = load(READER, "agentic_unverified_reader").policy_root(root)
skills/settle/scripts/settle.py:1834:    policy = reader.policy_root(root)
skills/verify/scripts/unverified_check.py:998:def policy_root(top):
skills/verify/scripts/unverified_check.py:1002:    return config.policy_root(home)
tests/behaviour/test_a_cited_section_stands_in_its_file.py:165:    return rules.pending(root, config.policy_root(os.path.join(root, "seal")))
tests/behaviour/test_waiver_decided_at_start.py:87:    policy = config.policy_root(os.path.join(ROOT, "seal"))
tests/github/test_rules.py:668:        policy = rules.sibling("config").policy_root(os.path.join(ROOT, "seal"))
tests/hooks/test_config.py:1976:        assert config.policy_root(str(tmp_path)) == root
tests/hooks/test_config.py:1977:        assert config.policy_root("") == "docs"
tests/skills/test_chain_check.py:1460:    ((line, reason),) = RULES.parse(text, reader.policy_root(str(root))).errors
tests/skills/test_chain_check.py:1468:    ((line, why),) = RULES.parse(text, reader.policy_root(str(root))).unread
tests/skills/test_unverified_check.py:1514:        assert UC.policy_root(str(d)) == "rules"
tests/skills/test_unverified_check.py:1517:        assert UC.policy_root(str(joined)) == "docs"
```

The second:

```
$ git grep -n "docs/\*" -- ':!seal/'
tests/github/test_release_report.py:327:        this tree defines, three leg rows, and a row for every `docs/*.md`."""
```

At 384e4f1f3 the second command also listed `release_report.py:24`, `:53`
and `:179`, and `rules.py:75` (executed). Each line of the first list was
read. `chain_check.py:1319` and the two test lines in `test_chain_check.py`
pass the root to `parse`. `settle.py:1214` does the same. `settle.py:1834`
hands the root to `fold_check.py`. `settle.py:1730` names the root in one
printed line. `unverified_check.py` and `hooks/lib/config.py` resolve the
root and list nothing. The two behaviour tests read pending designs
through `parse`. None of these lists documents of its own. The one line
left in the second list is phase 5's (below).

**Two readers the commands did not list read the root's documents.** Both
were found by the narrow runs, not by the two commands, so the commands
are not a complete list of readers (contract rule 12).

- `tests/behaviour/test_docs_line_wrap.py#is_rule_file` asked whether a
  file is a rule file by matching `rules.RULE_FILES`. Once `docs/*.md` left
  that tuple, seven policy documents read as prose, and their long
  `check:` lines failed the wrap limit (executed: 7 failed). The function
  now also asks `rules.py#policy_documents`.
- `ruff.toml` *per-file-target-version* lists each module that runs before
  any interpreter floor is checked. `rules.py` now loads `fold_check.py`,
  so `tests/hooks/test_launch.py::Test_module::test_what_runs_before_any_floor_is_linted_at_the_floor`
  failed on it (executed). 0ef30af9b adds `fold_check.py` at `py39`, and
  ruff passes on it at that target (executed).

**S5, seen red at 384e4f1f3's reader (executed):**

```
FAILED tests/skills/test_rule_changes.py::Test_parse::test_reads_a_file_in_one_group_directory_of_the_root
E       AssertionError: Parsed(ops=[], nothing=None, errors=[(9, '`docs/forms/a.md` is not a top-level docs/ file')], unread=[])
```

The refusals' case had a row `docs/sub/a.md`, refused as below the top
level. That row now reads `docs/a/b/c.md`, one level below a group. Two
rows were added: `docs/../a.md` and `docs/./a.md`. **A decision:** `parse`
refuses `.` and `..` as a group. `..` reaches outside the root. `.` would
let one document carry two spellings, and `rule_changes.py#group` joins
operations by their `file`. D4 says "one level and no deeper", and both
spellings break that. The three rows passed at the old reader, which
refused every path with a `/` in it. Each was seen red under `seal mutate`
(below).

The refusal message changed to "`<file>` is not a `.md` of `<root>`/ or of
one group directory in it". The `below-one-group` row now pins its whole
text (contract rule 14).

**S6, seen red at 384e4f1f3's readers (executed).** The fold:

```
E       assert 'held 4 documents under docs/ to 25000 estimated tokens, 1 past it\n' in 'seal fold: held 2 documents under docs/ to 25000 estimated tokens, 0 past it\ndocs/README.md:4 names no document of docs/\n'
```

`seal rules --check`, against a tree whose index names `docs/g/a.md`:

```
E       AssertionError: seal rules: all 0 check lines in 1 rule files hold.
```

The release report:

```
E         At index 3 diff: 'skills/core/SKILL.md' != 'docs/g/x.md'
```

**What a group is.** It is a decision D4 left to the build. A group is a
directory directly in the policy root whose name stands in a backticked
`<root>/<group>/<name>.md` path in a table row of the index, read by the
row walk `#index_problems` already used (`fold_check.py#index_rows`,
factored out of it). The directory has to exist, and the named file does
not. A row that names a missing file in an existing group still makes the
group read, so the group's other documents are still held to the index.
The row itself is refused as naming no document, as before. A path in
prose outside a table makes no group, so the `docs/experiments/` line in
`docs/README.md` keeps that directory unread. `.` and `..` are no group,
as in `parse`. Nothing below a group is read, because each directory is
read with `os.listdir`. Judged against D4's second row and S6.

**A decision: `rules.py` and the release report read the configured
policy root, not the literal `docs/`.** D4 has them read the documents
`fold_check.py#documents` reads, and the fold reads the root
`hooks/lib/config.py#policy_root` names. In a repository whose `Policy
root` row names another directory, `seal rules --check` now reads that
directory's documents and no longer reads `docs/*.md`. Judged against D4
and `skills/core/SKILL.md` *The rule a mechanism is kept against* ("A fact
has one source"). `release_report.py` is the plugin repository's own
report, and it resolves its root the same way. Its loader `meter` became
`script`, which loads the meter, the config reader and the fold. The
meter's refusal reads as it did.

`tests/github/test_rules.py::Test_main::test_every_check_line_in_the_tree_holds`
looked up each rule file's glob in `RULE_FILES`. A policy document now
matches none, so it raised `StopIteration` (executed). The case now plants
a defect in one policy document under its own bucket, `POLICY_DOCUMENTS`,
and still requires a planted file for every glob.

**Places that stated the old fact, corrected in the same commits** (contract
rule 19). The method was a search for the words, and the list is a sample:
`git grep` for "top-level", "top level", "최상위", `is not a top-level` and
`docs/*`, outside `seal/`. A restatement in other words is not matched.

- the three documents D4 names: `skills/settle/SKILL.md` *Rule changes* and
  *The index*, `templates/setup/config.md` *The fold's values* and
  `skills/config/SKILL.md`;
- both editions of the `seal fold` row in `README.md` and `README.ko.md`;
- the docstrings of `fold_check.py`, `rule_changes.py#parse`, `rules.py`
  and `release_report.py`, and `seal fold --help`, now pinned in the S6
  case;
- `tests/behaviour/test_a_cited_section_stands_in_its_file.py#excuser`'s
  docstring, and the reason string of `seal fold` in
  `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`.

**A departure: `skills/settle/SKILL.md` *The index* gained a sentence and a
`check:` line.** D4 asks for the "top-level document" wording to change. The
section had no statement of what a group is, and S6's rule needs one, so it
now has one. The rule paragraph ends with `check:
tests/skills/test_fold_check.py`. Judged against `skills/implement/SKILL.md`
*2.*, which asks a rule to name its case.

**A limit.** `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`
classes `seal fold` as walking no `specs/`. That stays true unless an
index row names a document in a `specs/` directory directly in the policy
root. A person who writes such a row has made that directory policy.

**Mutation (executed),** each `seal mutate <file> --replace … --tests
"bin/test -q -p no:xdist <module> -k <cases>"`:

| Unit | Mutation | Verdict |
|---|---|---|
| `rule_changes.py#parse` | the group's optional segment removed | red: the S5 case |
| `rule_changes.py#parse` | `.` and `..` no longer refused | red: `the-parent-as-a-group`, `the-root-as-a-group` |
| `rule_changes.py#parse` | a group may hold `/` | red: `below-one-group` |
| `rule_changes.py#parse` | the message reworded | red: `below-one-group` |
| `fold_check.py#documents` | no group read | red: the S6 fold case |
| `fold_check.py#groups` | every directory read, named or not | red: the S6 fold case, on `docs/experiments/e.md` |
| `fold_check.py#groups` | `.` and `..` not excluded | SURVIVED at first, then red (below) |
| `rules.py#policy_documents` | top-level documents alone | red: the S6 rules case |
| `rules.py#policy_documents` | the index's `Unusable` not caught | red: the exit-2 case |
| `release_report.py#documents` | top-level documents alone | red: `Test_documents` |
| `release_report.py#documents` | the index's `Unusable` not caught | red: `index not utf-8` |

The fold's `.`/`..` guard survived, since no case named `..` in an index
(executed: 29 passed). Without the guard, a row naming `docs/../out.md`
makes the repository's root a group and measures its files. bbae52750 adds
that row and a large `out.md` beside `docs/` to the S6 case. The same
mutation then went red on `docs/../out.md is about 25001 tokens`
(executed). The two exit-2 cases, added in fd331c80b, were seen red only
under mutation. At 384e4f1f3 no reader read the index, and both commands
exited 0 there (read).

**Narrow runs (executed).** The phase-boundary set is the 79 test modules
that name, import or walk a path this phase changed, or that this phase
changed. The list came from one `git grep -l` over `tests/*.py`, with the
changed files' names, `ls-files`, `os.walk`, `rglob` and the rule-file
globs as the pattern, joined with the changed tests. At 0ef30af9b,
`bin/test -q` over the 79 gave 3977 passed and 10 skipped. Before
0ef30af9b the same run gave 1 failed, the launch case above. The same
command at 953699548, with this record, `gaps.md` and the Status cell
written, gave 3979 passed and 10 skipped. That set holds the modules that
read a phase record and every tracked file:
`tests/behaviour/test_a_phase_hands_the_next_one_a_record.py`,
`tests/behaviour/test_chain_hooks_hardening.py` and `tests/test_censuses.py`.
`bin/seal fold` over this tree printed "held 17 documents under docs/ …, 0
past it" and "the index docs/README.md names every document", and exited
0.

**For the next phases.**

- Phase 3 rewrites the settle's ceiling sentence to the reader rule.
  `fold_check.py`'s module docstring ("one to split along its own
  headings") and `#past_ceiling_lines`' message ("split it along its own
  headings") state the same rule. The message is pinned in
  `tests/skills/test_fold_check.py::Test_main::test_a_document_past_the_ceiling_is_named_and_the_run_exits_0`.
- Phase 5 writes `docs/README.md` as group tables. A group is read only
  where a table row names one of its documents as a backticked path.
  `tests/github/test_release_report.py::Test_module::test_the_table_reads_this_tree_against_the_last_tag`
  lists `docs/` with `os.listdir`. Once the root is grouped it checks the
  top level alone, which leaves `README.md`. `gaps.md` *Not done* names it.
