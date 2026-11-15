# Review round 2: 1794530293-three-compatibility-paths-still-stand

```seal
target: aa6e93b7f, fixes c97122644..aa6e93b7f
```

This is the verifying round. The range holds the fix pass (`874b25a46`,
`305a9b838`, `acecc2e12`), the fold of round 1 finding 1 (`567f4d78e`), the
rewrite of two `pr.md` quotes (`69ed2e983`), the handoff's commit and removal
(`c8ab4897c`, `6437b3028`), one new row of `frame/plan.md` *Judgments of the
run* (`ac9d2cca3`), and the merge of `release/v0.38.1` (`aa6e93b7f`). The
merge is clean: against its first parent it brings
`skills/code-review/scripts/pr_wait.py` alone, as `05a92dbee` (#1547) left
it, and `git diff 05a92dbee aa6e93b7f -- skills/code-review/scripts/pr_wait.py`
prints nothing (executed). That help line is #1543's work item and was not
reviewed here. The base is now `release/v0.38.1` at `05a92dbee`, the merge
base of the target (executed: `git merge-base HEAD origin/release/v0.38.1`).
`seal/parity.json` is not declared, so no parity comparison was made.

The work item's records were read whole at `aa6e93b7f`: `routing.md`,
`frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`,
`changelog.md`, `pr.md`, `trail/phases/phase-1.md`, `trail/phases/phase-2.md`
and `trail/rounds/round-1.md`. No `pr.<lang>.md` stands, since both language
keys of `seal/config.json` read `English` (read). Carried from round 1 and
not established again: the base coordinates of the removed update steps
(`8f6acbb0e:skills/update/SKILL.md:39-43`, `:137-233`), that steps 4 and 4b
stand in every tag from v0.35.0 to v0.38.0, the callers of
`lib/tables.py`, and the six pin notices' three test lines. Each of those
was opened again where this round's verdict rests on it, and is named
there.

## Findings

### 1. The 0.38.1 Updating line says `/agentic:update` and `seal mode` dealt with every file it names, and no command ever dealt with the pact's two files

```seal
severity: should
location: `seal/threads/1794530293-three-compatibility-paths-still-stand/changelog.md:8`, `seal/threads/1794530293-three-compatibility-paths-still-stand/frame/design.md:107-114`
evidence: read `seal/threads/1794530293-three-compatibility-paths-still-stand/changelog.md:8`, `seal/threads/1794530293-three-compatibility-paths-still-stand/frame/design.md:107-114`, `8f6acbb0e:README.md:95-108`, `tests/lib/test_config.py:8`; executed `git grep -n -E '\| Signer|pact-paths\.md' 8f6acbb0e -- lib skills hooks agents templates .github ':!*.md'` and the same over `skills/update/SKILL.md`, `skills/implement/scripts` and `lib`, each printing nothing
regression: round-1#1
```

The unit is the second and third sentences of the *Updating* line at
`changelog.md:8`, which `874b25a46` wrote: "Until this release,
`/agentic:update` and `seal mode` dealt with these files only where they
ran, so reaching 0.37.0 or later took none of them out. Where one stands, do
by hand what the removed paths did." The folded *Scope* item 12 says the
same, "since until this release `/agentic:update` and `seal mode` dealt with
them only where they ran" (`frame/design.md:109-111`, from `567f4d78e`), and
the fix copied that sentence into the line, so the defect came from the
fold and the fix carried it into the release note.

"These files" are the files the line names next, six of them. Two are the
`| Signer |` table of a `seal/pact.md` and `~/.claude/agentic/pact-paths.md`.
No command dealt with either at the base. No code under `lib`, `skills`,
`hooks`, `agents`, `templates` or `.github` names a `| Signer |` table or
`pact-paths.md` at `8f6acbb0e` (executed). `tests/lib/test_config.py:8`
says the table "left with their reader" before this work. The README
paragraph this work removes said so in its own words: "Three files no
command converts are rewritten by hand", and it named `seal/parity.md`, the
pact's table and `pact-paths.md` (`8f6acbb0e:README.md:101-108`). The third
sentence, "do by hand what the removed paths did", was already in the line
round 1 read. It is wrong for the same two files, since no removed path
moved either of them.

Why it matters: this line is the one place a person is told what to do
after this release, and `/agentic:update` step 3 prints it. A person who ran
`/agentic:update` and `seal mode` on every machine and repository reads
that those commands dealt with these files where they ran. That person can
conclude that nothing of the list is left and skip the pact's two moves,
which no command ever made for them.

The fix keeps the opening sentence and the six acts as they read, and
replaces the two sentences between them:

```markdown
Updating: nothing to do where none of the files below stands, whatever release the plugin is on. Reaching 0.37.0 or later took none of them out. Until this release, `/agentic:update` and `seal mode` dealt with `seal/config.md`, `seal/parity.md`, the `CLAUDE.md` block and the launcher only where they ran, and no command ever converted the `| Signer |` table of a `seal/pact.md` or `~/.claude/agentic/pact-paths.md`. Where one stands, do by hand what follows. Write `seal/config.json` from `templates/setup/config.md`, with the rows of `seal/config.md` as its keys, and delete `seal/config.md`, since no command reads that file and every key reads as absent until then. Where `seal/parity.md` stands, write `seal/parity.json` from `templates/setup/parity.json` and delete `seal/parity.md`, since the parity arm reads no `parity.md`. Move the `| Signer |` table of a `seal/pact.md` into a `Pact signers` key of that repository's `seal/config.json`, and `~/.claude/agentic/pact-paths.md` into `~/.claude/agentic/pact-paths.json`. Delete the lines between `<!-- agentic:start -->` and `<!-- agentic:end -->` in `~/.claude/CLAUDE.md`, the markers included, which a release from 0.23.0 to 0.24.2 wrote. Remove from `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/settings.json` the `Stop` entry whose command runs `${CLAUDE_PLUGIN_DATA}/stamp.py`, then that file, which a release from 0.33.0 to 0.34.1 wrote.
```

*Scope* item 12 states the same fact, and the fix owes it too as a fold.
Its two sentences at `frame/design.md:107-114`, from "The *Updating* line
names who holds" to "each as one clause:", become:

```markdown
The *Updating* line names who holds what by the files themselves, not by
the release the plugin runs: the plugin version is one machine's, and
reaching 0.37.0 took none of these files out, since until this release
`/agentic:update` and `seal mode` dealt with the settings table, the
migration config, the block and the launcher only where they ran, and no
command dealt with the pact's table or `pact-paths.md`. It says that
nothing is to do where none of the files below stands, whatever release
the plugin is on, and that a person who holds one does each act below by
hand, each as one clause:
```

No other statement of the fact stands in the work item's records: the
other present-tense records name the removed paths' files without saying
which command dealt with them (read: `gaps.md:10`, `frame/plan.md:95-102`,
`frame/plan.md:121`).

### 2. `frame/plan.md` A3 says update steps 4 and 4b answer `nothing` for every person on 0.25.0 or later, and a machine on a later release can still hold the launcher

```seal
severity: should
location: `seal/threads/1794530293-three-compatibility-paths-still-stand/frame/plan.md:52`
evidence: read `seal/threads/1794530293-three-compatibility-paths-still-stand/frame/plan.md:52`, `seal/threads/1794530293-three-compatibility-paths-still-stand/frame/plan.md:95-100`, `seal/threads/1794530293-three-compatibility-paths-still-stand/frame/design.md:107-111`, `8f6acbb0e:skills/update/SKILL.md:39-43`, `8f6acbb0e:skills/update/SKILL.md:215-233`; executed `grep -n -o -E '.{0,90}\b0\.[0-9]+(\.[0-9x]+)?.{0,60}'` over the work item's present records, each line read
```

Why it matters: A3's failure scenario reads "runs two commands that answer
`nothing` for every person on 0.25.0 or later. The premise that keeps them
is a person on 0.24.2 or earlier, or on 0.33.0 to 0.34.1, who updates"
(`frame/plan.md:52`). That scopes the steps' readers by the plugin version,
which round 1 finding 1 and its fold set aside. The target contradicts it
in three places. *Operational impact* says a machine holding the block of
0.23.0 to 0.24.2 or the launcher of 0.33.0 to 0.34.1 "keeps it whatever
release the plugin has reached since, where `/agentic:update` or `seal
mode` never ran there" (`frame/plan.md:95-100`). *Scope* item 12 says
reaching 0.37.0 took none of these files out (`frame/design.md:109-111`).
The base step 2 ran step 4b on an already-current update for that very
reason, "because a person who reached this release by `claude plugin
update` alone may still hold the launcher" (`8f6acbb0e:skills/update/SKILL.md:39-43`).
On such a machine on 0.35.0, step 4b prints `launcher <path>`, not
`nothing` (`8f6acbb0e:skills/update/SKILL.md:226`, `:231`, read). The sentence
also contradicts itself: 0.33.0 to 0.34.1 is on 0.25.0 or later.

*Alternatives considered* carries no date, so A3 is read against the
target. A reader of the frame, the sealer or the settle among them, takes
from it the population the fold removed elsewhere. The fold in `567f4d78e`
rewrote the same version-scoped wording in *Technical context*, A1, A2, A6,
*Operational impact* and the title row, and left A3. The search that lists
every version a present record names (*Probes*) finds no other such
sentence. G3, R1 and R24, the paragraph at `frame/plan.md:41` and A2 state
the owner's judgment as the issue's comment gives it, and those are judged
under *Confirmations*.

The verdict of A3 stands. Its failure scenario becomes:

```markdown
| A3. Keep update steps 4 and 4b as steps that find nothing | Every `/agentic:update` run pays to read 97 lines of `skills/update/SKILL.md` and runs two commands that answer `nothing` on every machine that holds neither the block nor the launcher. The premise that keeps them is a machine that still holds the block a release from 0.23.0 to 0.24.2 wrote, or the launcher a release from 0.33.0 to 0.34.1 wrote, whatever release it runs now. The owner judged that no person on 0.36.x or earlier needs the path (G3), and the 0.38.1 note's *Updating* line tells a machine that still holds either file what to remove (`frame/design.md` *Scope* item 12) | Rejected, on the owner's decision |
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the *Updating* line no longer opens on a plugin version. It
reads "nothing to do where none of the files below stands, whatever release
the plugin is on" (`changelog.md:8`, read), and the folded *Scope* item 12
says the same (`frame/design.md:107-114`, read). The six acts after the
line's third sentence are byte for byte what round 1 read (executed: the
text after "removed paths did. " at `c97122644` and at the target,
compared with `[ "$a" = "$b" ]`, exit 0). The close's departure from the
paste-ready text holds: the paste-ready clause "where no command read a
setting on 0.37.x" named one case, and a repository where such a command
ran and refused the file still holds it too, since only `seal mode`
converted it (`8f6acbb0e:lib/config.py:139-141`, carried from round 1). The
`gaps.md` S7 row now states the folded S7 (`gaps.md:10`, `frame/design.md:171`,
read). Finding 1 above is a new defect in the sentence the fix added, and
it does not undo this close.

