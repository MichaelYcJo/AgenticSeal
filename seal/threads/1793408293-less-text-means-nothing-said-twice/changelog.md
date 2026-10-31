### Changed

- **The core says what "less text" means: nothing said twice, not fewer lines (#1192).** In 0.25.1, #1148 wrote its call for less text as a count, a change that removes more lines than it adds. A review finding and a question to the owner followed, and the owner answered that the count was never the criterion. `skills/core/SKILL.md` *The rule a mechanism is kept against* now says it after "A fact has one source, and every other place links to it.": a change that grows is kept where what it adds serves a reader, and a count of the lines a change adds against those it removes is context, never a criterion. The sentence rules out that one count. A limit on what one reader takes in still holds, such as the 10,000 characters the harness prints of one hook's output. No other shipped sentence or script held a change's line count as a criterion, so nothing else changes.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-10-31 | Less text means nothing said twice: a change that grows is kept where what it adds serves a reader, and a count of a change's added lines against its removed lines is context, never a criterion | #1148's issue misstated a net line count as its criterion, which cost its round 1 finding 6 and its question Q2 to the owner | https://github.com/MichaelYcJo/AgenticSeal/pull/1191#issuecomment-6534214778 |
