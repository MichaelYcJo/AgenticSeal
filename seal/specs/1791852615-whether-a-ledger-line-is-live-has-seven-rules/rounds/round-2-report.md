# 1791852615 — round 2 report (warden)

The verifying round. Target SHA `65385bd1`, base `origin/release/v0.21.1`
(`321e9de1`). The target is the fix diff `9b5239c6..e224390f`, one commit.
Read in a `git clone --no-local` of the worktree at the target SHA. Round 1's
record and report were read first, for coordinates. Every verdict below is
re-derived here.

## How the findings relate

Round 1's three findings are closed. The fix to 🟡 1 wrote one new sentence,
and that sentence is false for one of the two kinds of row its own bullet
names.

1. 🟡 1, 🟡 2 and 🟡 3 are closed, each on grounds checked in this round.
2. The new sentence says a row below a comment opener nobody closed is "the
   one place" a line nobody wrote live declares something. A `routing.md`
   row is not read by `hooks/config.py#hidden_lines` at all. Its reader,
   `hooks/routing.py#shown`, hides nothing where the walk is unsure, so a
   routing row below a fence nobody closed also declares (🟡 6).
3. The same wrong attribution sits in the frame and in the changelog
   fragment (⬜ 7, ⬜ 8). One clause of the 🟡 2 fix, worded in round 1's own
   paste-ready text, says a renderer "shows" comment text (⬜ 9).

⬜ 4 and ⬜ 5 are carried open from round 1 and are not reported again.

## The answers — round 1's three findings

### 🟡 1 is closed — the excusing headline now names its exception

`docs/the-evidence-ledger.md:633` to `:635` now reads "is not taken on
doubt, except where a declaring reader keeps an older reading that took
it". The protection sentence at `:642` is scoped to "everywhere else". On the
shape round 1 named, a `seal/config.md` row below a comment opener nobody
closed, both sentences now hold: the table still pins `read` for that cell,
and the bullet says so. The bold run still carries `EXCUSES`, so the
statement test's `bullets()` still finds it (executed below).

What the fix wrote in place of the old sentence opens 🟡 6. That is a new
claim, not round 1's finding left open.

### 🟡 2 is closed — the three partings are stated and pinned

The holding bullet (`docs/the-evidence-ledger.md:625` to `:632`) now names
all three shapes on which the rider check parts from the checker. The table
module carries the two added shapes, "a fence inside a comment that closes"
and "a closed fence below a fence nobody closed". The overview's divergence
row says three shapes.

I measured all seven readers on both shapes again in this round, calling the
readers rather than reading the table (executed). Every cell matches the
table at `65385bd1`:

| Reader | fence inside a closed comment | closed fence below an unclosed fence |
|---|---|---|
| checker's `quoted_lines` | not read | read |
| `claim_lines` | not read | read |
| `anchored_rows` | read | read |
| rider check's `quoted_lines` | read | not read |
| `live_lines` | not read | not read |
| `hidden_lines` | not read | not read |
| `readable` | not read | not read |

So the five readers whose cells rest on round 1's measurement rather than a
mutation are right. Each answer is also the one its docstring states:
`claim_lines` takes a closed line-start comment as an aside and an unclosed
region as read, `anchored_rows` reads every line, and `live_lines`,
`hidden_lines` and `readable` hide comment text and closed fences. No new
`BY_BIAS` cell was needed. These ten cells were not seen red under a
mutation. The table compares each reader's answer for equality, so any
change to a reader on either shape turns its cell red.

The statement's line 615, "A fence nobody closed is a malformed file whose
lines are read", now stands beside the rider's third parting, which states
the one exception. That is consistent.

### 🟡 3 is closed — the four holding readers declare one direction

