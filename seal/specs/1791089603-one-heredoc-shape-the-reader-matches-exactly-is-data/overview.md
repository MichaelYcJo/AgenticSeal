# 1791089603-one-heredoc-shape-the-reader-matches-exactly-is-data — overview

📋 implement applied
· spec:     `spec.md` §*The shape* clauses A–F, §*Why this shape*, §*#739's three refusals*, S1–S10; `plan.md` phases 1–3 and alternatives B–H; `questions.md` Q1–Q5; `docs/commit-review-gate-spec.md` §*A file edit goes through the `Edit` tool*, §*Two readings that prompted that run stay as they are*, §*Only what the shell would EXECUTE is read as commands*; `skills/agent-contract/SKILL.md` §9
· evidence: `seal/ledger/1791089603-one-heredoc-shape-the-reader-matches-exactly-is-data.md` — eight `Re-read ·` rows (E1, E2, E6, E9, E17, E18, G8, C1) and three `Corrected ·` rows (E3, E7, I10)
· verified: executed — the reader, gate, agreement and hygiene modules narrow, each new case red against a mutation; read — I10's generated corpus, not re-run

## Why this work exists

A pull request body or a note that only mentions a commit, written through
one exact heredoc shape, no longer costs an unattended run a refused Bash call,
and no other command reads any differently.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| An `Enforced by:` line in contract §9 | S10: "Each carries an `Enforced by:` line naming S1, S4 and S6's cases". The contract carries no `Enforced by:` line anywhere, and no checker reads one there | §9 names the policy statement that carries the grammar, and `tests/test_edits_go_through_the_edit_tool.py::test_the_rule_names_the_one_heredoc_shape_it_does_not_read` pins both carriers; the policy statement's `Enforced by:` line names S1, S4 and S6's cases | `skills/agent-contract/SKILL.md` has no section in that shape, and `fold-check` reads `docs/` only. A line nothing reads would be a pin that cannot fail |
| The reader's body form | Spec silent on whether the body carries its last newline | Each line with its newline | An empty body and a body of one empty line are otherwise the same string, and the shell writes them differently (`phases/phase-1.md`) |
| A program terminator followed only by newlines | Clause F: "where a suffix exists, a newline and the suffix" | Newlines alone are no suffix | A run of newlines runs nothing, and keeping them would make the reduced text differ from a sink's for no reading |

## Not verified

| Item | Who must answer |
|---|---|
| closed Q3 for bash 5.x: whether bash 5 cuts every admitted string where the reader does, directly and through `eval` | #997's `ubuntu-latest` leg ran `tests/test_one_heredoc_shape_agrees_with_the_shell.py` green |
| closed Q4: whether the moved row reaches the shape on the Windows leg, where `shlex.quote` gives a single-quoted path with backslashes | #997's `windows-latest` leg ran `tests/test_no_shape_the_base_stops_reads_silent.py` green |
| closed The agreement test on the Windows leg, where `bash` is Git Bash or is skipped by `shell_probe` | #997's `windows-latest` leg ran it green |
| closed How many commands of I10's generated corpus (11,393) and recorded sessions are the one shape | moot: the generator was a probe deleted after its one run (`1790660768`'s `spec.md` S7, read at 4d5a6917^), and the commit gate's text reading the count served left the tree with `hooks/commit-review-gate.py` at 61a8455a (#1027) |
| closed The full suite, repository-wide lint and typecheck | #769, merged with lint and the suite green on the ubuntu, macOS and Windows legs; the repository configures no typecheck |

## Not done

- The ten ledger rows still drifted (`templates/config.md`,
  `tests/test_release_hygiene.py#VERSIONS_OF_ANOTHER_PRODUCT`,
  `tests/test_the_suite_has_a_command_that_is_cheap_twice.py#fake_venv`) drift
  on `release/v0.18.1` at `edee5ca2` and are not this branch's to re-read.
- Lifting the CR and backslash-newline bans. Both shells here keep those
  bytes literal in a single-quoted body (`phases/phase-1.md`), which is a
  measurement for `plan.md`'s alternative H, not a decision this work makes.

## Fed back into the spec

none
