# Design: 1794200905-a-foreign-seal-dir-keeps-the-records-shared

## Grounding

The tree as read at `872ff59c`.

| Policy clause | What it fixes for this work |
|---|---|
| G1 `docs/layout/one-root-by-lifetime.md` *The opt-in signal is the root itself* (read), the rule #1051 brought in 0.23.0 (executed: `gh issue view 1051`) | A `seal/` is the root only where its `README.md` opens with `lib/optin.py#MARKER`. A `seal/` without the marker is the project's own, and first setup that meets one "writes nothing into it and keeps the root under the git directory". This work keeps the first two and changes the last clause, in *Rule changes*. No config key and no pointer file is added: the folder and its marker still say where the root is. |
| G2 the same document, *What first setup asks* and *Shared or local* (read) | First setup asks one question with three options. `seal mode` moves the root between the shared place and the local place, and `seal pr-checks install` refuses where the shared root is not in the tree. `lib/optin.py#home_at` is the only reader of where the root is. Each of these holds unchanged once `home_paths` names the shared place (*Scope* item 1). |
| G3 `skills/core/SKILL.md`, opening paragraph (read) | The core already makes one exception to "paths are the plugin's": `seal/`, "the records root `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* places". The sentence that defines the root's second name goes there, so every agent (through `skills:`) and every session in an opted-in repository (through `hooks/core-start.py`, which asks `optin.opted_in`, read at `lib/core.py:130`) reads it. |
| G4 contract rule 11 in `skills/agent-contract/SKILL.md` and `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | Both say every `seal/…` path means `<repo>/seal/` where it carries the marker, and the common git directory's `seal/` otherwise. Read with `seal/` as the name the core gives the root, both stay true. Each gains one clause pointing at the core's definition and does not spell the second name. |
| G5 `lib/optin.py` (read) | `home_paths(root, common)` returns `(<root>/seal, <common>/seal)`, and `home_at` returns the first of them that is a directory carrying the marker. The comment above `WORK_ITEMS` says the readers that classify repository-relative paths spell `seal/` as a string "because a path in a diff or a tree listing is only ever the shared root". That premise is false once the shared root can have a second name, and this work removes it (*Removes*). |
| G6 Which code spells the root's name (executed: a probe that walks every tracked `.py` outside `tests/`, `evals/` and `seal/` with `ast` and prints each string constant that is not a docstring and equals `seal` or holds `seal/` as a path segment; executed: `git grep -nE "optin\.HOME\|routing\.WORK_ITEMS\|DOC_ROOTS\|home_paths"`) | The modules whose code reads the root by its name are listed in *Scope* items 2 and 3. Every other hit is a message that uses `seal/` as the root's name (for example `skills/settle/scripts/settle.py:764`), the fenced-block info string `lib/fields.py#INFO`, or the command's own name `seal` (`skills/implement/scripts/seal.py:2753`). The issue's grep, which gave its figure of about 43 files, also matches docstrings, comments and messages that name the root in text. |
| G7 `skills/implement/bootstrap.md` *Orchestrator: Bootstrap* (read) and `skills/implement/scripts/seal.py:750-760` (read) | The orchestrator creates the root by hand, copying `templates/setup/seal-README.md` into the place the answer picks. With no root at either place, `seal mode` prints the shared and the local place, both taken from `optin.home_paths`. So once `home_paths` names the shared place, that printed line is where first setup puts a shared root, and the orchestrator needs no name of its own. |
| G8 `hooks/core-start.py` docstring (read) | "A session in a repository with no root receives nothing." At first setup no root stands yet, so the session's context does not hold the core's definition. Bootstrap therefore takes the shared place from `seal mode`'s output (G7), not from the core's sentence. |
| G9 `skills/implement/scripts/seal.py:594` and `:855` (read) | `seal export` names every zip member `seal/<path>`, and `seal import` refuses a member whose first part is not `optin.HOME`. That prefix is a name inside the archive format, not a path in the tree: import writes under the root `home_paths` resolves. It stays `seal/` whatever the tree calls the root. |
| G10 `templates/setup/seal-README.md:55-60` and `seal/README.md:55-60` (read) | Both say first setup that meets a `seal/` without the marker "keeps the root under the git directory". That becomes false and is rewritten (*Scope* item 5). The marker line, `# What AgenticSeal maintains in seal/`, stays one line for both names: in the text, `seal/` is the root's name. |
| G11 `skills/code-review/scripts/chain_check.py:2045-2056` (read) and `docs/checks/the-pull-request-check.md` *What the check reads at the pull request* (read) | Where the tree has no top-level `seal` entry, the check reads nothing as declared, and "a `seal` that is not a directory keeps the declarations judged". In a repository whose own `seal/` always stands, the literal test would never see the root leave. *Data & interfaces* gives the name the test reads. With `seal` read as the root's name, the policy sentence holds unchanged. |
| G12 `lib/gate.py#DOC_ROOTS` (read) | `("docs/", "seal/")`. In a repository whose own `seal/` holds code, a change to that code reads as confined to the document roots, so the parity arm owes no comparison. Resolving the name fixes that too. |
| G13 `docs/running/what-a-script-gates.md` *The checks* (read) | The table lists every check. Those that read the records are `seal stamp`, `chain_check.py`, `seal gate`, `seal rules --check`, `seal unverified`, `seal settle`, `seal pact`, `seal pr-body --check` and `seal fold`. `seal layout --check`, `seal deferrals`, `seal mutate` and the linters read no record. The acceptance takes its "every check" from the first list. |
| G14 `tests/behaviour/test_no_document_names_the_old_roots.py` (read) | Its `SCANNED` tuple is the set of shipped document paths, and `KEEP` is an allowlist where each entry must still occur. The check that no document but the core states the second name reads the same `SCANNED`, imported, so the scanned set has one source. |
| G15 The ticket and its two comments (executed: `gh issue view 1059 --json body,comments`) | The body is the owner's design of 2026-11-09. The comment of 2026-11-06 replaces "every hook" with `lib/optin.py#home_at` and `lib/gate.py#DOC_ROOTS`, since 0.33.0 removed the hooks. The comment of 2026-11-08 records the rewrite and the rejected placeholder token. Neither changes the request beyond the body. |
| G16 `seal/follow-up.md` (read); v0.36.0's `### Process changes` (executed: `gh release view --json body`) | No follow-up row waits on this work. v0.36.0 changed `skills/implement/bootstrap.md` step 1 to four questions. This work changes where step 1's shared answer lands, so its fragment carries a `### Process changes` row. |
| G17 `CLAUDE.md` *The core* (read) | "An agent spawned here receives the installed plugin's copy." The installed copy is 0.36.0, so an agent spawned from this session does not read the tree's new core sentence. The measurement in *Done when* needs the tree's plugin loaded (`frame/questions.md` Q1). |

