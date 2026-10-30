# Review round 1: 1793273065-the-core-reaches-no-users-repository

target: 007d9cb9 against origin/release/v0.25.0

## Findings

### 1. The core's added sentence says the one ask before the first edit is the routing question, which the two skills it cites say is one question of a larger batch

severity: should
location: `skills/core/SKILL.md:82-86`, `tests/text/test_review_axes.py:102-127`
evidence: read `skills/core/SKILL.md:77-86`, `skills/implement/orchestration.md:97-99`, `skills/implement/SKILL.md:171-175`
verdict: fixed 1562e058

The core is now the one text every session and every agent holds before
anything else. It also ranks above the skills. The sentence added to
*Asking a person is the most expensive judgment* reads: "That one ask is
the routing question". The sentence before it says whatever needs a person
is asked once, together, before the first edit. Read together, the batch
and the routing question are one and the same.

The two documents the paragraph cites say otherwise.
`skills/implement/orchestration.md:97` says "The routing question is one of
the questions `skills/implement/SKILL.md` *1.* has the orchestrator ask in
one batch". `skills/implement/SKILL.md:171-175` names what else that batch
holds: "a decision only they can make, an approval, a credential, a
permission the session does not have". A session that judges by the core
can read it as saying that only the routing question may be asked. It would
then let a credential or a permission wait until the first refusal, the
very mid-run stop the paragraph exists to prevent. Or it gets two readings
of one rule from two files. Either way the core breaks its own rule that
every sentence has one reading.

