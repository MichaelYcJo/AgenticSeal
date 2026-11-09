# Review round 1: 1794200906-settings-are-read-as-json

```seal
target: f644cf8b against origin/release/v0.37.0
```

The diff read is `git diff c0bf670d f644cf8b`, where `c0bf670d` is the tip of `origin/release/v0.37.0` and the merge base. The merge at `5c094f77` brought in #1445 and #1459, and this round reviews only this item's commits. No earlier round exists, so no fact is carried and every fact below was established this round. Every `seal` command this round ran is the clone's own `bin/seal` at `f644cf8b`, never the installed 0.36.0 one, which reads no setting on this branch. The issue (`gh issue view 1454 -R MichaelYcJo/AgenticSeal`) has no comments, and its *Done when* holds for the readers. `seal/config.md`, `parity.md`'s table and `pact.md`'s signer table are read as JSON or replaced by keys. A repository holding the old files is converted or told how. The walker reads no settings file: the only `gfm_table(` calls outside `tests/`, `docs/` and `seal/threads/` are `skills/implement/scripts/seal.py:1574` (the converter), `skills/settle/scripts/settle.py:1072` and `skills/verify/scripts/pact_check.py:364`, and `lib/config.py:48-50` imports `json`, `os` and `re` alone (executed: `git grep -n 'gfm_table('`).

## Findings

### 1. The changelog, both READMEs, the template and the frame say every `seal` command exits 2 on an unconverted `config.md`, and `seal rules`, `seal settle` and `seal unverified` do not

```seal
severity: should
location: `seal/threads/1794200906-settings-are-read-as-json/changelog.md:4`, `seal/threads/1794200906-settings-are-read-as-json/changelog.md:10`, `seal/threads/1794200906-settings-are-read-as-json/pr.md:8`, `README.md:105-106`, `README.ko.md:108-109`, `templates/setup/config.md:54-55`, `skills/implement/bootstrap.md:114-115`, `seal/threads/1794200906-settings-are-read-as-json/frame/plan.md:54`, `seal/threads/1794200906-settings-are-read-as-json/frame/design.md:259-262`, `seal/threads/1794200906-settings-are-read-as-json/frame/design.md:326-327`, `lib/config.py:358-373`
evidence: executed `bin/seal rules --check` in a scratch repository holding `seal/config.md` with `| Policy root | policies |` and a `policies/a.md` whose `check:` names a missing file, before and after `bin/seal mode`; executed `bin/seal gate --base HEAD`, `bin/seal fold` and `bin/seal mode --check` in the same repository; read `lib/config.py:310-373`, `.github/scripts/rules.py:233`, `skills/verify/scripts/unverified_check.py:978-987`
```

