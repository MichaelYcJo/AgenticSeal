### Fixed

- **`seal gate`'s verdict no longer depends on the stamp's mark sprite (#1582).** The broad gate loads `skills/verify/scripts/seal_stamp.py` for the panel's text rules, and that load read `skills/verify/scripts/seal-mark.txt` and raised where the file was malformed. So a sprite cut to one line ended the gate at exit 2 with `will not load, so nothing ran`, although the gate never draws. `seal_stamp.py` now reads the sprite in `build()`, where it draws, and loading the module reads no file. A case in `tests/skills/test_broad_gate.py` runs the gate as a process with the shipped sprite and with a cut one, and requires both runs to exit 0 and print the same report.
- **`seal stamp` and `seal stamp --from` refuse a malformed sprite in one line.** They exit 2 with the sentence that names the sprite's fault, where they exited 1 in a traceback, and `--from` leaves the values file pending under its own name. `seal stamp --stop` draws nothing beside a malformed sprite, still exits 0, and leaves the file pending. `seal stamp --guarantee` queues the stamp whatever the sprite holds, where it exited 1.

### Changed

- **One rule decides whether two spellings name one commit.** `seal_stamp.py` held two. The rule that decides whether the gate prints the base's ref took a hex ref of four characters and compared case-sensitively. The rule that matches a refusal record took any seven characters and folded case. Both now ask `_same_commit`: each spelling is hex, 7 to 40 characters in either case, and one is a prefix of the other. A person sees it in two spellings of `--base`. Four to six hex characters now print `<ref> @ <commit>` on the `BROAD GATE` lines and the panel's `base` row, where the commit printed alone. An upper-case spelling of seven or more characters now prints the commit alone, where it printed `<ref> @ <commit>`.
- **A module that raises while the gate loads it ends the gate at exit 1, in Python's traceback, where it ended at exit 2 in one line.** The exception is `chain_check.py`, which the gate loads for the rounds count: its raise still leaves the count alone and the run goes on. A copy of the plugin that lacks a module the gate loads still exits 2 and names the missing file.

### Removed

- **`broad_gate.py#sibling_module`, the wrapper that turned any exception a module raised while it loaded into exit 2.** Its only recorded cause was the sprite. The arms only it fed, and its five cases, went with it. The gate calls `lib/sibling.py#load` as every other script of the plugin does.
- **`seal_stamp.py#HEX_REF`**, the pattern behind the floor of four characters.
