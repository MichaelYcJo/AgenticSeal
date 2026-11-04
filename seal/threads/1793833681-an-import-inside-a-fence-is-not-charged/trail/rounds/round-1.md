# Review round 1: 1793833681-an-import-inside-a-fence-is-not-charged

```seal
target: d43285f1 against release/v0.32.2
```

The round read `release/v0.32.2..d43285f1` (2ecb8d4b to d43285f1) in a `git clone --no-local` of the branch at d43285f1. No earlier round exists, so no fact is carried; every coordinate below was opened this round.

Stage 1 read the code against `frame/design.md` *Scope* 1 to 4, S1 to S8, *Data & interfaces*, *Out* and *Removes*, then `CONTRIBUTING.md` *The test layout*. Stage 2 walked the axes of `skills/code-review/SKILL.md`. It added two axes of this change: whether the shared scan's other readers move, and where the meter's reading parts from CommonMark and the harness. Authorization, query scope, state transitions and concurrency have no surface here: the meter is an offline reader of local files, and the diff adds no state machine, no shared write and no external call.

## Findings

### 1. A copy of the meter without `unverified_check.py` now exits 2 on a run with no flag, and no case holds that new failure path

```seal
severity: should
location: `tests/skills/test_payload_meter.py:1441`, `skills/verify/scripts/payload_meter.py:410`
evidence: executed a mutant in the round's clone that makes `imports_of` return nothing where `unverified_check.py` is missing, then `bin/test tests/skills/test_payload_meter.py -q -p no:xdist` (exit 0, 56 passed); executed the copy of `payload_meter.py`, `hooks/lib/core.py` and `hooks/lib/optin.py` with no flag and a `CLAUDE.md` (exit 2); read `skills/verify/scripts/payload_meter.py:410`, `skills/verify/scripts/payload_meter.py:59-63`, `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/changelog.md:3`
```

Why it matters: the diff adds a failure path, and the error-paths axis counts each one. `imports_of` now calls `_fence_rule()` for every file that exists (`skills/verify/scripts/payload_meter.py:410`). So a copy that has `hooks/lib/core.py` but not `unverified_check.py` exits 2 on a plain `--root` run, wherever either file of the `CLAUDE.md` pair exists. Before the diff, only `--sections` reached that exit. The module docstring (`:59-63`) and the changelog fragment (`changelog.md:3`) both tell a person about the new exit. The crafter's account says, as read and not run, that a no-flag copy "now exits 2 from `imports_of`" and that "no case runs it, because `_core()` comes first". This round ran that copy. It exited 2 with the new sentence, so the claim holds. The round then ran a mutant that fails open: `imports_of` returns `[]` where the sibling is missing, which is the old silent reading in a worse form. The whole meter module stayed green under it, 56 passed. The copy-alone case (`tests/skills/test_payload_meter.py:1441`) builds a plugin with nothing but the script, so `_core()` refuses first on its no-flag row, and its `unverified_check.py` row runs under `--sections` only. Contract rule 14 asks that a change a person sees be pinned, and the `--sections` row pins the sentence but not this path.

The fix adds one case to `Test_module`, after `test_a_script_copied_alone_exits_2_and_names_what_it_misses`. Its precondition is that `hooks/lib/core.py` loads only `hooks/lib/optin.py` beside it (`hooks/lib/core.py:31`), which held for the run above. Every name in it is in the test module at d43285f1. The fix pass shows the case red under the mutant above before it commits it (contract rule 15).

```python
    def test_a_copy_without_the_scan_exits_2_on_a_run_that_reads_a_claude_md(
        self, tmp_path
    ):
        """#1185. Every read of a `CLAUDE.md` that exists asks
        `unverified_check.py` where its live text is, so a copy that holds the
        core hook's module and not that sibling exits 2 with no flag at all,
        and its sentence names the import reading."""
        alone = tmp_path / "alone"
        for rel in (TARGET, "hooks/lib/core.py", "hooks/lib/optin.py"):
            copy = alone.joinpath(*rel.split("/"))
            copy.parent.mkdir(parents=True, exist_ok=True)
            with open(os.path.join(ROOT, *rel.split("/")), encoding="utf-8") as f:
                copy.write_text(f.read(), encoding="utf-8")
        repo = tmp_path / "repo"
        repo.mkdir()
        (repo / "CLAUDE.md").write_text("# rules\n", encoding="utf-8")
        home = tmp_path / "home"
        home.mkdir()
        done = subprocess.run(
            [sys.executable, str(alone.joinpath(*TARGET.split("/"))), "--root", str(repo)],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            env=dict(os.environ, HOME=str(home), USERPROFILE=str(home)),
            cwd=str(repo),
        )
        assert done.returncode == 2, (done.returncode, done.stderr)
        assert "Traceback" not in done.stderr, done.stderr
        assert names_path(str(alone), done.stderr), done.stderr
        assert "no import of a `CLAUDE.md` can be read" in done.stderr, done.stderr
```

