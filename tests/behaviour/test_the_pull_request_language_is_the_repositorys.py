"""The pull request language is the repository's, stated in `seal/config.json`.

`skills/commit-pr-convention/SKILL.md` required English at five places, and a
repository whose team writes another language had nowhere to say otherwise.
One key now answers for all four prose surfaces — commit subject, commit
body, pull request title, pull request body — and absence means English, so
a repository that says nothing is unaffected (#82).

No gate reads the key, and the reason is recorded rather than
left as an absence a later reader takes for an oversight: judging what
language a commit message is in means being wrong about names, identifiers
and quoted English, and a wrong stop blocks a correct commit. The mechanism
is the skill's text, the way it already is for the prefix vocabulary. So the
cases here read the reader this file loads, and the spellings the skill and
the template name: the file, the key, the branch shapes, the mirror's name.
The skill's sentences around them are the proofer's to read.
"""

import glob
import json
import os
import subprocess

import pytest
from conftest import ROOT, config_json, flat, local_home, read

# No TARGET: its cases hold the language rows across skills/commit-pr-convention/SKILL.md, templates/setup/config.md and lib/config.py, and walk every template and pull request mirror git lists.


SKILL = ("skills", "commit-pr-convention", "SKILL.md")
TEMPLATE = ("templates", "setup", "config.md")


# --- the key, and where it is read from -------------------------------------


def test_the_skill_names_the_file_and_the_row():
    """S1. Both halves: a session that knows the path but not the key does
    not know what to look for, and one that knows the key but not the path
    has nowhere to look. #1454: the file is `config.json`."""
    text = flat(*SKILL)
    # The file name a session opens for the key.
    assert "config.json" in text, "the skill does not name the file it reads"
    # The key. A session looks for it in the file because the skill tells it
    # to. No hook or command of the plugin asks for this key; the cases of
    # this file read it through `lib/config.py#declared_value`.
    assert "Commit and pull request language" in text, "the skill does not name the key"


def test_the_root_is_resolved_rather_than_spelled():
    """S3. Local mode (#80) keeps the whole root under the common git
    directory. A skill that spells `<repo>/seal/` and stops sends a
    local-mode session to a path that is not there, and the config it then
    reports missing is the file that exists."""
    text = flat(*SKILL)
    # The command a session runs to find the local-mode root.
    assert "git rev-parse --git-common-dir" in text, (
        "the skill spells one place for the root, so a local-mode repository "
        "cannot carry a config at all"
    )
    # The path of the shared root, which a session opens first.
    assert "<repo>/seal/" in text, "the shared place went with the fix"


# --- what the row deliberately does not reach -------------------------------


# The four branch shapes, `<prefix>/<issue number>-<slug>`,
# `feat/110-117-<slug>`, `<prefix>/<slug>` and `release/vX.Y.Z`, which a
# session copies when it cuts a branch; the last is the one
# `.github/scripts/label_merged_on_release_branch.py#RELEASE_BRANCH` matches.
BRANCH_SHAPES = (
    "A branch cut from an issue is `<prefix>/<issue number>-<slug>`.",
    "A branch for two issues joins their numbers with a hyphen: `feat/110-117-<slug>`.",
    "A change with no issue has the slug alone: `<prefix>/<slug>`.",
    "A release branch is `release/vX.Y.Z`.",
)


def test_the_branch_names_section_states_the_shapes_and_the_list_links_it():
    """S6 of #940. The issue-number rule lives in *Branch names*, in place:
    the four shapes are stated there, and the exclusion list links the
    section. Whether a second statement of a shape or an example carrying a
    number that is not an issue's, as `perf/403-…` did, is back is the
    proofer's to read."""
    text = read(*SKILL)
    # The heading the exclusion list's citation *Branch names* resolves to.
    assert "## Branch names" in text, "the section was renamed; this case is now blind"
    section = " ".join(text.split("## Branch names", 1)[1].split("\n## ", 1)[0].split())
    for shape in BRANCH_SHAPES:
        assert shape in section, f"*Branch names* does not state {shape!r}"
    head = " ".join(text.split("## Branch names", 1)[0].split())
    # The citation *Branch names*, which a session reading the exclusion list
    # resolves to the section that states the shapes.
    assert "*Branch names* below states their shape" in head, (
        "the exclusion list no longer links the section that states the shape"
    )


# --- the mirror -------------------------------------------------------------


def test_the_mirror_is_named_for_its_own_language():
    """S7. The mirror is named for its own language, which since #1453 is
    the commit language of a repository whose two language keys differ:
    `pr.ko.md` where the records are English and the team writes Korean,
    `pr.en.md` the other way round.

    Both directions are asserted. One alone reads as an example rather than
    a rule, and an example is what a session copies literally."""
    text = flat(*SKILL)
    # The mirror's file name, and its two instances, which a session writes
    # and `seal pr-body` reads.
    assert "pr.<lang>.md" in text, "the mirror's name is still fixed to one language"
    assert "pr.ko.md" in text and "pr.en.md" in text, (
        "only one direction is given, so the rule reads as an example"
    )


