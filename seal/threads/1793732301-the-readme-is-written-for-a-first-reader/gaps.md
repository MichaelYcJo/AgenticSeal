# Closing memo: 1793732301-the-readme-is-written-for-a-first-reader

## Not verified

| Item | Who must answer |
|---|---|
| How GitHub's card shows `assets/seals/owl-social.png` once it is uploaded under Settings, General, Social preview. No subagent can upload it or open the card | the repository owner, who uploads it |
| How GitHub renders the new `README.md`: the owl at `assets/seals/owl.svg`, the `mermaid` workflow and the stamp at `assets/seals/owl.png`. No subagent opened a rendering of the page (S1 is read at review from the text) | the repository owner, on the branch's page on GitHub |

## Not done

The preview stays RGBA rather than RGB. Every pixel's alpha is 255, so the
image is opaque. Converting it would need a second tool after the
documented command, and then the command would no longer redraw the
committed file byte for byte (phase 1's record).

The message `skills/implement/scripts/seal.py:1060` prints when both roots
exist still says the README's *Shared or local* section "has both
commands". The section now names `seal mode` and sends the by-hand moves to
the root's own `seal/README.md`. Rewording a printed message is a script
change, which `frame/design.md` *Data & interfaces* excludes, and it would
need a case to pin it (contract rule 14), so phase 2 left it (phase 2's
record).