## Scope

In:

1. **The resolver knows the second name.** `lib/optin.py` gains the second fixed name `agentic-seal`, beside `HOME`. `home_paths(root, common)` returns as its shared entry `<root>/seal` where that directory carries the marker, else `<root>/agentic-seal` where that one does, else `<root>/seal` where nothing stands at that path, else `<root>/agentic-seal`. The local entry stays `<common>/seal`: nothing of a project's own lives under its git directory. `home_at` keeps its loop over `home_paths`, so the order it reads is a marked `seal/`, then a marked `agentic-seal/`, then local mode. A new function gives the shared root's repository-relative name for readers that classify paths as git prints them (*Data & interfaces*). The module docstring and the docstrings of `home_paths` and `home_at` state the new order.
2. **The `lib/` readers take the name from the resolver.** `lib/config.py#HOME` and `#inside_the_root`, `lib/gate.py#DOC_ROOTS` and `#touches_code`, and `lib/routing.py#WORK_ITEMS` stop spelling `seal`. Each takes the root's name from its caller, which reads it from `lib/optin.py`.
3. **Every script that spells the root's name reads it from the resolver.** These ten modules, the list G6's probe gave: `skills/code-review/scripts/chain_check.py`, `skills/implement/scripts/seal.py`, `skills/settle/scripts/settle.py`, `skills/settle/scripts/rule_changes.py`, `skills/verify/scripts/pact_check.py`, `skills/verify/scripts/seal_stamp.py`, `skills/verify/scripts/unverified_check.py`, `.github/scripts/rules.py`, `.github/scripts/release_report.py` and `.github/scripts/publish_release_note.py`. A path a person reads in a message is the real path. `skills/verify/scripts/broad_gate.py:2984` lists the places the root is looked for, and prints the paths `home_paths` gives, as `seal.py:755` already does. A message that calls the root "the `seal/` root" keeps that wording, since `seal/` is the root's name in text.
4. **No module outside `lib/optin.py` spells the root's name.** A text case walks every tracked `.py` outside `tests/` and `evals/` with `ast`, as G6's probe did. It refuses a string constant that is not a docstring and that equals either name or opens with either name followed by `/`. Its allowlist holds the constants that are not the root (G6), each entry with its reason and checked to still occur, in the shape `KEEP` has in G14's module.
5. **The text keeps `seal/` as the root's name, defined once.** `skills/core/SKILL.md`'s opening paragraph states that `seal/` names the repository's records root, which is `agentic-seal/` where the repository's own `seal/` belongs to something else and an `agentic-seal/` carries the marker. Contract rule 11 and `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* each point at that sentence and do not spell the second name. `skills/implement/bootstrap.md` takes the shared place from `seal mode`'s output, and its paragraph on a `<repo>/seal/` without the marker changes. A directory without the marker at the shared place `seal mode` prints is the project's own: the orchestrator writes nothing into it and offers only local. All three options are offered otherwise. `templates/setup/seal-README.md` and `seal/README.md` say the same, and `lib/optin.py`'s docstrings say it in code. A text case pins that the core states `` `agentic-seal/` `` once, that the name is `lib/optin.py`'s constant, and that no other file of G14's `SCANNED` states it.
6. **A case per check reads the records under `agentic-seal/`.** One behaviour module builds a repository whose `seal/` is a Python package with no marker and whose `agentic-seal/` carries the marker and a work item. One case for each check of G13's first list, and for `seal mode`, `seal mode --check`, `seal pr-checks install`, `seal export` and `seal import`, shows the command reading the records there.
7. **`changelog.md`**, in the shape `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file* states, under *Added*. It ends with a `### Process changes` table in `templates/records/process.md`'s shape, with one row: first setup's shared answer lands where `seal mode` prints (G16).