Why it matters: the changelog's *Updating* line becomes the release note a person acts on, and it says "until then every `seal` command that reads a setting exits 2". The *Changed* item, `pr.md`'s quote, both READMEs, `templates/setup/config.md:54` ("every reader refuses it and names `seal mode`"), `skills/implement/bootstrap.md:114` ("every `seal` command that reads it refuses"), `frame/plan.md` *Operational impact* and the design's *Rule changes* `to:` for `docs/layout/one-root-by-lifetime.md` and its Korean edition say the same. The code does not do that. `lib/config.py#policy_root` (`:366`) and `#reference_roots` (`:318`) take `declared_value`'s value and drop its refusal, by their documented contract, so an unconverted `config.md` reads as the default `docs` and the default `specs` rule. The probe shows it. In the scratch repository `seal rules --check` printed "all 0 check lines in 0 rule files hold" and exited 0 before `seal mode`. After `seal mode` it read `policies/`, refused the missing check target and exited 1. `seal settle` reads the policy root the same way (`unverified_check.py:987`), and `seal unverified` reads the reference roots (`:978`). `seal gate`, `seal fold` and `seal mode --check` did exit 2 naming `seal mode`. The code matches design *Scope* item 3 and S3, which name `seal gate`, `seal pr-body`, `seal fold` and `seal mode --check`. Only the sentences overreach. A person told every command refuses reads a 0 from `seal rules --check` as a pass over the policy root they declared. The other repair, making `policy_root` and `reference_roots` refuse an unconverted file, changes a contract both docstrings argue for (`lib/config.py:310-314`, `declared_pacts`' docstring at `:555-562`), so the paste-ready fix below rewrites the sentences. The fix pass owes every statement listed in `location:`, and `pr.md`'s quote changes with the changelog line it quotes.

```markdown
changelog.md:4, the sentence beginning "Until the conversion":
Until the conversion, `seal gate`, `seal pr-body`, `seal fold`, `seal pact` and `seal mode --check` exit 2 and name `seal mode`, and `seal rules`, `seal settle` and `seal unverified` read the `Policy root` and `Reference specs` defaults, as they do for any config they cannot read.

changelog.md:10, the first two sentences of the Updating line (and pr.md:8 quotes them as written here):
Updating: run `seal mode` once in each repository that holds `seal/config.md`. It writes `seal/config.json` from the table and removes the old file, and until then `seal gate`, `seal pr-body`, `seal fold`, `seal pact` and `seal mode --check` exit 2, and `seal rules`, `seal settle` and `seal unverified` read the default policy root and reference roots.

README.md:105-106:
the old file. Until then `seal gate`, `seal pr-body`, `seal fold`, `seal pact`
and `seal mode --check` exit 2 and name `seal mode`, and `seal rules`,
`seal settle` and `seal unverified` read the default policy root and
reference roots.

README.ko.md:108-109:
그 표에서 `seal/config.json` 을 쓰고 옛 파일을 지웁니다. 그 전까지는
`seal gate`, `seal pr-body`, `seal fold`, `seal pact`, `seal mode --check` 가
종료 코드 2 로 멈추고 `seal mode` 를 짚으며, `seal rules`, `seal settle`,
`seal unverified` 는 정책 루트와 참고 루트를 기본값으로 읽습니다.

templates/setup/config.md:54-55:
table. Where the root holds `config.md` and no `config.json`, every command
that refuses a config it cannot read (`seal fold`, `seal gate`, `seal mode`,
`seal pact`, `seal pr-body`) refuses it and names `seal mode`, and the
readers of `Policy root` and `Reference specs` read their defaults. Bare
`seal mode` writes `config.json`

skills/implement/bootstrap.md:114-115:
   bare `"` ends the string, so the file no longer parses and `seal gate`,
   `seal pr-body` and every other command that refuses an unreadable config
   refuses it, and a bare `\` before `t` or `n` reads as

frame/plan.md:54, the sentence beginning "Until it does":
Until it does, `seal gate`, `seal pr-body`, `seal fold`, `seal pact` and `seal mode --check` exit 2 and name `seal mode`, and nothing runs; `seal rules`, `seal settle` and `seal unverified` read the default policy root and reference roots.

frame/design.md:259-262, inside the `to:` value:
    its key, so a shell command carries a pipe as written. A `config.md` that
    stands in the root without a `config.json` is refused by every reader that
    refuses a file it cannot read, and read as no file by the readers of
    `Policy root` and `Reference specs`, and `seal mode` writes `config.json`
    from its `| Item | Value |` table and removes it.

frame/design.md:326-327, inside the `to:` value:
    `config.json` 없이 루트에 서 있는 `config.md` 는 읽지 못하는 파일을 거절하는
    읽는 쪽이 모두 거절하고 `Policy root` 와 `Reference specs` 를 읽는 쪽은 파일이
    없는 것으로 읽으며, `seal mode` 가 그 `| Item | Value |` 표에서 `config.json`
    을 쓰고 지웁니다.
```

```seal
verdict: fixed f8d33094
answer: Applied the paste-ready text at changelog.md:4 and :10, pr.md:8's quote, README.md, README.ko.md, templates/setup/config.md's conversion paragraph, skills/implement/bootstrap.md, frame/plan.md *Operational impact* and both design `to:` values. Before applying it I checked the list of commands that stop: `seal pact` was not among the round's probes, so I ran the tree's `bin/seal pact` in a scratch pact repository holding an unconverted `config.md`, and it exited 2 naming `seal mode` (executed). `git grep` for the same claim found three more statements of it, fixed in the same commit. `frame/plan.md:11` said a trailing comma makes "every `seal` command" exit 2. The template's paragraph on an unreadable file listed four commands as "a command a person runs" and now names the five that stop and the three that read defaults. `skills/config/SKILL.md:108-111` said "a command prints it and runs or writes nothing"; it now points at the template, because restating the list there failed `tests/text/test_no_passage_is_pasted_into_a_second_file.py` against README.md. `1577b86e` rewraps that paragraph. `lib/config.py:358-373` is unchanged: its docstrings state the defaults the code reads, and the finding's fix rewrites only the sentences that overreached.
```

### 2. Four shipped texts an agent reads still call a setting a row

```seal
severity: should
location: `agents/sealer.md:153`, `skills/code-review/SKILL.md:63`, `skills/writing-style/outside-the-review.md:34`, `skills/settle/SKILL.md:296`
evidence: executed `git grep -nwE "rows?|행"` over `agents/*.md`, `skills/**/*.md`, `templates/**`, `README.md`, `README.ko.md`, `seal/README.md`, `CONTRIBUTING.md`, `CLAUDE.md`, `hooks/*`, and each remaining line read; executed `git grep -n -C3` around every key name and `config.json` in the same files for `rows?`, `cell` and `행`; read `agents/sealer.md:150-155`, `skills/code-review/SKILL.md:55-63`, `skills/writing-style/outside-the-review.md:20-36`, `skills/settle/SKILL.md:292-298`
```

Why it matters: design *Scope* item 7 says a setting is a "key" in every rewritten sentence. A13 rejects "row" because the word names a table that no longer exists. Each line below is read by an agent at a step and names the setting by the old word:

- `agents/sealer.md:153`: "Choose a `Broad gate` command, or draw a stamp: the row is a person's". The `Broad gate` key is meant.
- `skills/code-review/SKILL.md:63`: "naming a remote one letter off a pact that row declares". The paragraph opens at `:55` with "Where `seal/config.json` has a `Pact` key", and the diff rewrote that line and left this one.
- `skills/writing-style/outside-the-review.md:34`: "두 행이 같은 언어면 `pr.md` 하나". The same paragraph's `:22`, which the diff rewrote to "두 언어 키", names the two language keys.
- `skills/settle/SKILL.md:296`: "no configuration row names one". `docs/checks/the-fold.md:191` holds the same sentence, and finding 3 carries its entry.

Phase 5's account (`trail/phases/phase-5.md`, the paragraph after the census) says it read the skills, agents and templates the patterns list for a bare "the row" meaning the `Broad gate` command, and it calls that read a sample. `agents/sealer.md` is on the pattern list (`config.json` stands at `:102`), and `:153` is that sense. So the sample missed an instance in a file it names as read. The other three lines use other senses, and the patterns did not reach them. My own list is a sample too. It reads every "row" or "행" word in the shipped markdown, and it reads Python docstrings and comments only near a key name or `config.json`. A docstring calling a setting a row with no key name in the three lines around it is not on it.

```markdown
agents/sealer.md:153:
- Choose a `Broad gate` command, or draw a stamp: the key is a person's, and

skills/code-review/SKILL.md:63:
naming a remote one letter off a pact that key declares.

skills/writing-style/outside-the-review.md:34:
이은 글(두 키가 같은 언어면 `pr.md` 하나)과 한 줄이라도 다르거나 뒷부분이

skills/settle/SKILL.md:296:
such a directory on its own, and no configuration key names one. Which
```

```seal
verdict: fixed b5715ae5
answer: Applied the four lines as given. I then listed every "row" and "행" word in shipped markdown with `git grep -nwE 'rows?|행'` over agents, skills, templates, both READMEs, seal/README.md, CONTRIBUTING.md, CLAUDE.md and hooks, 361 lines, and read each one. One more line meant a setting: `agents/sealer.md:84`, "the quotes rendered in the commit language where the rows differ", which now says keys. Every other hit names a table that still exists, such as routing.md, a plan's phases, a panel or the anchor table. I listed every "row" word in the shipped Python under lib, skills, .github and hooks (891 lines) and read the hits in the files that read a setting. Each names a panel row, an anchor row or a row of an old `config.md`. Three test docstrings and one comment said "where the rows differ" or "naming the two rows" for the language keys, in `tests/skills/test_pr_body.py`, `tests/skills/test_chain_check.py` and `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`, and now say keys. The Python list is a sample: I read hits only in the settings readers, and test identifiers such as `test_seal.py`'s ids "no row" and "two rows" stay, as gaps.md *Not done* says of identifiers.
```

### 3. Design *Rule changes* leaves six `docs/` lines that call a setting a row, five of them in `docs/running/the-broad-gate.md`

```seal
severity: should
location: `seal/threads/1794200906-settings-are-read-as-json/frame/design.md:471-480`, `docs/running/the-broad-gate.md:40-63`, `docs/checks/the-fold.md:191`, `seal/threads/1794200906-settings-are-read-as-json/gaps.md:15`
evidence: executed `git grep -nE` with design *Scope* item 7's patterns and `configuration row` over `docs/`, and `git grep -n -C4` around each key name, `config.json`, `config.md` and `broad command` over `docs/` for `rows?` and `행`, each hit compared with every `from:` of design *Rule changes*; read `docs/running/the-broad-gate.md:1-110`, `docs/checks/the-fold.md:180-193`
```

Why it matters: the settle writes `docs/` only from *Rule changes*. A sentence it holds no operation for stays as it is after the settle. `gaps.md:15` names five lines of `docs/running/the-broad-gate.md` *One act, one owner, and the owner is the orchestrator* that call the `Broad gate` command "the row" (`:41`, `:44`, `:45`, `:57`, `:63`). The design rewrites two other paragraphs of that file to "key", so after the settle the file would call one thing a key in one section and a row in the one above it. That is the sentence standing on the old fact which design G1 and `skills/core/SKILL.md` *The rule a mechanism is kept against* ask to be rewritten. The search above found one more line no entry reaches: `docs/checks/the-fold.md:191`, "no configuration row names such a directory", the policy copy of finding 2's `skills/settle/SKILL.md:296`. Every other hit of that search has an entry. *Rule changes* owes the operations below, after the last `docs/running/the-broad-gate.md` entry at `frame/design.md:480`. `gaps.md`'s third *Not done* paragraph (`:15`) then states something false and is removed in the same commit.

On the wording, the five lines speak of the exit status of the command the gate ran, not of the setting. "The command's exit" is what `skills/verify/scripts/broad_gate.py:82`, `:1345` and `:1360` say, and so does `templates/setup/config.md` *The criterion for choosing a value* rule 3, which `:61-63` of the same paragraph cites. So these operations say "the command". The existing `to:` sentences name the setting itself ("The key naming the repository's broad command", "shows the key rewritten") or its value through the key ("the key's command's exit code"). The shipped texts use "the key's command" too (`broad_gate.py:102`, `templates/setup/config.md:303`). Each wording has one reading in its sentence, so the two need not be made one, and the existing entries stay as written.

```markdown
- change
  file: docs/running/the-broad-gate.md
  section: One act, one owner, and the owner is the orchestrator
  from: has not passed, whatever the row's exit.**
  to: has not passed, whatever the command's exit.**
- change
  file: docs/running/the-broad-gate.md
  section: One act, one owner, and the owner is the orchestrator
  from: runs after the loop can change the row's exit and not that one. So an
    exit of 0 from the row does not say that nothing the session ran
    failed.
  to: runs after the loop can change the command's exit and not that one. So
    an exit of 0 from the command does not say that nothing the session ran
    failed.
- change
  file: docs/running/the-broad-gate.md
  section: One act, one owner, and the owner is the orchestrator
  from: Where the row exited 0, its failure form says so
  to: Where the command exited 0, its failure form says so
- change
  file: docs/running/the-broad-gate.md
  section: One act, one owner, and the owner is the orchestrator
  from: names the acts after the run loop that can turn the
    row's exit into 0,
  to: names the acts after the run loop that can turn the
    command's exit into 0,
- change
  file: docs/checks/the-fold.md
  section: The fold, and what tells it from a deletion
  from: and no configuration row names such a
    directory.
  to: and no configuration key names such a
    directory.
```

```seal
verdict: fixed 97b56c17
answer: Added the five operations after the last `docs/running/the-broad-gate.md` entry, and removed gaps.md's third *Not done* paragraph in the same commit. To check that each `from:` stands in its section, I ran the tree's `bin/seal settle --draft --released-at HEAD` in a scratch worktree at `97b56c17`, and it placed 98 of 99 operations (executed). The five new ones were placed: the drafted `docs/running/the-broad-gate.md` holds no "row" meaning the command, and `docs/checks/the-fold.md` reads "no configuration key names such a". The one unplaced operation is another work item's, `1794188289-the-body-reads-in-the-teams-language/frame/design.md:226`. The scratch worktree was then removed.
```

### 4. Both READMEs send a person upgrading to an unnamed release note for the three hand-written files, and name none of their targets

```seal
severity: should
location: `README.md:106-108`, `README.ko.md:110-112`
evidence: read `README.md:60-110`, `README.md:296-310`, `README.ko.md:100-112`, `frame/plan.md:64`, `seal/threads/1794200906-settings-are-read-as-json/changelog.md:10`
```

Why it matters: read as a person upgrading a repository that holds `seal/config.md`, the paragraph tells them to run `seal mode`, which is enough for the config. For the other three files it says only that they "are rewritten by hand, as the release note of the release that made the change says". The README neither names nor links that note. It does not say what any of the three becomes: the `Pact signers` key and `pact-paths.json` appear nowhere in either README, and `parity.json` appears only in *Migrations* (`README.md:302`). `frame/plan.md:64` records the owner's ask of 2026-11-09 that the READMEs state everything this release changes. The changelog's *Updating* line already holds the three targets in one sentence each, so the README can carry them without naming a version, which the phase 5 departure on "Earlier releases" avoids for `tests/behaviour/test_release_hygiene.py`.

```markdown
README.md:106-108:
and names `seal mode`. Three files no command converts are rewritten by
hand. `seal/parity.md` becomes `seal/parity.json`, written from
`templates/setup/parity.json`. The `| Signer |` table of a `seal/pact.md`
becomes a `Pact signers` key in that repository's `seal/config.json`, the
remote URLs separated by `;`. `~/.claude/agentic/pact-paths.md` becomes
`~/.claude/agentic/pact-paths.json`, one JSON object from remote URL to
checkout path.

README.ko.md:110-112:
어떤 명령도 바꿔 주지 않는 세 파일은 손으로 다시 씁니다. `seal/parity.md` 는
`templates/setup/parity.json` 에서 시작해 `seal/parity.json` 으로 씁니다.
`seal/pact.md` 의 `| Signer |` 표는 그 저장소 `seal/config.json` 의
`Pact signers` 키가 되고, 원격 URL 은 `;` 로 구분합니다.
`~/.claude/agentic/pact-paths.md` 는 원격 URL 에서 체크아웃 경로로 가는 JSON
객체 하나인 `~/.claude/agentic/pact-paths.json` 이 됩니다.
```

The fix pass applies this after finding 1's README edit, which rewrites the sentence before it.

```seal
verdict: fixed 0ed9487e
answer: Applied both READMEs' text after finding 1's edit. The English text begins at "Three files no command converts", because finding 1's sentence now ends the paragraph's first part, and the Korean text is as given. `templates/setup/parity.json` stands in the tree (read), and `tests/behaviour/test_release_hygiene.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/text` pass over both READMEs (executed).
```

### 5. A byte order mark reads in `config.json` and is refused in `parity.json` and `pact-paths.json`

```seal
severity: should
location: `lib/config.py:600-603`, `skills/verify/scripts/pact_check.py:392-397`
evidence: executed `python3 -I test_tmp_bom.py <clone>` (one probe, three files written with a leading U+FEFF); read `lib/config.py:126-142`, `skills/code-review/scripts/chain_check.py:495-506`, `skills/verify/scripts/pact_check.py:298-304`
```

Why it matters: design G12 found that a byte order mark makes `json.loads` raise and that `utf-8-sig` reads it, and S2 makes "A byte order mark reads" part of the contract for `config.json` (`lib/config.py:138`). This work also introduces two more JSON settings files, which an editor that writes the mark writes the same way. The probe gave `config_pairs` the members of a `config.json` with the mark. `baseline_commit` refused the same object as `parity.json` with "does not parse as JSON (Unexpected UTF-8 BOM ...)", and `path_map` refused a `pact-paths.json` whole. `chain_check.py#read_record` reads `parity.json` through `git show` or `open(..., encoding="utf-8")`, and `pact_check.py#read` opens the map as `utf-8`, so both texts reach `json.loads` with U+FEFF in front. A repository whose `parity.json` carries the mark has every ready pull request refused by the parity arm. Its `config.json` written by the same editor reads. Taking the mark off where the text is parsed covers both callers of `baseline_commit` (HEAD and `--worktree`). Each change owes a case in `tests/lib/test_config.py#Test_baseline_commit` and `tests/skills/test_pact_check.py#Test_path_map` (`skills/code-review/SKILL.md` *Regression test*). The `baseline_commit` and `path_map` docstrings, and `skills/legacy-parity/SKILL.md` *The migration config*, can say the mark reads, as `templates/setup/config.md:47-48` does for the config.

```python
# lib/config.py, beside CONFIG: the mark an editor may write first, which
# `config_pairs` already reads past by decoding `utf-8-sig`.
BOM = chr(0xFEFF)  # NAME NOT IN TREE: added by this fix

# lib/config.py, baseline_commit
    try:
        parsed = json.loads(text.removeprefix(BOM), object_pairs_hook=Members)
    except ValueError as exc:
        return None, f"does not parse as JSON ({exc})"

# skills/verify/scripts/pact_check.py, path_map
    try:
        parsed = json.loads(
            text.removeprefix(config.BOM), object_pairs_hook=config.Members
        )
    except ValueError as exc:
```

```seal
verdict: fixed 9d094d40
answer: Added `lib/config.py#BOM` and took it off the text before the parse in `baseline_commit` and in `pact_check.py#path_map`, as the paste-ready code gives. Each fix has a new case, `tests/lib/test_config.py#Test_baseline_commit::test_reads_past_a_byte_order_mark_an_editor_wrote` and `tests/skills/test_pact_check.py#Test_path_map::test_reads_past_a_byte_order_mark_an_editor_wrote`. Both were run before the fix and failed on "Unexpected UTF-8 BOM" (executed). After the commit, `bin/seal mutate` put back the unstripped parse in each unit, and each verdict was red, exit 0 (executed). The two docstrings and `skills/legacy-parity/SKILL.md` *The migration config* now say the mark reads. The first commit wrote the mark as an invisible literal character. `1577b86e` spells it `chr(0xFEFF)` in the constant and in both cases, and both mutation runs were repeated after it, red again (executed).
```

### 6. The changelog says the walker "reads records only", and two of its callers read policy documents and rule files

```seal
severity: should
location: `seal/threads/1794200906-settings-are-read-as-json/changelog.md:7`, `seal/threads/1794200906-settings-are-read-as-json/pr.md:6`, `lib/tables.py:6`
evidence: executed `git grep -n 'tables()\|sibling("tables")\|load(TABLES\|tables\.py' -- '*.py' ':!tests'`; read `skills/settle/scripts/rule_changes.py:365-380`, `.github/scripts/rules.py:155-165`, `skills/settle/rule-changes.md:27`
```

Why it matters: the changelog's fifth *Changed* item opens "The table walker lives in `lib/tables.py` and reads records only", and `pr.md:6` quotes it. Its next sentence names `seal mode`'s conversion of `config.md`, which is no record. `skills/settle/scripts/rule_changes.py#_last_row` (`:372`) calls `table_cells` and `opens_table` to place an `add` operation's table row into a policy document (`skills/settle/rule-changes.md:27`). `.github/scripts/rules.py:163`, which `seal rules` runs, calls `unfenced` over the rule files it reads. `lib/tables.py:6` says "Its callers read records" and then lists those two callers. The fact the item ships is that no setting is read through the walker, which S8 holds. "Records only" is a claim the release note would carry and the tree contradicts.

```markdown
changelog.md:7 (and pr.md:6 quotes its bold sentence as written here):
- **The table walker lives in `lib/tables.py`, and no setting is read through it.** It reads a frame's anchor table, *Judgments of the run*, the table row `settle --draft` places in a policy document and the lines `seal rules` reads, and `seal mode` converts an old `config.md` through it. `lib/config.py` holds the settings alone.

lib/tables.py:5-6:
cells, and `unfenced` and `table_cells` are the fence rule and the cell
split it reads through. Its callers read records and policy documents: the pact anchor table of
```

The `lib/tables.py` line is reflowed to the file's width when it is applied.

```seal
verdict: fixed c239f2ad
answer: Applied the changelog item and `pr.md:6`'s quote as given, and reflowed the `lib/tables.py` docstring to its width. `git grep` for the same claim found `frame/plan.md` A12, "the walker's lines ..., which read records", which now says they read records and policy documents and no setting. Every quote in `pr.md` stands word for word in `changelog.md` after the fix (executed: a substring check of each quote).
```

## Confirmations

What matched: the reader's states in design *Data & interfaces* hold at `lib/config.py:103-217`. No file reads as nothing, a `config.md` alone, an undecodable file, an unparseable file and a non-object top level are refusals, a key written twice and a value that is not a string are refused for that key alone, and a byte order mark reads (read, and executed through the probe in finding 5).

What matched: S4 and S5 hold at `skills/implement/scripts/seal.py:1536-1612` and `:2194-2271` (read). In the scratch repository bare `seal mode` wrote `{"Mode": "shared", "Policy root": "policies", "Reference specs": "none"}` in the table's order, removed `config.md`, and reported "They agree" (executed).

What matched: S3 for `seal gate`, `seal fold` and `seal mode --check`. Each exited 2 naming `seal mode` on an unconverted `config.md` (executed). `seal pr-body` was not run, and `pr_body.py:446` reads through `declared_value` and refuses on its refusal (read).

What matched: S8 holds, as the opening paragraph gives (executed).

What matched: `pr.md`'s nine quotes are found word for word in `changelog.md` at the coordinates each names (read). Both language keys are `English` in `seal/config.json`, so no `pr.<lang>.md` is owed.

What matched: the converter reads values as the old reader did. `seal.py#converted` takes `gfm_table`'s cells, which are stripped and unescaped as `lib/config.py#config_table` returned them at `c0bf670d`, so a converted `Broad gate` runs the command the old row ran (read `git show c0bf670d:lib/config.py`, `:311-360` and `:444-528`).

What matched: phase 5's departures. The "the command" wording has one reading in each sentence it stands in (finding 3 weighs it against the *Rule changes* wording). The hygiene step name is read only against this repository's `release` job (`skills/verify/scripts/broad_gate.py:1751`, `:1832`), and the template's job is `hygiene` (`templates/setup/hygiene.yml:56`), so a workflow an earlier release wrote into a user's repository is not misclassified. "Earlier releases" in the READMEs is the wording `tests/behaviour/test_release_hygiene.py` allows, and finding 4 weighs what the paragraph leaves out. The four replacement cases stand at `tests/behaviour/test_first_setup_asks_once.py:224`, `:269`, `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:660` and `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:42`, and their files pass (executed). The kept identifiers (`missing_row`, `ROW_NOT_RUN`, `BROAD_ROW`, `LANGUAGE_ROWS`, two test file names) are read by no party at a step, and `ROW_NOT_RUN`'s printed text holds no "row" (`broad_gate.py:2557`, read).

What matched: the `seal layout --pairs` notices over the 39 changed test files are seven pairs, and every case in them stood at `c0bf670d` (executed: `bin/seal layout --pairs`, then `git grep -c "def <name>" c0bf670d`). `seal layout --check` over the same files exited 0 (executed).

What matched: `chain_check.py --baseline origin/release/v0.37.0 --worktree` over the worktree with this record prints twelve test-pin notices at `frame/design.md:355` (the `remove` of the `docs/checks/the-fold.md` paragraph) and `:474` (the `remove` of the fenced-row paragraph of `docs/running/the-broad-gate.md`) (executed). Each named pin shares words with the removed text without holding its wording. "a fence nobody closed" is a corpus shape name (`tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:57`, `:203`), "| Item | Value |" is a walker fixture header (`tests/block_shapes.py:58`, `tests/lib/test_tables.py:441`, `:472`), and "inside an HTML block opened above it and never closed" is the walker's own refusal sentence (`tests/lib/test_tables.py:562`). So none is a finding. The pin `gaps.md:13` names, the `#hidden_lines` row of that test's `TABLE`, is not among the notices, and the settle owes it as `gaps.md` says.

Outside this item: `templates/setup/config.md:20-25` says a root with no `Mode` key has "the first Bash call of a session in that repository denied", and `skills/implement/scripts/seal.py:1418` names "a `PreToolUse` gate". `hooks/hooks.json` holds only a `Stop` and a `SessionStart` hook, and no `PreToolUse` hook is shipped (read). The sentence predates this branch (`git log -S'first Bash call'` names `e391ea04`). This diff rewrote it from row to key and kept the claim. It is named here for the orchestrator to route, not as this item's finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The whole suite, the repository-wide lint and the format check at `f644cf8b` (`unverified`); this round ran only the module sets in *Probes* | the branch at `f644cf8b` | the orchestrator, through this worktree's own `bin/seal gate` |
| Whether the 25 moved walker units equal the base's by `ast`, as phase 4 claims; this round ran `tests/lib/test_tables.py` and did not re-run the comparison | `lib/tables.py` | the sealer, where it samples the crafter's claims |
| Whether `frame/questions.md` Q1's default (no converter for `parity.md`, the signer table and `pact-paths.md`) is the owner's answer | `seal/threads/1794200906-settings-are-read-as-json/frame/questions.md` Q1 | the owner |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/lib/test_config.py tests/lib/test_tables.py tests/skills/test_seal.py tests/skills/test_pact_check.py` in the clone | exit 0, 712 passed |
| `bin/test -q tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` in the clone | exit 0, 155 passed |
| `bin/seal gate --base HEAD`, `bin/seal fold`, `bin/seal mode --check` in a scratch repository holding only `seal/README.md` and an unconverted `seal/config.md` | each exit 2, naming `seal mode` |
| `bin/seal rules --check` in the same repository, with `Policy root` `policies` in `config.md` and a missing `check:` target in `policies/a.md`, then `bin/seal mode`, then `bin/seal rules --check` again | exit 0 "all 0 check lines in 0 rule files hold"; then `config.json` written and `config.md` removed, exit 0; then exit 1 naming `policies/a.md:6` |
| `python3 -I test_tmp_bom.py <clone>`: `config_pairs`, `baseline_commit` and `pact_check.path_map` over files opening with U+FEFF | `config.json` read; `parity.json` and `pact-paths.json` refused, "Unexpected UTF-8 BOM (decode using utf-8-sig)" |
| `bin/seal layout --pairs` and `--check` over the 39 test files the diff changes | 7 pairs, each standing at `c0bf670d`; check exit 0 |
