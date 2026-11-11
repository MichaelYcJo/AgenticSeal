# Design: docstrings recount their history (#1485)

## Grounding

The tree as read at `38123f839`, the tip of `origin/release/v0.37.4` (executed: `git rev-parse origin/release/v0.37.4`). This branch adds only `routing.md` to it (executed: `git diff --stat 38123f839 HEAD`).

| Policy clause | What it fixes for this work |
|---|---|
| G1. Issue #1485 (executed: `gh issue view 1485 --json title,body,comments,labels`) | No comments. *Change* asks to keep the present behaviour and its reason and to remove the sentences that recount how it came to be, starting with the five largest files. *Done when* asks for a count below a value this frame states, measured before and after, and for the tests that pin a docstring sentence to pass or change with the sentence. The issue accepts losing an issue number as the trail to why a branch exists, because `git blame` still leads there. |
| G2. `skills/core/SKILL.md` *The rule a mechanism is kept against*, its last sentences, and *The first value: efficient development through the workflow*, the paragraph opening "A document is cut by who opens it" (read) | History goes to git, the release notes and the work record, and a change removes the comment that stood on the old fact. Text no agent acts on stands in the code's docstring. So a docstring or comment states what the code does now and why, and nothing else. |
| G3. The same section of `skills/core/SKILL.md`: "A reading that is noisy or guessed from words is reported, never used to block" (read) | The count is a measurement for this issue and never a check. No census refuses the pattern (`frame/plan.md` A3). |
| G4. `skills/verify/SKILL.md`, the table under "What can fail depends on what changed" (read) | A comment or docstring inside source can break only the module's import. This work proves more than that: the code of every edited script is unchanged (S1). |
| G5. The measurement at the base (executed: the counting command of *Data & interfaces* at `38123f839`) | 50 Python files under `lib/`, `hooks/`, `.github/scripts/` and `skills/*/scripts/` hold 33,491 lines: 17,499 code, 13,216 docstring or comment, 2,776 blank. 869 docstring or comment lines match the pattern. By kind, 676 lines carry a `#N`, 60 a date, 30 "used to" and 167 "measured"; one line can carry two kinds. The issue's figures (45 files, 865 lines) were taken at an earlier commit. `bin/` holds shell scripts, outside the Python count (G12). |
| G6. What the hit lines of G5 are (executed: the counting command with `--hits`, and a probe listing the lines whose every match sits in a code span; read: the listings) | All 30 "used to" lines recount a former state. All 60 date lines stamp a measurement or an owner's decision. 22 lines have every match inside a code span; 20 of them are samples of a format a script reads or writes, such as `Closes #1` or `... (#572)`, and two recount (`lib/lines.py:514`, `.github/scripts/roll_flow_measurement_issue.py:376`). Of the 111 lines whose only match is "measured", about 35 use the word for what the code measures now, such as "a measured run" or "exit 2 is everything that measured nothing"; that figure is a judgment over a read of the 111 lines, not a count a command gives. 18 lines cite an owner's decision, by `grep -i -E 'owner\|decision'` over the hit listing. |
| G7. The threshold (from G6) | The lines that stay are the keep classes of *Scope* item 1. By G6 they come to about 100: G6's samples of a format and present uses of "measured", about 30 observed behaviours and evidence counts, about 12 of G6's owner-decision lines, and a few dates of versionless observations. The last three figures are read estimates. The threshold is 150, which leaves about half that estimate again as room for the per-sentence judgment. Removing the `#N` lines alone would leave about 190 and miss it, so the threshold also asks for the dates and the "used to" sentences. |
| G8. What reads a script's docstring at runtime (executed: `git grep -n '__doc__\|getdoc\|get_docstring'` over the five trees; read: the heads it names) | `argparse` prints the first line of the module docstring of `.github/scripts/issue_claims_check.py`, `.github/scripts/release_report.py` and `.github/scripts/rules.py`, and the first paragraph of `skills/verify/scripts/payload_meter.py`. None of those heads holds a hit, and the build changes none of them, so no printed line changes and contract rule 14 has nothing to pin. `rules.py` also reads the docstrings of tests, which are out of scope. |
| G9. The cases that pin a script's docstring (executed: `git grep -n -E '__doc__\|get_docstring\|docstring' -- tests evals`; a probe listing each test literal of four or more words that occurs in a script's docstring or comment block holding a hit and not in its code; and a probe listing each test literal that carries a match of the counting pattern and occurs in a script's prose and not in its code; read: each case named below, the first probe's 170 lines, and each case the second probe names; and executed: `git grep -n -E 'get_docstring\|__doc__\|inspect\.getsource\|getdoc' 38123f839 -- tests evals`, every line read) | Five cases read a script's prose. `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py#test_the_gates_own_docstring_says_the_base_is_resolved` needs one paragraph of `broad_gate.py`'s module docstring to carry both `origin/` and `upstream`. `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py#test_the_stamp_docstring_names_the_file_its_mark_is_drawn_from` needs `` `seal-mark.txt` `` in `seal_stamp.py`. `tests/skills/test_seal_stamp.py`'s `test_admitteds_docstring_fits_the_line_length` holds each line of `admitted`'s docstring to 79 columns. Those three pin present facts this work keeps. `tests/skills/test_session_cost.py`'s `Test_module::test_the_module_states_the_rule_and_the_two_shapes_it_misses` holds `token_thirds`' docstring to name the check's path, the subscript and division residuals, and `#192`, the issue the class came from. That last assert pins a provenance *Scope* item 1 removes, so it goes with its sentence (*Removes*). `tests/skills/test_settle.py#test_surveys_docstring_does_not_invite_the_mutation_that_reopens_finding_4` reads `settle.py#survey`'s and `settle.py#apply`'s docstrings with `ast.get_docstring`. It needs "does not take its candidates from here" in `survey`'s and "not taken from `survey`" in `apply`'s, and needs "the retirement are both derived from" absent from `survey`'s. Those are present facts this work keeps. The last `git grep` lists every case that reads a docstring through `ast`, `inspect` or `__doc__`, and the cases on `broad_gate.py`, `admitted`, `token_thirds` and `survey` are all of those that read a script's. The first probe's lines are terms and fixture strings the scripts' prose also uses, such as "through the review chain"; none is a sentence that recounts. Every other literal the second probe names is a fixture value that shares a token with a script's prose by chance, such as `Closes #88`, a zip stem's `2026-09-03` or a judgment row's `2026-10-02`. A case that reads a script's whole text as a string, as the `seal-mark.txt` case does, is found only by the probes' literals and by the word "docstring" near it, so for that spelling this list is a sample, and the broad gate reads the rest. |
| G10. `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, its module docstring (read) | It reads every tracked file's citations: a backticked path with an italic section, `contract rule <N>`, and `path#name` into a `.py` file. A citation the build rewrites has to resolve. A removed one cannot fail it. |
| G11. `ruff.toml` (read) | `E501` is not selected, so no lint holds a docstring line's width. G9's third case holds `admitted`'s. |
| G12. `bin/` (executed: `grep -n -i -E` with the pattern over `bin/*` and `hooks/hooks.json`) | `bin/test:4-5` and `bin/test:28` recount (#156, #337, "one measured segment"). `bin/seal:12` names a file `seal-repo-2026-09-03.zip` in a usage line, a sample of a file name, which stays. |
| G13. `seal/follow-up.md` (read), and the riders in the scoped files (executed: `git grep -n RIDER 38123f839 -- lib hooks .github/scripts skills bin`; read: the comment it names) | The file holds no row. One `# RIDER:` comment stands in the scoped files, opening at `skills/implement/scripts/seal.py:1742`, and its lines 1744 and 1745 are hit lines: a measurement's date inside the rider's evidence. A rider is a present instruction to whoever opens the file (`seal/follow-up.md`), so its instruction stays, and *Scope* item 1 judges its other sentences as it judges any comment. |
| G14. The unsettled designs' `## Rule changes` (executed: an `awk` over each `seal/threads/*/frame/design.md`, grepped for docstring, comment and history) | None states a rule about what a docstring or comment holds. |
| G15. The `### Process changes` table of the latest release (executed: `gh release view --json body`) and of each fragment under `seal/threads/` (read) | No row touches docstrings or comments. |
| G16. #1489's frame on `test/1489-test-files-declare-no-target` at `d0ed5f84d` (read: `git show`), and that branch's script edits (executed: `git diff 38123f839...test/1489-test-files-declare-no-target -- lib skills hooks .github/scripts bin`) | #1489 edits `skills/verify/scripts/test_layout.py` (its design *Scope* items 1 and 2) and one docstring or comment paragraph each in `lib/blocks.py`, `lib/routing.py` and `lib/tables.py` (two in the last). Its *Scope* item 9 rewrites, in later phases, each script docstring that cites a test case it moves. G9's cases stand at their base paths on that branch, at `d0ed5f84d` and again at `871c8e346` (executed: `git grep`). Its overlap row puts #1489 first. |
| G17. `routing.md` (read) | Planning framer, implementation crafter, review through the review chain, automation yes, destination open the pull request. |

## Scope

In:

1. **The rule each sentence is judged by.** It applies to every docstring and every comment of the files of items 2 to 7. A sentence is judged by what it says, whether or not it matches the counting pattern. The pattern's hit listing is where a phase starts, not the edge of its work.

   What goes, and where it already stands:

   - **A sentence about a former state.** What the code, a reader or a document used to do, what replaced what, what a review found before a change: "used to", "before #667", "until #832", "the docstring this replaced". Git and the issue the commit names hold it.
   - **The provenance of a present fact.** The issue, review round, finding or work item a sentence's fact came from, where the sentence states the fact without it: `(#869)`, `#869 round 1's 🟡 2`, `round 5`, `finding 3`. `git blame` leads to the pull request and its issue.
   - **The date of a measurement or a check** of this code or of a tool that has versions. The version stays where the sentence names one.
   - **A coordinate into a work item's records**, such as `frame/design.md` *Measured before the first edit*, `questions.md` Q6, `decision 6 of work item 1791270164`. Those records leave the tree at the settle after their release, so the coordinate points at nothing.

   What stays:

   - **K1. A sample of a format.** A `#N`, a date or the word stands as an example of what the code reads or writes: a commit title's `(#N)`, `Closes #1`, a file name's date.
   - **K2. "measured" for what the code measures now.** "A measured run", "exit 2 is everything that measured nothing".
   - **K3. An observed behaviour a branch exists for, and the evidence a constant rests on.** It is stated in the present tense, with the version it holds for where the tool has one, such as git's or pytest's. An evidence count stays without its date and issue, such as "over 180 transcripts, 44 had no `Agent` call". Where the observed thing has no version, such as the plugin directory's web pages, the observation's date stays as the bound of the claim.
   - **K4. An owner's decision a value is held to.** One sentence says the owner chose the value, and the issue that holds the decision is its one coordinate, such as `#1174`. Its date and any record coordinate go.
   - **K5. A compatibility branch's reason.** It names the shape of the older record or input the branch still reads. It names the release that stopped writing that shape only where the shape alone does not tell a reader which records carry it.

   Where removing the history would leave a branch's reason unstated, the reason is rewritten in the present tense and stays. A sentence that is history alone, whose reason the same docstring or comment already states, goes whole. No line of code, no string constant and no printed message of the files of items 2 to 7 changes (S1). The heads G8 names stay as they are. A test assertion changes only where it pins a sentence this rule rewrites or removes, in the commit that changes the sentence, as G9's fourth case did.

2. **`skills/verify/scripts/session_cost.py`**, 133 hit lines at the base.
3. **`skills/verify/scripts/broad_gate.py` and `skills/code-review/scripts/chain_check.py`**, 154.
4. **`skills/implement/scripts/seal.py` and `skills/settle/scripts/settle.py`**, 83.

   Items 2 to 4 are the five largest files by lines at the base, from `session_cost.py`'s 3,592 to `settle.py`'s 2,234, the issue's starting point (executed: the counting probe's per-file listing).

