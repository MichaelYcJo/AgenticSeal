# Closing memo: 1793593418-two-config-rows-show-the-seal-mark

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the format check at the work item's head. Phase 1 ran its phase-boundary set of 54 modules and `bin/seal layout --check tests`, and ran `ruff check` and `ruff format --check` on its own three changed Python files alone (`trail/phases/phase-1.md` *The phase-boundary run*, contract rule 2) | answered: `trail/gate.md`, the `Broad gate` row passed at `42883972e` against `9c61be933`, and `guarantee.md` sealed on it |
| closed The new cases of `tests/skills/test_pr_body.py` on Linux and Windows. They build git repositories and ran on macOS alone | answered: #1297's `tests` run 41395591255 at `73ebb09e6` passed on its four `windows-latest` legs and every Linux leg |
| closed Where the placement of this design's three rule changes lands. Phase 1 ran `rule_changes.py#parse` alone, with no error and no unread line; `apply_op` was not run | answered: this settle (`chore/settle-0.28-0.29`)'s `seal settle --draft` placed the design's three operations, among 54 of 54 placed (commit `9266ec7b`) |
| closed Whether a pull request page draws the mark line as the icon in a browser, at desktop and at phone width | answered: #1305's body, written by `seal pr-body` after a seal, carries the mark line, and its page at https://github.com/MichaelYcJo/AgenticSeal/pull/1305 renders it as an `<img>` of width 128 with `max-width: 100%`, so it shrinks at phone width |
| closed Whether the mark at width 128 looks as the owner wants | a measurement no record asks for: the owner's taste, on which no failure, issue or design rests; the answer would have decided the width the mark is drawn at |
| closed Phase 2's code at the tag, in the `seal` job of `.github/workflows/publish-release.yml`: the row read from the checkout's `seal/config.md`, the image attached and the two-cell header written under `yes`. The cases run `seal_release` with `gh` and the tree replaced by fixtures (`trail/phases/phase-2.md` *The cases, and how each was shown red*) | answered: publish-release run 41397352734's `seal` job read `Release note seal mark` `yes` from `seal/config.md` and printed `attached seal.png to v0.28.0 and put it in the note`; the published v0.28.0 note opens with the image cell |

## Not done

- No case runs `DRY_RUN=1` under a row other than `yes`. The dry run's only branch on the row is the draw, which the S6 cases already hold, and `release_seal.py`'s docstring states that the PNG is drawn only where the row turns the image on. A case for it would repeat S6 through a second door.
