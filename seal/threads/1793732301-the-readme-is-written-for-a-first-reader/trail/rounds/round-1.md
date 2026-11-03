# Review round 1: 1793732301-the-readme-is-written-for-a-first-reader

```seal
target: c4ad189b5 against release/v0.31.0
```

The round read the branch against its base, 29182a206..c4ad189b5, in a
`git clone --no-local` at c4ad189b5. No earlier round exists, so no fact is
carried: every coordinate below was opened this round. The work item's
`frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`,
`changelog.md`, the three phase records and the issue with its five
comments were read whole. The axes were the frame's scenarios S1 to S9,
each fact the two pages state against its home, the cases the diff
repoints, contract rule 19's other statements of each fact the diff moved,
and the page as a first reader renders it.

## Findings

### 1. Neither edition shows its three install commands on a first screen, and the frame's S1 stopped measuring that

```seal
severity: should
location: `README.md:45-58`, `README.ko.md:46-61`, `seal/threads/1793732301-the-readme-is-written-for-a-first-reader/frame/design.md:64`
evidence: executed `gh api markdown -f mode=markdown -f text=README.md`, `Google Chrome --headless=new --window-size=1440,900 --dump-dom test_tmp_view.html`
```

Why it matters: the issue states the test of a draft as "that first
screen: a developer who reads only it knows what the plugin does, has seen
the owl and the workflow, and has the three install commands". The frame's
S1 replaced that measure with "reads to the end of `## Install`", read from
the text, and "No case reads a rendering" (`frame/design.md:64`). Read that
way the page passes, but the measure no longer asks where the commands
stand on a screen.

The round rendered each edition through GitHub's markdown API (mode
`markdown`, the one a repository README takes) and drew it in headless
Chrome. The page used `github-markdown-css` 5.5.1 and `mermaid` 10.9.1,
in a 1012-pixel container like GitHub's, with no GitHub header above the
article (`## Probes`). In a 1440 by 900 window, the bottom of the install
block stands at 1,169 pixels in `README.md` and at 1,157 in `README.ko.md`.
The first screen ends at the workflow chart, and `## Install` lies below
it. On GitHub the repository header, and on the repository's home page the
file list, push it lower still.

The commands also stand later than the frame's own outline puts them.
`frame/plan.md:16` lists `## Install` as "three commands, Python 3.12,
uninstall". `README.md:47-52` and `README.ko.md:48-55` instead put a
six-line requirement paragraph between the heading and the command block,
about 88 pixels at that width.

No viewport is named by the issue, so how much the first screen must hold
is the owner's call, and the fix below narrows the gap without closing it
at 900 pixels. Moving the third paragraph of the pitch, the three labels
(`README.md:27-30`, `README.ko.md:28-31`), below `## Install` would gain
about 88 pixels more. That move changes `frame/design.md` *Scope* 1, which
lists the labels among the first screen's items, so the fix pass owes that
item too if it takes it.

The fix, within the plan's outline: the command block comes first under
`## Install`, and the requirement paragraph follows it, unchanged. In
`README.md`:

~~~markdown
## Install

```bash
claude
> /plugin marketplace add MichaelYcJo/AgenticSeal
> /plugin install agentic@agenticseal
```

You need `git`, and Python 3.12 or newer answering to `python3` on your PATH.
The hooks are Python scripts, and `python3` is the command the plugin runs
them with. Run `python3 -V` before you install: macOS ships 3.9 as
`/usr/bin/python3`, and a version manager answers with whatever it was last
told. On Windows, where the official installer creates no `python3`, each
hook falls back to `py -3`.

That is the whole install. Nothing is written into your `CLAUDE.md`. The
auto-format hook uses `uv`, `uvx` or `ruff` where one is installed, and does
nothing where none is. To uninstall, run `/plugin uninstall agentic`.
~~~

In `README.ko.md` the same move: the `bash` block at lines 57-61 moves
above the paragraph at lines 48-55. The paragraph's words stay, since
"설치하기 전에 `python3 -V` 를 한 번 돌려 보세요" still reads true after the
block. The statements the fix also reaches are S1's *Verifiable how* cell
at `frame/design.md:64`, which should name the viewport the reading takes
(or say the owner sets it), and phase 2's and phase 3's records. Those
records stay as they are, and the fix pass names the move in its own
record.

