# Guarantee: 1793588973-pr-body-reads-a-details-tag-as-github-does

| Field | Value |
|---|---|
| Broad gate | 561cb8de6 against bf18be7d1 |

The base `release/v0.28.0` resolved through `release/v0.28.0@{upstream}` to `bf18be7d1` (executed). The gate's run commit `561cb8de6` resolves, is an ancestor of HEAD, and `git log --no-merges --name-only 561cb8de6..HEAD ^bf18be7d1` lists one commit, `8f40b3d52`, touching only `trail/gate.md` of this work item (executed). `seal pr-body <item> --body <the body file> --check` exited 0 with the installed plugin's `seal` and with the tree's `bin/seal` (executed). No `seal/parity.md` is in git (executed, `git ls-files`), so the verdict block holds no `original:` line.

## Claims re-run

Every run below was made in a `git clone --no-local` of the worktree at `8f40b3d52`, under the scratchpad, removed afterwards. `pr_body.py` and `tests/skills/test_pr_body.py` at `bf18be7d1` are byte-identical to `b3e74ca95`, the commit the phase record ran its red against (executed, `git diff --stat bf18be7d1 b3e74ca95` on those paths printed nothing).

| Claim | Source | Command | Result |
|---|---|---|---|
| The six new refused cases were seen red before the code changed, each `DID NOT RAISE Refused`, eight others passing | `trail/phases/phase-1.md:7` | `git checkout bf18be7d1 -- skills/code-review/scripts/pr_body.py`, then `bin/test tests/skills/test_pr_body.py -q -p no:xdist -k "copy_faithfully or code_span" -rf` | holds: exit 1, 6 failed, 8 passed; the six are the parameters for the sentence, the indented line, the upper-case line, the line with `open`, the self-closing line and the line ending in `<details`; each failure reads `DID NOT RAISE` |
| The code-span blanking removed alone turns the passing case red | `trail/phases/phase-1.md:19` | `bin/seal mutate skills/code-review/scripts/pr_body.py --replace 'CLOSER.SPAN.sub(" ", seen[rel][line - 1])' 'seen[rel][line - 1]' --tests "bin/test tests/skills/test_pr_body.py -q -p no:xdist -k code_span"` | holds: `red`, `test_accepts_a_details_tag_in_a_code_span` failed with `Refused` |
| The line-end arm removed alone turns the case for a line ending in `<details` red | `trail/phases/phase-1.md:18` | `bin/seal mutate ... --replace '(?=[\s/>]\|$)' '(?=[\s/>])' --tests "bin/test tests/skills/test_pr_body.py -q -p no:xdist -k copy_faithfully"` | holds: `red`, only the `said10` parameter failed, `DID NOT RAISE` |
| The case-insensitive flag removed alone turns the upper-case case red | `trail/phases/phase-1.md:13` | `bin/seal mutate ... --replace ', re.IGNORECASE)' ')' --tests "bin/test tests/skills/test_pr_body.py -q -p no:xdist -k copy_faithfully"` | holds: `red`, only the upper-case parameter failed |
| The module's cases pass at HEAD | `trail/rounds/round-2.md`, *Probes* | `bin/test tests/skills/test_pr_body.py -q -p no:xdist` | holds: exit 0, 31 passed |
| The reading refuses the further lines the frame's probe saw end or open the fold, and passes a code span | `frame/design.md:17` | `python -I -c` loading HEAD's `pr_body.py` and applying `TAG.search(CLOSER.SPAN.sub(" ", line))` to nine lines | holds: `</details >`, a list item, link text, `a <details> b` and a line ending in `</details` are matched; a single and a double backtick span, `<detailsx>` and a `summary` tag are not |
| Nothing of the three `## Removes` rows stands in the tree | `frame/design.md` `## Removes` | `git grep -n -E` for the equality arm `in (FOLD, FOLD_END)` and the three removed docstring phrases at HEAD, outside `seal/threads` | holds: no hit, exit 1 |
| The phase-boundary command passed 591 cases, and `seal layout --check`, `ruff check` and `ruff format --check` exited 0 | `trail/phases/phase-1.md:31` | not re-run | unverified as a phase claim; the broad run at `561cb8de6` answers the suite and the lint, and `trail/gate.md` holds that run |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Replace the equality test with a reading of `<details` or `</details`, any case, followed by whitespace, `/`, `>` or the line's end, outside a fence and a code span; six refused cases and one passing case; docstrings rewritten; no rule change | the issue's *Done when* (four lines, attributes, a code span excepted, a backticked `</details>` passing); the diff | none |
| the build | `TAG` at `pr_body.py:135` with `[^>]*>?` after the lookahead, applied at `:470`; the equality arm and its docstring text gone; seven guards each shown red | the design: the suffix matches whenever the lookahead does, so the refused set is the design's, as the phase record states; the tree, by the runs above | none |
| the last round | Round 2 confirms round 1's one `should` fixed at `662bca509` by the round's mutant alone, opens nothing | the tree: the `said10` parameter holds the whole refusal sentence (`tests/skills/test_pr_body.py:373-380`), and the line-end mutant above turns exactly that parameter red | none |
| the changelog | `seal pr-body` now refuses a copied line holding a `details` tag anywhere outside a code span, in any case; it names path, line and tag and says to write it in a code span; it reads characters, so a tag GitHub shows as text, in a table cell or an HTML comment, is refused too; exit codes and the `refused:` shape unchanged | the build; the docstring's *Limits* (`pr_body.py:48-53`); the issue | none |
| the orchestrator's part of the pull request body | `Closes #1218`; the old equality refusal and the four passing lines; the new reading and its repair; the framer kept the refusal on #1044's premise (`frame/plan.md` A3); round 1 judged the reading guesses no meaning; one `should` pinned and confirmed; the merge at `561cb8de6`; the broad run, 6242 passed and 12 skipped | the changelog, `frame/plan.md` A2 and A3, round 1's first confirmation, round 2, `trail/gate.md`, and the gate's output file, which prints `6242 passed, 12 skipped` | none. Its list of the orchestrator's commits names the routing, the round and gate records and the merge; whether the frame's commit `b3e74ca95` is the orchestrator's or the framer's the tree cannot tell, since every commit carries one author, and the sentence decides nothing the guarantee rests on |

```seal
target: 8f40b3d52 against bf18be7d1
Verdict: sealed
```
