"""Check the skill text against what the Gomnee server provides.

contract/gomnee-server.json is a copy of apps/web/tests/unit/plugin-contract.json
in the Gomnee product repository: the tool names the MCP server can register and
the Article house targets. Replace it with a fresh copy when that file changes.
"""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "gomnee"
CONTRACT = json.loads((ROOT / "contract" / "gomnee-server.json").read_text())
MARKDOWN = sorted(PLUGIN.rglob("*.md"))
SKILLS = sorted(path for path in (PLUGIN / "skills").iterdir() if path.is_dir())

# Row label in house-defaults.md -> the contract values it must quote, in order.
HOUSE_TARGETS = {
    "Depth": ("minimumWords", "tutorialMinimumWords", "tutorialTargetMaximum"),
    "Contextual inventory links": ("outboundMinimum", "outboundMaximum"),
    "Inbound suggestions": ("inboundMinimum", "inboundMaximum"),
    "Secondary terms": ("secondaryMinimum", "secondaryMaximum"),
    "Primary phrase repetition": ("densityMaximum",),
    "Commissioned FAQ": ("faqMinimum", "faqMaximum", "faqAnswerMinimum", "faqAnswerMaximum"),
    "Search title": ("titleMaximum",),
    "Search description": ("descriptionMinimum", "descriptionMaximum"),
    "Paragraphs": ("paragraphSentenceMaximum",),
    "Heading spacing": ("headingWordMaximum",),
}


class SkillContractTests(unittest.TestCase):
    def test_contract_copy_is_the_expected_document(self):
        self.assertEqual(CONTRACT["schemaVersion"], "gomnee_plugin_contract_v1")
        self.assertEqual(CONTRACT["toolNames"], sorted(set(CONTRACT["toolNames"])))

    def test_skills_name_only_tools_the_server_provides(self):
        known = set(CONTRACT["toolNames"])
        unknown = sorted({f"{path.relative_to(PLUGIN)}: {name}"
                          for path in MARKDOWN
                          for name in re.findall(r"\bgomnee_[a-z0-9_]+\b", path.read_text())
                          if name not in known})
        self.assertEqual(unknown, [])

    def test_every_skill_has_a_matching_name_and_a_real_description(self):
        for skill in SKILLS:
            frontmatter = re.match(r"\A---\n([\s\S]*?)\n---\n", (skill / "SKILL.md").read_text())
            self.assertIsNotNone(frontmatter, skill.name)
            self.assertRegex(frontmatter[1], rf"(?m)^name: {re.escape(skill.name)}$")
            self.assertRegex(frontmatter[1], r"(?m)^description: \S.{40,}$")

    def test_skills_leave_schema_versions_and_scopes_to_the_server(self):
        for skill in SKILLS:
            content = (skill / "SKILL.md").read_text()
            self.assertNotRegex(content, r"\b(?:article|strategy|planner)_[a-z_]+_v\d+\b", skill.name)
            self.assertNotRegex(content, r"\bgomnee:[a-z-]+:[a-z-]+\b", skill.name)

    def test_house_targets_equal_the_server_values(self):
        defaults = CONTRACT["articleEditorialDefaults"]
        rows = (PLUGIN / "skills/gomnee-write-article/references/house-defaults.md").read_text().split("\n")
        for label, keys in HOUSE_TARGETS.items():
            row = next((line for line in rows
                        if len(line.split("|")) > 1 and line.split("|")[1].strip() == label), None)
            self.assertIsNotNone(row, label)
            quoted = [float(value.replace(",", ""))
                      for value in re.findall(r"(?<![\w])\d[\d,]*(?:\.\d+)?", row)]
            self.assertEqual(quoted, [float(defaults[key]) for key in keys], label)

    def test_skills_do_not_contradict_the_house_policy(self):
        pattern = re.compile(
            r"No keyword density|No SEO theatre|There is no minimum number|"
            r"Fixed word counts, heading counts|skip when they do not help|"
            r"Length is a[\s\S]{0,40}not a rule")
        contradictions = [str(path.relative_to(PLUGIN)) for path in MARKDOWN
                          if "skills" in path.parts
                          and re.search(r"(?:editorial-standard|on-page|internal-links|SKILL)\.md$", path.name)
                          and pattern.search(path.read_text())]
        self.assertEqual(contradictions, [])


if __name__ == "__main__":
    unittest.main()
