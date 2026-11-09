"""Shared reader: what does this repository say about itself?

`config.json` sits in the root `lib/optin.py` resolves: one JSON object,
one key per item, each value a string in the grammar
`templates/setup/config.md` gives that key. Every absent key but four has a
default, which is what every repository got before that key existed. An
absent `Broad gate` is one exception: `seal gate` names the key and exits 2
with nothing run. `Commit and pull request language` and `Record language`
are two more: `seal pr-body` refuses to compose a pull request body without
either (#1453), and a commit is never refused for them.

`Mode` is the fourth, and it is why this module exists. What
every repository got before that key was *the folder decides*, which is not a
value, so an absent one has no default at all -- it is filled in from where the
folder actually is, by `seal mode`. Until somebody runs that command, a root
exists that nobody chose a mode for, and #151 is what that costs: a monorepo
was opted into shared mode, with its review records committed, without the
question ever being put to anyone.

The writer and every reader of the file need the SAME answer.
`skills/implement/scripts/seal.py` writes it and `seal mode --check` reads it
back, and `seal gate` and the other commands read the file's other keys. The
READER lives here and the writer in `seal.py`, so a script that only reads
imports this module and not the two-thousand-line command, and `seal.py`
re-exports these names rather than keeping a second copy. The file is read
by the standard library's JSON parser (`config_pairs`) and written by its
serializer, so the two cannot disagree about which key is which (#1454).

**Not in `optin.py`, deliberately.** That module's docstring says there is no
config key and everything in it fails toward *not opted in*; the root's
existence is the opt-in and `docs/layout/one-root-by-lifetime.md` *The opt-in signal
is the root itself* is the clause. The `Mode` key decides nothing about opting
in -- it RECORDS an answer -- and putting it in that module would read as the
clause being softened.

Everything here fails toward "nothing is declared" -- except where a written
answer would be read as absent. A file that is there and will not read or
parse, a `config.md` an earlier release wrote standing without a
`config.json`, and a key written twice or holding no string are refused by
`config_pairs` and `config_value` rather than read as nothing (#867), and a
command prints the refusal and stops: exit 2, or exit 1 for `seal pr-body`,
which exits 1 on every refusal.

The GFM table walker, which reads the tables of records and `seal mode`'s
converter of a `config.md`, is `lib/tables.py`; no setting is read through
it, and this module imports nothing beside the standard library.
"""

import json
import os
import re

CONFIG = "config.json"
# The byte order mark an editor may write first. `config_pairs` reads past it
# by decoding `utf-8-sig`; `baseline_commit` and `pact_check.py#path_map` are
# handed text already decoded, and take it off before they parse.
BOM = chr(0xFEFF)
# The file an earlier release wrote, a `| Item | Value |` table: refused
# where it stands without a `config.json`, and converted by `seal mode`.
OLD_CONFIG = "config.md"
MODE_KEY = "Mode"

# The two modes, spelled the way every document in this repository spells
# them. Read case-insensitively, written lowercase.
LOCAL, SHARED = "local", "shared"
MODES = (LOCAL, SHARED)

# The old file's table header, as the cells `lib/tables.py#gfm_table`
# matches a header by: what `seal mode`'s converter reads `OLD_CONFIG`
# through, and nothing else.
OLD_TABLE = ("Item", "Value")


def config_path(home):
    return os.path.join(home, CONFIG)


def old_config_path(home):
    return os.path.join(home, OLD_CONFIG)


class Members(list):
    """A JSON object's members as `(key, value)` pairs, in file order: what
    `config_pairs` parses every object into, so a key written twice is seen
    twice rather than taken last, and a value that is an object is told
    from one that is an array."""


def parse_config(text, path):
    """(pairs, refusal) for TEXT, the JSON of the config at PATH:
    `config_pairs`' last two states, for a caller that holds the text."""
    try:
        parsed = json.loads(text, object_pairs_hook=Members)
    except ValueError as exc:
        return None, (
            f"{path} does not parse as JSON ({exc}), so no key of it can be "
            "read — a config that is absent declares nothing, and one that "
            "will not parse is refused rather than read as absent"
        )
    if not isinstance(parsed, Members):
        return None, (
            f"{path} holds a JSON {json_type(parsed)} where the config is one "
            "object of keys, so no key of it can be read"
        )
    return parsed, None


