# Review round 2: 1793174170-two-facts-kept-in-several-files-have-drifted

target: f9bba0a7, fixes 64293c0d..f9bba0a7

## Findings

None. The fix range holds three commits: `21369c34`, the fix pass; `7f8ff5cc`, its answers in `trail/rounds/round-1.md`; and `f9bba0a7`, the orchestrator's close of two rows in `gaps.md`. This round read all three and nothing outside them.

## Confirmations

confirms: round-1#1
The close holds. `README.md:176` and `README.ko.md:170` carry round 1's replacement Where cells, word for word (read, `git diff 64293c0d..f9bba0a7`). `hooks/implementer-notice.py:147` returns where `optin.opted_in(cwd)` is false, and the opt-in is what both cells now state, so the cells match the hook. *First run* and the records table's `seal/` row were left unchanged. They select by `` `seal/` `` in the Where column, and that selection now includes the notice. The gate table's Where cells in both editions hold no other cell that points at another row (read, `README.md:172-186`, `README.ko.md:166-180`).

The new guard in `tests/behaviour/test_first_setup_asks_once.py:666-675`, read as code, makes two checks. The second is that a row opening `| implementer-notice |` stands among the rows whose Where cell names `` `seal/` ``. It pins this instance whatever words a later edit puts there, so any rewording that drops `seal/` goes red. The first refuses a Where cell opening with "same " or "같은 ". That covers two spellings of a pointer to another row, and the ways to write one are unbounded: "Same opt-in" with a capital, "as above" and "위와 같음" all pass it. So the comment's "Each cell names its condition itself" claims more than the check enforces. The fix pass's answer also overstates when it calls the two prefixes "the class a pointer by `seal/` drops". This does not reopen the finding, because the instance the finding named is pinned by the membership assertion. The limit is that a future row could point at another row in other words, and only a reader catches that. The module passed in this round's run (executed).

confirms: round-1#2
The close holds. `README.ko.md:168` now reads "옮길 것이 있는 디렉터리 아래에 커밋하지 않은 변경이 있으면 하나도 옮기지 않는다. 옮긴 것은 한 줄로 알린다." (read). Read against `hooks/root-migrate.py:153-191`, the check is on the directories the units come from, which "옮길 것이 있는 디렉터리" names, and a refusal moves nothing, which "하나도 옮기지 않는다" says. The one-line notice is now its own sentence, no longer inside the refusal's conditional, so it says what the English row says at `README.md:174`. The rest of the Korean row did not change. As the fix pass's answer says, no case pins the sentence's meaning, and `frame/design.md` *Out of scope* keeps that a reader's to check.

confirms: none
The two rows `f9bba0a7` closed in `gaps.md` *Not verified* say what round 1 found (read, `gaps.md:20-21`). Round 1 read the `worktree_consent` and `root-migrate` cells of both editions against the hooks and found every one sound but the Korean `root-migrate` Does cell. It read the other rewritten Korean sentences as saying what the English ones say. Both rows name finding 2 and `21369c34` as what corrected the one exception. The open row that remains is the broad gate, which the orchestrator answers.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `f9bba0a7`. Nothing remains open from the review rounds, so this is what comes due next, then the sealer's spawn | the whole tree | the orchestrator, through `seal gate` (contract rule 2) |
| The fix pass's red-first run and its two `seal mutate` mutants. This round read the guard and ran the module green, and re-ran neither | `tests/behaviour/test_first_setup_asks_once.py` | the sealer, which samples the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the 47 modules that `git grep -l` finds naming `README.md` or `README.ko.md` under `tests/`, `-q -p no:cacheprovider` | 2856 passed, 4 skipped, exit 0. The first attempt passed the module list as one word under zsh and exited 5 having collected nothing; it was run again with the list split |
| `bin/seal layout --check` | exit 0, 158 files read, 0 refused |
