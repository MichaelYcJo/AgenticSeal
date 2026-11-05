# Design: 1793853197-a-bare-commit-goes-or-states-its-reason

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "History goes to git, the release notes and the work record." A clause that says at which commit a case was seen red, or who measured a figure where, is history, and it goes. "A mechanism stays only while its record of what it caught outweighs what it costs", "A script holds a gate only on a fact it reads exactly" and "before a fix adapts to an existing structure, ask whether the structure should change" decide D2. "Nothing is kept beside the tree to stay in step with it, such as a stored count" decides D1 row 1 |
| `skills/core/SKILL.md` *The first value: efficient development through the workflow* (read) | A party pays for every byte of a file it opens. Whether a sentence holds grounds a reader acts on, or only provenance, is a judgment of meaning, which the proofer reads. A script does not re-encode it as a grammar rule. D2's arm reads no meaning: it reads whether git resolves a token to a commit and whether a ref contains it |
| `skills/agent-contract/SKILL.md` rules 12 and 15 (read) | Rule 15 says a new case's red is shown "in the hand-back", which a phase record holds. A case's docstring that names the commit it was red at holds a second copy of that evidence. Rule 12 asks for the class by a method that makes the list whole, which the two measures below are |
| `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/* (read, lines 155 to 170) | "A bare commit is not read: a plan's Status cell and a round's `fixed` line name the branch's own commits by rule, and whether a sentence cites a bare commit as where a file was read is the reviewer's reading." Both grounds stand under `seal/`. Outside it, no file has a Status cell or a `fixed` line, and a commit no clone holds misdirects whatever the sentence meant. The same paragraph says the squash discards every commit a feature branch wrote, so a reader sent to one "finds no source". D2 changes the first sentence for files outside `seal/` (`## Rule changes`) |
| `tests/text/test_a_cited_commit_outlives_the_squash.py` (read whole) | `cited` reads `COMMIT_PATH` tokens in each tracked file `read_here` admits. `unreached` refuses a commit no `REACHING` ref contains, `main` or a release branch, local or remote-tracking, and judges nothing where no such ref stands. Every planted case builds its token from a commit it makes. The module docstring says "A bare commit is not read." |
| The form with a check against the form without one (read: #1355's `guarantee.md` and `frame/design.md` *Grounding*, the reachability row; executed: the reachability row below) | At `f93d70ea4`, `origin/main` reached all 10 commits the 25 `<commit>:<path>` lines cited, a form the squash case has refused when unreached since #1270. Of the 44 bare tokens D1 rewrites, 34 are reached by no remote ref. The class the case does not read is the class that accumulated dead pointers |
| `.github/workflows/test.yml:114-122` (read; what `fetch-depth: 0` fetches is `actions/checkout`'s documented behaviour, not run here) | The `pytest` job checks out with `fetch-depth: 0`, so it holds the remote-tracking `main` and release refs and every branch the remote holds, a pull request's own branch among them. The squash case's S3 docstring says the same of CI's refs. So a bare commit of a pull request's own branch resolves there and is reached by no `REACHING` ref |
| #1359 body and its one comment (executed: `gh issue view 1359 --repo MichaelYcJo/AgenticSeal --json body,comments`, 2026-11-05) | The body gives the dispositions, *Done when* and *Out of scope*: `seal/`, `<commit>:<path>` citations, tags. The comment, which the orchestrator could not fold into the body, says the count depends on the pattern, asks the frame to write its pattern down, and puts the two fixture literals #1355 kept among the tokens read. *Done when* reads "each token the frame's pattern reads" |
| `routing.md` (read, committed at `2a11993e`) | Planning framer, Implementation crafter, Review through the review chain, Destination open the pull request, Automation yes. Nobody can be asked anything during this run |
| #1355's records: `seal/threads/1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds/frame/design.md` D1 and D2, `frame/plan.md` A2 to A7, `trail/rounds/round-1.md` *Not judged*, `guarantee.md` (read) | D1's four dispositions, P, G, N and F, are this frame's, and F is answered here by D, below. D2 added no case for `<commit>:<path>`, because a spelling check moves the text and does not remove its cost. #1355's rows 5 and 11 already took a seen-red clause naming a commit out as rule 15's evidence, which a phase record holds. The guarantee left "51" `unverified`: five patterns gave 50 to 67 at `f93d70ea4` |
| M1, the commits that resolve (executed at `2a11993e`, whose tree outside `seal/` is `31558c76`'s): `git grep -I -ohP '\b[0-9a-f]{7,40}\b' -- . ':(exclude)seal/' \| sort -u`, then `git cat-file -e "<token>^{commit}"` for each | 6,500 distinct hex tokens, of which 49 resolve as commits in this clone's object store. Four of them are the 40-hex forms of four 8-hex ones, so the 49 tokens name 45 commits. A second pattern, `(?<![0-9A-Za-z])[0-9a-fA-F]{7,40}(?![0-9A-Za-z])`, which also reads a token beside `_` and in upper case, gives the same 49 (executed) |
| M2, the commits this clone no longer holds (executed, then each line read): `git grep -I -ohP '\b[0-9a-f]{7,12}\b' -- . ':(exclude)seal/' \| sort -u`, kept where the token holds a digit and a letter, less M1's tokens | 45 tokens. Read at each line, 12 name a commit of this repository: `8fb1fb5`, `7e44106`, `81888e2`, `589cf25`, `0e676e6`, `e01e1b12`, `7966a9f9`, `0d59003`, `6bbaa4d1`, `dc1b0d14`, `e51fd0b`, `5d51b319`. Each stands after "at", "against" or "on" in a sentence about a run. The other 33 name no commit. They are synthetic values such as `aaa1111`, `abc1234` and `deadbee0123`, the key type `ed25519`, the stamp's example values `c46fd2d` and `1e2bed9` (`skills/verify/scripts/seal_stamp.py:1436`), and `d8cac16f`, which `evals/behaviour/framer/rule-framer-generated-page/scaffold.sh:90` computes as a CRC32 of a page (read). Tokens of 13 to 39 hex are two, `0123456789abcdef` and `fedcba9876543210`, both synthetic (executed) |
| The class, M1 and M2 together | 61 tokens on 115 lines in 46 files, naming 57 commits. M1 alone depends on which objects a clone holds, so the count moves between clones and as `git gc` drops unreachable commits. That is why #1355's 51 and its sealer's 50 to 67 differ from 49 here. M2 is a judgment at each line and lists the 12 the object store lost. A commit spelled with digits alone or letters alone that this clone does not hold is read by neither, and that is the measure's one limit |
| Reachability (executed: `git for-each-ref --contains <token> refs/remotes/origin` for each of the 45 commits M1 lists; `git ls-remote origin refs/heads/main` equals local `origin/main`, `31558c76`) | 22 of the 45 are reached by no remote ref. The 12 M2 lists resolve nowhere. So 34 tokens send a reader in a fresh clone to a commit it does not hold. All 34 are rewritten by this work (D1). Every token D1 keeps as data is reached by `origin/main` |
| `evals/scripts/seed_defects.py:34` and `:108` (read) | A seeded case "keeps the name `seeded-<the squash commit's first 8 hex>`". The four `evals/behaviour/proofer/seeded-*` cases and `seeded-279a580b` in the tests are names the generator gives, so they are data |
| `skills/verify/SKILL.md`, the table under *The narrow command still has to be able to fail* (read) | A comment or docstring inside source is proved by "the module still imports". That is how S4 holds the rewrites |
| Policy on red evidence in a docstring (executed: `git grep -n -iE 'red how\|seen red (at\|against)\|docstring.{0,40}(red\|commit)\|bare commit'` over `skills`, `agents`, `docs`, `templates`, `CONTRIBUTING.md`, `CLAUDE.md`) | No document asks a case's docstring to say where it was seen red. The one hit on a bare commit is the layout sentence above |
| The five sibling work items of 0.32.4 (executed: `gh issue view` for #1352, #238 and #1381; `git grep` of M1 and M2's tokens in each file the spawn names) | No token stands in `hooks/dispatch.py` (#1381), `README.md` or `README.ko.md` (#1382), `tests/test_version_check.py` (#238) or `.github/scripts/roll_flow_measurement_issue.py` (#146). #1352's sentences in `tests/hooks/test_routing.py` say "commit gate", at lines 4, 7, 62, 109, 263, 414, 533 and 555. D1 row 23's line 493 is not one of them, so this work names it. #1381 may add a case to `tests/hooks/test_dispatch.py`. Its issue changes `merge`, and neither of D1 rows 21 and 22 describes `merge`'s `allow`, so its edit removes neither sentence. `tests/github/test_roll_flow_measurement_issue.py:586`, D1 row 19, is the test module and not #146's script |
| `seal/follow-up.md` (read) | No row waits on this work. Its own commit citations stand under `seal/`, which is out of scope |
| Process changes (executed: `gh release view --repo MichaelYcJo/AgenticSeal --json tagName,body` gives `v0.32.3`, whose body holds no `### Process changes`; `grep` of the heading's rows over `seal/threads/*/changelog.md`) | Ten fragments hold the table. #1317's rows (`1793750411-rule-text-carries-no-history`) took history out of rule text, and a row of 2026-11-04 dropped from `skills/verify/orchestration.md` how a reading was measured on one machine. This work applies the same direction to code comments and test docstrings. No row changes how a commit is cited |
| Pending rule changes (executed: `grep -n 'file: docs/layout/the-record-layout.md'` over `seal/threads/*/frame/design.md`) | The one pending operation on that file is `1793732301-the-readme-is-written-for-a-first-reader`'s, in *The root records*. None touches *seal/threads/<work-item-id>/* |

**D1. Each of the 115 lines takes one of four dispositions, read for what its reader acts on today.**

- **P, provenance.** The clause names the commit a case was seen red or green at, or who found or measured something at a commit. The clause holding the token goes, and so does each sentence of the same paragraph that only makes sense with it, such as "the output is in the body of the commit that added this file". Where the clause also says what the earlier code did and the docstring states nowhere else what the case refuses, that half stays in present terms, with no moment named.
- **G, grounds.** The token stands beside the grounds of a behaviour the case holds. The grounds stay in one sentence. Where `gh` shows that an issue's page holds them, `#N` replaces the commit.
- **N, present.** The sentence needs the past to be read. It is rewritten to say in the present what the case or the constant holds.
- **D, data.** The token is a case's input, a generated name or a commit a scaffold fetches. It stays as it is. Each D row says why the reason is already plain at its line, so no comment is added.

#1355's F, a fixture built when its case runs, is not used. The tokens #1355 built that way are bare literals now (rows 45 and 46), and their cases read their value and not a commit.

| # | Lines at `31558c76` | Token | Disposition | What the rewrite leaves |
|---|---|---|---|---|
| 1 | `.github/workflows/test.yml:78` | `5623d728` | P | The dash clause, "12,819 on each at `5623d728`, in run 37580460950", goes. The sentence keeps that every leg collects the same cases. The count is a stored figure that drifts as cases are added |
| 2 | `skills/implement/scripts/seal.py:1216` | `8fb1fb5` | P | "(measured at `8fb1fb5`)" goes. What passed with both guards off stays |
| 3 | `skills/implement/scripts/seal.py:2191` | `55aea15d` | P | "(the sealer, at `55aea15d`)" goes. Git's refusal, quoted, is the grounds and stays |
| 4 | `tests/skills/test_seal.py:3330` | `55aea15d` | P | "The sealer at `55aea15d`:" goes. The fact after the colon is the docstring |
| 5 | `tests/behaviour/test_a_release_publishes_its_note.py:122` | `4134055a` | P | The clause naming the workflow at the commit goes, and the seen-red sentence at lines 119 to 123 still reads whole |
| 6 | `tests/behaviour/test_chain_hooks_hardening.py:91` | `5287dd42` | P | The seen-red sentence goes. What the tables lacked is stated in the present only if the docstring needs it |
| 7 | `tests/behaviour/test_chain_hooks_hardening.py:282` | `5623d728` | P | "Red against `5623d728`'s texts." goes |
| 8 | `tests/behaviour/test_first_setup_asks_once.py:15` | `7e44106` | P | The sentence at lines 15 to 17 goes, with "the output is in the body of the commit that added this file" |
| 9 | `tests/behaviour/test_first_setup_asks_once.py:142` | `81888e2` | P | The sentence at lines 141 to 143 goes |
| 10 | `tests/behaviour/test_first_setup_asks_once.py:668` | `589cf25` | P | "and the cases that read it were written against the block as it stood at 589cf25, each failing first" goes. The rest of the comment stays |
| 11 | `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:21` | `0e676e6` | P | The sentence at lines 21 to 23 goes |
| 12 | `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py:337` | `4edc5de6` | N | The comment says each line of `COMMENT_SHAPES` is a place a reading of fences or comments has had to be right, naming no work item and no commit. The section header at line 335, "the frame's shapes", is rewritten with it |
| 13 | `tests/block_shapes.py:12` | `4edc5de6` | N | The sentence at lines 11 to 13 says most shapes are an earlier reader's test strings, each a place an earlier attempt was wrong, with no work item id and no commit. `(#667)` already stands on the title line |
| 14 | `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:69` | `2759a60d` | P | "red against 2759a60d's sealer step" goes |
| 15 | `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:179` | `1e956838` | P | The sentence at lines 178 and 179 goes |
| 16 | `tests/github/test_publish_release_note.py:38`, `:40` | `8a1173c8`, `c55c3083b` | P | The paragraph at lines 35 to 41 goes whole. It is rule 15's evidence for three work items' phases |
| 17 | `tests/github/test_publish_release_note.py:1185` | `4134055a` | P | The seen-red sentence at lines 1184 and 1185 goes |
| 18 | `tests/github/test_release_seal.py:614`, `:640`, `:659` | `e01e1b12`, `7966a9f9` | P | Each seen-red sentence goes |
| 19 | `tests/github/test_roll_flow_measurement_issue.py:586` | `0d59003` | N | "Proofer round 1 on `0d59003` found that" goes. The defect the case holds stays as the docstring's own statement |
| 20 | `tests/hooks/test_config.py:870`, `:1027`, `:1040`, `:1368`, `:1859`, `:1878` | `4dfb3d0d`, `977b6613` | P | Each seen-red sentence goes |
| 21 | `tests/hooks/test_dispatch.py:281` | `551c7967` | N | The comment says what `UNREADABLE` holds: shapes `classify` and `merge` read without raising, after the gates ran and outside `run_gate`'s isolation. No commit is named |
| 22 | `tests/hooks/test_dispatch.py:424` | `02e47435` | P | The seen-red sentence goes |
| 23 | `tests/hooks/test_routing.py:493` | `126ee7b5` | N | The docstring states the case's input, an empty record, and names no build |
| 24 | `tests/skills/test_arm_check.py:669`, `:701`, `:998`, `:1010` | `346b4af7` | P | "at `346b4af7`" goes from each *Red how* paragraph. "On Python 3.14" and what it named stay |
| 25 | `tests/skills/test_arm_check.py:1415`, `:1615`, `:1694`, `:2316`, `:2390` | `a340221b` | P | "against the script at `a340221b`" goes from each *Red how* paragraph. What the script did stays, in the present or as the defect |
| 26 | `tests/skills/test_arm_check.py:1730`, `:2436`, `:2437`, `:2542` | `6bbaa4d1`, `dc1b0d14` | P | The same, for "at `6bbaa4d1`" and "at `dc1b0d14`" |
| 27 | `tests/skills/test_arm_check.py:2424`, `:2434` | `a340221b`, `6bbaa4d1` | N | Both sentences compare the case with what the command does on its other paths. They say it in the present: every other run ends with the module put back from the bytes held, and a refusal exits 2 |
| 28 | `tests/skills/test_chain_check.py:2134`, `:2162`, `:2192`, `:2225`, `:2248`, `:2271`, `:2297` | `c783f18f4`, `a10750aea`, `4105fd13c` | P | Each seen-red sentence goes |
| 29 | `tests/skills/test_pact_check.py:305`, `:819`, `:822`, `:889`, `:891`, `:998`, `:999`, `:1053` | `977b6613`, `28edee12`, `29e1b040`, `49bb6ba5` | P | Each seen-red clause goes. `(#1132, S1)` and `(#1132, S6)` stay where they cite a scenario |
| 30 | `tests/skills/test_payload_meter.py:402`, `:1293`, `:1316`, `:1338`, `:1347`, `:1372`, `:1382`, `:1488` | `0830987a`, `6137faf8` | P | Each seen-red or green-at clause goes. A mutation that showed the case red, as at lines 1347 to 1349 and 1488 to 1490, goes with it, since it is rule 15's evidence too |
| 31 | `tests/skills/test_payload_meter.py:422`, `:448`, `:1245` | `346cd01d` | G | The harness behaviour each case holds stays in the sentence. "`frame/design.md` at `346cd01d`, probe e" goes, and `#1177` stays where its page holds what the sentence sends the reader there for |
| 32 | `tests/skills/test_seal_stamp.py:1677` | `15a5ce66` | P | "the case is red at 15a5ce66, whose stamp read …" goes. The sentence keeps what the case holds |
| 33 | `tests/skills/test_session_cost.py:4499`, `:4770` | `ab116d1e`, `7b4162fd` | P | Each red-at sentence goes |
| 34 | `tests/skills/test_unverified_check.py:505` | `6137faf8` | P | "Each case is green at 6137faf8, and each was seen red with one boundary of `_scan` mutated" goes, with the mutation list after it |
| 35 | `tests/test_conftest.py:533` | `977b6613` | P | The seen-red sentence goes |
| 36 | `tests/text/test_a_moved_rule_leaves_its_definition.py:8` | `e51fd0b` | G | The defect the module exists for stays in the present: a rule's body pasted back under a new heading left the four named cases green. "Measured 2026-09-03 by the orchestrator, at `e51fd0b`" goes |
| 37 | `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:26`, `:28` | `5d51b319`, `c48cd5e3` | P | The paragraph at lines 25 to 29 goes whole. It is rule 15's evidence |
| 38 | `tests/text/test_a_rider_reaches_its_file.py:70` | `74c7963a` | P | The seen-red sentence at lines 69 and 70 goes |
| 39 | `tests/text/test_ci_gives_the_checks_what_they_need.py:673`, `:702` | `5287dd42` | P | Each seen-red sentence goes |
| 40 | `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py:30`, `:48` | `1fa25931`, `5a66666d` | N | A gone phrase is the carrier's wording before #639. The two commits go and `#639` stays |
| 41 | `evals/behaviour/proofer/seeded-55b66958/`, `seeded-5fd6b88c/`, `seeded-7a8899d5/`, `seeded-ea73e94f/`: `case.yaml:2`, `prompt.md:5`, `scaffold.sh:5`, `:6`, `:22` in each | the four seed commits; the four base commits `48d035aa`, `a92c358b`, `15a5ce66`, `5560c742`, short and full | D | Unchanged. A case's name is its seed commit by the generator's rule, and the scaffold fetches the base by its full SHA, which the command shows. `origin/main` reaches all eight |
| 42 | `.test_durations:1585` | `279a580b` | D | Unchanged. A generated file, keyed by a case id that row 43's parameter makes |
| 43 | `tests/evals/test_replay_targets.py:1043`, `tests/evals/test_seed_defects.py:582`, `:604` | `279a580b` | D | Unchanged. The name of a committed seeded case, which the case's docstring calls one |
| 44 | `tests/evals/test_replay_targets.py:632`, `:641` | `ce448bbe` | D | Unchanged. A fixture key of the monkeypatched `resolve` beside it |
| 45 | `tests/behaviour/test_a_cited_section_stands_in_its_file.py:668` | `f6ae6db6` | D | Unchanged. #1355 put `AT` here with the comment above it that says why |
| 46 | `tests/test_censuses.py:982`, `:983`, `:1055` | `5f11923f`, `67694cba`, `0ed5dd3b` | D | Unchanged. Fixtures of the `<commit>:<path>` form the censuses pass, which the case at line 974's docstring and the case at line 1052's name state |

Rows 1 to 40 are 85 lines: 72 P, 4 G, 9 N. Rows 41 to 46 are 30 lines of data. The text of each rewrite is the work's (`frame/questions.md` Q1).

**D2. `tests/text/test_a_cited_commit_outlives_the_squash.py` also reads a bare commit in a file outside `seal/`, and refuses one that no `main` or release ref reaches.** This departs from #1355's D2, which added no case, and from the layout's "A bare commit is not read". The grounds are in `frame/plan.md` *Alternatives considered*, rows A1 to A5. They were weighed against `skills/core/SKILL.md` *The rule a mechanism is kept against*:

- **What it would have caught.** 34 of the 44 bare tokens D1 rewrites name a commit no remote ref reaches, so a reader in a fresh clone finds nothing. The `<commit>:<path>` form, which the case already refuses when unreached, had none of that kind among #1355's 25 lines (*Grounding*, the comparison row). #1355's D2 could rest on the existing case catching the misdirection, and for the bare form nothing did.
- **It reads exact facts.** Git resolves `<token>^{commit}` or does not, and `git for-each-ref --contains` with the `REACHING` refs answers or does not. A token that resolves to no commit is not read, so the 33 values M2 reads as no commit pass without a mark. Every token D1 keeps as data is reached by `origin/main`, so no exemption mark is added. Whether a sentence meant the hex as a citation is not read, and need not be: outside `seal/`, no file has a reason to name a commit that no clone will hold.
- **It catches the writer at the pull request.** CI's `pytest` job checks out the whole history (*Grounding*, the `test.yml` row), so a commit of the pull request's own branch resolves there, and no `REACHING` ref contains it. Locally, a narrow run of the module refuses it the same way.
- **Under `seal/` it reads nothing new.** A plan's Status cell and a round's `fixed` line name the branch's own commits by rule, so the layout's grounds stand there.
- **What it does not read.** A commit the clone no longer holds cannot be told from a hex value that names nothing, so it is not read. The 12 M2 lists are of that kind, and this work removes them by hand. A reached commit cited as provenance passes. Of D1's rewrite tokens, 10 are of that kind, and whether such a sentence holds grounds is the proofer's reading.
- **What it costs.** One more pass over the files `cited` already reads, one `git cat-file --batch-check` process for every token, and one containment query per distinct resolved commit, six after phase 1. That is about half a second on this machine (*Data & interfaces*, measured). It adds no module, no mark and no second refusal path. The bare tokens join `cited`'s tokens in `unreached`, under the same `REACHING` and the same skip.

## Scope

In scope:

1. **The 85 comment and docstring lines.** Each line of D1 rows 1 to 40 is rewritten as its row says, and so is each sentence of the same paragraph that only makes sense with the clause that goes (D1, P).
2. **The 30 data lines stay.** D1 rows 41 to 46 are not edited.
3. **The record of each line.** The phase record lists each of the 115 lines at the base the phase was built on, with its token, its disposition, and the text that replaced it, `removed`, or `stays`. *Done when* asks for this.
4. **The bare reading in the squash case (D2).** `tests/text/test_a_cited_commit_outlives_the_squash.py` reads each bare token outside `seal/` that resolves as a commit and judges it with `unreached`. Its planted cases hold S7 to S10. Its module docstring, its refusal message and its repair text say what it now reads. The layout rule changes as `## Rule changes` states.

Out of scope:

- `seal/`, whose records keep what they said when written (#1359 *Out of scope*). `seal/follow-up.md`'s commit citations are among them.
- `<commit>:<path>` citations, which #1355 cleared, and tags (#1359 *Out of scope*).
- Hex values that name no commit: the 33 M2 reads as synthetic, a key type, a CRC or the stamp's example values. `skills/verify/scripts/seal_stamp.py`'s example rows and `assets/seals/red-lily.ans` draw the stamp, and none of them is a commit.
- History in a test docstring that names no commit, such as "Seen red against the workflow with no `seal` job" or "#942's phase 6 placed these cases". It has no spelling a method could list whole, so it is an open class, and it is not #1359's form. Each sentence D1 rewrites is read whole, and nothing beyond it.
- Work item ids such as `1790635413` standing alone. They are digits, not commits, and #1355 left them too. Where one stands in a sentence D1 rewrites, it goes or stays with that sentence.
- The sibling work items' sentences. None holds a token (*Grounding*, the siblings row).
- `.claude-plugin/plugin.json`'s version. This work item is not the release's first.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. Only data is left | Given the phase's commit, when `git grep -nP '\b(<the 61 tokens of D1>)\b' -- . ':(exclude)seal/'` runs, then it prints the 30 lines of D1 rows 41 to 46 and no other. When M1 and M2 run again in the same clone, then M1 lists only row 41 to 46 tokens and M2 lists no token that names a commit | the three commands at the phase's commit, run from the repository's own clone where the object store holds the commits. Their output goes in the phase record |
| S2. No new commit is cited | Given the phase's diff, when its added lines are read for hex tokens, then none names a commit | `git diff -U0 <base> -- . ':(exclude)seal/'`, the `+` lines grepped with M1's pattern, and each hit read |
| S3. Code is unchanged | Given `.github/workflows/test.yml` and `skills/implement/scripts/seal.py` at the phase's commit, when their diff against the base is read, then every added or removed line is a comment | `git diff -U0 <base> -- <file>`, each `+` and `-` line read |
| S4. The touched modules hold | Given the phase's commit, when each touched test module runs, then it passes, and the censuses refuse no rewrite. A rewrite naming a moved path, such as `hooks/routing.py`, is what `tests/censuses.py#vacated_paths` refuses | the narrow run of each touched module and of `tests/test_censuses.py` (`skills/verify/SKILL.md`: a docstring is proved by the module importing) |
| S5. Each line is named | Given the phase record, when it is read against D1, then it lists all 115 lines with their disposition and the replacement, `removed` or `stays` | the phase record read against D1 |
| S6. A cited issue holds what it is cited for | Given a rewrite that names `#N` where the base named a commit, when the page is read, then it holds what the sentence sends the reader there for | `gh issue view <N>` or `gh pr view <N>`, read, each named in the phase record |
| S7. A bare commit of a feature branch is refused | Given a planted repository whose second commit only the work branch and a remote feature ref contain, when a `.md` and a `.py` outside `seal/` name it bare, then `unreached` names each with its file, line and token | a planted case, seen red with only the bare reading removed (contract rule 15), its failing line read for that reading |
| S8. A bare commit under `seal/` is not read | Given the same commit named bare in a work item's `frame/plan.md` Status cell and in `seal/follow-up.md`, when `unreached` runs, then it names neither | a planted case. It is green with the bare reading removed too, so its red is shown by making the reading take `seal/` in, and its failing line read for that guard (contract rule 15) |
| S9. A token that names no commit, or a reached one, passes | Given a hex token that resolves to no commit and a bare token of a commit a `REACHING` ref contains, when `unreached` runs, then it names neither, and the tree case's verdict passes rather than skipping | a planted case, shown red by refusing every resolved token whatever ref contains it (contract rule 15) |
| S10. The refusal says what to do | Given a refused bare token, when the tree case's verdict fails, then its message holds the file and line, the token, and a repair that names no commit: state what the sentence needs, or cite the issue | a planted case reading the message (contract rule 14), seen red against the base's message |
| S11. The tree holds | Given the phase's commit in a clone holding `main` and the release refs, when `test_every_cited_commit_outlives_the_squash` runs, then it passes, and the bare tokens it read are those of D1 rows 42 to 46. Row 41's files are under `evals/behaviour/`, which `read_here` leaves out | the module's narrow run, and the bare reader called once in the phase, its output in the phase record |

## Data & interfaces

`tests/text/test_a_cited_commit_outlives_the_squash.py` gains one reader of bare tokens. It reads each `\b[0-9a-f]{7,40}\b` token in each tracked file that `read_here` admits and that is not under `seal/`, other than a token `COMMIT_PATH` already matches. It keeps the tokens one `git cat-file --batch-check` call resolves as `<token>^{commit}`, as `(rel, line, token)`. That call is one process fed every distinct token on stdin, one line each, and it answers one line per token in the same order, `<sha> commit <size>` or `missing` or `ambiguous`. No token gets a process of its own. `unreached` then judges the resolved tokens beside `cited(root)`'s tokens with the reading it has: one `git for-each-ref --contains` per distinct commit, and only resolved commits reach it. After phase 1 that is six distinct bare commits in the tree, D1 rows 42 to 46's.

**The cost this accepts** (executed on this macOS machine, 2026-11-05, at `31558c76`'s tree): the 6,500 distinct tokens through one `git cat-file --batch-check` took 0.40 s wall clock, and 49 resolved. The six containment queries for D1 rows 42 to 46's commits took 0.09 s together. Listing the tokens with `git grep` took 1.1 s, but the case reads the files `cited` already reads in Python, so that figure is an upper bound on the scan and not the case's own. The cost on the Windows and macOS CI legs is `unverified`, and phase 2's CI run answers it in the `--durations` table each leg prints. `refusal` and `REPAIR` name the bare form. The planted helpers `planted` and `cite` serve the new cases as they are. The names of the new reader and cases are the work's.

No other interface changes. Phase 1 changes comments and docstrings only, and no constant's value.

## Rule changes

- change
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: **A `<commit>:<path>` citation names a commit that `main` or a
    release branch reaches, except in a work item's `trail/` and its
    `guarantee.md`.**
  to: **A cited commit is one that `main` or a release branch reaches:
    a `<commit>:<path>` citation anywhere except a work item's `trail/`
    and its `guarantee.md`, and a bare commit in a file outside `seal/`.**
- change
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: A bare commit is not read: a plan's Status cell and a round's
    `fixed` line name the branch's own commits by rule, and whether a
    sentence cites a bare commit as where a file was read is the
    reviewer's reading.
  to: Outside `seal/` no file has a reason to name a commit that no clone
    will hold, so a bare hex token that resolves as a commit is read
    there, and one that resolves to no commit is not. Under `seal/` a bare
    commit is not read: a plan's Status cell and a round's `fixed` line
    name the branch's own commits by rule, and whether a sentence there
    cites a bare commit as where a file was read is the reviewer's
    reading.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the count, commit and run id that grounded "every leg collects the same cases" | `.github/workflows/test.yml`, the comment above the `pytest` job's `include` matrix | the claim stays |
| two parentheses naming who measured or found a behaviour at a commit | `skills/implement/scripts/seal.py#import_` and `#remove_workflow`, one comment each | git; the behaviour each states stays |
| the clauses and sentences naming the commit a case was seen red or green at, 72 lines with the paragraphs that only make sense with them | the docstrings and comments of the 21 test modules D1's P rows name | contract rule 15's evidence belongs to a phase record. Git holds the commits that are still reachable |
| three citations of a past frame's probe at a commit | `tests/skills/test_payload_meter.py#test_an_import_that_is_not_a_file_is_a_missing_row`, `#test_one_real_path_imported_twice_is_one_row` and `#test_accepts_a_symlink_as_its_target`, the docstrings | the behaviour stays in each sentence; `#1177` where its page holds it |
| the measurement that opens the module's motivation | `tests/text/test_a_moved_rule_leaves_its_definition.py`, the module docstring | the defect stays as a sentence |
| the work item and commit naming where the shapes came from | `tests/block_shapes.py`, the module docstring, and `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py`, the comment above `COMMENT_SHAPES` and its section header | the comments in present terms; `#667` on the title lines |
| a commit naming where shapes raised, a build that wrote a record, and two commits a phrase's old wording stood at | `tests/hooks/test_dispatch.py`, the comment above `UNREADABLE`; `tests/hooks/test_routing.py#test_accepts_a_branch_into_the_empty_record_an_earlier_build_left`, the docstring; `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py`, the comments on `CARRIERS` | each comment says what its constant or case holds; `#639` stays |
| two commits a refusal's behaviour is compared with | `tests/skills/test_arm_check.py#test_a_refused_run_leaves_the_module_as_it_was_before_the_command`, the docstring | the comparison in present terms |
| a proofer round's finding at a commit | `tests/github/test_roll_flow_measurement_issue.py#test_close_succeeds_but_open_fails_names_both_in_the_message`, the docstring | the defect stays as the docstring's statement |
| the sentence saying the case reads no bare commit | `tests/text/test_a_cited_commit_outlives_the_squash.py`, the module docstring | the docstring states what the case reads now (*Scope* item 4) |
| the layout's exemption of every bare commit | `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/* | `## Rule changes`; the settle writes it, and the exemption stands under `seal/` |

**What D2 adds, and what goes in return.** D2 widens one existing case's reading. Nothing goes in return, because no other mechanism reads bare commits, and the case keeps one refusal path, one `REACHING` and one skip. The catch record it stands on is the 34 unreached tokens D1 rewrites (*Grounding*, the reachability row). Whether it keeps catching is what the settle weighs, by `skills/core/SKILL.md` *The rule a mechanism is kept against*.

Framed 2026-11-05 by framer, before the build.