```seal
confirms: round-1#2
```
What holds: the comment above the import of `blocks` names no caller
(`lib/tables.py:23-25`, read), so it cannot fall out of step with
`.github/scripts/rules.py` or a later caller. `tests/lib/test_tables.py`
passes, 572 cases (executed). The close leaves the sentence at
`trail/phases/phase-1.md:43-44` as written. That holds:
`skills/implement/fix-pass.md` *The close blocks, last* says a fix pass
"writes no phase record" (read), the phase record states what phase 1
found at `3fb5b69cd`, and the close block names what that list missed.

What matched: G3, which the fix pass's crafter named as unfolded.
`frame/design.md:11` stands in the section dated to `dda87704c`, and its
second cell lists the issue's *Done when* items. Its last item, "the
release note's *Updating* line says what a person still on 0.36.x or
earlier does instead", is the issue's third *Done when* item word for word
(executed: `gh issue view 1500 --json body,comments`). The cell says what
the work must satisfy, so it was read against the target, and the target
does not contradict it. Every file the line names was written by a release
up to 0.36.0, and the line tells anyone who holds one what to do, whatever
release they run. So it says what a person still on 0.36.x or earlier
does, and it says it to every other holder as well. S7 and *Scope* item 12
add that the line ties none of this to the release; they widen the
audience G3 names and take no one out of it. G3 is no finding. R1's
"the owner judged no person on 0.36.x or earlier needs the path (G3)",
R24's grounds, `frame/plan.md:41` and A2 give the owner's judgment as the
comment of 2026-11-12T23:57:45Z states it: "The owner judged that no such
person needs that path now", where "such a person" is "a person still on
0.36.x or earlier" (executed, same command). `frame/plan.md:41` dates the
judgment 2026-11-13, and the comment itself says "On 2026-11-13 the owner
moved this issue", so the dates agree.

