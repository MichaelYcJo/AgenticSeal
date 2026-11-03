# Closing memo: 1793732301-the-readme-is-written-for-a-first-reader

## Not verified

| Item | Who must answer |
|---|---|
| How GitHub's card shows `assets/seals/owl-social.png` once it is uploaded under Settings, General, Social preview. No subagent can upload it or open the card | the repository owner, who uploads it |
| How GitHub renders the new `README.md`: the owl at `assets/seals/owl.svg`, the `mermaid` workflow and the stamp at `assets/seals/owl.png`. No subagent opened a rendering of the page (S1 is read at review from the text) | the repository owner, on the branch's page on GitHub |
| How GitHub renders the new `README.ko.md`: the same owl and stamp, and a `mermaid` workflow whose node labels are Korean. No subagent opened a rendering of the page | the repository owner, on the branch's page on GitHub |

## Not done

The preview stays RGBA rather than RGB. Every pixel's alpha is 255, so the
image is opaque. Converting it would need a second tool after the
documented command, and then the command would no longer redraw the
committed file byte for byte (phase 1's record).

The case
`tests/text/test_the_mode_is_a_row_and_a_command.py::test_both_readmes_name_the_command_before_the_by_hand_lines`
keeps its name, though neither edition now carries the by-hand lines. Its
assertions still hold the fact the frame keeps: the first block of the
section is `seal mode`, and no `mv ` stands in it. A rename changes no
assertion, and the pin table keeps the case as it is, so phase 3 left it
(phase 3's record).