def config_pairs(home):
    """(pairs, refusal) for `<home>/config.json` — the one place the file is
    opened, and the one place an absent file is told from one nobody can
    read.

      (None, None)     no `config.json` and no `config.md`, or a falsy HOME:
                       nothing is declared
      (pairs, None)    the file's object, as `Members` in file order
      (None, refusal)  a `config.md` an earlier release wrote, with no
                       `config.json` beside it; or a `config.json` that will
                       not read as UTF-8, will not parse as JSON, or whose
                       top level is not an object. REFUSAL is one sentence
                       opening with the `config.json` path

    **A file nobody can read is refused, never read as absent** (#867). An
    absent file is what every repository had before it wrote a key, so it
    declares nothing, everywhere. A file that is there and will not read is
    one whose answer nobody can read, and a command a person runs prints the
    sentence and stops with nothing judged (exit 2, or exit 1 for
    `seal pr-body`), because a command that reads a
    written answer as absent acts as if the person had written none. A
    `config.md` standing alone is such an answer, written in the table this
    release no longer reads: `seal mode` converts it (#1454).

    The text is decoded as `utf-8-sig`, so a byte order mark an editor wrote
    reads. A name that `lexists` but will not open -- a symbolic link to
    nowhere -- is a file that will not read: the name is there.
    """
    if not home:
        return None, None
    path = config_path(home)
    if not os.path.lexists(path):
        if os.path.lexists(old_config_path(home)):
            return None, unconverted_config(path)
        return None, None
    try:
        with open(path, encoding="utf-8-sig") as handle:
            text = handle.read()
    except (OSError, ValueError) as exc:
        return None, unreadable_config(path, exc)
    return parse_config(text, path)


def unconverted_config(path):
    """The sentence `config_pairs` refuses a root holding `config.md` and no
    `config.json` in, PATH being the `config.json` it looked for. It opens
    with that path and ends with no full stop, so it reads after a
    command's own prefix."""
    return (
        f"{path} is not there, and the {OLD_CONFIG} beside it is the table an "
        f"earlier release read, which no command reads now — run `seal mode` "
        f"once, which writes {CONFIG} from that table and removes {OLD_CONFIG}"
    )


def unreadable_config(path, exc):
    """The sentence `config_pairs` refuses an unreadable PATH in. It opens
    with the path and ends with no full stop, so it reads after a command's
    own prefix."""
    why = exc.strerror if isinstance(exc, OSError) and exc.strerror else str(exc)
    return (
        f"{path} is there and cannot be read as UTF-8 text ({why}), so no key "
        "of it can be read — a config that is absent declares nothing, and "
        "one that will not read is refused rather than read as absent"
    )


def json_type(value):
    """The JSON name of VALUE's type, as a refusal says it."""
    if isinstance(value, Members):
        return "object"
    if isinstance(value, list):
        return "array"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, (int, float)):
        return "number"
    if value is None:
        return "null"
    return "string"


def doubled_row(item, count):
    """The sentence `config_value` refuses a key written COUNT times in, the
    one sentence for every key."""
    return f"`{item}` appears {count} times — one value"


def config_value(pairs, key):
    """(value, refusal) for KEY among PAIRS, `config_pairs`' members — the
    one answer every reader of one config key gives (#867).

      (None, None)     no member is named KEY, or PAIRS is None (no file)
      (value, None)    one member: its string, as parsed, "" where empty
      (None, refusal)  KEY is written more than once, or its value is not a
                       string, and REFUSAL says which

    **A key written twice has no value**, not its first and not its last.
    A reader that took the last, as `json.loads` does, and a person editing
    the first are two answers to one file. So the one answer is a refusal,
    and what a caller does with it is its own kind's. **A value that is not
    a string has no value either**: every key's grammar is a string's, and
    a number or a list read as one would be a value nobody wrote. Every
    other key is read."""
    if pairs is None:
        return None, None
    values = [value for found, value in pairs if found == key]
    if len(values) > 1:
        return None, doubled_row(key, len(values))
    if not values:
        return None, None
    if not isinstance(values[0], str):
        return None, (
            f"`{key}` holds a JSON {json_type(values[0])}, and its value is a string"
        )
    return values[0], None


