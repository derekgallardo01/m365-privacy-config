"""Linter for the privacy-config checklist.

    python validate.py                              # check examples/ are fully filled in
    python validate.py path/to/checklist.md         # check one file (use this on your drafts)

Flags two things:
  - angle-bracket placeholders like `<tenant>`, `<region>` you forgot to fill
  - `- [ ]` checkbox items that haven't been responded to (still unchecked)

Exit code 0 if clean, 1 if anything remains — suitable for a sign-off gate
so half-checked configurations don't get filed as the client's privacy
assurance document.
"""

from __future__ import annotations

import glob
import re
import sys

PLACEHOLDER = re.compile(r"<[^<>\n]{1,80}>")
UNCHECKED = re.compile(r"^\s*-\s*\[ \]")

ALLOW = {
    "<br>", "<br/>", "<br />", "<details>", "</details>",
    "<summary>", "</summary>", "<html>", "</html>",
}


def lint(path: str) -> dict:
    placeholders: list[tuple[int, str]] = []
    unchecked: list[tuple[int, str]] = []
    with open(path, encoding="utf-8") as fh:
        in_fence = False
        for ln, line in enumerate(fh, 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for m in PLACEHOLDER.finditer(line):
                text = m.group(0)
                if text.lower() in ALLOW:
                    continue
                if text.startswith("<!--"):
                    continue
                if text.startswith("<https://") or text.startswith("<http://"):
                    continue
                placeholders.append((ln, text))
            if UNCHECKED.match(line):
                unchecked.append((ln, line.rstrip()))
    return {"placeholders": placeholders, "unchecked": unchecked}


def main(argv: list[str]) -> int:
    files = argv if argv else sorted(glob.glob("examples/*.md"))
    if not files:
        print("No files to check (no examples/*.md and no path provided).")
        return 0

    total = 0
    for path in files:
        try:
            issues = lint(path)
        except FileNotFoundError:
            print(f"SKIP {path}: not found")
            continue
        n = len(issues["placeholders"]) + len(issues["unchecked"])
        if n:
            print(f"\n{path}: {len(issues['placeholders'])} placeholder(s), "
                  f"{len(issues['unchecked'])} unchecked item(s)")
            for ln, text in issues["placeholders"][:8]:
                print(f"  placeholder line {ln}: {text}")
            for ln, text in issues["unchecked"][:8]:
                print(f"  unchecked   line {ln}: {text.lstrip()[:80]}")
            total += n
        else:
            print(f"OK   {path}")

    print(f"\n{total} item(s) total.")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