The snippet leaves the frame's statements of this path to the orchestrator's fold. `frame/plan.md:34` says "A run with no `CLAUDE.md` that holds an `@` behaves as it does today", which a partial copy with a `CLAUDE.md` that holds no `@` now contradicts. `frame/design.md:58` says no exit code changes. The set of codes is unchanged, but where exit 2 is reached has changed.

### 2. `live_pieces` is a new public function of `unverified_check.py` with no `Test_live_pieces` class in that module's test file

```seal
severity: should
location: `tests/skills/test_unverified_check.py:692`, `skills/verify/scripts/unverified_check.py:351-364`
evidence: executed `bin/seal layout --check` in the round's clone (exit 0), which printed "report: skills/verify/scripts/unverified_check.py: function live_pieces has no class Test_live_pieces" and no other report line for that module; read `CONTRIBUTING.md:230-249`, `tests/skills/test_unverified_check.py:44`, `tests/skills/test_unverified_check.py:461`
```

Why it matters: `CONTRIBUTING.md` *The test layout* says a module's test file "holds one class per public top-level function of the module, `Test_<name>`", with an accepting case and a refusing case. `tests/skills/test_unverified_check.py:44` declares the module as its `TARGET`, and every other public function of the module has its class. `live_pieces` has none. The phase record calls `live_pieces` the public function and calls its docstring its contract (`trail/phases/phase-1.md`, *Names the build chose*). That contract says a fence's lines hold no piece, a lone backtick run stays inside its piece, and a span's backticks and a comment's delimiters stand in none. Today only `imports_of`'s cases in `tests/skills/test_payload_meter.py` reach it, and only through whether an `@` is read. A later reader of `live_pieces` inherits a contract that no case in its own module holds. The crafter's seven mutants on `unverified_check.py` ran over the meter's cases, so they show what `imports_of` observes, not the docstring's whole contract. For example, a comment opener kept inside a piece changes no import.

The fix adds the class before `class Test_live_lines` (`tests/skills/test_unverified_check.py:692`). The expected offsets were worked out by reading `_scan` (`unverified_check.py:367-447`), not by running them, so the fix pass runs the class, then shows each case red with one boundary of `_scan` mutated (contract rule 15).

```python
class Test_live_pieces:
    """#1185. The offsets of each line's live text, from the one scan
    `liveness` reads: a fence's lines hold no piece, a lone backtick run
    stays inside its piece, and a span's backticks and a comment's
    delimiters stand in none."""

    def test_accepts_the_text_around_a_span_and_a_comment_as_pieces(self):
        lines = ["a `x` b <!-- c --> d", "```", "@a.md", "```", "lone ` run"]
        assert UC.live_pieces(lines, spans_cross_lines=True) == [
            [(0, 2), (5, 8), (18, 20)],
            [],
            [],
            [],
            [(0, 10)],
        ]

    def test_refuses_the_text_a_span_or_a_comment_reaches_across_lines(self):
        span = ["Run `cat @a.md", "@a.md` then @b.md"]
        assert UC.live_pieces(span, spans_cross_lines=True) == [[(0, 4)], [(6, 17)]]
        comment = ["x <!-- open", "@a.md"]
        assert UC.live_pieces(comment, spans_cross_lines=True) == [[(0, 2)], []]
