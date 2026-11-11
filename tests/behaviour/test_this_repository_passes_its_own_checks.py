"""Each check and reader this plugin ships, run over this repository's own
tree, refuses nothing.

The cases here run a shipped command over the tree itself rather than over a
fixture: `seal rules --check`, `seal layout --check`, `seal fold`,
`seal unverified` and `lib/routing.py`'s reader of the routing declarations.
Each reads files beyond its script, so it stands in a file that declares no
`TARGET` (`CONTRIBUTING.md` *The test layout*). Each script's own file
keeps the cases over fixtures and the helpers these cases call.
"""

import fnmatch
import glob
import os
import re
import shutil

from conftest import ROOT
from test_fold_check import command, fold_check
from test_routing import _absent_optional_rows_read_as_nothing
from test_rules import rules
from test_test_layout import layout
from test_unverified_check import run

# No TARGET: its cases run each shipped check over this repository's own tree.


# The bucket the tree-wide case plants one defect in for the policy root's
# documents, which no `RULE_FILES` glob names (`rules.py#policy_documents`).
POLICY_DOCUMENTS = "the policy root"


def declared():
    """`(ceiling, policy root)` as this repository's `seal/config.json` states
    them, read by the shipped command's own reader."""
    return fold_check.declared(fold_check.seal_home(ROOT))


class Test_seal_rules:
    def test_every_check_line_in_the_tree_holds(self, tmp_path, capsys):
        """The fact read on every pull request: `seal rules --check` over this tree is
        exit 0. On a scratch copy of what the check reads (the rule files, the
        files their targets name and the tests carrying their markers) one target
        renamed is exit 1 naming its line, and so is a check line naming a gone
        file, planted in a file of every other rule-file glob and in a document
        of the policy root, so a walk that read the policy root alone, or read
        a renamed target as resolving, goes red here. The pending designs
        are copied too, so a line a pending `remove` excuses stays excused, and
        no defect is planted in a file such a `remove` names."""
        assert rules.main(["--check", "--root", ROOT]) == 0, capsys.readouterr().out
        capsys.readouterr()
        files = rules.rule_files(ROOT)
        carriers = rules.markers(ROOT)
        designs = glob.glob(os.path.join(ROOT, "seal", "threads", "*", "frame", "*.md"))
        for path in designs:
            destination = tmp_path / os.path.relpath(path, ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, destination)
        home = os.path.join(ROOT, "seal")
        policy = rules.sibling("config").policy_root(home)
        pending = rules.sibling("rule_changes").pending(home, policy)
        removing = {o.file for o, _ in pending if o.kind == "remove"}
        named, renamed = {}, None
        for rel, text in files.items():
            held = [(n, rules.parse(line)[0]) for n, _, line in rules.check_lines(text)]
            for target in (t for _, targets in held for t in targets):
                if rules.MARKER.fullmatch(target):
                    sources = [path for path, _, _ in carriers.get(target, ())]
                elif target.endswith("/"):
                    sources = [target + rules.EVAL_CASE]
                else:
                    sources = [target]
                for source in sources:
                    origin = os.path.join(ROOT, *source.split("/"))
                    if not os.path.isfile(origin):
                        continue  # an excused line's target, gone from the tree
                    destination = tmp_path / source
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(origin, destination)
            pattern = next(
                (p for p in rules.RULE_FILES if fnmatch.fnmatchcase(rel, p)),
                POLICY_DOCUMENTS,
            )
            line = next((n for n, targets in held if targets), None)
            # One file per glob carries the planted defect, so a glob whose first
            # file names no target is planted there, not renamed in a later one.
            # A file a pending `remove` names carries none.
            if rel in removing:
                pass
            elif renamed is None and line is not None and pattern not in named:
                lines = text.split("\n")
                first = rules.parse(lines[line - 1].strip())[0][0]
                lines[line - 1] = lines[line - 1].replace(
                    first, f"{first}-renamed-away", 1
                )
                text, renamed, named[pattern] = "\n".join(lines), rel, rel
            elif pattern not in named:
                text += "\n\ncheck: tests/test_planted_and_gone.py\n"
                named[pattern] = rel
            destination = tmp_path / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(text, "utf-8", newline="\n")
        assert renamed is not None, "no rule file in the tree names a target"
        assert set(named) == {*rules.RULE_FILES, POLICY_DOCUMENTS}, named
        assert rules.main(["--check", "--root", str(tmp_path)]) == 1
        out = capsys.readouterr().out
        assert re.search(
            rf"^seal rules: {re.escape(renamed)}:\d+: .*-renamed-away", out, re.M
        )
        for rel in named.values():
            assert re.search(rf"^seal rules: {re.escape(rel)}:\d+: ", out, re.M), (
                rel,
                out,
            )
        assert f"seal rules: {len(named)} refused in " in out, out


