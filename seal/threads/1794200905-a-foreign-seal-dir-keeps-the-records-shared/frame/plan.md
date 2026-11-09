# Implementation Plan: 1794200905-a-foreign-seal-dir-keeps-the-records-shared

## Technical context

The tree as read at `872ff59c`.

`lib/optin.py#home_paths` (`:158`) is the one place that says where each mode's root would be, and `#home_at` (`:219`) reads those places in order against `#marked` (`:195`). Most readers already go through `home_at`: `pr_body.py:443`, `seal_stamp.py:1279`, `fold_check.py:269`, `release_seal.py:427` and `lib/core.py` through `opted_in`. `seal.py#resolve` (`:363`), `broad_gate.py#seal_home` (`:649`), `pact_check.py:650` and `chain_check.py#local_root` (`:1827`) take the shared place from `home_paths`, so *Scope* item 1 reaches these four units without an edit to them; other units of the same modules still spell the name. The readers that spell the name are the modules `frame/design.md` *Scope* items 2 and 3 list. There are two kinds. Some build a disk path, such as `os.path.join(root, "seal")` at `.github/scripts/rules.py:229`, `settle.py:1297` and `rule_changes.py:576`. Others classify a repository-relative path as git prints it, such as `routing.WORK_ITEMS` in `chain_check.py:1405` and `:1840`, `gate.DOC_ROOTS`, the regex at `publish_release_note.py:139`, and the `basename == "seal"` tests at `seal_stamp.py:1327` and `unverified_check.py:1248`, `:1276` and `:1301`. A disk-path reader takes `home_at` or `home_paths`. A classifying reader takes the repository-relative name (`frame/design.md` *Data & interfaces*).

The constraint that shapes the order of phases: `lib/routing.py#WORK_ITEMS`, `lib/gate.py#DOC_ROOTS` and `lib/config.py#HOME` each have callers in several scripts, so a phase that removes one changes its callers in the same phase, and the suite stays green at every phase's close.