```seal
verdict: fixed d64965d6f
answer: Built to the folded *Scope* item 1 rather than to the paste-ready fix alone. In both editions the install block now stands directly under the install heading and the requirement paragraph follows it unchanged; the paragraphs on why the parties are separate and on the claim labels moved below the install's uninstall paragraph, and the owl is drawn at 150 pixels instead of 180. The moved paragraph's first words changed, "That differs" to "This workflow differs" and "에이전트 하나에게 … 것과는 다릅니다" to "이 워크플로는 에이전트 하나에게 … 것과 다릅니다", because after the install its "That" would name the install. Measured as S1 states (executed: `gh api markdown -f mode=markdown`, `github-markdown-css` 5.5.1 and `mermaid` 10.9.1 in a 1012-pixel container, headless Chrome 1440 by 900, at d64965d6f): the install block's bottom stands at 785 pixels in `README.md` and 773 in `README.ko.md`, the owl's bottom at 182 and the chart at 513 to 594 and 489 to 582. The same harness read c4ad189b5 at 1,101 and 1,091 where this round read 1,169 and 1,157, so it sits 68 pixels higher than the round's; with that difference added the blocks end at 853 and 841, within 900 either way.
```

### 2. The import's two-root refusal sends the person to a README section that no longer holds the commands it promises

```seal
severity: should
location: `skills/implement/scripts/seal.py:1055-1062`, `tests/skills/test_seal.py:1311-1316`
evidence: read `skills/implement/scripts/seal.py:1055-1062`, `skills/implement/scripts/seal.py:2359-2366`, `README.md:154-168`
```

Why it matters: when both roots exist, `seal import` refuses and prints
"Move or remove one first; the plugin README's *Shared or local* section
has both commands." Before this branch, that section held the two by-hand
moves, so "both commands" named them. Now the section holds `seal mode
local` and `seal mode shared` (`README.md:157-162`) and sends the by-hand
moves to each root's `seal/README.md` (`README.md:166-168`). A person who
follows the message meets `seal mode` first. In this state, `seal mode`
refuses with `both_roots`, "Switching from here would leave the other where
nothing reads it. Move or remove one first."
(`skills/implement/scripts/seal.py:2359-2366`). The message sends the
person to a command that sends them back. That is a tool telling a person
something wrong, which is `should` under `skills/code-review/SKILL.md`
*The record*.

`gaps.md` *Not done* and `frame/plan.md` *Judgments of the run* row 2 claim
the message "is not false" and leave it because the frame excludes script
changes. That claim does not hold: the section the message names has
neither of the commands it says it has. The exclusion in `frame/design.md`
*Data & interfaces* is the frame's choice. The exclusion does not make the
printed sentence true, and contract rule 19 asks the change that moved the
fact to correct what stood on it.

The fix rewords the message to name where the by-hand moves now stand, and
pins it (contract rule 14):

```python
            "it. Move or remove one first; the `seal/README.md` in each root "
            "gives the two moves by hand, and `seal mode` refuses until one "
            "root is gone."
```

The fix's pin, in
`tests/skills/test_seal.py::Test_destination_root::test_refuses_two_roots_whatever_into_says`
(line 1311), goes after the existing
`startswith` assertion:

```python
        assert "the `seal/README.md` in each root gives the two moves by hand" in why
```

