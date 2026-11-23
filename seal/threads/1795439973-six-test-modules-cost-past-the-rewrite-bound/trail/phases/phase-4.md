# Phase 4: 1795439973-six-test-modules-cost-past-the-rewrite-bound

## What this phase found

### The frame, read against the tree before the build

The frame holds for `tests/github/test_release_seal.py`, with one count it states loosely. Read at `5c3fc12fb`: `wired` stands at `:338`, and its default suite record is `recorded(tmp_path, {"passed": 7003, "skipped": 66})`. That record holds 7,069 `test` lines, one `session` line and one `end` line, so the frame's "7,069 lines" counts the `test` lines alone. `Test_main` stubs `gh`, `tagged` and the pull request list, as *Grounding* says, so no case of the module runs `gh` or a git command of its own. The one git process a case starts is the shipped `lib/optin.py#git_common_dir`, which `home_at` runs in the fixture directory for `mark_on` and for the routing reader.

### Q1: where `Test_main`'s seconds went before the rebuild

**On the Windows leg.** Run 45181872904's artifact puts the module at 95.2 s over 60 cases and `Test_main` at 88.8 s over 32 (executed: the sum by case over the artifact the framer downloaded). The 25 cases that cost 2 s or more hold 92.9 s, and each of them reads a record of thousands of `test` lines through `suite_counts`: 24 cases of `Test_main` over `wired`'s default record of 7,069, and `Test_suite_counts::test_accepts_the_record_and_reads_it_through_the_gates_reader` over its own record of 7,138. The other cases of `Test_main` cost 0.01 s to 0.15 s each. Each of them is refused before the reader counts a line of the default record, or reads a record of 10 or 11 `test` lines it names itself.

Two refusals split a case's seconds. `[gh pr list fails]` stops right after `suite_counts`, before `chain_counts`, `mark_on` and any `gh` call, and costs 2.47 s. `[the header is not there]` stops after all three and costs 2.65 s. `[the suite step failed]`, which writes the same record and stops before reading it, costs 0.11 s. So reading the record held about 2.3 s of each case that reached it, and the rest of `main` up to the header about 0.2 s.

The nine cases that run `main` to its end cost more than that. `test_accepts_a_published_note_and_replaces_its_header` and the six cases of `test_a_row_other_than_yes_attaches_nothing_and_puts_the_results_alone` cost 4.2 s to 4.9 s each, and the two cases of `test_a_second_run_finds_no_header_to_replace_and_writes_nothing`, which run `main` twice, cost 8.2 s and 9.3 s. They hold 48.9 s. The same nine read 47.6 s in run 45189798316 and 50.5 s in run 45203717820, so the pattern repeats (executed: the same sum over the two dispatch artifacts the orchestrator downloaded). On this macOS machine they cost what the refusals cost, about 0.25 s each. The phase did not find what the extra 1.7 s or so is on the leg. These nine come first in the file's order among the cases that read the record, and the refusals after them, so the place of a case in the shard's run is one reading, and no run here measured it. `gaps.md` *Not verified* hands the question to the orchestrator's run.

