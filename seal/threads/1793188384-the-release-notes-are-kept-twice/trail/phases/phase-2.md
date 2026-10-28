# Phase 2: 1793188384-the-release-notes-are-kept-twice

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 5b2ab235 |

## What this phase was asked

Build phase 2 of `frame/plan.md`: the `update` skill. Step 2b reads the
installed `plugin.json`'s `version`, and step 3 reads the GitHub Releases
from the public API with no token, as `frame/design.md` *Scope* item 6 says.
S7 and S8 are each seen red against the skill at `8a1173c8`, and
`tests/behaviour/test_release_hygiene.py` runs green. `frame/questions.md`
Q1 stands on its default (a): `CHANGELOG.md` is removed in phase 4, so an
installed copy at 0.23.1 or earlier stops once at its own step 2b, and phase
4's `changelog.md` says so.

## What this phase found

**How S7 and S8 were seen red (executed).** With `skills/update/SKILL.md`
unchanged from `8a1173c8` (`git diff --quiet` exit 0), the two cases failed
on their first assertions: step 2b still named `CHANGELOG.md`, and step 3
carried no `https://api.github.com/repos/`. After the build commit,
`seal mutate` broke the skill five ways over the two cases: step 2b reading
`CHANGELOG.md` again, `oldest first` dropped, `gh api` in place of `curl`, a
failed read that stops, and the repository no longer read from `origin`.
5 red, 0 survived (exit 0).

**The two commands the skill now carries ran on this machine (executed,
2026-10-28).** Step 2b's two lines printed the installed copy's
`installPath` and `0.23.1`. Step 3's `curl` exited 0, and the list it
returned held 58 releases, newest `v0.23.1`, each with a `body`. That showed
the read works, not that it is cheap: as built, the step printed the whole
list into the session, 881,917 bytes (round 1, finding 2). The fix pass's
commit `9251500c` downloads it to a file and prints only the span; for
0.22.4 to 0.23.1 that printed `v0.23.0` and `v0.23.1`, 16,760 bytes, with
`curl` and the filter each exiting 0 (executed). The `sed`
that turns the `origin` URL into `<owner>/<repo>` was also run on an
`ssh`-form URL, `git@github.com:x/y.git`, and gave `x/y`.

**Step 2b's account of why step 3 cannot see a stale copy changed with the
step.** It said step 3 reads the marketplace clone, which was true only of
the release files. It now says step 3 reads the published release notes.

**S7 keeps its name and its other assertions.** The case pins step 2b as
#157 shaped it. Only the file whose `version` is compared changed, so the
case was re-pointed in place rather than replaced.

**A limit, not guarded.** Step 3 reads one page of 100 releases, newest
first. An update that skips more than 100 releases would miss the oldest of
them. 58 releases exist today.
