# Phase 2: 1793174170-two-facts-kept-in-several-files-have-drifted

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | e61cd169 |

## What this phase was asked

Build `frame/plan.md`'s phase 2, the counts in prose: the always-on
heading and the CLAUDE.md block row (S3), the hooks that reach the network
in both READMEs and `CONTRIBUTING.md` (S4), and the skills row (S5).
`NUMBER_WORDS` and the two count cases leave, and S5's membership case
replaces them. Each case is seen red at `5287dd42`'s prose before the
prose changes.

## What this phase found

- **The frame held at this tree.** Each sentence *Removes* lists for this
  phase stood at its coordinate, and no module other than
  `tests/behaviour/test_chain_hooks_hardening.py` read any of them (read,
  `git grep` on each phrase over the tree outside `seal/threads/` and
  `changelog/`). No link anywhere named the old heading's anchor.
- **S3, S4 and S5 seen red, then green.** Against the prose as it stood,
  the three new cases failed together with exit 1: S5 on `Fourteen` in
  `README.md`'s skills row, S3 on `context is 12 lines`, S4 on the missing
  `lint-python and version-check reach the network.`. After the prose
  edits the module passed, 29 cases, exit 0 (executed).
- **How the S5 case reads the row.** The on-demand sentence is the one
  sentence of the skills row, split on `. `, that holds "a session loads on
  its own" in English or "알아서 로드" in Korean. Its backticked names must
  equal the skills on disk that no agent's frontmatter preloads and whose
  frontmatter does not say `disable-model-invocation: true`. The whole row
  must hold no count word. The case's `COUNT_WORD` pattern matches a
  numeral, an English number word from one to twenty, or a Korean native
  numeral before `개`. It spells the two languages and counts nothing in
  the tree, so it is not the stored count `NUMBER_WORDS` was. The row's
  opening "Fourteen, in three groups" went, and "In three groups" was
  tried and failed the pattern, so the row opens with the preloaded skill.
- **The S3 case does not apply `COUNT_WORD` to the block row.** A first
  draft did and failed on "Its one source is", which names the block's one
  source and counts nothing. The frame asks for absence pins of the four
  phrases and for the row to name `templates/setup/claude-md-block.md`,
  and the case holds exactly that.
- **"Both" and "둘 다" went with the count.** "Both stay silent" became
  "Each stays silent", and "둘 다" became "어느 훅이든", because a word that
  means two is the count in another spelling. The S4 case pins both old
  spellings absent.
- **Phase 1's `root-migrate` row broke the old-names census.**
  `tests/test_censuses.py#Test_module::test_every_file_no_module_file_declares_meets_every_census`
  failed with exit 1 on `seal/specs`, then on `specseal`, at
  `README.md:174` and `README.ko.md:168`. A table cell has no line above
  it for the `# exempt from old_names:` marker, so the row now says "each
  0.22.x work item" and "the state files an earlier release wrote under its
  old name". The census then passed, 175 cases, exit 0 (executed).
- **`CONTRIBUTING.md:448` ran to 100 columns** after the S4 rewrite, and
  `test_docs_line_wrap.py` failed with exit 1. The paragraph was re-wrapped
  and the module passed, 39 cases, exit 0 (executed).
- **`.test_durations` lost the two removed cases' keys**, the way #1040's
  phase removed its removed case's key. The readers of that file ran green
  in the sweep below.
- **Each new unit was mutated, and each went red.** `seal mutate` printed
  `red` with exit 0 for eight mutants: `agent-contract` added to the
  English on-demand list, `verify` taken out of the Korean one, `Nine` and
  `아홉 개는` written into each row, `12줄` put back into the Korean heading,
  the template's name taken out of the English block row, "A third needs"
  put back into `CONTRIBUTING.md`, and "둘입니다" put back into the Korean
  privacy paragraph (executed).
- **Every module that reads a file this phase changed ran green.** Found
  with `git grep -l` on `README.md`, `README.ko.md`, `CONTRIBUTING.md` and
  `test_durations` under `tests/`, 52 modules, one per call, each exit 0 on
  the final run (executed). `uvx ruff check` and `uvx ruff format --check`
  passed over the changed test file (exit 0, executed).