def declared_value(home, key):
    """(value, refusal) for KEY in `<home>/config.json`: `config_pairs`,
    then `config_value`, so a file nobody can read and a key with no value
    reach the caller the same way -- as a refusal it acts on by its own
    kind.
    """
    pairs, refusal = config_pairs(home)
    if refusal is not None:
        return None, refusal
    return config_value(pairs, key)


def declared_mode(home):
    """(kind, value) for the `Mode` key — what the repository SAYS it wants.

      "none"     nothing is declared: no file, no such key, or an empty
                 value
      "mode"     `local` or `shared`, lowercased
      "unknown"  a key is there and its value is not a mode — a claim nobody
                 can act on, which is not the same as no claim
      "refused"  the file will not read, or the key is written more than
                 once or holds no string; VALUE is `declared_value`'s
                 sentence

    **There is no default.** A key with a default falls back to what
    every repository got before the key existed; for the mode that is
    *the folder decides*, so an absent key is filled in from the folder by
    `seal mode` rather than assumed here. A default of `shared` would report
    every undeclared local-mode repository as lying.

    **`refused` is not `none`** (#867). The reader tells them apart once:
    `seal mode` prints a refusal and writes nothing, because writing a key
    into a file nobody can read, or one whose answers disagree, cannot make
    it agree.
    """
    value, refusal = declared_value(home, MODE_KEY)
    if refusal is not None:
        return "refused", refusal
    lowered = (value or "").lower()
    if not lowered:
        return "none", ""
    return ("mode", lowered) if lowered in MODES else ("unknown", value)


# --- the reference roots (#688) -------------------------------------------
#
# A project may have kept its own `specs/` before the plugin arrived. The
# plugin writes only to its own root and reads every other directory named
# `specs` as history: a REFERENCE ROOT, read when a change touches what it
# describes and never moved, edited, absorbed or deleted. The checks that read
# a record ask `under_reference_root` before they read a path, so none of them
# carries a test of its own (`templates/setup/config.md` *Reference specs*).

REFERENCE_KEY = "Reference specs"
NO_REFERENCE = "none"
# The directory name the default reads as a reference root at any depth.
REFERENCE_NAME = "specs"


def inside_the_root(rel, name):
    """True when the `/`-joined repository-relative `rel` is the plugin's own
    root or under it — never a reference root, whatever a key says. NAME is
    the root's name in the tree, `lib/optin.py#home_name`'s answer, which
    the caller reads; "" where the root is local or absent, and then no tree
    path is inside it."""
    return bool(name) and (rel == name or rel.startswith(name + "/"))


def reference_roots(home, name):
    """The repository-relative directories `<home>/config.json`'s
    `Reference specs` key names, as a tuple; `()` for `none`; or None, the
    default — every directory named `specs` outside the plugin's root.

    The value is comma-separated prefixes, each with or without a trailing
    `/` or a leading `./`. No file, no such key, an empty value or a file
    that will not read all mean the default, which is what every repository
    got before the key existed. A prefix naming the plugin's own root, NAME
    in the tree as `inside_the_root` reads it, or anything under it is
    dropped: a reference root is outside the root by definition, and the
    root's records are read whatever the key says.

    **No root at either place is `()`, no reference root at all** — not the
    default. A reference root is defined against the plugin's root, and a
    repository with none has not opted in: the one layout the plugin ever
    read without a root is 0.3.x, whose top-level `specs/` was the plugin's
    own, and `seal unverified` still reads that spelling as its records. A
    person
    joining a project runs the bootstrap, which creates the root, before any
    check reads the tree.

    **A refusal reads as the default** (#867): a file that will not read,
    and a `Reference specs` key written twice or holding no string, which
    `config_value` gives no value. Its caller, `seal unverified`, does not
    refuse on it: what a refusal costs it is the reading every repository
    had before the key existed, and no record is written or lost on it."""
    if not home:
        return ()
    # A refusal carries no value, so it lands with no key and an empty one.
    value, _refusal = declared_value(home, REFERENCE_KEY)
    if not value:
        return None
    if value.lower() == NO_REFERENCE:
        return ()
    out = []
    for entry in value.split(","):
        prefix = entry.strip().replace("\\", "/")
        while prefix.startswith("./"):
            prefix = prefix[2:]
        prefix = prefix.strip("/")
        if prefix and not inside_the_root(prefix, name) and prefix not in out:
            out.append(prefix)
    return tuple(out)


