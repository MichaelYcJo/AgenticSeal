# Questions for the planner: #1204, two config rows show the seal mark on the pull request body and the release note

The issue left these judgments open, and the tree answered each. Their
grounds stand where each line points, and nobody needs to reopen them:

- The rows' exact names: `frame/design.md` *Data & interfaces*, the rows.
- Where a pull request body's image is served from, and what that ties a user's repository to: `plan.md` rows A4 to A7, and `frame/design.md` *Data & interfaces*.
- Whether the plugin ships the release-note step to a user's repository: `plan.md` row A8.
- The keep test, and what goes in return: `frame/design.md` *Removes*, its last row.
- When the mark counts as sealed, and why the orchestrator runs `seal pr-body` once more: `plan.md` rows A1 to A3.
- What the release note shows with its row off: `plan.md` row A9.
- Where the release row is documented: `plan.md` row A10.
- What a refused or unread row does: `plan.md` row A11.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does a pull request body holding the mark line show the icon on the pull request's page in a browser, at desktop and at phone width? | a measurement | It is read on the first pull request whose body `seal pr-body` from 0.28.0 or later writes after a seal, in a repository whose row reads `yes`. If it shows no image, the address or GitHub's handling of it changed, and the mark line is repaired in a later change; the rows and the condition stay. | The mark line as `frame/design.md` *Data & interfaces* gives it. | open |
| Q2 | Does the mark look as the owner wants where it now appears? Three looks: the mark under the body's heading at width 128; the wax stamp drawn in a real terminal; and `assets/seals/owl.png` and `.claude-plugin/icon.png` against what the owner approved for #1174. | a person | The width is one constant in `pr_body.py`; another value is a one-line change. A stamp or a picture the owner does not accept is a new issue against #1174's drawing, outside this work. | Width 128. The stamp, `owl.png` and `icon.png` stay as they are. | open |

Q1's reason it is a row: GitHub's renderer was probed and kept the `<img>`
as written, and the address answers with the PNG (`frame/design.md`
*Grounding*). How a browser lays it out on a pull request page can be seen
only on a pull request, and opening one is a write no framer's probe makes.
This work item's own pull request is written by the installed 0.27.3 and
carries no mark (`plan.md` *Operational impact*).

Q2's reason it is a row: what the mark should look like is the owner's to
accept, and the 0.27.1 settle re-homed the last two looks to whoever reviews
the mark's new places (the issue's *Folded from the comments*). No subagent
can see a real terminal. The framer opened both pictures and recorded what
they show, which is not an approval (`frame/design.md` *Grounding*, the last
row).
