# Review round 7: 1793273065-the-core-reaches-no-users-repository

target: 044da6e6, fixes a982b044..044da6e6

This is a verifying round, round 2 of the count after the reframe (round 6
was round 1). It reads the diff of round 6's fix pass: the two fix commits
`ccad9673` and `e9008079`, the orchestrator's two folds `6a925644`
(`frame/design.md`) and `756f6976` (`frame/plan.md`), and the fix pass's
record commit `044da6e6`. The core changed on the branch, so this round
read the tree's `skills/core/SKILL.md`, not the installed 0.24.2 copy.

Carried from round 6 and not searched again: the core's three sentences at
the coordinates round 6 named (`skills/core/SKILL.md:42-45`, `:84-90`,
`:101-117` at HEAD); `tests/text/test_review_axes.py#test_the_core_names_where_the_routing_question_is`
as the case that pins the routing sentence; `tests/censuses.py`
*real_identifiers* as the census that holds `CONTRIBUTING.md` *House rules*
**No real identifiers**; `evals/scripts/noninferiority.py#masked` as that
census's other reader. Re-established this round: every verdict below, the
narrow modules over the changed files, and both pinning cases red against
their fix reverted (executed, *Probes*).

## Findings

### 1. The slug census misses the projects directory of a session started in the home directory, `-Users-<name>` with no dash after the name

severity: should
location: `tests/censuses.py:903-907`, `tests/test_censuses.py:745-762`
evidence: executed `python3 -c "import sys; sys.path.insert(0, 'tests'); import censuses as c; print([m.group(0) for m in c.refused_user_paths('/private/tmp/claude-501/' + '-' + 'Users-somebody/abc/scratchpad')])"`, `ls ~/.claude/projects`
verdict: fixed f1217ac9
reopens: round-6#4

Round 6 finding 4 asked the census to read a user path spelled as a
projects directory's dashed slug, so that a slug naming a real user is
refused in CI. The close does not hold for one member of that class.
`SLUG_USER_RE` is `-Users-([\w.]+)-`: it requires a dash after the name.
A session started in the home directory itself gets a projects directory
and a scratchpad directory named `-Users-<name>`, followed by `/`, a
backtick or the end of the line. No dash follows the name, so the census
reads nothing there. The probe above prints `[]` for a scratchpad path of
that shape (executed). The case is not hypothetical: the machine this round
ran on holds one such projects directory beside the deeper ones (`ls`,
executed; the name is not written here). A record that cites a scratchpad
of a session started in a home directory, as `frame/design.md:42` cited one
of a session started in a repository, passes the census with a real user
name in it.

The trailing dash came from round 6's own paste-ready fix, which the
crafter copied as given, so the defect is the record's and not the fix
pass's. The trailing dash refuses nothing the pattern without it would
pass. Without it the name group is still greedy over word characters and
dots, so `-Users-x-repo` still reads `x` and passes, and a longer name
that opens with `x` is still read whole and refused. A placeholder
`-Users-<name>` and a pattern `-Users-[A-Za-z]` still match nothing. Over
the 625 tracked files, the census with the dash dropped refuses no line
(executed, *Probes*), the same as with it.

