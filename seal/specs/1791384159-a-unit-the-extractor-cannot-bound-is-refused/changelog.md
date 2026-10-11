### Fixed

- **A multi-line TypeScript signature no longer reads `ok` over a rewritten
  body (#848, #870).** A ledger row citing a function by name, in any file
  that is not Python or markdown, was bounded by a rule that guessed where
  the function ends from its indentation. For a signature whose parameters
  run over several lines, the way Prettier writes them, the guess stopped
  before the body, so a rewrite of the body still read `ok` and
  `--reverify` had nothing to notice. Such a row now reads `BROKEN` and
  says what to write instead: a quoted line of the function, whose region is
  the paragraph it sits in. #848's function has no blank line inside it, so
  one quote of its signature covers the whole function, body included.

### Changed

- **A unit is bounded only where a real parser reads it; everywhere else
  the anchor is a quoted line (#870).** A bare symbol (`path#name`) is read
  by Python's own parser in `.py` and `.pyi` files and by the heading path
  in `.md` files. In every other file — TypeScript, JavaScript, Go, Rust,
  Java, Kotlin, Swift, C, C++, C#, YAML, Ruby, shell, a file with no suffix —
  it reads `BROKEN` with "no bounding rule for `.ts`; anchor a quoted line
  instead:" followed by the anchor to write on the row's own path. A quoted
  line (`path#"a line of the unit"`) covers the run of non-blank lines it
  sits in, so a function with a blank line inside it is cited with one quote
  per paragraph, in the same cell. A bare symbol in a `.py` the running
  Python cannot parse reads `BROKEN` naming that Python's version and the
  error's line, where it used to be read by the guessing rule.
  `--migrate` leaves an old `path:line` row in such a file with the same
  sentence as its reason.

  **What an installer sees on upgrade.** The commit hook reads the new rule
  at the next commit after the plugin updates; the CI copy under `tools/`
  changes when `/specseal:evidence-ci` is run again. At either moment:
  every row citing a bare symbol in a file that is not `.py`, `.pyi` or `.md`
  reads `BROKEN` with the remedy on its line, including rows the old rule
  bounded right. The repair is one edit per row — quote a line of the unit
  (`path#"<the line>"@00000000`), then run `evidence-check --reverify`, which
  fills the hash; under `Ledger frozen from` the repair is the `Corrected ·`
  row `--reverify` names. A row citing a decorated `.pyi` stub reads
  `DRIFTED` once, because the parser takes the decorators into the span: read
  it again, then `--reverify`. Every `.py` and `.md` row keeps its hash and
  its verdict.
