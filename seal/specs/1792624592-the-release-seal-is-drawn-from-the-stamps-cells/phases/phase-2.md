# Phase 2: 1792624592-the-release-seal-is-drawn-from-the-stamps-cells

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | ed9ec343 |

## What this phase was asked

`plan.md` phase 2. `.github/workflows/publish-release.yml` loses the
`install rsvg-convert` step and its comment, and its opening comment is
rewritten. In `tests/test_a_release_publishes_its_note.py`, the install case
goes and the `seal` job's step count becomes five. In
`.github/scripts/run_tests.py`, the Pillow paragraph of the docstring, the
comment above `PILLOW_VERSION` and the top-up's messages are rewritten.
`tests/test_the_suite_has_a_command_that_is_cheap_twice.py` gets S9's pins.
`CONTRIBUTING.md` *Running the checks* is rewritten. The two `docs/` pins
lose their `rsvg-convert` assertions. The smith runs S8's `git grep` and
writes its output here.

## What this phase found

- **S7 and S8 could not both hold as written.** S7 asks for a case holding
  that no step of the `seal` job installs `librsvg2-bin`. S8 allows that
  package name only in the `docs/` sentences. The step-count case
  therefore asserts that no step of the job runs `apt-get` at all. That is
  stricter than S7, covers the same step, and keeps S8 true. The rest of S7
  is held as written: five steps, and the step whose `pip install` carries
  `run_tests.py#PILLOW` comes before the step that runs `release_seal.py`.
- **The same sentence stood in four places `## Removes` does not list.**
  Each said that Pillow only decodes the seal, or that one pixel case reads
  it. Each is rewritten in place (contract §19):
  - the comment above `run_tests.py#PACKAGES`;
  - the `run_tests.py#add_pillow` docstring;
  - the pin comment in `.github/workflows/test.yml`;
  - the `CONTRIBUTING.md` row of `tests/test_release_hygiene.py`'s reasons
    for a pinned version.

  The search was `git grep` for `Pillow`, `PIL` and `pixel case` over
  `tests/`, `.github/` and `CONTRIBUTING.md`.
- **S9's sentences name the pixel cases in the plural,** as phase 1 found
  they must. The top-up line reads `Pillow draws the release seal, and the
  release seal's pixel cases read what it draws.` The line after a failed
  install reads `Only the release seal's pixel cases import it, so those
  cases fail with a ModuleNotFoundError and every other case runs.`
- **The pin case for the `docs/branch-and-release.md` bullet still opens with
  #718's account of the letter.** Its docstring now says that the drawing is
  pinned by #1009's S1 and S2, and that the bullet's sentence about it is
  this work item's `## Rule changes` item. The checklist case's assertion
  `from a checkout at the tag` holds both before and after the rule change,
  so it stays.
- **How each new pin was seen red.** S9's five pins went red against #832's
  two messages before `run_tests.py` changed (executed). At ed9ec343, S7's
  three halves went red as follows (executed):
  - The count went red against the six-step job, before the workflow
    changed.
  - The `apt-get` half went red under `mutation-check` with an `apt-get`
    command put into the pip step.
  - The order half went red under `mutation-check` with the pip step moved
    after the draw. It failed on `([4], [3])`.
- **S8's `git grep`, executed at ed9ec343:**
  `git grep -n -i -e rsvg -e release-seal.svg -e librsvg -- ':!seal/specs' ':!changelog' ':!.test_durations'`

  ```
  docs/branch-and-release.md:63:  the tag, draws the owner's seal from `.github/scripts/release-seal.svg` with
  docs/branch-and-release.md:64:  `rsvg-convert`, which the job installs, attaches it as `seal.png`, and
  docs/release-checklist.md:242:      a `::warning::` line: the suite at the tag did not pass, `rsvg-convert`
  docs/release-checklist.md:248:      `rsvg-convert`, run the suite with the broad gate's recorder loaded
  ```

  These are the three `## Rule changes` sentences and nothing else. The
  first runs over lines 63 and 64.
