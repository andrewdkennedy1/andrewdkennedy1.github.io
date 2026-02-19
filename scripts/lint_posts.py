#!/usr/bin/env python3
import pathlib
import re
import sys
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
POSTS = ROOT / "_posts"

POST_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")
POST_URL_RE = re.compile(r"\{\%\s*post_url\s+([\w\-]+)\s*\%\}")


def main() -> int:
    errors: list[str] = []

    post_files = sorted(POSTS.glob("*.md"))
    if not post_files:
        print("No posts found.")
        return 1

    slug_set: set[str] = set()
    for p in post_files:
        m = POST_RE.match(p.name)
        if not m:
            errors.append(f"Invalid post filename format: {p}")
            continue
        slug_set.add(f"{m.group(1)}-{m.group(2)}")

    for p in post_files:
        text = p.read_text(encoding="utf-8")

        # Basic front matter delimiters
        if not text.startswith("---\n"):
            errors.append(f"Missing front matter start: {p}")
            continue
        if "\n---\n" not in text[4:]:
            errors.append(f"Missing front matter end: {p}")

        # Required fields
        for field in ("title:", "date:", "layout:"):
            if field not in text.split("\n---\n", 1)[0]:
                errors.append(f"Missing front matter field '{field}' in {p}")

        # Validate post_url targets
        for target in POST_URL_RE.findall(text):
            if target not in slug_set:
                errors.append(f"Broken post_url in {p}: {target}")

    if errors:
        print("POST LINT FAILED")
        for e in errors:
            print(f" - {e}")
        return 1

    print(f"POST LINT OK ({len(post_files)} files checked) @ {datetime.utcnow().isoformat()}Z")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
