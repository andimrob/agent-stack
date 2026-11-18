import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = REPO_ROOT / "skills" / "development" / "council-review"
REFERENCES = SKILL_DIR / "references"
COUNCIL_MEMBERS = (
    "Security",
    "Correctness",
    "Testing",
    "Architecture",
    "Design",
    "Performance",
    "Observability",
    "Analytics",
)
VOTES = ("agree", "object", "amend")


def read(path):
    return path.read_text(encoding="utf-8")


def headings(markdown, level):
    return re.findall(rf"^{'#' * level} (.+)$", markdown, re.MULTILINE)


def section(markdown, heading):
    start = markdown.index(heading)
    following = re.search(r"^#{1,3} ", markdown[start + len(heading) :], re.MULTILINE)
    end = start + len(heading) + following.start() if following else len(markdown)
    return markdown[start:end]


def collapsed(text):
    return " ".join(text.split())


class CouncilTest(unittest.TestCase):
    def test_seats_one_member_per_expertise(self):
        self.assertEqual(tuple(headings(read(REFERENCES / "council.md"), 2)), COUNCIL_MEMBERS)

    def test_every_member_states_its_remit_and_what_it_leaves_to_others(self):
        council = read(REFERENCES / "council.md")
        for member in COUNCIL_MEMBERS:
            with self.subTest(member=member):
                member_section = section(council, f"## {member}")
                self.assertIn("**Looks for**", member_section)
                self.assertIn("**Leaves to others**", member_section)

    def test_skill_seats_the_whole_council(self):
        skill = read(SKILL_DIR / "SKILL.md")
        for member in COUNCIL_MEMBERS:
            with self.subTest(member=member):
                self.assertIn(member, skill)


class DeliberationTest(unittest.TestCase):
    def test_defines_every_vote(self):
        deliberation = read(REFERENCES / "deliberation.md")
        for vote in VOTES:
            with self.subTest(vote=vote):
                self.assertIn(f"`{vote}`", deliberation)

    def test_keeps_each_member_for_every_round(self):
        deliberation = collapsed(read(REFERENCES / "deliberation.md"))
        self.assertIn("Keep each member for every round", deliberation)
        self.assertNotIn("for each round", deliberation)

    def test_ends_after_three_rounds(self):
        self.assertIn("at most three rounds", collapsed(read(REFERENCES / "deliberation.md")))

    def test_accepts_a_finding_only_when_every_member_agrees(self):
        for doc in (SKILL_DIR / "SKILL.md", REFERENCES / "deliberation.md"):
            with self.subTest(doc=doc.name):
                self.assertIn("every member votes `agree`", collapsed(read(doc)))

    def test_accepted_severity_is_the_lowest_any_member_voted_for(self):
        self.assertIn(
            "lowest severity any member voted for", collapsed(read(REFERENCES / "deliberation.md"))
        )


class ReportFormatTest(unittest.TestCase):
    def test_ranks_must_fix_findings_before_recommendations(self):
        report = read(REFERENCES / "report-format.md")
        self.assertLess(report.index("🔴 **Must fix**"), report.index("🟡 **Recommendation**"))

    def test_lists_findings_without_unanimity_apart(self):
        self.assertIn("⚖️ Not agreed", read(REFERENCES / "report-format.md"))

    def test_ends_with_a_summary_table_that_names_the_raiser(self):
        report = read(REFERENCES / "report-format.md")
        self.assertRegex(report, r"\| #\s+\| Sev\s+\| File\s+\| Finding\s+\| Raised by\s+\|")


class PostingTest(unittest.TestCase):
    def test_posting_waits_for_the_user_to_confirm(self):
        for doc in (SKILL_DIR / "SKILL.md", REFERENCES / "posting.md"):
            with self.subTest(doc=doc.name):
                self.assertIn("the user confirms", collapsed(read(doc)))

    def test_posts_only_accepted_findings(self):
        self.assertIn(
            "Not agreed findings stay in chat", collapsed(read(REFERENCES / "posting.md"))
        )

    def test_pins_inline_comments_to_the_reviewed_commit(self):
        self.assertIn("commit_id", read(REFERENCES / "posting.md"))


class SkillLinksTest(unittest.TestCase):
    def test_links_every_reference_it_names(self):
        skill = read(SKILL_DIR / "SKILL.md")
        for reference in sorted(REFERENCES.glob("*.md")):
            with self.subTest(reference=reference.name):
                self.assertIn(f"](references/{reference.name})", skill)


class ReadmeTest(unittest.TestCase):
    def test_lists_the_skill(self):
        self.assertIn("](skills/development/council-review/SKILL.md)", read(REPO_ROOT / "README.md"))


if __name__ == "__main__":
    unittest.main()
