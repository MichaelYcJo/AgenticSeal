"""The sixteen config shapes `seal/threads/1791852616-the-config-table-has-its-
own-grammar-beside-the-gfm-walker/frame/design.md` *Data & interfaces* measured, as
texts (#871).

Data and nothing else. Each shape is the document one row of that table is
about, keyed by the row's number, and each is a place where the config
table's own grammar and `hooks/config.py#gfm_table` answered differently
before #871 moved the table onto the walker. The texts that hold an HTML
comment opener build it by concatenation, so that no line of this file
begins with one.

`READ` is what the walker reads of each, as `(item, value)` pairs, and
`STOPS` the words its refusal names the stopping place by, or None where it
refuses nothing. Both were read off the walker the day the shapes were
written, against the frame's measurement of what cmark-gfm renders: a row
here is one the renderer shows, and a shape the renderer shows differently
from the walker is refused.
"""

OPEN = "<" + "!--"
CLOSE = "-->"
HEAD = "| Item | Value |\n|---|---|\n"
TOP = "# Repository config\n\n"

SHAPES = {
    # a non-blank line directly above the header: the migration's three
    1: TOP + f"{OPEN} note {CLOSE}\n" + HEAD + "| Mode | shared |\n",
    2: TOP + "A line of prose.\n" + HEAD + "| Mode | shared |\n",
    3: TOP + "| Item | Value |\n| Mode | shared |\n",
    4: TOP + HEAD + "a paragraph\n| Mode | shared |\n",
    5: TOP
    + HEAD
    + "| Mode | shared |\n"
    + f"{OPEN} the command before the move, kept for reference\n"
    + "| Broad gate | old -q |\n"
    + f"{CLOSE}\n"
    + "| Broad gate | bin/test -q |\n",
    6: TOP + HEAD + "| Record language | English |\n| a | b | c |\n| Mode | shared |\n",
    7: TOP
    + HEAD
    + "| Record language | English |\n"
    + "| Broad gate | bin/test -q | tee out |\n"
    + "| Mode | shared |\n",
    8: TOP + HEAD + "| Record language | English |\n|---|---|\n| Mode | shared |\n",
    9: TOP + HEAD + "| Record language | English |\n" + HEAD + "| Mode | shared |\n",
    10: TOP + "| Mode | local |\n\n" + HEAD + "| Mode | shared |\n",
    11: TOP + "| Mode | local |\n" + HEAD + "| Mode | shared |\n",
    12: TOP + " | Item | Value |\n|---|---|\n| Mode | shared |\n",
    13: TOP + HEAD + "| not a row\n| Mode | shared |\n",
    14: TOP + HEAD + "| Record language | English |\nprose after\n| Mode | shared |\n",
    15: TOP + HEAD + "| Mode | shared |\n## Notes\n| x | y |\n",
    16: TOP + "| Item | Value |\n|---|---|---|\n| Mode | shared |\n",
}

READ = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [("Mode", "shared")],
    6: [("Record language", "English")],
    7: [("Record language", "English")],
    8: [("Record language", "English")],
    9: [("Record language", "English"), ("Item", "Value")],
    10: [("Mode", "shared")],
    11: [],
    12: [("Mode", "shared")],
    13: [],
    14: [("Record language", "English")],
    15: [("Mode", "shared")],
    16: [],
}

STOPS = {
    1: f"directly under `{OPEN} note {CLOSE}`",
    2: "directly under `A line of prose.`",
    3: "with no delimiter row under it",
    4: "continues with `a paragraph`, a line with no pipe",
    5: "ends above `| Broad gate | bin/test -q |`, a row the walk never reaches",
    6: "stops at `| a | b | c |`, which is not a 2-cell row",
    7: "stops at `| Broad gate | bin/test -q | tee out |`, which is not a 2-cell row",
    8: "stops at `|---|---|`, a delimiter row out of place",
    9: "stops at `|---|---|`, a delimiter row out of place",
    10: None,
    11: "directly under `| Mode | local |`",
    12: None,
    13: "stops at `| not a row`, which is not a 2-cell row",
    14: "continues with `prose after`, a line with no pipe",
    15: None,
    16: "over a delimiter row of 3 cells",
}
