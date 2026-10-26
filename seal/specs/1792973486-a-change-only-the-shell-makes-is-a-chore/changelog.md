### Changed

- **A gate that stops a session is weighed by the work a work item owns
  (#1031).** This repository's `CLAUDE.md`, *The rule a mechanism is kept
  against*, now says that a gate that stops a session, the routing check
  among them, guards the work a work item owns. A change that would be
  routed `no work item`, such as a formatter run, a dependency bump or an
  identifier renamed across files by `sed`, is outside that work. A gap in
  that kind of gate which only such a change passes through is not a
  weakness to close, so no such gate is built to catch a change only the
  shell makes. The checks that run on every pull request are not that kind
  of gate, and the rule does not exempt them. Nothing the plugin installs
  into a consuming repository changes.
