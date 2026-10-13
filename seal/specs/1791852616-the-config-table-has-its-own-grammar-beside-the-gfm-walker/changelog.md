### Changed

- **`seal/config.md`'s table is read the way GitHub shows it, or refused
  (#871).** The `| Item | Value |` table had a reader of its own — a stop
  rule that stepped past some lines and stopped silently at others — beside
  the walker the plugin holds to cmark-gfm, GitHub's renderer, for the
  pact's tables. It now has only the walker. A row is a row where GitHub
  shows it as one; a line the walker cannot read as GitHub shows it is
  refused in a sentence naming the line and the edit; the rows above that
  line are read, and every row written below it is that refusal, never an
  absent row. What an installed config sees change, shape by shape:
  - a non-blank line directly above the header — a comment, a line of
    prose, a row of something else — was read, and is now refused: leave a
    blank line above the header. A config `seal mode` wrote, or one copied
    from `templates/config.md`, already has that blank line;
  - a header with no delimiter row under it, or one of another width, was
    read as a table GitHub does not render, and is now refused: write
    `|---|---|` under the header;
  - a bare pipe in a value (`| Broad gate | bin/test -q | tee out |`), which
    GitHub shows cut off at the pipe, used to end the table silently and drop
    every row below it to its default; it is now refused, and `broad-gate`
    names the escape: write it `\|`;
  - a third cell, a stray `|---|---|`, or a line of prose among the rows
    used to end the table silently, or was stepped past where no row had
    been read yet; it is now refused: write it as `| … | … |`, or take it
    out;
  - a row under a comment, a fence or a blank line that ends the table was
    read as one of its rows, which GitHub does not show; it is now refused
    as a row the walk never reaches: move it into the table, or, where it
    heads a table of something else, put a heading between the two tables;
  - a row after a form feed, U+2028 or another character only Python ends a
    line at, on the line of the row above, was read as a row of its own,
    which GitHub shows as more of the row above; it is now refused: put it
    on a line of its own;
  - an item written again below the line the walk stopped at has no value,
    as an item written twice anywhere has none, so the row read above that
    line is not taken as the answer;
  - a header indented one to three spaces, and a row indented the same way,
    were not read; they are, as GitHub shows them.
- **Every command reading the table refuses an unread row at exit 2, and no
  hook asks anything (#871).** `broad-gate` runs nothing and quotes the line
  — with *write it `\|`* where the line is its own row holding a bare pipe,
  and saying the rows below go unread only where a row is written below it;
  `seal mode` and `seal mode --check` write and move nothing; `fold-check`,
  `correction-check`, `evidence-check --reverify` and `pact-check` judge
  nothing. A row the walk read above the refused line is a value, and is
  used. The mode gate reads a refused `Mode` row as an answer it cannot act
  on and says nothing, as it does for a file that will not read; the prompt
  budget of a refused table is zero.
- **`seal mode` no longer writes a second `Mode` row under a bare pipe
  (#871).** The writer reads the walker's table, so it overwrites the line
  the walker read as the `Mode` row, inserts a new one after the last row the
  walker read, and refuses a table the walker refused — the file is left
  exactly as it was, and the line is named.
- **A vendored `evidence-check` carries the walker's line grammar (#871).**
  A copy with no `hooks/` beside it reads the table on the lines it can judge
  alone, follows a fence or an HTML comment above the header to its close —
  so the closed comment `seal mode` writes above every config's header is
  read — and refuses where it lacks the plugin's block state — a block left
  open above the header, a comment or fence inside the table — so it may
  refuse where the plugin reads, and never reads where the plugin refuses. Run `/specseal:evidence-ci` to pick it up; until then a
  repository's CI reads with the stop rule.
