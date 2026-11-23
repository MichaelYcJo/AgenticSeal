# Questions for the planner: 1795405728-lib-routing-splits-a-row-on-an-escaped-pipe

The judgments the issue left open that the tree answered, one line each:

- How the one splitter reads a row without its closing pipe: `frame/design.md` G8 and G11, and the first two rows of `frame/plan.md` *Alternatives considered*.
- Which markers the issue's "no `# exempt from splitlines` marker remains" covers: `frame/design.md` G13.
- Whether `passages.py`'s new fence reading makes the paste check name a new copy: `frame/design.md` G10.
- Whether a cell's edge whitespace follows cmark-gfm: `frame/design.md` G3.
- Which module holds the one splitter: the fourth row of `frame/plan.md` *Alternatives considered*.
- Whether `routing.md` is read through `gfm_table`: the fifth row of `frame/plan.md` *Alternatives considered*.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Once `tests/commonmark_oracle.py#hidden_text` answers for each CommonMark line, do `_starts_in_inline_html` and `_starts` in that file keep a caller? The answer depends on how phase 2 rewrites the cases that read the oracle, and no probe can read code not yet written | the work | A caller stays: the function stays, and its docstring names that caller. No caller stays: the function goes, as a row of `frame/design.md` `## Removes` already allows | The function goes where no caller stays, and phase 2's record names which went | answered 2026-11-23 by phase 2 at `f418c6af8`: no caller stays, and the two functions go with `_tokens`, `SENTINEL` and `SPACES`, which only `_starts_in_inline_html` read (`trail/phases/phase-2.md`) |
