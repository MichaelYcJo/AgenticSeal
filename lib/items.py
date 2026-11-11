"""Shared reader: the items of a section in the grammar of
`skills/settle/rule-changes.md` *Rule changes*.

An item is a line `- <kind>`, then one field per line indented two spaces,
`  <name>: <value>`, a value continuing on the lines below it indented four.
`items` reads a section's lines into items and `field_values` one item's
fields into values. The no-change block, `- nothing` with its one optional
field `why`, is the item a section that holds nothing writes alone:
`nothing_block` reads it, and `unread_block` names a first line that opens
like it and is not it. `lib/gaps.py` reads a closing memo's
`## Not verified` with them, and `skills/settle/scripts/rule_changes.py` a
design's `## Rule changes`.

Standard library only, and Python 3.9 syntax, as every module under `lib/`.
"""

import re

# A design section's items, `skills/settle/rule-changes.md` *Rule changes*: the
# item's line, then one field per line indented two spaces, a value continuing
# on the lines below it indented four.
ITEM_RE = re.compile(r"^- (\S+)\s*$")
FIELD_RE = re.compile(r"^  ([a-z]+):(?: (.*))?$")
CONTINUED = " " * 4
# The item a section that holds nothing writes alone, and its one field.
# `## Not verified` and `## Rule changes` read it through `nothing_block`.
NOTHING = "nothing"
WHY = "why"
NOTHING_WRITTEN = f"the block `- {NOTHING}` with `  {WHY}: <reason>`"
# A first line that opens like the block and is not it: `none` or `nothing`
# in any case, behind any list marker. The old `none — <why>` line is one.
# Such a line is no block, and its reader names it (`unread_block`).
NEAR_NOTHING = re.compile(r"[-*+\s]*(?:none|nothing)\b", re.IGNORECASE)
UNREAD_BLOCK = (
    f"`{{said}}` opens like {NOTHING_WRITTEN} and is not it, so it was read as prose"
)


def items(body):
    """`(items, error)` for BODY, `[(line number, line)]`, read as a design
    section's items. Each item is `{"kind", "line", "fields"}`, `fields`
    mapping a name to `[line number, [value lines]]`; ERROR is the first line
    that is no part of an item, as `(line number, why)`, or None."""
    found, item, last = [], None, None
    for no, line in body:
        m = ITEM_RE.match(line)
        if m:
            item, last = {"kind": m.group(1), "line": no, "fields": {}}, None
            found.append(item)
            continue
        if item is None:
            return found, (no, "a line outside an item")
        m = FIELD_RE.match(line)
        if m:
            last = m.group(1)
            if last in item["fields"]:
                return found, (no, f"`{last}` given twice")
            item["fields"][last] = [no, [m.group(2) or ""]]
            continue
        if last and (not line.strip() or line.startswith(CONTINUED)):
            item["fields"][last][1].append(line[len(CONTINUED) :])
            continue
        return found, (no, "a line that is not a field of the item above")
    return found, None


def field_values(item, need, may):
    """`(values, error)`: ITEM's fields as `{name: value}`, or ERROR, the
    first field outside NEED and MAY, missing from NEED, or empty."""
    fields, values = item["fields"], {}
    for name, (no, _) in fields.items():
        if name not in need + may:
            return None, (no, f"`{name}` is not a field of `{item['kind']}`")
    for name in need:
        if name not in fields:
            return None, (item["line"], f"`{item['kind']}` needs `{name}`")
    for name, (no, parts) in fields.items():
        values[name] = "\n".join(parts).strip("\n").rstrip()
        if not values[name].strip():
            return None, (no, f"`{name}` is empty")
    return values, None


def opens_the_block(line):
    m = ITEM_RE.match(line)
    return bool(m) and m.group(1) == NOTHING


def unread_block(body):
    """`(line number, why)` where BODY, a section's non-blank `[(line number,
    line)]`, opens with a line that opens like the no-change block and is
    not it (`NEAR_NOTHING`, `UNREAD_BLOCK`); else None. The line decides
    nothing: `nothing_block` passes it on as any other line, and its reader
    refuses the section for what it lacks and names the line. Whether it
    meant the block is the judgment of the agent that reads the record."""
    first_no, first = body[0]
    if opens_the_block(first) or not NEAR_NOTHING.match(first):
        return None
    return first_no, UNREAD_BLOCK.format(said=first.strip())


def nothing_block(body):
    """None where BODY, a section's non-blank `[(line number, line)]`, does
    not open with the no-change block; else its errors, `[(line number,
    reason)]`, empty where the block reads. The block is read in its one
    spelling, and a line that opens like it is passed on (`unread_block`).
    Its field `why` is optional and its value is returned to nobody: the
    readers use only that the section holds no row or no operation, and the
    reason is the agents' to read."""
    if not opens_the_block(body[0][1]):
        return None
    found, error = items(body)
    if error:
        return [error]
    if len(found) > 1:
        return [(found[1]["line"], f"`- {NOTHING}` is the section's one item")]
    _, error = field_values(found[0], (), (WHY,))
    return [error] if error else []