`skills/evidence-check/scripts/evidence_check.py:370` and `:5591` now read
`unknown refused`. They agree with the rider check's line
(`.github/scripts/rider_check.py:238`) and with `anchored_rows`
(`skills/settle/scripts/settle.py:590`). Each unit's consequence sentence
names a refusal. `docs/the-reader-registry.md:31` to `:35` defines `refused`
as the decision the value feeds refusing the input. A row read on doubt is
judged, and a malformed one ends at `BROKEN` or exit 2. The registry tests
passed at this SHA (the orchestrator's executed run).

W2's claim now says `refused` for the checker's two. `phases/phase-2.md:34`
still says `claim_lines` went in as `guess`/`passed`. That line records what
phase 2 did, and the overview's row records the change, so it is not a
finding.

### The nine re-stamped rows hold

The fix moved the hashes of `quoted_lines`, `claim_lines` and the statement's
section. The released rows anchored to those three are A4, P2-1, P2-3, P4-1,
P4-2 and R5 for the two units, and C2 for the section, found with
`git grep` over `seal/releases` and `seal/ledger.md`. Each has a `Re-read`
row in the fragment, and W2 and W3 carry the new hashes.

C2 belongs in the set although round 1 did not list it. Its anchor is the
section of `docs/the-evidence-ledger.md` the fix rewrote, so its hash moved.
Its claim, that no document under `docs/` is over the ceiling, still holds:
`bin/fold-check` lists 0 over 1000 lines, and the file is 708 lines
(executed). `bin/evidence-check --strict .` reports 0 drifted and 0 broken
(executed), so no moved anchor was missed.

## A new finding in what the fix wrote

### 🟡 6 — a `routing.md` row below a fence nobody closed declares, against the new "one place" sentence

The fix's sentence at `docs/the-evidence-ledger.md:642` reads: "That row is
the one place a line nobody wrote live declares something; everywhere else,
what this protects is that nothing is excused or declared by a line nobody
wrote live." The bullet's headline names "a `routing.md` row" among the
lines it covers, and it describes `hooks/config.py#hidden_lines` as the
reader that declares.

`hidden_lines` never reads a `routing.md`. Its callers are the config
reader's own walk (`hooks/config.py:176`, `:247`) and
`skills/verify/scripts/broad_gate.py#hidden_row_at`, which reads
`config_text`. A `routing.md` is read by `hooks/routing.py#table_rows`
through `hooks/routing.py#shown` (`hooks/routing.py:127` to `:149`). That
reader calls the walk directly. Where the walk is unsure, it keeps its own
reading from before #667, and that reading hid nothing. Its docstring says
so: "a fence or a `<` + `!--` nobody closed hides nothing".

My probe (executed) asked both readers about one routing row on four
shapes:

| Shape | `routing.py#table_rows` declares it | `config.py#hidden_lines` hides it |
|---|---|---|
| below a fence nobody closed | yes | yes |
| below a comment opener nobody closed | yes | no |
| inside a fence that closes | no | yes |
| a four-space indented code block | yes | no |

The first row contradicts the bullet twice: the statement says a row below a
fence nobody closed declares nothing, and that one shape is the only place a
hidden line declares. A session that parks a `Review` row inside an unclosed
fence, expecting the rule it read, finds the row declared and the commit
gate silent.

The same misattribution is in `hidden_lines`' own `Reads:` line
(`hooks/config.py:189`), "the lines of `seal/config.md` or a `routing.md`".
No caller hands it a `routing.md`.

The fix names the routing reader in the bullet and narrows the `Reads:` line
to what the unit is handed. It moves no reader's behaviour. The last row of
the probe table, an indented code block, is why the paste-ready text scopes
the protection to fences and comments: no reader of either kind models
indented code, so a universal "everywhere else" is not true there either.
`tests/test_the_hooks_hide_what_a_renderer_hides.py::test_the_routing_reader_never_leaves_both_readings`
already pins the routing reader's two readings.

## Notes on the paperwork and on one clause

### ⬜ 7 — the frame says `routing.py#shown` reads through `hidden_lines`

`seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/plan.md:58`
lists `routing.py#shown` among the readers that read `hidden_lines`
"through `unfenced`". It does not, as 🟡 6 shows. `spec.md:151` gives
`hidden_lines` "`seal/config.md` and `routing.md` lines" as its input. This
is where 🟡 6's attribution came from. Both are the frame's paperwork and
close at the run's end.

### ⬜ 8 — the changelog fragment says `hooks/config.py` is the one such reader

`seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/changelog.md:14`
says `hooks/config.py` "is the one reader of the second kind that still
reads a row below a comment opener nobody closed". The routing reader does
too (🟡 6's probe, second row). This fragment becomes release notes. A
wording that holds: "`hooks/config.py` and `hooks/routing.py` still read a
row below a comment opener nobody closed, because each keeps the reading it
gave before its walk was added, and the statement says so."

### ⬜ 9 — "a renderer shows as comment text"

`docs/the-evidence-ledger.md:631` says the rider reads a fence inside a
line-start comment that closes, "which a renderer shows as comment text". A
renderer shows nothing of an HTML comment. The behaviour stated is right,
and the rider's docstring says it correctly: such a fence line "is comment
text and opens nothing". The words came from round 1's own paste-ready fix.
"which a renderer reads as comment text, not as a fence" would hold.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 1's 🟡 1 is closed — the excusing headline names the declaring reader's exception, and the protection sentence is scoped away from the `seal/config.md` row below an unclosed comment opener | `docs/the-evidence-ledger.md:633` | confirmed | read: lines 633 to 646; executed: the statement test passes at `65385bd1`; the new sentence at `:642` opens 🟡 6 on a different row |
| 🟢 | round 1's 🟡 2 is closed — the three partings are stated, the two added shapes are in the table, and the overview says three | `docs/the-evidence-ledger.md:625` | confirmed | executed: all seven readers asked on both added shapes, every cell equal to the table; the five readers' cells resting on round 1's measurement are right and match their docstrings |
| 🟢 | round 1's 🟡 3 is closed — the four holding readers declare `unknown refused` | `skills/evidence-check/scripts/evidence_check.py:370` | confirmed | read: `:370`, `:5591`, `rider_check.py:238`, `settle.py:590` and `docs/the-reader-registry.md:31` to `:35`; W2 says `refused` |
| 🟢 | the nine re-stamped rows hold, C2 included, and no moved anchor was missed | `seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md` | confirmed | executed: `bin/evidence-check --strict .` 0 drifted, 0 broken; `bin/fold-check` 0 over the ceiling, which is C2's claim; `git grep` finds exactly A4, P2-1, P2-3, P4-1, P4-2, R5 and C2 anchored to the three moved anchors |
| 🟡 6 | the excusing bullet attributes `routing.md` rows to `hidden_lines` and calls a row below an unclosed comment opener the one place a hidden line declares; `routing.md` is read by `hooks/routing.py#shown`, which declares a row below a fence nobody closed; `hidden_lines`' `Reads:` line names `routing.md`, which no caller hands it | `docs/the-evidence-ledger.md:642` | open | executed: the probe, routing row below an unclosed fence declared by `table_rows` and hidden by `hidden_lines`; read: `hooks/routing.py:127` to `:149`, `hooks/config.py:176`, `:189`, `:247`, `broad_gate.py#hidden_row_at` |
| ⬜ 7 | the frame says `routing.py#shown` reads `hidden_lines` through `unfenced`, and gives `hidden_lines` `routing.md` lines as input | `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/plan.md:58` | open | read: `plan.md:58`, `spec.md:151`, `hooks/routing.py:127` to `:149` |
| ⬜ 8 | the changelog fragment says `hooks/config.py` is the one reader of its kind that reads a row below an unclosed comment opener; the routing reader does too | `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/changelog.md:14` | open | executed: 🟡 6's probe, second row |
| ⬜ 9 | the holding bullet says a renderer "shows" comment text; it shows none | `docs/the-evidence-ledger.md:631` | open | read: the bullet and the rider check's `quoted_lines` docstring; the behaviour stated is right |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`, `tests/test_docs_line_wrap.py` and `tests/test_a_folded_statement_names_what_enforces_it.py` with `-q` and `SPECSEAL_CASE_CEILING_S=600`, in the clone at `65385bd1` | exit 0, 145 passed |
| `bin/fold-check --root .` in the clone | exit 0: 186 statements in 19 documents, 0 over the 1000-line ceiling; `docs/the-evidence-ledger.md` is 708 lines |
| `bin/evidence-check --strict .` in the clone | exit 0: 8474 ok, 0 drifted, 0 broken, 0 malformed |
| `git diff --stat 321e9de1 HEAD -- seal/releases seal/ledger.md` in the clone | empty, exit 0 |
| one test_tmp probe module in the clone's `tests/`, run once through `bin/test`, then deleted: the seven readers through the table module's adapters on the two added shapes and on two indented-code shapes | the two added shapes match the table in every cell; on a four-space indented row after a blank line all seven read the row |
| one test_tmp probe module in the clone's `tests/`, run once through `bin/test`, then deleted: `hooks/routing.py#table_rows` and `hooks/config.py#hidden_lines` on one routing row in four shapes | below an unclosed fence: declared, hidden. Below an unclosed comment opener: declared, not hidden. Inside a closed fence: not declared, hidden. Four-space indented: declared, not hidden |
| the broad gate: full suite, repository lint, typecheck | not yet. It belongs to the sealer, once the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round 1, ⬜ 4 | `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:222` | carried open: the `BY_BIAS` label on `hidden_lines`' mid-line comment cell; W1's Notes cell still says four cells |
| round 1, ⬜ 5 | `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/overview.md:31` | carried open: the first `Not verified` row is answerable from the code |

## Paste-ready fixes

### 🟡 6

`docs/the-evidence-ledger.md`, replace lines 638 to 646, from
"`hooks/config.py#hidden_lines` keeps" to the end of the bullet:

```markdown
  `hooks/config.py#hidden_lines`, which reads `seal/config.md`, keeps,
  wherever its walk is unsure, the fence-only reading it gave before #667:
  a row below a fence nobody closed declares nothing, and a row below a
  comment opener nobody closed still declares, because that reading never
  hid one and work item 1790645290 was bound to miss no row the older
  reading saw. `hooks/routing.py#shown`, which reads a `routing.md`, keeps
  the reading it gave before #667 the same way, and that reading hid
  nothing: a row below a fence or a comment opener nobody closed still
  declares there. Those rows are the places a line nobody wrote live
  declares something; at every other fence or comment, what this protects
  is that nothing is excused or declared by a line nobody wrote live. The
  wrong answer is a fold reported as a deletion at exit 1, a fragment the
  sweep keeps, a hook that says nothing, or a gate that asks.
```

`hooks/config.py:189`:

```python
    Reads: guess — the lines of `seal/config.md`, through `hooks/blocks.py#walk`; unknown mixed
```

The `Reads:` line moves `hidden_lines`' hash, and the paragraph moves the
section's. Run `bin/evidence-check --reverify --checked <date> --into
seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md .`
for P3-1, C2 and W2. The statement test reads reader spellings only, so it
needs no change; `hooks/routing.py#shown` is named in prose and is not a
table row.

Needs a fix: yes — 🟡 6: the excusing bullet attributes `routing.md` rows to
`hidden_lines`, and its new "one place" sentence is false for a routing row
below a fence nobody closed.
Loses a record or crashes: no

The broad gate is not yet run. It belongs to the sealer, and it comes due
once a round leaves nothing open, which this one does not.

## Proof block

Files opened at `65385bd1` in the clone:

- `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/`:
  `rounds/round-1.md`, `rounds/round-1-report.md`, `changelog.md`,
  `routing.md`, `plan.md` lines 50 to 66, `spec.md` lines 50 to 62 and 146
  to 152, the grep hits in `overview.md`, `questions.md` and
  `phases/phase-2.md`
- `seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md`,
  through the fix diff and the grep hits
- `docs/the-evidence-ledger.md` lines 600 to 660;
  `docs/the-reader-registry.md` lines 26 to 42
- `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`, the
  whole module
- `skills/evidence-check/scripts/evidence_check.py` `quoted_lines` and
  `claim_lines`
- `.github/scripts/rider_check.py` lines 225 to 300
- `hooks/config.py` lines 160 to 246 and the `CONFIG_ROW` pattern;
  `hooks/routing.py` lines 120 to 182
- `.github/scripts/fold_ledger.py#live_markers` and `MARKER_LINE_RE`
- `skills/verify/scripts/broad_gate.py` lines 965 to 985
- `tests/test_the_hooks_hide_what_a_renderer_hides.py`, the test names
- `bin/test`; `tests/conftest.py#load_hook_module`
