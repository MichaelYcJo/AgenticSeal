# Overview: 1793226631-every-release-ends-with-a-preparation-pull-request

## Why this work exists

A release ended with a preparation pull request and a tag the owner pushed by hand; the version now moves in the release's first pull request, a process row rides in its work item's fragment, and the merge to `main` tags and publishes in one run.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| `tag_release.py#decide`'s arguments | `frame/design.md` *Data & interfaces*: "One function with no I/O takes the ref, the version at `BEFORE` (or None), the version at `AFTER`, and the commit the tag `v<version at AFTER>` names (or None)". The code also takes the pushed commit and `missing`, the reason the earlier version is None | the code | S3 and S4 compare the tag's commit with the pushed commit, and S6 asks the log to say "which" reason applies, which a bare None cannot carry |
| A pushed commit whose `plugin.json` names no version | spec silent; S1 to S6 do not name it | the code passes on no tag and says so | without the arm the tag would be `vNone` |
| Where a fragment's process section ends | `frame/design.md` *Data & interfaces*: "up to the next line starting with `#`". The code ends it at the next heading, read by `unverified_check.py#heading_level` | the code | `tests/censuses.py#heading_rule` refuses a second spelling of the heading rule in a shipped script, and a wrapped line opening `#120)` is not a heading |
| Where the process table's heading and header rows come from | spec silent | `publish_release_note.py#process_shape` reads them from `templates/records/process.md` | one source for the section's shape; a constant in the script would be a second |

## Not verified

| Item | Who must answer |
|---|---|
| Whether `gh api -X POST repos/<REPO>/git/refs` with the workflow's token creates the tag on this repository (`frame/questions.md` Q4) | the orchestrator, reading `gh run list --workflow publish-release.yml --limit 1` and that run's log after 0.24.0's merge into `main` |
| `console.to_utf8()` in `tag_release.py` has no case: its mutant survived, since no census reads `.github/scripts/` | the repository owner, through the existing `seal/follow-up.md` row on `console.to_utf8()` |

## Not done

nothing

## Fed back into the spec

none
