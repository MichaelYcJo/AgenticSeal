# Review round 1: 1793922918-a-keyword-inside-a-comment-reads-as-a-claim

```seal
target: 3db19c6d against release/v0.32.6
```

The round read the range `063e0678..3db19c6d` in a `git clone --no-local` of the branch at `3db19c6d`. It read the frame, `gaps.md`, `trail/phases/phase-1.md` and `changelog.md` whole. No earlier round exists, so no fact was carried. Every coordinate below was opened this round.

The axes walked were inputs (body shapes), exclusions and boundaries (the two arms of `COMMENT` and the line-start condition), deliberate non-exclusions (the four-space indented block and #1404's shape), response shape (the length-preserving blank in R26), error paths (the refusals of `seal pr-body`), and security (crafted bodies against the regex's cost). Two more axes are this change's own. One is the reach of each reader: which of the six readers the change moves. The other is the masking's direction: whether every shape it reads differently closes fewer, as the frame's grounds require.

## Findings

### 1. `seal pr-body` now copies a record line that begins with a `<!--` that never closes, which it refused before this branch when the line held a keyword or a `details` tag

```seal
severity: should
location: `skills/code-review/scripts/pr_body.py:629-648`, `skills/code-review/scripts/pr_body.py:40-50`, `tests/skills/test_pr_body.py:395-468`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/gaps.md:12`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/design.md:49`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/design.md:72`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/plan.md:83-85`
evidence: executed `bin/test tests/skills/test_tmp_round1_probe.py -s -q -p no:xdist -p no:cacheprovider` (a probe, deleted); read `skills/code-review/scripts/pr_body.py:582-596`, `skills/code-review/scripts/pr_body.py:638`, and `skills/code-review/scripts/pr_body.py:631` at `3cdf510d`, whose code files equal the base's
```

Why it matters: the frame's *Scope*, Out, at `frame/design.md:49`, and `gaps.md:12` *Not done* both claim that this branch did not cause the defect. They describe a copied line that begins with an unclosed `<!--`, after which GitHub hides the rest of the body (#1405). For the lines that hold a closing keyword or a `details` tag, the claim is false. At `063e0678`, `keywords_in("<!-- Closes #5")` returned `['5']`, so `_claims` refused the line at `pr_body.py:595`. A line `<!-- <details>` was refused by the tag reading over `CLOSER.SPAN`. At `3db19c6d`, `COMMENT`'s second arm masks both lines to their end. The probe composed a body from each of `<!-- Closes #5`, `<!-- <details>` and `- <!-- Closes #5` as a copied `changelog.md` line, and `compose` returned each line in the body with no refusal. On GitHub, everything below such a line is hidden: the rest of the records' copy, and the fold's end `</details>`. So the branch turned a refusal into a pass for a body that GitHub breaks. The release would ship a tool that writes a broken pull request body without a word. The line was refused before for the wrong reason, a keyword that would close an issue. The right refusal names the opener, and one condition covers the whole class: lines with no keyword, which no reader refused before, as well.

The fix reads the closer's own `COMMENT` on the copied line, so the line-start test keeps one definition. Its first arm matching at the line's start is a comment that closes on the line, and GitHub ends that HTML block on the same line, so that line stays accepted. The precondition is the one `_composed` already has: `seen[rel]` holds `readable` lines, where a fenced line is blank. In `_composed`, between the `HEADING` branch and the tag branch:

```python
        elif (opened := CLOSER.COMMENT.match(seen[rel][line - 1])) and (
            "-->" not in opened.group()
        ):
            causes.append(
                (
                    rel,
                    line,
                    "begins with a `<!--` that no `-->` closes, and GitHub hides "
                    "every line below such a line, the copy's other lines and "
                    f"the fold's end `{FOLD_END}` among them; write it in a code span",
                )
            )
```

The snippet does not reach every statement of the fact, and the fix pass owes the rest, as contract rule 14 asks for a new refusal text:

- Rows in `tests/skills/test_pr_body.py#test_refuses_a_record_it_cannot_copy_faithfully` for `CHANGELOG + "<!-- Closes #5\n"` and `CHANGELOG + "<!-- note\n"`, each at line 3, with the `said` text naming the opener. Each row is shown red against `3db19c6d`, and its docstring names the shape.
- The module docstring at `pr_body.py:46-50`, which says such an opener "hides the rest of the line". It is refused now.
- `_composed`'s docstring at `pr_body.py:600-611`.
- The second sentence of `frame/design.md:72`, and the sentence "No exit code, message text or command-line interface changes" in the same bullet and in `changelog.md:3`.
- The Out bullet at `frame/design.md:49`.
- The phrase "or after a `<!--` that begins the line" at `frame/plan.md:84-85`.
- The first paragraph of `gaps.md` *Not done*, which this fix answers.

### 2. A comment masked to one space joins a keyword to a number GitHub reads apart, so the closer reads a claim it did not read before

```seal
severity: should
location: `.github/scripts/close_issues_on_release.py:154-160`, `.github/scripts/close_issues_on_release.py:173-176`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/design.md:73-77`
evidence: executed `bin/test tests/skills/test_tmp_round1_probe.py -s -q -p no:xdist -p no:cacheprovider` (a probe, deleted); read `.github/scripts/close_issues_on_release.py:154-176`
```

Why it matters: `keywords_in` collapses each `HIDDEN` match to one space (`close_issues_on_release.py:176`). A comment standing between a keyword and its number becomes the whitespace that `CLOSING`'s `\s+` needs. The probe read `Closes<!-- -->#4` and `Closes <!-- x -->#4` (in code spans here) at both commits. At `063e0678` each read `[]`. At `3db19c6d` each read `['4']`. GitHub renders the first as the text `Closes#4`, with no space between the keyword and the number, so it does not read a claim there. The release closer would now shut issue `#4`, which is the false record the frame's grounds guard against (`frame/design.md:15`, #266's direction). The comment block at `close_issues_on_release.py:154-156` says of its limits, "Each masks more than GitHub, so the closer closes fewer". This shape is the opposite case and is not listed. `frame/design.md:73` says the same of its list. The class is wider than the comment. A code span between a keyword and a number, such as ``Closes`x`#4``, already read `['4']` at `063e0678` through the same one-space collapse. So the limit is the collapse, not the comment. No body in the normal flow writes this shape. A limit sentence, the frame's own form for a shape it does not guard, is the proportionate repair.

At `close_issues_on_release.py:154-160`, the limits paragraph reads:

```python
# Limits, stated and not guarded. Each but the last masks more than GitHub,
# so the closer closes fewer and the completeness check refuses the release,
# which is loud. A `<!--` in the middle of a line with a `-->` further down is
# a comment up to that `-->`, across blank lines too, where GitHub's inline
# comment ends with its paragraph. A marker without its space, such as
# `-<!--`, counts as a line start. A comment GitHub's renderer refuses for its
# contents, such as one holding `--`, is masked anyway. And a fence, a comment
# or a span collapses to one space, so one standing between a keyword and its
# number, as in `Closes<!-- -->#4`, joins them into a claim GitHub does not
# read: in that one shape the closer closes more.
```

The fix pass owes the same bullet in `frame/design.md` *Data & interfaces*, `:73-77`, where the lead sentence "Each one masks more than GitHub" changes the same way.

## Confirmations

What matched: `COMMENT` at `.github/scripts/close_issues_on_release.py:162-165` is the pattern `frame/design.md:70` gives, character for character, with `re.M | re.S`. `HIDDEN` at `:167-170` joins `FENCE`, `COMMENT` and `SPAN` in that order. Neither `COMMENT` nor `SPAN` holds a capturing group, so `FENCE`'s `\1` still names its own group. `SPAN` takes on `re.M | re.S` inside `HIDDEN`. It holds no `.`, `^` or `$`, so its reading does not change (read).

What matched: the claim that `keywords_in` reads GitHub's set for the four measured bodies. `tests/github/test_close_issues_on_release.py:434-471` holds #1402's body as S1, #1403's and #1405's as S4, and #1404's as the row at `:484`. Each passed in the narrow run (executed, below).

What matched: R26 masks in one length-preserving pass at `.github/scripts/issue_claims_check.py:168`. Its import line `:92`, `__all__` at `:335` and the docstrings at `:38` and `:70-78` name the comment, as Scope 2 asks. The identity case asserts `check.HIDDEN is closer.HIDDEN` (`tests/github/test_issue_claims_check.py:405`). The source case refuses a restated `COMMENT`, `SPAN` or `HIDDEN` (`:416-423`) (read).

What matched: `pr_body.py:638` blanks the tag reading with `CLOSER.HIDDEN`. The keyword reading at `:595` goes through `keywords_in`, so the two are blanked one way, as `_composed`'s docstring says (read).

What matched: the claim that the frame's line ranges are right after the fold `3db19c6d`. At `3cdf510d`, the ranges hold the text the frame names: `issue_claims_check.py:70-76`, `tests/github/test_close_issues_on_release.py:441-445`, `skills/verify/scripts/unverified_check.py:92-93` and `skills/code-review/scripts/pr_body.py:631` (executed, `git show 3cdf510d:<path>`). The new citation at `unverified_check.py:92-93` names *A keyword claims the one number after it*, the heading at `docs/releasing/issues-and-milestones.md:270` (read).

What matched: the class of readers. A `git grep` for `FENCE`, `SPAN`, `keywords_in`, `HIDDEN` and `COMMENT` over `*.py` outside `tests/` (executed) lists the six readers `frame/design.md:19` names, and no other reader of a body's closing keyword. `publish_release_note.py:550` reads `SPAN` for a pull request title's `<` escaping and reads no keyword, so it stands outside the class (read). The two statements the phase record says it corrected outside the frame's list are at `label_merged_on_release_branch.py:19` and `tests/github/test_close_issues_on_release.py:385-393` (read). A `git grep` of the `*.md` files outside `seal/threads/` finds one statement HEAD contradicts, `docs/releasing/issues-and-milestones.md:292-303`. That statement is the `from` of the frame's rule change, which the settle writes (executed).

What matched: the departure at `b28430f2`. `bin/seal layout --pairs` (executed, exit 0) names two pairs in `tests/github/test_close_issues_on_release.py`, in `Test_comments_on` and `Test_close_issue`. The diff does not touch either class, and no pair names a case the diff adds or changes. Each new case was read against the cases of the function it covers. The closer's case and R26's `prose_only` case hold the comment, which no earlier case of their group holds. R27's case and the two accepting and refusing rows of `pr_body` hold S7 and S8 (read).

What matched: the `gaps.md` *Not done* second paragraph. `label_merged_on_release_branch.py` compiles neither `COMMENT` nor `HIDDEN`, and it reads every body through `closer.keywords_in` at `:216` (read).

The crafter's 14 `seal mutate` pairs, its 69-module run and its red runs at `3cdf510d` were read as claims and not re-run. The narrow run below covers the seven modules of the plan's phase row at `3db19c6d`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether GitHub reads the text after a `-->` on a line that begins with `<!--`, such as `<!-- x --> Closes #4` (in a code span here). CommonMark makes the whole line an HTML block. The closer reads the keyword, as at `063e0678`. S3's second row pins `['4']` for ``<!-- it's ` here --> Closes #4 and `x` ``, which the phase record says read `[]` at `3cdf510d`. `frame/plan.md:64`, row B2, says that A "reads it as GitHub does", and no measurement taken for #1181 holds this shape | `tests/github/test_close_issues_on_release.py:456`, `.github/scripts/close_issues_on_release.py:162-165` | the orchestrator, from a throwaway pull request into `main` read through `closingIssuesReferences`, as for #1402 to #1405 |
| The full suite, the repository-wide lint and the format check at `3db19c6d`: `unverified` | `seal/config.md`, the `Broad gate` row | the orchestrator, through its broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_close_issues_on_release.py tests/github/test_issue_claims_check.py tests/github/test_release_completeness_check.py tests/github/test_label_merged_on_release_branch.py tests/github/test_publish_release_note.py tests/skills/test_pr_body.py tests/behaviour/test_a_body_naming_two_issues_claims_one.py -q` at `3db19c6d` | 285 passed, exit 0 |
| `bin/test tests/skills/test_tmp_round1_probe.py -s -q -p no:xdist -p no:cacheprovider`: the closer at `063e0678` and at `3db19c6d`, loaded with `git show`, read six bodies, and `compose` at `3db19c6d` read three copied lines | `<!-- Closes #5` and `- <!-- Closes #5` read `['5']` at the base and `[]` at HEAD. `Closes<!-- -->#4` and `Closes <!-- x -->#4` read `[]` at the base and `['4']` at HEAD. `<!-- x --> Closes #4` reads `['4']` at both. `compose` copied `<!-- Closes #5`, `<!-- <details>` and `- <!-- Closes #5` with no refusal. The first version of the file stood at the clone's root, outside `tests/`, and failed at import before it read anything. It was deleted and written again under `tests/skills/`, and that run is the one reported here. Exit 0, deleted |
| `bin/test tests/github/test_tmp_round1_timing.py -s -q -p no:xdist -p no:cacheprovider`: `keywords_in` timed over three crafted bodies of about 65536 characters, GitHub's body limit | 16383 openers in the middle of one line, none closed: 3.1 s. 13000 line-start openers closed by one `-->` at the end: under 0.001 s. 9362 lines `a <!--`: 1.6 s. Each body finishes in seconds, so the Security axis holds no finding on cost. Exit 0, deleted |
| `bin/seal layout --pairs` at `3db19c6d` | exit 0. Two pairs are named in `tests/github/test_close_issues_on_release.py`, in classes the diff does not touch, and none among the new cases |
