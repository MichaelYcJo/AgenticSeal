### Changed

- **The release note's seal is now the terminal stamp's disc (#1009).**
  Before this, the image was the owner's SVG, rasterised by `rsvg-convert`,
  which the `seal` job installed with `apt-get`. Now
  `.github/scripts/release_seal.py` reads the cells and colours of
  `skills/verify/scripts/seal_stamp.py#build`. It paints each cell as one
  opaque square of 12 by 12 pixels in that cell's colour, with Pillow, and
  leaves the PNG transparent outside the disc. The disc is 28 cells across,
  so the PNG is 336 pixels square and the note shows it 168 CSS pixels
  wide, where the SVG was shown 160 wide. A change to the disc's mark now
  changes the terminal stamp and the release image together. The SVG and
  the `rsvg-convert` install step are gone. Releases already published keep
  their attached image. A failure to draw still leaves the note as it was
  published, with one `::warning::` line. Where Pillow is missing or the
  stamp's module will not load, the suite at the tag fails first, and that
  line names the suite's outcome.
