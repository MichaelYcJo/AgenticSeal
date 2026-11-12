# Phase 2: 1794465690-a-passing-release-note-reads-like-a-failure

## What this phase found

**The frame holds for the colours.** At `e870dec22`, `badge` read `BADGE_VALUE_COLOUR` and `BADGE_LABEL_COLOUR` (`publish_release_note.py:674-675`), and the comment above them still read the two reds from `assets/seals/owl.svg`. That file holds `#8e0c12` once, as the wax gradient's outer stop, and `#d42420` once, as the relief's fill (executed: `grep -o` over the file). The twelve labels of `frame/design.md` G8 are the ones `release_seal.py#results` and `publish_release_note.py#count_badges` hand to `badge` (read). `git grep` over the tree for `d42420`, `8e0c12`, `labelColor`, the two constant names, "seal's reds", "dark red", "bright red" and "two reds" found the colours stated in the two scripts, the two test files, `owl.svg` itself and `docs/releasing/branch-and-release.md:97`. That last one is `## Rule changes`' third operation, for the settle. `release_seal.py` stated no colour. This list is a sample: it was built by searching for words, and the words were the ones above.

**One table of the labels whose colours differ, and one pair for every other label.** `BADGE_COLOURS` maps `SEALED`, `suite`, `skipped`, `capped` and `deferred` to `(value colour, label colour)`. `BADGE_DEFAULT_COLOURS` is blue on grey for every other label, and `badge` reads `BADGE_COLOURS.get(label, BADGE_DEFAULT_COLOURS)`. The grey of the labels is one constant, `BADGE_LABEL_GREY`, so the five grey labels state it once. Judged against `frame/plan.md` *Alternatives considered* A9, the chosen row, and `frame/design.md` *Scope* item 4. The comment that reads the reds from `owl.svg` now stands on the `SEALED` entry, as the *Removes* row for the pair of constants says. The value never decides the colours, so a `not read` keeps its label's colours. That answers the third judgment `frame/questions.md` lists above its table, by A9.

**One case holds the colours of every label, one parameter per label.** `frame/design.md` S4's *Verifiable how* cell names "a case per colour class". The phase built one case, `tests/github/test_publish_release_note.py#test_a_badge_takes_its_two_colours_from_its_label`, with a parameter for each of the twelve labels of G8. Each parameter asks `badge` for that label with the value `not read` and compares the address's colour field and its `labelColor` with the colours the label takes. The parameters cover every class: `SEALED`, `suite`, the three grey labels, and seven blue labels. A label with no entry is held by the existing case `#test_a_badge_spells_its_label_and_value_as_the_service_reads_them`, whose label `a-b_c d` now reads blue on grey. Judged against the crafter's rule *A new test starts from its group*. `seal layout --pairs` over the two test files named 0 pairs. The group of `badge` is the spelling case and the whole-string cases of the sealed header. In `test_publish_release_note.py` those whole strings hold neither `review`, `work items` nor `deferred`, nor any label with the value `not read` but `capped`. So the new case covers what its group did not, and a separate case for each class would have repeated its body five times.

**The test helpers take the colours as an argument.** In both test files, `badge(path, alt, colours=BLUE)` now writes the colours it is given, and `SEAL_RED`, `GREEN`, `GREY` and `BLUE` name the four pairs. `BADGE_LINES` passes the colour of each badge whose label has its own. So the whole-string cases of S2, S3 and S5 now pin each badge's colours as well as its text.

**Seen red before the code.** With the cases and helpers in place and `badge` still reading the one pair, this command failed 21 cases and passed 104:

`bin/test tests/github/test_publish_release_note.py tests/github/test_release_seal.py -q -p no:xdist`

The failures were the S2 and S3 cases, the spelling case, eleven of the twelve parameters of the new case, the S5 case with the image, and the six parameters of the S5 case without it. The `SEALED` parameter passed, because `SEALED` keeps the two reds the old pair gave every label. Its red came from the mutation run below. With the code written, the same command passed 125.

**Mutation, after commit `bb2562f70`.** Every run's verdict was `red`, and no mutant survived. The cases were `-k colours_from_its_label` in `tests/github/test_publish_release_note.py`, unless the row names others.

| Break | Cases run | Verdict |
|---|---|---|
| the `SEALED` entry removed, so it takes the default | the new case | red, at the `SEALED` parameter alone |
| `suite`'s value grey in place of green | the new case | red, at the `suite` parameter alone |
| `skipped`'s value blue | the new case | red |
| `capped`'s value blue | the new case | red |
| `deferred`'s value blue | the new case | red |
| `BADGE_LABEL_GREY` the seal's dark red | the new case | red, at eleven parameters, every one but `SEALED` |
| `BADGE_DEFAULT_COLOURS`' value the seal's bright red | the new case | red |
| the same break | the spelling case (`-k spells_its_label`) | red |
| `badge` looks up the value in place of the label | the new case | red, at the five labels that have an entry |
| `deferred`'s value blue | `tests/github/test_release_seal.py -k replaces_its_header` | red |
| `BADGE_DEFAULT_COLOURS`' value grey | `tests/github/test_release_seal.py -k other_than_yes` | red |

**A docstring commit after the code.** Reading the range against HEAD found that `release_seal.py#results`' docstring held one line of 108 characters, which phase 1's correction at `d5d029827` left when it rejoined the paragraph. Commit `66cfb82b0` rewraps it and adds that each badge's colours are `publish_release_note.py#badge`'s, read by its label, so a reader of `results` does not look for colours there. It changes no code: `ruff check` and `ruff format --check` passed over the file, and it parses.

**Phase boundary.** The set is the two test files, `tests/text` and `tests/behaviour`, as in phase 1, because no other test file reads either script and `CONTRIBUTING.md` names those two directories as the tree-wide files.
