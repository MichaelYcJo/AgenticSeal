# Review round 1: 1793171929-the-suite-tells-the-agent-it-is-evaluated

target: 86c9496b against c825fd2c

## Findings

### 1. A replay or seeded case that drifted from its generator is reported as holding the copied words, not as a stale case

severity: should
location: `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py:110-118`, `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py:132-135`, `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py:195`, `seal/threads/1793171929-the-suite-tells-the-agent-it-is-evaluated/gaps.md:27`
evidence: executed `python -c "T.hits('<scratch>/drift')"`
verdict: fixed efa93f62

Why it matters. The case exempts a value that a replay or seeded generator
copies from this repository's history. It finds those values by rendering
the generator's current text and matching the case file against it. Where
the case file no longer equals what the generator writes,
`copied_spans` returns no span, so every copied value is scanned as if the
generator had written it. The check then reports the copied words. It does
not report that the case is stale. A reader who acts on the report sees a
hit inside the asked paragraph, which `evals/README.md:91-102` calls
exempt. The fix the report points at is to reword text that came from a
record, or to edit a generated case by hand, which `evals/README.md:104`
forbids. The real fix is to write the case again with `--case NAME`.

Grounds. The probe copied `replay-1791382684-r2/prompt.md` to
`<scratch>/drift/proofer/replay-1791382684-r2/prompt.md`. In the copy it
changed one phrase of the generator's own text, "commit nothing yourself."
to "commit nothing.", and that phrase holds no refused word.
`hits` returned `[('proofer/replay-1791382684-r2/prompt.md', 5, 'judge')]`.
Line 5 is the asked paragraph the generator copied from the round record.
The drift is a real path. Nothing compares a replay or seeded case with its
generator (`frame/plan.md` *Technical context*, read). So a commit that
changes `replay_targets.py#prompt` or `seed_defects.py#prompt` and does not
regenerate the cases turns this case red with this message.

Claimed: `gaps.md:27` records under *Fed back into the spec* that "a
replay or seeded case file that is not its generator's text keeps no
exemption", as inferred during implementation. It cites the S5 case that
the same commit added. That is the account citing itself.
`frame/design.md` *Data & interfaces* exemption 2 says only that "the
generator's own template text in those cases is not exempt". It is silent
on a file the generator no longer writes. Removing the exemption is the
right choice. The defect is the report: it names the wrong cause.

```python
def copied_spans(text, generator, file_name):
    """The spans of TEXT that hold a value GENERATOR copied, where TEXT holds
    one of the texts it writes as FILE_NAME; None where it holds none."""
    for shape in rendered(generator, file_name):
        pattern, names = pattern_of(shape.strip())
        m = pattern.search(text)
        if m:
            return [m.span(i) for i, name in enumerate(names, 1) if name in COPIED]
    return None


# in hits(), in place of the loop at :132-135
        for prefix, generator in by_prefix.items():
            if case.startswith(prefix):
                spans = copied_spans(text, generator, os.path.basename(path))
                if spans is None:
                    # The generator no longer writes this file, so a word
                    # below may be a copied value: write the case again with
                    # `--case NAME` before rewording anything.
                    found.append(
                        (os.path.relpath(path, suite), 0, "not its generator's text")
                    )
                    spans = []
                for start, end in spans:
                    masked[start:end] = " " * (end - start)


# the S5 case's third reading, at :195
        (
            "not-the-generators-text",
            planted,
            real,
            [(0, "not its generator's text"), (1, "judged"), (5, "judge")],
        ),
```

The fix pass also rewrites the `gaps.md:27` clause to the new behaviour,
and the `hits` docstring to name the stale-case hit.

answer: The finding holds. `copied_spans` now returns `None` where no text its generator writes matches the file. `hits` then reports the file at line 0 with `STALE`, "not its generator's text: write the case again with `--case NAME`". That report comes before the file's words, which are still all scanned. The `hits` docstring names it (`efa93f62`). The S5 case's third reading now expects `(0, STALE)` before `(1, "judged")` and `(5, "judge")`. Against the old `hits` it went red, exit 1 (executed). After the fix, `bin/test tests/text/test_no_case_tells_the_agent_it_is_evaluated.py tests/evals/test_rule_cases.py -q` exited 0 with 16 passed (executed). `seal mutate` turned both new units red: dropping the `STALE` hit, and returning `[]` in place of `None` (executed). `gaps.md:27` now states the rule as it stands (`bc5388dc`). `git grep` found one other statement of the old rule, `trail/phases/phase-1.md:40`. It records what phase 1 built at `5ac41e48`, and a fix pass writes no phase record, so it stands.

## Confirmations

confirms: none
The 14 `rule-*` cases at HEAD equal `rule_cases.py`'s output byte for byte.
The four `seeded-*` cases equal `seed_defects.py --case` output byte for
byte, with `origin` set to the URL the frame names (executed: both
generators run into a scratch directory, then `diff -r` against each
committed case, every exit 0). The frame's grounding row "No case file is
edited by hand" holds for this branch.

