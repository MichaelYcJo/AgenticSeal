# Phase 2: 1793051803-settle-runs-in-local-mode

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | c814dcc9 |

## What this phase was asked

Phase 2 is what else stood on the refusal.
`seal_stamp.py#queue_for_written_guarantee`'s docstring is rewritten (*In*
item 10). A `git grep` outside `docs/` and `seal/specs/` finds every other
statement that `settle` refuses or retires no local-mode work item, and each
is rewritten or named here. S12 is run over this work item's `spec.md`.
Phase 2 is the last phase, so it also writes `overview.md` and the changelog
fragment in the shape #1033's used, and fills `plan.md`'s Status column.

## What this phase found

**The frame holds** (`read`). The docstring sentence stood where *Grounding*
says, at `skills/verify/scripts/seal_stamp.py` line 1229 at `2c20bc60`. It now
gives the reason the `## Rule changes` item for *The stamp* gives: "since a
local-mode work item stays under the root until the settle after its release
removes it".

**S11** (`executed`): before the edit, `git grep -n "retires no
local-mode"` outside `docs/`, `tests/` and `seal/specs/` returned
`skills/verify/scripts/seal_stamp.py:1229`. After it, the same command exits 1
with no line. S11 has no case; its reader is the warden.

**The sweep** (`executed`: `git grep -n -i -E` over the refusal's wordings,
"retires no local", "refuses in local mode", "Local mode is refused",
"settle" within 80 characters of "local mode" either way, "no ref holds the
work item" and "nothing removed from them could be recovered", outside
`seal/specs/` and `changelog/`. A second pass listed every local-mode line in
each file outside `skills/settle/` that names `settle`). What stands, and why:

- `docs/the-review-record.md` line 382, *The stamp*: the policy root, which
  this pull request does not edit. The second item of `spec.md` *Rule
  changes* carries its new reason for the settle to write.
- `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` line 207: it
  pins that policy sentence. `spec.md` *Out* leaves it to that settle.
- `templates/hygiene.yml` line 13, "Why it refuses in local mode", and
  `tests/test_first_setup_asks_once.py` line 461, which pins it: they are
  about the pull-request workflow, not `settle`.
- `changelog/0.5.0.md` line 9: a released note, which is history.
- No other line in `README.md`, `README.ko.md`, `seal/README.md`,
  `templates/seal-README.md`, `docs/`, `skills/`, `hooks/` or `agents/`
  says that `settle` refuses a local root.

**S12** (`executed`: `rule_changes.py#parse` over this `spec.md` with policy
root `docs`, then `section_lines` and `pattern` over each operation's
document). `## Rule changes` parses to 2 operations and no error. The `add`
to `docs/the-record-layout.md` *The fold, and what tells it from a deletion*
finds its section at lines 60 to 193, and its `to` is not there yet. The
`change` to `docs/the-review-record.md` *The stamp* finds its section at
lines 334 to 485, with its `from` found and its `to` not found.

**The real `gh` answers in the shape the reader parses** (`executed`, a
read-only probe). `settle.py#merged_pull_requests` was run against this
repository for `feat/1033-settle-writes-each-sections-latest-decision`. It
returned `[(1035, '91d570289b8a0770a130978a96e84d69ba2aaee4')]`, and
`settle.py#reaches` read that merge commit as reachable from `HEAD` and not
from `origin/main`. That is the same reading as `spec.md` *Grounding*'s last
row. No local-mode settle was run on a real local root (`spec.md` *Out*).

**The narrow checks** (`executed`, exit 0): `bin/test tests/test_seal_stamp.py
tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py -q` returned 165
passed at `c814dcc9`. `uvx ruff check` and `uvx ruff format --check` over
`seal_stamp.py` report nothing. At the phase boundary, with `overview.md` and
`changelog.md` written, `bin/test tests/test_settle.py
tests/test_rule_changes.py tests/test_settle_reads_before_it_removes.py
tests/test_seal_stamp.py
tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py
tests/test_chain_hooks_hardening.py
tests/test_a_phase_hands_the_next_one_a_record.py
tests/test_the_changelog_is_gathered_at_release.py
tests/test_a_shrunken_corpus_declines_to_judge.py tests/test_docs_line_wrap.py
tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_rules.py
tests/test_censuses.py tests/test_unverified_rows_close.py -q` returned 681
passed. `unverified-check` over this work item reads 2 open rows and nothing
unreadable.