```

### 3. A comment opener that CommonMark reads as text hides every later import, and `imports_of`'s list of what it does not model leaves the shape out

```seal
severity: should
location: `skills/verify/scripts/payload_meter.py:377-406`
evidence: executed `bin/test tests/skills/test_tmp_round1_probe.py -q -s -p no:xdist` in the round's clone, its shapes case; read `skills/verify/scripts/unverified_check.py:420-423`, `skills/verify/scripts/unverified_check.py:536`, `hooks/lib/blocks.py:94`, `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/frame/design.md:11`, `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/frame/design.md:25`
```

Why it matters: the meter reports and gates nothing, so the cost is a payload row a person reads as missing when the harness loads that file. `_scan` opens a comment at any `<!--` in live text (`unverified_check.py:420-423`), and a comment nobody closed runs to the end of the file. CommonMark opens a comment block only at the start of a line. It reads an inline `<!--` with no `-->` after it as text. A comment block ends at the line that holds `-->`. The probe returned:

- `Use <!-- to open a comment.` then a blank line and `@b.md`: `[]`. The docs and the harness read `@b.md`. The harness reads an `@` in a text token (`frame/design.md:11`, G3).
- `<!-- a --> @b.md <!-- c` then a blank line and `@d.md`: `[("b.md",)]`. The comment block ends on its own line, so the harness reads `@d.md` as well.

The frame states the rule, "one nobody closed hides the rest of the file" (`frame/design.md:25`, *Scope* 1). Its ground, G3, is the harness skipping an HTML block token that holds no `-->`. That ground covers a comment block that opens a line, not an opener inside a paragraph or after a comment that closed on its line. So compliance holds, and the reading is still a misreading on this shape. The shared scan must not move (S7), so the repair is the sentence. The docstring's *What this does not model* (`payload_meter.py:395-406`) is the list a person reads to learn where the meter and the harness part, and it lacks this shape.

A second instance of the same class was found by reading `_scan` and was not run. Take `- ```` as a list item's first line, then `  @a.md`, then `  ````. `fence_opener` refuses the first line (`hooks/lib/blocks.py:94`). Its backtick run finds no partner, because `_paragraph_ends_at` stops at the third line, which is a fence opener (`unverified_check.py:536`). So the second line is read, which the docstring states. Then the third line, which closes the list item's fence in CommonMark, opens a fence for the meter, and every line below it is hidden up to the next fence line, or to the end of the file where none follows. The docstring says the meter reads the import inside such a fence. It does not say that the fence's closing line hides the lines below it.

The fix rewrites the docstring's last sentences in place. `frame/design.md` *Out*, first bullet, states the same list and is the orchestrator's to fold.

```python
    a fence behind `>` or a list marker, where the shared fence rule opens
    no fence; where that fence's closing line stands within three spaces of
    the margin, the rule reads it as an opener, which hides the lines below
    it up to the next fence line or the end of the file. A `<!--` hides the rest of the file wherever it
    stands in live text and no `-->` follows it, where CommonMark reads an
    opener inside a paragraph, or after a comment that closed on its line,
    as text, and the harness reads the imports below it. And it reads no
    import whose `@` follows a code span, a comment, emphasis or a link with
    no whitespace between them, where the harness can begin a text token
    with the `@`."""
```

## Confirmations

What matched: S7 holds beyond the existing cases. `liveness` at d43285f1 returned what it returned at 2ecb8d4b for every tracked `.md` file of the clone, 537 files and 38,437 lines, under all four combinations of `spans_cross_lines` and `comments` (executed: the probe's first case). That case failed, and the failure was in the probe: it compared two `live_lines` generator objects, which are never equal. `live_lines` (`unverified_check.py:572-640`) yields from two `liveness` calls and nothing else, so it is unchanged too (read). `heading_starts` is not in the diff (read). The flag in `_scan` (`unverified_check.py:384`) and every state change of the old loop are kept. The new code only adds the `start` and `pieces` bookkeeping (read).

What matched: `_scan`'s pieces hold their own invariants over the same corpus (executed: the probe's second case, 0 violations). The pieces of a line are in order and inside the line. A line that begins dead never has a piece at 0. A non-fence line that begins live and is not empty always opens with one.

What matched: the crafter's red claim. HEAD's `tests/skills/test_payload_meter.py` was run against 2ecb8d4b's two scripts with the crafter's `-k` words. It ended 13 failed and 6 passed (exit 1), and the 13 are S1 to S6 and the S8 row, each as the phase record lists. The guard case `test_accepts_an_import_after_a_backtick_its_paragraph_never_closes` went red with `_partner_ahead`'s answer replaced by True, on `assert [] == [('b.md',)]` (executed). The green claim matched: 449 passed over `tests/skills/test_payload_meter.py` and `tests/skills/test_unverified_check.py` (executed, exit 0). The mutation counts, 7 of 7 and 4 of 4, were read and not re-run, apart from the one mutant above. A mutation score licenses *tested*, never *safe*. Finding 2 names part of `live_pieces`'s contract that those mutants could not see.

What matched: the probe's other shapes agree with *Scope* 1 and the docstring. An `@` after whitespace at the start of a piece is read, so the lookbehind sees the character before the piece. An `@` straight after a span is not read. A path ends where a span opens. A comment across lines inside a paragraph hides its `@a.md`. A `<!--` inside a fence or a span opens nothing. CRLF lines read as LF lines. `@a\` at the end of a line reads as `a`, which is the path group Claude Code uses (`frame/design.md:11`) (executed).

What matched: `tests/behaviour/test_release_hygiene.py` passes with the new `VERSIONS_OF_ANOTHER_PRODUCT` row (executed, 33 passed, exit 0). The row names `payload_meter.py` and `2.1.318`, and the docstring at `payload_meter.py:395` names that build.

