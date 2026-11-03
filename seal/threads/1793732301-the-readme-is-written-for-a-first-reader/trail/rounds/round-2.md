# Review round 2: 1793732301-the-readme-is-written-for-a-first-reader

```seal
target: 00052c56a, fixes b858a8e4f..00052c56a
```

This verifying round read the fix diff, b858a8e4f..00052c56a, in a
`git clone --no-local` at 00052c56a. It also read b858a8e4f itself: round
1's record and the orchestrator's fold of the frame (`frame/plan.md`
*Judgments of the run* row 4, and the *Scope* 1, S1 and *Data & interfaces*
edits of `frame/design.md`). The commits read are 7c1bb00fb, 8cff4fa5a,
d64965d6f, 9b44c80e5, 24c035842, d664414b6 and 00052c56a.

Facts carried from round 1 and not re-established: where the two-root
refusal lives (`skills/implement/scripts/seal.py:1055-1064`) and its pin
(`tests/skills/test_seal.py::Test_destination_root::test_refuses_two_roots_whatever_into_says`).
Also carried: that `seal mode` refuses both roots in `both_roots`
(`skills/implement/scripts/seal.py:2360-2367`, opened again this round),
and round 1's render readings at c4ad189b5 (1,169 and 1,157 pixels), used
here only to set this round's harness beside round 1's. Every verdict below
was reached on the code at 00052c56a.

The implementer's account was read as claims. The fix pass claimed a
render at 785 and 773 pixels, a pin seen red, two `seal mutate` runs red,
1185 passed and ruff clean. It also claimed that round 1's paste-ready
message would send a reader to by-hand moves that nest one root inside the
other. Each is answered below by what this round ran or read.

## Findings

This round raises no finding. No new failure path enters with the fix
diff: the only code change is the wording of an existing refusal.

## Confirmations

```seal
confirms: round-1#1
```
What holds: both editions now put the three install commands on a first
screen of 1440 by 900, as S1 states it. `README.md:33-39` and
`README.ko.md:34-40` open `## Install` and `## 설치` with the `bash` block,
and the requirement paragraph follows it unchanged (read). The lines above
each block hold *Scope* 1's items in order: owl at width 150, the title,
the plugin's sentence, the badge line, one paragraph, and the chart (read).
The two moved paragraphs stand after the uninstall sentence, still inside
`## Install` and before `### Updating`. The English one opens "This
workflow differs", and the Korean one opens "이 워크플로는" (read: `README.md:52-63`,
`README.ko.md:55-65`). That matches the folded *Scope* 1 and the plan's
outline row for `## Install`.

The round re-measured both editions (executed, `## Probes`). This round's
harness reads 757 pixels for the English install block's bottom and 746
for the Korean. The same harness reads c4ad189b5 at 1,075 and 1,064, which
is 94 and 93 pixels above round 1's 1,169 and 1,157. With that offset
added, the blocks end at about 851 and 839 under round 1's harness. The
crafter's 853 and 841 agree within 2 pixels. All three harnesses put the
block within 900 pixels. The chart stands above it, at 497 to 582 and 473
to 571, and the owl at 32 to 182. As S1 says, the measure leaves out
GitHub's page header; that limit stays under `## Not judged`.

```seal
confirms: round-1#2
```
What holds: the refusal at `skills/implement/scripts/seal.py:1059-1063`
no longer sends the person to a README section whose `seal mode` refuses
the same state. It now says "keep the root that holds the records you
want, copy across by hand what only the other holds, and delete the other.
`seal mode` refuses while both exist, too." The second sentence is true:
`both_roots` at `:2360-2367` refuses a switch while both roots carry the
marker (read).

The fix pass claimed that round 1's paste-ready text would mislead. The
claim holds, so round 1's snippet was wrong and this departure from it is
right. The snippet pointed at "the two moves by hand" in `seal/README.md`.
Those moves are at `templates/setup/seal-README.md:39-44`: `mv` of the
local root to the tree path, and `mv` of the tree root to the
common-git-directory path. In the state this message prints, the target
path already exists as a directory. POSIX `mv` then moves the source inside
it, leaving `seal/seal/` or `<git-common-dir>/seal/seal/`. Neither path is
a root the gates read (read).

Is the new instruction right and safe? It is right. Keeping one root and
deleting the other is the only end state that clears the refusal at
`:1055`, which needs both roots to carry the marker. It is safe in its
order: the copy comes before the delete, so nothing only one root holds is
lost when the steps run in sequence. The two deletions differ. A tracked
`seal/` that is deleted can be restored from git until a commit removes it,
and removing it in a commit is the same act as the by-hand move from shared
to local. A deleted `<git-common-dir>/seal/` cannot be restored. The
message covers that case by putting the copy first. A file both roots hold
with different bytes is "what only the other holds" in content, not by
name. The message does not spell that reading out, and `seal import`'s
never-overwrite merge is not reachable here, because this very refusal
stands in its way. That is a limit of a hand copy, not a false statement,
so it is no finding.

