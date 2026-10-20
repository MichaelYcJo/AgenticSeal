# a reader declares its input class (#835) — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. Facts that must outlive this work item go to the
evidence ledger, not here. -->

📋 implement applied
· spec:     `spec.md` (every section), `plan.md` (phases, seams, alternatives), `questions.md` Q1–Q7, `docs/the-evidence-ledger.md`, `docs/the-record-layout.md`, `templates/config.md` §*The ledger freeze*, `skills/agent-contract/SKILL.md` §§1–17
· evidence: `seal/ledger/1791384152-a-reader-declares-its-input-class.md` — one test-held row per scenario group (R1–R10, S1–S8), D1 on the new document, one `Corrected ·` row (0.8.0's R5) and the `Re-read ·` rows `--reverify --into` wrote — and the in-place re-stamps `--reverify` made in the live fragments 1791384154, 1791384156, 1791384158 and 1791384159
· verified: executed — the registry module, the records-arm and freeze modules, every module reading an edited document, `bin/evidence-check --strict`, one `mutation-check` per new unit; read — the claim of every ledger row the edits drifted

## Why this work exists

Every unit of shipped Python now says in its own docstring what class of input
it reads, a new or changed unit cannot land without saying it, and a frame
names what its work removes where a check reads it, so 0.21.0's theme — every
reader is observed, forces a format, or is deleted — has a mechanism that
holds it after the release.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| K1's count | `spec.md` §*The population*: 621 units call a K1 primitive at 4ba84e19, by matching a method by its attribute name on every receiver. The walker read 620 at the build | the spec, since round 1 | the build judged a method on a module K1 names by the table alone, so `ast.walk` was not `walk`. Round 1's 🟡 1 showed that read the table as complete for each such module and let `os.open` pass. The fix matches a method by its name on every receiver, as the spec says, and adds the module functions the round measured (`os.open`, `os.path.islink`, `re.split`, `shlex.shlex` and others): 632 at 2fc65bea. `phases/phase-1.md` carries the build's reading |
| The population's edge | the spec's reproducing command reads `ast.parse(...).body` | the walker takes every `def` and `class` inside no other, through module-level `if`, `try`, `except` and `with` | the spec's own rule is *every unit*, and `py_spans` keys such a unit by its bare name too; at this tree the two agree |
| The limits list | `spec.md` §*What neither check can read*: six | seven in `docs/the-reader-registry.md`, the seventh a census line put back by hand | the row below; a limit nobody states is the one a reader meets by surprise |
| What the census can hold | `spec.md`: the census *only shrinks* | shrinks by convention: the writer refuses to run over an existing file, and a line put back by hand passes | telling a restored line from an original one needs history, and the check calls git only to list files (`plan.md` §*Constraints*). The test module's docstring names it as the sixth limit; the warden reads the census's diff |
| A wrapped declaration | the grammar's direction word is *last after `; unknown`* | the word must end the declaration's one line, and a paragraph under the line explains it | *One line per unit* (`spec.md` §*The vocabulary*); reading a wrapped paragraph would mean deciding where a person's prose ends |
| S9's exit code | `plan.md` phase 3 *Verified by*: exit 1 naming `STANDING` at the probe commit | exit 2 | `spec.md` S1 grades `STANDING` like a stated name the tree lacks, which `exit_code` counts as refused, exit 2 under either reading; the spec outranks the plan's verification cell |
| The arm's status words | `questions.md` Q4 left the word for a refused row open | `STANDING` for a removal still in the tree, `REFUSED` for a row the ledger's grammar would refuse, a bare `nothing`, a section a cutoff requires, and a `Removes from` value that is not an id | one new word per distinct repair; `MALFORMED` was not reused because the ledger arm grades it exit 1 lenient, and a records refusal is exit 2 |
| Where the section is cut | Q4: in `claim_lines` or a sibling | a sibling, `removes_section`, over `claim_lines`' output; `file_claims` drops the section's line numbers from the name and stamp halves | `claim_lines` stays unchanged, so its many readers keep their answer |
| The framer's Seams rows | `plan.md` §*Seams* names removed units as `file`'s `name` | two rows carry `NAME NOT IN TREE` | once this item's fragment existed its records were read, and four removed names (`pull_request_is_ready`, the brace reader's three) are no token anywhere else; the marker is the arm's sanctioned answer for a record that means an absent name |

## Not verified

| Item | Who must answer |
|---|---|
| closed the full suite, repository-wide lint and typecheck after the rounds settle | #895, merged with lint and the suite green on the ubuntu, macOS and Windows legs; the repository configures no typecheck |

## Not done

Nothing re-reads a `Reads:` class once written, and nothing checks a census
line was there before: both are the warden's at review, as `spec.md` §*What
neither check can read* says.

## Fed back into the spec

none
