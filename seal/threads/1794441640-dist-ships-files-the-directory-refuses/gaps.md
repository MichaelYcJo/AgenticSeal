# Closing memo: 1794441640-dist-ships-files-the-directory-refuses

## Scope confirmation

Mark the `.svg` and `.ans` files under `assets/seals/`, `ruff.toml` and `.gitattributes` `export-ignore`, draw both readmes' header emblem from `.claude-plugin/icon.png`, and pin the archive's file types with one census case, as #1535 states.

## Not verified

| Item | Who must answer |
|---|---|
| Whether the directory's next review of `dist` lists none of these paths under `LOCAL_CODE_FILE_TYPE`, and whether it refused `.gitattributes` at all | the owner, reading the directory's page after 0.37.5's `dist` commit; no script can reach the page |

## Not done

The frontmatter keys `skills`, `user-invocable` and `disable-model-invocation` stay, though the directory may refuse them. Each changes what the plugin does, so removing one is a behaviour change and belongs to #1420.

`assets/seals/README.md` embeds `horned-owl.svg`, which does not resolve in `dist`'s copy of the page. The page keeps the vector drawing for `main`, where a reader of the drawings' history opens it.