The comment above the pattern states its precondition in shape ("The name
is word characters") and leaves out what follows from it, which the
orchestrator asked about. A name holding a dash is read only up to its
first dash. So it is still refused, unless that first part is the fixture
user's `x`. Claude Code also spells a dot in the path as a dash, so the
same holds for a name holding a dot. The census's reader finds neither in
the comment, and round 6's record stated the first only beside its fix
block. The fix states both where the pattern stands.

```python
# A projects directory spells the path its session started in with dashes:
# `-Users-<name>-<repo>`, or `-Users-<name>` alone for a session started in
# the home directory. So a user path reaches a record that way too. Built
# from two halves, like USER_PATH_RE. The name is read as word characters
# and dots up to the first character that is neither. A name holding a dash,
# or a dot the slug spells as one, is read by its first part, and refused
# unless that part is the fixture user's. A placeholder such as `<name>` or
# a pattern such as `[A-Za-z]` is no name.
SLUG_USER_RE = re.compile("-" + r"Users-([\w.]+)")
```

```python
    def test_refuses_a_user_path_spelled_as_a_projects_directorys_slug(self, tmp_path):
        """#1177 round 6 finding 4, round 7 finding 1. A projects directory
        spells the path its session started in with dashes, so a scratchpad
        path reaches a record as `-Users-<name>-<repo>`, or as
        `-Users-<name>` alone for a session started in the home directory,
        and the slashed pattern read none of it. The fixture user `x` passes
        in that spelling too, and a placeholder or a character class is no
        user name."""
        name = "-" + "Users-somebody"
        root = plant(
            tmp_path,
            "leak.md",
            f"a draft at /private/tmp/claude-501/{name}-Documents-GitHub-repo/s\n"
            "a fixture at ~/.claude/projects/-Users-x-repo/1.jsonl\n"
            "a pattern `-Users-[A-Za-z]` and a placeholder -Users-<name>-repo\n"
            f"a home session at ~/.claude/projects/{name}/1.jsonl\n"
            "a home fixture at ~/.claude/projects/-Users-x/1.jsonl\n",
        )
        refused = (
            f"real_identifiers: {name} is a real user path, and "
            "fixtures use /Users/x/"
        )
        assert censuses.real_identifiers("leak.md", root) == [
            f"leak.md:1: {refused}",
            f"leak.md:4: {refused}",
        ]
```

This round did not run the case. Against HEAD's pattern it fails: the
probe above shows the census reads nothing on the fourth line's shape, and
it reads the first line's slug with its trailing dash. With the dash
dropped, the probe reads both lines' slug as `{name}`, and the tree's
census stays clean (executed, *Probes*). The fix pass shows the case red
before it commits it.

answer: `tests/censuses.py#SLUG_USER_RE` drops its trailing dash, and the comment above it is the finding's text: it names the home-directory spelling, and says that a name holding a dash, or a dot the slug spells as one, is read by its first part and refused unless that part is the fixture user's. `tests/test_censuses.py#Test_real_identifiers::test_refuses_a_user_path_spelled_as_a_projects_directorys_slug` is the finding's case, with the user name built from halves. It adds a home session line naming a user other than `x`, which is refused, and a home fixture line for `x`, which passes. Against the dashed pattern, `bin/test -q -p no:xdist tests/test_censuses.py -k projects_directorys_slug` failed 1 (exit 1): the census refused line 1 and not line 4. After the fix, the same command passed 1 (exit 0). `bin/test -q tests/test_censuses.py` passed 176 (exit 0). `git grep -n -E -- "-Users-[A-Za-z0-9_.]+"` outside `.test_durations` finds 14 lines, and every match is the fixture user `x`.

## Confirmations

confirms: round-6#1
The scope sentence at `skills/core/SKILL.md:102-105` is round 6's text word
for word, and it reads one way (read). "This test of whether a mechanism
stays" names the bold lead's test, so it no longer scopes the section's
other sentences, which keep the reach `:18` gives them: work run through
the workflow. "a gate, a check, a hook, a CI step or a rule among them" is
an absolute phrase closed by "among them". It cannot be read as more
objects of "governs", and the clause after the semicolon gives a user's
repository's mechanisms to that repository's own policy. The orchestrator
asked whether "a rule" carries the test to the core's own rules or to a
skill's prose in a way the frame did not intend. It does not. The list is
`CONTRIBUTING.md:378-382`'s, "a mechanism (a gate, a checker, a hook, a CI
step, a rule)", which already holds a rule this plugin adds to the same
test through its `## Removes`. The core before phase 8 (`git show
6ebfada5:skills/core/SKILL.md`, executed) put no limit on the kinds at all,
so the list restores that reach rather than widening it. A rule is now
among the mechanisms the test governs, and the section heading calls the
test itself "The rule", so the test governs its own keep. That is how
`## Removes` already treats a rule. The test decides whether a mechanism
stays through a change the owner merges. It gives no agent licence to skip
a rule mid-run, which `:92-97` and the contract hold apart. A skill's prose
that states no rule is no mechanism and is not reached. `frame/design.md`
*Scope* item 10 *Whose mechanisms* (`:224-232`), as folded at `6a925644`,
states the same kinds and the same naming of the test, so the core and the
frame agree. `git grep` on "gates, checks and hooks", "This rule governs"
and "keeps or drops" outside the round records finds the new sentence alone
(executed).

confirms: round-6#2
`skills/core/SKILL.md:42-45` reads "What a script answers exactly, such as
the suite, the lint, the broad gate and the merge check, stays a script,
and the session waits on its exit code rather than reasoning about what it
would print" (read). Both directives reach the class again, the four
scripts stand as examples, and the sentence differs from the one at
`6ebfada5` only by "such as" and "and", which add no directive. `git grep`
on "answer exactly and stay" finds nothing outside the round records
(executed).

