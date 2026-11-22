# Review round 1: 1795339519-the-thread-layout-has-one-spelling

```seal
target: 6af655c2 against origin/release/v0.38.5
```

This is a finding round over `git diff 0eca6e77..6af655c2`. No earlier round exists, so no fact was carried and every coordinate below was opened this round. The work item has no `frame/` and no `trail/phases/`: `routing.md` declares no `Planning` row, and the second-rung scope confirmation in `gaps.md` stands in for the plan. Compliance was judged against the *Done when* of issue #1567 as it stands after its edit of 2026-11-22T09:37:58Z. No `seal/parity.json` is declared, so no parity comparison was owed.

The reading taken of the first *Done when* item, "No script outside `lib/`, `tests/` and `evals/` spells a name those two modules define", is the one the issue's own table draws. It covers the names of a thread's files and directories (`lib/optin.py:41-64`), `lib/routing.py#FILENAME` and the round-record pattern (`lib/routing.py:332`). The row and answer words `lib/routing.py` also defines, such as `Branch`, were not searched, and `## Not judged` names that row.

## Findings

### 1. Three scripts still spell a thread's file names inside longer literals, at three lines in code that reads the file

```seal
severity: must
location: `skills/verify/scripts/session_cost.py:3140`, `skills/settle/scripts/settle.py:1732`, `skills/settle/scripts/settle.py:1778`, `skills/verify/scripts/session_cost.py:3078`, `skills/code-review/scripts/chain_check.py:1104`, `skills/code-review/scripts/chain_check.py:1110`
evidence: executed `python3 -I test_tmp_literals.py scripts.txt tokens` in the clone at 6af655c2 and at 0eca6e77 (the `## Probes` row); read `skills/verify/scripts/session_cost.py:3105-3141`, `skills/settle/scripts/settle.py:1728-1786`, `skills/code-review/scripts/chain_check.py:1080-1115`
```

Why it matters: the first *Done when* item says no script outside `lib/`, `tests/` and `evals/` spells a name `lib/optin.py` or `lib/routing.py` defines. The changelog says "Now each script reads the one module" (`changelog.md:3`). Six spellings stand at the target.

- `session_cost.py:3140` reads every other work item's routing file from git with `f"{tree}:routing.md\n"`. The read at `:3182`, in `other_work_items`, which calls `branch_declarations` directly, now uses `routing.FILENAME`. The issue's table listed `:3068` and `:3179` and missed `:3140`, and the build kept to the table.
- `settle.py:1732` (`CITATION_RE`, `threads/`) and `settle.py:1778` (`"threads/" not in text`) find citations of a work item directory by `lib/optin.py#WORK_ITEMS` spelt again. The same diff replaced `settle.py`'s `WORK_ITEMS = "threads"` with `_optin.WORK_ITEMS` at `:229`. Where `WORK_ITEMS` moves, `seal settle` stops seeing a citation into a directory `--apply` removes, and the dry run lists none.
- `session_cost.py:3078`, `chain_check.py:1104` and `chain_check.py:1110` build a path a person reads, `{item}/routing.md`, in the same two functions the diff edited. In `chain_check.py:1104` and `:1110` the same f-string reads `{item}/{OPTIN.DESIGN}` from the module and spells `routing.md` beside it. The diff routed other messages of the same kind through the module (`chain_check.py:1090`, `:1782`, `:298-302`), so it drew them into the class itself.

The probe's diff between the base and the target shows the cause. Every instance the build removed was a whole string literal whose value is the name, such as `"routing.md"` or `"threads"`. Every instance left holds the name inside a longer literal. Finding 2 takes up the method.

The snippets below repair the six lines. They also repair the comment at `settle.py:1728` that states the pattern. The docstring sentence at `settle.py:1767` ("SPECS (`threads`)") is prose about the parameter, and the fix pass weighs it with the sentences finding 2 lists.