5. **The other scripts under `skills/`** but `test_layout.py`: `skills/verify/scripts/seal_stamp.py`, `skills/code-review/scripts/pr_body.py`, `skills/verify/scripts/mutation_check.py`, `skills/verify/scripts/payload_meter.py`, `skills/verify/scripts/pytest_record/agentic_pytest_record.py`, `skills/settle/scripts/rule_changes.py`, `skills/verify/scripts/pact_check.py`, `skills/verify/scripts/unverified_check.py`, `skills/settle/scripts/fold_check.py`, `skills/verify/scripts/coordinates.py`, `skills/verify/scripts/deferral_check.py` and `skills/settle/scripts/passages.py`, 204.
6. **Every `.py` under `.github/scripts/`**, 178.
7. **Every `.py` under `lib/`, `hooks/core-start.py`, `skills/verify/scripts/test_layout.py`, and `bin/test`'s comments** (G12), 117 counted lines; `bin/test` is outside the count. These are the files #1489 edits (G16).

   The hit counts of items 2 to 7 sum to G5's total.

8. **The count at the base and at the last phase's commit**, by the counting command, in phase 1's and the last phase's records.
9. **The work item's `changelog.md`**, written by the last phase.
10. **A sentence outside the files of items 2 to 7 that this work made false.** Where a sentence in another file says what a script's docstring or comment holds or where it stands, and this work's rewrite of that prose made the sentence false, the sentence is corrected in place, and nothing else in that file is (`skills/core/SKILL.md` *The rule a mechanism is kept against*, contract rule 19). The last phase corrects them, after #1489 has merged (`frame/plan.md` *Phases*). A list of the range `c21b4248f..e15ce6b77`, made by `git grep` over `tests`, `evals`, `.github/workflows`, `docs`, `skills/**/*.md`, `agents`, `templates`, `CONTRIBUTING.md` and `README.md` for lines naming an edited script beside "docstring" or "comment" and a verb such as says, names, holds or promises, gives 42 lines; read against HEAD, two are false (executed, then read). It is a sample, because the wording is unbounded, and the last phase runs the same search over its own range:
    - `.github/workflows/hygiene.yml:47-48`, which says `close_issues_on_release.py`'s comment stands "two lines above its regex". At `e15ce6b77` that comment stands above `KEYWORDS`, and `CLOSING` follows the tuple.
    - `tests/github/test_label_merged_on_release_branch.py`, the comment in `test_the_label_reader_has_one_source` at `:365-368`, which says the sibling's docstring tells in prose that it used to unpack `closer._issue_api`. Phase 5 removed that sentence. The assert on `"_issue_api("` stands, and the comment keeps the reason the assert reads the call and not the bare name.

