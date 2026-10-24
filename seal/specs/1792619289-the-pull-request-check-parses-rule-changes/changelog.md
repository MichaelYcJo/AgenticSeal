### Fixed

- **A spec whose `## Rule changes` does not parse now fails its own pull
  request (#1006).** Before this, the section was first parsed at the
  owner's settle after the release. There a section that does not parse
  applies nothing, and no pull request is left to fix it in. `chain-check`
  now parses the section with the reader `settle` uses, in the spec of each
  work item whose `routing.md` it judges, under either `Planning` answer.
  On a pull request that declares a work item, it also parses every work
  item spec the pull request's own commits add or change, since a declared
  work item can edit another work item's section. A refusal names the spec,
  the line the reader names and the reader's reason. It fails a ready pull
  request and prints on a draft. The broad gate's own run prints it, and
  fails on it only where a ready pull request is already open. A spec with
  no `## Rule changes` section, a work item with no `spec.md`, a spec
  another pull request's squash carried, a spec only moved, and every spec
  of a pull request that declares nothing are left alone. Where the reader
  will not load, the check exits 2 and says so.
- **A near miss of the `## Rule changes` heading is refused instead of read
  as a spec with no section (#1006).** A heading at any level whose letters,
  case folded, are those of `Rule changes`, such as `## Rule Changes` or
  `### Rule changes`, and that is not `## Rule changes` itself, is refused at
  its line. Before this, `settle` named such a spec as one written before the
  section existed and applied nothing from it. Now `settle` holds it, and
  `chain-check` refuses it at the pull request. A heading with other
  letters, such as `## Rules changes`, is still another section.
