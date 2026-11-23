# Guarantee: 1795390622-the-root-places-omit-agentic-seal

The audit read the tree at `16938f6d7`. The base `release/v0.38.6` resolved
through `release/v0.38.6@{upstream}` to `c22d58982` (executed,
`git rev-parse --verify --quiet`). The local `release/v0.38.6` stands at
`641b6bfb5`, so it was not used.

`trail/gate.md` records `run: ede9a12b6 against c22d58982`. `ede9a12b6` is an
ancestor of HEAD. The one commit after it outside the base, `16938f6d7`,
touches only `seal/threads/1795390622-the-root-places-omit-agentic-seal/trail/gate.md`
(executed, `git log --no-merges --name-only ede9a12b6..HEAD ^c22d58982`).
`seal pr-body <item> --body <body file> --check` exited 0 under both the
installed plugin's `seal` and the tree's `bin/seal` (executed).

The merge `ede9a12b6` brought nothing of its own into the branch's change.
Outside the work item's directory, `git diff c22d58982 HEAD` matches
`git diff 641b6bfb5 f7e4f8aa3` line for line once the `index` and `@@`
lines are set aside (executed). `f7e4f8aa3` is the target round 3 read, so
every line of the change outside the records was read by a round.

## Claims re-run

The `seen red` claims were re-run in a clone under the sealer's scratch
directory. The clone was at HEAD with the 24 changed files outside `tests/`
and `seal/threads/` restored from `c22d58982`. The mutants were run in the
same clone after HEAD was restored, through `bin/seal mutate`, and
`git status --short` printed nothing after each one. The tree under audit
was not changed.