What matched: `pr.md`. Each of its seven quotes stands word for word at the
coordinate it names, with runs of whitespace collapsed (read:
`frame/plan.md:29-33`, `frame/plan.md:42-44`, `frame/design.md:20`,
`frame/questions.md:30-35`, `routing.md:20`, `frame/plan.md:120`). The two
`69ed2e983` rewrote quote the folded paragraph as it stands. The first quote's
"because no command that read a setting ran there while the plugin was on
0.37.x" gives one case where the line gives the cause. That is right for a
failure scenario, which tells one concrete story, and the target does not
contradict it.

What matched: the title row of *Judgments of the run* as the fold rewrote
it (`frame/plan.md:120`). With no file held, steps 4 and 4b printed
nothing at the base (`8f6acbb0e:skills/update/SKILL.md:210`, `:232`,
read), so nothing a person sees changes. The one exception is step 4b's
`no data directory` row, which told the person that the check could not
run. That message belonged to the removed step, so it is part of "the
removal itself" the row names, and the row's conclusion holds.

What matched: the new row of *Judgments of the run* (`frame/plan.md:122`).
`origin/release/v0.38.1` heads at `05a92dbee`, #1547's commit, and the
version move stays with this work item: `.claude-plugin/plugin.json` reads
`0.38.1` at the target (executed: `git log --oneline -3 05a92dbee`; read).