```python
# skills/settle/scripts/settle.py:1728-1732
# A path into a work item directory, however it is spelled before
# `lib/optin.py#WORK_ITEMS` and its `/`. The name may be cut short with an
# ellipsis, which is how this repository's prose abbreviates a long id; a
# marker and a bare id carry no `/` after the name, so neither is read as a
# citation.
CITATION_RE = re.compile(
    re.escape(WORK_ITEMS) + r"/(\d{6,}[^\s/`'\"()\[\]|<>*]*)/"
)

# skills/settle/scripts/settle.py:1778
        if f"{WORK_ITEMS}/" not in text:

# skills/verify/scripts/session_cost.py:3140, in branch_declarations
    routing = lib_module("routing")
    batch = "".join(f"{tree}:{routing.FILENAME}\n" for tree in trees).encode("ascii")

# skills/verify/scripts/session_cost.py:3078, in work_item_keys, where `routing` is bound at :3066
            f"{os.path.join(name, routing.FILENAME)} names no branch, so the "

# skills/code-review/scripts/chain_check.py:1104 and :1110, in frame(), whose `routing` is a parameter
            f"{item}/{routing.FILENAME} says {who} and {item}/{OPTIN.DESIGN}'s mark says `{mark[1]}`"
                f"{item}/{routing.FILENAME} says {who} and {item}/{OPTIN.DESIGN}'s foot says {line}"
```

The `lib_module("routing")` call at `:3140` adds no load path: `branch_declarations` is reached only from `other_work_items`, which has loaded the module at `:3172`.

### 2. The closing memo states a search method and a limit that the target contradicts

```seal
severity: should
location: `seal/threads/1795339519-the-thread-layout-has-one-spelling/gaps.md:14`
evidence: executed `python3 -I test_tmp_literals.py scripts.txt tokens` at 6af655c2 and 0eca6e77; read `seal/threads/1795339519-the-thread-layout-has-one-spelling/gaps.md:14`
```

Why it matters: the claim was that the class was listed by a search for each name `lib/optin.py` and `lib/routing.py` define, as a code literal, and that only "a name built another way, such as by concatenation" lies outside it. I found that a search for each name as a code literal reaches `f"{tree}:routing.md\n"` at `session_cost.py:3140` and `r"threads/(..."` at `settle.py:1732`. Neither of those is built by concatenation. The search that was run found the name only as a whole literal, so the limit the memo names is not the one that left the instances of finding 1. The sealer and the settle read this paragraph as the bound of the class. It hands back a sample as a whole list.

The memo is also silent on a second population, which the same *Done when* sentence reaches: sentences of messages and help text that name a thread's file to a person. At the target these are `settle.py:679`, `:681`, `:685`, `:689`, `:789`, `:874`, `:880`, `:896`, `:916`, `:956`, `:998`, `:1016`, `:1813`, `:1848`, `:1878`, `:2165`; `broad_gate.py:2130`, `:2379`; `seal_stamp.py:980`, `:1516`; `unverified_check.py:314`; `chain_check.py:1971`; `session_cost.py:3480`; `seal.py:166`; `.github/scripts/release_seal.py:335`; `.github/scripts/publish_release_note.py:899`. Docstrings and comments were not walked. The fix pass either routes these through the modules or writes the bound into the memo. The snippet takes the second course, because no script reads a file through any of them.

```markdown
The class was listed by walking every string constant that is not a docstring, in every tracked Python file outside `lib/`, `tests/` and `evals/`. Each constant was split into tokens on whitespace, backticks, quotes, brackets and punctuation, and each token on `/`. A token part equal to a name `lib/optin.py` or `lib/routing.py` defines for a thread's files, or to the round-record pattern, was kept. That walk reaches a name inside a longer literal, such as `f"{tree}:routing.md\n"`. A name built at run time, such as by concatenation, is outside it. A sentence of a message or of help text that names a thread's file to a person, such as the `NO_FRAGMENT` sentence of `settle.py`, which names `changelog.md`, stays spelt there. It is a word a person reads, no script reads a file through it, and a rename of the file rewrites it with the documents. A message that joins the name to a path, such as `{item}/routing.md says`, reads the module. `evals/scripts/rule_cases.py` writes record files into fixture repositories by their names; it builds a corpus rather than reading one, so it stays.
```

### 3. Every `seal` command now stops at exit 2 where `lib/core.py` is absent, and the changelog names only `lib/routing.py`

```seal
severity: should
location: `skills/implement/scripts/seal.py:196`, `skills/verify/scripts/broad_gate.py:312-317`, `seal/threads/1795339519-the-thread-layout-has-one-spelling/changelog.md:3`
evidence: executed `python3 -I test_tmp_core_absent.py clone` and `python3 -I test_tmp_core_absent.py base-tree` (the `## Probes` row); read `skills/implement/scripts/seal.py:114-117`, `:182-196`, `bin/seal`, `skills/verify/scripts/broad_gate.py:154-156`, `:207-223`, `:391-394`, `:2433`, `lib/sibling.py:104-117`
```

Why it matters: the changelog says that in a whole plugin no command's output or exit code changes. It names one exception: "A plugin copy without `lib/routing.py` now ends `seal gate --record` at exit 2". A second new hard load goes unnamed, and it reaches further.

- `seal.py:196` now loads `lib/core.py` at import. `bin/seal` runs `seal.py` for every subcommand, `seal gate` among them (`seal.py:114-117`), so a plugin copy without `lib/core.py` now ends every `seal` command at exit 2 with the loader's sentence. At the base, `seal.py` did not load it.
- `broad_gate.py#plugin_version` now loads `lib/core.py` through `sibling_module`, and `main` reaches it on every run through `running_line` (`:2433`). An absent module is the loader's `Absent`, exit 2, and `sibling_module` lets it through (`:214-215`). The probe shows it: with the loader's root pointed at a `lib/` without `core.py`, `plugin_version` returns `'0.38.4'` at the base and ends with the loader's sentence and `SystemExit 2` at the target. The docstring above it still says "a run never stops on a label". That sentence now reads as covering this case too, and it does not.