confirms: none
S2 holds. The seeded scaffold case passed with `HOME` set to an empty
directory and `GIT_CONFIG_NOSYSTEM=1`. It also passed with a `HOME` whose
only config is `user.useConfigOnly = true` (executed, exit 0 both times).
The amend at `evals/scripts/seed_defects.py:313` sets no identity. Claimed
by the crafter at `trail/phases/phase-1.md` under *Q3*, and the claim
matches.

confirms: none
S4 was red at the base, as `trail/phases/phase-1.md` claims. The case's
`hits`, run over `c825fd2c`'s `evals/behaviour/` with `c825fd2c`'s
generators, found 128 hits in 23 files: 18 scaffolds and the 5 sealer
prompts (executed). Over HEAD's suite it finds 0.

confirms: none
S6 is seen red with the old prefix. With
`evals/scripts/noninferiority.py:611` set back to `prefix="agentic-eval-"`
in the scratch clone, the new *Test_run_side* case failed naming
`agentic-eval-16b9s5vm` (executed, exit 1; the line was restored and the
clone's diff read empty).

confirms: none
One author constant holds. `evals/scripts/rule_cases.py:84-85` defines
`AUTHOR` and `BY`, and every commit in the 14 rule scaffolds is the one
`BY` form (executed: 40 commit lines, all
`git -c user.name=textutil -c user.email=textutil@example.com commit -q -m`).
`EVIDENCE` at `:88` is read by `sealer_case` at `:667` and by
`tests/evals/test_rule_cases.py`. `git grep` for `agentic-eval`,
`user.name=eval` and `eval@example` finds them only in work item records
(executed).

confirms: none
The frame did not move after approval. `git diff d7cc30c9..HEAD` over
`frame/` changes only the two Status cells of `frame/plan.md` and Q3's
Status cell of `frame/questions.md` (executed).

confirms: none
The divergence in `gaps.md` holds. Phase 2's README sentence is grounded in
`frame/design.md` *Scope* item 6, which places the rule's statement in one
paragraph of `evals/README.md` (read `evals/README.md:91-102`).

confirms: none
The modules that read the files this branch changed pass, and so do the two
checks (executed). `git grep -l` over `tests/` for each changed path and
name chose 24 modules, run in one `bin/test` call: exit 0, 1196 passed.
`bin/seal layout --check` exited 0 with 0 refused. `bin/seal rules --check`
exited 0, all 266 check lines holding. `tests/behaviour/test_docs_line_wrap.py`
and `tests/skills/test_test_layout.py` were among the 24.

No fact was carried from an earlier round: this is round 1.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD. Not run here (contract rule 2); `gaps.md` labels them `unverified`, and that label is honest | the branch at `86c9496b` | the orchestrator, through `seal gate` |
| Whether a directory `claude plugin eval` makes itself holds a refused word: the clone the agent works in, which every rule prompt has it name through `git rev-parse --show-toplevel`, and the `--keep-temp` directories. S6 reads only the directory `run_side` makes | `evals/scripts/noninferiority.py:611-632` | the orchestrator, from one saved trace's working directory, with `questions.md` Q2 |
| The odds that `mkdtemp`'s eight random characters spell a stem: phase 2 computes about one run in 400,000 and did not measure it | `tests/evals/test_noninferiority.py:1307-1325` | nobody owes it at those odds; recorded so the next round does not re-derive it |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the 24 modules `git grep -l` chose, `-q` | exit 0, 1196 passed |
| `bin/seal layout --check`; `bin/seal rules --check` | exit 0, 160 files read, 0 refused; exit 0, all 266 check lines hold |
| `python evals/scripts/rule_cases.py --out <scratch>/regen-rule`, then `diff -r` per case | exit 0; 14 cases, no difference |
| `python evals/scripts/seed_defects.py --case` for the four seeded cases, `--out <scratch>/regen-seed`, then `diff -r` per case (the four orphaned targets fetched into the scratch clone first) | exit 0; four cases, each `diff -r` exit 0 |
| `HOME=<empty> GIT_CONFIG_NOSYSTEM=1 python -m pytest` on the seeded scaffold case, then again with `user.useConfigOnly = true` as the only config | exit 0, 1 passed, both runs |
| `python -c` calling `hits` over `c825fd2c`'s suite with `c825fd2c`'s generators, over a drifted copy of `replay-1791382684-r2`, and over HEAD's suite | 128 hits in 18 scaffolds and 5 sealer prompts; one hit, `judge` at line 5; 0 hits |
| `prefix="agentic-eval-"` set at `noninferiority.py:611` in the scratch clone, `bin/test tests/evals/test_noninferiority.py -k test_refuses_a_temporary_directory_whose_name`, then restored | exit 1, naming `agentic-eval-16b9s5vm`; clone diff empty after the restore |
