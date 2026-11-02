# Closing memo: 1793599990-each-result-is-a-badge

## Not verified

| Item | Who must answer |
|---|---|
| closed Whether a reader's browser shows each badge's alt text in its place when the badge service or GitHub's image proxy cannot serve it (`frame/questions.md` Q1). No browser runs in this environment, and the alt text is written whichever way the browser draws it. | answered: the published v0.29.0 note gives every badge an `alt` naming its label and value, such as `alt="suite: 6374 passed"`, which a browser shows where it cannot load the image |
| closed How the badges look on a published release page. The cases pin the HTML, and the framer rendered a sample table through GitHub's Markdown API, but no release carrying the new header exists before v0.29.0 is tagged. | answered: the releases page of v0.29.0, fetched from https://github.com/MichaelYcJo/AgenticSeal/releases/tag/v0.29.0, renders the header with `seal.png` beside the badges served by `img.shields.io` |

## Not done

The suite's duration file, `.test_durations`, is not edited for the renamed
`results` case or the new badge-encoding case. It holds no row under the
touched cases' current names, so it is not kept in step with each rename,
and `trail/phases/phase-1.md` gives the coordinate.
