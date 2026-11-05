"""Tests for tools/skill_coverage.py. Standard library only: ``python -m unittest discover -s tests``."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
_SPEC = importlib.util.spec_from_file_location("skill_coverage", REPO_ROOT / "tools" / "skill_coverage.py")
sc = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = sc  # dataclasses look the module up by name
_SPEC.loader.exec_module(sc)

GUIDE = "> Source: https://manual.mikrotik.com/docs/{path}\n\n# Title\n\nText.\n"
MENU = "# {path}\n\n> Source: https://manual.mikrotik.com/docs/cli-reference{path}\n\nType: {kind}\n\n{body}"

SCOPES = {
    "scopes": [
        {"name": "routeros-a", "manual": ["net"], "cli": ["ip", "certificate"]},
        {"name": "routeros-b", "manual": ["vpn", "net/special$"], "cli": ["interface/wifi"]},
    ]
}
SNAPSHOT = {"manual": {"crawled": "2026-10-18"}}


def write(root: Path, rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def make_repo(root: Path, skill_a: str = "", skill_b: str = "") -> None:
    """Two skills: a has two guides and four CLI pages, b has one guide and one menu."""
    write(root, "skills/routeros-a/SKILL.md", f"---\nname: routeros-a\n---\n{skill_a}\n")
    write(root, "skills/routeros-b/SKILL.md", f"---\nname: routeros-b\n---\n{skill_b}\n")
    write(root, "skills/routeros-a/references/INDEX.md", "# Index\n")
    write(root, "skills/routeros-a/references/guides/net/dns.md", GUIDE.format(path="net/dns"))
    write(root, "skills/routeros-a/references/guides/net/dhcp/server.md", GUIDE.format(path="net/dhcp/server"))
    write(root, "skills/routeros-a/references/guides/net/dhcp/client.md", GUIDE.format(path="net/dhcp/client"))
    write(root, "skills/routeros-a/references/guides/net/special.md", GUIDE.format(path="net/special"))
    args = "- `name` (string): The name.\n- `comment` (string): A comment.\n"
    write(
        root,
        "skills/routeros-a/references/cli/ip/dns.md",
        MENU.format(path="/ip/dns", kind="Settings Directory", body=args),
    )
    write(
        root,
        "skills/routeros-a/references/cli/ip/dns/static.md",
        MENU.format(path="/ip/dns/static", kind="Directory", body=args),
    )
    write(
        root,
        "skills/routeros-a/references/cli/ip/firewall/filter.md",
        MENU.format(path="/ip/firewall/filter", kind="Directory", body=args),
    )
    cert = MENU.format(
        path="/certificate", kind="Directory", body=args + "\n## Commands\n\n### /certificate/add-acme\n\nText.\n"
    )
    write(root, "skills/routeros-a/references/cli/certificate.md", cert)
    write(root, "skills/routeros-b/references/guides/vpn/wireguard.md", GUIDE.format(path="vpn/wireguard"))
    write(
        root,
        "skills/routeros-b/references/cli/interface/wifi.md",
        MENU.format(path="/interface/wifi", kind="Directory", body=args),
    )
    write(root, "skills/routeros-b/references/products/model.md", "# Model\n")
    write(root, "tools/scopes.json", json.dumps(SCOPES))
    write(root, "tools/coverage_policy.json", json.dumps({"excluded": []}))
    write(root, "docs-snapshot.json", json.dumps(SNAPSHOT))


def classified(root: Path, policy: list[dict[str, str]] | None = None) -> dict[str, sc.Skill]:
    skills = sc.load_inventory(root)
    sc.classify(skills, policy or [])
    return skills


def statuses(skills: dict[str, sc.Skill]) -> dict[str, str]:
    return {
        **{m.path: m.status for s in skills.values() for m in s.menus},
        **{p.rel: p.status for s in skills.values() for p in s.pages},
    }


def run(argv: list[str]) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            code = sc.main(argv)
        except SystemExit as exc:
            code = int(exc.code)
    return code, out.getvalue(), err.getvalue()


class TempRepo(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)


class MentionTests(TempRepo):
    def trie(self) -> sc.Trie:
        make_repo(self.root)
        return sc.build_trie(sc.load_inventory(self.root))

    def test_both_spellings_name_the_menu(self) -> None:
        trie = self.trie()
        self.assertEqual(sc.mentioned_paths("/ip firewall filter add chain=input", trie), {"/ip/firewall/filter"})
        self.assertEqual(sc.mentioned_paths("see `/ip/firewall/filter`.", trie), {"/ip/firewall/filter"})

    def test_a_parent_is_not_credited_for_a_child(self) -> None:
        self.assertEqual(sc.mentioned_paths("/ip/dns/static add name=a", self.trie()), {"/ip/dns/static"})

    def test_prose_after_the_menu_does_not_count(self) -> None:
        self.assertEqual(sc.mentioned_paths("Use `/ip dns` and then statics.", self.trie()), {"/ip/dns"})

    def test_urls_and_file_paths_are_not_menus(self) -> None:
        text = "https://example.com/ip/dns and references/cli/ip/dns.md and ./ip/dns"
        self.assertEqual(sc.mentioned_paths(text, self.trie()), set())

    def test_a_longer_word_is_a_different_menu(self) -> None:
        self.assertEqual(sc.mentioned_paths("/ip/dns-over and /ip/dnsX", self.trie()), set())

    def test_a_command_credits_its_menu(self) -> None:
        self.assertEqual(sc.mentioned_paths("/certificate add-acme domain-names=x", self.trie()), {"/certificate"})
        self.assertEqual(sc.mentioned_paths("/certificate/add-acme", self.trie()), {"/certificate"})

    def test_standard_commands_stop_the_walk(self) -> None:
        self.assertEqual(sc.mentioned_paths("/ip dns set servers=1.1.1.1", self.trie()), {"/ip/dns"})


class FileMentionTests(unittest.TestCase):
    def test_files_folders_and_names(self) -> None:
        text = "`references/guides/net/dns.md`, `references/guides/net/dhcp/`, see special.md."
        mentions = sc.file_mentions(text)
        self.assertIn("guides/net/dns.md", mentions.files)
        self.assertIn("guides/net/dhcp", mentions.folders)
        self.assertIn("special.md", mentions.names)

    def test_a_folder_names_everything_below_it_but_not_its_siblings(self) -> None:
        mentions = sc.file_mentions("references/guides/net/dhcp/")
        self.assertTrue(sc.names_file(mentions, "guides/net/dhcp/server.md", set()))
        self.assertFalse(sc.names_file(mentions, "guides/net/dns.md", set()))
        self.assertFalse(sc.names_file(mentions, "guides/net/dhcp.md", set()))

    def test_a_longer_path_does_not_name_its_parent_folder(self) -> None:
        mentions = sc.file_mentions("references/cli/ip/dns/static.md")
        self.assertFalse(sc.names_file(mentions, "cli/ip/firewall/filter.md", set()))

    def test_the_bare_top_folder_names_nothing(self) -> None:
        mentions = sc.file_mentions("everything under references/guides/ and references/cli/")
        self.assertFalse(sc.names_file(mentions, "guides/net/dns.md", set()))
        self.assertFalse(sc.names_file(mentions, "cli/ip/dns.md", set()))

    def test_a_bare_file_name_needs_to_be_unique(self) -> None:
        mentions = sc.file_mentions("read server.md")
        self.assertTrue(sc.names_file(mentions, "guides/a/server.md", {"server.md"}))
        self.assertFalse(sc.names_file(mentions, "guides/a/server.md", set()))


class ClassifyTests(TempRepo):
    def test_statuses(self) -> None:
        make_repo(
            self.root,
            skill_a="Recipe: `/ip dns static add` and `/certificate add-acme`. Read `references/guides/net/dhcp/`.",
            skill_b="Needs `/ip firewall filter` too. Read `references/guides/vpn/wireguard.md`.",
        )
        found = statuses(classified(self.root))
        self.assertEqual(found["/ip/dns/static"], "named")
        self.assertEqual(found["/certificate"], "named")
        self.assertEqual(found["/ip/dns"], "unnamed")
        self.assertEqual(found["/ip/firewall/filter"], "elsewhere")
        self.assertEqual(found["/interface/wifi"], "unnamed")
        self.assertEqual(found["guides/net/dhcp/server.md"], "named")
        self.assertEqual(found["guides/net/dns.md"], "unnamed")
        self.assertEqual(found["guides/vpn/wireguard.md"], "named")

    def test_lookup_pages_are_counted_apart(self) -> None:
        make_repo(self.root)
        skills = classified(self.root)
        self.assertEqual(skills["routeros-b"].lookup, {"products": 1})
        self.assertEqual(len(skills["routeros-b"].pages), 1)

    def test_exclusions_leave_the_counts(self) -> None:
        make_repo(self.root)
        policy = [{"skill": "routeros-a", "folder": "guides", "prefix": "net/dhcp", "reason": "a test"}]
        skills = classified(self.root, policy)
        found = statuses(skills)
        self.assertEqual(found["guides/net/dhcp/server.md"], "excluded")
        self.assertEqual(found["guides/net/dns.md"], "unnamed")
        self.assertIn("| routeros-a | guides | `net/dhcp` | 2 | a test |", "\n".join(sc.render_policy(policy, skills)))


class PolicyTests(TempRepo):
    def problems(self, entries: list) -> list[str]:
        make_repo(self.root)
        return sc.check_policy(entries, sc.load_inventory(self.root))

    def test_a_valid_entry(self) -> None:
        entry = {"skill": "routeros-a", "folder": "cli", "prefix": "ip/dns", "reason": "x"}
        self.assertEqual(self.problems([entry]), [])

    def test_wrong_shape_unknown_skill_empty_reason_and_stale_entry(self) -> None:
        good = {"skill": "routeros-a", "folder": "cli", "prefix": "ip", "reason": "x"}
        text = "\n".join(
            self.problems(
                [
                    {"skill": "routeros-a"},
                    {**good, "skill": "nope"},
                    {**good, "reason": " "},
                    {**good, "prefix": "nothing/here"},
                    {**good, "folder": "products"},
                ]
            )
        )
        for fragment in ("exactly skill", "unknown skill", "a reason is required", "matches nothing", "folder must be"):
            self.assertIn(fragment, text)


class IndexAndDriftTests(unittest.TestCase):
    INDEX = (
        "# MikroTik RouterOS Manual\n\nIndex of the RouterOS 7.26 manual, in documentation menu order.\n\n"
        "- [DNS](https://manual.mikrotik.com/docs/net/dns.md): d\n"
        "- [New](https://manual.mikrotik.com/docs/net/new.md): n\n"
        "- [Nowhere](https://manual.mikrotik.com/docs/other/page.md): n\n"
        "- [Menu](https://manual.mikrotik.com/docs/cli-reference/ip/dns.md): m\n"
        "- [Wifi](https://manual.mikrotik.com/docs/cli-reference/interface/wifi/easymesh.md): m\n"
        "- [Widget](https://manual.mikrotik.com/docs/cli-reference/compare-versions.md): w\n"
    )

    def test_parse_index(self) -> None:
        index = sc.parse_index(self.INDEX)
        self.assertEqual(index.version, "7.26")
        self.assertEqual(index.guides, {"net/dns", "net/new", "other/page"})
        self.assertEqual(index.cli, {"/ip/dns", "/interface/wifi/easymesh", "/compare-versions"})
        self.assertEqual(index.entries, 6)

    def test_drift_names_added_removed_and_unassigned_pages(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_repo(root)
            skills = sc.load_inventory(root)
            drift = sc.compute_drift(skills, sc.scope_rules(root), sc.parse_index(self.INDEX), None, {})
        self.assertEqual([p["path"] for p in drift["guides"]["added"]], ["net/new", "other/page"])
        self.assertEqual(drift["guides"]["added"][0]["skill"], "routeros-a")
        removed = {p["path"] for p in drift["guides"]["removed"]}
        self.assertEqual(removed, {"net/dhcp/server", "net/dhcp/client", "net/special", "vpn/wireguard"})
        self.assertEqual({p["path"] for p in drift["cli"]["added"]}, {"/interface/wifi/easymesh", "/compare-versions"})
        self.assertEqual(drift["unassigned"], ["other/page", "/compare-versions"])
        errors, warnings = sc.drift_counts(drift)
        self.assertEqual(errors, 2)
        self.assertGreater(warnings, 0)
        self.assertIn("**none: add it to tools/scopes.json**", sc.render_drift(drift))

    def test_longest_prefix_and_exact_rules_of_scopes_json(self) -> None:
        rules = [("manual", "net", "a"), ("manual", "net/special$", "b"), ("manual", "net/special/deep", "c")]
        self.assertEqual(sc.match_scope("manual", "net/dns", rules), "a")
        self.assertEqual(sc.match_scope("manual", "net/special", rules), "b")
        self.assertEqual(sc.match_scope("manual", "net/special/x", rules), "a")
        self.assertEqual(sc.match_scope("manual", "net/special/deep/x", rules), "c")
        self.assertIsNone(sc.match_scope("manual", "other", rules))
        self.assertIsNone(sc.match_scope("cli", "net", rules))

    def test_lock_comparison_and_validation(self) -> None:
        index = self.INDEX.encode()
        lock = sc.make_lock(index, b"corpus", {"index": {"etag": '"x"', "last_modified": None}}, SNAPSHOT, "2026-11-05")
        self.assertEqual(sc.check_lock(lock), [])
        self.assertEqual(lock["manual"]["version"], "7.26")
        self.assertEqual(lock["index"]["etag"], '"x"')
        self.assertNotIn("last_modified", lock["index"])
        self.assertEqual(lock["snapshot_crawled"], "2026-10-18")
        same = sc.compute_drift({}, [], sc.parse_index(self.INDEX), lock, {"index": sc.sha256(index)})
        self.assertEqual(same["lock_changes"], [])
        newer = sc.parse_index(self.INDEX.replace("7.26", "7.27"))
        changed = sc.compute_drift({}, [], newer, lock, {"index": "0" * 64, "corpus": sc.sha256(b"corpus")})
        self.assertEqual(len(changed["lock_changes"]), 2)
        self.assertIn("7.26 -> 7.27", changed["lock_changes"][0])
        broken = {**lock, "reviewed": "yesterday", "index": {"sha256": "nope", "bytes": 1}}
        self.assertEqual(len(sc.check_lock(broken)), 2)

    def test_an_index_without_a_version_cannot_make_a_lock(self) -> None:
        with self.assertRaises(sc.CoverageError):
            sc.make_lock(b"- [A](https://manual.mikrotik.com/docs/a.md)", b"x", {}, SNAPSHOT, "2026-11-05")

    def test_only_the_two_manual_files_can_be_downloaded(self) -> None:
        with self.assertRaises(sc.CoverageError):
            sc.download("https://example.com/llms.txt")


class CommandLineTests(TempRepo):
    def test_write_then_check(self) -> None:
        make_repo(self.root, skill_a="`/ip dns static add`")
        self.assertEqual(run(["--root", str(self.root), "--write"])[0], 0)
        report = (self.root / "docs/skill-coverage.md").read_bytes()
        self.assertNotIn(b"\r", report)
        self.assertEqual(run(["--root", str(self.root), "--check"])[0], 0)
        write(self.root, "skills/routeros-a/SKILL.md", "---\nname: routeros-a\n---\n`/ip dns static add` `/ip dns`\n")
        code, _, err = run(["--root", str(self.root), "--check"])
        self.assertEqual(code, 1)
        self.assertIn("is stale", err)

    def test_the_report_is_deterministic(self) -> None:
        make_repo(self.root, skill_a="`/ip dns static add`")
        first = run(["--root", str(self.root)])[1]
        second = run(["--root", str(self.root)])[1]
        self.assertEqual(first, second)
        self.assertIn("| CLI menus | 1 (20%) | 0 | 4 | 0 | 5 |", first)

    def test_list_prints_what_is_not_named(self) -> None:
        make_repo(self.root, skill_a="`/ip dns static add`")
        code, out, _ = run(["--root", str(self.root), "--list", "routeros-a"])
        self.assertEqual(code, 0)
        self.assertIn("references/guides/net/dns.md", out)
        self.assertIn("/ip/firewall/filter", out)
        self.assertNotIn("/ip/dns/static", out)
        self.assertEqual(run(["--root", str(self.root), "--list", "nope"])[0], 2)

    def test_drift_flags_follow_the_rules(self) -> None:
        make_repo(self.root)
        index = self.root / "llms.txt"
        index.write_text(IndexAndDriftTests.INDEX, encoding="utf-8")
        code, out, _ = run(["--root", str(self.root), "--manual-index", str(index)])
        self.assertEqual(code, 1)
        self.assertIn("2 page(s) without a skill", out)
        clean = "Index of the RouterOS 7.26 manual\n- [DNS](https://manual.mikrotik.com/docs/net/dns.md): d\n"
        index.write_text(clean, encoding="utf-8")
        self.assertEqual(run(["--root", str(self.root), "--manual-index", str(index)])[0], 0)
        self.assertEqual(run(["--root", str(self.root), "--manual-index", str(index), "--strict"])[0], 1)

    def test_drift_reports_and_lock_are_written(self) -> None:
        make_repo(self.root)
        index, corpus = self.root / "llms.txt", self.root / "llms-full.txt"
        index.write_text("Index of the RouterOS 7.26 manual\n", encoding="utf-8")
        corpus.write_text("corpus", encoding="utf-8")
        argv = ["--root", str(self.root), "--manual-index", str(index), "--manual-corpus", str(corpus)]
        report, data = self.root / "drift.md", self.root / "drift.json"
        code, _, _ = run([*argv, "--report", str(report), "--json", str(data), "--write-lock"])
        self.assertEqual(code, 0)
        self.assertIn("# Manual drift", report.read_text(encoding="utf-8"))
        self.assertEqual(json.loads(data.read_text(encoding="utf-8"))["live_version"], "7.26")
        lock = json.loads((self.root / "docs/manual.lock.json").read_text(encoding="utf-8"))
        self.assertEqual(lock["corpus"]["sha256"], sc.sha256(b"corpus"))
        self.assertEqual(run(["--root", str(self.root), "--check"])[0], 1, "the report is not written yet")

    def test_flags_that_need_a_manual_input_are_rejected(self) -> None:
        make_repo(self.root)
        for flag in ("--strict", "--write-lock"):
            self.assertEqual(run(["--root", str(self.root), flag])[0], 2)
        index = self.root / "llms.txt"
        index.write_text("x", encoding="utf-8")
        self.assertEqual(run(["--root", str(self.root), "--manual-index", str(index), "--write-lock"])[0], 2)

    def test_a_missing_policy_file_is_an_error(self) -> None:
        make_repo(self.root)
        (self.root / "tools/coverage_policy.json").unlink()
        self.assertEqual(run(["--root", str(self.root)])[0], 2)


class RepositoryTests(unittest.TestCase):
    """The checked-in files agree with each other."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.skills = classified(REPO_ROOT, sc.load_policy(REPO_ROOT))
        cls.rules = sc.scope_rules(REPO_ROOT)

    def test_the_report_is_current(self) -> None:
        code, out, err = run(["--check"])
        self.assertEqual(code, 0, err)
        self.assertIn("is current", out)

    def test_every_page_is_in_the_skill_that_scopes_json_names(self) -> None:
        wrong = []
        for skill in self.skills.values():
            for page in skill.pages:
                if page.folder == "guides" and page.source and page.source.startswith(sc.MANUAL + "/docs/"):
                    path = page.source.removeprefix(sc.MANUAL + "/docs/").rstrip("/")
                    if sc.match_scope("manual", path, self.rules) != skill.name:
                        wrong.append(f"{skill.name}: {path}")
            for menu in skill.menus:
                if sc.match_scope("cli", menu.path.lstrip("/"), self.rules) != skill.name:
                    wrong.append(f"{skill.name}: {menu.path}")
        self.assertEqual(wrong, [])

    def test_the_inventory_matches_the_snapshot_counts(self) -> None:
        snapshot = json.loads((REPO_ROOT / "docs-snapshot.json").read_text(encoding="utf-8"))
        guides, cli = sc.snapshot_pages(self.skills)
        self.assertEqual(len(cli), snapshot["manual"]["cli_reference_pages"])
        self.assertGreaterEqual(len(guides), snapshot["manual"]["guides"] - 5)

    def test_the_lock_is_valid(self) -> None:
        lock = json.loads((REPO_ROOT / sc.LOCK).read_text(encoding="utf-8"))
        self.assertEqual(sc.check_lock(lock), [])


if __name__ == "__main__":
    unittest.main()
