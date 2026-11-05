# Questions for the planner: an import inside a fence is not charged (#1185)

The ticket left these judgments open, and the tree answered each of them:

- Whether a code span is skipped as well as a fence: `frame/design.md` G2, and `frame/plan.md` *Alternatives considered*, the third row.
- What a fence is, a tilde fence and a fence nobody closed among them: `frame/design.md` G3.
- Whether an import inside an HTML comment is charged: `frame/design.md` G2 and G3.
- Whether the meter reads spans and comments by a rule of its own or through `liveness`: `frame/plan.md` *Alternatives considered*, the first and second rows.
- Whether a path continues through `\ `: `frame/design.md` G2 and G4.
- Whether the test's second import pattern changes: `frame/plan.md` *Alternatives considered*, the fourth row.

The frame assumes that a span whose partner stands on a later line is a span only where `_partner_ahead` finds that partner before the paragraph ends. Where `_paragraph_ends_at` misjudges a paragraph's end, an import beside such a run is charged or left uncharged wrongly. No file the meter reads today holds the shape (G6), and a different answer would not change what gets built.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Should `seal payload` follow Claude Code's import reader where it goes past the memory docs? Claude Code 2.1.318 also skips indented code blocks and every HTML block other than a comment. It cuts a path at `#`, refuses a path that opens with a character other than `./`, `~/`, `/`, a letter, a digit, `.`, `_` or `-`, skips an imported file whose extension is not text, and reads no import in a frontmatter block (`frame/design.md` G3). | a person | Follow the docs only: the meter reads what the docs promise, and the docstring names each other shape as one it does not model. The next Claude Code release cannot make the meter wrong where the docs did not move. Follow the binary too: the meter matches 2.1.318 on every shape, and each later release can change any of them with no line in the docs. | Follow the docs only, with the limits named in `imports_of`'s docstring (`frame/design.md` *Scope*, *Out*). | open |

Q1 is a person's because it decides which source the meter answers to, the published docs or one release's code. No probe can say which source a person wants the meter held to.