def test_the_existing_mirrors_are_consistent_with_the_rule():
    """The twelve committed files, checked against the rule rather than
    assumed to match it.

    Round 1 🟡 5: this used to assert `seal/config.md` does not EXIST, so a
    repository that legitimately created one — holding the template's own
    default row, even — turned it red. Existence was never the question. The
    row is, and it is read the same way a session reads it.

    Round 2 found that fix reproducing the same defect one line over, and the
    two assertions below are in the order the finding pairs demand.
    """

    mirrors = sorted(
        os.path.basename(p)
        for p in glob.glob(os.path.join(ROOT, "seal", "threads", "*", "pr.*.md"))
    )
    # `assert mirrors, "... this case is blind"` stood here, and every mirror
    # lives in a directory the next fold retires (#517). Blindness is asked
    # of the tree instead, by a second listing that has to agree at any size,
    # and the rule's teeth move to
    # `test_a_mirror_named_for_a_country_is_refused_by_the_same_rule`.
    # `pr.md` is a file of the body's first part, not a mirror, and the glob
    # does not match it, so the listing leaves it out too (#1415).
    threads = os.path.join(ROOT, "seal", "threads")
    listed = sorted(
        name
        for d in (os.listdir(threads) if os.path.isdir(threads) else [])
        if os.path.isdir(os.path.join(threads, d))
        for name in os.listdir(os.path.join(threads, d))
        if name.startswith("pr.") and name.endswith(".md") and name != "pr.md"
    )
    assert mirrors == listed, "the glob and the listing disagree about the mirrors"

    # 🟡 7 first, and unconditionally: every mirror is named for A language.
    # Narrowing to "not the body's own" dropped that, and `pr.kr.md` — `kr`
    # is a country, `ko` the language — is the mistake twelve files are one
    # copy away from. It would have stayed green.
    unknown = unknown_mirrors(mirrors)
    assert not unknown, (
        f"a mirror is not named for a language this file knows: {unknown}. "
        f"Known codes: {sorted(LANGUAGE_CODES.values())} — `kr` is a country "
        "and `ko` is the language, which is the near miss to check for first"
    )

    # 🔴 1: the template licenses "a language's English name" in as many
    # words, so `French` is a legitimate config and a three-entry dictionary
    # is always one short. A language with no code here is a gap in the
    # dictionary rather than a defect in the repository.
    commit = configured_language()
    record = configured_language(row=RECORD_ROW)
    refused = mirror_to_refuse(record)
    if refused is None:
        pytest.skip(
            f"this repository's record language is {record!r} and this file "
            "has no code for it, so which mirror name to refuse cannot be "
            "computed. The rule still holds; adding the code to "
            "LANGUAGE_CODES is what makes it checkable again"
        )
    assert refused not in mirrors, (
        f"{refused} is named for the records' own language, which `pr.md` "
        f"already holds, so it is no mirror. This repository's record "
        f"language is {record}"
    )
    # #1453: where the two keys differ, the mirror is written in the commit
    # language, and it is named for that language.
    wanted = the_mirror(commit, record)
    if wanted is not None:
        stray = [name for name in mirrors if name != wanted]
        assert not stray, (
            f"{stray} is not named for this repository's commit language, "
            f"{commit}, which is the language the mirror is written in"
        )


def unknown_mirrors(mirrors):
    """The mirror names that are not named for a language this file knows."""
    return sorted(
        name
        for name in set(mirrors)
        if name[len("pr.") : -len(".md")] not in set(LANGUAGE_CODES.values())
    )


def test_a_mirror_named_for_a_country_is_refused_by_the_same_rule():
    """The teeth the real corpus stops showing once the directories holding
    its mirrors are retired: `kr` is a country and `ko` the language."""
    assert unknown_mirrors(["pr.ko.md", "pr.kr.md"]) == ["pr.kr.md"]


def test_a_config_holding_the_templates_default_row_reads_as_english(tmp_path):
    """tests-todo row 1, first half. The file the plugin ships a template for
    must not be the file that breaks the check. Its two language keys both
    read English, so they name one language and no mirror is asked for. The
    template's example object is written as the file."""
    home = tmp_path / "seal"
    home.mkdir()
    (home / "config.json").write_text(
        config_json(*items(read(*TEMPLATE))), encoding="utf-8"
    )
    commit = configured_language(tmp_path)
    record = configured_language(tmp_path, row=RECORD_ROW)
    assert (commit, record) == ("English", "English")
    assert the_mirror(commit, record) is None, (
        "two keys naming one language ask for no mirror"
    )
    assert mirror_to_refuse(record) == "pr.en.md", (
        "a file in the records' own language is no mirror"
    )


@pytest.mark.parametrize(
    "commit, record, wanted, refused",
    [
        ("Korean", "English", "pr.ko.md", "pr.en.md"),
        ("English", "Korean", "pr.en.md", "pr.ko.md"),
    ],
)
def test_rows_that_differ_name_the_mirror_for_the_commit_language(
    commit, record, wanted, refused, tmp_path
):
    """tests-todo row 1, second half, as #1453 leaves it. The rows are read,
    not the file's presence. Where they differ, the mirror is written in the
    commit language, so it is named for that language, and a file named for
    the records' language is no mirror."""
    home = tmp_path / "seal"
    home.mkdir()
    (home / "config.json").write_text(
        config_json((COMMIT_ROW, commit), (RECORD_ROW, record)), encoding="utf-8"
    )
    read_commit = configured_language(tmp_path)
    read_record = configured_language(tmp_path, row=RECORD_ROW)
    assert (read_commit, read_record) == (commit, record)
    assert the_mirror(read_commit, read_record) == wanted, (
        f"the mirror of a repository whose commits are {commit} and whose "
        f"records are {record} is named for {commit}"
    )
    assert mirror_to_refuse(read_record) == refused


