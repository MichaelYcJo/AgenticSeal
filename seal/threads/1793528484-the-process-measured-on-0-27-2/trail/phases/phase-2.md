# Phase 2: 1793528484-the-process-measured-on-0-27-2

## What this phase found

### The measured state

- **The after tree is still `94b03636`**, the head of `origin/release/v0.27.2` after `git fetch origin` when the phase started (executed: `git rev-parse origin/release/v0.27.2`). `git diff --stat 94b03636 origin/release/v0.27.2 -- . ':!seal/threads' ':!seal/follow-up.md'` printed nothing, so no process change landed after the frame. Scenario S8's `git diff --stat origin/release/v0.27.2...HEAD -- . ':!seal/threads/1793528484-the-process-measured-on-0-27-2'` printed nothing at `a937e12a` (both executed).
- **#1038 was not merged when this phase read it.** Pull request #1257 was open at `f8d1b8f6` (executed: `gh pr view 1257 --json state,headRefOid,mergedAt,mergeCommit`). Its six segments below were read before its merge. #1257 merged at 2026-11-01T11:35:14Z as `569780ef` with its head still `f8d1b8f6`, and #1038's directory is the same at both commits (executed: `gh pr view 1257 --json state,mergedAt,mergeCommit,headRefOid`, `git diff --stat f8d1b8f6 569780ef -- seal/threads/1793521558-the-record-decides-each-proposed-verifier`, which printed nothing), and phase 3 found no seventh segment (`trail/phases/phase-3.md` *The measured state*), so the six are its whole run.
- **The moment.** Both samples were read at 2026-11-01T11:00:09Z (executed: `date -u` before each run). Session `db35d01d` ended in October and no longer grows. Session `fabe08e7` held 35 subagent transcripts at that moment (executed: `ls <session>/subagents/*.jsonl | wc -l`).
- **The before segments** are session `db35d01d`'s 30 segments of the four kinds: 12 `specseal:framer`, 4 `specseal:smith`, 9 `specseal:warden` and 5 `specseal:sealer`. Each names plugin 0.20.0 as the first plugin cache path in its transcript, each records Claude Code 2.1.292 on every row, and each ends with a `SubagentHandback` call (executed: `segments.py`). The session's other 17 segments are `general-purpose` and `fork`, which are none of the four kinds.
- **The after segments** are session `fabe08e7`'s 32 segments whose spawn description names #1221, #1222, #1223, #1229 or #1038: 5 `agentic:framer`, 9 `agentic:crafter`, 12 `agentic:proofer` and 6 `agentic:sealer`. Each names plugin 0.27.1, each records Claude Code 2.1.316 on every row, and each ends with a `SubagentHandback` call, so none of them grows after the moment above (executed: `segments.py`). Three transcripts are left out because they are this work item's own: `agent-a34e51bcc13459bc7` (the framer of #947), `agent-a910c8ca62680218b` (phase 1) and `agent-ad3977b73b3102826` (this phase, still running). No segment of either sample failed to confirm.
- **The kinds pair** as `frame/design.md` G12 says: framer and framer, smith and crafter, warden and proofer, sealer and sealer.

### Whether the frame holds

G10's counts hold at the moment above: `fabe08e7` holds 5 framer, 9 crafter, 12 proofer and 6 sealer segments of the five after work items, and `db35d01d` holds 12, 4, 9 and 5 segments naming plugin 0.20.0 (executed: `segments.py`). The tree's reader `skills/verify/scripts/payload_meter.py#first_prefix` reads the first assistant `usage` block as *Scope* item 6 defines the measure (read), so `segments.py` imports it from this worktree and calls it, as `frame/plan.md` *Alternatives considered* A4 chooses.

Two readings the frame names do not give the body's figures, and one reading needs a rule the frame leaves open. Each is decided below.

1. *Scope* item 6's before does not reproduce. Every figure of the body is above the largest first prefix of its kind in `db35d01d`: framer 83,437 against a largest 80,804, crafter 84,823 against 83,309, proofer 78,624 against 75,112, and sealer 58,386 against 57,819. No subset of this sample gives the body's medians.
2. *Scope* item 7's readings (a) and (b) give medians under 7 KB on the before side, where the body gives 134 KB to 310 KB. Neither is within 10 per cent of any of the body's three figures.
3. *Scope* item 7 (b) counts a file "whether in the repository or the plugin's installed copy", and does not say how a path is placed in the repository. A segment's working directory does not place it: framer `agent-a1b1794efec644816` ran with its working directory at the main checkout and read every repository file it opened from a worktree of #836.

### The measures

Every figure below is `executed` by `segments.py` at the moment above, and each command stands whole under *Commands*. A median is over the segments of one kind on one side. A byte count is the UTF-8 bytes of the tool result's text.

**First-turn prompt tokens per spawn, the median.** The first assistant `usage` block's `input_tokens + cache_creation_input_tokens + cache_read_input_tokens`, read by `payload_meter.first_prefix`. The before ran under Claude Code 2.1.292 and the after under 2.1.316, so the harness's own share of each prefix can differ between the sides.

| Kinds | Body | Re-run over `db35d01d` | After over `fabe08e7` | Before |
|---|---|---|---|---|
| framer, framer | 83,437 | 73,640 (12 segments) | 45,218 (5) | not reproduced (-11.7 per cent) |
| smith, crafter | 84,823 | 83,160 (4) | 44,342 (9) | not reproduced (-2.0 per cent) |
| warden, proofer | 78,624 | 75,004 (9) | 43,876 (12) | not reproduced (-4.6 per cent) |
| sealer, sealer | 58,386 | 57,799 (5) | 43,892 (6) | not reproduced (-1.0 per cent) |

**Prose opened on demand per spawn, the median.** Reading (a) is every tool result returned for a `Read` of a path ending `.md`. Reading (b) is the same, restricted to files under `agents/`, `skills/`, `docs/` and `templates/`, and to `CLAUDE.md` and `CONTRIBUTING.md`, by the rule of decision 3 below.

| Kinds | Body | Before (a) | Before (b) | After (a) | After (b) | Before |
|---|---|---|---|---|---|---|
| framer, framer | 310,350 B | 6,340 B | 1,070 B | 0 B | 0 B | not reproduced |
| smith, crafter | 296,676 B | 846 B | 0 B | 34,653 B | 33,989 B | not reproduced |
| warden, proofer | 134,716 B | 0 B | 0 B | 0 B | 0 B | not reproduced |
| sealer, sealer | no figure | 0 B | 0 B | 0 B | 0 B | no figure to reproduce |

`segments.py` also prints (a) and (b) over the file content the harness records beside each result, which leaves out the line numbers a `Read` result carries. Those figures run 3 to 53 per cent under (a) and (b) where they are not zero, and they change no label above.

The after crafters' 33,989 B in (b) is one `Read` of `skills/implement/SKILL.md`, which `agents/crafter.md` step 1 tells the crafter to open. Seven of the nine after crafter segments read that file, five of them once and two twice, and one of the two also read `skills/verify/SKILL.md`. The other two crafter segments read nothing (b) counts.

**Each segment.** The plugin version is the first plugin cache path the transcript names. The work item is the one the spawn description names; the before descriptions are not filtered, so the column holds `-`.

| Session | Agent file | Kind | Work item | Plugin | Claude Code | First prefix | (a) B | (b) B |
|---|---|---|---|---|---|---|---|---|
| `db35d01d` | `agent-a0251159d8279a689` | specseal:framer | - | 0.20.0 | 2.1.292 | 73,665 | 5,621 | 0 |
| `db35d01d` | `agent-a1b1794efec644816` | specseal:framer | - | 0.20.0 | 2.1.292 | 73,655 | 108,596 | 70,707 |
| `db35d01d` | `agent-a1bc0d7d7f98098fe` | specseal:framer | - | 0.20.0 | 2.1.292 | 73,580 | 5,592 | 0 |
| `db35d01d` | `agent-a22a71c9104380da3` | specseal:framer | - | 0.20.0 | 2.1.292 | 73,635 | 74,877 | 69,261 |
| `db35d01d` | `agent-a394ea13eae250ba0` | specseal:framer | - | 0.20.0 | 2.1.292 | 73,643 | 5,593 | 0 |
| `db35d01d` | `agent-a45c8cb40895fd21f` | specseal:framer | - | 0.20.0 | 2.1.292 | 73,740 | 23,877 | 18,958 |
| `db35d01d` | `agent-a65225ee5a34442ec` | specseal:framer | - | 0.20.0 | 2.1.292 | 73,601 | 7,059 | 2,140 |
| `db35d01d` | `agent-a6acfab611c98787a` | specseal:framer | - | 0.20.0 | 2.1.292 | 73,600 | 13,530 | 7,937 |
| `db35d01d` | `agent-a9fc86d958e63c609` | specseal:framer | - | 0.20.0 | 2.1.292 | 73,637 | 4,919 | 0 |
| `db35d01d` | `agent-aa4176debde685669` | specseal:framer | - | 0.20.0 | 2.1.292 | 73,663 | 4,919 | 0 |
| `db35d01d` | `agent-ab93125c56255675f` | specseal:framer | - | 0.20.0 | 2.1.292 | 73,619 | 4,919 | 0 |
| `db35d01d` | `agent-abcf23b44e39a60f8` | specseal:framer | - | 0.20.0 | 2.1.292 | 80,804 | 145,577 | 12,947 |
| `db35d01d` | `agent-a1a52dbbc88822d66` | specseal:smith | - | 0.20.0 | 2.1.292 | 83,208 | 0 | 0 |
| `db35d01d` | `agent-ac212bd19e0cc8c17` | specseal:smith | - | 0.20.0 | 2.1.292 | 82,845 | 1,693 | 0 |
| `db35d01d` | `agent-aeaade423e84ea08d` | specseal:smith | - | 0.20.0 | 2.1.292 | 83,309 | 0 | 0 |
| `db35d01d` | `agent-af8f9dfdbf3f5fbb3` | specseal:smith | - | 0.20.0 | 2.1.292 | 83,113 | 18,901 | 0 |
| `db35d01d` | `agent-a14d80181c5d466e0` | specseal:warden | - | 0.20.0 | 2.1.292 | 75,060 | 0 | 0 |
| `db35d01d` | `agent-a313f298be3e4cdb7` | specseal:warden | - | 0.20.0 | 2.1.292 | 74,992 | 0 | 0 |
| `db35d01d` | `agent-a3efa5d647d6be2b0` | specseal:warden | - | 0.20.0 | 2.1.292 | 75,112 | 0 | 0 |
| `db35d01d` | `agent-a70f104558878efba` | specseal:warden | - | 0.20.0 | 2.1.292 | 75,004 | 34,644 | 2,727 |
| `db35d01d` | `agent-a781b5f8937cde34e` | specseal:warden | - | 0.20.0 | 2.1.292 | 74,942 | 0 | 0 |
| `db35d01d` | `agent-a8d3442981360a010` | specseal:warden | - | 0.20.0 | 2.1.292 | 74,923 | 0 | 0 |
| `db35d01d` | `agent-aa611ba3e30854803` | specseal:warden | - | 0.20.0 | 2.1.292 | 75,063 | 28,366 | 0 |
| `db35d01d` | `agent-ad20ea9c0dfca45bc` | specseal:warden | - | 0.20.0 | 2.1.292 | 74,988 | 59,487 | 13,503 |
| `db35d01d` | `agent-aeff6b827314d22b7` | specseal:warden | - | 0.20.0 | 2.1.292 | 75,018 | 17,753 | 0 |
| `db35d01d` | `agent-a1fbae1ecbb5584bd` | specseal:sealer | - | 0.20.0 | 2.1.292 | 57,803 | 0 | 0 |
| `db35d01d` | `agent-a250b9a3cf785f7b2` | specseal:sealer | - | 0.20.0 | 2.1.292 | 57,742 | 0 | 0 |
| `db35d01d` | `agent-a27de18cb7194d39a` | specseal:sealer | - | 0.20.0 | 2.1.292 | 57,799 | 0 | 0 |
| `db35d01d` | `agent-a538eeba7b30cc5b3` | specseal:sealer | - | 0.20.0 | 2.1.292 | 57,792 | 0 | 0 |
| `db35d01d` | `agent-ab4d0718cf0fe0470` | specseal:sealer | - | 0.20.0 | 2.1.292 | 57,819 | 0 | 0 |
| `fabe08e7` | `agent-aa2e19eab03cac311` | agentic:framer | #1038 | 0.27.1 | 2.1.316 | 45,489 | 0 | 0 |
| `fabe08e7` | `agent-addd8a88d9f97f3d3` | agentic:framer | #1221 | 0.27.1 | 2.1.316 | 45,209 | 0 | 0 |
| `fabe08e7` | `agent-a558e5e21c405a1d2` | agentic:framer | #1222 | 0.27.1 | 2.1.316 | 45,335 | 0 | 0 |
| `fabe08e7` | `agent-a402a322bff15c69b` | agentic:framer | #1223 | 0.27.1 | 2.1.316 | 45,185 | 0 | 0 |
| `fabe08e7` | `agent-ad4c1015c92272e00` | agentic:framer | #1229 | 0.27.1 | 2.1.316 | 45,218 | 0 | 0 |
| `fabe08e7` | `agent-a2e92f19573ddf777` | agentic:crafter | #1038 | 0.27.1 | 2.1.316 | 44,415 | 33,989 | 33,989 |
| `fabe08e7` | `agent-a92a477eefc668efe` | agentic:crafter | #1038 | 0.27.1 | 2.1.316 | 44,291 | 71,289 | 71,289 |
| `fabe08e7` | `agent-af7f67d6a639d894e` | agentic:crafter | #1038 | 0.27.1 | 2.1.316 | 44,509 | 39,448 | 33,989 |
| `fabe08e7` | `agent-a99ed23532f48819f` | agentic:crafter | #1221 | 0.27.1 | 2.1.316 | 44,368 | 0 | 0 |
| `fabe08e7` | `agent-af876f3d1dc917e2d` | agentic:crafter | #1221 | 0.27.1 | 2.1.316 | 44,059 | 33,989 | 33,989 |
| `fabe08e7` | `agent-a4313ae6247730ba9` | agentic:crafter | #1222 | 0.27.1 | 2.1.316 | 43,943 | 34,653 | 33,989 |
| `fabe08e7` | `agent-aeef3fbe075f90ff0` | agentic:crafter | #1222 | 0.27.1 | 2.1.316 | 44,405 | 1,976 | 0 |
| `fabe08e7` | `agent-a81542fdb852ddfad` | agentic:crafter | #1223 | 0.27.1 | 2.1.316 | 44,219 | 71,253 | 67,978 |
| `fabe08e7` | `agent-a114548fa5e21fbd5` | agentic:crafter | #1229 | 0.27.1 | 2.1.316 | 44,342 | 99,885 | 33,989 |
| `fabe08e7` | `agent-af7b4d2c84875d7e1` | agentic:proofer | #1038 | 0.27.1 | 2.1.316 | 44,032 | 283,960 | 0 |
| `fabe08e7` | `agent-ad5312929c3f3940f` | agentic:proofer | #1221 | 0.27.1 | 2.1.316 | 43,882 | 0 | 0 |
| `fabe08e7` | `agent-a3d8e0c1c353e505f` | agentic:proofer | #1222 | 0.27.1 | 2.1.316 | 44,050 | 606 | 606 |
| `fabe08e7` | `agent-a8032925ced1e9bdc` | agentic:proofer | #1222 | 0.27.1 | 2.1.316 | 43,808 | 0 | 0 |
| `fabe08e7` | `agent-ab14f1c65d4d5dc4a` | agentic:proofer | #1222 | 0.27.1 | 2.1.316 | 44,018 | 0 | 0 |
| `fabe08e7` | `agent-a0c77518212ca8840` | agentic:proofer | #1223 | 0.27.1 | 2.1.316 | 43,782 | 0 | 0 |
| `fabe08e7` | `agent-a312608390f14cab3` | agentic:proofer | #1223 | 0.27.1 | 2.1.316 | 43,797 | 16,306 | 0 |
| `fabe08e7` | `agent-a909dce2470e57c12` | agentic:proofer | #1223 | 0.27.1 | 2.1.316 | 43,637 | 0 | 0 |
| `fabe08e7` | `agent-a92677279cea57905` | agentic:proofer | #1223 | 0.27.1 | 2.1.316 | 43,670 | 0 | 0 |
| `fabe08e7` | `agent-a1afa03e39c353aa8` | agentic:proofer | #1229 | 0.27.1 | 2.1.316 | 44,231 | 0 | 0 |
| `fabe08e7` | `agent-a94bb729f78e3d9f7` | agentic:proofer | #1229 | 0.27.1 | 2.1.316 | 43,870 | 0 | 0 |
| `fabe08e7` | `agent-a9b5ca5a81b345a9e` | agentic:proofer | #1229 | 0.27.1 | 2.1.316 | 43,945 | 0 | 0 |
| `fabe08e7` | `agent-a81b6f430344fe056` | agentic:sealer | #1038 | 0.27.1 | 2.1.316 | 44,203 | 0 | 0 |
| `fabe08e7` | `agent-a396728162f49dd6f` | agentic:sealer | #1221 | 0.27.1 | 2.1.316 | 43,726 | 746 | 0 |
| `fabe08e7` | `agent-aa9a1042fcc13ec4f` | agentic:sealer | #1221 | 0.27.1 | 2.1.316 | 43,868 | 0 | 0 |
| `fabe08e7` | `agent-ad97c27db226d57fd` | agentic:sealer | #1222 | 0.27.1 | 2.1.316 | 43,915 | 0 | 0 |
| `fabe08e7` | `agent-aa9077e9ec4fee5ff` | agentic:sealer | #1223 | 0.27.1 | 2.1.316 | 43,867 | 0 | 0 |
| `fabe08e7` | `agent-a90e77289b7479d90` | agentic:sealer | #1229 | 0.27.1 | 2.1.316 | 44,026 | 0 | 0 |

### Where the prose before does not reproduce

The agents of both samples open most prose through `Bash` (`cat`, `sed`, `git show`), not through `Read`, so readings (a) and (b) see a small part of it. `search.py` tried six wider readings over the before segments at 2026-11-01T11:00:45Z, and none gives the body's three figures together (executed):

| Reading, median per kind | framer | smith | warden | sealer |
|---|---|---|---|---|
| Body | 310,350 | 296,676 | 134,716 | no figure |
| every tool result | 312,852 | 337,790 | 266,378 | 7,493 |
| every `Read` result | 58,964 | 84,371 | 92,939 | 0 |
| every `Bash` result | 263,474 | 251,446 | 156,214 | 7,124 |
| every `Read` and `Bash` result | 311,350 | 335,817 | 265,018 | 7,124 |
| `Bash` results whose command names a `.md` file | 130,582 | 159,771 | 81,378 | 0 |
| (a), and the `Bash` results of the row above | 176,334 | 169,222 | 94,971 | 0 |

"Every tool result" gives the framer within 0.8 per cent and is 13.9 per cent over for the smith and 97.7 per cent over for the warden, so it is not the body's method. The last two rows decide by a command's words which file it opened, so they are a reading guessed from text and decide nothing. The same readings over the after segments, for phase 3's context only: every tool result gives framer 195,884, crafter 303,706, proofer 133,489 and sealer 185,672; the last row gives 98,726, 148,236, 68,942 and 47,364 (executed, `search.py --item`).

The body's sample is not on this machine. Its *Before* heading says the figures were read "on 0.21.x runs". Of the 16 sessions under the harness's two project directories for this repository that spawned a plugin agent, none names plugin 0.21.x, and `db35d01d` is the only one naming 0.20.x (executed: `survey.py`).

### The decisions, each with its grounds

1. **The first prefix's before is labelled not reproduced for all four kinds, with its percentage, and phase 3's comparison rests on the re-run.** Phase 1 labels a re-run `reproduced` only where it gives the body's figure, and these four records feed one table, so this phase keeps that one meaning. Three of the four are within 5 per cent of the body. Judged against: `frame/design.md` *Scope* item 6 and scenario S2, and `frame/plan.md` *Alternatives considered* A1, "the comparison rests on the re-run".
2. **Prose opened on demand reports readings (a) and (b) on both sides, and the body's figures are labelled not reproduced.** Neither median falls within 10 per cent of any of the three figures, and *Scope* item 7 states this outcome and what follows it. The wider readings above are a search for the body's method, recorded so that it is not run again; they are no measure of this work. Judged against: `frame/design.md` *Scope* item 7.
3. **Reading (b) places a path by the path itself.** A path counts where it lies past the plugin's installed root (`.../plugins/cache/<marketplace>/<plugin>/<version>/`), or from its first `agents/`, `skills/`, `docs/` or `templates/` component, or at a last component `CLAUDE.md` or `CONTRIBUTING.md`, with no `seal/`, `tests/` or `evals/` component above it. The harness's own files under `~/.claude/` never count. Every `.md` path both samples read was listed and checked against the rule, and every one it counts is a prose file of the repository or the plugin, such as `docs/the-record-layout.md`, `templates/sdd-plan.md` and `skills/implement/SKILL.md` (executed). Judged against: `frame/design.md` *Scope* item 7 (b), "whether in the repository or the plugin's installed copy".
4. **A segment is finished where its last assistant message calls `SubagentHandback`**, which every segment of both samples does. This phase's own segment and the other two of #947 are left out, as *Scope* item 1 says. Judged against: `frame/design.md` *Scope* item 1 and G10.

### What the next phase needs

- In 6 of the 8 kind and side cells, the median of (b) is 0 B. Phase 3 compares on (a) and (b) as *Scope* item 7 directs, and its row should say that both read only what an agent opens through `Read`.
- The first prefix moved under a harness change as well, from Claude Code 2.1.292 to 2.1.316. No `general-purpose` segment in `fabe08e7` gives the after side's harness floor, so the reading cannot separate the harness's share from the plugin's, as `frame/plan.md`'s failure scenario says.
- #1038's six segments were read before its merge, with #1257 open at `f8d1b8f6`. #1257 later merged at that head, so they are its whole run.

### Commands

Every command ran with the working directory at this worktree. `$PROJECT` is the harness's project directory for this repository's main checkout, and `$PROJECT_WT` the one for its worktrees directory. The probes are saved under their file names in one directory and run with `python3 -I`. `segments.py` takes this worktree as its first argument and imports `payload_meter` from it.

```sh
git fetch origin && git rev-parse origin/release/v0.27.2
git diff --stat 94b03636 origin/release/v0.27.2 -- . ':!seal/threads' ':!seal/follow-up.md'
git diff --stat origin/release/v0.27.2...HEAD -- . ':!seal/threads/1793528484-the-process-measured-on-0-27-2'
gh pr view 1257 --json state,headRefOid,mergedAt,mergeCommit
date -u +%FT%TZ; ls $PROJECT/fabe08e7*/subagents/*.jsonl | wc -l
python3 -I segments.py "$PWD" $PROJECT/db35d01d* specseal:framer specseal:smith specseal:warden specseal:sealer
python3 -I segments.py "$PWD" $PROJECT/fabe08e7* agentic:framer agentic:crafter agentic:proofer agentic:sealer --item 1221 --item 1222 --item 1223 --item 1229 --item 1038
python3 -I search.py $PROJECT/db35d01d* specseal:framer specseal:smith specseal:warden specseal:sealer
python3 -I search.py $PROJECT/fabe08e7* agentic:framer agentic:crafter agentic:proofer agentic:sealer --item 1221 --item 1222 --item 1223 --item 1229 --item 1038
python3 -I survey.py $PROJECT $PROJECT_WT
```

`segments.py`:

```python
"""First-turn prompt tokens and prose opened on demand, per segment of one
session's subagents/ directory. Read-only: it opens each agent-<id>.jsonl and
its .meta.json and writes nothing.

Usage: segments.py <checkout of this repository> <session directory> <kind>... [--item <n>...]
  <session directory> is <the harness's project directory>/<session id>
  <kind> is a meta.json agentType, such as agentic:crafter
  --item keeps a segment only where its spawn description names #<n>

Per segment it prints: the session's first eight hex digits, the agent file,
the kind, the work item named, the plugin version (the first
plugins/cache/<marketplace>/<plugin>/<version>/ the transcript names), the
Claude Code version(s) its rows record, the last tool its last assistant
message calls ("text" where it calls none), the first prefix
(payload_meter.first_prefix, the tree's reader), and four prose readings,
each the UTF-8 bytes of tool results returned for a Read call:
  a   every Read of a path ending .md, the tool result's text
  b   the same, restricted to agents/ skills/ docs/ templates/, CLAUDE.md and
      CONTRIBUTING.md, in a copy of this repository or the plugin's (relative())
  a'  as a, the file content the harness records (toolUseResult.file.content)
  b'  as b, the same content
"""
import json
import os
import re
import statistics
import sys

checkout, session, *rest = sys.argv[1:]
items, kinds = [], []
it = iter(rest)
for arg in it:
    if arg == "--item":
        items.append(next(it))
    else:
        kinds.append(arg)
sys.path.insert(0, os.path.join(checkout, "skills/verify/scripts"))
import payload_meter  # noqa: E402

helpers = payload_meter._session_cost()
PLUGIN = re.compile(r"/plugins/cache/[^/\s\"']+/[^/\s\"']+/(\d+\.\d+\.\d+)/")
PLUGIN_ROOT = re.compile(r"^.*/plugins/(?:cache/[^/]+/[^/]+/[^/]+|marketplaces/[^/]+)/")
HARNESS = os.path.expanduser("~/.claude/")
PROSE_DIRS = ("agents", "skills", "docs", "templates")
PROSE_FILES = ("CLAUDE.md", "CONTRIBUTING.md")
NOT_A_ROOT = {"seal", "tests", "evals"}


def rows(path):
    with open(path, encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if line.strip():
                try:
                    yield json.loads(line)
                except ValueError:
                    pass


def text_bytes(content):
    if isinstance(content, str):
        return len(content.encode())
    if isinstance(content, list):
        return sum(len(c.get("text", "").encode()) for c in content if isinstance(c, dict))
    return 0


def relative(path):
    """The path inside a copy of this repository: past the plugin's installed
    root, or from the first agents/ skills/ docs/ templates/ component (or a
    last component CLAUDE.md or CONTRIBUTING.md) with no seal/, tests/ or
    evals/ component above it. None for the harness's own files under
    ~/.claude/ and for anything else."""
    m = PLUGIN_ROOT.match(path)
    if m:
        return path[m.end():]
    if path.startswith(HARNESS):
        return None
    parts = path.split("/")
    for i, part in enumerate(parts):
        if part in NOT_A_ROOT:
            return None
        if (part in PROSE_DIRS and i < len(parts) - 1) or (part in PROSE_FILES and i == len(parts) - 1):
            return "/".join(parts[i:])
    return None


def prose(path):
    rel = relative(path)
    return rel is not None and (rel.split("/")[0] in PROSE_DIRS or rel in PROSE_FILES)


def segment(path):
    rs = list(rows(path))
    versions = sorted({r["version"] for r in rs if isinstance(r.get("version"), str)})
    with open(path, encoding="utf-8", errors="replace") as handle:
        m = PLUGIN.search(handle.read())
    reads, last = {}, None
    a = b = a2 = b2 = 0
    for r in rs:
        msg = r.get("message")
        if not isinstance(msg, dict) or not isinstance(msg.get("content"), list):
            continue
        if msg.get("role") == "assistant":
            tools = [c.get("name") for c in msg["content"] if isinstance(c, dict) and c.get("type") == "tool_use"]
            last = tools[-1] if tools else "text"
        for c in msg["content"]:
            if not isinstance(c, dict):
                continue
            if c.get("type") == "tool_use" and c.get("name") == "Read":
                reads[c.get("id")] = str((c.get("input") or {}).get("file_path") or "")
            elif c.get("type") == "tool_result" and c.get("tool_use_id") in reads:
                p = reads[c["tool_use_id"]]
                if not p.endswith(".md"):
                    continue
                n = text_bytes(c.get("content"))
                tur = r.get("toolUseResult")
                f = tur.get("file") if isinstance(tur, dict) else None
                n2 = len(str(f.get("content", "")).encode()) if isinstance(f, dict) else 0
                a, a2 = a + n, a2 + n2
                if prose(p):
                    b, b2 = b + n, b2 + n2
    return {
        "prefix": payload_meter.first_prefix(path, helpers),
        "plugin": m.group(1) if m else None,
        "cc": ",".join(versions),
        "last": last,
        "a": a, "b": b, "a2": a2, "b2": b2,
    }


sub = os.path.join(session, "subagents")
out = {}
for name in sorted(os.listdir(sub)):
    if not name.endswith(".meta.json"):
        continue
    meta = json.load(open(os.path.join(sub, name)))
    kind, desc = meta.get("agentType"), meta.get("description") or ""
    if kind not in kinds:
        continue
    named = [n for n in items if re.search(rf"#{n}\b", desc)]
    if items and not named:
        continue
    agent = name[: -len(".meta.json")]
    s = segment(os.path.join(sub, agent + ".jsonl"))
    out.setdefault(kind, []).append(s)
    print("\t".join(map(str, [os.path.basename(session)[:8], agent, kind, ",".join("#" + n for n in named) or "-",
                              s["plugin"], s["cc"], s["last"], s["prefix"], s["a"], s["b"], s["a2"], s["b2"]])))
for kind, ss in out.items():
    med = {k: statistics.median(x[k] for x in ss if x[k] is not None) for k in ("prefix", "a", "b", "a2", "b2")}
    print(f"median {kind} n={len(ss)}\t" + "\t".join(f"{k} {v:,.0f}" for k, v in med.items()))
```

`search.py`:

```python
"""Search for the reading behind the body's prose figures: per segment of one
session, the UTF-8 bytes of tool results under several candidate readings,
and the median per kind. Read-only.

Usage: search.py <session directory> <kind>... [--item <n>...]
  --item keeps a segment only where its spawn description names #<n>
"""
import json
import os
import re
import statistics
import sys

session, *rest = sys.argv[1:]
items, kinds = [], []
it = iter(rest)
for arg in it:
    if arg == "--item":
        items.append(next(it))
    else:
        kinds.append(arg)
MD_CMD = re.compile(r"\.md\b")


def text_bytes(content):
    if isinstance(content, str):
        return len(content.encode())
    if isinstance(content, list):
        return sum(len(c.get("text", "").encode()) for c in content if isinstance(c, dict))
    return 0


def readings(path):
    uses, out = {}, dict.fromkeys(
        ("all", "read", "read_md", "bash", "bash_md", "read_md+bash_md", "read+bash", "skill"), 0)
    for line in open(path, encoding="utf-8", errors="replace"):
        try:
            r = json.loads(line)
        except ValueError:
            continue
        m = r.get("message")
        if not isinstance(m, dict) or not isinstance(m.get("content"), list):
            continue
        for c in m["content"]:
            if not isinstance(c, dict):
                continue
            if c.get("type") == "tool_use":
                uses[c.get("id")] = (c.get("name"), c.get("input") or {})
            elif c.get("type") == "tool_result" and c.get("tool_use_id") in uses:
                name, inp = uses[c["tool_use_id"]]
                n = text_bytes(c.get("content"))
                out["all"] += n
                if name == "Read":
                    out["read"] += n
                    out["read+bash"] += n
                    if str(inp.get("file_path", "")).endswith(".md"):
                        out["read_md"] += n
                        out["read_md+bash_md"] += n
                elif name == "Bash":
                    out["bash"] += n
                    out["read+bash"] += n
                    if MD_CMD.search(str(inp.get("command", ""))):
                        out["bash_md"] += n
                        out["read_md+bash_md"] += n
                elif name == "Skill":
                    out["skill"] += n
    return out


sub = os.path.join(session, "subagents")
by = {}
for name in sorted(os.listdir(sub)):
    if name.endswith(".meta.json"):
        meta = json.load(open(os.path.join(sub, name)))
        kind, desc = meta.get("agentType"), meta.get("description") or ""
        if kind in kinds and (not items or any(re.search(rf"#{n}\b", desc) for n in items)):
            by.setdefault(kind, []).append(readings(os.path.join(sub, name[: -len(".meta.json")] + ".jsonl")))
for kind, rs in by.items():
    print(kind, len(rs), {k: int(statistics.median(r[k] for r in rs)) for k in rs[0]})
```

`survey.py`:

```python
"""Every session under one harness project directory that spawned a plugin
agent: the count of its segments by kind and by the plugin version each
transcript names first. Read-only.

Usage: survey.py <the harness's project directory>...
"""
import collections
import json
import os
import re
import sys

PLUGIN = re.compile(rb"/plugins/cache/[^/\s\"']+/[^/\s\"']+/(\d+\.\d+\.\d+)/")
for project in sys.argv[1:]:
    for session in sorted(os.listdir(project)):
        sub = os.path.join(project, session, "subagents")
        if not os.path.isdir(sub):
            continue
        counts = collections.Counter()
        for name in os.listdir(sub):
            if not name.endswith(".meta.json"):
                continue
            kind = json.load(open(os.path.join(sub, name))).get("agentType") or ""
            if ":" not in kind:
                continue
            with open(os.path.join(sub, name[: -len(".meta.json")] + ".jsonl"), "rb") as handle:
                m = PLUGIN.search(handle.read())
            counts[(kind, m.group(1).decode() if m else None)] += 1
        if counts:
            print(session[:8], dict(sorted(counts.items())))
```
