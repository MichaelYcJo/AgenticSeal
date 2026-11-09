# Design: settings are read as JSON (#1454)

## Grounding

The tree as read at `20bd4132`.

| Policy clause | What it fixes for this work |
|---|---|
| G1 `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | A script holds a gate only on a fact it reads exactly, and a parser's result is one. A fact has one source. Before a fix adapts to a structure, ask whether the structure should change. A change rewrites the text it amends in place and removes in the same commit what stood on the old fact. So the settings move to a format the standard library parses and writes, the table walker's settings readers leave with the readers they served, and every sentence that states the table shape is rewritten. |
| G2 `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* (read) | Agents read the language keys, `Policy root`, `Reference specs` and `Broad gate` to judge. Scripts read every key exactly. An agent reads JSON as well as it reads a table, so the format serves the scripts and costs the agents nothing. |
| G3 `docs/layout/one-root-by-lifetime.md` *What the repository decides for itself, and how it is read* (read) | One file holds what a repository says about itself, documented in `templates/setup/config.md` and reached through `/agentic:config`. Its paragraph *A cell may carry an escaped pipe…* states the table rule this work replaces (*Rule changes*). |
| G4 `lib/config.py#config_text` and `#config_value` docstrings, #867 and #871 (read; executed `gh issue view 867`, `871`) | A file that is there and will not read is refused, never read as absent, and a row written twice has no value. Both carry over to JSON: a file that will not parse is refused, and a key written twice has no value. A `config.md` standing without a `config.json` is a written answer this release does not read, so it is refused by the same rule. |
| G5 The table shape's own defects (executed `gh issue view` 867, 871, 925, 1119) | #867: a row written twice was read several ways. #871 and #925: a grammar of its own disagreed with GitHub's renderer on 16 shapes. #1119: `pact_check` read the path map with the config table's retired grammar. Each came from reading settings through a markdown table. |
| G6 #1211 (executed `gh issue view 1211`) and the issue's *Out of scope* (owner) | Tables inside records and documents stay markdown. The `| Pact | Clause | Hash |` anchor table stands in a work item's `frame/design.md` and *Judgments of the run* in `frame/plan.md`, both records, so both stay and stay read by the walker. |
| G7 `skills/commit-pr-convention/SKILL.md` *Every way of not naming a language lands on English* and #1453, merged in 0.36.0 (read) | The two language rows exist and are required, and "a file that cannot be read or does not parse as that table" is one of the four ways of not naming a language. #1453 is merged at `dfd0c995`, so this work moves the rows as #1453 left them: the same two names, as keys. |
| G8 `templates/setup/config.md` (read, 525 lines by `wc -l`) | Documents every row and what an absent one means. The issue keeps it whatever the format, so it stays at its path and documents keys. Its opening `| Item | Value |` table, its escaped-pipe rules in *Broad gate* and its list of walker refusals describe the table and change. |
| G9 What the walker reads (executed `git grep -n 'gfm_table(\|read_table('` outside `tests/`) | `lib/config.py#gfm_table` is called for: `config.md`'s `| Item | Value |` (`config_table`); `parity.md`'s `| Field | Value |` and `pact.md`'s `| Signer |` (`read_table`, through `baseline_commit` and `pact_signers`); `~/.claude/agentic/pact-paths.md`'s `| Remote | Path |` (`pact_check.py#path_map`); and two records, the anchor table (`pact_check.py#first_table`) and *Judgments of the run* (`settle.py#plan_rows`). After this work the walker keeps the two records' readers. |
| G10 The issue's names against the tree (executed `git grep`) | The issue says "`parity.md`'s path map and `pact.md`'s anchor". `parity.md` holds a `| Field | Value |` table, and its machine-local path map `~/.claude/agentic/parity-paths.md` is read by no script, only by agents (`skills/legacy-parity/SKILL.md` *The migration config*). `pact.md` holds the `| Signer |` table; the anchor table stands in frames (G6). This frame reads the issue's *Done when*, "no settings file is read by the markdown table walker", as the criterion, and so takes the four settings tables of G9 and the parity path map beside them. |
| G11 The walker's size (executed: a probe that walks `lib/config.py` with `ast` from the roots `gfm_table`, `unfenced`, `table_cells`) | Those roots reach 25 units spanning 520 lines. `lib/config.py` is 1420 lines at `20bd4132` (`wc -l`); the issue's 1,417 is the count at `1af09327`. |
| G12 JSON in the standard library (executed: the same probe, Python 3.15.0) | `json.loads` takes the last of a key written twice; an `object_pairs_hook` sees both and lets the reader refuse that key. A byte order mark makes `json.loads` raise; decoding with `utf-8-sig` reads it. A trailing comma raises. This repository's seven rows, read by `config_table` with no refusal, dump with `indent=2, ensure_ascii=False` and load back equal, in order. |
| G13 The installed plugin is not the tree (executed `which seal`: `~/.claude/plugins/cache/agenticseal/agentic/0.36.0/bin/seal`; read `.github/workflows/hygiene.yml`) | The orchestrator's `seal` and every agent definition come from 0.36.0, which reads `seal/config.md`. This repository's CI runs the tree's scripts (`python3 skills/implement/scripts/seal.py mode --check`, `chain_check.py`), which after this work read `seal/config.json`. So the build converts this repository's own config, and `frame/plan.md` *Overlap with the release* and *Operational impact* draw the consequences. |
| G14 `templates/setup/seal-README.md` *Layout* and `seal/README.md` (read) | The layout block already says that `templates/setup/config.md` documents every item. The comment `seal mode` writes at the head of `config.md` says the same thing a second time, so a JSON file that carries no comment loses no pointer. |
| G15 `skills/implement/scripts/seal.py#write_row`, `#with_row`, `#doubled_modes` (read) | The writer keeps line endings, finds the row by the reader's walk, and reads its own write back before it writes, because a write into a markdown table can land where no walk reads it (#429). A JSON writer serializes the object, and none of that applies. |
| G16 `skills/verify/scripts/broad_gate.py` lines 664-1100 (read) | `missing_row` gives four refusals for a `Broad gate` row nobody read, one per walker cause, with the helpers that quote the line. In JSON a key is read or it is absent, so one refusal is left. |
| G17 `templates/setup/parity.md` and `skills/parity-setup/SKILL.md` (read); `skills/code-review/scripts/chain_check.py:1595-1625` (read) | A script reads one field of `parity.md`, `Baseline commit`, through `baseline_commit`. Agents read the others. The file's presence is the declaration. Its `Policy root` field may read `none`, which `config.md`'s `Policy root` row refuses (`templates/setup/config.md` *The fold's values*), so the two are not one key and the parity fields keep a file of their own. |
| G18 `docs/layout/the-pact.md` *The words* and *`seal pact` reconciles, locally*; `templates/setup/config.md` *Pact* (read) | The pact's repository is identified by holding `seal/pact.md`, its clauses are its `##` headings, and its `| Signer |` table lists every other signer. A `Pact notify` row is read by nobody, which is the rule for any key no reader asks for. |
| G19 `skills/settle/rule-changes.md` *Rule changes* and `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | This work item's subject is the code, so the `docs/` sentences it makes false are stated as operations in *Rule changes*, for the settle. `Policy root` is absent from `seal/config.md`, so the policy root is `docs`. |
| G20 `seal/follow-up.md` (read); v0.36.0's `### Process changes` (executed `gh release view --json body`) | No follow-up row waits on this work. Three process rows of 0.36.0 name the language rows of `config.md` that the orchestrator asks for and writes; this work changes the file and the word they name, so its fragment carries process rows. |
| G21 The ticket (executed `gh issue view 1454 --json body,comments`) | No comments. The body is the request; *Out of scope* is the owner's decision. |
| G22 #1059's frame, uncommitted in its worktree (read at `/Users/michael/Documents/GitHub/SpecSeal-worktrees/feat/1059-a-foreign-seal-dir-keeps-the-records-shared`) | It removes `lib/config.py#HOME`, changes `inside_the_root`, and edits `chain_check.py#originals_of`, `seal.py`, `pact_check.py`, `seal-README.md` and contract rule 11. `frame/plan.md` *Overlap with the release* takes it from there. |

## Scope

In:

1. **`seal/config.json` is read by one reader in `lib/config.py`.** The file is one JSON object. Each member is a key named as the row was (`Commit and pull request language`, `Record language`, `Mode`, `Broad gate`, `Reference specs`, `Pact`, `Policy root`, `Document token ceiling`, `Pull request seal mark`, `Release note seal mark`), and each value is a JSON string in the grammar `templates/setup/config.md` gives that key today. The reader's states are in *Data & interfaces*. `declared_value`, `declared_mode`, `policy_root`, `reference_roots`, `declared_pacts` and `pact_declaration` keep their contracts on top of it.
2. **`seal mode` writes `config.json`, and converts a `config.md` once.** It writes the `Mode` key by serializing the object, keeping every other key and its order. Where the root holds `config.md` and no `config.json`, bare `seal mode` reads the `| Item | Value |` table through the walker, writes `config.json` with the rows in order, and removes `config.md`. A walk refusal or a row written twice writes nothing and prints the sentence. `seal mode --check` writes nothing and exits 2 on an unconverted `config.md`. `seal mode` also names a `parity.md` standing without a `parity.json`, with the keys to write (Scope item 4). This repository's `seal/config.md` becomes `seal/config.json` through the tree's `seal mode`.
3. **Every script that reads a setting reads it through Scope item 1's reader.** `broad_gate.py`, `fold_check.py`, `pr_body.py`, `.github/scripts/release_seal.py`, `seal.py`'s report, `chain_check.py`'s naming of a missing language key, `unverified_check.py` and `.github/scripts/rules.py`, `release_report.py` through `policy_root`. `broad_gate.py`'s units that explain a walker refusal of the `Broad gate` row leave (*Removes*), and its refusal for an absent key stays.
4. **`seal/parity.json` replaces `seal/parity.md`, and `~/.claude/agentic/parity-paths.json` replaces `parity-paths.md`.** Its presence is the declaration. `lib/optin.py#PARITY_CONFIG` names it. `chain_check.py`'s parity arm reads its `Baseline commit` key, and refuses a `seal/parity.md` that git carries at HEAD without a `seal/parity.json`, naming the keys to write, wherever the arm would read the config. `templates/setup/parity.json` replaces `templates/setup/parity.md`, whose prose moves to `skills/legacy-parity/SKILL.md` *The migration config*. `skills/parity-setup/SKILL.md`, `skills/legacy-parity/SKILL.md` and the agents name the new files.
5. **The pact's signers stand in a `Pact signers` key, and the path map is `~/.claude/agentic/pact-paths.json`.** In the pact's repository, `seal/config.json` holds `Pact signers`, remote URLs separated by `;` in the grammar of `Pact`, read through `remote_entries`. An absent or empty key is the refusal a `pact.md` with no signer table gets today, worded to name the key. `seal/pact.md` keeps its clauses, and `templates/setup/pact.md` loses its `| Signer |` table. The map is a JSON object from remote URL to checkout path; two keys that normalise to one remote are refused and neither is read.
6. **The walker moves to `lib/tables.py`, and `lib/config.py` holds the settings alone.** `gfm_table` and the units G11 lists move. `pact_check.py`, `settle.py`, `.github/scripts/rules.py` and `seal.py`'s converter import it there. The units that read a settings table leave `lib/config.py` (*Removes*). `seal.py#LIB_PURPOSES` names `tables.py`, and `lib/config.py` no longer imports `lib/blocks.py`.
7. **Every shipped text that names a settings file or calls a setting a row is rewritten.** The closed set is what `git grep` lists for `config\.md`, `parity\.md`, `parity-paths\.md`, `pact-paths\.md`, `Item \| Value`, `Field \| Value`, `Signer \|`, `Remote \| Path`, `language rows?`, `config rows?`, `config table` and each key of Scope item 1 and `Pact signers` and `Baseline commit` followed by ` row` or ` rows`, outside `seal/threads/` and `docs/`. A hit naming `templates/setup/config.md`, the document, stays. The `docs/` hits are *Rule changes*. A setting is a "key" in every rewritten sentence.
8. **The tests and the eval scaffolds build JSON settings.** `tests/conftest.py`'s config helpers write `config.json`. Cases that pin a walker refusal of a settings table leave with the code they pinned; the walker's own cases and `tests/gfm_table_oracle.py` stay. `evals/scripts/rule_cases.py`'s `CONFIG` and `SEALER_CONFIG` become JSON, and the scaffolds are generated again from it.
9. **`changelog.md`**, in the shape `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file* states, under *Changed* and *Removed*, with an *Updating* line: run `seal mode` once in each repository that holds `seal/config.md`; write `seal/parity.json`, a `Pact signers` key and `~/.claude/agentic/pact-paths.json` by hand from the old files. It ends with a `### Process changes` table in `templates/records/process.md`'s shape (G20).

Out:

- **Tables in records and documents.** The owner's decision (G6): the anchor table, *Judgments of the run*, `routing.md`, `gaps.md`, the `docs/` index.
- **The values' grammars.** Every value stays a string in its documented grammar, `;` and `,` lists included (`frame/plan.md` *Alternatives considered* A6).
- **A converter for `parity.md`, `pact.md`'s signer table and `pact-paths.md`.** The release note says what to write; `frame/questions.md` Q1 holds the default.
- **A pact headed with the 0.18.x word.** It is a pact with no `Pact signers` key, refused as one.
- **`templates/setup/config.md`'s path.** It stays, as the document of the keys.
- **`docs/experiments/`**, which is no policy.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a key is read | Given `config.json` holding `{"Broad gate": "bin/test -q \| tee out"}`, `declared_value(home, "Broad gate")` returns the string with a plain pipe, and `seal gate` runs it. | cases in `tests/lib/test_config.py` and `tests/skills/test_broad_gate.py` |
| S2 what does not read is refused | A file that will not decode, will not parse or whose top level is not an object is refused for every key. A key written twice, or one whose value is not a string, is refused for that key alone, and every other key reads. No file reads as nothing declared. A byte order mark reads. | cases in `tests/lib/test_config.py` |
| S3 an unconverted config | Given a root holding `config.md` and no `config.json`, `seal gate`, `seal pr-body`, `seal fold` and `seal mode --check` exit 2 naming `seal mode`, and nothing ran. | one case per command |
| S4 the conversion | Given a `config.md` whose table holds a `\|` value, bare `seal mode` writes `config.json` with every row in order and the pipe plain, removes `config.md`, and `seal mode --check` passes. Given a table the walker refuses, or a row written twice, nothing is written and the sentence is printed. Given both files, `config.json` is read and `config.md` is named and left in place. | cases in `tests/skills/test_seal.py` |
| S5 the writer | With no `Mode` key, `seal mode` adds it and keeps every other key and its order; with no file, it writes `{"Mode": "<folder's mode>"}`; with a refused file, it writes nothing. | cases in `tests/skills/test_seal.py` |
| S6 the parity arm | Given `parity.json` whose `Baseline commit` is a SHA, the arm compares as today. Given `parity.md` at HEAD and no `parity.json`, the check refuses once, naming the keys. A `Baseline commit` that is not 7 to 40 lowercase hex digits is refused. | cases in `tests/skills/test_chain_check.py` |
| S7 the pact | `seal pact` reads the signers from `Pact signers`, and exits 2 naming that key where it is absent. The map reads from `pact-paths.json`; two keys naming one remote are refused and neither is read. | cases in `tests/skills/test_pact_check.py` |
| S8 no settings file is read by the walker | `git grep` of `gfm_table` callers lists `settle.py#plan_rows`, `pact_check.py#first_table` and `seal.py`'s converter of `config.md`, and `lib/config.py` imports neither `tables.py` nor `blocks.py`. | read at review |
| S9 this repository | `seal/config.json` holds the keys G12 lists and `seal/config.md` is gone; `tests/behaviour/test_this_repository_passes_its_own_checks.py` passes. | the broad gate, the orchestrator's run |
| S10 the text | Scope item 7's `git grep` returns no shipped sentence that names `seal/config.md`, `parity.md`, `parity-paths.md` or `pact-paths.md` as the current file, outside the converter's and the refusals' own sentences and the changelog fragment. | read at review |

## Data & interfaces

**`lib/config.py`.** `CONFIG = "config.json"`, and the name before it, `config.md`, beside it for the converter and the refusal. A reader `(pairs, refusal) = config_pairs(home)` opens the file once, decoding `utf-8-sig`, and parses with an `object_pairs_hook` that returns the members as a list in file order:

| State | `pairs` | `refusal` |
|---|---|---|
| no `config.json` and no `config.md`, or a falsy home | `None` | `None` |
| `config.md` and no `config.json` | `None` | a sentence naming `config.md` as not read and `seal mode` as what converts it |
| `config.json` will not decode, will not parse, or is not an object | `None` | a sentence naming the path and the parser's message |
| otherwise | the members | `None` |

`config_value(pairs, key)` gives `(value, refusal)`: absent is `(None, None)`, a key written twice is `doubled_row`'s sentence, a value that is not a string names its JSON type, and a string is the value as parsed. `declared_value(home, key)` is the two in turn. The crafter names the functions; the states are the contract.

**`seal.py`.** The writer reads the pairs, sets or appends `Mode`, and writes `json.dumps(dict(pairs), indent=2, ensure_ascii=False) + "\n"` with `\n` endings, refusing where the reader refuses. The converter reads `config.md` through `lib/tables.py#gfm_table` with the header `("Item", "Value")`.

**`seal/parity.json`.**

```json
{
  "Original repo": "<org/repo>",
  "Module": "<path within it, or whole repo>",
  "Baseline commit": "<SHA>",
  "Policy root": "<docs/, or none>",
  "Coordinate-trust exceptions": [],
  "Scope notes": ""
}
```

An exception is an object with `Path`, `Why it needs re-verification` and `Noticed`, so the empty list is "none" and the old field that said "none" beside the table goes. `Baseline commit` is the SHA alone; the date `skills/parity-setup/SKILL.md` step 3 records is the date of the commit that writes the file.

**`config.json` in the pact's repository** adds `"Pact signers": "<remote URL>; <remote URL>"`.

**`~/.claude/agentic/pact-paths.json` and `parity-paths.json`** are each `{"<origin remote URL>": "<checkout path>"}`.

**`lib/tables.py`** holds `gfm_table`, `table_cells`, `unfenced`, `fence_map`, `hidden_lines`, `gfm_line_starts` and the units they reach (G11), unchanged.

## Rule changes

- change
  file: docs/README.md
  section: docs/layout/
  from: and what the repository's config rows decide |
  to: and what the repository's config keys decide |
- change
  file: docs/layout/one-root-by-lifetime.md
  section: One root, laid out by lifetime
  from: and what a repository's config row decides.
  to: and what a repository's config key decides.
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: 루트 하나, 수명 순으로 배치한다
  from: 저장소의 설정 행이 무엇을 정하는지를 적습니다.
  to: 저장소의 설정 키가 무엇을 정하는지를 적습니다.
- change
  file: docs/layout/one-root-by-lifetime.md
  section: Shared or local
  from: **`seal/config.md`'s `Mode` row is not the opt-in, and the difference is what
    reads it.** The row says where the root *should* be; the folder's location
    says where it *is*, and no hook, gate or check resolves the root through the
    row: `lib/optin.py#home_at` is the only reader of the question. A gate that
    trusted a hand-editable row would look in a place with no folder, and that
    module fails toward *not opted in* rather than toward a guess. What the row
    buys is a repository that can say which mode it wants before the folder is
    moved, and a check that names a disagreement left standing. An absent row is
    filled in from where the folder is, the only value that cannot be wrong.
  to: **`seal/config.json`'s `Mode` key is not the opt-in, and the difference is
    what reads it.** The key says where the root *should* be; the folder's
    location says where it *is*, and no hook, gate or check resolves the root
    through the key: `lib/optin.py#home_at` is the only reader of the question.
    A gate that trusted a hand-editable key would look in a place with no
    folder, and that module fails toward *not opted in* rather than toward a
    guess. What the key buys is a repository that can say which mode it wants
    before the folder is moved, and a check that names a disagreement left
    standing. An absent key is filled in from where the folder is, the only
    value that cannot be wrong.
- change
  file: docs/layout/one-root-by-lifetime.md
  section: Shared or local
  from: `seal mode` moves the root and writes the `Mode` row, and leaves `.github/` alone.
  to: `seal mode` moves the root and writes the `Mode` key, and leaves `.github/` alone.
- change
  file: docs/layout/one-root-by-lifetime.md
  section: Shared or local
  from: No config row says whether the checks are installed:
  to: No config key says whether the checks are installed:
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: shared 인가 local 인가
  from: **`seal/config.md` 의 `Mode` 행은 옵트인이 아니고, 차이는 무엇이 그것을
    읽느냐에 있습니다.** 그 행은 루트가 *있어야 할* 자리를 말하고, 폴더의 자리는
    루트가 *있는* 자리를 말합니다. 어떤 훅, 게이트, 검사도 그 행으로 루트를 찾지
    않습니다. 이 질문을 읽는 것은 `lib/optin.py#home_at` 하나뿐입니다. 손으로
    고칠 수 있는 행을 믿는 게이트는 폴더가 없는 자리를 찾아가게 되고, 그 모듈은
    짐작하는 쪽이 아니라 *옵트인하지 않음* 쪽으로 실패합니다. 그 행이 주는 것은,
    폴더를 옮기기 전에 저장소가 원하는 모드를 말할 수 있다는 것과, 남아 있는
    불일치를 검사가 이름 붙여 준다는 것입니다. 행이 없으면 폴더가 있는 자리로
    채웁니다.
  to: **`seal/config.json` 의 `Mode` 키는 옵트인이 아니고, 차이는 무엇이 그것을
    읽느냐에 있습니다.** 그 키는 루트가 *있어야 할* 자리를 말하고, 폴더의 자리는
    루트가 *있는* 자리를 말합니다. 어떤 훅, 게이트, 검사도 그 키로 루트를 찾지
    않습니다. 이 질문을 읽는 것은 `lib/optin.py#home_at` 하나뿐입니다. 손으로
    고칠 수 있는 키를 믿는 게이트는 폴더가 없는 자리를 찾아가게 되고, 그 모듈은
    짐작하는 쪽이 아니라 *옵트인하지 않음* 쪽으로 실패합니다. 그 키가 주는 것은,
    폴더를 옮기기 전에 저장소가 원하는 모드를 말할 수 있다는 것과, 남아 있는
    불일치를 검사가 이름 붙여 준다는 것입니다. 키가 없으면 폴더가 있는 자리로
    채웁니다.
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: shared 인가 local 인가
  from: `seal mode` 는 루트를 옮기고 `Mode`
    행을 쓰며,
  to: `seal mode` 는 루트를 옮기고 `Mode`
    키를 쓰며,
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: shared 인가 local 인가
  from: 검사가 설치되었는지를 말하는 설정 행은 없습니다.
  to: 검사가 설치되었는지를 말하는 설정 키는 없습니다.
- change
  file: docs/layout/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: `seal/config.md` is the one file a repository writes about itself, one row
    per item, read by the checkers and editable by hand. The rows that exist are
    documented in `templates/setup/config.md`, which also states what an absent
    row means, rather than leaving it to whoever reads the code.
  to: `seal/config.json` is the one file a repository writes about itself, one
    JSON object with one key per item, read by the checkers and editable by
    hand. The keys that exist are documented in `templates/setup/config.md`,
    which also states what an absent key means, rather than leaving it to
    whoever reads the code.
- change
  file: docs/layout/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: Every row is
    reachable from a command that shows the whole file and routes a change, because first
    setup asks its questions in one batch and never asks again, and the rows that
    arrive after it would otherwise be found only by reading a template a person
    has no reason to open. The routing layer holds no logic of its own: a row
    with a side effect routes to the script that performs it, and a row that is
    only a row is written directly.
  to: Every key is
    reachable from a command that shows the whole file and routes a change,
    because first setup asks its questions in one batch and never asks again,
    and the keys that arrive after it would otherwise be found only by reading
    a template a person has no reason to open. The routing layer holds no logic
    of its own: a key with a side effect routes to the script that performs it,
    and a key that is only a key is written directly.
- change
  file: docs/layout/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: so the language lives in a config
    row,
  to: so the language lives in a config
    key,
- change
  file: docs/layout/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: **Two rows, because one cannot express the middle answer.**
  to: **Two keys, because one cannot express the middle answer.**
- change
  file: docs/layout/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: One row cannot say the middle, and one row per document kind is seven rows
    where nobody sets the sixth differently from the fifth.
  to: One key cannot say the middle, and one key per document kind is seven keys
    where nobody sets the sixth differently from the fifth.
- change
  file: docs/layout/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: Whatever either row says,
  to: Whatever either key says,
- change
  file: docs/layout/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: **A cell may carry an escaped pipe, and one line that will not parse is named
    rather than treated as the end of the table.** A value like a shell command
    with a pipe in it is ordinary content, and a reader that stops at it
    silently takes every row below it out of the config. The reader and the writer
    share the constant that describes a row, because their disagreement about
    which line is a given row is what turns one edit into a duplicate row in a
    person's file.
  to: **The file is read by the standard library's JSON parser and written by its
    serializer, and what will not read is refused, never read as absent.** A
    parser's result is a fact a script reads exactly, and a markdown table read
    by a walker held to a renderer is not one: each shape the two could
    disagree on was a defect of its own. A file that will not parse, or whose
    top level is not an object, is refused whole. A key written twice, or one
    whose value is not a string, has no value, and every other key is read.
    Each value is a string in the grammar `templates/setup/config.md` gives
    its key, so a shell command carries a pipe as written. A `config.md` that
    stands in the root without a `config.json` is refused by every reader,
    and `seal mode` writes `config.json` from its `| Item | Value |` table and
    removes it.
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: 저장소가 스스로 정하는 것, 그리고 그것을 읽는 방법
  from: `seal/config.md` 는 저장소가 자기에 대해 적는 유일한 파일입니다. 항목마다 한
    행이고, 검사기가 읽으며, 손으로 고칠 수 있습니다. 있는 행은
    `templates/setup/config.md` 에 적혀 있고, 행이 없을 때 무엇을 뜻하는지도
  to: `seal/config.json` 은 저장소가 자기에 대해 적는 유일한 파일입니다. JSON
    객체 하나에 항목마다 키 하나이고, 검사기가 읽으며, 손으로 고칠 수 있습니다.
    있는 키는 `templates/setup/config.md` 에 적혀 있고, 키가 없을 때 무엇을
    뜻하는지도
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: 저장소가 스스로 정하는 것, 그리고 그것을 읽는 방법
  from: 모든 행은 파일
    전체를 보여 주고 변경을 연결해 주는 명령 하나로 닿을 수 있습니다. 처음 설정은
    질문을 한 번에 묻고 다시 묻지 않으므로, 그 뒤에 생긴 행은 사람이 열어 볼 이유가
    없는 템플릿을 읽어야만 찾을 수 있었을 것이기 때문입니다. 연결하는 층은 자기
    로직을 갖지 않습니다. 부작용이 있는 행은 그 일을 하는 스크립트로 보내고, 행일
    뿐인 행은 바로 씁니다.
  to: 모든 키는 파일
    전체를 보여 주고 변경을 연결해 주는 명령 하나로 닿을 수 있습니다. 처음 설정은
    질문을 한 번에 묻고 다시 묻지 않으므로, 그 뒤에 생긴 키는 사람이 열어 볼 이유가
    없는 템플릿을 읽어야만 찾을 수 있었을 것이기 때문입니다. 연결하는 층은 자기
    로직을 갖지 않습니다. 부작용이 있는 키는 그 일을 하는 스크립트로 보내고, 키일
    뿐인 키는 바로 씁니다.
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: 저장소가 스스로 정하는 것, 그리고 그것을 읽는 방법
  from: 그래서 언어는 설정 행에 두고,
  to: 그래서 언어는 설정 키에 두고,
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: 저장소가 스스로 정하는 것, 그리고 그것을 읽는 방법
  from: **행이 둘인 것은, 하나로는 가운데 답을 말할 수 없기 때문입니다.**
  to: **키가 둘인 것은, 하나로는 가운데 답을 말할 수 없기 때문입니다.**
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: 저장소가 스스로 정하는 것, 그리고 그것을 읽는 방법
  from: 행 하나로는 가운데를 말할 수 없고, 문서 종류마다
    행을 두면 아무도 여섯째를 다섯째와 다르게 두지 않는 행이 일곱 개가 됩니다.
  to: 키 하나로는 가운데를 말할 수 없고, 문서 종류마다
    키를 두면 아무도 여섯째를 다섯째와 다르게 두지 않는 키가 일곱 개가 됩니다.
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: 저장소가 스스로 정하는 것, 그리고 그것을 읽는 방법
  from: 어느 행이 무엇을 말하든
  to: 어느 키가 무엇을 말하든
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: 저장소가 스스로 정하는 것, 그리고 그것을 읽는 방법
  from: **셀에는 이스케이프한 파이프가 들어갈 수 있고, 해석되지 않는 줄 하나는 표의
    끝으로 취급하지 않고 이름을 붙여 알립니다.** 파이프가 들어간 셸 명령 같은 값은
    평범한 내용이고, 거기서 멈추는 읽기는 그 아래의 모든 행을 설정에서 조용히
    빼 버립니다. 읽는 쪽과 쓰는 쪽은 행을 설명하는 상수를 함께 씁니다. 어느 줄이
    그 행인지를 두고 둘이 엇갈리면 편집 한 번이 사람의 파일에 중복 행을 만들기
    때문입니다.
  to: **파일은 표준 라이브러리의 JSON 파서가 읽고 직렬화기가 쓰며, 읽히지 않는
    것은 없는 것으로 읽지 않고 거절합니다.** 파서의 결과는 스크립트가 정확히
    읽는 사실이고, 렌더러에 맞춘 워커가 읽는 마크다운 표는 그렇지 않습니다. 둘이
    엇갈릴 수 있는 모양마다 결함이 하나씩 났습니다. 해석되지 않는 파일과 맨 위가
    객체가 아닌 파일은 통째로 거절합니다. 두 번 적힌 키와 값이 문자열이 아닌 키는
    값이 없고, 나머지 키는 읽습니다. 값은 모두 `templates/setup/config.md` 가 그
    키에 정한 문법의 문자열이므로, 셸 명령은 파이프를 적힌 그대로 담습니다.
    `config.json` 없이 루트에 서 있는 `config.md` 는 모든 읽는 쪽이 거절하고,
    `seal mode` 가 그 `| Item | Value |` 표에서 `config.json` 을 쓰고 지웁니다.
- change
  file: docs/layout/the-record-layout.md
  section: Every kind of record, at a glance
  from: | The configuration | `seal/config.md`, one row per item; `templates/setup/config.md` documents every row | under target | the `Item` column |
  to: | The configuration | `seal/config.json`, one key per item; `templates/setup/config.md` documents every key | under target | its keys |
- change
  file: docs/layout/the-record-layout.md
  section: seal/
  from: | `seal/config.md` | what this repository says about itself, one row per item |
  to: | `seal/config.json` | what this repository says about itself, one key per item |
- change
  file: docs/layout/the-record-layout.md
  section: seal/
  from: | `seal/parity.md` | which codebase this repository ports behaviour from, and at which baseline commit; present only where a migration is declared |
  to: | `seal/parity.json` | which codebase this repository ports behaviour from, and at which baseline commit; present only where a migration is declared |
- change
  file: docs/checks/the-fold.md
  section: The fold, and what tells it from a deletion
  from: **A line that EXCUSES or DECLARES something — a `seal/config.md` row, a
    `routing.md` row — is not taken on doubt, except
    where a declaring reader keeps an older reading that took it.**
  to: **A line that EXCUSES or DECLARES something, such as a `routing.md` row, is
    not taken on doubt, except where a declaring reader keeps an older reading
    that took it.**
- remove
  file: docs/checks/the-fold.md
  section: The fold, and what tells it from a deletion
  from: `lib/config.py#hidden_lines`, which reads `seal/config.md`, keeps,
    wherever its walk is unsure, the fence-only reading it gave before the walk:
    a row below a fence nobody closed declares nothing, and a row below a
    comment opener nobody closed is not hidden, because that reading never hid
    one, and the walk may miss no row the older reading saw. That row declares
    nothing either: `lib/config.py#config_table` refuses a
    `| Item | Value |` header inside an HTML block opened above it and never
    closed, because GFM renders no table there, so every item of that table is
    a refusal, which a command prints with exit 2
    (`templates/setup/config.md` *Repository config*).
- change
  file: docs/checks/the-fold.md
  section: The fold, and what tells it from a deletion
  from: `lib/routing.py#shown`, which reads a `routing.md` and is not one of
    the four, keeps the reading it gave before the walk the same way, and that
    reading hid nothing:
  to: `lib/routing.py#shown`, which reads a `routing.md` and is not one of
    the four, keeps the reading it gave before the walk, and that reading hid
    nothing:
- change
  file: docs/checks/the-fold.md
  section: The fold, and what tells it from a deletion
  from: The holding bias would let a
    `seal/config.md` row quoted in an example declare a value nobody set,
  to: The holding bias would let a
    `routing.md` row quoted in an example declare a value nobody set,
- change
  file: docs/checks/the-pull-request-check.md
  section: What the check reads at the pull request
  from: where `seal/parity.md` is declared, the
    migration config's `Baseline commit`,
  to: where `seal/parity.json` is declared, the
    migration config's `Baseline commit`,
- change
  file: docs/checks/the-pull-request-check.md
  section: What the check reads at the pull request
  from: **Where `seal/parity.md` is declared and the change reaches outside
    `docs/` and `seal/`, every round record of a work item declaring `through the review chain` carries one `original:` line in its round block naming the migration config's baseline.** The check reads `seal/parity.md` at HEAD
  to: **Where `seal/parity.json` is declared and the change reaches outside
    `docs/` and `seal/`, every round record of a work item declaring `through the review chain` carries one `original:` line in its round block naming the migration config's baseline.** The check reads `seal/parity.json` at HEAD
- change
  file: docs/checks/the-pull-request-check.md
  section: What the check reads at the pull request
  from: Each
    refusal names the record, or the config, and both commits where two are
    compared.
  to: A `seal/parity.md` that git carries at HEAD without a `seal/parity.json`
    is refused once, naming the keys to write. Each refusal names the record,
    or the config, and both commits where two are compared.
- change
  file: docs/checks/the-pull-request-check.md
  section: What the check reads at the pull request
  from: `original:` line, or holds one whose commit and the
    `Baseline commit` row's SHA are not one a prefix of the other, and a
  to: `original:` line, or holds one whose commit and the
    `Baseline commit` key's SHA are not one a prefix of the other, and a
- change
  file: docs/checks/the-pull-request-check.md
  section: What the check reads at the pull request
  from: **Where `seal/parity.md` is declared and the change reaches outside
    `docs/` and `seal/`, the `guarantee.md` of a work item declaring
  to: **Where `seal/parity.json` is declared and the change reaches outside
    `docs/` and `seal/`, the `guarantee.md` of a work item declaring
- change
  file: docs/checks/the-pull-request-check.md
  section: What the check reads at the pull request
  from: the guarantee holds no such line, or one whose commit and the
    `Baseline commit` row's SHA are not one a prefix of the other.
  to: the guarantee holds no such line, or one whose commit and the
    `Baseline commit` key's SHA are not one a prefix of the other.
- change
  file: docs/forms/the-guarantee.md
  section: The guarantee
  from: where `seal/config.md`'s `Pull request seal mark` row reads `yes` and
  to: where `seal/config.json`'s `Pull request seal mark` key reads `yes` and
- change
  file: docs/forms/the-guarantee.md
  section: The guarantee
  from: The row's other
    values,
  to: The key's other
    values,
- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: `seal/config.md`'s `Release note seal mark` row reads `yes` at the tag,
  to: `seal/config.json`'s `Release note seal mark` key reads `yes` at the tag,
- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: states
    the row's values and who reads it.
  to: states
    the key's values and who reads it.
- change
  file: docs/releasing/release-checklist.md
  section: 6. After the merge
  from: `seal/config.md`'s `Release note seal mark` row reads `yes`;
  to: `seal/config.json`'s `Release note seal mark` key reads `yes`;
- change
  file: docs/running/the-broad-gate.md
  section: What the gate runs, and how the list is kept true
  from: The row naming the repository's broad command is read by the gate and
    by nobody else until the gate runs, so a value that cannot do what the row
    promises would otherwise be discovered at the one moment the run was supposed
    to save. The refusal names the form, quotes the value, and shows the row
    rewritten: exit 2, nothing run, the shape an absent row already takes. The
    criterion for choosing a value has one owner, the template that documents the
    row,
  to: The key naming the repository's broad command is read by the gate and
    by nobody else until the gate runs, so a value that cannot do what the key
    promises would otherwise be discovered at the one moment the run was
    supposed to save. The refusal names the form, quotes the value, and shows
    the key rewritten: exit 2, nothing run, the shape an absent key already
    takes. The criterion for choosing a value has one owner, the template that
    documents the key,
- remove
  file: docs/running/the-broad-gate.md
  section: What the gate runs, and how the list is kept true
  from: **A fenced example in a config file is not a config row.** The one walk of
    the `| Item | Value |` table reads the file through one fence rule, and the
    writer overwrites the line that walk names. A reader and a writer that
    disagree about which line is the row leave a file two rows deep that no
    command can bring into agreement, so a repair landing in the reader alone is
    half a repair.
    check: tests/lib/test_config.py tests/skills/test_seal.py tests/skills/test_broad_gate.py
- change
  file: docs/running/the-review-and-parity-arms.md
  section: The two arms
  from: The migration config lives at `seal/parity.md`, so declaring it
  to: The migration config lives at `seal/parity.json`, so declaring it
- change
  file: docs/running/the-review-and-parity-arms.md
  section: Parity arm
  from: Opt-in: `seal/parity.md`.
  to: Opt-in: `seal/parity.json`.
- change
  file: docs/running/what-a-script-gates.md
  section: The checks
  from: `seal/parity.md`'s `Baseline commit`
  to: `seal/parity.json`'s `Baseline commit`
- change
  file: docs/running/what-a-script-gates.md
  section: The checks
  from: | `seal gate`'s `Broad gate` row and arm 3 | the orchestrator's one run | the row's command's exit code; the gate's pytest recorder; the `Mode` row | refuses at exit 2 a row it would not run as the command it reads as,
  to: | `seal gate`'s `Broad gate` key and arm 3 | the orchestrator's one run | the key's command's exit code; the gate's pytest recorder; the `Mode` key | refuses at exit 2 a key it would not run as the command it reads as,
- remove
  file: docs/layout/the-pact.md
  section: The words
  from: **A pact headed with the word 0.18.x used still reads, and `seal pact`
    names the rename on it in no exit class.** Through 0.18.x a signer was
    called a signatory, and a pact's `| Signatory |` table carried that word
    into a file nobody regenerates. A file holding no table under the new header
    is read under the old one exactly as it would be under the new; a file
    holding one is read from it alone, and an old header beside it is refused,
    because its rows would otherwise go unread. `seal pact` prints one line
    naming the file, both headers and the release that renamed them before that
    file's other lines, and its exit is what the new header gives. No command
    rewrites a pact: the line says to rename the header when the file is next
    edited, and every text this plugin ships says `signer`.
    check: tests/skills/test_pact_check.py tests/lib/test_config.py
- remove
  file: docs/layout/the-pact.md
  section: The words
  from: A text that spells the 0.18.x header in order to
    read it, as the rule on a pact headed with that word says, names no signer
    another way.
- change
  file: docs/layout/the-pact.md
  section: How a signer names the pact
  from: **Every signer but the pact's repository names the pact in a `Pact` row
    of its `seal/config.md`, and one reader answers that row for every
    caller.**
  to: **Every signer but the pact's repository names the pact in a `Pact` key
    of its `seal/config.json`, and one reader answers that key for every
    caller.**
- change
  file: docs/layout/the-pact.md
  section: How a signer names the pact
  from: and stops nothing, so every reader of the row reads the same row. A `Pact`
    row written twice has no value at all: its first row is not the answer. A
    `Pact` row the config table does not hold is no row, so `seal pact` reads
    that signer as naming no pact, a relationship recorded on one side only.
  to: and stops nothing, so every reader of the key reads the same key. A `Pact`
    key written twice has no value at all. A config that holds no `Pact` key
    names no pact, so `seal pact` reads that signer as naming no pact, a
    relationship recorded on one side only.
- change
  file: docs/layout/the-pact.md
  section: The pact anchor
  from: a work item's `frame/design.md`, and `seal pact` reads the table with
    `lib/config.py#gfm_table`.**
  to: a work item's `frame/design.md`, and `seal pact` reads the table with
    `lib/tables.py#gfm_table`.**
- change
  file: docs/layout/the-pact.md
  section: The pact anchor
  from: pact's repository, as the signer's `Pact` row writes it, compared
  to: pact's repository, as the signer's `Pact` key writes it, compared
- change
  file: docs/layout/the-pact.md
  section: The pact anchor
  from: every `##` heading of `seal/pact.md`
    below its `| Signer |` table is a clause, and a `###` narrows inside one.
  to: every `##` heading of `seal/pact.md`
    is a clause, and a `###` narrows inside one.
- change
  file: docs/layout/the-pact.md
  section: The pact anchor
  from: The walker reads the table as GitHub renders it, as it reads every other
    table here, so nothing in a row is quoted or escaped except a pipe, written
    `\|`. A row naming another pact the signer's `Pact` row declares is passed
    over,
  to: The walker reads the table as GitHub renders it, as it reads every table
    of a record, so nothing in a row is quoted or escaped except a pipe, written
    `\|`. A row naming another pact the signer's `Pact` key declares is passed
    over,
- change
  file: docs/layout/the-pact.md
  section: The pact anchor
  from: row whose `Pact` cell names a pact the signer's `Pact` row does not declare,
  to: row whose `Pact` cell names a pact the signer's `Pact` key does not declare,
- change
  file: docs/layout/the-pact.md
  section: `seal pact` reconciles, locally
  from: **`seal pact`, run at the pact's repository, reads every signer the pact
    lists and says which way each mismatch points.** It finds each checkout
    through the `| Remote | Path |` table of `~/.claude/agentic/pact-paths.md`
    or the one sibling directory with that origin, guessing nothing;
  to: **`seal pact`, run at the pact's repository, reads every signer the
    `Pact signers` key of that repository's `seal/config.json` lists and says
    which way each mismatch points.** It finds each checkout through
    `~/.claude/agentic/pact-paths.json`, a JSON object from remote URL to
    checkout path, or the one sibling directory with that origin, guessing
    nothing;
- change
  file: docs/layout/the-pact.md
  section: `seal pact` reconciles, locally
  from: The map is read by `gfm_table`, as every other table is, and a map
    that is there and will not read, holds no such table, holds it twice, or has
    a row the walk does not read is refused at exit 2, because a row nobody reads
    reports its signer as not found. A remote written on two rows of the map is
    refused, and neither row is read.
  to: A map that is there and will not parse as a JSON object, or that holds a
    value that is not a path, is refused at exit 2, because an entry nobody
    reads reports its signer as not found. A remote written as two keys of the
    map, compared normalised, is refused, and neither is read. An absent or
    empty `Pact signers` key is refused at exit 2, because a pact nobody signs
    is not a pact.
- change
  file: docs/layout/the-pact.md
  section: What this does not see
  from: `seal pact` reads and the signer's `Pact` row,
  to: `seal pact` reads and the signer's `Pact` key,

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the `| Item | Value |` reader and its refusals | `lib/config.py#CONFIG_TABLE`, `#config_table`, `#config_rows`, `#config_text`, `#rows_named_below`, `#FIRST_CELL`; the per-row half of `#config_value` and `#value_of` | the JSON reader of *Data & interfaces*; a key is read or absent, so no line below a refusal is counted |
| the readers of `pact.md`'s and `parity.md`'s tables, and the 0.18.x header | `lib/config.py#read_table`, `#renamed_header`, `#RENAMED_IN`, `#SIGNER_HEADER`, `#pact_signers`, `#_signer`, `#PARITY_TABLE`, `#FIRST_CODE_SPAN`, `#baseline_commit`; `skills/verify/scripts/pact_check.py`'s call that prints the rename | `Pact signers` read through `remote_entries` (Scope item 5) and `parity.json`'s `Baseline commit` read by the parity arm (Scope item 4); a pact without the key is refused as a pact nobody signs |
| the walker and its helpers in `lib/config.py`, and the `lib/blocks.py` import | the units G11 lists; `lib/config.py`'s import of `blocks` | `lib/tables.py`, unchanged (Scope item 6) |
| the explanations of a `Broad gate` row the walker did not read | `skills/verify/scripts/broad_gate.py#config_text`, `#FIRST_CELL`, `#names_this_row`, `#refused_broad_row`, `#STOPPED_AT`, `#ROWS_BELOW`, `#IT_AND_ROWS_BELOW`, `#stopping_line`, `#rows_written_below`, `#fenced_row_at`, `#commented_row_at`, `#hidden_row_at`, `#fenced_row`, `#fence_left_open`, `#BARE_PIPE`, `#walker_refusal`, and the walker arms of `#missing_row` | a JSON key has no walker cause; the absent-key refusal stays |
| the table writer | `skills/implement/scripts/seal.py#NEW_CONFIG`, `#with_row`, `#doubled_modes`, `#line_ending`, `#ending_of`, the read-back guard in `#write_row`, and the re-exports `config_table`, `unfenced`, `fence_map`, `config_rows` | the serializer (*Data & interfaces*) |
| `fold_check.py`'s own walk of the config | `skills/settle/scripts/fold_check.py#config_rows` | `declared_value` |
| the map's table reading | `skills/verify/scripts/pact_check.py#path_map`'s table half and `#MAP_TABLE` | `json.loads` of `pact-paths.json` |
| the migration config template and its prose | `templates/setup/parity.md` | `templates/setup/parity.json`; the prose lands in `skills/legacy-parity/SKILL.md` *The migration config*, which already holds the machine-local paragraph and drops its copy |
| the `| Signer |` table and the paragraph introducing it | `templates/setup/pact.md` | `templates/setup/config.md` *Pact* documents `Pact signers` |
| the opening comment of a generated config | the comment in `seal.py#NEW_CONFIG` | `templates/setup/seal-README.md` *Layout* already says where every key is documented (G14) |
| the escaped-pipe rules, the walker's refusal list and the opening table | `templates/setup/config.md` *Broad gate* (the `\|` rows of *What is refused, and what stays allowed*), *Repository config*'s list of refused shapes, and its `| Item | Value |` table; `skills/config/SKILL.md`'s copy of that list | a fenced JSON example; a JSON string carries a pipe as written |
| "To create it, copy `templates/setup/config.md`" | `skills/commit-pr-convention/SKILL.md` *Every way of not naming a language lands on English*'s next paragraph | `seal mode` creates the file; the template is a document, not a file to copy |
| the cases that pin a walker refusal of a settings table, a `Signatory` pact, `with_row`'s line placement and `missing_row`'s walker arms | in `tests/lib/test_config.py`, `tests/skills/test_seal.py`, `tests/skills/test_broad_gate.py`, `tests/skills/test_pact_check.py` and `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py` | the code they pinned leaves; the walker's own cases and `tests/gfm_table_oracle.py` stay with `lib/tables.py`. The phase record names each case removed |
| the policy sentences *Rule changes* removes | `docs/running/the-broad-gate.md`, `docs/layout/the-pact.md`, `docs/checks/the-fold.md` | the settle |

This work adds a refusal of a `config.md` standing without a `config.json`, a refusal of a `parity.md` that git carries without a `parity.json`, `seal mode`'s converter, and `seal mode`'s line naming a `parity.md` it does not convert. In return the rows above go. Their record of what they caught is #867, #871, #925, #1119, #415, #429 and #430: shapes a markdown table can take and a JSON object cannot, so none of them can recur. The two refusals exist because a written file read as absent is the silent default #867 was opened about (G4).

Framed 2026-11-09 by framer, before the build.
