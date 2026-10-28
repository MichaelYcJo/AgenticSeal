"""`.github/scripts/tag_release.py`, one class per function.

#1117: the merge of a release into `main` tags it. The push to `main` runs
the publish workflow, whose first step decides from the push whether the
release is to be tagged, creates the `vX.Y.Z` tag where it decides to, and
passes the tag on to the note step:

  S1  the push moved `plugin.json`'s version and no tag names it: the tag is
      created on the pushed commit, through the API and in the checkout,
      and passed on
  S2  the push moved no version: nothing is created and no tag passed on
  S3  the tag already names the pushed commit, a re-run: it is passed on
      and not created again
  S4  the tag names another commit: nothing is created and no tag passed
      on, and the log names the commit the tag names
  S5  a tag pushed by hand is passed on as it is
  S6  no earlier commit to read the version at: nothing is created
  S7  a dry run prints what it would create and passes on no tag

**Nothing here reaches GitHub.** The cases that drive `main` put a `gh` of
their own first on PATH, which writes each call's arguments to a file and
answers with the exit code the case names, and they drive a real `git`
repository in `tmp_path`.

**Shown red before it was committed (contract rule 15).** Every case was
run against no script, in phase 1 of work item
`1793226631-every-release-ends-with-a-preparation-pull-request`.
"""

import importlib.util
import json
import os
import sys

import pytest
from conftest import ROOT, census_case, commit_everything, git_out, git_repo, write

TARGET = ".github/scripts/tag_release.py"

SCRIPT = os.path.join(ROOT, ".github", "scripts", "tag_release.py")

# `tests/behaviour/test_release_hygiene.py` refuses a loaded document naming the running
# version or anything above it. These are illustrative, which is the form that
# document's own message points at.
BEFORE_VERSION = "1.2.2"
VERSION = "1.2.3"
TAG = "v1.2.3"
REPO = "example/repo"
MAIN = "refs/heads/main"
PUSHED = "a" * 40
ELSEWHERE = "b" * 40
ZEROS = "0" * 40
MANIFEST = ".claude-plugin/plugin.json"


def tagger():
    spec = importlib.util.spec_from_file_location(
        "agentic_tag_release_for_tests", SCRIPT
    )
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


FAKE_GH = """import json, sys
with open({log!r}, "a", encoding="utf-8") as handle:
    handle.write(json.dumps(sys.argv[1:]) + "\\n")
if {code}:
    sys.stderr.write("HTTP 422: Reference already exists\\n")
sys.exit({code})
"""


def fake_gh(monkeypatch, where, code=0):
    """A `gh` first on PATH that logs its arguments and exits with `code`;
    the path of its log."""
    where.mkdir(parents=True, exist_ok=True)
    log = where / "calls.jsonl"
    script = where / "gh_fake.py"
    script.write_text(FAKE_GH.format(log=str(log), code=code), encoding="utf-8")
    if os.name == "nt":
        (where / "gh.cmd").write_text(
            f'@"{sys.executable}" "{script}" %*\r\n', encoding="utf-8"
        )
    else:
        stub = where / "gh"
        stub.write_text(
            f'#!/bin/sh\nexec "{sys.executable}" "{script}" "$@"\n', encoding="utf-8"
        )
        stub.chmod(0o755)
    monkeypatch.setenv("PATH", os.pathsep.join([str(where), os.environ["PATH"]]))
    return log


def calls(log):
    if not log.exists():
        return []
    return [json.loads(line) for line in log.read_text(encoding="utf-8").splitlines()]


def released(tmp_path):
    """A repository whose second commit moves the version from 1.2.2 to
    1.2.3; `(repo, before, after)`."""
    repo = git_repo(tmp_path / "repo")
    write(repo, MANIFEST, json.dumps({"version": BEFORE_VERSION}))
    before = commit_everything(repo, "the release before")
    write(repo, MANIFEST, json.dumps({"version": VERSION}))
    after = commit_everything(repo, "the release")
    return repo, before, after


def wire(monkeypatch, repo, before, after, output, **env):
    mod = tagger()
    monkeypatch.setattr(mod, "ROOT", str(repo))
    monkeypatch.setenv("REF", env.pop("REF", MAIN))
    monkeypatch.setenv("BEFORE", before)
    monkeypatch.setenv("AFTER", after)
    monkeypatch.setenv("REPO", REPO)
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    monkeypatch.delenv("DRY_RUN", raising=False)
    for key, value in env.items():
        monkeypatch.setenv(key, value)
    return mod


def local_tag(repo):
    return git_out(repo, "tag", "--list", TAG)


