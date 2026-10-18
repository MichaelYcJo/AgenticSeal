# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — review round 6

target: b81719e2, fixes 03ee1bab..b81719e2

## Findings

This verifying round raises no finding. Round 5's one close holds: the
replaced sentence is true of what a clone copies, its repair carries out
without a person, and the sealer's definition and the spawn paragraph do not
contradict it.

## Confirmations

confirms: round-5#1
The sentence at `skills/code-review/orchestration.md:222-225` now offers one
repair, a respawn with the branch worktree itself as the sealer's clone, and
drops the fetch whose plain spelling failed. a5d4d32c changes that file and
no other, and the text matches round 5's paste-ready block word for word
(read, `git show a5d4d32c`).

Its claim about a clone holds (executed). In a `git clone --no-local -q` of
the worktree at b81719e2, and in a plain `git clone -q` of it, the
clone's `refs/remotes/origin/*` less `HEAD` is exactly the worktree's
`refs/heads/*`, 26 names each and `diff` exit 0, and the worktree's own
`refs/remotes/origin/release/v0.22.1` is absent. So a clone copies the
worktree's branches, as remote-tracking refs, and none of its `origin/` refs.
`rev-parse --verify --quiet` for `release/v0.22.1@{upstream}`,
`origin/release/v0.22.1` and `release/v0.22.1` exits 1, 1, 1 in both clones,
the verdict's condition, and 1, 0, 1 in the worktree.

Its claim that the base resolves in the worktree is true by construction, not
only in this worktree (read). The sealer is spawned only after
`broad-gate --base <base> --record <item>` exits 0
(`skills/code-review/orchestration.md:182-189`), and `broad_gate.py` refuses
with "does not resolve" when `resolve_base` returns no commit
(`skills/verify/scripts/broad_gate.py:2954-2959`). `resolve_base` asks the
same three spellings in the same order as the sealer
(`skills/verify/scripts/broad_gate.py:647-699`, `agents/sealer.md:42-47`), so
the checkout the gate ran in resolves the base, and the respawn cannot meet
the same verdict there. The sentence names two of the three spellings; the
one it leaves out, `<base>@{upstream}`, is asked first by the sealer anyway,
so the repair does not depend on which spelling answers.

The two places the prompt named agree with it (read). `agents/sealer.md:36`
says the sealer works "in the clone the prompt names, at its HEAD", which a
prompt naming the branch worktree satisfies, and the sealer writes only
`guarantee.md` (`agents/sealer.md:30`, `:91-92`), the file the orchestrator
then commits in that worktree. The spawn paragraph
(`skills/code-review/orchestration.md:187-188`) names the base, the work
item's directory, the issue and the pull request, and names no clone, so it
neither says nor contradicts "the branch worktree itself as its clone". That
silence is a row of *Not judged* below, not a defect in this fix.

Executed: the eight modules below pass at b81719e2 in the clone.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The first spawn of the sealer names no clone, so an orchestrator can hand it a fresh `git clone`, meet `withheld — the base <name> resolves to no commit here`, and only then take this sentence's repair. Whether the spawn paragraph should name the branch worktree from the first spawn, which would leave the verdict unreachable from this cause, is a design question outside the fix range | `skills/code-review/orchestration.md:187-188` | the orchestrator, with the owner |
| `test_no_real_identifiers` and `rules --check`, which round 5's answer reports, were not run this round | `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/rounds/round-5.md:59` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck at b81719e2: `unverified` here | the branch | the orchestrator, by `broad-gate --record` once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `git log --oneline -4`, `git diff --stat` and `git diff -- skills/` of 03ee1bab..b81719e2 in the worktree | two commits, a5d4d32c and b81719e2; two files; the sentence replaced as round 5's block reads |
| `git clone --no-local -q` and `git clone -q` of the worktree into `<scratchpad>/969-round-6/` | 0, 0 |
| `rev-parse --verify --quiet` of `release/v0.22.1@{upstream}`, `origin/release/v0.22.1`, `release/v0.22.1` in the worktree, the `--no-local` clone and the plain clone | worktree 1, 0, 1; `--no-local` clone 1, 1, 1; plain clone 1, 1, 1 |
| `for-each-ref` of the clone's `refs/remotes/origin` against the worktree's `refs/heads`, names compared with `diff` | 0, 26 names each; the worktree's `refs/remotes/origin/release/v0.22.1` absent from the clone |
| `bin/test` in the `--no-local` clone over `test_one_word_one_meaning`, `test_docs_line_wrap` and the six other modules `git grep -l "code-review/orchestration.md" -- tests` names, `-q` | 0, 202 passed, 6 skipped |