Out, each with its reason:

- **The docstrings of `tests/` and `evals/`.** The issue names the scripts. #1489 rewrites the docstrings of the test files it moves (its *Scope* item 10), and a second pass over them now would conflict with it (`frame/plan.md` A8).
- **String constants and printed messages**, the heads of G8 among them. They are text a person reads at a terminal, and changing one owes a pin by contract rule 14, which no part of this issue asks for.
- **`bin/seal:12`.** Its date is a sample file name (K1).
- **Prose under `docs/`, `skills/*.md`, `agents/` and `templates/`.** The issue names the scripts, and those texts have their own work items in this release.
- **The history in `.github/workflows/*.yml` comments**, such as `hygiene.yml`'s account of PR #162 and the 0.8.0 release, or `publish-release.yml`'s `(#718)`, except the sentences of item 10. The issue's directories do not name the workflows, and their history is no fact this work changed; removing it is a second issue of the same kind, which the orchestrator files or leaves.
- **A check that refuses the pattern.** G3; `frame/plan.md` A3.
- **Settling two present claims that disagree.** `session_cost.py`'s `DELEGATING` comment and `spawn_cycles`' docstring give about 1,000 s as a subagent's median, and `measure_segments`' docstring gives 716 s as the median and 1,000 s as the mean over another population (read: `gaps.md` *Not done*). Neither sentence recounts history, so *Scope* item 1 keeps both. Settling them means measuring transcripts that are not in the tree, which this issue does not ask for.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. Only prose changed in the scripts | Given a phase's range, from the commit it started at to its last commit, when the code command of *Data & interfaces* compares them over the pathspecs `lib hooks .github/scripts skills`, then it prints `code differs in: none` and exits 0. A test file the range changes is outside those pathspecs: it is a pinning case changed with its sentence, and the phase record names each assertion it changed | executed by the crafter at each phase's close, its output in the phase record; each changed assertion read at review |
| S2. The count is below the threshold | Given the last phase's commit, when the counting command runs at it, then the `hits` total is below 150, against G5's total at `38123f839` | executed by the crafter in the last phase, both totals in its record; read again by the proofer |
| S3. What stays is a keep class | Given the `--hits` listing at the last phase's commit, then each line is one of K1 to K5 of *Scope* item 1 | read at review, each line against item 1 |
| S4. No reason was lost | Given a removed sentence, when its base text is read beside the code it stands over, then the reason that code exists is still stated at HEAD, in the same docstring or comment or the one above the same code | read at review, the routing's reason for the review chain |
| S5. The docstring pins and the citations hold | Given G9's cases and G10's module, when a phase whose files they read closes, then each passes, or the case changed with its sentence in the same commit | executed by the crafter: G10's module at every phase, the case on `token_thirds` at the phase of *Scope* item 2, the case on `broad_gate.py` at the phase of item 3, the case on `survey` at the phase of item 4, the two on `seal_stamp.py` at the phase of item 5 |
| S7. No sentence elsewhere describes prose this work changed | Given *Scope* item 10's search run over the whole build's range at the last phase's commit, then each line it lists states what the script's prose holds at that commit | executed by the crafter in the last phase, the search and its count in its record; each listed line read at review |
| S6. The edited files lint | Given a phase's edited `.py` files, when `uvx ruff check <files>` and `uvx ruff format --check <files>` run, then both exit 0 | executed by the crafter at each phase's close, as a narrow run of those files alone |

