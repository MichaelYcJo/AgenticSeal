### Fixed

- **An `automation` run in a migration repository no longer stops at the
  smith's first code commit (#988).** Before this, the commit gate's parity
  arm stood on every code commit that carried no parity mark at HEAD, and in
  a review chain the warden writes that mark only after the smith has
  committed. Under the `automation` press the commit was refused and handed
  back, so the build ended there. Now a branch whose `routing.md` answers
  `through the review chain` meets neither arm at the commit, inside git and
  in the PreToolUse reading alike. A branch with no declaration, and one
  answering `straight to the PR`, still meet the parity arm at the commit.
- **A chain-declared pull request in a migration repository owes the
  comparison in every round record (#988).** Where `seal/parity.md` is
  declared and the pull request changes a path outside `docs/` and `seal/`,
  `chain-check` refuses a ready pull request while a round record of a work
  item reviewed through the review chain holds no `original:` line, or holds
  one naming a commit other than the migration config's `Baseline commit`.
  It also refuses a migration config whose `Baseline commit` row names no
  commit. Each refusal names the record or the config, and both commits
  where two are compared; a draft prints the same lines. The warden writes
  the line in each round once it compared that round's target with the
  original. In a migration repository, a chain-declared work item whose
  round records were written before this release carries no such line and
  meets the refusal at its next ready pull request, so it merges before the
  upgrade or has its rounds written after it, as
  `docs/the-review-record.md` *What the check reads at the pull request*
  says of a line the grammar table adds.
- **Three shapes leave a chain-declared branch's code uncompared and
  unchecked (#988).** The pull-request half runs from the plugin release
  that `.github/workflows/hygiene.yml` pins, while the commit half runs from
  the installed plugin. A migration repository moves the pin's
  `v<version>` to this release when it upgrades; until then its CI reads no
  `original:` line, and a chain-declared branch commits code nobody
  compared. In local mode nothing under the root is committed, so no
  pull-request check reads a round record, the cost the review arm's
  declaration already carries there. And a declaration rewritten from
  `through the review chain` to `straight to the PR` after code was
  committed leaves those commits compared by nobody, because the check
  reads the answer at HEAD.
- **A `## Rule changes` line that begins inside a code span is refused at
  its line (#988).** A value whose code span opened at the end of one line
  and closed on the next left the second line beginning inside the span,
  and `rule_changes.parse` dropped it as it drops a comment. The section
  parsed clean, `chain-check` passed it, and `settle` would have written
  the value without that line. `parse` now refuses the line at its number,
  and the spec applies nothing until each span closes on the line that
  opens it.