What matched: the chain check's six notices are the six round 1 weighed,
moved to `frame/design.md:192` and `:200` by the fold, for example "a test
pins text this operation takes out of `docs/layout/one-root-by-lifetime.md`:
`tests/block_shapes.py:59` holds "| Item | Value |", and the `to` does not".
The three lines they name, `tests/block_shapes.py:59` and
`tests/lib/test_tables.py:816` and `:847`, are still table headers in the
walker's fixtures (read). None of them pins a rule's wording or a fact a
reader acts on, so no notice is a finding.

Outside the fix diff, `tests/block_shapes.py:62` opens the `C1` to `C8`
shapes with the comment "the config reader". No shipped reader reads that
table now. The comment is read only by whoever next edits the shapes, and
it states none of the three paths, so this round opens no finding for it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check, the `Broad gate` key of `seal/config.json`, at the target. This round ran only `tests/lib/test_tables.py`, so the suite stays `unverified` | the whole tree | the orchestrator, at its broad run once the rounds settle |
| `skills/code-review/scripts/pr_wait.py`'s help line, which the merge brings from #1547 | `skills/code-review/scripts/pr_wait.py` | #1543's work item and its rounds |
| Whether the published v0.37.1 note keeps its date, which `frame/questions.md` assumes | GitHub release v0.37.1 | the owner |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/lib/test_tables.py` | exit 0, 572 passed |
| `git grep -n -E '\| Signer\|pact-paths\.md' 8f6acbb0e -- lib skills hooks agents templates .github ':!*.md'`, and the same over `skills/update/SKILL.md`, `skills/implement/scripts` and `lib` | nothing printed either time |
| `grep -n -o -E '.{0,90}\b0\.[0-9]+(\.[0-9x]+)?.{0,60}'` over `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` | every line naming a version, each read; only `frame/plan.md:52` scopes who holds a file by the release they run outside a statement of the owner's judgment |
| `gh issue view 1500 --repo MichaelYcJo/AgenticSeal --json body,comments` | the third *Done when* item and the owner's comment of 2026-11-12T23:57:45Z, as quoted under *Confirmations* |
| `git diff 05a92dbee aa6e93b7f -- skills/code-review/scripts/pr_wait.py` | nothing printed: the merge brings #1547's file unchanged |
| `skills/code-review/scripts/chain_check.py --baseline 05a92dbee --root <clone> --worktree`, before this record existed | exit 0. It printed the six pin notices quoted under *Confirmations*, said a verifying round is owed for round 1 finding 2 and for `305a9b838`, and named the absent gate record and guarantee |
