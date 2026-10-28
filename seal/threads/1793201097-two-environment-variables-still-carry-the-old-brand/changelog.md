### Changed

- **The language of the worktree guard's prompts is the plugin option `worktree_guard_language` (#1096).** `.claude-plugin/plugin.json` declares it under `userConfig`, as a string with no default, and a person sets it once in `/config` to `ko` or `en`. A value starting with `ko` gives Korean prompts and any other value English. The guard reads the option first. Where the option is empty it reads `SPECSEAL_LANG` as before, through the 0.24.x releases, and the next minor release removes that read. With neither set, the system locale decides, as before. Whoever set `SPECSEAL_LANG=ko` keeps Korean prompts after this update. To carry the choice over, they set the option to `ko` in `/config`, and can then remove the variable from their settings. The other gates still speak English only.

### Removed

- **The lint hook no longer reads `SPECSEAL_LINT` (#1096).** `hooks/lint-python.py` runs ruff only in a project that configures it, and setting the variable to `off` no longer stops it there, so such a project gets ruff's fixes on save again. No record showed the switch in use. Both READMEs lose its row.
