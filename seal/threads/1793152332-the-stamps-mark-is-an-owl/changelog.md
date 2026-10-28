### Changed

- **The stamp's mark is the owl (#857).** The sealer's stamp draws a 16 × 16 owl at the centre of its 28-cell wax disc, where it drew a placeholder S from 0.20.0 through 0.23.0. Every cell of the owl is one of the stamp's own reds, and no cell is shaded by its neighbours. The disc's frame and the panel beside it do not change. `skills/verify/scripts/seal-mark.txt` holds the sprite, one letter per cell, and `assets/seals/README.md` gives the owl's entry with the command that draws it again.
- **An installed user sees the owl from their first session after updating (#857).** The stamp is drawn by the installed plugin, so a session still on 0.23.0 draws the S. A stamp queued before the update and drawn after it shows the owl, because what a hook queues carries the panel's values and no disc. Nothing in a user's repository names the mark, so no repository migrates.
- **The plugin has an icon (#857).** `.claude-plugin/plugin.json` names `.claude-plugin/icon.png` as its `icon`, a 512 × 512 PNG drawn from the owl's vector, `assets/seals/owl.svg`. Claude Code ignores the field when it loads the plugin, and Anthropic's plugin directory reads it. The directory takes the icon only the first time the plugin is saved or submitted in its portal.
- **The release note's seal is the plugin's icon (#857).** The publishing job attaches `.claude-plugin/icon.png` as `seal.png`, shown at 256 CSS pixels, where it painted the stamp's disc cell by cell at 168. Where the manifest names no icon, or the file is missing or is not a PNG, the job prints one warning naming the cause, uploads nothing and leaves the note as it was published.

### Removed

- **Pillow is no longer installed (#857).** Its only reader was the release seal's painting, which is now a copy. `bin/test` no longer installs it into `.venv`, neither CI workflow installs it, and the fallback commands in `CONTRIBUTING.md` no longer name it. A `.venv` that already holds it keeps it, and nothing reads it.
