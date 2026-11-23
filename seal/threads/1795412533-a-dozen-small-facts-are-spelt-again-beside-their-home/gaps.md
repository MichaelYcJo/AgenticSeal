# Closing memo: 1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the build's last commit, after the base merge that brings in #1576 and #1572 | the orchestrator's broad run, after the review rounds settle |

## Not done

`fold_check.py#declared` still opens `config.json` twice: once through `config_pairs` for the ceiling key, and once inside `lib/config.py#declared_policy_root`. The key is read once, which is what `frame/design.md` *Scope* item 2 asks. Reading the file once would need `declared_policy_root` to take the parsed pairs, and `frame/design.md` *Data & interfaces* gives it `home`. The second open costs one small file read per `seal fold` run, and it was so before this phase, through `policy_root`.
