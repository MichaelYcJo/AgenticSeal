# Review round 2: 1793171930-no-check-reads-a-citation-of-most-files

target: c6b32357, fixes fa687320..c6b32357

## Findings

None. Both closes of round 1 hold, and the fix diff raises nothing new.

## Confirmations

confirms: round-1#1
The close `fixed 5a590a2c` holds.
`tests/text/test_a_language_section_of_writing_style_opens_alone.py:44-48`
now ends `WRITING_RULE_CHECKS[0]` with
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`, in the same
order as the `check:` line of `skills/writing-style/SKILL.md:268` (read).
Round 1's evidence line was re-run at `c6b32357`. The module passes, inside
the module run below, which ended exit 0 (executed).

confirms: round-1#2
The close `fixed 5a590a2c` holds. `NAME_CITED`
(`tests/behaviour/test_a_cited_section_stands_in_its_file.py:55`) now
captures ` skill's` as group 2 and the cited text as group 3. `cited_in`
reads a name citation where the skill is tracked or group 2 stands
(`:93-100`), and such a citation's target, `skills/<name>/SKILL.md`, is read
and refused when nobody tracks it (`:199-204`) (read). The bare form keeps
the tracked filter. S5 pins both halves: the bare `` `unlisted` *Gone five* ``
stays unread, and the `skill's` line at 20 is dangling (`:388-404`, read).
The crafter says S5 failed `assert 9 == 10` before the reader change. That
claim was read, not re-run. It follows from the old filter, which dropped
the `unlisted` match at the old `:96`.

The `format` construction in `SPELLINGS` (`:351-375`) was reviewed as code.
`SPELLINGS` holds no other brace, so `str.format` substitutes only `{d}` and
`{u}` and raises on nothing (executed: the probe counted 0 braces in the
built string). A backticked `{d}` does not match `NAME_CITED`, whose name
opens with a lowercase letter or a digit. So S1, which reads this module's
own text, finds no `skills/` citation in it at `c6b32357` (executed). The
crafter labelled one consequence `read`: written with the literal names,
the module would make S1 fail. The probe confirmed it. With `{d}` and `{u}`
replaced by `drafting` and `unlisted`, the module's text yields three
`skill's` citations, at lines 358, 360 and 373, of
`skills/drafting/SKILL.md` and `skills/unlisted/SKILL.md`. Neither file is
tracked, so all three dangle (executed). The comment at `:351-353` gives
the reason.

The new `gaps.md` row (`gaps.md:15`) states the departure from the frame's
grammar table and grounds it in round 1's finding 2 (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck. Nothing is left open in this work item, so the broad run comes next, then the sealer's spawn after it. | `seal/threads/1793171930-no-check-reads-a-citation-of-most-files/gaps.md:21` | the orchestrator, at `seal gate` |
| The crafter's count of 1843 passed over 21 modules. This round ran its own set of 12 modules instead (below). | `seal/threads/1793171930-no-check-reads-a-citation-of-most-files/trail/rounds/round-1.md:42` | the orchestrator, at `seal gate` |

## Probes

| Command | Result |
|---|---|
| `bin/test` over `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/text/test_a_language_section_of_writing_style_opens_alone.py`, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`, `tests/behaviour/test_unverified_rows_close.py`, `tests/behaviour/test_the_set_a_work_item_always_has.py`, `tests/behaviour/test_chain_hooks_hardening.py`, `tests/behaviour/test_one_heading_rule_holds_to_commonmark.py`, `tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`, `tests/behaviour/test_a_phase_hands_the_next_one_a_record.py`, `tests/test_censuses.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/text/test_the_rules_have_one_owner.py`, `-q`, in a clone at `c6b32357` | exit 0, 421 passed |
| `bin/seal layout --check` | exit 0, 160 files read, 0 refused |
| `bin/seal rules --check` | exit 0, all 266 check lines in 55 rule files hold |
| `tests/behaviour/test_tmp_round2_probe.py`, one file run once and deleted. It runs `cited_in` over the module's committed text, and again with `{d}` and `{u}` replaced by `drafting` and `unlisted`, and counts the braces in the built `SPELLINGS`. | exit 0. Committed text: no `skills/` citation. Literal names: three, at 358, 360 and 373, all untracked and dangling. Braces: 0. |