Both loads follow the policy each script states for its other `lib/` modules (`broad_gate.py:154-156`: "an absent one is its sentence and exit 2"). So the defect is in what the changelog and the docstring tell a reader, not in the loads. The snippet names the second load in the changelog and bounds the docstring's promise to the manifest. A fix pass that would rather keep the label promise for an absent module has to make both loads lazy, the one in `seal.py#plugin_version` as well, because `seal gate` stops at `seal.py`'s import before the gate runs.

```markdown
In a whole plugin, no command's output or exit code changes. A plugin copy without `lib/routing.py` now ends `seal gate --record` at exit 2 with `lib/sibling.py`'s sentence when it counts the round records, and a copy without `lib/core.py` now ends every `seal` command at exit 2 the same way, as it already did for the other modules under `lib/`.
```

```python
# skills/verify/scripts/broad_gate.py:312
def plugin_version(plugin):
    """`version` from `<plugin>/.claude-plugin/plugin.json`, or `?` where the
    file cannot be read or does not say -- a run never stops on the manifest.
    The manifest is read by `lib/core.py#manifest`, which loads as every other
    `lib/` module does: absent, it is the loader's sentence and exit 2."""
    version = sibling_module(CORE).manifest(plugin).get("version")
    return str(version) if version else "?"
```

### 4. `routing.md` gives the size of the diff as three scripts and one `lib/` module, and the diff is nine scripts and no `lib/` module

```seal
severity: should
location: `seal/threads/1795339519-the-thread-layout-has-one-spelling/routing.md:19`
evidence: executed `git diff --stat 0eca6e77..6af655c2`; read `seal/threads/1795339519-the-thread-layout-has-one-spelling/routing.md:19`
```

Why it matters: `routing.md:19` grounds the choice of the session as implementer on "The diff is three scripts, one `lib/` module and the cases that name the copies". That sentence says what the work does, so it is read against the target. The diff changes nine scripts: `broad_gate.py`, `chain_check.py`, `seal_stamp.py`, `settle.py`, `rule_changes.py`, `pact_check.py`, `session_cost.py`, `unverified_check.py` and `seal.py`. It changes no `lib/` module. The settle reads a judgment's grounds against what the judgment cost (`skills/core/SKILL.md` *A judgment stands on a source document*). A ground that states a third of the diff misleads that reading. The sentence at `:17`, "The change touches three check scripts", stays true, because it names the three the gate runs.

```markdown
- **Implementation, the session.** The orchestrator has already read every coordinate the issue names. The issue named seven scripts and the cases that name the copies; the diff came to nine scripts, no `lib/` module and the cases, which is not large enough to threaten what the orchestrator still has to hold.
```

## Confirmations

What matched: every row of the issue's table is replaced at the target. `broad_gate.py`'s `ROUND_RE`, `GATE_FILE`, `ROUNDS_DIR` and `round_records`, `chain_check.py`'s four file constants and `:434`, `seal_stamp.py`'s `ROUND_FILE`, its `trail/rounds` join and its `("guarantee.md", "threads")`, `settle.py:229`, `:232` and `:738`, `rule_changes.py:660`, `pact_check.py:493` and `session_cost.py:3068` and `:3179` each read `lib/optin.py`, `lib/routing.py#FILENAME` or `lib/routing.py#rounds` (read, the diff; executed, the probe's base-to-target difference). `unverified_check.py`'s `ITEMS`, outside the table, reads `OPTIN.WORK_ITEMS`.

