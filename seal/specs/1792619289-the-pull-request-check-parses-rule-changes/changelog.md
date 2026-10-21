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
- **A near miss of the `## Rule changes` heading is refused instead of read
  as a spec with no section (#1006).** A heading at any level whose letters,
  case folded, are those of `Rule changes`, such as `## Rule Changes` or
  `### Rule changes`, and that is not `## Rule changes` itself, is refused at
  its line. Before this, `settle` named such a spec as one written before the
  section existed and applied nothing from it. Now `settle` holds it, and
  `chain-check` refuses it at the pull request. A heading with other
  letters, such as `## Rules changes`, is still another section.