The pin was seen red this round. With the message's last sentence deleted
in the clone, three parametrisations failed and three passed (executed).
The pin also asserts that no README is named. Its comment, as 24c035842
corrected it, says the moves "it links" would nest, which matches the
section the old message named (read: `tests/skills/test_seal.py:1317-1328`).
The class was searched by words: `git grep` for "both commands",
"Move or remove one", "plugin README" and "README's *Shared" outside the
records (executed). Only two other messages print in the two-root state.
One is `seal mode`'s `both_roots`, which names no README. The other is the
pin's comment. This was a search on words, so the list is a sample. The
docstrings at `seal.py:1760` and `:2501` ("the README's `mv` by hand") stay
outside the reach round 1 gave this finding. The class names no other
printed message.

The `changelog.md` bullet the fix added states the old message, why it
misled, and the new wording, and all three match the code (read). The
paragraph `gaps.md` *Not done* dropped was the one this fix answered
(read).

```seal
confirms: round-1#3
```
What holds: the comment at
`tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:80-82` is
round 1's paste-ready text word for word. The entry's value stays 1 (read).
The module passed in this round's narrow run (executed).

```seal
confirms: none
```
What matched: the orchestrator's folds at b858a8e4f and d664414b6. *Scope*
1 now names the first screen's five items, sets them to one 1440 by 900
viewport, and says the moved paragraph's subject is named. S1's *Verifiable
how* now asks for a rendering at review, and this round took one. *Data &
interfaces* names the one script change and the one comment. `frame/plan.md`
rows 4 and 5 give the change, its grounds and its source document. Each of
these matches the code at 00052c56a (read). S1's *Then* cell still lists
"why its parties are separate" among what a reader has at the end of
`## Install`. It still holds, because the moved paragraph stands inside
that section (read).

```seal
confirms: none
```
What matched: the fix pass's run claims. This round ran ten modules in one
`bin/test -q` call: `tests/skills/test_seal.py`, the folds, hooks-hardening,
line-wrap, paste-check, shrunken-corpus, mode, census, first-setup and
records-carried modules. Result: 723 passed, exit 0 (executed). The
crafter's 1185 counts a different set, so the number was not compared.
`uvx ruff check` and `uvx ruff format --check` over the three Python files
the diff changes exited 0 (executed). The two `seal mutate` runs were not
re-run. Instead, the pin was seen red by deleting the sentence it pins.

## Not judged

| What | Location | Who answers |
|---|---|---|
| How GitHub itself renders both pages, with its repository header and file list above the article, which every harness so far leaves out. On GitHub's repository home page the README stands below the file list, so the install block cannot sit on the first screen there, whatever the page holds. The chart's label size at GitHub's column also stays unjudged | `README.md:1-39`, `README.ko.md:1-40` | the repository owner, on the branch's page on GitHub, with `gaps.md` *Not verified* rows 2 and 3 |
| Whether the plugin directory renders the relative owl path and the `mermaid` block | `frame/questions.md` Q2 | the repository owner, after the release (Q2's default) |
| Whether the social preview carries the name, and the field colour | `frame/questions.md` Q1 | the repository owner |
| The broad gate: the full suite, the repository-wide lint and the typecheck at the commit the pull request carries. The fix pass handed its suite over labelled `unverified` for the broad run, with its narrow set `executed`, and that label is honest. This round leaves nothing open, so the orchestrator's broad run is due, and then the sealer's spawn | `seal/config.md` `Broad gate` row | the orchestrator, after the rounds settle; the sealer's spawn follows it |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over ten modules (`tests/skills/test_seal.py` and the folds, hooks-hardening, line-wrap, paste-check, shrunken-corpus, mode, census, first-setup and records-carried modules) | exit 0, 723 passed |
| the last sentence of the two-root message deleted in the clone with the `Edit` tool, then `bin/test -q -p no:xdist tests/skills/test_seal.py -k test_refuses_two_roots_whatever_into_says`, then `git checkout -- skills/implement/scripts/seal.py` | exit 1, 3 failed (the `None`, `shared` and `local` parametrisations of the pin), 3 passed; the clone clean after |
| `gh api markdown -f mode=markdown -f text=<each edition>` at 00052c56a and at c4ad189b5, then headless Chrome at 1440 by 900 with `--virtual-time-budget=20000 --dump-dom` over a page wrapping the fragment with `github-markdown-css` 5.5.1 and `mermaid` 10.9.1 in a 1012-pixel container, served from a scratch directory on 127.0.0.1 | at 00052c56a: install block 666 to 757 (English) and 655 to 746 (Korean), chart 497 to 582 and 473 to 571, owl 32 to 182; at c4ad189b5: install block bottom 1,075 and 1,064 |
| `uvx ruff check` and `uvx ruff format --check` over `skills/implement/scripts/seal.py`, `tests/skills/test_seal.py`, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` | both exit 0 |
| `git grep -n -i -E` for "both roots", "Move or remove one", "Shared or local\*", "two roots", "both commands", "plugin README" and the README's `mv`, outside `seal/threads` and `.test_durations` | the two-root messages at `seal.py:1056` and `:2362`, the pin, its comment, and the docstrings at `seal.py:1760` and `:2501`; no other statement of the old message |
