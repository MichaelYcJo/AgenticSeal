# Phase 6: 1793188384-the-release-notes-are-kept-twice

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | 0ae4229a |

## What this phase was asked

Build phase 6 of `frame/plan.md`, added at `9f2f34ee`. #1041's work item
merged into `release/v0.24.0` as #1137, and `origin/release/v0.24.0` was
merged into this branch at `9477538d`. So `skills/implement/orchestration.md`
has no other owner, and `frame/questions.md` Q4's Status gives it to this
work item. Each sentence that names this plugin's gather, or the marker the
gather wrote (`:530`, `:538`, `:541` and `:578` at `9477538d`), is rewritten
in place to the release note built at the tag. A sentence that describes a
host repository's own changelog convention, which this work does not
change, is kept and recorded as kept. The file ships to other repositories,
so each paragraph is read before its sentence is judged. This work item's
`changelog.md` gains a word for it if it needs one.

## What this phase found

**The four sentences, each judged in its paragraph (read at `9477538d`).**

| Line | Paragraph | Judgment |
|---|---|---|
| `:529-530`, "the accumulated entries are gathered and dated" | *Which branch the pull request lands on*: a pull request into `main` is a release | Rewritten: "the accumulated entries go out under it". The sentence states unconditionally what any release does, and it stated the gather this work removed. The new wording names no mechanism, so it holds for this plugin, whose note is built at the tag, and for a host repository that gathers |
| `:538`, "one fragment per work item that a release gathers" | *Where an entry accumulates is the repository's convention*: two shapes a host repository may use | Kept. It names a shape of the host repository's convention, which the orchestrator reads before writing an entry |
| `:541`, "Where the repository gathers fragments, basing on `main` means running the gather" | the same paragraph | Kept. It is conditioned on the repository gathering, and it sends the reader to that repository's contribution guide for the command |
| `:577-578`, "the marker the changelog gather writes" | *One id, minted once, names the directory in every repository* | Rewritten: "the marker the release note carries above that fragment". The marker is this plugin's, and since this work the tag's workflow writes it into the note |

Rewriting `:578` pushed two lines past the 88-column wrap that
`tests/behaviour/test_docs_line_wrap.py` holds. The paragraph's last three
lines are rewrapped, and none of their words changed.

**The row's grep (executed at `0ae4229a`).** `git grep -n -i -E
"gather|changelog marker|CHANGELOG\.md|changelog/" -- skills/ agents/`,
each hit judged by whether it names this plugin's gather. `-i` makes
`CHANGELOG\.md` also match a work item's `changelog.md` fragment.

| Hit | Names this plugin's gather? |
|---|---|
| `agents/crafter.md:19`, `agents/sealer.md:76`, `skills/code-review/orchestration.md:66`, `:233`, `skills/commit-pr-convention/SKILL.md:70`, `skills/config/SKILL.md:47`, `skills/implement/SKILL.md:46`, `:115` | no: each names a work item's `changelog.md` fragment |
| `skills/implement/SKILL.md:492` | no: it says the release note is built from the fragment, rewritten in phase 4 |
| `skills/implement/orchestration.md:538`, `:541` | no: a host repository's own convention, kept as above |
| `agents/framer.md:19` | no: "Gather, judge, plan", the framer's own acts |
| `skills/implement/scripts/seal.py:2448` | no: reasons gathered before a switch |
| `skills/verify/orchestration.md:419` | no: the segment readings the flow log gathers |

So no sentence under `skills/` or `agents/` names this plugin's gather any
longer.

**`changelog.md` gains nothing.** The two rewritten sentences correct a
skill's account of the release. Nothing a user does or sees changes with
them, and the fragment's entry on the release notes already covers the
removal.

**The modules naming `orchestration.md` (executed).** 35 modules, `bin/test
-q`: 1058 passed, exit 0, after the rewrap. Before it, one case failed,
`test_prose_stays_within_the_wrap_limit[skills/implement/orchestration.md]`,
on line 578 at 90 columns and then line 580 at 89. `bin/seal layout --check`
and `bin/seal rules --check` exited 0.