def under_reference_root(rel, roots, name):
    """True when the repository-relative path `rel` is a reference root or
    under one. `roots` is `reference_roots`' answer: None reads the default —
    any directory named `specs` on the path, outside the plugin's root NAME
    (`inside_the_root`) — and a tuple reads its prefixes alone.

    A predicate on a TREE path, so local mode needs no arm of its own: its
    root is under the git directory and never in the tree, NAME is "", and
    every `specs` the tree holds is outside it."""
    parts = [p for p in rel.replace("\\", "/").split("/") if p and p != "."]
    if not parts or inside_the_root(parts[0], name):
        return False
    if roots is None:
        return REFERENCE_NAME in parts
    joined = "/".join(parts)
    return any(joined == p or joined.startswith(p + "/") for p in roots)


# --- the policy root (#953) -------------------------------------------------

POLICY_KEY = "Policy root"
POLICY_DEFAULT = "docs"


def policy_root(home):
    """The repository-relative directory `<home>/config.json`'s `Policy
    root` key names, without a leading `./` or a trailing `/`, or `docs`.

    No root, no file, no such key, an empty value, a refusal and a value
    that leaves the repository (an absolute path or a `..` part) all read as
    `docs`, the directory every repository read before the key existed.
    `templates/setup/config.md` *The fold's values* states the key."""
    value = declared_value(home, POLICY_KEY)[0] if home else None
    rel = (value or "").strip().replace("\\", "/")
    while rel.startswith("./"):
        rel = rel[2:]
    rel = rel.rstrip("/")
    if not rel or rel.startswith("/") or ".." in rel.split("/"):
        return POLICY_DEFAULT
    return rel


# --- the pact a signer declares (#647) -------------------------------------
#
# A work item can commit in more than one repository, and where those
# repositories keep one contract together, the one copy of it is the PACT:
# `seal/pact.md` in the repository that holds it. Every repository of such a
# work item is a SIGNER, the pact's repository included. A signer other
# than the pact's repository names the pact here, by the origin remote URL of
# the repository that holds it, and the pact's repository needs no `Pact`
# key: it is identified by holding `seal/pact.md` (`docs/layout/the-pact.md`).
# The pact's repository lists every other signer in a `Pact signers` key, in
# the grammar of `Pact`.
#
# One command asks the two keys, through THESE readers:
# `skills/verify/scripts/pact_check.py`, run as `seal pact`, which reads
# every signer from the pact's repository and refuses what will not parse. A
# signer's CI reads nothing of the pact (`docs/layout/the-pact.md`).

PACT_KEY = "Pact"
SIGNERS_KEY = "Pact signers"
PACT_SEPARATOR = ";"
# The sentence a pact no `Pact signers` key signs is refused in.
NO_SIGNER = (
    f"no `{SIGNERS_KEY}` key names a signer, and a pact nobody signs is not a "
    "pact — write the origin remote URL of every other signer into that key, "
    f"separated by `{PACT_SEPARATOR}`"
)


