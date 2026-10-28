# Questions for the planner: 1793174170-two-facts-kept-in-several-files-have-drifted

The issue left these judgments open, and the tree answered them. They are not
reopened. The grounds of each are in `frame/design.md` or in `plan.md`'s
Alternatives table.

- **Which of the three places is the home of the way back before the commit
  to shared** (issue item 2: "one of those three"). The home is
  `skills/config/SKILL.md` *Before switching to shared, say what cannot be
  undone*. That is where the warning is said before the act, and
  `tests/text/test_the_settings_have_a_front_door.py:119` already pins the
  command there. The rule that the history is the one-way door stays in
  `docs/one-root-by-lifetime.md` *Shared or local* (`:182-188`), which the
  skill cites.
- **The home of the `README.md` and `skills/config/SKILL.md` pair** (issue
  item 6: "the work's to name"). The pair's 21 shared runs are all item 2's
  passage (executed, a 15-word window comparison), so item 2's answer names
  it.
- **Whether the template gains `concurrency` as well as `permissions`.**
  Both. The reason `tests/text/test_ci_gives_the_checks_what_they_need.py`
  gives for cancelling superseded runs holds for any workflow on
  `pull_request`, the shipped one included.
- **Whether `permissions: contents: read` is enough for the template's job.**
  It is. The repository's own job runs `actions/checkout` under
  `contents: read` (`.github/workflows/hygiene.yml:30-38`), and the
  template's other steps clone a public repository and read files (read,
  `templates/setup/hygiene.yml:38-96`).
- **Whether `worktree_consent` and `root-migrate` get gate-table rows, or
  are exempted.** They get rows. Both write on a person's machine, and an
  exemption list would be a second list beside `GROUPS`.
- **Whether the plugin description's copies are deleted or checked.** They
  are checked. JSON cannot link, and how the marketplace listing renders
  without the copies is not visible from this tree.
- **Whether the workflow step "both READMEs move together" goes once the
  outline case reads the README pair.** It stays. It reads the diff, which no
  case reads, and it fails nothing.
- **Whether the README headline keeps its number.** It does not. The issue
  says "The prose drops the numbers", and the heading is prose.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does `skills/implement/SKILL.md` *3. The SDD file set* still hold the pasted sentence at `:355-359` when phase 3 is built? #1110 rewords that file after #1041 on its own branch, so the coordinate can move if #1110 reaches `release/v0.24.0` first. The tree at `5287dd42` cannot say which branch lands first | the work | Unchanged: replace the sentence with the link, as framed. Already reworded by #1110: find the 15-word runs the file still shares with `docs/the-agent-set.md`, replace those, and record the divergence in the phase record | Build as framed against the branch tip, re-finding the passage by its words and not by its line numbers | open |
| Q2 | Does `docs/the-review-record.md` still have the heading *What the check reads at the pull request* when phase 4 is built? #1041 owns that file and runs in parallel. S10's comment names the section by its heading, so a renamed heading would leave the template's comment naming nothing | the work | Heading unchanged: name it as framed. Heading renamed by #1041 on the release branch: name the new heading, and record the divergence | Name the heading as it stands at the branch tip when phase 4 is built | open |
| Q3 | Do #1053 or #1117 edit `.github/workflows/hygiene.yml` in a hunk that phase 4 also edits? Their scope is the release steps with their comments (`:42-130`, `:165-206`) and phase 4's is the comments of the two shared steps and the file head. The two scopes do not overlap at `5287dd42`, but neither branch is in this tree | the work | No overlap: build as framed. Overlap: the branch that lands second resolves the conflict, keeping both edits | Build as framed. A conflict at the merge is resolved by whichever branch lands second | open |
| Q4 | Does #1056 change what `hooks/worktree_consent.py` writes or when it runs, so that phase 1's new README row describes it wrongly? #1056 edits that hook on its own branch. S1's case reads only the row's name, so a stale description would not go red | the work | Unchanged: the row as framed. Changed by #1056 before phase 1: describe the hook at the branch tip, and record the divergence | Describe the hook as `hooks/worktree_consent.py`'s docstring has it at the branch tip when phase 1 is built | open |
