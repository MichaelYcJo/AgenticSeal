# Questions for the planner: a pull request body past GitHub's length limit folds its longest parts

The issue left these judgments open, and the tree answered each. Their grounds stand where each line points:

- What one part is: a section after `## What changed` (`frame/plan.md` *Alternatives considered* rows 1 and 2).
- The fixed line that names a folded part's file, and why it names no commit (`frame/design.md` *Data & interfaces* D2; `frame/plan.md` *Alternatives considered* row 3).
- How `seal pr-body` says which parts it folded (`frame/design.md` *Data & interfaces* D6).
- Where the folded body stands against the `<details>` fold and the seal mark (`frame/design.md` *Data & interfaces* D3 and D4; `frame/plan.md` *Alternatives considered* row 4).
- Which documents state the limit (`frame/design.md` *Rule changes* and *Removes*; G6).
- What happens where folding cannot fit the body (`frame/design.md` *Data & interfaces* D5; `frame/plan.md` *Alternatives considered* row 5).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | In which unit does GitHub count a pull request body's 65,536 characters? The one source read reports code points, and it is a community measurement (`frame/design.md` G7). No probe here can settle it, because the probe has to send a body to GitHub, and contract rule 6 withholds posting from every agent | a measurement: whoever may post, sending `gh api -X PATCH repos/<owner>/<repo>/pulls/<N> -F body=@<file>` to a scratch pull request with a body of 65,536 Hangul syllables, then one of 65,537, and the same with emoji | Code points or UTF-16 code units: D1's UTF-16 count fits under both, and the code stands as written. UTF-8 bytes: a body in Korean passes GitHub's limit at about a third of `LIMIT`, and D1's count becomes `len(text.encode("utf-8"))` | UTF-16 code units, counted as D1 states | open |