**On this macOS machine.** `bin/test tests/github/test_release_seal.py -q -p no:xdist --durations=0` at `5c3fc12fb` passed 60 cases in 7.14 s, and `Test_main`'s cases took 6.54 s of the 7.01 s the listed cases summed (executed). Under `cProfile`, `Test_main`'s 32 cases spent 11.3 s in their calls (executed: `python -m cProfile -m pytest ... -k Test_main`, `before-main.prof` in this phase's scratch). Of that, `broad_gate.read_record` took 7.1 s, 6.2 s of it in 183,836 calls of `broad_gate.record_path`, which resolves the line's path and the worktree with `os.path.realpath` for every `test` line. `recorded`, writing the records, took 2.9 s. The 100 git processes of `optin.git_common_dir` took 1.2 s. The profiler inflates the many small calls, so these are shares and not seconds of a plain run.

### What the rebuild changed

All of it is in `b4cab3e9c`, and `db5309a31` corrects the new comment's count to the record's `test` lines.

- **`wired` records `SUITE`, ten `test` lines.** `SUITE` counts 7 passed and 3 skipped. The two counts differ from each other and from every other count the header holds: 2 pull requests, 2 issues, 1 outside contributor, 1 round, 1 work item, 1 capped and 1 deferred. So a count put in another badge shows. `BADGE_LINES` carries the two badges as `suite-7%20passed` and `skipped-3`, and the dry run's case asserts the row `suite    7 passed, 3 skipped`.
- **`Test_suite_counts::test_accepts_the_record_and_reads_it_through_the_gates_reader` reads two sessions of 7 passed, 4 skipped and 2 xfailed, and 5 passed, 2 skipped and 1 xpassed.** It asserts `(12, 6)`. A reader of the first session alone gives `(7, 4)`, of the last alone `(5, 2)`, an xfail counted as a skip gives 8 skipped, and an xpass counted as a pass gives 13 passed, so the sum and the two categories it leaves out are held as before.
- **No case keeps a wide count, because no case's fact is a count's width.** The case of each class was read for it. The accepting and refusing cases of `Test_main` assert the header, the warning line, the upload and the edit. The dry run's case asserts that the rows and the note are printed. Where a value fits `PANEL_VALUE_WIDTH` and where a five-digit suite moves its skips to their own row is `Test_release_rows`' fact, over rows handed to `release_rows` directly, and `Test_module::test_the_results_are_the_stamps_rows_as_labelled_values` holds the split row in `results`. Those cases keep `7003` and `10003`, and they read no record.

The local figures after the rebuild are in the second part below. The figure that judges the phase is the Windows leg's, from the orchestrator's run at this phase's Status commit (`frame/design.md` S1).

### Departures from the frame

None. *Scope* item 4 asks for the smallest record that holds each case's fact, and the phase changed nothing else. Two costs stay, and `gaps.md` *Not done* names both:

- **The git processes of `optin.home_at`.** A case that reaches `mark_on` starts four `git rev-parse --git-common-dir` processes in its fixture directory, which is no repository (read from the profile: 28 calls over the seven cases of `test_accepts_a_published_note_and_replaces_its_header` and the row cases). On the leg they sit inside the 0.2 s that `[the header is not there]` costs past `[gh pr list fails]`.
- **No change to `tests/conftest.py` would cut this module's cost.** The module takes `ROOT`, `census_case`, `config_json`, `mark_root`, `symlink_or_skip` and `load_module` from it, and none of them starts a process (read: `tests/conftest.py`). Each costs the cases that call it a few files written or read. So the spawn's bar on that file cost this phase nothing.

### The four parts `CONTRIBUTING.md` *The test layout* asks of a rebuilt module

**1. The move check, and the mutation table.**

`bin/seal layout --moved 5c3fc12fb --from tests/github/test_release_seal.py --to tests/github/test_release_seal.py` exits 1 (executed). Its last line reads `seal layout: moved: 27 old cases, 59 items against 59 at 5c3fc12fb4b0, 9 failed`. Every case over `wired` names `SUITE` and a changed `wired`, and the two rewritten bodies stand for no old case. So the mutation table carries part 1.

The mutants sit at the decision points of every function of `.github/scripts/release_seal.py` a case reaches. All 68 ran in one call against `b4cab3e9c` (executed): `bin/seal mutate .github/scripts/release_seal.py --replace OLD NEW ... --tests "bin/test tests/github/test_release_seal.py -q -x"`, built by `run_mutants.py` from `mutants.py` in this phase's scratch. It printed `seal mutate: 68 mutants, 61 red, 7 SURVIVED, 0 with no verdict (72.4s)`. Under `-n auto`, `-x` stops the run with exit 2, which is the exit each red line shows. Mutant 1 run alone in file order exits 1 and fails `Test_release_rows`' two cases on their assertions (executed). `db5309a31` changes a comment alone, and the module passes at it (executed). Each row shows the lines the mutant changes, joined. The full OLD and NEW of each are in `mutants.py`.

The base column is filled for a survivor alone. The seven survivors ran again against the test file at `5c3fc12fb`, copied to `tests/github/test_tmp_release_seal_base.py` and removed after the run. That call printed `seal mutate: 7 mutants, 0 red, 7 SURVIVED, 0 with no verdict (50.6s)` (executed). So each survivor is a gap older than this phase, and the phase lost no fact that killed one. Why each lives:

- 28: no case gives `chain_counts` a round record it cannot open or decode.
- 30: no case's verdict other than `deferred` has a home that is exactly `#N`.
- 42: no case's icon path holds an empty segment, and a `.` segment names the same file once joined.
- 44: no case gives `draw` a file that opens with the PNG signature and holds no `IHDR` chunk or fewer than 24 bytes.
- 47: every case's tag is a `vX.Y.Z` tag.
- 57: no case's `gh release view` prints text that is not JSON.
- 68: no case's reason spans more than one line.

The phase adds no case for them, as phases 2 and 3 added none for theirs: the frame makes each case's record smaller and adds no fact (`frame/design.md` *Scope* item 4), and `agents/crafter.md` *Never* bars building beyond the request. `gaps.md` *Not done* names the seven.

| # | Unit | Old | New | New file | `5c3fc12fb` |
|---|---|---|---|---|---|
| 1 | `release_rows` | `if len(whole) <= PANEL_VALUE_WIDTH:` | `if len(whole) < PANEL_VALUE_WIDTH:` | red |  |
| 2 | `release_rows` | `if items is None or rounds is None` | `if items is None` | red |  |
| 3 | `release_rows` | `NOT_READ if capped is None or items is None else` | `NOT_READ if capped is None else` | red |  |
| 4 | `release_rows` | `if deferred is None` | `if False` | red |  |
| 5 | `release_rows` | `("tag", sha[:8]),` | `("tag", sha[:7]),` | red |  |
| 6 | `results` | `by[last].append(value)` | `pass` | red |  |
| 7 | `results` | `[("commit", tag[0]), *(("on", branch) for branch in tag[1:])],` | `[("commit", tag[0])],` | red |  |
| 8 | `results` | `if items == NOT_READ:` | `if False:` | red |  |
| 9 | `results` | `("capped", capped if capped == NOT_READ else capped.split()[0]),` | `("capped", capped),` | red |  |
| 10 | `results` | `lines = [[("suite", passed), ("skipped", skipped.split()[0])]]` | `lines = [[("suite", skipped.split()[0]), ("skipped", passed)]]` | red |  |
| 11 | `suite_counts` | `if not directory:` | `if False:` | red |  |
| 12 | `suite_counts` | `if not key:` | `if False:` | red |  |
| 13 | `suite_counts` | `if not record.sessions:` | `if False:` | red |  |
| 14 | `suite_counts` | `if record.unread:` | `if False:` | red |  |
| 15 | `suite_counts` | `if record.unended:` | `if False:` | red |  |
| 16 | `suite_counts` | `if record.unplaced:` | `if False:` | red |  |
| 17 | `suite_counts` | `if failed or errors:` | `if failed:` | red |  |
| 18 | `suite_counts` | `return record.counts.get("passed", 0), record.counts.get("skipped", 0)` | `return record.counts.get("skipped", 0), record.counts.get("passed", 0)` | red |  |
| 19 | `readers` | `return routing, chain` | `return chain, routing` | red |  |
| 20 | `labels_of` | `(label.get("name") if isinstance(label, dict) else str(label)) or ""` | `str(label) or ""` | red |  |
| 21 | `chain_counts` | `capped = sum(1 for pull in pulls if CAPPED_LABEL in labels_of(pull))` | `capped = 0` | red |  |
| 22 | `chain_counts` | `with sibling.going_on(): routing, chain = readers()` | `if True: routing, chain = readers()` | red |  |
| 23 | `chain_counts` | `except (Exception, SystemExit) as problem: # `Absent`'s path; an `ImportError` carries a `path` of its own. if isinstance` | `except Exception as problem: # `Absent`'s path; an `ImportError` carries a `path` of its own. if isinstance` | red |  |
| 24 | `chain_counts` | `if isinstance(problem, SystemExit) and getattr(problem, "path", None):` | `if False:` | red |  |
| 25 | `chain_counts` | `if not routing.declarations(root):` | `if False:` | red |  |
| 26 | `chain_counts` | `if CAPPED_LABEL in labels_of(pull): lost.append` | `if False: lost.append` | red |  |
| 27 | `chain_counts` | `if routing.rounds_unreadable(item):` | `if False:` | red |  |
| 28 | `chain_counts` | `except (OSError, UnicodeDecodeError): unread.append(path)` | `except (OSError, UnicodeDecodeError): pass` | survived | survived |
| 29 | `chain_counts` | `if errors: unread.append(path)` | `if False: unread.append(path)` | red |  |
| 30 | `chain_counts` | `issue = chain.issue_of(home) if kind == chain.DEFERRED else None` | `issue = chain.issue_of(home)` | survived | survived |
| 31 | `chain_counts` | `if lost:` | `if False:` | red |  |
| 32 | `chain_counts` | `return items, None if rounds_unread else rounds, capped, None` | `return items, rounds, capped, None` | red |  |
| 33 | `mark_on` | `home = module("lib/optin.py").home_at(root)` | `home = root` | red |  |
| 34 | `mark_on` | `return module("lib/config.py").switch(home, MARK_KEY, NO_IMAGE)` | `return module("lib/config.py").switch(home, MARK_KEY, "")` | red |  |
| 35 | `gh` | `out = gitcmd.gh(*args) except gitcmd.Failed as failed:` | `out = gitcmd.gh(*args) except ImportError as failed:` | red |  |
| 36 | `gh` | `if out.returncode: raise Refused(f"gh` | `if False: raise Refused(f"gh` | red |  |
| 37 | `tagged` | `out = gitcmd.git(os.curdir, "rev-parse", f"{tag}^{{commit}}") except gitcmd.Failed as failed:` | `out = gitcmd.git(os.curdir, "rev-parse", f"{tag}^{{commit}}") except ImportError as failed:` | red |  |
| 38 | `tagged` | `if out.returncode: raise Refused(f"git rev-parse` | `if False: raise Refused(f"git rev-parse` | red |  |
| 39 | `tagged` | `return out.stdout.strip()` | `return out.stdout` | red |  |
| 40 | `draw` | `except (OSError, ValueError) as problem: raise Refused( f"the plugin's manifest` | `except OSError as problem: raise Refused( f"the plugin's manifest` | red |  |
| 41 | `draw` | `if not isinstance(icon, str) or not icon:` | `if False:` | red |  |
| 42 | `draw` | `ROOT, *(part for part in icon.split("/") if part not in ("", "."))` | `ROOT, *icon.split("/")` | survived | survived |
| 43 | `draw` | `except OSError as problem: raise Refused( f"the icon {icon} the manifest` | `except ValueError as problem: raise Refused( f"the icon {icon} the manifest` | red |  |
| 44 | `draw` | `if data[:8] != PNG_SIGNATURE or data[12:16] != b"IHDR" or len(data) < 24:` | `if data[:8] != PNG_SIGNATURE:` | survived | survived |
| 45 | `draw` | `except OSError as problem: raise Refused(f"the seal could not be written` | `except ValueError as problem: raise Refused(f"the seal could not be written` | red |  |
| 46 | `draw` | `return int.from_bytes(data[16:20], "big") // DENSITY` | `return int.from_bytes(data[20:24], "big") // DENSITY` | red |  |
| 47 | `seal_release` | `if version is None: raise Refused` | `if False: raise Refused` | survived | survived |
| 48 | `seal_release` | `if outcome and outcome != "success":` | `if False:` | red |  |
| 49 | `seal_release` | `except (OSError, ValueError) as problem: raise Refused(f"the suite's counts` | `except OSError as problem: raise Refused(f"the suite's counts` | red |  |
| 50 | `seal_release` | `if pulls is None:` | `if False:` | red |  |
| 51 | `seal_release` | `chain = chain_counts(ROOT, work)` | `chain = (None, None, None, None)` | red |  |
| 52 | `seal_release` | `len(work), len(closed), suite, chain)` | `len(work), len(closed), (0, 0), chain)` | red |  |
| 53 | `seal_release` | `print(f"{label:<8} {value}")` | `print(f"{label} {value}")` | red |  |
| 54 | `seal_release` | `if unread: print(IMAGE_WARNING + unread)` | `if False: print(IMAGE_WARNING + unread)` | red |  |
| 55 | `seal_release` | `if on: # The upload names` | `if True: # The upload names` | red |  |
| 56 | `seal_release` | `path = os.environ.get("SEAL_PNG") if dry else ""` | `path = ""` | red |  |
| 57 | `seal_release` | `except (ValueError, KeyError, TypeError) as problem:` | `except (KeyError, TypeError) as problem:` | survived | survived |
| 58 | `seal_release` | `if body.count(header) != 1:` | `if header not in body:` | red |  |
| 59 | `seal_release` | `if on: image =` | `if False: image =` | red |  |
| 60 | `seal_release` | `if dry: print("DRY_RUN -- nothing uploaded` | `if False: print("DRY_RUN -- nothing uploaded` | red |  |
| 61 | `seal_release` | `if not on: gh("release", "edit"` | `if False: gh("release", "edit"` | red |  |
| 62 | `seal_release` | `except Refused as problem: raise Refused( f"{problem}; {ASSET}` | `except ValueError as problem: raise Refused( f"{problem}; {ASSET}` | red |  |
| 63 | `main` | `dry = os.environ.get("DRY_RUN", "").strip() not in ("", "0", "false", "no")` | `dry = False` | red |  |
| 64 | `main` | `with sibling.going_on(): seal_release(tag, repo, dry)` | `if True: seal_release(tag, repo, dry)` | red |  |
| 65 | `main` | `except (Exception, SystemExit) as problem: if isinstance(problem, Refused):` | `except Exception as problem: if isinstance(problem, Refused):` | red |  |
| 66 | `main` | `if isinstance(problem, Refused): reason = str(problem)` | `if False: reason = str(problem)` | red |  |
| 67 | `main` | `elif isinstance(problem, SystemExit) and getattr(problem, "path", None):` | `elif False:` | red |  |
| 68 | `main` | `reason = " ".join(reason.split())` | `pass` | survived | survived |

**2. Cases and seconds, before and after, on this macOS machine.** The figures are local. `frame/design.md` *Grounding*, *What a figure of the Windows leg can show*, takes no local figure as evidence of a saving on the Windows leg. The module's Windows figure is the orchestrator's `workflow_dispatch` run at this phase's Status commit (`frame/design.md` S1).

| Measure | Before, `5c3fc12fb` | After, `b4cab3e9c` |
|---|---|---|
| Cases of the module | 60 | 60 |
| `bin/test tests/github/test_release_seal.py -q -p no:xdist`, the module | 7.14 s | 1.74 s |
| The same runs, `Test_main`'s cases | 6.54 s | 1.25 s |
| The same runs, a case of `Test_main` that reads `wired`'s default record | 0.20 s to 0.47 s | under 0.005 s to 0.10 s; 0.05 s for each case that reaches `mark_on` |
| `bin/test tests/github/test_release_seal.py -q`, under `-n auto` | not run | 0.85 s |
| `test` lines in `wired`'s default record | 7,069 | 10 |
| Windows leg, the module, from the three runs' `test-durations` artifacts | 95 s, 93 s and 96 s in runs 45181872904, 45189798316 and 45203717820 | not measured |

The per-case figures of both local runs are in this phase's scratch, `before-durations.txt` and `after-durations.txt`. A `-p no:xdist` run lists the cases of 0.005 s or more, and the sums above add those.

**Q2: the floor.** The phase gives no answer to Q2 for this module, since no local figure is evidence of the Windows leg. The module holds no case whose fact needs a real process, so nothing in it sets a floor. The orchestrator reads the module's figure at this phase's Status commit against the modules no phase changed in the same run, as `frame/design.md` *Grounding* says.

**3. The real-git cases kept.** None. The module ran no git command and no `gh` of its own at the base, and runs none now. `Test_main` stubs `gh`, `tagged` and the pull request list, and the two cases of `Test_module` that hold `gh` and `tagged` replace `subprocess.run`. The git processes a case still starts are the shipped `optin.home_at`'s, named under *Departures from the frame*.

**4. Old cases cut or rewritten.** No case was cut. Each case below was rewritten. Its name and its facts are as they were, and what changed is the suite record it reads.

- `Test_suite_counts::test_accepts_the_record_and_reads_it_through_the_gates_reader`: two sessions of 7,000 passed, 60 skipped and 2 xfailed, and 69 passed, 6 skipped and 1 xpassed, before. Two sessions of 7, 4 and 2, and 5, 2 and 1 now, and it asserts `(12, 6)` for `(7069, 66)`. Run alone against mutant 18, which swaps the two counts, it is red (executed).
- `Test_main::test_accepts_a_published_note_and_replaces_its_header` and the six cases of `test_a_row_other_than_yes_attaches_nothing_and_puts_the_results_alone`: `wired`'s record of 7,003 passed and 66 skipped before, `SUITE` now. Each asserts the same header with `BADGE_LINES`' suite badges carrying 7 and 3. Run alone against mutant 18, which swaps the two counts, and against mutant 10, which swaps the two badges, `test_accepts_a_published_note_and_replaces_its_header` is red (executed).
- `Test_main::test_a_dry_run_draws_and_prints_and_writes_nothing`: the same record change, and it asserts the row `suite    7 passed, 3 skipped` for `suite    7003 passed, 66 skipped`. Run alone against mutant 52, which drops the label column's width, it is red (executed).
- `Test_main::test_a_second_run_finds_no_header_to_replace_and_writes_nothing`, `test_a_hand_edited_note_is_left_alone_and_nothing_is_uploaded`, and the cases of `test_refuses_on_any_failure_and_leaves_the_note_as_published` that take `wired`'s default record: the same record change, and their assertions are unchanged. The refusal cases that name their own record, `[a line of the record did not parse]`, `[a session of the suite stopped part-way]`, `[the suite counts a failure]` and `[the suite counts an error]`, read the record they read before.

No case of the module reads a document's prose as its fact, and none waits for another module's rebuild.

### Checks at the phase's close

- `bin/test tests/github/test_release_seal.py -q -p no:xdist --durations=0` at `b4cab3e9c`'s tree: 60 passed in 1.74 s (executed, file order).
- `bin/test tests/github/test_release_seal.py -q`: 60 passed in 0.85 s at `b4cab3e9c`, and 60 passed in 1.18 s at `db5309a31` (executed, under `-n auto`).
- `bin/seal layout --check tests/github/test_release_seal.py`: exit 0, `seal layout: 1 files read, 0 refused, 0 declare no TARGET` (executed). It prints 10 `report:` lines, each a function of `release_seal.py` with no class of its own name. A report line refuses nothing, and the phase adds and removes no class.
- No other test file imports from the module. `tests/behaviour/test_the_release_seal_is_drawn.py` names it in its docstring alone (read), so *Scope* item 9 and S4 ask nothing of this phase.
- The *Phase boundary* set, `bin/test tests/github/test_release_seal.py tests/behaviour tests/text -q`: 935 passed, 9 skipped (executed, over this record's tree). Its six warnings name citations that other work items' pending rule changes correct.
- `uvx ruff format` and `uvx ruff check` over the changed file: clean (executed).
- The suite: `unverified`. The broad gate is the orchestrator's, once the review rounds settle.