Failure scenario of the chosen approach, six months on: a reader added after this work builds `<root>/agentic-seal` or `<root>/seal` itself, or compares a basename with a literal. The text case of *Scope* item 4 refuses the literal. A reader that derives the name some other way, such as from `optin.HOME` joined under the root, passes that case. In a repository whose root is `agentic-seal/`, it then reads nothing, and only a case built on the foreign-`seal/` fixture would show it. The fixture of *Scope* item 6 is the one to extend. A second failure: a repository whose `seal/` and `agentic-seal/` both carry the marker reads `seal/` and never says the other exists. That state needs two first setups, and it is a limit stated in `home_paths`'s docstring.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the structure: a foreign `seal/` sends the root to local mode (#1051, G1) | A team whose repository keeps its own `seal/` cannot share records or run the pull request checks, which is the issue. The premise that keeps it, that a second place costs a configured name, is false: a second fixed name found by the same marker needs no configuration. | rejected |
| Replace the structure: rename the root to `agentic-seal/` for every repository | Every repository with a marked `seal/` moves its root, and every shipped sentence spelling `seal/` either changes or reads through the core's definition anyway. That breaks *Done when* "a repository with a marked `seal/` reads it exactly as before". | rejected |
| A configured root name or a pointer file at the repository's top (the owner, 2026-11-09, G15) | A row or file that says where the root is says twice what the folder and its marker say. A gate trusting it looks where no folder is, as `docs/layout/one-root-by-lifetime.md` *Shared or local* states of the `Mode` row. | rejected by the owner |
| A placeholder token such as `{root}` in the text (the owner, 2026-11-09) | Every reader substitutes a symbol, and a record's `location:` and `evidence:` coordinates must still be real paths a check opens. | rejected by the owner |
| A second fixed name, `agentic-seal/`, found by its marker after `seal/`. Every reader takes the root from `lib/optin.py`, and the text keeps `seal/` with one definition in the core | A reader added later that derives the name without the resolver reads nothing there (*Technical context*). | chosen (the owner's design) |
| First setup takes the shared place from the core's sentence | At first setup no root stands, so `hooks/core-start.py` prints no core (G8). The orchestrator would have to open the core and judge which name applies, which is a judgment a script answers exactly. | rejected; `seal mode`'s printed place is used (G7) |
| Classifying readers match both fixed names at once, with no resolution | A change to code under a project's own `seal/` reads as confined to the document roots, which is today's defect at `lib/gate.py#DOC_ROOTS` (G12). A project's files under `seal/threads/` would read as declarations. | rejected |
| `chain_check.py` reads the root as leaving where HEAD has no marked root | A pull request that deletes only `README.md` reads as declaring nothing, where today a `seal` entry of any kind keeps the declarations judged (G11). | rejected; the test asks for HEAD's entry at the merge base's name (`frame/design.md` *Data & interfaces*) |
| The zip's member prefix follows the tree's name | A zip from one clone and an import into another clone of the same repository agree either way. Changing the prefix makes zips exported before this work, and zips moving between repositories, fail `seal import`'s member check. The prefix names nothing in the tree (G9). | rejected |
| The local root follows the shared name | Nothing of a project's own lives under its git directory, so no clash exists to avoid. `seal mode local` would land at a second local path, which every reader of the common directory would then have to try. | rejected |
| No text case for the readers, with the proofer reading each new reader | Each behaviour case pins one reader. A reader added by a later item, or by #1454's integration, has no case on the fixture and reads nothing, and no check fails. This issue is that record. | rejected; *Scope* item 4's case is kept against it |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* item 1; item 3 for `skills/implement/scripts/seal.py`; item 6's cases for S1, S2, S6 and `seal pr-checks install` | `bin/test tests/lib/test_optin.py tests/skills/test_seal.py tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py`; S1's and S2's cases seen red at the phase's parent | d17f73bd |
| 2 | *Scope* item 2 for `lib/gate.py` and `lib/routing.py`; item 3 for `chain_check.py` and `seal_stamp.py`; item 6's cases for S3, S4 and `seal pr-body --check` | `bin/test tests/lib/test_gate.py tests/lib/test_routing.py tests/skills/test_chain_check.py tests/skills/test_seal_stamp.py tests/skills/test_pr_body.py tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py`; S3's three cases seen red at the phase's parent | |
| 3 | *Scope* item 2 for `lib/config.py`; item 3 for the remaining modules and the `broad_gate.py` message; item 4; item 6's cases for the rest of S5 | `bin/test tests/lib/test_config.py tests/skills/ tests/github/test_rules.py tests/github/test_publish_release_note.py tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py` and the new text case; S9 seen red with one literal planted | |
| 4 | *Scope* items 5 and 7 | `bin/test tests/text/ tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_no_document_names_the_old_roots.py tests/behaviour/test_a_cited_section_stands_in_its_file.py`; `seal rules --check`; S8 seen red with the core's sentence deleted; `git grep -n "agentic-seal" -- skills agents templates docs README.md README.ko.md CONTRIBUTING.md CLAUDE.md` lists `skills/core/SKILL.md` alone | |

## Overlap with the release

The spawn names #1454 and #1445, and neither frame was committed when this one was read. #1454's `frame/design.md` stood as a skeleton in its worktree, so its rows below are read from its issue (executed: `gh issue view 1454`). #1445's branch differs from `dfd0c995` by its `routing.md` alone (executed: `git diff --stat dfd0c995 fix/1445-agents-write-commands-the-parser-reads`).

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1454, settings read as JSON | `lib/config.py` (this item removes `HOME` and changes `inside_the_root`; #1454 replaces the table reader). `skills/implement/scripts/seal.py` (`CONFIG_PATHSPEC` at `:1436` and the `Mode` writer). The `policy_root(os.path.join(root, "seal"))` lines at `.github/scripts/rules.py:229`, `:379` and `.github/scripts/release_report.py:213`. `broad_gate.py#config_text`. `pact_check.py`'s `seal/{CONFIG_FILE}` display paths. `skills/implement/bootstrap.md` step 1, where the orchestrator writes rows into the config `seal mode` creates. `docs/layout/one-root-by-lifetime.md`, in another section. This item's text case of *Scope* item 4 reads every module #1454 adds or changes. | #1454 | This item adds a case that reads the whole shipped tree's string constants, so it merges after the item whose new config readers that case reads. Taking #1454's merge into this branch then routes any config path #1454 spells through the resolver, inside rounds this item spends anyway. In the other order, #1454's new readers would meet a case written before they existed. |
| #1445, agents write commands in plain POSIX syntax | `skills/agent-contract/SKILL.md`: #1445 changes the rules on commands, and this item adds one clause to rule 11. This item's text case of *Scope* item 5 reads every file under `skills/` and `agents/`, #1445's text among them. | #1445 | It carries the version move to 0.37.0, which goes in before every other item of the release. Its contract text does not spell the root's second name, so the merge into this branch is a textual merge of separate rules. |

The merge order these rows state is #1445, then #1454, then this item.

## Operational impact

No migration. A repository with a marked `seal/` resolves it first, as before. A repository that first setup put in local mode because its own `seal/` stood there can now run `seal mode shared`, which moves its root to `agentic-seal/` and stages it. The release note's entry from `changelog.md` says so. No new environment variable or dependency. This pull request does not move the version: #1445 carries the move to 0.37.0.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