The rest of the suite is `unverified` at every phase. The orchestrator answers it with the broad gate.

## Data & interfaces

The work changes no interface, no output and no stored shape. The two commands below are what S1 and S2 run. The crafter writes each to its scratch directory under the name shown and runs it with `python3 -I`.

The counting command, `test_tmp_count.py <repo> <rev> [--hits]`. A docstring is the first statement of a module, class or function when that statement is a string; every line it spans counts. A comment is a `tokenize` comment token. `--hits` prints each matching line as `path:line: text`.

```python
import ast, io, re, subprocess, sys, tokenize

PATTERN = re.compile(r"#\d+\b|\b\d{4}-\d{2}-\d{2}\b|\bused to\b|\bmeasured\b", re.I)

def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True,
                          text=True, encoding="utf-8", check=True).stdout

def prose_lines(src):
    lines = set()
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            first = node.body[0] if node.body else None
            if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) \
                    and isinstance(first.value.value, str):
                lines.update(range(first.lineno, first.end_lineno + 1))
    for tok in tokenize.generate_tokens(io.StringIO(src).readline):
        if tok.type == tokenize.COMMENT:
            lines.add(tok.start[0])
    return lines

repo, rev = sys.argv[1], sys.argv[2]
listed = git(repo, "ls-tree", "-r", "--name-only", "-z", rev, "--",
             "lib", "bin", "hooks", ".github/scripts", "skills").split("\0")
paths = sorted(p for p in listed if p.endswith(".py")
               and (not p.startswith("skills/") or "/scripts/" in p))
total = {"files": 0, "lines": 0, "blank": 0, "prose": 0, "code": 0, "hits": 0}
for path in paths:
    src = git(repo, "show", f"{rev}:{path}")
    text, prose = src.splitlines(), prose_lines(src)
    blank = sum(1 for i, l in enumerate(text, 1) if not l.strip() and i not in prose)
    hits = [i for i in sorted(prose) if PATTERN.search(text[i - 1])]
    if "--hits" in sys.argv:
        for i in hits:
            print(f"{path}:{i}: {text[i - 1].strip()}")
    for key, n in (("files", 1), ("lines", len(text)), ("blank", blank),
                   ("prose", len(prose)), ("code", len(text) - blank - len(prose)),
                   ("hits", len(hits))):
        total[key] += n
print(total)
```

