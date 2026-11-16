# Phase 1: 1794797697-a-census-cell-states-an-impossible-result

## What this phase found

- **The paragraph's first wrapping put a line at 93 columns.** `tests/behaviour/test_docs_line_wrap.py` refused `agents/framer.md:180` (executed). The orchestrator rewrapped the paragraph at 76 columns, the width of the paragraphs around it, and kept the code span `## Removes` on one line. The three modules of the phase's *Verified by* cell then passed, 148 cases (executed: `bin/test tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_release_hygiene.py -q`).
- **The paragraph adds 1,195 bytes, not the 900 design G14 estimated.** `agents/framer.md` goes from 14,533 to 15,728 bytes (executed: `wc -c`), about 3.3 percent of the 35,884-byte preload G14 counts. The paragraph states each of C1 to C5 once, and its one citation replaces a restatement of the verify section.
- **The version search the cell names prints nothing after the build** (executed: `git grep -n -F '0.38.1' -- . ':!seal/threads'`, exit 1).
