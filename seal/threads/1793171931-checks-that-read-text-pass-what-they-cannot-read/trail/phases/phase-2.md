# Phase 2: 1793171931-checks-that-read-text-pass-what-they-cannot-read

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 393df2cd |

## What this phase was asked

Audit family B, readers R16 to R24 of `frame/design.md` *The readers to
audit*, at `c825fd2c`, with "base version; #913" on R16, R17 and R24, whose
files #913 changes on its own branch. Each row's verdict carries an executed
probe recorded here; the probe lives in the scratch directory as `test_tmp_*`,
runs once and is deleted before the phase closes. No tree file outside the
work item directory changes.

## What this phase found

### The rows

The `Fix` cell reads as phase 1's does: `0.24.1 <module>` is one issue per
module in `release: 0.24.1`, and `0.24.1 limits` is the one issue for every
`limit` sentence.

| Row | Reader | Reads and decides | On input it cannot read | Lets through | Probe | Fix |
|---|---|---|---|---|---|---|
| R16 | `hooks/lib/config.py#config_table`, `#config_value`, `#declared_mode`, `#policy_root`, `#reference_roots`, `#hidden_lines` (base version; #913) | `seal/config.md`, a person's or `seal mode`'s; returns a value or a refusal per item, and no verdict of its own | `mixed`: a `Mode` value it cannot read is `unknown`; a doubled row, and a table the walker refuses above an item, are a refusal for that item; a `Policy root` or `Reference specs` item spelt otherwise reads as no row, which is the default; a table under a `<!--` nobody closed is refused | `no`: the reader returns values and refusals; R18 carries what the mode gate does with them, and R30 what the fold does with the default policy root | `Mode` `Shared`: read, lowercased to a mode by `declared_mode`; `**shared**`: read as written, an unknown mode; `**Mode**`: no row; `Mode` twice: refused; a comment line directly above the header: the table refused; a row below a fence nobody closed: no row; a row below a `<!--` nobody closed: refused, GFM renders no table there; `Policy Root` capitalised: `docs`; `Policy root` backticked: the value with its backticks; `Reference Specs` capitalised: the default; `Reference specs` backticked: a prefix with backticks | none |
| R17 | `hooks/lib/config.py#gfm_table`, `#read_table`, `#pact_declaration`, `#pact_signers`, `#baseline_commit` (base version; #913) | the pact's `Pact` row and `Signer` table, and the `Baseline commit` row of `seal/parity.md` | `mixed`: a baseline with no code span, in capitals, or under a row name in another case is refused naming why; a blank line between signers is refused naming the row it leaves unread; a `Pact` item spelt otherwise reads as no pact | `no`: `seal pact` refuses a signer whose config names no `Pact` row as recorded on one side only (`skills/verify/scripts/pact_check.py:558-568`, read), and a backticked signer is read as a remote no checkout has, which `seal pact` reports as not found | `` `abcdef1` ``: read; `abcdef1`, `` `ABCDEF1` `` and a `baseline commit` row: refused; emphasis around the code span and prose after it: read from the first code span; `pact` and `Pacts` rows: no pact, no refusal; a backticked `Pact` value: refused; a blank line between two signers: one signer read and the second refused | none |
| R18 | `hooks/mode-gate.py#undeclared`, `#decide`, through R16 | the `Mode` row; denies, then asks, once per session, where a root has no mode | `mixed`: a `Mode` value or item it cannot read is undeclared and the gate denies; a doubled row or a table the walker refuses is silence | `limit`: a root with no `Mode` row at all, whose table the walker refuses for another line, is let through in silence; the bootstrap writes the `Mode` row when it creates the root, so the one-issue flow never meets a root without one | a scratch repository per shape: `Mode` `shared`: silent; `**shared**` and `**Mode**`: deny; `Mode` twice: silent; no `Mode` row and a comment line directly above the header: silent; no `Mode` row and a table the walker reads: deny | 0.24.1 limits |
| R19 | `hooks/lib/optin.py` `MARKER` and `EARLIER_HEADINGS`, through `#marked` and `#earlier` | the first line of `seal/README.md` | `skips`: a first line that is not the marker byte for byte is no root, and every gate is silent there | `limit`: the README is written by setup from `templates/setup/seal-README.md`, and no work item edits it | the exact line and CRLF: marked; a trailing space, a byte order mark and a blank line first: not marked; an earlier heading: `earlier` | 0.24.1 limits |
| R20 | `hooks/stub-remove.py#is_stub`, with `#remove` | the second line of each file in the clone's git hooks folder | `mixed`: a stub whose marker is indented or on the third line is left in place; a file whose second line only begins with the marker, or whose first line holds a form feed before the marker, is removed | `limit`: the rule is that a hook without the marker line stays byte for byte, and the probe removed a person's hook whose second line begins `# specseal-git-hook-like`; no hook manager writes such a line, and the earlier release's stubs are byte-fixed | six files in a scratch folder: `pre-commit`, a CRLF `post-commit`, `persons-own-hook` and `form-feed-first-line` removed; `indented-marker` and `marker-on-line-three` left | 0.24.1 limits |
| R21 | `hooks/lib/tokens.py#given` | the bare words of a Bash command, the model's, read for the guard's consent tokens | `mixed`: a token in another case, with an underscore, without brackets, or after an apostrophe in a comment is not read, which costs a refusal; a token that is a whole quoted word is read | `no`: a read token is "an audit trail, not an authorization" (`docs/worktree-guard-spec.md:458-459`, read), and a model that types it quoted could type it bare | `[Worktree-ok]`, `[worktree_ok]`, `worktree-ok`, and the token after `person's` in a comment: none read; `git commit -m "[worktree-ok]"`: read; `echo [worktree-ok]; git worktree add ...`: read | none |
| R22 | `hooks/lib/one_heredoc.py#reduce` | one heredoc shape in a Bash command | `skips`: every near miss returns None, and the caller reads the command as written through `cmdline.py#drop_heredoc_bodies` | `no`: the wider reader takes the body out too, so a token in the body of a near miss is not read | `<<"EOF"`, `<< 'EOF'`, a terminator with a trailing space, and an unquoted `<<EOF` followed by a command: None, and `tokens.given` read no token from the body in each | none |
| R23 | `hooks/lib/cmdline.py`, `hooks/lib/cmdline_base.py`, as `hooks/worktree-guard.py` calls them | Bash commands, the model's, for a branch switch or a worktree creation | `mixed`: a git in a string handed to a shell, in `eval`, or behind a backslash inside its word is read and judged; a git spelled by a substitution or a parameter, and a brace expansion, are not read | `limit`: `docs/worktree-guard-spec.md` *Known limits* states that a word the shell builds before git runs is not read, and names the brace and substitution spellings | a scratch repository on one stream with a tracked change, `HOME` pointed at the scratch folder: `git switch feature`, `eval 'git switch feature'`, `git sw\itch feature` and `bash -c 'git switch feature'`: ask; `git rebase {main,feature}`, `git stash {branch,} y`, `$(echo git) switch feature` and `G=git; $G switch feature`: silent | none: the limit sentence stands |
| R24 | `skills/verify/scripts/pact_check.py#check`, `#grade`, `#near_miss`, `#path_map`, with `skills/verify/scripts/coordinates.py#resolve_unit` (base versions; #913) | pact anchors in a signer's designs, graded against the pact's clauses | `mixed`: an anchor under emphasis or in a code span is graded; one with curly quotes is refused; a hash with a stray letter is graded on its hex prefix; an anchor written `pact: ` with a space, or `PACT:`, is neither graded nor refused | `yes`: a stale anchor written `PACT:` or `pact: ` is never graded, so `seal pact` says nothing of it; `docs/the-record-layout.md:145-152` reads a line that holds an anchor on doubt and wants the wrong answer loud | a pact repository and a signer as siblings in the scratch folder, eight anchors at `@0000000N`: lines 5, 7 (backticked), 15 (`@0000000G`, graded as `@0000000`) and 19 (emphasised) UNMATCHED; line 17 (`## a`) BROKEN; line 13 (curly quotes) REFUSED; lines 9 (`pact: `) and 11 (`PACT:`) absent from the report; 5 anchors counted, exit 2 | 0.24.1 `pact_check.py` |

### Pairs for R43

- R16's `config_value` is read by the mode gate (R18), `seal gate`'s
  `broad_command` and `seal fold`; a refusal is silence to the hook and
  exit 2 to the commands, which `config_text`'s docstring chooses by kind.
- R17's `pact_declaration` is read by `chain_check.py`, which prints, and by
  `seal pact`, which refuses; one reader, so the two agree on what the row
  holds.
- R21's `tokens.given` is the guard's and the consent writer's one reader of
  a token (`hooks/lib/tokens.py:46`, read).

### Where the frame does not hold

- R16's tree claim, quoted from `docs/the-record-layout.md:158-162`, is that
  "a row below a comment opener nobody closed still declares". The probe
  shows `config_table` refusing that table: GFM renders no table inside an
  HTML block nobody closed, and the walker says so. The mode gate reads the
  refusal as silence and `seal gate` exits 2 on it, so no row is taken on
  doubt; the sentence in the policy document is the one that does not hold.
  It goes to `gaps.md` and to the documents' issue phase 5 files.

### The probe

`python3 -I <scratch>/c956/test_tmp_2.py > <scratch>/c956/out2.txt 2>&1; echo "exit $?"`
printed `exit 0`. It loaded each reader by path from this worktree, ran the
two hooks as subprocesses with the payload on stdin and `HOME` pointed at a
folder inside the scratch directory, and made every repository it needed
under one scratch folder. The file, its output and that folder were deleted
by their recorded paths before this record was committed.

### Q3

No row of this family reaches either situation `SECURITY.md` names. R20
removes a file only in the clone's own git hooks folder, which a clone does
not receive from the repository it clones. R19 and R18 read a root a
repository chose; a hostile one that switches its own gates off gains
nothing it did not have. R23 and R24 read text the session's model or the
signer's author typed.