# --- the config, read by the one reader -------------------------------------
#
# This file once carried its own copy of the config reader, and the copy
# answered a different question about the same file as soon as the
# production reader moved (#415). So it loads `lib/config.py` by path and
# reads a key through `declared_value`, the reader every script asks.

CONFIG_READER = ("lib", "config.py")


def _config_reader():
    """`lib/config.py`, loaded by path — the one reader of the config."""
    import importlib.util

    path = os.path.join(ROOT, *CONFIG_READER)
    spec = importlib.util.spec_from_file_location("agentic_config_for_pr_lang", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


READER = _config_reader()
declared_value = READER.declared_value


def items(text):
    """The keys of TEXT's first ```json block as (key, value), in the order
    written: the example object `templates/setup/config.md` shows, read by
    the same parser the config's reader uses."""
    block = text.split("```json\n", 1)[1].split("\n```", 1)[0]
    return list(json.loads(block, object_pairs_hook=list))


# The mirror cases above call these. They live here because they are built
# on the reader, and Python resolves a name when the call runs rather than
# where it sits.

COMMIT_ROW = "Commit and pull request language"
RECORD_ROW = "Record language"
LANGUAGE_CODES = {"English": "en", "Korean": "ko", "Japanese": "ja"}
CODES_BY_NAME = {name.casefold(): code for name, code in LANGUAGE_CODES.items()}


def as_language_name(value):
    """A key's value reduced to the language name it spells.

    Markdown emphasis off both ends and case folded, because the value is
    typed by a person: `**Korean**`, `_Korean_` and `korean` all name
    Korean. Nothing else is normalised — `Korean (KR)` is a different
    value and answering for it would be guessing.
    """
    return value.strip().strip("*_`").strip().casefold()


def mirror_to_refuse(language):
    """The one `pr.<code>.md` that cannot be a mirror, or None.

    LANGUAGE is the record language. A file named for it would render
    sentences into the language the records already hold them in, so it is
    no mirror (#1453).

    None is an answer, not a failure. `templates/setup/config.md` licenses "a
    language's English name" and says the reader is a model rather than a
    lookup table, so a value this dictionary does not hold is a legitimate
    config — round 2 🔴 1, where indexing it raised `KeyError` on `French`
    and turned a legitimate repository red. A table that must list every
    language is always one short.

    But None has to mean the language is ABSENT, not spelled differently.
    Round 3 finding 2: an exact lookup answered None for `**Korean**` and
    `korean`, so the mirror case skipped saying the file has no code for the
    language — which was false, and round 2's own probe table had already
    recorded `configured_language` returning `**Korean**` for an emphasised
    row. A person writing a markdown table emphasises a cell; that is the
    same value.
    """
    code = CODES_BY_NAME.get(as_language_name(language))
    return f"pr.{code}.md" if code else None


def the_mirror(commit, record):
    """The `pr.<code>.md` a work item holds where the two keys differ, or None.

    Where COMMIT and RECORD name different languages, the mirror is written
    in the commit language, so it is named for the commit language (#1453).
    Where they name one language no mirror is asked
    for, and a commit language this file has no code for answers None too.
    """
    if as_language_name(commit) == as_language_name(record):
        return None
    return mirror_to_refuse(commit)


def config_homes(root):
    """The two places the root can be, in the order the skill reads them.

    `<repo>/seal/` first, then `$(git rev-parse --git-common-dir)/seal/`,
    which is where local mode keeps it (#80). Round 2 🟡 2: this reader
    joined the first and stopped, which is the very defect round 1 fixed in
    the prose — a Korean row under `.git/seal/` read back as English.

    git is asked rather than `.git/seal` spelled, because in a linked
    worktree `.git` is a FILE and the root belongs to the main tree's common
    directory. A path that is not a repository answers nothing and leaves
    the one home, which is what a `tmp_path` fixture is.
    """
    base = str(root or ROOT)
    homes = [os.path.join(base, "seal")]
    try:
        common = subprocess.run(
            ["git", "-C", base, "rev-parse", "--git-common-dir"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
        ).stdout
    except (OSError, subprocess.SubprocessError):
        common = ""
    common = (common or "").strip()
    if common:
        homes.append(os.path.join(base, common, "seal"))
    return homes


def configured_language(root=None, row=COMMIT_ROW):
    """A repository's language for ROW, read the way the skill says.

    ROW is `Commit and pull request language` unless a case names
    `Record language`.

    Every way of not naming one lands on English, and there are four: no
    file, no such key, an empty value, and a file that cannot be read or is
    not one JSON object, a key that does not read among them. The direction
    is deliberate — a config nobody can read must not stop a commit.

    The ROOT is resolved first and the config read from that one, the way
    `lib/optin.py#home_at` resolves it: whichever of the two directories
    exists is the answer, and an unreadable file inside it is one of the
    four ways rather than a reason to look in the other place.
    """
    for home in config_homes(root):
        if not os.path.isdir(home):
            continue
        value, _refusal = declared_value(home, row)
        return (value or "").strip() or "English"
    return "English"


# FOUR ways, in five ids. "Cannot be read or is not one JSON object" is one
# way with two spellings, and the last two below are both that way — a file
# that does not parse as JSON, and one whose top level is an array. Round 2
# ❓ 8 settled the count: the skill's sentence says four, so four is the
# number, and keeping five shapes here costs nothing and exercises more.
UNNAMED = [
    ("no file at all", None),
    ("a file with no such key", config_json(("Other", "x"))),
    ("an empty value", config_json((COMMIT_ROW, ""))),
    ("a file that does not parse as JSON", "# notes\n\nno object here.\n"),
    (
        "a file whose top level is an array",
        f'[["{COMMIT_ROW}", "Korean"]]\n',
    ),
]


@pytest.mark.parametrize("what, body", UNNAMED, ids=[w for w, _ in UNNAMED])
def test_every_way_of_not_naming_a_language_lands_on_english(what, body, tmp_path):
    """🟡 3, run rather than only asserted in prose. A session that meets one
    of these and stops, asks, or guesses is the failure; all five answer the
    same."""
    home = tmp_path / "seal"
    home.mkdir()
    if body is not None:
        (home / "config.json").write_text(body, encoding="utf-8")
    assert configured_language(tmp_path) == "English", what


# --- round 2's findings, each with the case that would have caught it -------


def test_a_language_this_file_has_no_code_for_does_not_raise():
    """tests-todo row 5, from round 2 🔴 1.

    `templates/setup/config.md` licenses any language's English name, so `French`
    is a legitimate config. Indexing a three-entry dictionary with it raised
    `KeyError` — not a failing assertion with a message, a traceback — which
    is round 1 🟡 5's own wording: a legitimate config still turned the case
    red.
    """
    assert mirror_to_refuse("French") is None, (
        "an unknown language must answer 'no name to refuse' rather than "
        "raising, so the case can skip with a reason instead of erroring"
    )
    assert mirror_to_refuse("English") == "pr.en.md"
    assert mirror_to_refuse("Korean") == "pr.ko.md", (
        "the two directions the skill gives as examples must both compute"
    )


@pytest.mark.parametrize(
    "value", ["**Korean**", "korean", "KOREAN", " Korean ", "_Korean_", "`Korean`"]
)
def test_a_language_spelled_differently_is_the_same_language(value):
    """tests-todo row 12, from round 3 finding 2.

    None has to mean the language is ABSENT. An exact lookup answered None
    for these, so the mirror case skipped with a message saying the file has
    no code for the language — false, and the skip hid the check. A person
    writing a markdown table emphasises a cell; that is the same value.
    """
    assert mirror_to_refuse(value) == "pr.ko.md", (
        f"{value!r} is Korean spelled by a person, and answering None for it "
        "makes the mirror case skip on a claim that is not true"
    )


def test_a_language_that_is_genuinely_absent_still_answers_none():
    """The other half, so the normalisation above does not become guessing.
    `French` is absent, and `Korean (KR)` is a different value this file has
    no business resolving."""
    assert mirror_to_refuse("French") is None
    assert mirror_to_refuse("Korean (KR)") is None, (
        "normalising past a parenthetical would be inventing an answer, not "
        "reading the row"
    )


def test_the_reader_finds_a_config_under_the_git_directory(repo):
    """tests-todo row 6, from round 2 🟡 2.

    The prose was fixed in round 1 and the reader shipped in the same commit
    joined `<root>/seal/` and stopped, so a local-mode repository's config
    was invisible to the one executable model of a session's reading this
    branch ships. `local_home` asks git for the common directory, the way
    the scripts do.
    """
    home = local_home(repo)
    (home / "config.json").write_text(
        config_json((COMMIT_ROW, "Korean")), encoding="utf-8"
    )
    assert configured_language(repo) == "Korean", (
        "a config under the local-mode root read back as English, which is "
        "the default meaning 'nobody said' — the wrong answer, silently"
    )


def test_the_tree_root_still_wins_over_the_git_directory(repo):
    """The order, not just the fallback. Whichever directory exists first is
    the root, so a repository holding both is answered by the committed one
    — `lib/optin.py#home_at` resolves it that way and a reader that
    disagreed would send a session to the wrong file."""
    local = local_home(repo)
    (local / "config.json").write_text(
        config_json((COMMIT_ROW, "Korean")), encoding="utf-8"
    )
    shared = repo / "seal"
    shared.mkdir(parents=True, exist_ok=True)
    (shared / "config.json").write_text(
        config_json((COMMIT_ROW, "Japanese")), encoding="utf-8"
    )
    assert configured_language(repo) == "Japanese"


def test_a_mirror_named_for_a_country_is_caught():
    """tests-todo row 10, from round 2 🟡 7 — the can-it-fail half.

    `pr.kr.md` is one keystroke from `pr.ko.md` and twelve files are one
    copy away from it. The case above asserts the repository has none; this
    one asserts the rule those files are checked against actually rejects
    the near miss, rather than being a check that cannot fail.
    """
    known = set(LANGUAGE_CODES.values())
    assert "kr" not in known, (
        "`kr` is a country code; admitting it here would make the case above "
        "green for the exact mistake it exists to catch"
    )
    assert "ko" in known and "en" in known, (
        "the two codes this repository's mirrors actually use must be known, "
        "or every mirror reads as a near miss"
    )


def test_an_unreadable_config_lands_on_english_too(tmp_path):
    """The fifth way, which needs a filesystem rather than a string: a
    `config.json` that is a DIRECTORY, which the reader refuses as a file
    that will not read, so a permission error lands the same way."""
    (tmp_path / "seal" / "config.json").mkdir(parents=True)
    assert configured_language(tmp_path) == "English"


def test_the_template_is_one_item_value_table_whose_first_row_is_the_language():
    """S8, as #1454 leaves it. Parsed, not eyeballed: the example object the
    template shows is read by a JSON parser, and its first key is the
    language."""
    keys = items(read(*TEMPLATE))
    assert keys, "no ```json example in the template"
    assert keys[0] == ("Commit and pull request language", "English"), (
        f"the first key is not the language reading English: {keys[0]}"
    )
    # The second key is the records' own, and it is not the same question.
    # #106 split them because a repository can want Korean pull requests and
    # English specifications, and one key cannot say that.
    assert keys[1] == ("Record language", "English"), (
        f"the second key is not the record language reading English: {keys[1]}"
    )


def test_this_file_loads_the_one_reader_and_not_a_copy_of_it(tmp_path):
    """A8 of #415. The copy of the loop that used to live here agreed with
    the production reader right up until one of them moved.

    Asserted by where the code was COMPILED, the way
    `tests/skills/test_seal.py#Test_module::test_the_command_and_the_gate_read_one_parser`
    already asserts it for `seal.py`: this file loads that module under a
    name of its own, so the two module objects differ while the
    implementation behind them must not. An `import` check alone would not
    see a copy return — a reimplementation loaded under the same name passes
    it.
    """
    owner = os.path.join("lib", "config.py")
    where = declared_value.__code__.co_filename
    assert where.endswith(owner), f"`declared_value` is compiled from {where}"
    # And it is the reader that sees a key written twice, not something that
    # merely lives at that path: `json.loads` alone would take the last.
    home = tmp_path / "seal"
    home.mkdir()
    (home / "config.json").write_text(
        config_json((COMMIT_ROW, "Korean"), (COMMIT_ROW, "English")),
        encoding="utf-8",
    )
    value, refusal = declared_value(str(home), COMMIT_ROW)
    assert value is None and "2 times" in refusal


# The reader's own cases are in `tests/lib/test_config.py`.


# --- every template has a reader --------------------------------------------


def shipped_templates(root):
    """Every TRACKED file under `<root>/templates/`, at any depth.

    Asked of `git ls-files`, which is the list the corpus is built from too,
    so both sides of the comparison agree about what exists. It answers
    repository-relative `/` paths, it descends, and it lists tracked
    dotfiles — the three properties round 2 needed.

    Round 3 finding 1: this globbed the WORKING TREE, and a glob and
    `git ls-files` disagree wherever `.gitignore` does. `.DS_Store` is
    ignored here and opening `templates/` in Finder creates one, so the check
    failed naming a file that is not a template and that `git status` does
    not show. Round 2's widening to dotfiles is what carried it in — the
    plain `*` it replaced happened to skip them.
    """
    out = subprocess.run(
        # `check=True`: round 4 finding 1, narrowed by round 5's 1. It closes
        # ONE state — a path git cannot read as a repository, which used to
        # answer `[]` and so read exactly like "there are no templates".
        # Two states this comment used to claim are not this argument's. A
        # repository with no tracked `templates/` answers `[]` at exit 0, and
        # that IS the true answer. A stubbed helper never reaches git at all,
        # and the existence assertion in
        # `test_an_untracked_file_under_templates_is_not_a_template` is what
        # catches that one, as its own docstring says.
        #
        # `-z`: round 4 finding 3. git C-escapes a non-ASCII path by default,
        # so the name came back in a spelling no prose can contain and the
        # check called it unreachable. EITHER argument turns that escaping
        # off by itself — issue #98, re-measured on git 2.50.1 (Apple
        # Git-155), where `core.quotePath=false` alone answered
        # `templates/한글.md` unescaped. Round 5 recorded that it does not,
        # and this comment used to repeat that.
        #
        # What `-z` does that the config does not, measured the same way, is
        # two things. It turns off the escaping of CONTROL characters as
        # well: under `core.quotePath=false` alone, a name holding a newline
        # still comes back as `"templates/new\nline.md"`, quoted. And it
        # separates on NUL, the one byte a filename cannot hold — the split
        # below is on NUL, so dropping `-z` returns the whole listing as one
        # entry.
        #
        # `core.quotePath=false` therefore changes nothing while `-z` is
        # here — the two listings are byte-identical. It stays as the
        # argument that would still be doing part of the job if `-z` were
        # ever dropped, so if one of the two is ever pruned, prune this one.
        # That instruction is unchanged; only the grounds under it were wrong.
        [
            "git",
            "-c",
            "core.quotePath=false",
            "-C",
            str(root),
            "ls-files",
            "-z",
            "templates",
        ],
        check=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
    ).stdout
    return sorted(name for name in (out or "").split("\0") if name.strip())


def unreachable_templates(root, listed):
    """The templates no PROSE document among `listed` names.

    Prose is `.md`. Round 2 🟡 4: reading `skills/`, `agents/` and `lib/`
    whole takes their Python in too, and a template named only in a code
    comment is as unreachable as one named nowhere — a session bootstrapping
    a file does not read `chain_check.py` to find out what to copy.
    """
    corpus = ""
    for relative in listed:
        if not relative.endswith(".md"):
            continue
        try:
            with open(os.path.join(str(root), relative), encoding="utf-8") as handle:
                corpus += handle.read()
        except OSError:
            continue
    return [name for name in shipped_templates(root) if name not in corpus]


# Templates no session bootstraps from, so no shipped document has to name
# them. `templates/setup/claude-md-block.md` holds the two markers alone
# because the update to 0.25.0 runs 0.24.x's own update step, which diffs the
# marketplace clone's copy against the person's `CLAUDE.md`
# (`tests/behaviour/test_the_old_block_leaves_through_update.py`). The README
# named it until #1492 left that account to `skills/update/SKILL.md`, and it
# leaves the tree with the block's compatibility path.
READ_BY_AN_EARLIER_RELEASE = ("templates/setup/claude-md-block.md",)


def test_every_template_is_named_by_a_document_that_ships():
    """tests-todo row 4, from round 1 🟡 1.

    The finding was that `templates/setup/config.md` was named by nothing except a
    line-width list, so a session told to write `seal/config.md` had no
    source for it. That is a property of the DIRECTORY rather than of the one
    file it was found on: any template no document names is a file a session
    cannot find, and it writes one from scratch instead.

    `tests/` is excluded on purpose. A test naming a template is what the
    finding was about — the mention that looks like a reader and is not.

    Round 2 🟡 4 found the same hole one layer down. Excluding `tests/` and
    then reading `skills/`, `agents/` and `lib/` whole takes in their
    PYTHON, and `templates/records/sdd-round.md` was passing on four comments inside
    `skills/code-review/scripts/chain_check.py`. A comment is not a document
    a session bootstraps from, so the corpus is prose — `.md` only. Two
    narrowings went with it: the glob returned a subdirectory as one entry
    and never descended, and it skipped dotfiles.

    #1492: a template only an earlier release's update step reads is no file
    a session bootstraps, so `READ_BY_AN_EARLIER_RELEASE` names it and the
    case asks no document to; an entry the tree no longer holds is refused.
    """
    # The same three arguments `shipped_templates` carries, for the same
    # reason. Round 5 finding 3: round 4 applied them to one of two sibling
    # calls, and this one still C-escaped a non-ASCII name and — through
    # `.split()`, which splits on ANY whitespace — cut a name with a space in
    # two. `unreachable_templates` then dropped that document from the corpus
    # through its `except OSError: continue`, in silence, and a template only
    # that document named was reported unreachable.
    #
    # No `check=True` here: the assertion on the next line already turns an
    # empty listing red, which is what that argument buys above.
    listed = subprocess.run(
        [
            "git",
            "-c",
            "core.quotePath=false",
            "ls-files",
            "-z",
            "skills",
            "agents",
            "lib",
            "docs",
            "README.md",
            "README.ko.md",
            "CONTRIBUTING.md",
            "CLAUDE.md",
            "seal/README.md",
        ],
        cwd=ROOT,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
    ).stdout
    listed = [name for name in listed.split("\0") if name.strip()]
    assert [name for name in listed if name.endswith(".md")], (
        "no shipped prose documents were listed — this case is blind"
    )
    assert shipped_templates(ROOT), "no templates found — this case is blind"
    # #1492: an entry the tree no longer holds is a stale exemption.
    stale = [n for n in READ_BY_AN_EARLIER_RELEASE if n not in shipped_templates(ROOT)]
    assert not stale, f"exempted templates the tree no longer holds: {stale}"
    unreachable = [
        name
        for name in unreachable_templates(ROOT, listed)
        if name not in READ_BY_AN_EARLIER_RELEASE
    ]
    assert not unreachable, (
        "templates no shipped prose document names, so a session "
        f"bootstrapping one has nothing to copy: {unreachable}"
    )


def test_the_templates_check_reads_prose_only_and_descends(repo):
    """tests-todo rows 8 and 11, from round 2 🟡 4 and round 3 finding 1.

    Built on a real repository rather than a bare directory, because what is
    under test is now a `git ls-files` call: a fixture git never sees would
    report nothing and the case would pass having exercised nothing.

    Four properties in one tree. A Python comment must NOT count as a reader
    — that is round 2's finding. A template in a subdirectory or behind a dot
    must not hide. An UNTRACKED file must not be reported as a template at
    all, which is round 3's: `.DS_Store` is gitignored here and arrives from
    opening the folder in Finder.

    And tests-todo row 14, from round 5's 3: a prose document whose own NAME
    is not ASCII, or holds a space, has to reach the corpus. git C-escapes
    the first and `.split()` cut the second in two, and either way
    `unreachable_templates` dropped that document silently and called the
    template only it names unreachable. Each of the two documents below
    carries the only mention of one template — `안내.md` names
    `templates/sub/buried.md` and `two words.md` names
    `templates/.hidden.md` — so dropping either one leaves that template
    reported unreachable, and the assertion at the end of this case goes red.
    (#98: this said both documents named the same one template, which is
    true of neither. The conclusion it drew is unchanged.)
    """
    (repo / "templates" / "sub").mkdir(parents=True)
    (repo / "templates" / "named.md").write_text("x", encoding="utf-8")
    (repo / "templates" / "sub" / "buried.md").write_text("x", encoding="utf-8")
    (repo / "templates" / ".hidden.md").write_text("x", encoding="utf-8")
    (repo / "doc.md").write_text("start from templates/named.md\n", encoding="utf-8")
    (repo / "안내.md").write_text(
        "templates/sub/buried.md 에서 시작합니다\n", encoding="utf-8"
    )
    (repo / "two words.md").write_text(
        "start from templates/.hidden.md\n", encoding="utf-8"
    )
    (repo / "code.py").write_text(
        "# see templates/sub/buried.md and templates/.hidden.md\n", encoding="utf-8"
    )
    subprocess.run(
        ["git", "-C", str(repo), "add", "-A"],
        check=True,
        capture_output=True,
    )
    # Written AFTER the add, so it is untracked exactly as the real one is.
    (repo / "templates" / ".DS_Store").write_bytes(b"\x00\x01")

    assert shipped_templates(repo) == [
        "templates/.hidden.md",
        "templates/named.md",
        "templates/sub/buried.md",
    ], (
        "either the listing does not descend or skips tracked dotfiles, or "
        "the untracked `.DS_Store` came back as a template"
    )

    assert unreachable_templates(repo, ["doc.md", "code.py"]) == [
        "templates/.hidden.md",
        "templates/sub/buried.md",
    ], (
        "a Python comment was accepted as a reader, which is exactly how "
        "`templates/records/sdd-round.md` passed on four comments in chain_check.py"
    )

    # Row 14. The two documents whose own names git used to mangle are the
    # only prose naming these two templates, so a corpus that drops either
    # one reports the template it names as unreachable — which is what this
    # empty list refuses.
    assert unreachable_templates(repo, ["안내.md", "two words.md"]) == [
        "templates/named.md",
    ], (
        "a prose document whose name is not ASCII, or holds a space, did not "
        "reach the corpus, so the template only it names reads as unreachable"
    )


def _checker(name, *parts):
    """Import a checker by path, the way this repository's own cases do."""
    import importlib.util

    path = os.path.join(ROOT, *parts)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _chain():
    """`chain_check.py`, which loads `lib/fields.py` at its import."""
    return _checker("chain_check", "skills", "code-review", "scripts", "chain_check.py")


def _round_record_grammar():
    """Every key of the `seal` blocks of a round record, read from
    `lib/fields.py` rather than copied, and the `## Findings` section
    `chain_check.py` reads."""
    chain = _chain()
    keys = [key for kind in chain.FIELDS.ROUND_RECORD for key in kind.keys]
    return [*dict.fromkeys(keys), chain.FINDINGS_HEADING]


def _round_record_fields():
    """What a round record carries: its grammar. Two lines are owed only
    where their condition holds, `original:` in a repository that declares
    `seal/parity.json` and `reopens:` on a finding that raises an earlier
    close, so the template's one finding shows the other relation,
    `regression:`, and neither of these. The headings only the parties read
    are the proofer's to read (#1319)."""
    fields = _chain().FIELDS
    left_out = (fields.ORIGINAL, fields.REOPENS)
    return [key for key in _round_record_grammar() if key not in left_out]


ROUND_RECORD_FIELDS = _round_record_fields()


@pytest.mark.parametrize("field", ROUND_RECORD_FIELDS)
def test_the_round_template_carries_the_fields_it_is_expected_to(field):
    """`ROUND_RECORD_FIELDS` is checked against `templates/records/sdd-round.md`, so
    what runs is that the template still carries the fields this list
    expects — a pin on the template, and on nothing else."""
    # A key `chain_check.py` reads through `lib/fields.py`, or the
    # `## Findings` heading it reads, which a round record copies from the
    # template.
    assert field in read("templates", "records", "sdd-round.md"), (
        f"{field!r} is a field a round record is expected to carry and is "
        "not in `templates/records/sdd-round.md`, the file a round starts from"
    )


def test_the_review_skill_names_the_round_template():
    """The review skill names the template a round starts from, so a
    session bootstrapping a round record finds the file."""
    text = flat("skills", "code-review", "SKILL.md")
    # The path of the template a round record starts from, which a session
    # opens to write one.
    assert "templates/records/sdd-round.md" in text, (
        "the file's only mention in the prose corpus went, which makes it "
        "unreachable again"
    )


def test_an_untracked_file_under_templates_is_not_a_template(repo):
    """tests-todo row 11, from round 3 finding 1, isolated.

    The case above would also catch this, mixed in with two other
    properties. This one fails for one reason only: before the fix,
    `unreachable_templates` reported `templates/.DS_Store` and the check went
    red naming a file that is not a template and that `git status` hides.

    Round 4 finding 1: asserting `== []` twice pins only one direction. A
    helper that had stopped seeing anything would satisfy both, so the
    existence assertion below is what keeps this case from passing on
    silence.
    """
    (repo / "templates").mkdir(parents=True)
    (repo / "templates" / "named.md").write_text("x", encoding="utf-8")
    (repo / "doc.md").write_text("start from templates/named.md\n", encoding="utf-8")
    subprocess.run(
        ["git", "-C", str(repo), "add", "templates", "doc.md"],
        check=True,
        capture_output=True,
    )
    assert shipped_templates(repo) == ["templates/named.md"], (
        "the listing sees nothing, so every `== []` below would pass on "
        "silence rather than on the property they are here for"
    )
    assert unreachable_templates(repo, ["doc.md"]) == []

    (repo / "templates" / ".DS_Store").write_bytes(b"\x00\x01")
    assert unreachable_templates(repo, ["doc.md"]) == [], (
        "an untracked file under `templates/` is reported as an unreachable "
        "template, so anyone who opens the folder in Finder fails this check"
    )


def test_the_template_names_the_rows_an_absent_one_is_refused_for():
    """The template says what absence means, and which keys have no default.
    #1453 made the two language keys required, so every repository carries
    the file with those keys, and the template names them among the four
    exceptions. How it says so is the proofer's to read."""
    text = flat(*TEMPLATE)
    # The two keys besides the language keys whose absence is refused, which
    # a person writing the file fills in.
    assert "`Mode` and `Broad gate`" in text, (
        "the template does not name the keys an absent one is refused for"
    )


# --- a new permanent file in the root is listed where the root is described --


@pytest.mark.parametrize(
    "parts",
    [
        ("templates", "setup", "seal-README.md"),
        ("seal", "README.md"),
        ("README.md",),
        ("README.ko.md",),
    ],
)
def test_the_layout_lists_the_config(parts):
    """S9. Four documents draw the root's contents and a file in none of them
    is a file nobody finds. `seal/README.md` is written from the template, so
    the two move as one edit."""
    # The file name of the config, which a reader of the root's layout opens.
    assert "config.json" in read(*parts), (
        "/".join(parts) + " draws the root without the config file in it"
    )


# --- the exclusion list, derived rather than compared ----------------------


def _governs_nothing():
    """The `What no key governs` section of the template, flattened."""
    text = read(*TEMPLATE)
    start = text.index("## What no key governs")
    end = text.index("\n## ", start + 1)
    return " ".join(text[start:end].split())


def _literal_strings():
    """Every string the checkers match literally, read from the checkers.

    Derived, not copied. Round 1 of #106 found two headings missing from a
    hand-written list that had been copied into three documents — and the
    list's own grounds are *what a checker reads*, so a second source of it
    is a second source of the truth it claims to state.

    The keys of the `seal` blocks are not among them: the list names the
    module that spells them (`test_the_exclusion_list_points_at_the_block_
    grammar`), so a checker's constant here is one
    outside that module. The info string and the `## Findings` heading are,
    since the module's keys do not hold them.

    The settle reads a plan's *Judgments of the run* under its exact heading
    and header, the release note lifts a fragment's process section under
    the first line of `templates/records/process.md`, and a design's `to`
    holds `check:` lines that `.github/scripts/rules.py` reads (#1319).
    """
    unverified = _checker("gaps", "lib", "gaps.py")
    rules = _checker("rule_changes", "skills", "settle", "scripts", "rule_changes.py")
    body = _checker("pr_body", "skills", "code-review", "scripts", "pr_body.py")
    settle = _checker("settle", "skills", "settle", "scripts", "settle.py")
    checks = _checker("rules", ".github", "scripts", "rules.py")
    process = read("templates", "records", "process.md").splitlines()[0]
    chain = _chain()
    fields = {f"{f}:" for need, may in rules.GRAMMAR.values() for f in need + may}
    found = {
        f"## {settle.JUDGMENTS}",
        *settle.JUDGMENTS_HEADER,
        process,
        checks.LABEL.strip(),
        body.HEADING,
        body.PHASES,
        body.NOT_DONE,
        unverified.HEADING,
        unverified.CLOSED,
        *unverified.HEADER,
        f"## {rules.HEADING}",
        *rules.GRAMMAR,
        *fields,
        chain.FIELDS.INFO,
        chain.FINDINGS_HEADING,
    }
    return sorted(found)


BLOCK_GRAMMAR = "`lib/fields.py`"


def test_the_exclusion_list_points_at_the_block_grammar():
    """S4, under #1198. The keys of a round record's, a guarantee's and a
    gate record's `seal` blocks have one statement, `lib/fields.py`,
    which `chain_check.py` and the stamp read them through, so the list names
    the module. Whether a key of it is copied beside the citation is the
    proofer's to read."""
    said = _governs_nothing()
    # The citation of the module that spells the keys, which a person
    # translating the records resolves to the keys that stay English.
    assert BLOCK_GRAMMAR in said, (
        "the exclusion list no longer names the module that spells the keys "
        "of a record's `seal` blocks"
    )


@pytest.mark.parametrize("literal", _literal_strings())
def test_the_exclusion_list_holds_every_string_a_checker_matches(literal):
    """S6. The list's grounds are *what a checker reads literally*, so it is
    checked against the checkers rather than against itself.

    A repository that set `Record language` to another language and
    translated `## Findings` or `verdict:` would have every round record
    refused by `chain_check.py`, and one that translated `## Not verified`
    turns `unverified_check.py` red on every pull request.
    """
    # Each spelling a checker matches literally, which a repository
    # translating its records reads here to leave in English. Backticked,
    # because the section spells every literal that way and a
    # BARE substring is satisfied by a longer entry that contains it —
    # `fixed` was held by `agreed, fixed` alone, and deleting the standalone
    # entry left this case green (round 2).
    assert f"`{literal}`" in _governs_nothing(), (
        f"a checker matches `{literal}` literally and the exclusion list does "
        "not hold it as an item of its own, so a repository translating its "
        "records breaks that checker with nothing to warn it"
    )


# Every shipped document that tells a session which key to read. A document
# naming the wrong key sends the session to a key that does not exist, and
# round 1 found two that had drifted with nothing red.
ROW_READERS = [
    ("templates", "setup", "config.md"),
    ("skills", "config", "SKILL.md"),
    ("skills", "implement", "SKILL.md"),
    ("skills", "commit-pr-convention", "SKILL.md"),
    ("skills", "code-review", "SKILL.md"),
    # Phases 3 and 4 of #107 re-pointed both definitions' rows here: the
    # record-language section was in two of them in near-identical words and
    # in the third not at all, and it is contract rule 11 now. That
    # neither definition kept a copy is held by
    # `tests/text/test_a_moved_rule_leaves_its_definition.py`, so removing a row
    # from this list is a move rather than a deletion.
    ("skills", "agent-contract", "SKILL.md"),
]


@pytest.mark.parametrize("parts", ROW_READERS, ids=lambda p: "/".join(p))
def test_every_document_that_names_a_language_row_names_the_shipped_one(parts):
    """The pairing this branch was reviewed as one round for: a document
    naming the wrong key is invisible until somebody follows it."""
    text = flat(*parts)
    # The key of `config.json` a session reads for the records' language.
    assert "Record language" in text, (
        f"{'/'.join(parts)} does not name `Record language`, the key that "
        "governs the prose it is about"
    )