At `38123f839` it prints the figures G5 states (executed: the block above, extracted from this file and run).

The code command, `test_tmp_same_code.py <repo> <from> <to> [pathspec ...]`. It compares each `.py` file the range changes under the pathspecs, every `.py` file where none is given, with every docstring taken out of the tree, and exits 1 where any file's code differs. Comments are not in the tree, so a comment edit cannot reach it.

```python
import ast, subprocess, sys

def code(src):
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            first = node.body[0] if node.body else None
            if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) \
                    and isinstance(first.value.value, str):
                node.body = node.body[1:] or [ast.Pass()]
    return ast.dump(tree)

def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True,
                          text=True, encoding="utf-8", check=True).stdout

repo, start, end = sys.argv[1:4]
specs = sys.argv[4:] or ["*.py"]
paths = [p for p in git(repo, "diff", "--name-only", start, end, "--", *specs).split()
         if p.endswith(".py")]
changed = [p for p in paths
           if code(git(repo, "show", f"{start}:{p}")) != code(git(repo, "show", f"{end}:{p}"))]
print(f"{len(paths)} .py files differ in text; code differs in: {changed or 'none'}")
sys.exit(1 if changed else 0)
```

It exits 0 for `38123f839` against itself, and 1 for `52f87b8d3` against `38123f839`, a range that changed code, with and without S1's pathspecs. Over phase 1's range `c21b4248f..386e46c8b` it exits 1 without them, naming `tests/skills/test_session_cost.py`, and 0 with them (executed: the block above, extracted from this file and run). A range that holds a merge of `release/v0.37.4` carries other items' code, so a phase runs it from the commit after its last merge.