What matched, against the implementer's account: the phase record claims every place *Scope* 4 lists was rewritten in place. The module docstring (`payload_meter.py:59-63`), the comment above `IMPORT` (`:115-123`), `_fence_rule`'s docstring and stderr sentence (`:166-185`), the copy-alone comment and purpose string (`tests/skills/test_payload_meter.py:1419-1429`) and the fence-rule readers comment (`unverified_check.py:98-117`) each state the new reading (read). Its sweep is called a sample by wording, and that label is honest. This round's `git grep` on `` `@` line `` and `` `@` lines `` outside `seal/threads/` listed the same hits the record names and leaves standing, with the reasons it gives (executed). The `liveness` hit outside the module and the tests, `skills/settle/scripts/rule_changes.py:33`, names it as a function loaded by path, which is still true (executed: `git grep -n liveness`).

What matched, against the orchestrator's fold, d43285f1: the sentence dating the frame's coordinates to 0611019b stands at the head of `frame/design.md` *Grounding* (`:5`) and `frame/plan.md` *Technical context* (`:5`). Each statement the second judgment row lists is rewritten in `frame/design.md` and matches a departure in `trail/phases/phase-1.md`. The third row gives the HTML comment bytes rung 4. `docs/running/the-run.md:50-55`, under `## The run`, gives rung 4 as "it names nobody", homed in "the round record alone, and the pull request body". The leftover is a frame *Out* item, not a round's finding, so the frame stands where the round record would. The pull request body naming it is still owed when the body is written, and the sealer reads that.

Duplicates were read against their group. `bin/seal layout --pairs` names four pairs inside `Test_imports_of` at d43285f1, all among the new cases, and none in `tests/skills/test_unverified_check.py` (executed). Each pair has equal bodies with different inputs: a fence, a span, a comment, and the lone-backtick guard. Each input reaches a different branch of `_scan`, so no case covers only what its group covers. S1's closed three-backtick fence takes the same path in `_scan` as S2's four-backtick case. The frame names S1 as its own acceptance row, so the round opens no finding for it. `CONTRIBUTING.md:285-288` counts a pair inside a class toward the threshold at which a module's tests are written anew. These four pairs bring `tests/skills/test_payload_meter.py` to that threshold when that module is next rebuilt.

## Not judged

| What | Location | Who answers |
|---|---|---|
| `frame/questions.md` Q1: whether the meter follows Claude Code's reader past the docs; the build used the default, the docs only | `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/frame/questions.md:16` | the owner |
| Whether G3's reading of the Claude Code 2.1.318 binary is right; no round can open the binary's minified functions again cheaply, and finding 3 rests on G3 only for the shape of a comment block | `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/frame/design.md:11` | the owner, where Q1 is answered |
| The full suite, the repository-wide lint and the format check at d43285f1, and the crafter's phase-boundary run of 38 modules, which this round did not re-run | `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/gaps.md` | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_payload_meter.py tests/skills/test_unverified_check.py -q -p no:xdist` at d43285f1 | exit 0, 449 passed |
| `tests/skills/test_tmp_round1_probe.py`, run once by `bin/test ... -q -s -p no:xdist`, then deleted | exit 1. `liveness` at d43285f1 and at 2ecb8d4b agreed on all 537 tracked `.md` files under the four readings; the failure was the probe comparing `live_lines` generators. 0 piece invariant violations. The shapes case printed each chain quoted in finding 3 and the Confirmations |
| HEAD's `tests/skills/test_payload_meter.py` over 2ecb8d4b's `payload_meter.py` and `unverified_check.py`, `-k "fence or span or comment or backslash or backtick or copied_alone"`, then both scripts restored to d43285f1 | exit 1, 13 failed and 6 passed |
| `_partner_ahead(lines, n + 1, width)` replaced by `True` in `_scan`, `-k test_accepts_an_import_after_a_backtick_its_paragraph_never_closes`, then restored | exit 1, 1 failed on `assert [] == [('b.md',)]` |
| `imports_of` made to return `[]` where `unverified_check.py` is missing, `bin/test tests/skills/test_payload_meter.py -q -p no:xdist`, then restored | exit 0, 56 passed: no case holds the no-flag exit 2 (finding 1) |
| a copy of `payload_meter.py`, `hooks/lib/core.py` and `hooks/lib/optin.py` alone, run with `--root` on a repository whose `CLAUDE.md` holds `# rules`, under a scratch home | exit 2; stderr names the missing `unverified_check.py` and "no import of a `CLAUDE.md` can be read" |
| `bin/seal layout --check` and `bin/seal layout --pairs` | exit 0 each; the `live_pieces` report line of finding 2 and the four pairs above |
| `bin/test tests/behaviour/test_release_hygiene.py -q -p no:xdist` | exit 0, 33 passed |
