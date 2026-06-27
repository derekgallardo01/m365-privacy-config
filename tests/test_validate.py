import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

import validate  # noqa: E402


def _abs(rel):
    return os.path.join(ROOT, rel)


def test_example_checklist_is_fully_completed():
    issues = validate.lint(_abs("examples/checklist-meridian-advisory.md"))
    assert issues["placeholders"] == [], f"placeholders remain: {issues['placeholders'][:3]}"
    assert issues["unchecked"] == [], f"unchecked items remain: {issues['unchecked'][:3]}"


def test_blank_checklist_still_looks_like_a_checklist():
    # The bare template SHOULD have all checkboxes unchecked.
    issues = validate.lint(_abs("privacy-config-checklist.md"))
    assert len(issues["unchecked"]) >= 10, (
        "bare template should have many unchecked items — if not, it's been "
        "accidentally completed"
    )


def test_no_internal_engagement_leaks_in_template():
    # Defensive check: the original template once contained a reference to an
    # internal client engagement. If anything similar slips back in, fail loud.
    with open(_abs("privacy-config-checklist.md"), encoding="utf-8") as fh:
        text = fh.read().lower()
    forbidden = ["copilot&claude", "claude client", "internal client",
                 "for derek", "playbook"]
    for token in forbidden:
        assert token not in text, f"internal-sounding token leaked into template: {token!r}"