## Rule changes

- nothing
  why: The work rewrites docstrings and comments to a rule `skills/core/SKILL.md` already states (G2), and no section under `docs/` states what a docstring or comment holds.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| Sentences that recount a former state | The docstrings and comments of the files of *Scope* items 2 to 7 | Git history and the issue each commit names; *Scope* item 1 |
| Issue numbers, review rounds and findings given as the provenance of a present fact | The same files | `git blame` leads to the pull request and its issue (G1) |
| Measurement and check dates on behaviours that have a version or belong to this code | The same files | Git history; the version stays in the sentence (K3) |
| Coordinates into work items' records, such as `frame/design.md` sections, `questions.md` rows and work item ids | The same files | Nothing: the records left the tree at their settle. An owner's decision keeps its issue number (K4) |
| The recounting comment lines of `bin/test` | `bin/test:4-5`, `bin/test:28` | Git history and issues #156 and #337 |
| The two clauses outside the scoped files that the rewrite made false | `.github/workflows/hygiene.yml:47-48`, "two lines above its regex"; `tests/github/test_label_merged_on_release_branch.py:365-367`, the clause saying the sibling's docstring tells that it used to unpack `closer._issue_api` | Nothing: each is corrected in place to what the script's prose holds (*Scope* item 10) |
| The assert that `token_thirds`' docstring names `#192` | `tests/skills/test_session_cost.py#test_the_module_states_the_rule_and_the_two_shapes_it_misses` | Nothing: the provenance it pinned goes by *Scope* item 1, and the case keeps its three asserts on present facts (G9). An assert a later phase removes with its sentence is a removal this table did not name, and goes to that phase's record |

Framed 2026-11-11 by framer, before the build.
