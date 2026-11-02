# Questions for the planner: 1793599990-each-result-is-a-badge

The judgments the issue left to the frame, each answered from the tree or by
a probe. Their grounds are where each line points, and are not restated here.

- The reader without images: each badge's `alt` text is its label and value.
  `frame/design.md` *Grounding*, the #1153 row; *Scope* item 1; S3.
- The external service, and what a reader sees when it or the proxy fails:
  `frame/design.md` *Grounding*, the `skills/core/SKILL.md` row and the three
  probe rows on the Shields host and GitHub's image proxy; `plan.md`
  *Technical context*, its failure scenario.
- Escaping: `frame/design.md` *Grounding*, the probe row on the `/badge/`
  path; *Scope* item 2; `plan.md` A1 and A2.
- The cell without the image: the same badges. `frame/design.md`
  *Grounding*, the #1204 row; `plan.md` A12.
- The pull request body: out of scope, since it renders no results cell.
  `frame/design.md` *Grounding*, the `pr_body.py#MARK` row.
- The re-run rule: unchanged, since `header` is unchanged. `frame/design.md`
  *Grounding*, the #718 row; `plan.md` A9; S7.
- The labels, which badges share a line, the colours and the style:
  `frame/design.md` *Data & interfaces*; *Grounding*, the icon probe row;
  `plan.md` A7, A8, A11 and A13.
- The census of real domains: the badge host joins `ALLOWED_DOMAINS`.
  `frame/design.md` *Grounding*, the `tests/censuses.py` row; `plan.md` A10.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | When a badge cannot be served, does a reader's browser show its `alt` text in its place on the release page? The proxy's 404 for a failing origin was probed; how a browser draws that image was not, because no browser runs in a subagent's environment and the only browser in reach is the person's own. | a measurement | Yes: the reader sees `suite: 6328 passed` and the rest as words. No, a broken-image mark alone: the numbers are still in the note's body as `gh release view --json body` prints it, but not on the page. Either answer leaves the build as it is, since the `alt` text is written either way. | The browser shows the `alt` text; the build proceeds as framed. Answerable after the 0.29.0 release by opening its note with images blocked. | open |
