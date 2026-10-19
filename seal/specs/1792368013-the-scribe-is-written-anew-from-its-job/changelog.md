### Changed

- **The scribe preloads the contract alone and opens `legacy-parity` at its
  first step (#970).** `agents/scribe.md` is written to the shape the
  warden, the smith and the sealer have: `skills: [agent-contract]`, then
  `## Job`, `## Order of work`, `## Never` and `## Rules`. It is spawned by
  your session, not by the smith, and where it cannot find the original it
  returns `original not found` with what it tried, leaving the question to
  your session.
- **A parity review's verdicts are four words (#970).** `differs`,
  `grounded`, `equivalent` and `unread` replace the four emoji, one word at
  the start of each line. A round record or report written with the emoji is
  history and stays as it is; nothing reads the labels.
- **`legacy-parity` names who writes the parity mark (#970).** The warden
  writes it in a review round, and a session where it compared without one.
  The scribe and the smith write none. The skill's migration-config section
  points at `templates/parity.md` for the fields rather than copying them.
- **The parity setup no longer proposes `docs/policies/` (#970).** A new
  `seal/parity.md` written from the template carries a placeholder for the
  policy root, the directory your repository already keeps ratified policy
  in, or `none`, and the setup reads it from your tree instead of offering
  to create one. An existing `seal/parity.md` is read as before.

  | Agent | Preload bytes | Read-set bytes | Outcome |
  |---|---|---|---|
  | scribe | 40,466 → 34,697 | 40,466 → 40,385 | unverified: no case runs the scribe, and the repository owner answers it at the first parity run |

  Each pair is the tree at `1d665d48` → the tree at `c8391342`, measured by
  `payload-meter --agent scribe`, whose figures include the `CLAUDE.md` pair
  on the measuring machine (14,775 B on both sides). The read set adds the
  bytes of `skills/legacy-parity/SKILL.md`, which the scribe opens at its
  first step: 0 at `1d665d48`, where the skill was preloaded and already in
  the figure, and 5,688 at `c8391342`. The agent's own share of the read set
  is 25,691 → 25,610 B.
  (`1792368013-the-scribe-is-written-anew-from-its-job`, #970)
