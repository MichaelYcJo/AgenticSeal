# The reader registry — what each unit reads, and what a frame removes

Every unit of shipped Python says, in its own docstring, what class of input
it decides from. That line is the registry: opening the unit is what finds
it, and `grep -rn "Reads: guess"` is the list. A frame names what its work
takes out of the tree in one section of its own `spec.md`, where a checker
reads each row as a claim that the thing is gone. This document is the
standing account of both rules, what holds each, and the edge of what either
can see.

Its rules came from #835, after the inventory of every reader (#834) found
that the readers which kept being reopened were the ones imitating a tool
they did not control.

## The four classes and the line that declares one

<!-- specs/1791384152-a-reader-declares-its-input-class -->
**A unit declares the class of what it reads in one docstring line, and the
check reads two words of it.** The line is `Reads: <class> — <what it reads>;
unknown <direction>`, or `Reads: nothing — <why>`. The class is the word right
after `Reads:` and the direction is the last word of the line; the prose
between them is for the reviewer. The classes:

| Class | Means |
|---|---|
| `owned` | a format this repository's own writer produces, or a vocabulary its own checker defines |
| `observed` | a fact asked of the system: an exit code, an AST, `git ls-files`, a JSON a program wrote |
| `guess` | a person's text, or a shape predicted from text the reader does not control |
| `nothing` | the unit decides from no input except what a declaring caller handed it: a writer, a formatter of its own output, a pure function |

The direction says what the unit does with input it does not understand:
`refused`, `passed` or `mixed`. A unit reading several inputs declares the
weakest, `guess` being the weakest, and a unit parsing text its caller handed
it takes the class of where that text came from. The declaration is one line:
a wrapped line has no last word to read, so its explanation goes in the
paragraph under it. ` — ` and ` -- ` both separate, and a `nothing` line
names its reason, as an `Enforced by: nothing` line does.
Enforced by: tests/test_a_reader_declares_its_input_class.py::test_a_declaration_in_the_grammar_passes, tests/test_a_reader_declares_its_input_class.py::test_a_declaration_outside_the_grammar_is_refused_naming_its_words, tests/test_a_reader_declares_its_input_class.py::test_two_declarations_in_one_unit_are_refused

## Who declares: every unit, found by a rule

<!-- specs/1791384152-a-reader-declares-its-input-class -->
**Every top-level `def` and `class` in every tracked `.py` file outside
`tests/test_*.py` declares, and no list of calls decides who.** The file set
is what `git ls-files -z -- '*.py'` names, so a file in a directory nobody
listed is in on arrival. A unit is one inside no other `def` or `class`, a
module-level `if`, `try` or `with` included, and a class declares once for its
methods. Test modules are out by one rule on the file name; a helper module
under `tests/` is in.

Three ways to find a reader were weighed. A list of reading calls choosing
who declares fails quietly: a unit reading through a call the list lacks
needs no line and nothing says so, which is the enumeration over an open
domain that the inventory's release spent its rounds learning not to write. Watching which
units a test run opened misses every unit the suite never runs, and a regex
over a string is no event any audit hook reports, so the `guess` class is the
one it cannot see. **Every unit declaring** fails loudly instead: an
undeclared unit is refused whatever it calls, and what can still pass is a
false declaration, which is a claim a reviewer reads rather than an absence
nobody sees. It costs one line per unit, paid when the unit is touched.
Enforced by: tests/test_a_reader_declares_its_input_class.py::test_the_population_is_every_top_level_unit_git_lists, tests/test_a_reader_declares_its_input_class.py::test_a_new_unit_with_no_declaration_is_refused_whatever_it_calls, tests/test_a_reader_declares_its_input_class.py::test_every_unit_of_shipped_python_declares_or_is_on_the_census

<!-- specs/1791384152-a-reader-declares-its-input-class -->
**The list of reading calls, K1, refuses one lie it can see and selects
nobody.** A unit declaring `nothing` whose body calls a K1 primitive is
refused, naming the call and its line. K1 has two families: the process
boundary (`open`, the `read` methods, `subprocess`, `os.environ`, `sys.stdin`,
`sys.argv`, directory listings and existence tests) and a standard-library
parser handed text (the `re` matchers, `shlex.split`, `json`, `ast.parse`,
`tomllib`, `xml.etree`, `csv`, `splitlines`). A method is matched by its name
on any receiver, a module's included, so `os.open` is `open` and `ast.walk`
is `walk`: the table adds calls and never vouches that a module's other calls
read nothing, because a table read as complete for a module is the quiet
direction again. A module function the table lists counts only where the
file's imports bind it, so a repository's own `load` is not `json.load`. A
call K1 does not list is a row to add, and buys one more contradiction the
check can see, never one more unit that has to declare.
Enforced by: tests/test_a_reader_declares_its_input_class.py::test_nothing_beside_a_k1_primitive_is_refused_naming_the_call, tests/test_a_reader_declares_its_input_class.py::test_a_call_k1_does_not_name_leaves_nothing_standing, tests/test_a_reader_declares_its_input_class.py::test_the_stated_limit_a_primitive_k1_does_not_list_passes

<!-- specs/1791384152-a-reader-declares-its-input-class -->
**A module body that reads outside every unit declares in its module
docstring.** Statements outside any `def` or `class` belong to no unit and
have no ledger spelling, so this is the one place K1 selects: a module whose
body makes a K1 call declares for the body with the same line, and one whose
body makes none owes nothing. A module-level read through a call K1 does not
list is unseen, and it is the whole of what stays quiet in the first rule.
Enforced by: tests/test_a_reader_declares_its_input_class.py::test_a_module_body_that_reads_without_a_declaration_is_refused, tests/test_a_reader_declares_its_input_class.py::test_a_module_body_with_no_k1_call_owes_no_line, tests/test_a_reader_declares_its_input_class.py::test_a_module_body_declaring_nothing_beside_a_read_is_refused

