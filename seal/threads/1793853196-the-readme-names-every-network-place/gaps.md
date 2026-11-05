# Closing memo: 1793853196-the-readme-names-every-network-place

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the format check at the branch's HEAD | answered: the orchestrator's broad run at `4b7dd432` against `12d48178` passed the `Broad gate` row of `seal/config.md`, the whole suite, lint and format check (`trail/gate.md`), and `guarantee.md` sealed on it |

## Not done

- **The side effect `uv run` leaves in the user's project.** The probe in
  `trail/phases/phase-1.md` found that lint-python's first runner leaves
  `.venv` and `uv.lock` in a project whose `pyproject.toml` has a
  `[project]` table. The README's side-effects paragraph says only that
  lint-python rewrites the saved `.py` file. That is a write on the user's
  machine, not a network place, so it is outside #1382, which names the
  places the plugin reaches the network. It was left for the orchestrator
  to raise as an issue.
