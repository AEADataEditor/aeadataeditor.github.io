#!/usr/bin/env python3
"""Generate AI agent instruction file from guidance markdown sources.

Strips Jekyll front matter and site-navigation elements, prepends an
agent-oriented preamble, and concatenates all preparing-replication-package
guidance sections into a single file suitable for AI agent consumption.
"""

import re
from pathlib import Path

BASE_URL = "https://aeadataeditor.github.io/aea-de-guidance"

GUIDANCE_DIR = Path("_guidance")
OUTPUT = Path("_site/aea-de-guidance/preparing-replication-package.agent.md")

PREAMBLE = f"""\
# AEA Replication Package Preparation: Agent Instructions

This document contains official guidance from the AEA Data Editor for preparing
an economics replication package for submission to the American Economic
Association. It is auto-generated for AI agent use from the source documents at
{BASE_URL}/preparing-replication-package

## How to use these instructions

You are an AI assistant helping an economics researcher prepare their replication
package for submission to the AEA Data Editor. Work through each step in order:

1. Review the replication package against each checklist item.
2. Identify issues or missing elements.
3. Suggest specific, actionable fixes — include code examples where relevant.
4. Confirm each step is satisfied before moving to the next.

**Note on links:** Bare link targets such as `(preparing-replication-package-step1)`
are relative references to pages at {BASE_URL}/. The full content of all
referenced pages is already included in this document, so you do not need to
follow those links.

"""

SECTIONS = [
    "preparing-replication-package.md",
    "preparing-replication-package-step1.md",
    "preparing-replication-package-step2.md",
    "preparing-replication-package-step3.md",
    "preparing-replication-package-step4.md",
    "preparing-replication-package-step5.md",
    "preparing-replication-package-finalize.md",
    "preparing-replication-package-details.md",
]

# Matches the breadcrumb/back-link navigation line present at the top of each step file.
# These lines start with [◀ or [Back and are pure navigation with no content.
NAV_LINE = re.compile(r"^\[[◀B]")

# Matches image-button navigation links used at the bottom of step files,
# e.g. [![Next: Step 2](/images/next-button-step2.png)](...)
IMAGE_NAV = re.compile(r"^\[!\[")

# Matches the back-reference unique to the details page.
DETAILS_BACKREF = re.compile(r"^> For the checklist, see \[previous page\]")


def strip_jekyll(text: str) -> str:
    text = re.sub(r"(?s)\A---\n.*?\n---\n", "", text)
    lines = []
    for line in text.splitlines(keepends=True):
        if NAV_LINE.match(line):
            continue
        if IMAGE_NAV.match(line):
            continue
        if DETAILS_BACKREF.match(line):
            continue
        lines.append(line)
    result = "".join(lines)
    # Remove trailing horizontal rule left behind after stripping image-button nav
    result = re.sub(r"\n---\s*\Z", "\n", result)
    return result


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as out:
        out.write(PREAMBLE)
        for section in SECTIONS:
            path = GUIDANCE_DIR / section
            stripped = strip_jekyll(path.read_text(encoding="utf-8"))
            out.write("\n---\n\n")
            out.write(stripped)
    print(f"Generated {OUTPUT}")


if __name__ == "__main__":
    main()