What matched: `lib/routing.py#rounds` (`lib/routing.py:338-410`) reads what the removed listings read. It matches `round-(\d+)\.md` with `fullmatch`, orders by number, and gives `[]` for an unreadable `trail/rounds`, a file in its place among them. So the `rounds` row of `seal gate` and the `rounds` count of `seal stamp` (`seal_stamp.py:1211`, `count = len(rounds)` over the one caller's `routing.rounds(item)` at `:1347`) are unchanged in a whole plugin (read). The one difference, `$` matching before a trailing newline in the removed `^round-(\d+)\.md$`, reaches only a file name ending in a newline.

What matched: both `plugin_version` functions read the manifest through `lib/core.py#manifest` (`lib/core.py:68-76`), which gives `{}` for an unreadable file and for a JSON value that is not an object. `seal.py:1687` keeps `""` and `broad_gate.py:316-317` keeps `?`, the two fallbacks the old bodies returned for the same three failures (read).

What matched: `quote` has one body, at `seal_stamp.py:986`, and `broad_gate.quote` had no caller at the base (executed, `git grep` for `quote(` over `skills`, `.github`, `lib`, `hooks` and `bin` at 0eca6e77 found only `shlex.quote` and the definitions). The broad-gate case `test_refuses_to_leave_a_metacharacter_to_cmd_exe` moved to `tests/skills/test_seal_stamp.py:1186`. It pins a Windows quote of a path with no space, which the group's space case at `:1179` does not, so it covers something its group does not (read).

What matched: `tests/skills/test_broad_gate.py:198`'s file-equality assertion went with the copies, and no other case under `tests/` holds a copy of a thread's file name equal to a module's (executed, `git grep` over `tests/` for equality against `optin.*`, `routing.FILENAME` and `ROUND_RE`). `Test_rounds` in `tests/lib/test_routing.py:462` is the first direct case of `routing.rounds` (executed, `git grep` for `routing.rounds(` over `tests/`). No tracked file outside the old work items cites a removed name as `script#NAME` (executed, `git grep`).

What matched: each joined path in the diff splits the `/`-joined name before `os.path.join` (`broad_gate.py:1714`, `seal_stamp.py:1355`, `pact_check.py:495`, `rule_changes.py:600-602`), and each git path keeps `/` (`chain_check.py`), so the Windows leg's slash-in-join class (`tests/censuses.py:1294`) gains no instance (read).

What matched: the claim in `gaps.md:10` that the narrow suites pass. I ran `bin/test -q` over eleven test modules of the touched code plus `tests/lib/test_optin.py`: 1946 passed, 1 skipped. I ran `tests/skills/test_pr_body.py`, which reads `chain_check.CLOSING_RECORDS`: 107 passed. Without the 70 cases of `test_optin.py`, the two runs make 1983, the implementer's count over twelve files (executed). The memo does not name the twelve, so only the count matches. A narrow `uvx ruff check` and `uvx ruff format --check` over the thirteen touched Python files exit 0 (executed). The suite stays `unverified` in `gaps.md:10`, and the orchestrator answers it, so the label is honest.

What matched: both quotes in `pr.md` stand word for word at the coordinates they carry, `routing.md:15` and `gaps.md:16` (read). `gaps.md:16`'s "as the issue's *Done when* first said" holds: the issue's edits of 09:24:35Z and 09:27:34Z said `quote` would have one body under `lib/` (executed, the issue's `userContentEdits`). `Commit and pull request language` is English, so no `pr.<lang>.md` is owed.

The case `test_the_gate_and_the_check_spell_the_flag_alike` (`tests/skills/test_broad_gate.py:197`) still holds two copies of `--sealing` equal. The flag is no name of a thread's file, so it is outside this issue's class, and the second *Done when* item removes a case only with its copies.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at 6af655c2, which no agent runs (contract rule 2) | `seal/config.json` `Broad gate` | the orchestrator |
| Whether "a name those two modules define" also covers the row and answer words of `lib/routing.py` (`Branch`, `Review`, `yes`); this round read it as a thread's file names and the round pattern, as the issue's table does | `lib/routing.py:57-96` | the orchestrator |
| The premise of the docstring `seal_stamp.py#quote` now carries in full, that on Windows "the person types the command into `cmd.exe`". In PowerShell, double quotes expand `$`. The code is unchanged from the base, and only the sentence is new to this file | `skills/verify/scripts/seal_stamp.py:997-1002` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_literals.py scripts.txt tokens`, run from the clone at 6af655c2 and from a worktree at 0eca6e77. The probe walks every `ast.Constant` string that is not a docstring in each tracked `.py` outside `lib/`, `tests/` and `evals/`. It splits each string on whitespace, backticks, quotes, brackets, commas, colons, semicolons and asterisks, then splits each token on `/` and `\`, and prints a part equal to `threads`, `frame`, `trail`, `design.md`, `plan.md`, `questions.md`, `phases`, `rounds`, `gate.md`, `gaps.md`, `guarantee.md`, `changelog.md`, `pr.md`, `parity.json`, `agentic-scratch`, `routing.md` or `agentic-seal` | 71 hits at the base and 46 at the target. Every hit removed is a whole literal equal to the name. The remaining path-building hits are the six lines of finding 1. The rest are panel labels (`rounds`), the `found["threads"]` dictionary key of `settle.py` and the message sentences finding 2 lists |
| `python3 -I test_tmp_core_absent.py <tree>` for each of the clone and the base worktree. The probe copies `lib/` without `core.py` into the scratch directory, imports `broad_gate`, points `sibling.ROOT` at the copy and calls `plugin_version(<tree>)` | target: the loader's `cannot read .../lib/core.py` sentence and `SystemExit 2`. base: `'0.38.4'` |
| `bin/test -q` over `tests/lib/test_core.py`, `test_routing.py`, `test_optin.py` and `tests/skills/test_broad_gate.py`, `test_chain_check.py`, `test_pact_check.py`, `test_rule_changes.py`, `test_seal_stamp.py`, `test_seal.py`, `test_session_cost.py`, `test_settle.py`, `test_unverified_check.py` | exit 0, 1946 passed, 1 skipped |
| `bin/test -q tests/skills/test_pr_body.py` | exit 0, 107 passed |
| `uvx ruff check` and `uvx ruff format --check` over the thirteen `.py` files the diff changes | exit 0 and exit 0 |