The wording comes from `frame/design.md` *Scope* item 1 ("the one question
is the routing question"). The crafter built what the frame asked for, so
the defect is in the frame's sentence, and the build carries it. The diff
of the old `CLAUDE.md:3-93` against the core's body (executed, *Probes*)
shows this sentence as the one change, so nothing else in the core needs
correcting. `tests/text/test_review_axes.py#test_the_core_names_where_the_routing_question_is`
reads the section's name and the hook's name, and neither changes below.
Where the fix pass also corrects *Scope* item 1 to match (contract rule
19), its answer says so.

```markdown
**Asking a person is the most expensive judgment.** Between two designs
that catch the same defect, the one that stops to ask a person costs more,
and the difference has to be argued rather than assumed. Whatever needs a
person is asked once, together, before the first edit, and nothing comes
back mid-run; `skills/implement/SKILL.md` *1. Read the documents that
outrank the code first* holds that rule with its reasoning. The routing
question is one of that batch, which the orchestrating session puts as
`skills/implement/orchestration.md` *Orchestrator: how the work is routed*
states, and `hooks/routing-edit-gate.py` refuses the first edit until it is
answered.
```

answer: The finding holds: `skills/implement/orchestration.md:97` makes the routing question one of the batch, and `skills/implement/SKILL.md:171-175` puts a decision, an approval, a credential and a permission in that batch too. The core's sentence is now the one the finding proposes, "The routing question is one of that batch", with the section and the hook named as before. The fix also landed outside `location:`, in `tests/text/test_review_axes.py#test_the_core_names_where_the_routing_question_is`: its docstring said "the one question is the routing question", the same reading, and it now holds an assertion that the paragraph says "The routing question is one of that batch". That assertion was seen red against the old core and green after the fix (`bin/test -q -p no:xdist tests/text/test_review_axes.py -k test_the_core_names_where_the_routing_question_is`, exit 1 then exit 0). `git grep` on "one ask is", "one question is the routing", "the one question" and "only question" finds no other text stating this reading, outside the frame. `frame/design.md` *Scope* item 1 still says "the one question is the routing question", and the frame is the orchestrator's to fold.

### 2. Four shipped texts say the block's line points outside a project when written into a project's CLAUDE.md, but the line is relative and points inside it

severity: should
location: `install.sh:22-24`, `README.md:302-305`, `README.ko.md:297-299`, `seal/threads/1793273065-the-core-reaches-no-users-repository/changelog.md:3`, `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py:272-274`
evidence: read `templates/setup/claude-md-block.md:2`, `install.sh:22-24`, `install.sh:98-99`, `README.md:302-305`, `README.ko.md:297-299`, `seal/threads/1793273065-the-core-reaches-no-users-repository/changelog.md:3`, `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py:272-274`
verdict: fixed 6016faf7

The release removes `bash install.sh --project`, and every place that says
why gives the same reason. The installer header says "from a project's
CLAUDE.md the import resolves outside the working directory". The fragment
says "from a project's `CLAUDE.md` the import points outside the project, so
it waits on an approval dialog". `README.md` says the import "would reach
outside the working directory", `README.ko.md` says the same in Korean, and
the case's docstring says "the import is external".

The line the release ships is `@plugins/marketplaces/agenticseal/skills/core/SKILL.md`
(`templates/setup/claude-md-block.md:2`), a path relative to the file that
holds it. Written into `<project>/CLAUDE.md`, it names
`<project>/plugins/marketplaces/agenticseal/skills/core/SKILL.md`. That
path is inside the working directory and does not exist. The installer
computes exactly this a few lines further down: `CORE="$(dirname
"$TARGET")/$IMPORT"` at `install.sh:99`. So a project-scope block is an
import of a missing file, which loads nothing and says nothing (probe e). It
is not an external import that waits on a dialog. The external case
(probe d) applies only to a line rewritten to reach the clone, which nothing
in this release writes.

The conclusion stands, and the scope should go. But the release note is
what a user reads to learn why their `--project` is gone, and it tells them
something false. A user who then runs `bash install.sh ./CLAUDE.md`, which
is still accepted, would look for a dialog that never comes. The
installer's own warning at that point names the in-project path, so the
header and the warning contradict each other in one file. The design's
plan row A9 carries the same reasoning, and the fix pass may correct it
alongside.

```bash
# install.sh:22-24
# There is no project scope. The block's line is relative to the file that
# holds it, so in a project's CLAUDE.md it names a plugins/ directory inside
# the project, which is not there; a line written to reach the clone from
# there would resolve outside the working directory, which an approval
# dialog gates and a headless session never loads.
```

```markdown
<!-- changelog.md:3, the sentence on --project -->
`bash install.sh --project` is gone: in a project's `CLAUDE.md` the block's line names a `plugins/` directory inside the project, which is not there, and a line written to reach the marketplace clone from there would point outside the project, where it waits on an approval dialog and a headless session never loads it.

<!-- README.md:302-305 -->
There is no project scope. In a project's `CLAUDE.md` the block's line
names a `plugins/` directory inside the project, which is not there, and a
line written to reach the clone from there would point outside the working
directory, which Claude Code asks about interactively and a headless
session never loads.

<!-- README.ko.md:297-299 -->
프로젝트 범위는 없습니다. 프로젝트의 `CLAUDE.md` 에 넣으면 블록의 줄은 프로젝트
안의 `plugins/` 디렉터리를 가리키는데, 그곳에는 그 파일이 없습니다. 거기서
클론까지 닿도록 줄을 바꾸면 작업 디렉터리 밖을 가리키게 되고, Claude Code 는
이것을 대화형으로 묻고 헤드리스 세션은 아예 로드하지 않습니다.
```

```python
def test_install_sh_has_no_project_scope(tmp_path):
    """In a project's `CLAUDE.md` the block's relative line names a
    `plugins/` directory inside the project, which is not there, and a line
    written to reach the clone from there is external: an approval dialog
    gates it and a headless session never loads it (#1177, probe d), so the
    scope is gone. An option, `--project` among them, is refused rather than
    taken for a file named after it."""
```

answer: The finding holds: `install.sh:99` computes `CORE="$(dirname "$TARGET")/$IMPORT"`, so the shipped relative line in `<project>/CLAUDE.md` names a missing `plugins/` directory inside the project, not an external file. All five texts now give the finding's reason in the finding's proposed words: the installer header, `README.md`, `README.ko.md`, the `--project` sentence of `changelog.md`'s `### Fixed` entry, and the docstring of `test_install_sh_has_no_project_scope`. Every change is inside `location:`. `bash -n install.sh` exits 0, ruff passes on the test module, and 95 modules that read `skills/core`, a README, `install.sh`, `gaps.md` or `skills/` pass together with this fix and finding 1's. No case pins the reason's wording, because no code renders it. `git grep` on "outside the working directory", "import is external", "resolves outside", "reach outside" and "points outside" finds the same old reading only in the frame: `frame/design.md:28` (probe d's row), `frame/design.md:244` (*Removes*, the `--project` row), `frame/plan.md:62` (A9) and `frame/questions.md:21`. They are left for the orchestrator to fold.

### 3. The closing memo hands the agents' double read of the core to #1183, whose body does not mention it, and it gives the payload's net growth as the cost of the second read

severity: should
location: `seal/threads/1793273065-the-core-reaches-no-users-repository/gaps.md:26`
evidence: executed `gh issue view 1183 --json body --jq .body | grep -n -i "subagent\|spawn\|twice\|skills:"`
verdict: fixed 85edcd81

`gaps.md` *Not done* ends: "#1183's review weighs it, because a
`SessionStart` hook may not reach a subagent at all (unverified)". The
search of #1183's body (executed) finds "twice" on two lines only, and both
are about a session. One is the hook's `source` values for a resumed
session. The other is the switch from the old block. No line names a
subagent, a spawn, `skills:` or an agent's double read. Its *Done when*
compares the two shapes on "reach, version, path, token cost per project
and visibility". The cost per spawn is not on that list. So the deferral
points at a home that does not hold it. The question of whether A5 removes
the second read would then go unasked, and the 2,100 tokens per spawn would
stand with no owner.

