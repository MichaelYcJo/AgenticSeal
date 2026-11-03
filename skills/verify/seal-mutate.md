# verify, `seal mutate`

A party that proves condition 2 of `skills/verify/SKILL.md` *2. Able to
fail* for one unit opens this file before it runs `seal mutate`: the crafter
at each unit that adds behaviour, and a round or the sealer re-running a
claim. It holds the command, its verdicts with their exit codes, and its
bound.

## `seal mutate` asks condition 2 of one unit, one break at a time

`seal arms` breaks a module's arms under two fixed operators. The unit an
implementer has just added is usually something else: a constant, a flipped
comparison, a sentence a case pins. The break is whatever makes that unit
wrong, so the loop is one command per break:

```
seal mutate <file> --replace "<old>" "<new>" --tests "bin/test tests/<module>.py -q -k <cases> -p no:xdist"
```

`<old>` is literal text and must occur exactly once in the file, or nothing
is written; `<new>` may be empty, which deletes. Any UTF-8 text file can be
the target.

**A `.py` mutant that does not compile is refused before anything is written
or run.** Cases that load the module fail on the syntax error whatever the
unit does, and that red would read as a case noticing the break. For a target
whose name ends in `.py`, the command compiles each mutant with the builtin
`compile` over the bytes the write would put on disk, and refuses at the
first `SyntaxError`, naming its line. The file as it is is compiled first.
Where it does not compile under the interpreter running `seal`, no mutant is
compiled, the verdict comes from the cases' exit code alone, and the first
line printed says the mutants were not compiled, with that interpreter's
version and the error's line: the cases may run under another interpreter
that reads the file. No other kind of file is compiled or parsed, a `.md`,
a `.yml`, a JSON or TOML file and a script with no `.py` suffix among them,
so a mutant its loader cannot parse can still read `red`. Two limits stay
beside that one. The compile uses the grammar of the interpreter running
`seal`, not the cases', so a construct only one of the two accepts is read
wrongly in one direction or the other. And a mutant that compiles and then fails at import, a misspelt
module-level name for one, is not refused: whether its red watches the unit
is for the reader of the run, and running that one pair alone shows the
output.

The command first runs `--tests` against the file as it is, and
goes on only if that passes. A `-k` that selects nothing, a mistyped module
and a case that already fails each exit non-zero, and without that run each
would read `red` for a unit no case ran against. Then it writes the break,
removes that file's cached bytecode
for every interpreter tag, runs `--tests` with `PYTHONDONTWRITEBYTECODE=1`,
puts the file back from the bytes it read first and compares their sha256,
and removes the bytecode again. Nothing is read from git. The script is
`skills/verify/scripts/mutation_check.py`, and it uses `seal arms`'s own two
functions for the bytecode and the restore.

The first line printed is the verdict, then the command's own output:

- `red`, exit 0: a case failed against the break, so the unit is watched.
- `SURVIVED`, exit 1: the cases passed, so nothing they run watches the unit.
- exit 2 for every run that measured nothing: `no baseline` (the cases fail
  without the break, so the break was never written), `timed out`, `could not
  start`, `could not run`, `refused` (nothing was written: `<old>` does not
  land once, or a `.py` mutant does not compile), `not restored`
  (the file may still hold the break; restore it from the commit made
  before the run), and
  `interrupted`.

So `seal mutate … && seal mutate …` stops at the first unit nothing
watches, or at the first run that could not say.

**Several mutants of one file go in one call.** Give `--replace OLD NEW` once
per mutant. Every pair is checked before anything runs, and one that does not
land exactly once, or a `.py` mutant that does not compile, refuses the whole
call, naming the pair by its place. The baseline then runs once, and
each mutant is written alone, run once and restored, in the order given. The
call prints `mutant <n>: <verdict>` per pair and a line counting the
verdicts. A red line carries the cases' exit code, `mutant <n>: red (exit
<N>, <s>s)`, and the command decides nothing from it: under pytest a 2 is a
collection error, and a 1 is a failing case or an import error raised
inside one. The call exits 1 where any mutant survived, 2 where none did
and a run measured nothing, and 0 where every mutant is red. Put `-x` in `--tests`, so
each mutant's run stops at the first case that notices it; the command does
not stop the cases itself.

**Why the cache beside the file, and not `tests/__pycache__`.** CPython runs
a cached `.pyc` instead of the source whenever the size and whole-second
mtime it recorded still match, and a same-length break written inside one
second matches. Only the mutated file's cache can be stale. An importer's is
valid for its unchanged source, so clearing `tests/__pycache__` removes
caches that are right and misses the one that matters whenever the mutated
file lives anywhere else. Every tag goes, because the
interpreter that runs the command and the one that runs the cases can
differ.

**The cases inherit `PYTHONDONTWRITEBYTECODE=1`.** A case that needs a
`.pyc` to exist, such as one that plants a cache to show it is removed, has
to write it itself, with `py_compile` or with `sys.dont_write_bytecode`
switched off for the plant. An import made under the variable writes
nothing, and the case then goes red on its own precondition whatever the
break was.

**The bound ends the run, not only the process it spawned.** `--timeout` is
300 seconds by default for each of the two runs, and `0` removes it. On
POSIX the command runs in a session of its own and a timed-out run's whole
process group is killed, so a wrapper's pytest does not outlive the verdict.
That is the hole `seal arms`'s bound still has. The group of a run
that exited is ended too, and the wait is on the process rather than on its
output, so a child the cases leave behind neither outlives the verdict nor
holds it back. A process that put itself in yet another session is outside
the group and outlives the kill; the verdict names that as the bound's
limit, and cannot tell whether one did. Ctrl-C
reaches this command rather than the cases, and it ends the group before the
restore. On Windows only the direct child is ended, and the verdict says that
anything it started was not.

`-p no:xdist` belongs on a handful of cases: starting the workers takes
longer than the cases do. For a module's arms rather than one unit,
`seal arms` (`skills/verify/seal-arms.md`) is the command.