def normalise_remote(url):
    """A remote URL reduced to host and path, so two spellings of one
    repository compare equal.

    `git@example.com:org/repo.git` and `https://example.com/org/repo` are one
    repository, and ssh at one machine with https at another is the ordinary
    case — comparing the strings would refuse every real import.

    The scheme goes, a `user@` prefix goes, the scp-style `host:path` colon
    becomes `/` **only where there was no scheme** (so the port in
    `https://example.com:8443/x` is left alone), a trailing `.git` and `/` go,
    and the result is lowercased.

    Wrong in the accepting direction would need two different repositories to
    reduce to the same host and path, which is the same repository. Wrong in
    the refusing direction costs a message naming `--allow-other-repo`. That
    asymmetry is why this is done at all.

    Anything that is not text reduces to "", because one caller passes a field
    out of a manifest another machine wrote. `read_manifest` checks that the
    manifest is an object and that its `format` is one this build reads; every
    other field is whatever the zip says, and a list here used to reach the
    console as an `AttributeError`.

    **It lives here and `skills/implement/scripts/seal.py` re-exports it**
    (#647), the arrangement this module's docstring records for the `Mode`
    reader. The `Pact` reader below needs it, and this module cannot import
    `seal.py`: that file imports this one, and a reader must not load a
    two-thousand-line command to read a key. One normaliser, reached by the
    name each caller already spells.
    """
    if not isinstance(url, str):
        return ""
    text = url.strip()
    if not text:
        return ""
    schemed = "://" in text
    if schemed:
        text = text.split("://", 1)[1]
    authority = text.split("/", 1)[0]
    if "@" in authority:
        text = text.split("@", 1)[1]
    if not schemed and ":" in text:
        text = text.replace(":", "/", 1)
    text = text.rstrip("/")
    if text.endswith(".git"):
        text = text[: -len(".git")]
    return text.lower()


def remote_entries(entries, empty):
    """(parsed, refusals) for ENTRIES, each a remote URL as somebody wrote
    it: `parsed` as `(as written, normalised)` in order, and one sentence
    per entry refused, EMPTY being the sentence for an empty one. An entry
    holding a space, one that reduces to no host and path, and two entries
    naming one repository are refused. Two entries that end in one segment
    are two repositories: a pact anchor names a pact by its URL.
    """
    parsed, refusals, seen = [], [], {}
    for entry in entries:
        written = entry.strip()
        if not written:
            refusals.append(empty)
            continue
        if any(ch.isspace() for ch in written):
            refusals.append(f"`{written}` holds a space — one remote URL per entry")
            continue
        normalised = normalise_remote(written)
        if "/" not in normalised:
            refusals.append(
                f"`{written}` is not a remote URL — it reduces to no host and "
                "path, so no repository can be found by it"
            )
            continue
        if normalised in seen:
            refusals.append(f"`{written}` and `{seen[normalised]}` are one repository")
            continue
        seen[normalised] = written
        parsed.append((written, normalised))
    return parsed, refusals


def pact_declaration(pairs):
    """(pacts, refusals) for the `Pact` key among PAIRS, a config's
    members as `config_pairs` gives them, None for no file.

      pacts     [(as written, normalised)] for every entry of the `Pact`
                key that parsed, in the order the key lists them; [] where
                no key names a pact
      refusals  one sentence per thing that would not parse, naming it

    **It refuses in sentences and stops nothing.** Its caller, `seal pact`,
    run at the pact's repository, exits 2 on a refusal.

    No file, no key and an empty value are one state, *no pact is held
    elsewhere* — the direction everything in this module fails in. A value
    that is there and does not parse is not that state, and it is refused
    rather than read as absent: a signer that wrote a key and is read as
    having written none is the silence this reader exists to end. A `Pact`
    key written twice or holding no string has no value, by
    `config_value`'s rule and in its sentence (#867), so it lists no pact.

    **Only the `Pact` key is read.** A key of any other name is no answer
    about a pact, a `Pact notify` key an earlier release read included
    (`templates/setup/config.md` *Pact*).
    """
    value, refused = config_value(pairs, PACT_KEY)
    if refused:
        return [], [refused]
    if not value:
        return [], []
    return remote_list(PACT_KEY, value)


def signer_declaration(pairs):
    """(signers, refusals) for the `Pact signers` key among PAIRS, the
    pact's repository's config members as `config_pairs` gives them, None
    for no file.

      signers   [(as written, normalised)] for every entry that parsed, in
                the order the key lists them
      refusals  one sentence per thing that would not parse, naming it

    **An absent or empty key is a refusal**, `NO_SIGNER`, unlike an absent
    `Pact` key: its one reader, `seal pact`, reads it only in the repository
    that holds `seal/pact.md`, and a pact nobody signs is not a pact. A key
    written twice or holding no string has no value, by `config_value`'s
    rule and in its sentence (#867), so it lists no signer. Each entry is
    read as `Pact`'s are."""
    value, refused = config_value(pairs, SIGNERS_KEY)
    if refused:
        return [], [refused]
    if not value:
        return [], [NO_SIGNER]
    return remote_list(SIGNERS_KEY, value)