## The census: the units that stood undeclared at landing

<!-- specs/1791384152-a-reader-declares-its-input-class -->
**`tests/undeclared_readers.txt` lists every unit undeclared when the rule
landed, and a listed unit owes nothing until it changes.** Each line is
`path#unit@hash`, the ledger's own spelling and hash
(`evidence_check.py`'s `py_spans` and `content_hash`), so a changed unit is a
moved hash, and the check says to declare it and remove its line. A line
naming a unit that is gone, renamed, declared since or outside the population
is refused, and so is a line outside the grammar. The census need not empty
on a schedule: a unit nobody touches costs nothing listed, and a new or
changed unit declares. When the file lists nothing, the check says to delete
it.

It only shrinks by convention. `tests/reader_registry.py`'s writer refuses to
run where the file exists, but a line put back by hand passes, because
telling it from an original needs history the check does not read. The
census's diff is the reviewer's.
Enforced by: tests/test_a_reader_declares_its_input_class.py::test_a_changed_census_unit_must_declare, tests/test_a_reader_declares_its_input_class.py::test_a_census_line_naming_no_undeclared_unit_is_refused, tests/test_a_reader_declares_its_input_class.py::test_the_writer_refuses_where_a_census_exists

## A frame names what its work removes

<!-- specs/1791384152-a-reader-declares-its-input-class -->
**A `spec.md`'s `## Removes` section lists what the work takes out of the
tree, and each row is read as a claim of absence.** A row's coordinate is the
ledger's grammar without a hash: a function or class in a `.py` file, a
heading path in a `.md` file, a quoted line anywhere else. `evidence-check`'s
records arm reads the section in every live frame: a coordinate that still
resolves is `STANDING`, and a cell the ledger would refuse is `REFUSED`, never
read as gone — a cell that is no coordinate, a test's node id, a bare symbol
in a file no parser bounds, a path that escapes the tree or walks through
`..`, a path that is there and will not read as a file, and a path carrying
a `--map` prefix. A row is read in this tree and nowhere else, so neither the
original a migration declares nor a mapped checkout answers for it. Both
exit 2, as a stated name the tree lacks does. A work item removing nothing writes `nothing — <why>`. The names on the
section's lines are not read as stated names, because the section exists to
say they are gone.

The per-phase removal table this replaces recorded the same fact once per
phase and was read by nothing. A removal a phase makes that the frame did not
name is a divergence, and it goes to `overview.md`.
Enforced by: tests/test_a_record_states_what_the_tree_has.py::test_a_named_removal_that_still_stands_is_standing, tests/test_a_record_states_what_the_tree_has.py::test_a_cell_that_is_no_coordinate_is_refused_naming_the_row, tests/test_a_record_states_what_the_tree_has.py::test_a_bare_symbol_no_rule_bounds_is_refused_never_read_as_gone, tests/test_a_record_states_what_the_tree_has.py::test_a_coordinate_that_does_not_read_is_refused_never_read_as_gone, tests/test_a_record_states_what_the_tree_has.py::test_a_removal_is_read_in_this_tree_never_in_another_checkout

<!-- specs/1791384152-a-reader-declares-its-input-class -->
**Where `seal/config.md` declares `Removes from`, every frame at or above
that work-item id carries the section.** The row is read by the same reader
as `Ledger frozen from`: absent means presence is not checked, and a value
that is not an id is refused naming the row. A frame below the cutoff is read
where the section is present and not required. `templates/config.md`
documents the row, and this repository's value is the second it was written,
so no work item framed before it is bound.
Enforced by: tests/test_a_record_states_what_the_tree_has.py::test_presence_is_required_at_or_above_the_cutoff, tests/test_a_released_row_is_read_again_in_a_fragment.py::test_a_removes_row_that_is_not_an_id_is_refused_in_the_freezes_shape

## What neither check can read

<!-- specs/1791384152-a-reader-declares-its-input-class -->
**Seven things pass both checks, and the reviewer is the reader of each.**
Stated so nobody meets the edge by surprise:

1. A false declaration: `nothing` on a unit reading through a call K1 does
   not list, or `owned` on a unit that guesses.
2. A unit inside `tests/test_*.py`. Widening is one exclusion deleted.
3. A reader outside Python: `bin/`, a workflow's shell steps, a `sh -c`
   string inside a Python call.
4. A module-level read through a call K1 does not list.
5. A stale line: a reader redesigned from `guess` to `owned` keeps its old
   line until somebody moves it, as nothing re-reads an `Enforced by:` target.
6. A census line put back by hand.
7. A `## Removes` coordinate that never existed: the arm reads HEAD, and a
   misspelled Python name reads as a removal that happened.

Enforced by: nothing — each is the warden's reading of the diff at review, which is where a `Reads:` line and a `## Removes` row are argued

## The counts at landing

The reading of one moment, not a pin: 1,587 population units at the build's
tree, 632 of them calling a K1 primitive as K1 stands after its first review
(621 by the list as framed) and 194 with no docstring; two
module bodies K1 selects; 1,683 non-test top-level functions inside the test
modules, out by the file-name rule. Every one of the 1,587 started on the
census. 943 of them carry 2,392 anchors in the released ledger files and 247
carry 691 in the live fragments, which is what a docstring line written on
each would drift. Read at 2fc65bea, the tree every sibling of #835 left.