class Test_seal_layout:
    def test_accepts_this_repositorys_tests(self, capsys):
        assert layout.main(["--check", os.path.join(ROOT, "tests")]) == 0
        out = capsys.readouterr().out
        assert "refused:" not in out, out
        assert "tests/skills/test_test_layout.py: declares no TARGET" not in out
        assert "declare no TARGET" in out.splitlines()[-1]


class Test_seal_fold:
    def test_accepts_this_repository_with_no_flags(self):
        """S1 and S13: the values come from `seal/config.json`, every check runs,
        and a document past the ceiling is named and does not fail the run."""
        code, out, err = command("--root", ROOT)
        assert code == 0, (out, err)
        ceiling, policy = declared()
        assert f" under {policy}/ to {ceiling} estimated tokens" in out, out
        for rel, tokens in fold_check.past_ceiling(ROOT, policy, ceiling):
            assert f"{rel} is about {tokens} tokens, past the ceiling" in out, out
        assert f"seal fold: the index {policy}/README.md names every document" in out


class Test_seal_unverified:
    def test_this_repositorys_own_overviews_are_all_readable(self):
        """The corpus is the real test, and it states the rule for new work:
        a work item that writes an overview writes this section in it."""
        assert run([os.path.join(ROOT, "seal", "threads")]) == 0


class Test_routing_declarations:
    def test_every_declaration_in_this_repository_still_parses(self):
        """Executed against the real files, not a fixture: the declarations
        committed here are the population the optional rows exist for.

        S8 of #84 extends it rather than opening a second case beside it. What an
        optional row has to survive is a declaration that does not carry it -- a
        required row, or a row whose absence took the declaration down, would
        make every one of those no declaration, and the pull request's check
        would read the branch each names as undeclared. So the assertion is over
        the declarations that OMIT each row, and never over how many answer it:
        #351 wrote the first `Planning` answer, and a case premised on nobody
        answering goes red on the commit that writes one rather than on a defect.

        The vacuity guard is over the axes together, not per axis. Every
        committed declaration answers `Implementation`, so a per-axis guard would
        be red the day it was written.

        All three optional rows are swept rather than the two that existed first.

        No count is written down here either. The docstring this replaced carried
        two -- `the twelve committed here` and `Seventy-two declarations` -- for a
        tree that held 73, and a number in a docstring is a claim nothing reads.
        """
        import glob

        found = sorted(
            glob.glob(os.path.join(ROOT, "seal", "threads", "*", "routing.md"))
        )
        # `assert found` and the vacuity guard over `omitted` stood here, and both
        # were floors a fold turns red (#517). The first asked whether the glob
        # found the declarations that are there, and is asked of the tree instead:
        # a second listing, by `os.listdir`, has to agree with it at any size.
        # The second asked whether the corpus holds a declaration that omits an
        # optional row, which is a question about what the repository happens to
        # hold, and it moves to
        # `test_an_absent_optional_row_reads_as_nothing_over_a_built_declaration`.
        specs = os.path.join(ROOT, "seal", "threads")
        listed = sorted(
            os.path.join(specs, n, "routing.md")
            for n in (os.listdir(specs) if os.path.isdir(specs) else [])
            if os.path.isfile(os.path.join(specs, n, "routing.md"))
        )
        assert [os.path.normpath(p) for p in found] == [
            os.path.normpath(p) for p in listed
        ], "the glob and the listing disagree about which declarations exist"
        _absent_optional_rows_read_as_nothing(found)
