# Phase 1: 1793163944-the-issues-were-filed-against-the-old-tree

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | |

## What this phase was asked

File F1, F2 and F3 of `frame/design.md` *Filed as new issues* into
`release: 0.24.0` of `MichaelYcJo/AgenticSeal`, each with the title the
frame gives and a body holding every evidence line of its section, and record
the numbers they were filed under. Every act is on GitHub; no tree file
outside this work item's directory changes. Body files go to a scratch
directory outside the tree and are removed when the phase closes.

## What this phase found

**The numbers.** Each issue was filed with `gh issue create --repo
MichaelYcJo/AgenticSeal --milestone "release: 0.24.0" --title <title>
--body-file <file>`, its exit code read directly (executed).

| Finding | Issue | Exit code | createdAt |
|---|---|---|---|
| F1 | #1109 | 0 | 2026-10-28T05:29:34Z |
| F2 | #1110 | 0 | 2026-10-28T05:29:42Z |
| F3 | #1111 | 0 | 2026-10-28T05:29:48Z |

Phases 2 and 4 write these numbers where the frame writes `F1`, `F2` and
`F3`.

**S4 read back (executed).** `gh issue view <N> --json
title,milestone,state` reads each issue open in `release: 0.24.0` under the
frame's title, and each body read back with `gh issue view <N> --json body`
equals the file sent (`diff` exit 0, after the newline `--jq` appends).

**The evidence was opened again before it was filed (executed at the tree of
`c1b79d40`, which differs from `0b75346f` only inside this work item's
directory).** Three figures differ from the frame's, and the issues carry the
re-measured ones with their commands:

- F2, `docs/`: 18 lines hold the word `spec` or `specs`, where the frame
  wrote 17. The command is the frame's, `git grep -h -i -w -E 'specs?'`
  outside the Korean editions with lines naming `docs/worktree-guard-spec.md`
  dropped. The 18 include `specs/` in a path (`docs/one-root-by-lifetime.md:23`,
  `:26`) and the *Reference specs* heading (`:25`), and the body says so. The
  other seven figures match the frame.
- F3, the assert count: the frame gives no regular expression for "asserts
  shaped `assert "<25 or more characters>" in`". The one this phase ran,
  `grep -h -E 'assert \(?\s*"[^"]{25,}"\s*\)?\s+in\b' -r tests/<dir>`, counts
  `tests/text` 182, `tests/behaviour` 308, `tests/skills` 224, `tests/github`
  57, `tests/hooks` 31, `tests/evals` 13, where the frame wrote 193, 340, 270,
  67, 36 and 15. The body states the command and keeps the frame's caveat that
  the figure bounds the class from above.
- F3, `PINS` stands at `tests/text/test_the_agent_contract_holds_the_universal_rules.py:38-65`,
  not `:40-65`; and the two sentences `tests/text/test_broad_gate_rule.py`
  pins at `:54-55` are `skills/verify/orchestration.md`'s, which the body
  names.

The other evidence lines held as the frame states them: the six `detracer`
sites and `ab14194b` (`git log -S detracer`); `tests/censuses.py:984-1030`
matching the old names as whole words; the `\ncrafter` and `redesign`
results; `seal/process/0.23.0.md` row 2; the F2 examples at `agents/framer.md:55`,
`:150`, `agents/tracer.md:31`, `:59`, `agents/sealer.md:84`,
`skills/settle/SKILL.md:17-20`; 16 of 20 `check:` lines naming the contract
module.

**Old-form hits in the new bodies, each judged.** The search of `plan.md`
*Technical context* finds:

- #1109, `scribe` twice: the old name is the issue's subject, the substitution
  that produced `detracer` and the census pattern that matches it. History the
  issue exists to state.
- #1110, `spec.md` and `overview.md` as the names the rename retired, and
  `docs/worktree-guard-spec.md`, a current path whose name ends in
  `spec.md`. Both are the issue's subject.
- #1111: no hit.

**The title of F2 stays the frame's.** It names the template's title
"Overview", which is the issue's own finding.

The three body files were written to the crafter's scratch directory outside
the tree as `f1.md`, `f2.md` and `f3.md`, and removed by those paths when
this phase closed.