confirms: round-6#3
`skills/core/SKILL.md:85-90` names the question in the middle clause,
"puts the routing question as" (read), and no pronoun in the paragraph has
"that batch" as its nearest noun. The case's new assertion pins the clause.
With the clause reverted to "puts it as" in this round's clone,
`bin/test -q -p no:xdist` over the case failed; with it restored, the case
passed in the narrow run (executed, *Probes*).

confirms: none
`frame/design.md:42`, folded at `6a925644`, cites the draft as
`<scratchpad>/core-draft/SKILL.md`, and *Scope* item 11 (`:238`) cites it as
"the path *Grounding* names", so the citation still resolves within the
frame (read). The census over every tracked file at HEAD refuses no line
(executed, *Probes*). Round 6 finding 4's case is red against the census
without the slug arm and green with it (executed, *Probes*), and
`evals/scripts/noninferiority.py#masked`, which now also replaces a slug by
the fixture path, passes its module in the narrow run. A slug match starts
and ends at a dash, which a JSON escape never holds, so `apart` is not
reached by the new arm (read `evals/scripts/noninferiority.py:236-290`).

confirms: none
The token figures in current-state text agree with the core at HEAD. The
hook's output at HEAD is the 6,180 B body below the frontmatter under a
header whose length is the printed path's: 6,481 B in this round's clone,
whose path is long, about 6,350 B under a plugin cache path (executed,
*Probes*). At the meter's assumed 3.2 B per token that is about 1,980 to
2,030 tokens. `changelog.md:3` gives "about 1,980" and `frame/plan.md:102`
gives "about 2,000" (read), so the plan's fold at `756f6976` and the
fragment state the same fact at two roundings and contradict nothing.
`git grep` for "1,950", "2,100", "6,180", "6,347" and "6,853" outside
`.test_durations` finds the old figures only in phase and round records,
which are history of their commits (`trail/phases/phase-10.md:48` among
them), and in `frame/design.md:41`, a grounding row measured at its own
commit (executed). No current-state text carries "about 1,950".

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `044da6e6`. Contract rule 2 keeps them from this round; `trail/gate.md` and `guarantee.md` are stale against this range | the tree | the orchestrator, through `seal gate` |
| Whether the core's three rewritten sentences need S11 run again, carried from round 6. Each changes a sentence after the commit S11's runs read, and `gaps.md` *Not verified* records the owner's decision of 2026-10-30 not to run the proofer's and crafter's sides | `skills/core/SKILL.md` | the orchestrator |
| Whether the real user path round 6 finding 4 removed from the tree must also leave the pushed history. `4d436388` added it, and the branch's commits stand on the remote behind PR #1186 until the squash; the squash keeps it out of `main`, and the commits the pull request holds keep it | the remote's refs for PR #1186 | the owner |
| `frame/questions.md` Q2 and Q3, carried from round 6 | `frame/questions.md` | the owner after the release (Q2); anyone with an `ANTHROPIC_API_KEY` (Q3) |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/test_censuses.py tests/text/test_review_axes.py tests/hooks/test_core.py tests/evals/test_noninferiority.py tests/skills/test_core_check.py` in this round's clone at `044da6e6` | exit 0, 486 passed |
| The core's middle clause edited back to "puts it as" and the `SLUG_USER_RE` arm dropped from `refused_user_paths`, both with the `Edit` tool in the clone, then `bin/test -q -p no:xdist tests/text/test_review_axes.py tests/test_censuses.py -k "test_the_core_names_where_the_routing_question_is or projects_directorys_slug"`; both edits undone the same way | exit 1, 2 failed: `test_the_core_names_where_the_routing_question_is`, `test_refuses_a_user_path_spelled_as_a_projects_directorys_slug`; `git status --short` empty after |
| `python3 -c` calling `censuses.real_identifiers` on every file `git ls-files` lists, as committed, then with `SLUG_USER_RE` rebound to `"-" + r"Users-([\w.]+)"` in the same process, and `refused_user_paths` on a scratchpad path built as `'-' + 'Users-somebody'` followed by `/`, and on the same name at the end of a line | 625 files, no refusal either way; as committed, both home-directory lines return `[]`; with the dash dropped, both return the slug, and the fixture, placeholder and pattern lines return nothing |
| `python3 -c` over `hooks/lib/core.py#output('.', '.')` in the clone, the header line's bytes and the rest | 6,481 B whole, 301 B header, 6,180 B body; `wc -c skills/core/SKILL.md` 6,853 B |
| `git grep -n -E` for the token and byte figures, outside `.test_durations` | the hits *Confirmations* names, and nothing in a current-state text but `changelog.md:3` and `frame/plan.md:102` |