| Claim | Source | Command | Result |
|---|---|---|---|
| Row 24 (where the records root is found) fails against the old text: the core names neither `<repo>/seal/`, the common-dir path nor `lib/optin.py#home_at`, and the link case fails at `skills/implement/orchestration.md` | `trail/phases/phase-1.md` *The new `RULES` row was red before the text moved* | `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py -q -p no:xdist -rf`, base text restored | holds (executed): the owner case fails naming those three facts, and the link case fails naming `skills/implement/orchestration.md` |
| The `agentic-seal/` fact of row 24 fails with that fact alone taken out of the core | `trail/phases/phase-1.md`, the core's four facts | `bin/seal mutate skills/core/SKILL.md --replace '`agentic-seal/` beside it' '`agentic/` beside it' --tests '... -k "owner_states_the_rule and 24"'` | holds (executed): 1 failed, `assert not ['`agentic-seal/`']` |
| Rows 25 and 26 fail against the old text, row 25 naming `trail/phases/phase-N.md` and row 26 naming its spellings | `trail/phases/phase-2.md` *Both new rows were red before the text moved* | the same run, base text restored | holds (executed): row 25 names `trail/phases/phase-N.md`, and row 26 names all five of its spellings, the one round 2's fix pass added among them |
| Rows 27, 28 and 29 fail, the row 28 link fails, and `test_no_document_leaves_the_base_reading_as_the_ref_you_typed` fails naming `docs/running/the-broad-gate.md`; row 16 passes at the base | `trail/phases/phase-3.md` *The new rows were red before the text moved* | the same run, base text restored | holds (executed): each fails naming its owner or carrier, and row 16's owner case passes |
| The sealer case's rewritten `readers` table fails against the old label **New?** | `trail/phases/phase-3.md`, the sealer case | the same run, base text restored | holds (executed): `skills/verify/orchestration.md does not name `new?`` |
| Row 29 fails with `## Removes` alone taken out of the agent-set paragraph (at the base the paragraph already held it, so the base run cannot show this one) | `trail/phases/phase-3.md`, row 29 | `bin/seal mutate docs/running/the-agent-set.md --replace '`## Removes`' '`Removes`' --tests '... -k "owner_states_the_rule and 29"'` | holds (executed): 1 failed, `assert not ['`## Removes`']` |
| Every citation of the template's absent-key paragraph is held by the citation case | `trail/phases/phase-2.md` *The six citations of the paragraph are held by the citation case* | `bin/seal mutate templates/setup/config.md --replace '**An absent language key is a refusal at the pull request body' '**An absent language key is a rejection at the pull request body' --tests 'bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist'` | holds (executed): red, naming seven citations at HEAD, the phase's six and `skills/implement/bootstrap.md:142`, which round 2's fix pass added |
| The modules the plan's three rows name pass at HEAD | `frame/plan.md` *Phases*, Verified by cells | `bin/test` over the 16 modules of those cells and the two that hold the core's citation of *Document layout* | holds (executed): exit 0, 424 passed |
| `bin/seal rules --check` exits 0 | `trail/phases/phase-3.md` *The searches and the rules check* | `bin/seal rules --check` at HEAD | holds (executed): "all 175 check lines in 67 rule files hold", exit 0 |
| `seal/README.md` is byte-identical to its template | `frame/design.md` G21 | `diff seal/README.md templates/setup/seal-README.md` | holds (executed): no output, exit 0 |
| Removes: the registry document and its index row | `frame/design.md` *Removes* | `ls docs/forms/the-reader-registry.md`; `git grep -n 'reader-registry' -- ':!seal/threads'` | holds (executed): no file, and the search exits 1 |
| Removes: rule 11 spells no place and drops "A repository with both is shared" | `frame/design.md` *Removes*, row 1 | rule 11 read at HEAD; `git grep -n 'with both is shared' -- ':!seal/threads'` | holds (read; executed): rule 11 cites the core's paragraph, and the search prints nothing |
| Removes: the policy sentence names the core, not rule 11 | `frame/design.md` *Removes*, row 3 | `git grep -n 'rule 11'` over `docs/layout/one-root-by-lifetime.md` and its `.ko.md` pair | holds (executed): no hit, and `:27-28` names the core's opening paragraph (read) |
| Removes: the ways a key is absent stand only in the template's paragraph | `frame/design.md` *Removes*, row 5; S4 | `git grep -n -F 'no such key' -- skills agents templates docs ':!*.py'` | holds (executed): `templates/setup/config.md:32`, the paragraph, and `:211`, the `seal mode` line S4 keeps |
| Removes: the `Reframed` line is spelt only in *The run* | `frame/design.md` *Removes*; S5 | `git grep -n -e 'Reframed <date>' -e 'Reframed …' -- ':!seal/threads'` | holds (executed): `docs/running/the-run.md:19`, the message in `chain_check.py`, the case's frame in `tests/skills/test_chain_check.py` and the `RULES` fact, the four S5 names |
| Removes: the base order and the gate's words stand outside their owners only where `gaps.md` names them | `frame/design.md` *Removes*; `gaps.md` *Not done* | `git grep -n -F` on `origin/<base>`, `@{upstream}`, `` `new?` `` and `failing on base too` over the shipped roots | holds (executed): the owners, `agents/sealer.md:44` (out of scope), `skills/code-review/orchestration.md:480` and `docs/running/what-a-script-gates.md:57` (both in `gaps.md`), and the crafter's act at `agents/crafter.md:150-151` |
| Removes: the cases that held a copy are gone | `frame/design.md` *Removes*, last row | `git grep -n` on the four removed case names over `tests/` | holds (executed): exit 1. `DESCRIBES_THE_BASE` reads `(POLICY,)` (read) |
| The root's places outside the core are cited, not spelt | issue *Done when*, item 1 | `git grep -n -F -e '<repo>/seal' -e 'common-dir)/seal' -e 'two places' -e 'either place'` over the shipped roots, each hit read | holds (executed; read): each remaining hit names a mode's place, counts the shared and the local root as `lib/optin.py#home_paths` does, or is the core itself. Round 1 judged the same hits on that ground |
| The core names the three places in the order `lib/optin.py#home_at` reads them | `frame/design.md` *Scope* item 1 | `skills/core/SKILL.md:18-32` and `lib/optin.py:280-319` read at HEAD | holds (read) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Each of the issue's five facts gets one owner, and every other statement cites it. The core's opening paragraph owns the root's places. No code under `lib/`, `skills/*/scripts/` or `hooks/` changes (D2). The `## Removes` rows list what leaves | the issue's *Direction* and *Done when*; the diff; the claims above | none |
| the build | Three phases, at `222b5b5b5`, `7aa027aaf` and `30a0b05ef`, each with its `trail/phases/phase-N.md`. Each departure from the frame is written with its grounds | the design (the diff stat shows no file under `lib/`, `skills/*/scripts/` or `hooks/`); the claims re-run above | none |
| the last round | Round 3, a verifying round over `69d2700cf..f7e4f8aa3`, with one `should` finding located in `changelog.md` and `frame/design.md` alone, closed `fixed 6b2fa3a54` | `6b2fa3a54` touches only `changelog.md`, `frame/design.md`, `frame/plan.md` and `pr.md` of the work item (executed, `git show --stat`). The text at HEAD is the finding's paste-ready text word for word: `changelog.md` item 3's new sentence, process row 2's Change and Why clauses, G11's added sentence and `:121-123`, and the *Removes* row's `:121-123` (executed, `git show --word-diff`) | none |
| the changelog | Eight `Changed` items, one `Removed` item and five process rows, one for each fact. Five policy files keep their sentence on the absent key's refusal | the diff; `gaps.md` *Not done*, which names the same five policy files and the commit skill's lead; the round 3 fix | none |
| the orchestrator's part of the pull request body | `pr.md`: three quotes and `Closes #1578` | Each quote stands word for word at its coordinate: `frame/plan.md` *Judgments of the run*, the row on the title's prefix, its Judgment and Grounds cells, and `routing.md` *Why this way*, the Branch item (read) | none |
| `routing.md` *Why this way*, the orchestrator's account under `agentic` | A work item rewriting text every agent acts on, built by a crafter, reviewed through the chain, under automation | The diff is that kind of change: rule and policy text, the cases that hold it, and no code, hook or workflow (executed, the diff stat). `Implementation` reads `crafter`, and every phase whose Status cell holds a commit has its record. The grounds' "about a dozen files" was an estimate made before the first edit. The diff touches 24 rule and policy files and 9 test modules, so the estimate is low, and the larger count does not weaken the crafter route it argued for | none |
| `frame/plan.md` *Judgments of the run*, the stop row | The run ends at round 3, and no round follows the records-only fix, because its reader is the sealer | `docs/running/the-run.md:8` says a fix pass is followed by no round where its reader is the sealer. The core's row *No fix that no round reads* admits a fix that touched the work item's records alone, closing a finding located there alone. Both hold for `6b2fa3a54` | none |

The full suite at HEAD is the broad run's. `trail/gate.md` records its
commit. Its counts, 5700 passed and 9 skipped, are the spawn prompt's
statement, and the record does not hold them (`unverified` by the sealer;
the orchestrator answers). No `seal/parity.json` is carried, so no
comparison with an original is owed.

```seal
target: 16938f6d7f8ecfa15b5511436bf156d2366dc7d0 against c22d589829c1e216f824ac3d4d5ffb882efb8b64
Verdict: sealed
```