The memo's number is also off. "That is +6,796 B per spawn" gives the
growth of each agent's whole payload as the cost of the second read.
`trail/phases/phase-3.md` *After this change every agent's prefix holds the
core twice* breaks that number down. The second read is the core's 6,711 B.
The 6,796 B is that read, plus the first one through `skills:`, less the
6,663 B the pair lost, plus 37 B of opening sentence. "About 2,100 tokens"
holds for either number at 3.2 B/token, so only the bytes figure is wrong.

The repair to #1183 is made outside the tree and closes `deferred #1183`.
The memo's sentence is a commit.

```markdown
<!-- #1183, a bullet under "Not verified, and the probes that decide it" -->
- Whether a plugin's `SessionStart` hook output reaches a subagent. Under A1, where the block is installed, every agent reads the core twice: once through `skills:` and once through the import, which #292 measured reaching every spawn. That is the core's 6,711 B again, about 2,100 tokens per spawn (#1177 `trail/phases/phase-3.md`). A5 removes the second read only if the hook does not reach a spawn, and the comparison weighs that.

<!-- #1183, Done when: "token cost per project" becomes -->
token cost per project and per agent spawn

<!-- gaps.md:26, the second sentence -->
That is the core's 6,711 B a second time, about 2,100 tokens at 3.2 B/token, inside a per-agent growth of 6,796 B (`trail/phases/phase-3.md`).
```

answer: The number half holds and is fixed: the memo's second sentence is now the finding's proposed sentence, with the core's 6,711 B as the second read inside the 6,796 B growth. The home half does not hold as written. #1183's body does not mention the agents' double read, but the orchestrator's comment of 2026-10-29 on #1183 (https://github.com/MichaelYcJo/AgenticSeal/issues/1183#issuecomment-6498975932, read with `gh api`) names it. The comment covers both carriers, the cost per spawn, and the unverified question of whether a `SessionStart` hook reaches a subagent. `docs/issues-and-milestones.md` *An issue is its body and its comments together* makes that comment part of the issue, so the memo's deferral has a home and its sentence stands. The comment itself still says "+6,796 B per spawn", the same wrong figure; the comment and the body's *Done when* list are outside the tree, and their edit is the orchestrator's. `git grep "6,796"` finds no other text that gives 6,796 B as the cost of the second read: `trail/phases/phase-3.md` uses it only as the per-agent growth, and breaks it down. The fragment gives tokens only, and it says nothing about this.

## Confirmations

confirms: none
The grounds `gaps.md` *Not done* gives for keeping both paths hold against
the issue and the core. Read: the issue's *Done when*, second bullet, names
`skills:` as how an agent is handed the core and the preset block as how a
session in a user's repository loads it. With the user's `CLAUDE.md`
reaching every spawn, both paths together make the double read. The
constraint "No session reads the core twice" names sessions, and the block
is a session's only path. A user-scope `@` import has no form that loads
for one reader and not another, so the only ways to remove the second read
are to drop `skills:`, which breaks the issue's own clause and leaves an
agent with no core on a machine without the block, or to change the carrier,
which is #1183's question. That the pair reaches a spawn is #292's premise
and is not measured here. This round's own spawn context does hold the
contents of `~/.claude/CLAUDE.md` and of a `CLAUDE.md` for this repository
(read), which is consistent with it. That copy of `CLAUDE.md` is the 93-line
one from before phase 1, while the checkout at `007d9cb9` holds the 17-line
one, so what a spawn receives may be the parent session's file as of its
start. The core's first value prices tokens, and the cost is recorded with
a number. What does not hold is the home it is deferred to: finding 3.

confirms: none
The core moved whole. Executed: `diff` of the old `CLAUDE.md` from line 3
on, at `origin/release/v0.25.0`, against `skills/core/SKILL.md` from
`## The first value` on prints one hunk, the added routing sentence
(`skills/core/SKILL.md:82-86`), and nothing else. The headings are
unchanged, as *Data & interfaces* requires. `CLAUDE.md` holds `# AgenticSeal`
and `## The core` alone, no `@` line, and names `skills/core/SKILL.md`
(read `CLAUDE.md:1-17`).

confirms: none
Every definition lists `core` then `agent-contract` under `skills:` (read
`agents/crafter.md:7-9`, `agents/framer.md:9-11`, `agents/proofer.md:7-9`,
`agents/sealer.md:12-14`, `agents/tracer.md:8-10`). The template is the two
markers around the one `@` line, byte for byte as *Data & interfaces* gives
it (read `templates/setup/claude-md-block.md:1-3`).