The fix also reaches `gaps.md` *Not done*, whose second paragraph goes, and
`frame/design.md` *Data & interfaces*, whose last bullet then names this
one script change. The fix pass sees the new assertion red against the
current message before it commits the reword. The docstring comments at
`skills/implement/scripts/seal.py:1758` and `:2499` ("the README's `mv` by
hand") stay true of `seal/README.md` and are not in this finding's reach.

```seal
verdict: fixed 7c1bb00fb
answer: The message is reworded in the fix pass's own words, not the paste-ready ones: read in the state that prints it, both roots present, the two by-hand moves in `seal/README.md` would move one root into the other (`mv` into an existing `seal/` nests it), so the message now says "Move or remove one first: keep the root that holds the records you want, copy across by hand what only the other holds, and delete the other. `seal mode` refuses while both exist, too." The pin in `test_refuses_two_roots_whatever_into_says` asserts both sentences and that no README is named; it ran red against the old message (three parametrisations failed) before the reword, and two `seal mutate` runs over the new sentences each read red after the commit; 24c035842 corrects the pin's comment, which named the by-hand moves as the README's rather than the ones it links. `gaps.md` *Not done* drops its paragraph on the message (9b44c80e5), and `changelog.md` gains a bullet for it.
```

### 3. A comment in the shrunken-corpus census still describes the paste check as the ratchet this branch removed

```seal
severity: should
location: `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:80-82`
evidence: executed `git grep -n -i -E 'ratchet|BASELINE|measured at|over_baseline' -- ':!seal/threads' ':!.test_durations'`
```

Why it matters: the comment over the paste check's corpus entry reads
"#730's ratchet. It judges what it finds and fails only on a count that
rose, so a file listed and not on disk can lower a count and never raise
one". After a734aa9ea the check names every pair that shares any run
(`tests/text/test_no_passage_is_pasted_into_a_second_file.py`
`shared_runs`), and no count is stored or compared. The comment is the
grounds for the entry's classification, so the next contributor who weighs
whether this reader should decline reads grounds that describe a check that
no longer exists. Contract rule 19 asks the same change to correct a
comment that stood on the old fact.

Phase 2's rule-19 search was `git grep -n -i readme` over the shipped
directories. It did not search `tests/` for the ratchet's own words, so it
could not list this comment. This round's search above is also a search on
words, and so a sample. It found this comment and the policy sentence
`docs/layout/the-record-layout.md:185-188`, which the design's `## Rule
changes` already carries.

The entry's decision stands: a missing file removes pairs and adds none,
so skipping the missing half is still safe in the same direction. The
words change:

```python
    # #730's paste check. It names every pair of the files it finds that
    # shares a run, so a file listed and not on disk removes pairs and adds
    # none; it skips the missing half and does not decline.
```

```seal
verdict: fixed 8cff4fa5a
answer: The comment now reads as the round's paste-ready text, word for word; the entry's value stays 1. A `git grep -i -E 'ratchet|BASELINE|measured at|over_baseline'` outside the records and `.test_durations` found no other statement of the ratchet but the policy sentence `docs/layout/the-record-layout.md:185-188`, which the design's `## Rule changes` carries to the settle.
```

## Confirmations

```seal
confirms: none
```
What matched: S2. The assertion added at
`tests/behaviour/test_chain_hooks_hardening.py:153-158` reads the paragraph
under `# AgenticSeal` with its line breaks folded. It requires a blank line
and nothing else between title and paragraph. `README.md:8-9`, folded, is
the `description` of `.claude-plugin/plugin.json` verbatim (read). The
module passed in the round's narrow run (executed).

```seal
confirms: none
```
What matched: S4 and S5. `BASELINE`, the *Why a ratchet* paragraph and the
two ratchet cases left
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`, and
`shared_runs` names every pair sharing a run (read). The module passed
against the new `README.md` (executed). The design's `from` at
`frame/design.md:88` is the sentence at
`docs/layout/the-record-layout.md:185-188` word for word (read).

```seal
confirms: none
```
What matched: S8. The command `assets/seals/README.md` gives, taken from
the file by `grep` and run under `uv run --isolated --no-project --with
resvg_py==0.5.0` over a deleted `owl-social.png`, exited 0. The redraw is
byte for byte the committed file (`git diff --quiet` exited 0), a 1280 by
640 RGBA PNG of 190,963 bytes (executed). `owl-social.svg` places
`owl.svg` by `<image href>` and copies none of its paths (read).

```seal
confirms: none
```
What matched: S3, S6 and S7. Twelve modules passed in one `bin/test -q` run
(438 cases, exit 0, executed): the six the diff changes, the outline case,
the line-wrap case, the stamp case, the cited-section case, the census
and the mode case. The repointed `switch_block` reads the two by-hand moves
from `templates/setup/seal-README.md:39-44`, the spans after "From local to
shared:" and "From shared to local:" (read). Each hook row's *Fires* cell
matches the event and matcher in `hooks/hooks.json` (read). Every `docs/`,
`skills/`, `agents/`, `hooks/`, `templates/` and `assets/` path either
edition cites in backticks exists in the tree (executed: a loop over the
backticked spans with `test -e`).

```seal
confirms: none
```
What matched: S9 and K4. The round read `README.ko.md` against `README.md`
section by section and found the same facts in the same order, with the
same homes. The Korean edition links the two Korean editions that exist.
The version-check row at `README.ko.md:293` carries
"`/agentic:update` 와 릴리스를 불러오는 두 방법" (read). Phase 3's account of
the comparison holds as far as this reading reached.

```seal
confirms: none
```
What matched: the stale facts *Removes* names. The page describes no
recurrence check (issue comment 5) and states no round count as a cap.
`docs/running/the-run.md` *The run* is linked for the bound
(`README.md:226-228`). The routing answers at `README.md:107-112` match
`skills/implement/orchestration.md` *Question 1* and *Question 2*, and
`seal import --help` names the two flags `README.md:191-193` sends a reader
to (executed). The orchestrator's edit of `trail/phases/phase-2.md:43-44`
replaces the host's name with a description and changes no claim of the
record (read).

```seal
confirms: none
```
What matched: `gaps.md` *Not done*'s third paragraph. The case
`tests/text/test_the_mode_is_a_row_and_a_command.py::test_both_readmes_name_the_command_before_the_by_hand_lines`
keeps its name, and its assertions hold the fact the frame keeps: the first
`bash` block of the section holds `seal mode local` and `seal mode shared`,
and no `mv ` (read: lines 22-37). The name reads as the case's history, and
no reader is led to act on it, so it is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| How GitHub itself renders both pages. The round's render used `mermaid` 10.9.1 and `github-markdown-css` 5.5.1, not GitHub's viewer. In it, the chart's `viewBox` was 1,698 pixels wide in English and 1,473 in Korean, drawn into 914. That puts its 16-pixel labels at about 8.6 and 9.9 pixels. Two-line labels (`framer<br/>design and plan`) measured 1,325 wide, about 11 pixels. Whether the chart reads at GitHub's narrower column is a look at the branch's page | `README.md:32-43`, `README.ko.md:33-44` | the repository owner, on the branch's page on GitHub, with `gaps.md` *Not verified* rows 2 and 3 |
| Which viewport the issue's "first screen" means, and so whether finding 1's fix is enough or the pitch's third paragraph moves too | `frame/design.md:64` | the repository owner |
| Whether the plugin directory renders the relative owl path and the `mermaid` block | `frame/questions.md` Q2 | the repository owner, after the release (Q2's default) |
| Whether the social preview carries the name, and the field colour | `frame/questions.md` Q1 | the repository owner |
| The broad gate: the full suite, the lint and the typecheck at the commit the pull request carries. Phase 3's suite stands labelled `unverified` only in the sense contract rule 2 gives it: its narrow set is `executed` and the broad run is owed. That label is honest | `seal/config.md` `Broad gate` row | the orchestrator, after the rounds settle; the sealer's spawn follows it |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over twelve modules (the six changed, the outline, line-wrap, stamp, cited-section, census and mode modules) | exit 0, 438 passed |
| `gh api markdown -f mode=markdown -f text=<each edition>`, then headless Chrome at 1440 by 900 and 1280 by 900 over a page wrapping the fragment with `github-markdown-css` 5.5.1 and `mermaid` 10.9.1, served from a scratch directory on 127.0.0.1 | install block's bottom at 1,169 pixels (English) and 1,157 (Korean); chart top 785 and 761, rendered 914 wide and 81 and 93 tall; at both window widths, since the container caps at 1012 |
| the same page with the chart's labels split over two lines | `viewBox` 1,325 wide; install block's bottom at 1,218 |
| `uv run --isolated --no-project --with resvg_py==0.5.0 sh -c` over the command `assets/seals/README.md` gives, after deleting `owl-social.png` in the clone | exit 0; `git diff --quiet HEAD -- assets/seals/owl-social.png` exit 0; `file` 1280 x 640 RGBA; 190,963 bytes |
| `bin/seal import --help`, `bin/seal export --help` | the two flags `--allow-other-repo` and `--allow-unreadable-remote`; export's default name built at `skills/implement/scripts/seal.py:573` |
| a loop over every backticked tree path in both editions with `test -e` | no path missing |
