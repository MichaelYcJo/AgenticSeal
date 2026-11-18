# Design: 1794986401-the-process-has-no-name

## Grounding

The tree as read at `c637848af`.

| Policy clause | What it fixes for this work |
|---|---|
| **G1** Issue #1557 (executed by the orchestrator on 2026-11-18: `gh issue view 1557 --json body,comments`, no comment) | The request: one name for the whole process that another repository can cite, placed where the issue's *Change* lists, and "workflow" left only where it names a GitHub Actions workflow. The owner's decisions are in its *Decision*: the name is the AgenticSeal process, "AgenticSeal 프로세스" in Korean; "review chain", "the run" and `agentic` keep their meanings; the scope is the places that name the whole process. |
| **G2** The places that call the process "workflow" (executed: `git grep -n -i workflow -- README.md skills/core/SKILL.md lib/optin.py .claude-plugin templates/setup/hygiene.yml`, and `git grep -n 워크플로 -- '*.ko.md'`) | The process: `README.md:8, 56, 114, 374, 383, 388, 458, 468`; `README.ko.md:9, 61, 118, 371, 380, 385, 455, 464`; `.claude-plugin/plugin.json:5`, `.claude-plugin/marketplace.json:3, 11`; `skills/core/SKILL.md:18, 19, 30, 32, 37, 43, 45`; `lib/optin.py:1, 25, 315, 326, 331`; `templates/setup/hygiene.yml:1`; `templates/setup/seal-README.md:18, 78` and `seal/README.md:18, 78` (the two files are equal, executed: `diff`); `docs/layout/one-root-by-lifetime.md:84` and `docs/layout/one-root-by-lifetime.ko.md:79`. A GitHub Actions workflow: `README.md:224` and `README.ko.md:226` (the file `seal pr-checks install` writes), the "workflow run" inside the row at `README.md:383` and `README.ko.md:380`, and `skills/core/SKILL.md:111`. |
| **G3** The citations of the core's heading *The first value: efficient development through the workflow* (executed: `git grep -n 'efficient development through the' -- . ':!seal/threads'`) | `CLAUDE.md:20-21`, `CONTRIBUTING.md:392-393`, `docs/releasing/branch-and-release.md:122`, `skills/settle/SKILL.md:448-449`, `tests/behaviour/test_chain_hooks_hardening.py:774-775` and `tests/text/test_every_agent_reads_the_contract.py:139`. The first search matched one line and missed the three that break the heading across a line; a search across line breaks finds all six (executed: `re.finditer(r"through\s+the\s+workflow")` over every tracked file outside `seal/threads/`). `tests/behaviour/test_a_cited_section_stands_in_its_file.py` reads every tracked file outside the records, so a citation left on the old heading fails there. |
| **G4** `tests/behaviour/test_chain_hooks_hardening.py:176-181` (read) | The description in `.claude-plugin/plugin.json` must equal both descriptions in `.claude-plugin/marketplace.json`, so the three change together. |
| **G5** `skills/writing-style/SKILL.md` *용어는 실물을 확인하고 고른다* and *저장소가 정의한 용어는 정의한 뜻으로만 쓰고, 같은 것을 다른 말로 바꿔 부르지 않는다* (read) | A product's own word stays in English and is explained at first use. One thing is called by one name, so every place in scope uses the full name, and none shortens it to "the process", which would be a second name. |
| **G6** `README.ko.md:166-173` (read) | "도장" there names only the stamp the `Stop` hook draws for a sealed work item. The phrase "도장 체인" stands nowhere in the tree (executed: `git grep -n '도장 체인\|도장체인'`, exit 1). |
| **G7** `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file*, the paragraph opening *A change to the way of working writes its process row in its own fragment* (read) | The diff changes `skills/core/SKILL.md` and `CLAUDE.md`, so `changelog.md` ends with `### Process changes`, one row per change. The session builds, so the orchestrator writes it. |
| **G8** `.claude-plugin/plugin.json:4` reads `0.38.2`; `gh issue list --milestone 'release: 0.38.3'` lists #1557 alone; `docs/releasing/branch-and-release.md` *The version moves at the start of a release, in the first pull request into `release/vX.Y.Z`.* (executed; read) | This work item is the release's first and only one, so it moves the version to 0.38.3 in the commit that adds its `changelog.md`. |
| **G9** `docs/layout/the-record-layout.md` is not touched; `docs/layout/one-root-by-lifetime.md` is in the policy root (read: `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*) | The subject of this work item is the text of the documents in scope, the policy root's one row among them, so that row is edited in place in this pull request and `## Rule changes` holds the no-change block. |
| **G10** The preload every spawn reads (executed: `wc -c skills/core/SKILL.md`, 9,322 bytes) | The core grows by the definition clause and the longer name at each place. `.github/scripts/release_report.py` prints the preload against the last tag on the release pull request. |

## Scope

In:

1. `README.md` and `README.ko.md`: the tagline names the process; one paragraph after the opening paragraph defines the name; each place G2 lists as the process uses the name; the "workflow run" inside the network table's row becomes a GitHub Actions workflow run.
2. `.claude-plugin/plugin.json` and both descriptions in `.claude-plugin/marketplace.json` carry the README's new tagline.
3. `skills/core/SKILL.md`: the opening sentence names and defines the process; lines 19, 30, 32, 37, 43 and 45 use the name; line 111 says a GitHub Actions workflow. The new heading is cited at each of the six places G3 lists.
4. `lib/optin.py`'s docstrings and comments, `templates/setup/seal-README.md` with `seal/README.md`, the header comment of `templates/setup/hygiene.yml`, and the row of `docs/layout/one-root-by-lifetime.md` and its Korean edition use the name.
5. The work item's `changelog.md` with its `### Process changes` table, and `.claude-plugin/plugin.json` moved to `0.38.3`, in one commit.

Out, each with its reason:

- **"the workflow" in `docs/`, `skills/` and `agents/` outside the files above.** The owner chose the places that name the whole process (G1). Elsewhere the context says which is meant, and a sweep would grow the diff and every agent's preload.
- **"review chain" and "the run".** Each keeps its narrower meaning (G1).
- **The routing answer `agentic`.** It names an answer a person picks, not the process.
- **A case asserting the new name.** It would pin wording. The cited-section case already holds the renamed heading (G3).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given a reader in another repository, when they open `README.md` or `README.ko.md`, then before *Install* they find the name, what it covers, and that it is not translated | The proofer reads the two paragraphs against *Data & interfaces* D1 and D2 |
| S2 | Given the files of *Scope* items 1 to 4, when "workflow" or "워크플로" is searched in them, then every remaining line names a GitHub Actions workflow | `git grep -n -i workflow -- README.md skills/core/SKILL.md lib/optin.py .claude-plugin templates/setup/hygiene.yml templates/setup/seal-README.md seal/README.md CLAUDE.md docs/layout/one-root-by-lifetime.md` and `git grep -n 워크플로 -- README.ko.md docs/layout/one-root-by-lifetime.ko.md` print, after the build, only lines that name a GitHub Actions workflow. Run at `c637848af` (executed), the two searches printed 58 lines. The build changes the process lines G2 lists. Kept, each naming a GitHub Actions workflow or its path: `README.md:11, 181, 219, 224, 383, 384`, `README.ko.md:226, 380`, `skills/core/SKILL.md:111`, `seal/README.md:33`, `templates/setup/seal-README.md:33`, `templates/setup/hygiene.yml:7, 23, 43, 46`, `docs/layout/one-root-by-lifetime.md:104, 128, 143, 144, 148, 149` and `docs/layout/one-root-by-lifetime.ko.md:121, 135, 140, 143, 144, 146`, where `README.md:383`, `README.ko.md:380` and `skills/core/SKILL.md:111` keep the word in the text the build rewrites as a GitHub Actions workflow. The pathspecs name files outside `seal/threads/`, so this work item's records, which quote the old lines, are not searched. The proofer reads each kept line |
| S3 | Given the build's commit, when the cited-section, line-wrap, manifest-description and contract cases run, then all are green | `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_chain_hooks_hardening.py tests/text/test_every_agent_reads_the_contract.py tests/lib/test_optin.py -q` green |
| S4 | Given the commit that adds `changelog.md`, when `.claude-plugin/plugin.json` is read, then it names `0.38.3`, and the fragment ends with a `### Process changes` table | `tests/behaviour/test_release_hygiene.py` green; `git grep -n -F '0.38.2' -- . ':!seal/threads'` prints nothing; at `c637848af` it prints `.claude-plugin/plugin.json:4` alone (executed) |

## Data & interfaces

- **D1, the definition in English.** One paragraph after the opening paragraph of `README.md`: everything the opening paragraph describes, from the routing question to the sealer's guarantee, is the AgenticSeal process, and the diagram draws it. Another repository points at it by that name, which is a product name and is not translated. *Seal* keeps one meaning, the last agent's guarantee, and the stamp later in the README is a drawing of it. *The review chain* names only the review rounds inside the process.
- **D2, the definition in Korean.** The same paragraph in `README.ko.md`, with the Korean form "AgenticSeal 프로세스", and a sentence saying it is not rendered as "도장 체인" or "인장 과정" (G6).
- **D3, the tagline.** "The AgenticSeal process: agents frame, build, inspect and seal a change, and it ends in a seal bound to a commit." The three manifest descriptions carry it verbatim (G4). The Korean tagline says the same.
- **D4, the core's opening.** "This file governs work run through the AgenticSeal process, everything the plugin does with one issue from the routing question to the sealer's guarantee; a session doing other work is not bound by it to start the process." The second "process" stays, because the sentence has just defined it; every later place uses the full name (G5).
- **D5, the heading.** *The first value: efficient development through the AgenticSeal process*. Line 32's "through an agent workflow" becomes "through a process of agents", because the paragraph's subject is AgenticSeal and repeating the name there says nothing.

## Rule changes

- nothing
  why: the work names the process and changes no rule. The one policy root row it touches, in `docs/layout/one-root-by-lifetime.md` and its Korean edition, is edited in place because the subject of this work item is that text (G9).

## Removes

- nothing
  why: the work replaces a word at each place G2 lists and adds one definition paragraph per README and one clause to the core. No copy, reader or check stands on "the workflow" (executed: `git grep -n -i 'the workflow' -- tests`, two lines, `tests/github/test_release_completeness_check.py:436`, a docstring about a GitHub Actions workflow, and the heading at `tests/text/test_every_agent_reads_the_contract.py:139`, which *Scope* item 3 updates).

Framed 2026-11-18 by the session, before the build.
