### Changed

- **A rule of the agent contract is cited by its number in words, and
  another file's section by its heading text (#1005).** The contract's
  headings read `## <N> <title>`. A spawn prompt and every file outside
  the contract cite a rule as `contract rule <N>`, and the contract and the
  agent definitions as `rule <N>`. Another file's section is its backticked
  path and the heading text in italics, and a step is cited by its heading,
  never its number. No living file writes the section sign:
  `tests/test_no_living_file_writes_the_section_sign.py` refuses one at its
  path and line, outside `seal/specs/`, `changelog/`, `CHANGELOG.md` and
  `evals/behaviour/`. The label `session_cost.py --segments` prints for an
  agent that spawned another now reads `Contract rule 6`, and the broad
  gate's refusals, `settle`'s readers heading and the tracker label's
  source name their section by its heading. Every agent's preload is
  smaller: framer 16 bytes, smith 78, warden 70, sealer 81 and scribe 59.
- **The record templates carry no comment and no guidance (#1005).** Each
  of the eight `templates/sdd-*.md` holds headings, table headers,
  placeholders, the labelled lines its record's grammar asks for and its
  foot line. The guidance is stated once, in the skill or definition the
  record's writer reads, and a record started from a template carries none.
  Records already in the tree keep their comments, and the readers still
  hide them, until #1012.
- **The fence rule and the line split are written once (#1005).**
  `unverified_check.py` takes `fence_opener`, `fence_closes`, `GFM_LINE_RE`
  and `gfm_lines` from `hooks/blocks.py`, so a change to the rule reaches the
  hook readers and the record readers in one commit.
