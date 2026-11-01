# Design: the settle folds named directories the person marks (#1054)

## Grounding

Every coordinate is at the base, `57d6665b5` (`release/v0.27.3`'s merge into `main`), where this branch was cut, unless its row names another commit.

| Policy clause | What it fixes for this work |
|---|---|
| G1 `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*: "a script does not re-encode that judgment as a grammar rule: it reads what a command wrote or what a real parser returns." | Which policy section a document bears on, whether it is promoted or skipped, and the grounds, "read from the document and checked against the code" in the issue's words, are meaning. `seal settle --from` prints what git answers exactly about each document, and the settling session writes the proposal. The issue's *Done when* bullet "A dry run with `--from` lists every document ... with its section, its proposal and its grounds" is met by the procedure's dry-run step, the command's listing plus the session's proposal table, and not by the script alone. The core outranks the ticket (`skills/implement/SKILL.md` *1. Read the documents that outrank the code first*). |
| G2 `skills/core/SKILL.md` *Asking a person is the most expensive step*: "Whatever needs a person is asked once, together, before the first edit". `skills/implement/SKILL.md` *1. Read the documents that outrank the code first*: "A question in this batch names its answers, and every answer continues." | Both settle questions are put before the first edit, and each names its answers, every one of which continues. The second question cannot join the first, because its rows come from the first's answer; the owner decided the two on 2026-10-27 (the issue's *The person decides, before the first edit*). A run whose first answer names no directory asks nothing more. |
| G3 `skills/core/SKILL.md` *The rule a mechanism is kept against*: "Nothing is kept beside the tree to stay in step with it, such as a stored count or coordinate." | No ledger of skipped documents is kept. A document skipped once is told apart at the next settle from git and from the last settle's pull request body, which already holds each row with its mark (*Scope* item 5). |
| G4 `skills/settle/SKILL.md` at the base: the intro, "**It asks nobody at any step**"; the usage block; *What the dry run shows*; *The settling session's procedure*; *What `--apply` does*, whose last paragraph opens "**A reference root is history, never input.**"; *What this does not do*. | These are the texts the skill's change rewrites in place (contract rule 19). The skill is not under the policy root, so the build edits it. |
| G5 `templates/setup/config.md` *Reference specs*: "The plugin writes only to its own root, and it never moves, edits, absorbs or deletes a reference root." and "That party reads a reference root when the change touches what it describes, and cites what it read, in `frame/design.md` or in the statement `settle` folds into `docs/`, so the next reader can open the same file." | A named directory is read and never written, which the row's rule already says for a reference root. A promoted decision cites its document by path in the statement the settle writes, which is the citation the row already asks for (*Scope* item 6). A named directory need not be a reference root, and no configuration row names one (the issue's *The settle skill asks for them*). |
| G6 `docs/one-root-by-lifetime.md` *The root and its lifetimes*: "no code of the plugin opens a top-level `specs/` or `.specseal/`." The Korean edition says the same under *루트와 그 안의 수명*. | `seal settle --from specs` opens a top-level `specs/` where a person names it. The sentence changes through `## Rule changes` to say "on its own". `docs/the-record-layout.md` *A document with a `.ko.md` edition changes with it, heading for heading* puts the Korean edition in its own item. `tests/behaviour/test_no_document_names_the_old_roots.py` keeps the entries "`specs/` or `.specseal/`" and "`specs/` 나 `.specseal/`", and both `to` values keep those words. |
| G7 `docs/release-checklist.md` *2b. Settle what earlier releases left behind*: "the session running the settle writes each section as its group's latest decision, checked against the code, and closes each open row with what closed it, asking nobody." | The settle now asks before its first edit, so the sentence changes through `## Rule changes`. |
| G8 `docs/README.md` *The records*: `docs/the-record-layout.md` answers "what tells a settle from a deletion". Its section *The fold, and what tells it from a deletion* opens "The procedure is `skills/settle/SKILL.md`. This section holds the rules its readers share." | The rule that a named directory is read and never written, and that only promoted rows reach the policy root, is added there. |
| G9 The unsettled designs' rule changes (read, `awk` over each `seal/threads/*/frame/design.md`). `1793541310-a-band-flags-a-row-and-a-judgment-decides` changes the records-alone sentence of *2b*. `1793541311-the-seal-root-files-listed-at-one-home` changes the layout sentence of *The root and its lifetimes* and *루트와 그 안의 수명*. `1793538229-each-passage-keeps-its-home` changes *The root records*, a sibling of *The fold*. | Two of this design's places share a section with a pending design, so the settle reads them as one group each. Each `from` here quotes a sentence the other design does not touch, so the operations do not collide, and the baseline is the policy in force at each sentence quoted. |
| G10 `hooks/question-gate.py` docstring (read): "PreToolUse gate: on a branch declared `Automation` `yes`, no question is put." `skills/settle/SKILL.md` *A settle is not a work item*: it "edits under `seal no-work-item`". | A settle's branch has no `routing.md`, so the gate reads it as attended and lets the settle's two questions through. Nothing in the gates changes. |
| G11 `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py` (read). `READERS` holds the paragraph of `skills/settle/SKILL.md` that points at `templates/setup/config.md` *Reference specs* to the words "touches what", "describes", "cite", "frame/design.md" and a "never writ" match. `SHIPPED` classifies `seal settle` as reading "the plugin's root by a constant under seal/". | The rewritten reference-root paragraph still states each of those facts, since each stays true. The `SHIPPED` reason for `seal settle` gains the `--from` read, which it does not state today. |
| G12 `tests/text/test_settle_reads_before_it_removes.py#test_both_cheat_sheets_carry_the_command` (read) pins the cell `` `seal settle [--apply]` `` in `README.md` and `README.ko.md`, and the row's links. | The cell stays as it is. The row's prose names `--from` and drops "asking nobody" (and the Korean row its equivalent), so the pin does not move. |
| G13 `skills/settle/scripts/settle.py#main` (read, lines 1112-1119): a root holding no work item prints the settled line and returns 0 before `survey` runs. | A `--from` run lists its documents in that state too. The listing does not depend on `--released-at`, which only work items need. |
| G14 `skills/settle/scripts/rule_changes.py#order` (read): a design's place is the first commit adding it in `git log --full-history --topo-order --reverse --no-renames --diff-filter=A`, "a directory moved under a new id counting as added where it lands". | A named document is placed by the same reading, so a design and a document compare in one order. |
| G15 P1 below (executed): one `git log` per named directory gives each file's adding commit and last change; `git ls-files --cached --others --exclude-standard` lists tracked and untracked files and leaves ignored ones out; `git status --porcelain` names a file changed or untracked in the working tree. | The facts the listing prints are each one git command's output (*Data & interfaces*). |
| G16 P2 below (executed): this design's `## Rule changes` parses and each `from` is found in its section. | `chain-check` and the settle read the operations as written. |
| G17 The issue's comments (executed: `gh issue view 1054 --json comments,milestone`): none, milestone `release: 0.28.0`. The milestone's description (executed: `gh api .../milestones`) orders #1054 before #1045 and #1217, which edit `skills/settle/SKILL.md` and `settle.py` after it. | The body is the request. #1045's and #1217's scopes are out (*Scope*). |
| G18 `seal/follow-up.md` (read): no row waits on this work. `seal/config.md` (read): no `Record language` row and no `Policy root` row. | The records are English, and the policy root is `docs/`. |

### The earlier decisions this frame builds on or departs from

| Decision | Coordinate | Builds on or departs | Grounds |
|---|---|---|---|
| D1 The owner's decision of 2026-10-27: "`settle` takes such directories as input when a person names them, and the person decides what of them becomes policy." | #1054's body, read whole in the spawn and confirmed to have no comment (G17) | Builds on it whole: *Scope* items 1 to 7 are its *The change* bullets. It departs in one reading: "The dry run proposes" is the procedure's dry-run step, the command's listing with the session's proposal, and not the script's output alone | The proposal is meaning, which `skills/core/SKILL.md` gives to judgment and not to a script (D5, G1). The core outranks the ticket |
| D2 #1051, *The plugin stops reading a top-level `specs/`*: "no part of the plugin opens a top-level `specs/` any more, and a repository whose `specs/` belongs to another tool is never read." Built in `ab14194b1`; the issue is closed | `gh issue view 1051` (executed); `docs/one-root-by-lifetime.md` *The root and its lifetimes* states the rule today (G6) | Departs, narrowly: `seal settle --from specs` reads a top-level `specs/` where a person names it. Builds on the rest: the migration, the gates and every other command still never read one, nothing finds one on its own, and nothing writes there | #1051 removed `hooks/root-migrate.py`'s arm, which told a 0.3.x work item from another tool's directory by a guess (a tracked `routing.md` or `rounds/`) and moved what it guessed was its own. Here nothing is guessed and nothing moves: a person names the directory, and the command only reads it (*Scope* item 7). The rule changes by "on its own" in both editions, the one word that separates the two cases. #1051's acceptance, a repository holding another tool's `specs/` untouched by a session, keeps holding, and A6 pins the untouched half for the settle |
| D3 The 0.27.x settle, #1269, merged as `14bfd992`: a body stating each group's decision in merge order, the open rows by kind with what closed each, the defaults taken and the verification; a run that asked nobody | `gh pr view 1269` (executed) | Builds on its body's shape: the proposal rows with the person's marks are one more part of it, beside *The decisions*, and a promoted row's decision is stated there as a group's is. Departs from "asked nobody" by the two questions, both before the settle's first edit | D1. The released records are still settled asking nobody, as #1269 settled them; only the named directories' documents are put to the person, because which of them becomes policy is the person's to decide (D1), and the policy root holds "Norms, ratified by humans" (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*) |
| D4 The settle's current procedure: the script reads and removes and judges nothing; the session writes each section as its group's latest decision checked against the code, in merge order, with no marker; `--apply` removes only under `seal/threads/`; "It asks nobody at any step"; "A reference root is history, never input." | `skills/settle/SKILL.md` at the base (G4), and `docs/the-record-layout.md` *The fold, and what tells it from a deletion* | Builds on the first four: a promoted document joins its section's group and is ordered by commits as a design is (G14), the section is written in the session's words with no marker, and `--apply` is unchanged and refuses `--from`. Departs from the last two, which *Removes* rewrites in place | D1. The citation a promoted section carries is a path in its grounds, not a marker: `templates/setup/config.md` *Reference specs* already asks the statement the settle folds to cite what it read (G5) |
| D5 `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* | the core, as the session received it | Builds on it: `settle.py` prints what git answers exactly, each document's path and its two commits and whether the working tree changed it (P1), and the settling session writes the place, the proposal and the grounds. The script carries no list of extensions or names for what a document is | A script that guessed a document's section or its proposal from its words would re-encode a meaning judgment as a grammar rule, which the section names as the worst result the workflow can give |
| D6 `skills/core/SKILL.md` *Asking a person is the most expensive step*: "Whatever needs a person is asked once, together, before the first edit", and "the design that asks argues why its question is worth that cost" | the core | Builds on "before the first edit" and on every answer continuing (G2). Departs from "once, together": the settle may ask twice | The second question's rows come from the first's answer, so the two cannot be one batch, and both still come before any file is written. The cost is bounded by the answers: a run that names no directory asks once, and a run whose directories hold no document asks once. Each question is worth its cost because the tree cannot answer it: which directories hold decisions is the guess D2 removed, and which decision becomes policy is the person's (D1, D3) |

### The probes

Each ran under `<scratchpad>/1793573496-the-settle-folds-named-directories-the-person-marks/frame/`, which is gone.

- **P1, what git says of a named directory** (executed). A scratch repository with `adr/0001.md` added then changed, `adr/sub/0002.txt` added and then moved to `adr/0002.txt`, `adr/0003.md` untracked, `adr/x.log` ignored by `.gitignore`, and `adr/0001.md` changed in the working tree. `git log --topo-order --reverse --no-renames --name-status --format='%x00%h %cs' HEAD -- adr` printed `A adr/0001.md` at the first commit and `M adr/0001.md` at the second, and the move as `A adr/0002.txt` with `D adr/sub/0002.txt` at the third. `git ls-files --cached --others --exclude-standard -- adr` printed `adr/0001.md`, `adr/0002.txt` and `adr/0003.md`, and not `adr/x.log`. `git status --porcelain -- adr` printed ` M adr/0001.md` and `?? adr/0003.md`.
- **P2, the rule changes parse** (executed). In a `git clone --no-local` of the worktree at `421e44038`, `skills/settle/scripts/rule_changes.py#parse` read this design's `## Rule changes` with the policy root `docs`, and `#section_lines` with `#facts`' comparison compared each `from` and `to` with its section, runs of whitespace collapsed. It parsed one `add` and three `change` items, with no error and no line named as not read. Each section was found once: *The fold, and what tells it from a deletion* at `docs/the-record-layout.md:78-240`, *2b* at `docs/release-checklist.md:31-103`, *The root and its lifetimes* at `docs/one-root-by-lifetime.md:10-26` and *루트와 그 안의 수명* at `docs/one-root-by-lifetime.ko.md:10-28`. Each of the three `from` values was found in its section, and none of the four `to` values was.

## Scope

In:

1. **`seal settle --from <dir>`, repeatable, lists every document of each named directory.** A document is every file `git ls-files --cached --others --exclude-standard` lists under the directory, at any depth and of any extension; a file git ignores is not listed. Each is printed with its repository path, the commit that added it and the commit that last changed it, each as a short hash and a date. A file no commit adds is printed as such, and a file changed in the working tree since its last commit is printed as such. Documents are listed in the order of the commits that add them, read as `rule_changes.py#order` reads a design's, a moved file counting as added where it lands; those no commit adds come last, in path order. Two named directories that hold one file list it once. The listing's heading says that the settling session proposes each document and the person marks it, as the dry run's other headings say who decides.
2. **What `--from` refuses, each with exit 2 and one sentence.** A path that is not a directory in the repository's working tree. A path at or under the resolved `seal/` root, whose records the settle already reads. `--from` given with `--apply`, because `--apply` removes only under `seal/threads/` and a flag it accepted would read as one it acted on.
3. **A run without `--from` prints what it prints at the base, line for line.** A run with `--from` in a root that holds no work item lists the documents, then prints the settled line it prints today. The listing needs no `--released-at`.
4. **The settle skill asks for the directories, first.** `skills/settle/SKILL.md` *The settling session's procedure* opens with the question whether any directory besides `seal/` holds decisions to fold. Its answers are "none", which runs the settle as at the base, or the paths, each passed as `--from <dir>`. Nothing in the plugin finds or opens such a directory on its own, and no configuration row names one. A session that cannot put the question takes "none", and its pull request body says so.
5. **The settling session proposes, and the person marks, before the first edit.** Where the dry run lists a document, the session reads each one whole, with the code it bears on, and writes one proposal row per document: the policy place it bears on, `promote` or `skip`, and the grounds.
   - **The place** is written as a `## Rule changes` operation names one: a `file` picked from the index, `<policy root>/README.md`, and a `section`. It names an existing heading, or a new section or new document marked as new. A document bearing on several sections names each in the one row, and a document whose decisions bear on no section of the policy is proposed `skip` with that as its grounds. A document's own headings decide nothing: it is read whole.
   - **The grounds** say what a promote writes, so a document holding one decision the code bears out and one the code has left is proposed `promote` with the grounds naming the first alone. A plan not yet built, or a decision the code has since left, is proposed `skip` with that reason.
   - **A document skipped at an earlier settle** is proposed `skip` again, with grounds naming that settle's pull request, where the last settle's pull request body holds its row marked `skip` and its last change is a commit that settle's merge commit reaches. Any other document is new. The session finds the last settle's pull request from the last commit that changed the policy root.
   - **The second question** puts the numbered table to the person once. Its answers are "as proposed", "skip every row", or the numbers of the rows whose mark the person flips. Every answer continues, and only a row the person's answer leaves marked `promote` is written.
6. **The promoted decisions are written as the released designs' are.** A promoted row joins the group of the place it names, and the group is ordered by the commits *Scope* item 1 prints beside the designs' commits, a document deciding as of its last change. The session writes the section as the group's latest decision checked against the code, in its own words, and the section's grounds cite the document by its repository path. The settle's pull request body lists each proposal row with its place, its proposal, its grounds and the person's mark.
7. **A named directory is read and never written.** No step of the skill writes, moves or removes a file under it, and `seal settle --apply` removes only under `seal/threads/`. The skill's paragraph "**A reference root is history, never input.**" is rewritten: a reference root is read where the work touches what it describes and cited where it was read, and it is input to a settle only where a person names it at the first question; neither the command nor the session ever writes there.
8. **Every sentence that says the settle asks nobody is rewritten** (contract rule 19). In the skill: the intro's "It asks nobody at any step", and step 4's and step 5's wording where they assume no question. In `README.md` and `README.ko.md`: the `seal settle [--apply]` row's "asking nobody" and its Korean equivalent, which also gain one clause naming `--from`. In the skill's usage block, `settle.py`'s module docstring and its `--from` help: the flag. `templates/setup/config.md` *Reference specs* gains one sentence that `seal settle --from` reads a reference root a person names and writes nothing there. `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py#SHIPPED`'s reason for `seal settle` names the `--from` read.
9. **The policy changes** are this design's `## Rule changes`, which the settle after the release writes into `docs/the-record-layout.md`, `docs/release-checklist.md` and both editions of `docs/one-root-by-lifetime.md`. The build edits no file under `docs/`.

Out:

- **#1045 and #1217**, which edit `skills/settle/SKILL.md` and `settle.py` after this work (G17), and #1139's `--apply` hold on a published note.
- **A configuration row, or any discovery, naming the directories.** The issue rules both out, and the migration and the gates still never read a top-level `specs/`.
- **The script judging a document.** No section, proposal or grounds is printed by `settle.py` (G1).
- **A record of the marks beside the tree** (G3). The settle's pull request body is the record.
- **A case or eval that drives a settling session.** The two questions, the proposal and what reaches the policy root are the session's acts. Where they are held is `questions.md` Q1.
- **`.claude-plugin/plugin.json`**, whose version the orchestrator moves.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A1 An empty first answer | Given a repository with released work items, when the dry run runs without `--from`, then it prints what the base prints, and no line of the named-directory listing | The existing cases of `tests/skills/test_settle.py` pass unchanged, and a new case asserts that the listing's heading is absent from a run without `--from` |
| A2 Every document is listed in git's order | Given a named directory holding a nested file, a file of no `.md` extension, a file moved within it, a file changed after it was added, an untracked file, a file changed in the working tree and an ignored file, when the dry run runs with `--from` that directory, then every file but the ignored one is listed once, with its adding and last-changing commits, in the order of the commits that add them, the untracked file last as one no commit adds, and the changed one named as changed in the working tree | A new case of `tests/skills/test_settle.py`, seen red against the base, where `--from` is an argument error |
| A3 Two directories, one file | Given `--from a` and `--from a/b`, when the dry run runs, then a file under `a/b` is listed once | A new case of `tests/skills/test_settle.py` |
| A4 What `--from` refuses | Given a path that does not exist, a file, a path outside the repository, `seal`, `seal/threads`, or `--from` beside `--apply`, when `seal settle` runs, then it exits 2 with one sentence naming the path or the pair, and reads and removes nothing | New cases of `tests/skills/test_settle.py` |
| A5 A root with no work item | Given a `seal/` root with no work item and a named directory holding a document, when the dry run runs with `--from`, then it lists the document and prints the settled line, exit 0 | A new case of `tests/skills/test_settle.py` |
| A6 A named directory is never written | Given a named directory, when the dry run with `--from` runs and then `seal settle --apply` removes a released work item, then every file under the named directory has the bytes and paths it had before, and `git status --porcelain` of it is unchanged | A new case of `tests/skills/test_settle.py` that records each path and its bytes before and compares after both runs |
| A7 The questions come first, and only promoted rows reach the policy root | Given a settling session, when it runs the skill, then its first act is the directories question; a "none" answer runs the base procedure; with a listing, the proposal table is put in one second question before any edit; only rows left `promote` are written; and the pull request body lists every row with its mark | The owner, reading the settle's pull request body against its diff (Q1) |
| A8 The rule changes parse | Given this design, when `chain-check` reads it at the pull request and the settle groups it, then every operation parses and each `from` is found in its section | P2 (executed), and `chain-check` at the pull request |
| A9 The texts that said the settle asks nobody say what it does | Given the build's diff, when the proofer reads it, then no sentence outside a record says the settle asks nobody without naming its two questions | `git grep -n -i 'asks nobody\|asking nobody\|묻지 않'` over `skills/settle`, `README.md`, `README.ko.md` and `templates`, read at review; the policy root's two sentences change at the settle through `## Rule changes` |

## Data & interfaces

**The command line.** `seal settle [--released-at REF] [--root DIR] [--from DIR]...` for the dry run and `seal settle --apply [--released-at REF] [--root DIR]`. `--from` takes a path relative to the directory `seal settle` runs in, or an absolute one, and is resolved to a repository-relative directory. It is `action="append"` in `settle.py#main`'s parser.

**The listing.** One section of the dry run's output, printed only with `--from`, after *The judgments* and before what `--apply` removes. Its heading says the settling session proposes each document and the person marks it. Under it, one line per named directory with its document count, and under each, one line per document:

```
    <path>  added <hash> <YYYY-MM-DD>  last changed <hash> <YYYY-MM-DD>
    <path>  added <hash> <YYYY-MM-DD>  last changed <hash> <YYYY-MM-DD>  changed in the working tree
    <path>  no commit adds it
```

The exact words are the build's, held to *Scope* item 1. The facts come from three git commands run at the repository's top, each once per named directory (P1): `git ls-files --cached --others --exclude-standard -z -- <dir>` for the documents; `git log --full-history --topo-order --reverse --no-renames --name-status --format=... HEAD -- <dir>` for each path's adding commit, the last `A` line for it, and its last change, the last line naming it; and `git status --porcelain -z -- <dir>` for a working-tree change. A repository whose HEAD has no commit prints every document as one no commit adds.

**The exit codes** are the base's, with *Scope* item 2's refusals added to exit 2.

**The proposal table**, written by the settling session in its message to the person and copied into the pull request body with the marks:

| # | Document | Place | Proposal | Grounds | Mark |
|---|---|---|---|---|---|

## Rule changes

- add
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  to: **A directory a person names at the settle is read and never
    written, and only the documents the person marks promote reach the
    policy root.** A repository's decisions also stand outside `seal/`, in
    architecture decision records, RFCs and another tool's spec files, and
    nothing gathers them into the policy root on its own. So the settling
    session asks the person, before its first edit, whether any directory
    besides `seal/` holds decisions to fold. `seal settle --from <dir>`
    lists every document of each directory named, placed in the timeline by
    the commit that added it and the commit that last changed it. The
    session proposes each document as promote or skip, with the section it
    bears on and the grounds, read from the document and checked against
    the code, and the person marks each row in one more question. A
    promoted decision is written into its section as a released design's
    is, and the section cites the document by its path. The settle's pull
    request body states each row with its mark. No step writes, moves or
    removes a file under a named directory, and `seal settle --apply`
    removes only under `seal/threads/`. An empty first answer runs the
    settle as it ran before, and no configuration row names such a
    directory. `skills/settle/SKILL.md` *The settling session's procedure*
    is the procedure.
    check: tests/skills/test_settle.py
- change
  file: docs/release-checklist.md
  section: 2b. Settle what earlier releases left behind
  from: Between the first and the second, the session running the settle
    writes each section as its group's latest decision, checked against the
    code, and closes each open row with what closed it, asking nobody.
  to: Before the first, the session running the settle asks the person
    whether any directory besides `seal/` holds decisions to fold, and
    passes each one named to the first as `--from <dir>`. Where the first
    lists a document of one, the session proposes each document as promote
    or skip, and the person marks the rows in a second question, before
    the session's first edit. Between the first and the second, the session
    writes each section as its group's latest decision, checked against the
    code, writes each decision the person marked promote into its section,
    and closes each open row with what closed it, asking nobody about
    either. A named directory is read and never written
    (`docs/the-record-layout.md` *The fold, and what tells it from a
    deletion*).
- change
  file: docs/one-root-by-lifetime.md
  section: The root and its lifetimes
  from: no code of the plugin opens a top-level `specs/` or `.specseal/`.
  to: no code of the plugin opens a top-level `specs/` or `.specseal/` on
    its own. `seal settle --from` reads a directory only where a person
    names it at the settle, and writes nothing there.
- change
  file: docs/one-root-by-lifetime.ko.md
  section: 루트와 그 안의 수명
  from: 플러그인의 어떤 코드도 최상위 `specs/` 나 `.specseal/` 을 열지 않습니다.
  to: 플러그인의 어떤 코드도 최상위 `specs/` 나 `.specseal/` 을 스스로 열지
    않습니다. `seal settle --from` 은 settle 때 사람이 이름을 댄 디렉터리만
    읽고, 그 안에는 아무것도 쓰지 않습니다.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| "**It asks nobody at any step**" | `skills/settle/SKILL.md`, the intro | Rewritten in place: the session asks the two questions of *The settling session's procedure* before its first edit and nothing after them, and settles the released records asking nobody |
| "**A reference root is history, never input.**" and its paragraph | `skills/settle/SKILL.md` *What `--apply` does* | Rewritten in place (*Scope* item 7). The never-written half stays, and the input half now names the person's answer as the one way in |
| "asking nobody" in the `seal settle [--apply]` row, and its Korean equivalent | `README.md` and `README.ko.md`, the command table | Rewritten in place (*Scope* item 8) |
| "asking nobody" in *2b*, and "no code of the plugin opens a top-level `specs/`" without "on its own", in both editions | `docs/release-checklist.md` *2b. Settle what earlier releases left behind*, `docs/one-root-by-lifetime.md` *The root and its lifetimes*, `docs/one-root-by-lifetime.ko.md` *루트와 그 안의 수명* | Replaced by the `change` operations above, which the settle writes |
| Nothing of the settle's mechanisms | `skills/settle/scripts/settle.py` | This design adds a flag and two questions, mechanisms under `skills/core/SKILL.md` *The rule a mechanism is kept against*. None of the settle's existing mechanisms does part of their job, so none goes in return: the dry run's sections read `seal/threads/` alone, and `--apply` removes there alone. What the flag costs is one git reading per named directory, run only when a person names one. What it catches has no record yet, since nothing read these directories before; the owner decided the capability on 2026-10-27, and the settle's pull request bodies will be its record |

Framed 2026-11-02 by framer, before the build.
