# Phase 5: 1793140810-each-directory-holds-everything-in-one-level

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | bb5a17ff |

## What this phase was asked

Build `frame/plan.md` row 5, the last phase, on `questions.md` Q2's default:

- remove `debug`, `build-fix`, `checkpoint`, `gap-analysis`,
  `security-audit`, `testing`, `learn` and `audit` with `git rm -r`;
- make `README.md` and `README.ko.md` count fourteen skills, take the eight
  out of their group lists, and take the `/agentic:security-audit` and
  `/agentic:testing` row out of the cheat sheet;
- make the count words in `tests/behaviour/test_chain_hooks_hardening.py`
  carry fourteen;
- write the work item's `changelog.md`, with a *Changed* entry that says
  where `templates/`, the `hooks/` modules and the `tests/` files now stand,
  and a *Removed* entry that names each skill and says the two commands are
  gone;
- in the same commit, remove everything else that stood on a removed skill:
  an agent's `skills:` entry, a `check:` line, a census or a test that names
  one, and a citation in `docs/`, `skills/` or `CONTRIBUTING.md`, found by
  `git grep` for each name and each `skills/<name>/` path. Released records
  keep their names.

The removal owes no new case, no red run and no `seal mutate`. The phase
ends with one `bin/test` command over the row's four modules and the modules
that read what it changed, the row's `git grep` matching only records, and
`claude plugin validate .` exiting 0.

## What this phase found

**What stood on the removed skills.** `git grep` for each name, in
backticks, quoted and as a whole word, and for each `skills/<name>/` path,
over every tracked file outside the records and the removed directories,
found these readers (executed):

- `README.md:43` and `README.ko.md:43`, the skills row, and `README.md:273`
  and `README.ko.md:265`, the cheat-sheet row. The row lists the nine
  on-demand skills, and the cheat-sheet row is gone.
- `tests/behaviour/test_chain_hooks_hardening.py#test_migrated_commands_stay_user_invoked`
  looped over `preset-setup`, `security-audit` and `testing`, and asserted
  each `SKILL.md` exists. It now checks `preset-setup` alone.
- `tests/behaviour/test_chain_hooks_hardening.py#test_installer_prints_commands_a_user_can_actually_type`
  held `security-audit` and `testing` in its set of plugin commands. The set
  holds `preset-setup` and `parity-setup`.
- The docstring of
  `test_every_shipped_skill_is_named_in_both_readmes` gave `audit` and
  `/agentic:security-audit` as its example of a bare name matched inside a
  longer one. It states the same reason without the removed names.

No agent's `skills:` list, no `check:` line, no census constant and no
citation in `docs/`, `skills/`, `CONTRIBUTING.md`, `evals/`, `.github/`,
`hooks/` or `bin/` named a removed skill. The only `check:` text inside
the eight files was a `NOT for:` clause in `skills/gap-analysis/SKILL.md`.
Each removed directory held its `SKILL.md` and nothing else.

**A name that stays, because it stands on no removed skill.**
`tests/hooks/test_review_skill_gate.py:92` passes `"debug"` to
`test_accepts_any_other_skill_name` as an unrelated skill name. The gate
reads no skill directory, so the case tests a name and not the skill, and
another plugin's `debug` still exists.

**The count case needed two spellings and one phrase.** The tree holds
fourteen `skills/*/SKILL.md`, split into one preloaded by an agent
(`agent-contract`), nine on demand and four typed by name (`config`,
`parity-setup`, `preset-setup`, `update`). `skills/evidence-check/` holds
`scripts/` and no `SKILL.md`, so it is not a skill and is not counted.
`NUMBER_WORDS` gained 14, `Fourteen` and `열네`. The group spellings had no
entry for 9, and spelt 4 as `four`, which cannot open the sentence "Four you
invoke by name". They gained 9, `Nine` and `아홉`, and 4 is `Four`. The
Korean phrase of the user-invoked group was `나머지 %s은`, which read
`나머지 여섯은` and would read `나머지 네은` for four. It is `나머지 %s 개는`,
and the Korean row says `나머지 네 개는`. The docstring's sum is
`14 = 1 + 9 + 4`. `NUMBER_WORDS` keeps 20 to 24, so a row that still says
`Twenty-two` stays refused.

**The changelog fragment has no template to start from.** The spawn prompt
names `templates/records/sdd-changelog.md`. No such file stands in
`templates/records/`, and no commit on any ref has held it at that path or
at `templates/sdd-changelog.md` (executed: `ls templates/records`,
`git log --all` over both paths). The fragment takes the shape of
`ab14194b:seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/changelog.md`,
the 0.23.0 fragment that `changelog/0.23.0.md` gathered: `### Changed` and
`### Removed`, one bold sentence per entry naming the issue, and no line
starting `## `. Its *Changed* entries also carry the limit
`frame/plan.md` *Operational impact* says the fragment states: the
`hooks/optin.py#MARKER` and `templates/config.md` spellings a repository set
up before 0.23.1 keeps. Both old spellings were read at `8fcc543b~1`.

**Existing cases relied on.** One `bin/test` command ran 34 modules: the
row's four, at `tests/behaviour/test_chain_hooks_hardening.py`,
`tests/skills/test_payload_meter.py`,
`tests/text/test_every_agent_reads_the_contract.py` and
`tests/hooks/test_review_skill_gate.py`; the 25 modules that open the
top-level `README.md` or `README.ko.md`; the three others that glob
`skills/*/SKILL.md`; `tests/github/test_rules.py`, `tests/test_censuses.py`,
`tests/github/test_gather_changelog.py` and
`tests/text/test_the_changelog_is_gathered_at_release.py`. It passed 991
cases and skipped 8 (executed). No case was written new.

**The row's checks (executed).** The row's `git grep` matched one line,
`frame/design.md:277` of this work item, which is a record. `claude plugin
validate .` exited 0 with two warnings, the plugin root's `CLAUDE.md` and
the missing icon, neither about a skill. The tree's `bin/seal rules --check`
and `bin/seal layout --check` exited 0. `uvx ruff check` and `uvx ruff
format --check` over `tests/behaviour/test_chain_hooks_hardening.py` exited
0.
