# Closing memo: 1793599990-each-result-is-a-badge

## Not verified

| Item | Who must answer |
|---|---|
| Whether a reader's browser shows each badge's alt text in its place when the badge service or GitHub's image proxy cannot serve it (`frame/questions.md` Q1). No browser runs in this environment, and the alt text is written whichever way the browser draws it. | a measurement: the owner opens v0.29.0's published note with images blocked |
| How the badges look on a published release page. The cases pin the HTML, and the framer rendered a sample table through GitHub's Markdown API, but no release carrying the new header exists before v0.29.0 is tagged. | the owner, reading v0.29.0's note once the seal job has run |

## Not done

The suite's duration file, `.test_durations`, is not edited for the renamed
`results` case or the new badge-encoding case. It holds no row under the
touched cases' current names, so it is not kept in step with each rename,
and `trail/phases/phase-1.md` gives the coordinate.
