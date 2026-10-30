# Design: 1793273065-the-core-reaches-no-users-repository

The plugin's core, the two sections `CLAUDE.md` opened with, is read by
nobody outside this repository: a plugin user's session reads the preset
block and an agent reads `agent-contract`, and neither carries it (#1177).
This design moves the core into one shipped file, `skills/core/SKILL.md`,
and gives every reader one way to reach it. An agent receives it through
its definition's `skills:` list. A session receives it from the plugin's own
`SessionStart` hook, which prints the file under a first line naming the
file, the plugin's version and the file's SHA-256, and `seal core` reads
that line back from the session's transcript. In this repository the hook
prints the tree's copy, so the tree's core governs here and a session reads
it once. The preset block, its installer, its uninstaller and
`/agentic:preset-setup` retire; `/agentic:update` takes an installed block
out of `~/.claude/CLAUDE.md`. The owner chose this shape (A5) over the
block's `@` line (A1) on 2026-10-30, after round 5, because under A1 every
agent read the core twice (`questions.md` Q1, the issue's *Update (owner,
2026-10-30)*).

## Grounding

| Policy clause or fact | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read at HEAD `346cd01d`): "A fact has one source, and every other place links to it" | The core is one file. The hook prints it and copies nothing into the tree; `CLAUDE.md` names it; no file keeps a copy. `tests/text/test_no_passage_is_pasted_into_a_second_file.py` reads `skills/` and `CLAUDE.md` for copies |
| `skills/core/SKILL.md` *The first value: efficient development through the workflow* (read): "this file holds what all of them share" | The core is not split into an agent's side and a session's side. Both readers get the same bytes |
| `docs/the-agent-set.md` *One contract every agent receives, and one definition each* (read): the file every agent receives arrives through `skills:` | `core` stands before `agent-contract` in every definition's `skills:` list (phase 1, closed at `5a283bd8`) |
| `docs/the-session-hooks.md` *Registration* (read): `hooks/hooks.json` registers `hooks/dispatch.py <group>` per event, a gate is added to `GROUPS`, and each script `GROUPS` names has one row in the gate table of `README.md` and `README.ko.md`, derived by `tests/behaviour/test_chain_hooks_hardening.py` | The core's printer is a gate of a new group, `session-core`, with one README row in each edition |
| `hooks/dispatch.py#merge` (read): where any gate of a group prints JSON, the merged output is the first JSON object, and a neighbour's plain text is dropped. `hooks/version-check.py` prints a JSON `systemMessage` when a release is behind (read) | The core cannot be a gate of the existing `session-start` group: on a day version-check speaks, the core would vanish. It gets its own group and its own `hooks.json` entry |
| `CONTRIBUTING.md` *House rules*, **Hooks stay local and quiet** (read): no writing outside the repository being worked on, and a crashing gate lets the work through | The hook only reads. Taking a block out of `~/.claude/CLAUDE.md` stays `/agentic:update`'s act, which a person asked for |
| `docs/one-root-by-lifetime.md` *The opt-in signal is the root itself* (read): every gate is silent in a repository with no `seal/` root; `stub-remove` runs in any git repository (`README.md` gate table, read) | The opt-in is a convention for gates that judge or write, not for the core: the session that bootstraps a fresh repository has no root at its start and orchestrates its first work item, so a hook keyed to the root would leave that session without the core. The hook prints in every session, the reach the issue's default and A1 had |
| `skills/update/SKILL.md` steps 1 and 5 (read at HEAD): a session keeps the version it started with, and `$CLAUDE_PLUGIN_ROOT` still resolves to it | `/agentic:update` from 0.24.x to 0.25.0 runs 0.24.x's procedure, never 0.25.0's |
| 0.24.2's `skills/update/SKILL.md` step 4 (read at `~/.claude/plugins/cache/agenticseal/agentic/0.24.2/`): it diffs the marker region of the refreshed marketplace clone's `templates/setup/claude-md-block.md` against `~/.claude/CLAUDE.md` and, where they differ, backs up and replaces the region with the template's | The 0.25.0 template must hold no `@` line, or the update to 0.25.0 would install a second read of the core. It holds the two markers and nothing between them, so that update leaves an empty marker pair; 0.25.0's own step 4 takes the pair out at the next update. A missing template would leave 0.24.x's step diffing a file that is not there, which no case can predict |
| The issue body and its update: `gh issue view 1177 --repo MichaelYcJo/AgenticSeal --json body,comments` (executed 2026-10-30): the update is the request; one comment, 2026-10-29, the prevention home for the core's byte figures, which still holds | Exact byte figures live in the phase record that measured them and in the pull request body at the broad gate's HEAD; every other record states approximate tokens and links there |
| #1183 (executed, `gh issue view 1183`): its *Update (owner, 2026-10-30)* takes A5 and has #1177 own the switch | The pull request closes #1183 as well as #1177 |
| The orchestrator's probe of 2026-10-30 (read, `hook-probe/results.md` in the session scratchpad, two runs, Claude Code 2.1.312, `--plugin-dir`): a plugin `SessionStart` hook's stdout reached the main session and not a `general-purpose` subagent; the project's `CLAUDE.md` reached both; a `SubagentStart` hook's `additionalContext` reached the subagent only | A session reads the core once, from the hook, and an agent once, from `skills:` |
| Probe R, resume (executed 2026-10-30, Claude Code 2.1.312, `claude -p --model haiku --tools "" --plugin-dir <scratch plugin> --output-format json`, then `claude -p --resume <id>` with the same flags). The scratch plugin's `SessionStart` hook had no matcher and printed one numbered fact per run, naming the payload's `source` | The resumed session answered both the startup run's fact and the resume run's fact. A resumed session keeps its start's output, and a hook that also answers `resume` puts a second copy in. The matcher leaves `resume` out |
| Probe M, matcher (executed, same flags, the hook registered with `"matcher": "startup\|clear\|compact"`) | The resume run fired no hook, and the resumed session answered the startup fact alone. The harness filters `SessionStart` by `source` through the matcher |
| Probe C, compact (executed, `claude -p --resume <id> ... "/compact"`, then a resumed question). Read from that transcript with a scratch reader that prints entry types and no content | The compaction wrote a `type: system` entry with `subtype: compact_boundary`, `parentUuid: null` and `compactMetadata` (`trigger` `manual`, `preservedMessages.uuids`, `preservedSegment`), then a `user` entry with `isCompactSummary: true`, then an `attachment` entry of `type: hook_success`, `hookName: SessionStart:compact`. The session after it answered the compact run's fact, so a compaction's hook output reaches the context. The summary carried the earlier facts as paraphrase. Two `SessionStart:resume` entries written just before the boundary were listed in `preservedMessages.uuids` and stayed in context word for word |
| A survey of this machine's interactive transcripts (executed, `grep -rl compact_boundary ~/.claude/projects`, then the scratch reader over 23 main transcripts, Claude Code 2.1.283 to 2.1.312) | Every `compact_boundary`, `auto` and `manual`, is followed by an `isCompactSummary` entry and a `SessionStart:compact` `hook_success`. A resume appends a `SessionStart:resume` entry to the same file; a `/clear` opens a new file whose first `SessionStart` entry is `SessionStart:clear` |
| Probe S, size (executed, the scratch hook printing 9,990, 10,010 and 11,049 characters, one session each) | At 9,990 characters the entry's `content` equalled its `stdout`. At 10,010 and 11,049, `stdout` held the whole output and `content`, what the model received, was a `<persisted-output>` preview of about 2,400 characters naming a file. The 11,049 run's session said it saw only the preview. The harness's cap on one hook's output lies between 9,990 and 10,010 characters |
| `wc -c skills/core/SKILL.md` and a character count (executed at HEAD): 6,749 B, 6,705 characters | The core and its first line sit near 6,900 characters, about 3,100 under the cap. A case holds the hook's whole output under 10,000 characters, so a core that #1148 grows past it fails in CI and not silently in a session |
| The owner, 2026-10-30, in the orchestrating session (the orchestrator's finding): the core's prose is refactored in this work, not in #1148 or #1170, keeping every directive and every sentence that gives a directive's reason, and removing only repetition and pointers to issues. A draft at `/private/tmp/claude-501/-Users-michael-Documents-GitHub-SpecSeal/aa6bb73b-1ad1-4e11-8e2a-ddc39af2340a/scratchpad/core-draft/SKILL.md` is 5,518 B against the core's 6,780 B at `dc030a86` (`wc -c`, executed by the orchestrator), of which the frontmatter is 673 B at `dc030a86` | Scope items 9 to 12 and phase 8. The draft is a starting point the crafter checks sentence by sentence against the core at `dc030a86`; it is not a source |
| `evals/README.md` *The behaviour suite* (read): "A rewrite of an agent's preload is proved not worse by running this suite on the old tree and on the new one", compared by `evals/scripts/noninferiority.py`. Past sides cost 16.12 USD for the framer and 3.34 USD for the sealer (`git show a19090962:…/framer-phase-2.md`, `b196fe9bc:…/sealer-phase-3.md`, executed) | The core is a preload of all four agents with cases under `evals/behaviour/`, so the refactor is proved by the four agents' suites, old side at `6ebfada5`, the commit before phase 8's first, so the two sides differ by phase 8 alone, and new side at phase 8's last commit (S11) |
| `env` in this agent's Bash (executed): `CLAUDE_CODE_SESSION_ID` is set and names the orchestrating session, whose transcript is `~/.claude/projects/<slug of its starting directory>/<that id>.jsonl` (`ls`, executed); `CLAUDE_PLUGIN_ROOT` is not set in a Bash call. `hooks/lib/hooksession.py#SESSION_VARIABLE` names that variable (read) | `seal core` finds the transcript from the session id, and compares against the file the hook's first line names, since it cannot read the hook's plugin root |
| The `SessionStart` payload (executed, logged by the scratch hook): `cwd`, `hook_event_name`, `session_id`, `source`, `transcript_path`, and on `resume` a few cost fields | The hook knows the session's working directory, so it can tell the plugin's own repository from any other |
| `.claude-plugin/plugin.json` at HEAD (read): `name` `agentic`, `version` `0.25.0` | The hook prints the tree's copy where the session's repository is a clone of this plugin: its top level holds `.claude-plugin/plugin.json` naming the running plugin, and `skills/core/SKILL.md` |
| `claude --help` (executed): "`--bare` Minimal mode: skip hooks (those defined in settings and by installed plugins …) … Anthropic auth is strictly ANTHROPIC_API_KEY or apiKeyHelper". `claude -p --bare …` here printed `Not logged in` (executed) | A bare session runs no plugin hook, so `seal core` fails there. No bare session can run on this machine; a planted transcript stands in (`questions.md` Q3) |
| `skills/verify/scripts/payload_meter.py` (read): `calibration_of` reads each subagent transcript's first assistant `usage` and subtracts the `general-purpose` spawn's prefix (`BASELINE_AGENT`, line 93); `composition` lists one agent's definition, skills and the `CLAUDE.md` pair with what their `@` lines import | Neither the baseline subagent nor a plugin agent receives the hook's output (the orchestrator's probe), so the subtraction still leaves each agent's own files and `BASELINE_AGENT` stays. What the meter lacks is the session: a table of the pair plus the hook's output |
| code.claude.com/docs/en/memory.md (read 2026-10-29): an `@` import resolves against the file that holds it, at most four hops, and user-scope imports load without a dialog | The meter keeps following `@` lines (`imports_of`, phase 3): any user's `CLAUDE.md` can import a file, and the harness adds the pair to every spawn whatever the core does |
| `~/.claude/CLAUDE.md` on this machine holds the 0.24.x block, eight rules and no `@` line (the orchestrator's finding; read in this agent's own context) | During the switch no machine holds the core twice: the old block carries no core, and the 0.25.0 template carries no line that imports one |
| `docs/branch-and-release.md` *Cutting a release* (read): the version moves in the first pull request into `release/vX.Y.Z`, in the commit that adds the fragment | Phase 4 moved `plugin.json` to `0.25.0` (`0c1144ef`); phase 10 rewrites the fragment and leaves the version |

## Scope

**In.**

1. **The core is `skills/core/SKILL.md`, and every agent preloads it.**
   Phase 1 stands as built (`5a283bd8`). The one change to the file here is
   its `description:`, which says a session receives the core from the
   plugin's `SessionStart` hook instead of the block's `@` line.
2. **A hook prints the core into a session.** `hooks/lib/core.py` holds the
   one definition of what is printed, so the hook, the check and the meter
   share it:
   - `origin(cwd, plugin_root)`: the file to print. It is
     `<top>/skills/core/SKILL.md` where `<top>`, the top level `git -C <cwd>
     rev-parse --show-toplevel` prints, holds `.claude-plugin/plugin.json`
     whose `name` equals the `name` in `<plugin_root>/.claude-plugin/plugin.json`
     and holds that file. Otherwise it is `<plugin_root>/skills/core/SKILL.md`.
   - `header(path, version, digest)`: the first line, `AgenticSeal core from
     <absolute path>, plugin <version>, sha256 <64 hex digits>.`, where the
     digest is over the file's bytes as read.
   - `output(cwd, plugin_root)`: the header, a newline, then the file's text.
     Where the file is not there, the one line `AgenticSeal core: <path> is
     not a file, so no core was printed.`
   - `CAP = 10_000`, the harness's cap on one hook's output in characters,
     measured between 9,990 and 10,010 on Claude Code 2.1.312 (*Grounding*,
     probe S).
   - `parse(text)`: the header's three fields and the body, or `None` where
     the first line is not a header.

   `hooks/core-start.py` reads the payload's `cwd`, takes the plugin root
   from `$CLAUDE_PLUGIN_ROOT` and the version from its `plugin.json`, and
   prints `output(...)` as plain text. `hooks/dispatch.py#GROUPS` gains
   `"session-core": ("core-start.py",)`. `hooks/hooks.json` gains a second
   `SessionStart` entry, `"matcher": "startup|clear|compact"`, running
   `dispatch.py session-core` in the shape of the other entries. `resume` is
   left out because a resumed session keeps its start's output (probe R); a
   compaction drops it and `compact` prints it again (probe C); `/clear`
   opens a new context. The hook prints in every session, in any directory.
3. **`seal core` reads the fact back.** `skills/verify/scripts/core_check.py`,
   registered in `skills/implement/scripts/seal.py#TOOLS` as `core`, with the
   help line "whether this session's context holds the core, read from its
   transcript". It reads the transcript named by `--transcript <path>`, or
   else the file `<config>/projects/*/<id>.jsonl`, where `<config>` is
   `$CLAUDE_CONFIG_DIR` or `~/.claude` and `<id>` is
   `$CLAUDE_CODE_SESSION_ID` (`hooks/lib/hooksession.py#SESSION_VARIABLE`).
   The project directory is globbed, because its name encodes the working
   directory the session started in, which a worktree changes.
   - **In context** is every entry after the last `type: system`,
     `subtype: compact_boundary` entry, and every earlier entry whose `uuid`
     that boundary's `compactMetadata.preservedMessages.uuids` lists. With no
     boundary, every entry is in context.
   - **A core entry** is an in-context `type: attachment` entry whose
     `attachment.type` is `hook_success`, whose `attachment.hookEvent` is
     `SessionStart`, and whose `attachment.stdout` opens with a header
     `parse` reads.
   - **It passes, exit 0,** where exactly one core entry is in context, its
     `attachment.content` equals its `attachment.stdout`, the body equals the
     file the header names, and that file's SHA-256 equals the header's.
     Bodies are compared with every `\r` before a `\n` read as part of the
     line ending, and with trailing line endings, a last `\r` included,
     removed. It prints one line: the header's path, version and digest, the
     `hookName`, and "in context once".
   - **It fails, exit 1,** with one line naming the reason, where: no
     session id and no `--transcript` was given; no transcript is found; no
     core entry is in context (it names `--bare` where `CLAUDE_CODE_SIMPLE` is
     `1`); `content` is not `stdout`, which is the harness's preview past
     `CAP`; the body or the digest differs from the file on disk; the named
     file is not there; or more than one core entry is in context. A
     transcript whose shape it does not recognise has no core entry, so a
     Claude Code release that changes the shape fails the check.
   - Exit 2 stays `seal`'s own: an unusable argument, or a missing
     `hooks/lib/` module.
   - Run from an agent's Bash, `CLAUDE_CODE_SESSION_ID` names the session
     that spawned it (*Grounding*), so the check reads the orchestrating
     session's transcript. The help says so.

   `skills/implement/orchestration.md` *Orchestrator: the order inside a
   ticket*, step 1, gains one sentence: the orchestrator runs `seal core`
   once before the first edit; where it reports no core entry, the
   orchestrator opens the file the output names once, which is then the
   session's one read, and continues; any other failure is said in its next
   reply and the work goes on.
4. **The block and the machinery that writes it retire.** `install.sh`,
   `uninstall.sh` and `skills/preset-setup/` are deleted.
   `templates/setup/claude-md-block.md` becomes the two markers and nothing
   between them, for one release (*Grounding*, 0.24.2's step 4).
   `skills/update/SKILL.md` step 4 becomes *Take out the preset block*: in
   `${CLAUDE_CONFIG_DIR:-~/.claude}/CLAUDE.md`, a region between
   `<!-- agentic:start -->` and `<!-- agentic:end -->`, or between the older
   `<!-- specseal:start -->` and `<!-- specseal:end -->`, is backed up to
   `CLAUDE.md.bak` and removed with its markers, and the step says that the
   core now arrives from the plugin's hook and that the rules an older block
   stated stand in the skills and definitions. A start marker with no end
   marker stops the step with that said. No block means nothing is said.
   Where the current repository's `CLAUDE.md` holds a marker region, which
   0.24.x's `install.sh --project` wrote, the step names the file under
   *Needs action* and does not edit it, since the file is the project's
   committed text. No question is asked.
5. **This repository's `CLAUDE.md` says how a session here reaches the
   core.** `# AgenticSeal`, then *The core*: the core is
   `skills/core/SKILL.md`, one file for every party; an agent receives it
   through `skills:`; a session receives it from the plugin's `SessionStart`
   hook, and in this repository the hook prints the tree's copy, whose path
   its first line names, so the tree's core governs a session here and the
   session reads it once; this file imports nothing and copies nothing;
   where no hook message opening `AgenticSeal core from` stands in the
   session's context, the installed plugin predates the hook, and the
   session opens `skills/core/SKILL.md` once. An agent spawned here receives
   the installed plugin's copy, the last release's, through `skills:`, as it
   receives every other installed skill.
6. **`seal payload` counts the session's core.** The meter's JSON gains a
   `session` object and `render` a table before the agents': the
   `CLAUDE.md` pair with their imports (`harness` share, as today) and one
   row, `SessionStart hook: skills/core/SKILL.md`, share `hook`, whose bytes
   are `len(hooks.lib.core.output(root, root))` encoded, the output a
   session in the measured tree would receive; a tree with no
   `skills/core/SKILL.md` gets the row at 0 bytes, marked `missing`,
   because only a tree that has the hook prints `output`'s refusal, and a
   session in a tree without the core receives nothing. Tokens are estimated at
   `ASSUMED_RATIO` and labelled so; no transcript calibrates a session's
   prefix. `BASELINE_AGENT` stays `general-purpose`, and the module
   docstring says why: the hook's output reaches no subagent, so it is in
   neither the baseline's prefix nor an agent's. The before and after
   numbers come from two runs against a scratch home: base `53f21b54` with
   the 0.24.2 block, and HEAD with no block. Both go into phase 9's record
   and the pull request body.
7. **The release shape.** `changelog.md` is rewritten: its `### Fixed` entry
   says the core arrives in every session from the plugin's hook and in
   every agent through `skills:`, how to see it (`! seal core`), that
   `/memory` no longer lists it, how to turn it off (disable the plugin's
   hooks), that the preset block, `install.sh`, `uninstall.sh` and
   `/agentic:preset-setup` are gone, and that `/agentic:update` empties the
   old block on the way to 0.25.0 and takes it out at the next update. Its
   `### Process changes` row is rewritten. `gaps.md` *Not done* drops the
   double read, which this redesign fixes. `.test_durations` is refreshed
   from the branch's CI artifact once the new cases exist.
8. **What stood on the old fact is corrected in the same commit** (contract
   rule 19, found with `git grep` on "preset block", "preset-setup",
   "install.sh", "uninstall.sh", "claude-md-block", "`@` line" and
   "/memory"): the README rows and sections of both editions (the
   `CLAUDE.md block` row at `README.md:45`, the cheat-sheet rows at `:266`
   and `:270`, the install step at `:295-307`, the rename steps at `:323`,
   the update paragraph at `:369-372`, and `README.ko.md` the same);
   `skills/implement/orchestration.md:460`; `.gitignore:14`;
   `tests/censuses.py:1014-1015`; and every test docstring and case
   *Removes* names.
9. **The core's prose is refactored, and decides what it decided.** Every
   session and every agent reads `skills/core/SKILL.md` whole, so its size
   is paid in every session. The crafter removes the sentences that repeat
   another sentence of the core and the pointers to issues (`#1167`), and
   tightens the wording, keeping every directive, every path and section it
   cites, the five invariants, and every sentence that gives a directive's
   reason. The headings stay as they are, so no citation of a section
   moves. The `description:` phase 5 wrote stands. The proof is S11.
10. **The core says where it applies and how a user's repository reads it**
    (the owner, 2026-10-30, in the orchestrating session). The hook puts
    the core in every session on a machine with the plugin, in every
    repository, so three readings it allowed when only this repository's
    sessions read it are closed in phase 8's commit:
    - **Where it applies.** One sentence says the values govern work run
      through the workflow, and a session doing work outside the workflow
      is not bound by this file to start one. The routing sentence stays,
      and the gate that holds it judges only an opted-in repository.
    - **Whose paths.** One sentence says every path the core cites is
      relative to the plugin's root, the directory that holds the file the
      hook's first line names, and never to the session's repository.
      The sentence citing `CONTRIBUTING.md` *What a change to a gate must
      carry* names this plugin's repository, not a user's, so it moves to
      this repository's `CLAUDE.md`, which holds what is this repository's
      own.
    - **Whose owner.** "a command the owner runs" names whose owner: the
      owner of the repository whose release the judgments were made in.
    - **Whose mechanisms.** One sentence in *The rule a mechanism is kept
      against* says the rule governs this plugin's own mechanisms, its
      gates, checks and hooks. A user's repository's mechanisms are kept or
      removed by that repository's own policy. Read without it, "existing
      is no reason to keep it" lets a crafter remove a user's guard that
      has no record of catches (the owner chose this over extending the
      rule to every mechanism the workflow adds, 2026-10-30).
    These change how the core is read, not what its values decide. The
    proof is S11, run once over phase 8's commit.
11. **Where two sentences ask for one thing, one stays; where a sentence
    reads two ways, it is rewritten** (the owner, 2026-10-30, in the
    orchestrating session). The orchestrator's refined draft, 5,518 B at
    the path *Grounding* names, carries these as found by reading the core
    sentence by sentence; the crafter checks each against the core at
    `dc030a86` and may find more:
    - "nothing comes back mid-run" in *Asking a person* repeats the fifth
      invariant; it stays in the invariants alone.
    - "argued for time and stability" names no subject; it becomes what
      verification buys.
    - "the most expensive judgment" calls asking a judgment, and "the
      difference is argued" names nobody; asking becomes a step, and the
      design that asks argues its cost.
    - "in closed form" is this repository's word; it becomes "exactly, such
      as an exit code or a parser's result", and a guessed reading is
      reported, never used to block.
    - "its history shows what it caught against what it costs" leaves the
      comparison open; it becomes a record of catches that outweighs the
      cost.
    - "A few invariants hold the chain and are not open to judgment", which
      a first draft dropped, stays: without it the five items lose their
      standing.
    Two pairs that look alike stay apart, because each says a different
    thing: judgment by meaning against a script's exact answer (the first
    value), and what a script may block on (the rule).
12. **The hook prints the core without its frontmatter.** The
    `description:` reaches every session already, in the harness's skill
    listing, so printing it again puts it in context twice. `output` prints
    the file's body below the closing `---`, the header's digest stays the
    whole file's, and `seal core` compares the entry against that body. The
    `vercel` plugin's `SessionStart` injector strips frontmatter the same
    way (`hooks/inject-claude-md.mjs`, `stripFrontmatter`, read in the
    marketplace cache 2026-10-30 by the orchestrator).

**Out.**

- What the values decide. #1170 and #1148 own any change to it; this work
  refactors their prose (Scope item 9) and closes the readings global
  delivery opened (Scope item 10).
- A `SubagentStart` hook, or a memory line telling a session to load the
  core skill: the owner decided against both (the issue's *Decided in this
  update*).
- How long a straight upgrade from before 0.23.0, or from 0.24.x past
  0.25.x, stays supported, and so when the emptied template and the
  `specseal` markers go: #1154 (0.25.2).
- The README rewritten for a first reader: #1102 (0.25.1). Only the rows and
  sections this change makes false are rewritten.
- Writing `~/.claude/CLAUDE.md` on this machine or any other. It changes
  through `/agentic:update` after the release.
- What `/memory` and `/context` show on screen for the hook's output. An
  interactive screen is the owner's to read (`questions.md` Q2).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 An agent receives the core once | Given any definition under `agents/`, when the harness spawns it, then its context holds `skills/core/SKILL.md` from `skills:` and from nothing else | `tests/text/test_every_agent_reads_the_contract.py` (phase 1); the block template holds no `@` line (S6's case); `seal payload` lists the core once per agent |
| S2 A session receives the core once | Given a session started, cleared or compacted with the plugin enabled, when its context is built, then the hook's output is in it once, and a resumed session holds its start's output and no second copy | `tests/hooks/test_core_start.py`: the printed text is `output(...)` for `startup`, `clear` and `compact` payloads; a case reads `hooks/hooks.json` and finds the `session-core` entry with the matcher `startup\|clear\|compact`; probes R, M and C (*Grounding*) for the harness's half |
| S3 The output names its origin | Given the hook's output, when its first line is read, then it names the file printed, the plugin's version and that file's SHA-256 | `tests/hooks/test_core.py`: `header` and `parse` round-trip; the digest is the file's; a header with a path holding a comma parses |
| S4 The tree's core governs here | Given a session whose working directory is a clone of this plugin, when the hook runs, then it prints that clone's `skills/core/SKILL.md`; in any other repository, or outside one, it prints the plugin's | `tests/hooks/test_core.py`: a scratch repository holding `.claude-plugin/plugin.json` named `agentic` and a core gets the tree's path; one named otherwise, one with no core file, and a directory outside git get the plugin's |
| S5 A session can verify the core loaded | Given a session's transcript, when `seal core` runs, then it exits 0 for one whole core entry in context matching its file, and 1 with the reason for every other state | `tests/skills/test_core_check.py` over planted transcripts: one startup entry passes; no entry fails; an entry only before the last boundary fails; an entry the boundary preserves counts; startup plus compact after one boundary passes; two entries in context fail; `content` a preview fails; a file changed after the start fails on the digest; a missing named file fails; no session id fails; `CLAUDE_CODE_SIMPLE=1` names `--bare`. Each case seen red first |
| S6 The block leaves without a second read | Given a machine on 0.24.x, when `/agentic:update` runs to 0.25.0 and later past it, then the first run leaves an empty marker pair and the second removes it, and no step writes an `@` line | `tests/behaviour/test_the_old_block_leaves_through_update.py`: the template's marker region is the two markers alone; `skills/update/SKILL.md` step 4 removes both marker pairs after a backup, names the hook, and names a project file it does not edit; this repository's `CLAUDE.md` holds no marker and no `@` line |
| S7 The output stays under the harness's cap | Given the tree's core, when `output` is built, then it is under `CAP` characters | A case in `tests/hooks/test_core.py` reads the tree's `skills/core/SKILL.md` through `output` |
| S8 The cost is measured | Given the tree before and after, when `seal payload` runs against a scratch home, then a session table shows the pair and the hook's row, and every agent's table shows the core once | `tests/skills/test_payload_meter.py`: the session table carries the hook row with `output`'s bytes; the JSON's `session` object; the agent tables carry no hook row; phase 9's record carries the two numbers |
| S9 The machinery is gone | Given the tree, when it is searched, then `install.sh`, `uninstall.sh` and `skills/preset-setup/` are absent and no shipped document tells a reader to run them | The README cases; `tests/behaviour/test_chain_hooks_hardening.py` without its `preset-setup` and `install.sh` cases; `git grep` in the phase record |
| S10 The release names the change | Given the fragment, when it is read, then it says how the core arrives, how to see it and how to turn it off, and ends with its process table | `tests/github/test_publish_release_note.py` for the shape; the sealer reads the text |
| S12 The core reads the same in any repository | Given a session or agent in a repository that is not this plugin's, when it reads the core, then it reads which work the core governs, resolves each cited path against the plugin's root, and finds no sentence that names this plugin's own repository | The proofer reads `skills/core/SKILL.md` at phase 8's commit against Scope item 10; `CLAUDE.md` holds the `CONTRIBUTING.md` sentence; every case that read that sentence in the core reads it in `CLAUDE.md` (found by `git grep -l "What a change to a gate must carry" -- tests`); S11 runs over the same commit |
| S11 The refactored core decides what the core decided | Given the four agents that preload the core, when each agent's behaviour suite runs on the tree at `6ebfada5` and at phase 8's last commit, then the new side passes the five rules of `noninferiority.py#verdict` against the old side | `evals/scripts/noninferiority.py run` for `framer`, `crafter`, `proofer` and `sealer` on both sides and `compare --phase 8`, each record written to `seal/threads/1793273065-the-core-reaches-no-users-repository/evals/<agent>-phase-8.md`; the cases that already read the core (phase 5's set) stay green with no case added, since a refactor adds no behaviour; S7's case holds the smaller output under `CAP` |

## Data & interfaces

- `hooks/hooks.json`, the added entry under `SessionStart`:

  ```
  {
    "matcher": "startup|clear|compact",
    "hooks": [
      {
        "type": "command",
        "command": "python3 \"${CLAUDE_PLUGIN_ROOT}/hooks/dispatch.py\" session-core || py -3 \"${CLAUDE_PLUGIN_ROOT}/hooks/dispatch.py\" session-core"
      }
    ]
  }
  ```

- The hook's output, in shape:

  ```
  AgenticSeal core from /Users/x/.claude/plugins/cache/agenticseal/agentic/0.25.0/skills/core/SKILL.md, plugin 0.25.0, sha256 <64 hex digits>.
  ---
  name: core
  …the file as it stands
  ```

  The header's pattern is `^AgenticSeal core from (?P<path>.+), plugin
  (?P<version>\S+), sha256 (?P<digest>[0-9a-f]{64})\.$`, anchored at the
  end so a path holding a comma still parses.
- `hooks/lib/core.py`: `origin`, `header`, `output`, `parse`, `CAP`, as
  *Scope* item 2 states. Python 3.9 syntax, since a hook runs under a stock
  macOS `python3`.
- `skills/verify/scripts/core_check.py`: `main(argv)`; `--transcript PATH`;
  the exit codes of *Scope* item 3. It imports `hooks/lib/core.py` by path
  as `seal.py` imports its `hooks/lib/` modules, and `seal.py#HOOK_PURPOSES`
  gains `core.py` with the sentence "it is what reads the core hook's first
  line".
- The transcript entries the check reads, as Claude Code 2.1.312 writes them
  (*Grounding*, probe C and the survey): `{"type": "system", "subtype":
  "compact_boundary", "compactMetadata": {"preservedMessages": {"uuids":
  [...]}, ...}}`; `{"type": "attachment", "uuid": ..., "attachment":
  {"type": "hook_success", "hookEvent": "SessionStart", "hookName":
  "SessionStart:<source>", "stdout": ..., "content": ..., "command": ...}}`.
- `payload_meter.py`: `session_composition(root, home)` returning the rows
  of *Scope* item 6; `measure` adds `out["session"]`; `render` prints it.
- `templates/setup/claude-md-block.md` after the change, whole:

  ```
  <!-- agentic:start -->
  <!-- agentic:end -->
  ```

- `changelog.md`: `### Fixed` with one entry, then `### Process changes`
  with one row, date `2026-10-30`, change "the core is one shipped file every
  agent preloads through `skills:` and every session receives from the
  plugin's `SessionStart` hook, whose first line `seal core` reads back; the
  preset block and its installer retire", why "the values that make the
  workflow reached no repository but this one, and the block's import made
  every agent read them twice", source the issue.

## Rule changes

- change
  file: docs/the-agent-set.md
  section: One contract every agent receives, and one definition each
  from: **The rules true of every agent live in one file every agent receives before its first tool call, without a prompt asking for it.**
  to: **The core every party shares and the rules true of every agent each live in one file every agent receives before its first tool call, without a prompt asking for it: `skills/core/SKILL.md`, then `skills/agent-contract/SKILL.md`, in that order in every definition's `skills:` list.**
- change
  file: docs/the-record-layout.md
  section: Every kind of record, at a glance
  from: | The repository's rules | `CLAUDE.md` for the rules a session must hold, `CONTRIBUTING.md` for a contributor's procedure, and the `docs/` document each one links to | each file under target | this document, and `docs/README.md` |
  to: | The repository's rules | `skills/core/SKILL.md` for the core every party reads, `CLAUDE.md` for how a session in this repository reaches it, `CONTRIBUTING.md` for a contributor's procedure, and the `docs/` document each one links to | each file under target | this document, and `docs/README.md` |
- change
  file: docs/the-record-layout.md
  section: A change writes fragments, never a shared file
  from: A work item whose diff changes `CLAUDE.md`, an `agents/*.md` file, a `skills/*/orchestration.md` file or `skills/implement/bootstrap.md` ends its `changelog.md`
  to: A work item whose diff changes `skills/core/SKILL.md`, `CLAUDE.md`, an `agents/*.md` file, a `skills/*/orchestration.md` file or `skills/implement/bootstrap.md` ends its `changelog.md`
- change
  file: docs/the-record-layout.md
  section: The root records
  from: | `CLAUDE.md` | the rules a session in this repository must hold, each linking to its home |
  to: | `CLAUDE.md` | how a session in this repository reaches the core, `skills/core/SKILL.md`, which the plugin's hook prints from the tree here; any rule this repository alone asks of a session, each linking to its home |
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: a red nobody here can act on is what `CLAUDE.md`'s first goal is against.
  to: a red nobody here can act on is what `skills/core/SKILL.md` *The first value: efficient development through the workflow* is against.
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: a red nobody can act on is what `CLAUDE.md`'s first goal is against.
  to: a red nobody can act on is what `skills/core/SKILL.md` *The first value: efficient development through the workflow* is against.
- add
  file: docs/the-session-hooks.md
  section: Registration
  to: **The core reaches a session from the plugin's own `SessionStart` hook, once.** `hooks/hooks.json` registers `hooks/dispatch.py session-core` for `SessionStart` with the matcher `startup|clear|compact`, and its one gate, `core-start`, prints `skills/core/SKILL.md` under a first line naming the file it printed, the plugin's version and the file's SHA-256. A resumed session keeps the output its start printed, so `resume` is not matched; a compaction drops it, so `compact` prints it again. In a clone of the plugin's own repository the file printed is the clone's. The core has a group of its own because a group merges a gate's plain text away beside a neighbour's JSON. The whole output stays under the harness's cap on one hook's output, measured between 9,990 and 10,010 characters, past which the context holds a preview and not the file. `seal core` reads the entry back from the session's transcript and exits 1 unless the context holds it once and whole.
    check: tests/hooks/test_core.py tests/hooks/test_core_start.py tests/skills/test_core_check.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The eight rule bullets of the preset block | `templates/setup/claude-md-block.md` at base `53f21b54` | Phase 2 (`6eaf371c`) moved each to its home, and that stands: tooling and lint in `skills/implement/SKILL.md` *2.*, worktrees in `skills/implement/orchestration.md` step 1, the three-fix rule in `agents/crafter.md`, the verification gate in `skills/verify/SKILL.md` and contract rule 4, the scope in contract rule 2, batching in contract rule 10, routing in `skills/implement/orchestration.md` *Orchestrator: how the work is routed* with the core naming it |
| The two sections of `CLAUDE.md` | `CLAUDE.md` at base | `skills/core/SKILL.md` (phase 1) |
| The block's `@` line | `templates/setup/claude-md-block.md:2` | The hook carries the core. The template keeps its two markers for one release, so 0.24.x's update step empties an installed block |
| The installer | `install.sh` | Nothing is left to write: the template is two markers. Its reason to exist, that a plugin cannot carry what a `CLAUDE.md` block carries, is false: a plugin hook's output reaches the session (the orchestrator's probe, *Grounding*) |
| The uninstaller | `uninstall.sh` | `skills/update/SKILL.md` step 4 is the one place an installed block is taken out; two removers would be two sources of one act. A user who uninstalls the plugin deletes the lines between the markers, which the README says |
| `/agentic:preset-setup` | `skills/preset-setup/SKILL.md` | It wrote the block from inside Claude Code; there is no block to write |
| The diff-and-replace body of update step 4 | `skills/update/SKILL.md` *4. Take the preset block if it moved*, its diff command, its four-row table and its paragraph on a session in a clone of the plugin's own repository | The step takes the block out instead (*Scope* item 4); a session here reads the hook, not a block |
| The installer's test module | `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py`, whole | `tests/behaviour/test_the_old_block_leaves_through_update.py` holds what still needs holding (S6) |
| Cases that read the installer or the setup skill | `tests/behaviour/test_chain_hooks_hardening.py:198-203` (preset-setup migrated) and `:1165-1176` (namespaced commands in `install.sh`); `tests/behaviour/test_release_hygiene.py#test_update_tells_the_user_when_the_preset_block_changed`, rewritten to the removal step; the `install.sh` and `uninstall.sh` entries of `tests/behaviour/test_release_hygiene.py:50-51`, `tests/behaviour/test_the_release_check_watches_what_ships.py:65-66` and `tests/behaviour/test_no_document_names_the_old_roots.py:47-48`; the template cases `tests/text/test_no_passage_is_pasted_into_a_second_file.py#test_a_paste_into_the_block_template_is_named` and `#test_the_block_template_is_read_whole_and_fences_and_headings_are_not`; the template read in `tests/text/test_a_language_section_of_writing_style_opens_alone.py#test_the_rules_for_text_an_agent_or_a_check_reads_reach_both_languages` (line 185) and the template entry of `tests/text/test_the_rules_claude_md_names_have_one_home.py#CARRIERS` | The files they read are gone or hold two markers. A census or list entry for a deleted file goes with it |
| The `@`-line wording in test docstrings | `tests/behaviour/test_first_setup_asks_once.py:788-798`, `tests/text/test_review_axes.py:210`, `tests/text/test_broad_gate_rule.py:5-6`, `tests/text/test_the_rules_claude_md_names_have_one_home.py:24` and `:100-101`, `tests/skills/test_payload_meter.py#Test_measure.test_an_import_in_either_file_of_the_pair_is_a_harness_row_under_it` (its docstring and its planted A1 line) | Each says the core reaches a session from the hook |
| The A1 sentences of shipped text | `skills/core/SKILL.md:7-8` (description), `CLAUDE.md:5-17`, `skills/implement/orchestration.md:460` ("through the preset block's one `@` line"), `README.md:45`, `:266`, `:270`, `:295-307`, `:323`, `:369-372` and `README.ko.md` the same rows, `.gitignore:14` ("generated by install.sh") | Each says the hook, `seal core`, or `/agentic:update`'s removal in its place |
| The closing memo's double-read paragraph | `gaps.md` *Not done* | The redesign fixes it: no session and no agent reads the core twice |
| The core's sentence citing `CONTRIBUTING.md` *What a change to a gate must carry* | `skills/core/SKILL.md` at `dc030a86`, the last sentence of *The rule a mechanism is kept against* | It names this plugin's repository; read in a user's repository it names that repository's file. It moves to this repository's `CLAUDE.md` (Scope item 10) |
| The core's repeated sentences and its pointer to #1167 | `skills/core/SKILL.md` at `dc030a86` | Each repeated sentence states a fact another sentence of the core already states; the pointer names an issue that closes while the core is read in every session. Scope item 9, proved by S11 |

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-29 by framer, before the build.
Reframed 2026-10-30 by framer, after round 5.
