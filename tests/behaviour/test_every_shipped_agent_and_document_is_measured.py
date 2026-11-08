"""The two meters read this repository's own tree whole: the release table
has a row for every agent `agents/` defines and every policy document, and
`seal payload` names every shipped agent.

Each case lists `agents/` or `docs/`, so it stands in a file that declares no
`TARGET`. They came, unchanged, from `tests/github/test_release_report.py`
and `tests/skills/test_payload_meter.py`, which keep each meter's cases over
fixtures and the helpers these cases call.
"""

import json
import os

from censuses import POLICY_GROUPS
from conftest import ROOT
from test_payload_meter import run, write
from test_release_report import report, rows_of


class Test_release_report:
    def test_the_table_reads_this_tree_against_the_last_tag(self):
        """The repository's own two trees read: an agent row for every agent
        this tree defines, three leg rows, and a row for every `docs/*.md` and
        every document of the groups `docs/` holds (#1312)."""
        rows = report.table(
            "v0",
            report.reading(ROOT, report.meter()),
            report.reading(ROOT, report.meter()),
            {},
            {},
        )
        found = rows_of(rows)
        agents = sorted(
            f[: -len(".md")] for f in os.listdir(os.path.join(ROOT, "agents"))
        )
        for agent in agents:
            assert found[f"preload `{agent}` (bytes)"][2] == "+0 (+0.0%)", agent
        docs = [f for f in os.listdir(os.path.join(ROOT, "docs")) if f.endswith(".md")]
        docs += [
            f"{group}/{f}"
            for group in POLICY_GROUPS
            for f in os.listdir(os.path.join(ROOT, "docs", group))
            if f.endswith(".md")
        ]
        for name in docs:
            assert f"`docs/{name}` (bytes)" in found, name
        assert sum(1 for k in found if k.endswith("leg (minutes)")) == 3, found


class Test_payload_meter:
    def test_the_real_tree_runs_and_names_every_shipped_agent(self, tmp_path):
        """The meter's default root is the plugin root resolved from its own
        location, so it works from the version cache and from a clone."""
        home = tmp_path / "home"
        write(str(home / ".claude" / "CLAUDE.md"), "## user\n")
        result = run(["--json"], home)
        assert result.returncode == 0, result.stderr
        data = json.loads(result.stdout)
        shipped = sorted(
            n[: -len(".md")] for n in os.listdir(os.path.join(ROOT, "agents"))
        )
        assert sorted(data["agents"]) == shipped
        for name, agent in data["agents"].items():
            assert agent["files"][0]["path"] == f"agents/{name}.md"
            assert not any(f.get("missing") for f in agent["files"]), name