confirms: none
The four divergences in `gaps.md` hold on the code. The opening sentence's
fixed break is pinned in `tests/text/test_every_agent_reads_the_contract.py#SENTENCE`.
The design's "`uninstall.sh` is unchanged" would have left the uninstaller
on `$HOME/.claude/CLAUDE.md` while the installer writes under
`CLAUDE_CONFIG_DIR` (read `uninstall.sh:15`, `install.sh:44`), and
`test_both_scripts_default_to_the_config_directorys_file` runs both scripts
with `HOME` moved. The option refusal is the `case` at `install.sh:41-43`,
read by message in `test_install_sh_has_no_project_scope`. The two cases
kept in part read the home alone (read
`tests/text/test_review_axes.py#test_the_routing_section_holds_the_answers_and_the_shape`).

confirms: none
`payload_meter.py#imports_of` follows *Scope* item 5. It finds `@` at a
line's start or after whitespace and refuses a quoted or backticked path. It
expands `~` to the given home and resolves against the importer's directory,
stops at four hops, keeps one row per real path across the pair with the
pair's own files seeded, and leaves a missing target as a row (read
`skills/verify/scripts/payload_meter.py:100-105`, `:305-337`, `:340-384`).
The phase-3 claim that the meter has no fence rule is true, and neither
file of the pair nor the core holds a fenced `@` line.

confirms: none
The class of citations rule 19 owes was enumerated again with
`git grep -n "CLAUDE\.md"` over `skills`, `agents`, `hooks`, `templates`,
`docs`, `CONTRIBUTING.md` and `bin` (executed). Two lines still cite
"`CLAUDE.md`'s first goal", `docs/branch-and-release.md:99` and
`docs/release-checklist.md:193`, and both are under `frame/design.md`
*Rule changes*. No shipped skill or definition cites the old home.

confirms: none
The core ships references that only resolve in this repository:
`CONTRIBUTING.md` *What a change to a gate must carry* and `#1167`
(`skills/core/SKILL.md:93`, `:111-112`). A session in a plugin user's
repository would open its own `CONTRIBUTING.md` or issue. The design puts
the core's wording out of scope, and #1148 (body read) names this exact
reference as one in the wrong direction under its principle 2 and reads the
shipped core. That deferral has a home.

confirms: none
The labels are honest. `gaps.md` *Not verified* names the full suite, the
repository-wide ruff and Q2 as unverified, each with an answerer. Phase 4's
version move and fragment are one commit (executed `git show --stat
0c1144ef`: `.claude-plugin/plugin.json` and `changelog.md`). The narrow run
in *Probes* passed over the installer, meter, contract-shape and review-axes
modules.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether Claude Code resolves the block's relative line against a symlinked `~/.claude/CLAUDE.md`'s own directory or its target's (a dotfiles setup). `install.sh:99` and the meter's first hop use the link's directory; the meter's nested hops use the real path. No probe ran | `install.sh:99`, `skills/verify/scripts/payload_meter.py:330` | the orchestrator, with Q2's measurement after the release |
| `/agentic:update` reads `~/.claude/CLAUDE.md` and `~/.claude/plugins/...` at four places, so under `CLAUDE_CONFIG_DIR` step 4 never sees the block `install.sh` now writes there. This was true before the diff, and `trail/phases/phase-2.md` *Left for others* records it with no home | `skills/update/SKILL.md:46`, `:61`, `:81`, `:135` | the orchestrator, by a `seal/follow-up.md` row or an issue |
| Whether an orchestrating session should still hold the three-fix stop. `frame/design.md` *Removes* row 1 homes it in `agents/crafter.md`, which only the crafter receives, and decides only the batch rule's absence for the session explicitly. A session working under `no work item` now holds neither | `frame/design.md`, `agents/crafter.md:133` | the owner, at #1148's reading of every document against the core |
| The full suite, the repository-wide lint and the typecheck at `007d9cb9` | the tree | the orchestrator, through `seal gate` |
| Q2: the one-line block loads the core in an interactive and a headless session with no dialog | `frame/questions.md` | the orchestrator, on an installed machine after the release |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/behaviour/test_the_installer_writes_the_block_from_its_template.py tests/skills/test_payload_meter.py tests/text/test_every_agent_reads_the_contract.py tests/text/test_review_axes.py` | exit 0, 89 passed |
| `diff <(git show origin/release/v0.25.0:CLAUDE.md \| sed -n '3,$p') <(sed -n '/^## The first value/,$p' skills/core/SKILL.md)` | one hunk at old line 65: the routing sentence added, nothing else |
| `gh issue view 1183 --json body --jq .body \| grep -n -i "subagent\|spawn\|twice\|skills:"` | lines 20 and 28, both about a session; no subagent, spawn or `skills:` |
