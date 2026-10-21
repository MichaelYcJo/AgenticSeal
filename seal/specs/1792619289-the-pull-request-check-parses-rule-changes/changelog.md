### Fixed

- **A spec whose `## Rule changes` does not parse now fails its own pull
  request (#1006).** Before this, the section was first parsed at the
  owner's settle after the release. There a section that does not parse
  applies nothing, and no pull request is left to fix it in. `chain-check`
  now parses the section of each work item whose `routing.md` it judges,
  under either `Planning` answer, with the reader `settle` uses. A refusal
  names the spec, the line the reader names and the reader's reason. It
  fails a ready pull request, prints on a draft, and stays a refusal in the
  broad gate's own run. A spec with no `## Rule changes` section, a work item
  with no `spec.md`, and a work item another pull request's squash carried
  are left alone. Where the reader will not load, the check exits 2 and says
  so.