class Test_main:
    def test_a_push_that_moved_the_version_creates_the_tag_and_passes_it_on(
        self, monkeypatch, tmp_path, capsys
    ):
        """S1. The tag is created on the pushed commit through the API, then
        in the checkout so the note step finds it without a fetch, and
        `tag=v1.2.3` goes to `$GITHUB_OUTPUT`."""
        repo, before, after = released(tmp_path)
        log = fake_gh(monkeypatch, tmp_path / "bin")
        output = tmp_path / "github_output"
        mod = wire(monkeypatch, repo, before, after, output)
        assert mod.main() == 0
        assert calls(log) == [
            [
                "api",
                "-X",
                "POST",
                f"repos/{REPO}/git/refs",
                "-f",
                f"ref=refs/tags/{TAG}",
                "-f",
                f"sha={after}",
            ]
        ]
        assert git_out(repo, "rev-parse", f"{TAG}^{{commit}}") == after
        assert output.read_text(encoding="utf-8") == f"tag={TAG}\n"
        out = capsys.readouterr().out
        assert f"from {BEFORE_VERSION} to {VERSION}" in out, out

    def test_a_refused_creation_goes_red_and_passes_on_no_tag(
        self, monkeypatch, tmp_path, capsys
    ):
        """Exit 1 where GitHub refuses the tag, naming its error: the release
        is untagged, and the run says so rather than publishing nothing in
        silence. No tag is made in the checkout either."""
        repo, before, after = released(tmp_path)
        fake_gh(monkeypatch, tmp_path / "bin", code=1)
        output = tmp_path / "github_output"
        mod = wire(monkeypatch, repo, before, after, output)
        assert mod.main() == 1
        assert local_tag(repo) == ""
        assert output.read_text(encoding="utf-8") == "tag=\n"
        out = capsys.readouterr().out
        assert "Reference already exists" in out, out

    def test_a_dry_run_creates_nothing_and_passes_on_no_tag(
        self, monkeypatch, tmp_path, capsys
    ):
        """S7. The tag it would create and the commit are printed; no `gh`
        call is made, no tag lands in the checkout, and no tag is passed on."""
        repo, before, after = released(tmp_path)
        log = fake_gh(monkeypatch, tmp_path / "bin")
        output = tmp_path / "github_output"
        mod = wire(monkeypatch, repo, before, after, output, DRY_RUN="1")
        assert mod.main() == 0
        assert calls(log) == []
        assert local_tag(repo) == ""
        assert output.read_text(encoding="utf-8") == "tag=\n"
        out = capsys.readouterr().out
        assert f"would create {TAG} on {after}" in out, out

    def test_a_rerun_passes_on_the_tag_it_created_before(self, monkeypatch, tmp_path):
        """S3, read from the checkout: the tag the first run created is in
        the checkout's tags, so a re-run passes it on and calls nothing."""
        repo, before, after = released(tmp_path)
        git_out(repo, "tag", TAG, after)
        log = fake_gh(monkeypatch, tmp_path / "bin")
        output = tmp_path / "github_output"
        mod = wire(monkeypatch, repo, before, after, output)
        assert mod.main() == 0
        assert calls(log) == []
        assert output.read_text(encoding="utf-8") == f"tag={TAG}\n"

    @pytest.mark.parametrize(
        "before, said",
        [
            pytest.param(ZEROS, "names no earlier commit", id="all zeros"),
            pytest.param(ELSEWHERE, f"does not hold {ELSEWHERE}", id="not held"),
        ],
    )
    def test_without_an_earlier_commit_nothing_is_tagged(
        self, monkeypatch, tmp_path, capsys, before, said
    ):
        """S6, read from the checkout: a `before` of all zeros, or one the
        checkout does not hold, creates nothing, passes on no tag, and the
        log says which."""
        repo, _, after = released(tmp_path)
        log = fake_gh(monkeypatch, tmp_path / "bin")
        output = tmp_path / "github_output"
        mod = wire(monkeypatch, repo, before, after, output)
        assert mod.main() == 0
        assert calls(log) == []
        assert output.read_text(encoding="utf-8") == "tag=\n"
        assert said in capsys.readouterr().out


class Test_decide:
    def test_a_moved_version_with_no_tag_is_created(self):
        """S1's decision."""
        decided = tagger().decide(MAIN, PUSHED, BEFORE_VERSION, VERSION, None)
        assert (decided.tag, decided.create) == (TAG, True)

    def test_a_push_that_moves_no_version_tags_nothing(self):
        """S2. The log says the version did not move."""
        decided = tagger().decide(MAIN, PUSHED, VERSION, VERSION, None)
        assert (decided.tag, decided.create) == ("", False)
        assert "did not move the version" in decided.said, decided.said

    def test_a_tag_on_the_pushed_commit_is_passed_on_and_not_created(self):
        """S3. A re-run after a failed note step finds the tag it created and
        passes it on, so the note step runs and leaves a release that exists
        as it is."""
        decided = tagger().decide(MAIN, PUSHED, BEFORE_VERSION, VERSION, PUSHED)
        assert (decided.tag, decided.create) == (TAG, False)

    def test_a_tag_on_another_commit_is_neither_created_nor_passed_on(self):
        """S4. The log names the commit the tag names."""
        decided = tagger().decide(MAIN, PUSHED, BEFORE_VERSION, VERSION, ELSEWHERE)
        assert (decided.tag, decided.create) == ("", False)
        assert ELSEWHERE in decided.said, decided.said

    def test_a_tag_pushed_by_hand_is_passed_on(self):
        """S5. Nothing about the version is read for a tag push."""
        decided = tagger().decide(f"refs/tags/{TAG}", PUSHED, None, None, None)
        assert (decided.tag, decided.create) == (TAG, False)

    def test_no_earlier_version_tags_nothing_and_says_why(self):
        """S6. The reason the version before the push is unknown reaches the
        log as given."""
        why = "the push names no earlier commit"
        decided = tagger().decide(MAIN, PUSHED, None, VERSION, None, why)
        assert (decided.tag, decided.create) == ("", False)
        assert why in decided.said, decided.said


test_census = census_case(TARGET)
