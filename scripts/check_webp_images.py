#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
DISALLOWED_IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".tif",
    ".tiff",
    ".avif",
}
ALLOWED_IMAGE_EXTENSION = ".webp"
IMAGE_REFERENCE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)|<img[^>]+src=[\"']([^\"']+)[\"']", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fail if docs images or image references are not in WebP format."
    )
    parser.add_argument(
        "--staged",
        action="store_true",
        help="Only inspect staged Markdown and image files for local pre-commit usage.",
    )
    return parser.parse_args()


def staged_paths() -> set[Path]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    paths = set()
    for line in result.stdout.splitlines():
        if not line:
            continue
        path = Path(line)
        if path.is_absolute():
            path = path.relative_to(REPO_ROOT)
        paths.add(path)
    return paths


def tracked_docs_paths() -> set[Path]:
    result = subprocess.run(
        ["git", "ls-files", "docs"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return {Path(line) for line in result.stdout.splitlines() if line}


def is_local_path(target: str) -> bool:
    lowered = target.lower()
    return not (
        lowered.startswith("http://")
        or lowered.startswith("https://")
        or lowered.startswith("data:")
        or lowered.startswith("mailto:")
        or lowered.startswith("#")
    )


def clean_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    target = target.split()[0]
    target = target.split("?", 1)[0]
    target = target.split("#", 1)[0]
    return target


def scan_markdown_file(path: Path) -> list[str]:
    violations: list[str] = []
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        violations.append(f"{path.relative_to(REPO_ROOT)}: unreadable Markdown file encoding")
        return violations

    for match in IMAGE_REFERENCE_RE.finditer(content):
        raw_target = match.group(1) or match.group(2)
        target = clean_target(raw_target)
        if not target or not is_local_path(target):
            continue
        suffix = Path(target).suffix.lower()
        if suffix in DISALLOWED_IMAGE_EXTENSIONS:
            violations.append(
                f"{path.relative_to(REPO_ROOT)}: image reference '{target}' must use {ALLOWED_IMAGE_EXTENSION}"
            )
    return violations


def scan_docs_images(paths: set[Path]) -> list[str]:
    violations: list[str] = []
    for relative_path in sorted(paths):
        if relative_path.suffix.lower() in DISALLOWED_IMAGE_EXTENSIONS:
            violations.append(
                f"{relative_path}: stored docs image must use {ALLOWED_IMAGE_EXTENSION}"
            )
    return violations


def collect_docs_paths(only_staged: bool) -> set[Path]:
    if not only_staged:
        return tracked_docs_paths()
    return {path for path in staged_paths() if path.parts and path.parts[0] == "docs"}


def collect_markdown_paths(doc_paths: set[Path]) -> list[Path]:
    markdown_paths = []
    for relative_path in sorted(doc_paths):
        if relative_path.suffix.lower() != ".md":
            continue
        absolute_path = REPO_ROOT / relative_path
        if absolute_path.is_file() and DOCS_DIR in absolute_path.parents:
            markdown_paths.append(absolute_path)
    return markdown_paths


def main() -> int:
    args = parse_args()
    docs_paths = collect_docs_paths(args.staged)
    violations = scan_docs_images(docs_paths)
    for markdown_path in collect_markdown_paths(docs_paths):
        violations.extend(scan_markdown_file(markdown_path))

    if not violations:
        print("All docs images use WebP.")
        return 0

    print("Docs images must use WebP:", file=sys.stderr)
    for violation in violations:
        print(f"- {violation}", file=sys.stderr)
    print(
        "Convert the image to .webp and update the Markdown reference before committing.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