def remote_list(key, value):
    """`remote_entries` over VALUE, KEY's value split at `PACT_SEPARATOR`,
    with the sentence an empty entry is refused in."""
    return remote_entries(
        value.split(PACT_SEPARATOR),
        f"the `{key}` value `{value}` holds an empty entry — one remote "
        f"URL between each `{PACT_SEPARATOR}`",
    )


def declared_pacts(home):
    """`pact_declaration` over `<home>/config.json`, or None where that
    file is refused by `config_pairs`.

    **Not the rule the other readers here keep**, and on purpose (round 1 of
    #647, white 5). `reference_roots` and `policy_root` answer a refused file
    as no key, because a gate that refuses wrongly stops a session with
    nobody able to get past it. This reader's caller is `seal pact`, run by
    a person at the pact's repository, and a signer whose written keys read
    as absent is the silence `pact_declaration` exists to end. So no file is
    no key, and a refused file is None, which `seal pact` refuses as
    `UNREADABLE` with `config_pairs`' sentence."""
    pairs, refusal = config_pairs(home)
    if refusal is not None:
        return None
    return pact_declaration(pairs)


# --- the migration config's baseline (#988) --------------------------------
#
# `seal/parity.json` is written from `templates/setup/parity.json`, one JSON
# object whose `Baseline commit` key holds the SHA the original's
# coordinates refer to, and nothing else. `chain_check.py` compares each
# round record's `original:` line with it, and reads it through this one
# function. Agents read the other keys.

# The template's keys, in its order: what the sentence below names for a
# person converting an earlier release's `parity.md`.
PARITY_KEYS = (
    "Original repo",
    "Module",
    "Baseline commit",
    "Policy root",
    "Coordinate-trust exceptions",
    "Scope notes",
)
BASELINE_KEY = "Baseline commit"
BASELINE_SHA = re.compile(r"[0-9a-f]{7,40}")


def baseline_commit(text):
    """`(sha, None)` for the migration config TEXT, `parity.json`'s, whose
    one `Baseline commit` key holds 7 to 40 lowercase hex digits and
    nothing else; else `(None, why)`.

    Text that will not parse as JSON, a top level that is not an object, no
    such key, the key written twice, a value that is not a string, and a
    string that is not a SHA alone, the template's `<SHA>` among them, are
    each a `why` that reads after the file's name. A byte order mark an
    editor wrote reads, as it does in `config.json`."""
    try:
        parsed = json.loads(text.removeprefix(BOM), object_pairs_hook=Members)
    except ValueError as exc:
        return None, f"does not parse as JSON ({exc})"
    if not isinstance(parsed, Members):
        return None, (
            f"holds a JSON {json_type(parsed)} where the migration config is "
            "one object of keys"
        )
    value, refusal = config_value(parsed, BASELINE_KEY)
    if refusal is not None:
        return None, refusal
    if value is None:
        return None, f"holds no `{BASELINE_KEY}` key"
    if not BASELINE_SHA.fullmatch(value):
        return None, (
            f"has a `{BASELINE_KEY}` key whose value is `{value}`, and the "
            "commit is that value alone, 7 to 40 lowercase hex digits"
        )
    return value, None


def unconverted_parity(path):
    """The sentence an earlier release's `parity.md` standing without the
    `parity.json` at PATH is named in, by the parity arm of `chain_check.py`
    and by `seal mode`: the file to write, the template it is written from,
    and each key of it. It reads after the old file's name and ends with no
    full stop."""
    keys = ", ".join(f"`{key}`" for key in PARITY_KEYS[:-1])
    return (
        "is the migration config an earlier release read, a table no check "
        f"reads now — write {path} from `templates/setup/parity.json`, one "
        f"JSON object holding {keys} and `{PARITY_KEYS[-1]}`, with "
        f"`{BASELINE_KEY}` the SHA alone, then delete the old file"
    )
