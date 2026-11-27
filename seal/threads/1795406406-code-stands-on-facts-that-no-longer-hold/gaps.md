# Closing memo: 1795406406-code-stands-on-facts-that-no-longer-hold

## Not verified

| Item | Who must answer |
|---|---|
| closed The close-issues workflow without the label step, on a push to `main`: the close runs, and the roll runs after it even where the close failed. A14 reads the workflow's YAML and no run of the workflow was made | answered: `close-issues-on-release.yml` run 45961118322 passed when 0.39.3 reached `main` |

## Not done

The message `skills/settle/scripts/settle.py` prints for a `trail/rounds` it cannot count, "its trail/rounds is not a directory this can list, so no round was counted", was left as it is when phase 2 removed the file state. Each state it is still printed for, a link and a directory nothing can list, fits those words, and rewording a line a person reads would need its own pinned case for no gain in what it says (`trail/phases/phase-2.md`).