Out:

- **The places sentence is stated in four documents**: contract rule 11, `skills/implement/SKILL.md`, `docs/layout/one-root-by-lifetime.md` and `docs/layout/the-record-layout.md` *seal/*. It was stated in all four before this work, and each stays true with `seal/` as the core's name. Folding them into one is a separate change.
- **The local root's name.** It stays `seal` under the common git directory, where no project keeps a directory of its own (*Scope* item 1).
- **A root renamed between commits.** A reader that reads at a commit other than the working tree reads under the name the working tree resolves, except `chain_check.py`'s test of a root leaving (*Data & interfaces*). A repository that moved its root from one name to the other reads its earlier history under the current name. This is a limit, stated in `home_paths`'s docstring.
- **Both names taken by the project.** Where `<repo>/seal/` and `<repo>/agentic-seal/` both stand without the marker, the root goes under the git directory, as a foreign `seal/` did before this work (*Scope* item 5). This is a limit, not a guard.
- **`tests/` and `evals/`.** Their fixtures and scaffolds build repositories whose root is `seal/`, and this repository's own root is `seal/`. Existing cases change only where a signature in *Scope* item 2 changes.
- **`.gitattributes`'s `/seal/ export-ignore`**: this repository's own archive rule, for a root that is `seal/`.
- **A placeholder token in the text, and a configured name or pointer file.** The owner weighed both and rejected them (G15). `frame/plan.md` *Alternatives considered* holds the grounds.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 first setup beside a foreign `seal/` | Given a repository whose `seal/` has no marker and no root anywhere, when `seal mode` runs, then it prints `<repo>/agentic-seal` as the shared place and the common git directory's `seal` as the local place. When a `README.md` copied from `templates/setup/seal-README.md` is put there and `seal mode` runs again, it writes `Mode` as shared into `agentic-seal/config.md`, `seal mode --check` passes, and nothing under `seal/` changed. | a case in the behaviour module of *Scope* item 6 |
| S2 the resolver's order | `home_at` returns a marked `seal/` over a marked `agentic-seal/`, a marked `agentic-seal/` over a local root, and the local root where both tree directories stand without the marker. `home_paths`'s shared entry follows *Scope* item 1 in each of these states, and in the state where `seal/` is absent. | cases in `tests/lib/test_optin.py` |
| S3 the pull request's check | Given S1's repository with a routing declaration under `agentic-seal/threads/<id>/`, `chain_check.py` reads it as declared, and reads a change to `seal/__init__.py` as reaching outside the document roots. A pull request that deletes `agentic-seal/` reads nothing as declared. A pull request that deletes only `agentic-seal/README.md` keeps its declarations judged. | cases in the behaviour module |
| S4 the stamp | `seal stamp --guarantee` given `agentic-seal/threads/<id>/guarantee.md` queues it, as it does for `seal/threads/<id>/guarantee.md`. | a case in the behaviour module |
| S5 every other check of G13's first list | `seal gate`, `seal rules --check`, `seal unverified`, `seal settle`'s dry run, `seal pact`, `seal pr-body --check` and `seal fold` each read the record or the config they read under `agentic-seal/`, one case each. | cases in the behaviour module |
| S6 moving and carrying the root | `seal mode local` moves `agentic-seal/` to the common git directory's `seal/` and stages the removal of `agentic-seal/`. `seal mode shared` moves it back to `agentic-seal/` and stages that. `seal export` from S1's repository writes members named `seal/…`, and `seal import` of that zip into a fresh clone of S1's repository writes under `agentic-seal/`. | cases in the behaviour module |
| S7 a marked `seal/` reads as before | Every existing case of `tests/lib/`, `tests/skills/` and `tests/behaviour/` passes with no edit except a changed signature, and except `tests/skills/test_seal.py::Test_refusals::test_refuses_a_projects_own_seal_as_a_destination_not_as_two_roots`, which stated the old rule and now builds the state where both `seal/` and `agentic-seal/` are the project's own (`b41ce59e`). | the broad gate, the orchestrator's run |
| S8 the name is stated once | `skills/core/SKILL.md` holds `` `agentic-seal/` `` once and it equals `lib/optin.py`'s constant. No other file of `SCANNED` holds `agentic-seal`. Deleting the core's sentence turns the case red. | a text case (*Scope* item 5) |
| S9 no reader spells the name | A string constant `"seal"` added to any shipped module outside `lib/optin.py`, not on the allowlist, turns the case red. | the text case of *Scope* item 4 |
| S10 an agent writes there | An agent run in S1's repository writes its records under `agentic-seal/`. A measurement, read once. | `frame/questions.md` Q1 |

## Data & interfaces

**`lib/optin.py`.** The second name is a module constant beside `HOME`. `home_paths(root, common=None)` keeps its signature and its `(shared, local)` return, and its shared entry follows *Scope* item 1. A new function, called with `(root, common=None)`, returns the `/`-joined repository-relative name of the root in force where that root is the shared one (`seal` or `agentic-seal`), and `""` where the root is local or absent. The name follows the module's naming, and the crafter picks it. A second function returns the same name for a tree read through a callable, `read(relpath) -> text or None`: the first of the two names whose `README.md` opens with `MARKER`, or `""`. `home_at` and the first function use it on the disk, and `chain_check.py` uses it at a commit through `read_record`. The order and the marker comparison then have one home.

**`lib/gate.py#touches_code(paths, home)`** treats `docs/` and `<home>/` as the document roots, and only `docs/` where `home` is `""`. `chain_check.py#originals_of` passes the name in force at HEAD.

**`lib/routing.py`.** `WORK_ITEMS` goes. A caller that classifies paths as git prints them composes `<name>/threads` from the name and `optin.WORK_ITEMS`.

**`lib/config.py`.** `HOME` goes. `inside_the_root(rel, home)` takes the name from its caller.

**`chain_check.py`, the root leaving.** Declarations at HEAD are listed under the name HEAD's tree resolves. A deleted declaration is matched under the name the merge base's tree resolved. The test that reads nothing as declared asks whether HEAD has a top-level entry at the merge base's name. That keeps "an entry is anything at that name", so a pull request that deletes only the marker keeps its declarations judged (S3). It also keeps a project's own `seal/` from counting as the root that stayed.

**`seal export` and `seal import`.** The zip's member prefix stays `optin.HOME` (G9).

## Rule changes

- change
  file: docs/layout/one-root-by-lifetime.md
  section: The opt-in signal is the root itself
  from: as a package named `seal` has one, and reads as not opted in; first setup
    that meets one writes nothing into it and keeps the root under the git
    directory.
  to: as a package named `seal` has one, and reads as not opted in. First
    setup that meets one writes nothing into it, and the shared root takes
    the second name `skills/core/SKILL.md` gives it, recognised by the same
    marker; `seal mode` prints that place before the root exists. Where a
    directory of the project's own stands at the second name too, the root
    goes under the git directory.
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: 옵트인 신호는 루트 자체다
  from: 그런 디렉터리를 만난 처음 설정은 그 안에
    아무것도 쓰지 않고 루트를 git 디렉터리 아래에 둡니다.
  to: 그런 디렉터리를 만난 처음 설정은 그 안에 아무것도 쓰지 않고, shared
    루트는 `skills/core/SKILL.md` 가 정한 두 번째 이름을 같은 표식으로
    씁니다. 루트가 아직 없을 때 `seal mode` 가 그 자리를 출력합니다. 두 번째
    이름의 자리에도 프로젝트 자신의 디렉터리가 있으면 루트는 git 디렉터리
    아래에 둡니다.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the comment saying the readers that classify repository-relative paths spell `seal/` as a string | `lib/optin.py`, the comment above `WORK_ITEMS` | its premise, that a path in a diff is only ever under `seal/`, is false (G5); the readers take the name from the resolver (*Scope* items 2 and 3) |
| `HOME`, the copy of `optin.HOME`, its comment, and the pin holding it equal to `optin.HOME` | `lib/config.py#HOME`; the equality case in `tests/lib/test_config.py` | `inside_the_root` takes the name from its caller, so there is no copy to keep in step |
| `DOC_ROOTS` and the comment explaining why it spells `seal/` | `lib/gate.py#DOC_ROOTS` | `touches_code` takes the name (*Data & interfaces*) |
| `WORK_ITEMS` and its comment | `lib/routing.py#WORK_ITEMS` | callers compose the prefix from the resolved name |
| the clause *offers neither shared option, because `<repo>/seal/` is the shared root's one place* and the one-line notice of local mode | `skills/implement/bootstrap.md` *Orchestrator: Bootstrap* | the shared place is the one `seal mode` prints, and the notice applies only where that place is taken too (*Scope* item 5) |
| the sentence *First setup that meets such a directory writes nothing into it and keeps the root under the git directory.* | `templates/setup/seal-README.md`; `seal/README.md` | rewritten to the rule *Rule changes* states |
| `CONFIG_PATHSPEC`, the config's path spelled under `seal/` | `skills/implement/scripts/seal.py#CONFIG_PATHSPEC` | `refusals` and `switch` stage the config under the shared root's name (`b41ce59e`) |
| the literal places in the no-root message | `skills/verify/scripts/broad_gate.py:2984` | the message prints `home_paths`'s paths (*Scope* item 3) |

This work adds two text cases: *Scope* item 4's reader check and *Scope* item 5's name check. The four removals in `lib/` above go in return: three copies of the root's name and one pin that existed only to keep one copy in step. The record of what the reader check would catch is this issue: every reader that spelled `seal` read nothing in a repository whose root has another name, and no case failed, because each case built a `seal/`. The name check is the owner's *Done when*.

Framed 2026-11-09 by framer, before the build.
