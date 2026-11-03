# verify, `seal arms`

A party that proves condition 2 of `skills/verify/SKILL.md` *2. Able to
fail* for a whole module opens this file before it runs `seal arms`. It
holds what the command breaks, its bound, its two operators and what it does
not claim.

## `seal arms` asks condition 2 of a whole module, one arm at a time

Condition 2 is asked of the case at hand. **A module has arms nobody
ever asked it of**, and a count of them taken by hand is wrong as soon as the
module changes.

```
seal arms hooks/routing-edit-gate.py
seal arms hooks/routing-edit-gate.py --tests "bin/test tests/hooks/test_routing_edit_gate.py -q"
```

With no `--tests` it lists the arms and mutates nothing. With `--tests` it
first runs that command once against the module as it is, which has to pass
(below). Then it makes each arm wrong in turn, runs the command again, and
names the arms nothing kills. It restores the module from held bytes and
compares the sha256 after every mutation, never with `git checkout`, which
reaches the uncommitted work in the rest of the tree.

**`--timeout` bounds the wait, and not the work.** Each operator's command is
waited for at most 900 seconds by default (`--timeout 0` removes the bound),
and an arm asks two operators, so one arm can take twice that. When the bound
is reached, only the command's own process is killed. A wrapper command is the
one that leaks: where `--tests` names a runner that starts pytest as a child of
its own, as the example above does, a timed-out pair leaves that suite running,
unbounded and unreported, beside every arm after it. The first run against the
unmutated module is waited for under the same bound and leaks the same way
when it reaches it, before the run is refused. Against a module whose
suite can approach the bound, name the pytest command in `--tests` directly
rather than a wrapper.

**There are two ways to be wrong and the counts differ by a lot**, so the
report keeps them apart and a quoted number has to say which one it is:

| Operator | Asks |
|---|---|
| `invert` | would a case notice this test being **backwards** |
| `remove` | would a case notice this arm being **absent** |

**A survivor count is a measurement, not a property of the module**: it moves
when either the module or its cases change. Take it with the command above
whenever it is needed, and never write one into a document.

The two denominators differ because **a pair both operators answer identically
is asked once.** A handler with one type left is aimed at what nothing raises
by either operator, so `invert` refuses it and the report names the pair;
`remove` keeps it.

An arm counts watched when **either** is noticed, because *does any case
depend on this arm* is answered by one yes.

An arm is an `ExceptHandler` counting each member of an except tuple
separately, or an `If`, `While` or `IfExp` counting each **top-level** member
of the boolean test separately, plus a `match_case`'s alternatives and guard
and a comprehension's `if` guards. The walk is derived from the grammar rather
than from a list, and it **refuses an AST node type it does not recognise**
instead of skipping it: a walk that skips silently undercounts the way a hand
count does.

**A `killed` is a measurement only when the command passed without the
mutation**, so `--tests` runs once against the module as it is before
anything is written. A `-k` that selects no case, a module path that does not
exist and a case already failing each exit non-zero whatever the module
holds, so without that run each would read `killed` beside every arm. When
that first run exits non-zero, does not return within `--timeout`, or cannot
be spawned, the command prints `no baseline:` with the cause and what the
command printed, writes nothing, measures no arm, and exits 2, the code it
already gives a negative `--timeout`. If the command itself changed the module
during that run, the module is put back from the bytes read before it and the
line says so instead. Where it cannot be put back, because the command left
it unreadable, unwritable or replaced by a directory, the line names the
error.

Two things it does not claim. **A survivor is not automatically a defect:** an
arm that cannot be constructed, or one whose removal preserves behaviour,
belongs in the report and is not work anybody owes. And a measured run is
**report-only, exit 0 either way**: whether an unwatched arm should fail a
run is an open decision, not an omission.
