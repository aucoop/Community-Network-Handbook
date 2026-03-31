#!/usr/bin/env python3
"""Pre-process MkDocs markdown files into a single Pandoc-ready document.

Handles:
- Admonition syntax (!!! type "Title") -> Pandoc fenced divs
- Material icons (:material-xxx:) -> text substitution
- Image path resolution (relative to docs/)
- .webp -> .png extension replacement
- Image width attributes
- HTML comment stripping
- Heading level adjustment for book structure
- Mermaid block extraction to .mmd files + replacement with image refs
- Cross-chapter link simplification for print
"""

import re
import sys
import os
from pathlib import Path


# ---------------------------------------------------------------------------
# File ordering derived from mkdocs.yml nav.
# Each entry: (filepath_relative_to_docs, heading_shift)
#   shift 0 = h1 stays h1 -> \part (chapter-level index)
#   shift 1 = h1 -> h2 -> \chapter (section-level index or direct child)
#   shift 2 = h1 -> h3 -> \section (sub-page)
# ---------------------------------------------------------------------------

NAV_ORDER = [
    # Preface (home page) -- will have its h1 stripped
    # ("index.md", 0),  # handled specially as preface

    # Part 1: Introduction
    ("1-Introduction/index.md", 0),
    ("1-Introduction/1.1-Motivation.md", 1),
    ("1-Introduction/1.2-Target-Reader.md", 1),

    # Part 2: Imaginary Use Case
    ("2-Imaginary-Use-Case/index.md", 0),
    # Act 1 -- Getting Connected
    ("2-Imaginary-Use-Case/2.1-The-First-Router/index.md", 1),
    ("2-Imaginary-Use-Case/2.1-The-First-Router/2.1.1-Choosing-Hardware.md", 2),
    ("2-Imaginary-Use-Case/2.1-The-First-Router/2.1.2-Installing-OpenWrt.md", 2),
    ("2-Imaginary-Use-Case/2.1-The-First-Router/2.1.3-Debrick.md", 2),
    ("2-Imaginary-Use-Case/2.2-Expanding-Coverage/index.md", 1),
    ("2-Imaginary-Use-Case/2.2-Expanding-Coverage/2.2.1-Planning.md", 2),
    ("2-Imaginary-Use-Case/2.2-Expanding-Coverage/2.2.2-IP-Addressing.md", 2),
    ("2-Imaginary-Use-Case/2.2-Expanding-Coverage/2.2.3-Wired-vs-Wireless.md", 2),
    ("2-Imaginary-Use-Case/2.3-The-Other-Building/index.md", 1),
    ("2-Imaginary-Use-Case/2.3-The-Other-Building/2.3.1-Antennas.md", 2),
    # Act 2 -- Growing Pains
    ("2-Imaginary-Use-Case/2.4-Mass-Config/index.md", 1),
    ("2-Imaginary-Use-Case/2.5-Monitoring/index.md", 1),
    ("2-Imaginary-Use-Case/2.6-DNS/index.md", 1),
    ("2-Imaginary-Use-Case/2.7-Remote-Access/index.md", 1),
    ("2-Imaginary-Use-Case/2.8-Captive-Portal/index.md", 1),
    ("2-Imaginary-Use-Case/2.9-User-Management/index.md", 1),
    ("2-Imaginary-Use-Case/2.10-Security/index.md", 1),
    # Act 3 -- Adding Value
    ("2-Imaginary-Use-Case/2.11-Local-Services/index.md", 1),
    ("2-Imaginary-Use-Case/2.12-Virtualization/index.md", 1),
    ("2-Imaginary-Use-Case/2.13-Storage/index.md", 1),
    ("2-Imaginary-Use-Case/2.14-Clustering/index.md", 1),
    # Act 4 -- Protecting What You Built
    ("2-Imaginary-Use-Case/2.15-Power/index.md", 1),
    ("2-Imaginary-Use-Case/2.16-Backups/index.md", 1),
    ("2-Imaginary-Use-Case/2.17-High-Availability/index.md", 1),
    ("2-Imaginary-Use-Case/2.18-Updates/index.md", 1),
    # Act 5 -- Telling the World
    ("2-Imaginary-Use-Case/2.19-Domain/index.md", 1),
    ("2-Imaginary-Use-Case/2.20-Website/index.md", 1),
    # Act 6 -- Equipping the Community
    ("2-Imaginary-Use-Case/2.22-Laptop-Deployment/index.md", 1),
    # Act 7 -- The Long Run
    ("2-Imaginary-Use-Case/2.21-Sustainability/index.md", 1),

    # Part 3: Guide
    ("3-Guide/index.md", 0),
    ("3-Guide/Antennas/index.md", 1),
    ("3-Guide/Captive-Portal/index.md", 1),
    ("3-Guide/Clustering/index.md", 1),
    ("3-Guide/DNS/index.md", 1),
    ("3-Guide/Domain/index.md", 1),
    ("3-Guide/Flash-OpenWrt/index.md", 1),
    ("3-Guide/Flash-OpenWrt/Cudy-WR3000E.md", 2),
    ("3-Guide/Flash-OpenWrt/Debrick.md", 2),
    ("3-Guide/High-Availability/index.md", 1),
    ("3-Guide/IP-Addressing/index.md", 1),
    ("3-Guide/Laptop-Deployment/index.md", 1),
    ("3-Guide/Wireless-Mesh/index.md", 1),
    ("3-Guide/Nextcloud/index.md", 1),
    ("3-Guide/OpenWISP/index.md", 1),
    ("3-Guide/Power-and-UPS/index.md", 1),
    ("3-Guide/Proxmox/index.md", 1),
    ("3-Guide/Proxmox-Backup-Server/index.md", 1),
    ("3-Guide/RADIUS/index.md", 1),
    ("3-Guide/Security/index.md", 1),
    ("3-Guide/Storage/index.md", 1),
    ("3-Guide/Updates-and-Maintenance/index.md", 1),
    ("3-Guide/VPN/index.md", 1),
    ("3-Guide/Website/index.md", 1),
    ("3-Guide/Zabbix/index.md", 1),

    # Part 4: Real Use Cases
    ("4-Real-Use-Cases/index.md", 0),
    ("4-Real-Use-Cases/4.1-Namibia/index.md", 1),

    # Appendix
    # ("contributing.md", 0),  # handled specially as appendix
]


# ---------------------------------------------------------------------------
# Text transforms
# ---------------------------------------------------------------------------

def shift_headings(text: str, shift: int) -> str:
    """Shift all markdown headings by `shift` levels."""
    if shift == 0:
        return text

    def _replace(m):
        level = min(max(len(m.group(1)) + shift, 1), 6)
        return "#" * level + m.group(2)

    return re.sub(r"^(#{1,6})([ \t].*)$", _replace, text, flags=re.MULTILINE)


def strip_first_heading(text: str) -> str:
    """Remove the first h1 heading from the text, keeping everything else."""
    return re.sub(r"^# .+\n*", "", text, count=1)


def convert_admonitions(text: str) -> str:
    """Convert !!! type 'Title' blocks to Pandoc fenced divs."""
    lines = text.split("\n")
    result: list[str] = []
    i = 0

    while i < len(lines):
        m = re.match(r"^!{3}\s+(\w+)(?:\s+\"([^\"]*)\")?\s*$", lines[i])
        if m:
            adm_type = m.group(1)
            title = m.group(2) or adm_type.capitalize()

            # Collect indented content (4-space indent)
            content: list[str] = []
            i += 1
            while i < len(lines):
                if lines[i].startswith("    "):
                    content.append(lines[i][4:])
                    i += 1
                elif lines[i].strip() == "":
                    # Peek ahead: if next non-empty line is indented, continue
                    j = i + 1
                    while j < len(lines) and lines[j].strip() == "":
                        j += 1
                    if j < len(lines) and lines[j].startswith("    "):
                        content.append("")
                        i += 1
                    else:
                        break
                else:
                    break

            # Trim trailing blanks
            while content and content[-1].strip() == "":
                content.pop()

            result.append(f'::: {{.admonition .{adm_type} title="{title}"}}')
            result.extend(content)
            result.append(":::")
            result.append("")
        else:
            result.append(lines[i])
            i += 1

    return "\n".join(result)


def replace_material_icons(text: str) -> str:
    """Replace :material-xxx: emoji shortcodes with text equivalents."""
    # Specific known icons
    known = {
        ":material-connection:": "",
        ":material-alert-circle:": "",
        ":material-plus-circle:": "",
        ":material-shield:": "",
        ":material-earth:": "",
        ":material-laptop:": "",
        ":material-infinity:": "",
    }
    for icon, repl in known.items():
        text = text.replace(icon, repl)
    # Catch-all for any remaining :material-xxx: patterns
    text = re.sub(r":material-([a-z-]+):", "", text)
    return text


def fix_image_paths(text: str, source_file: str, docs_dir: str) -> str:
    """Resolve image paths relative to docs/ and swap .webp -> .png."""
    source_dir = os.path.dirname(os.path.join(docs_dir, source_file))

    def _replace(m):
        alt = m.group(1)
        path = m.group(2)
        attrs = m.group(3) or ""

        # Resolve relative path to be relative to docs_dir
        if not os.path.isabs(path) and not path.startswith("http"):
            abs_path = os.path.normpath(os.path.join(source_dir, path))
            path = os.path.relpath(abs_path, docs_dir)

        # Swap .webp -> .png
        path = re.sub(r"\.webp$", ".png", path)

        # Convert { width="600" } to Pandoc-native {width=80%}
        if "width=" in attrs:
            attrs = "{width=80%}"
        elif attrs.strip():
            attrs = attrs  # keep other attrs as-is
        else:
            attrs = ""

        return f"![{alt}]({path}){attrs}"

    return re.sub(
        r"!\[([^\]]*)\]\(([^)]+)\)(\{[^}]*\})?",
        _replace,
        text,
    )


def simplify_internal_links(text: str) -> str:
    """Convert internal .md cross-references to plain text for print."""

    def _replace(m):
        display = m.group(1)
        target = m.group(2)
        # Only simplify relative .md links (internal cross-refs)
        if target.endswith(".md") or ".md#" in target or "/index.md" in target:
            return f"*{display}*"
        return m.group(0)

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _replace, text)


def strip_html_comments(text: str) -> str:
    """Remove HTML comments (<!-- ... -->)."""
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def extract_and_replace_mermaid(
    text: str, source_file: str, mermaid_dir: str
) -> tuple[str, list[tuple[str, str]]]:
    """Extract mermaid code blocks, save as .mmd files, replace with image refs.

    Returns (modified_text, [(mmd_filename, mermaid_source), ...]).
    """
    counter = [0]
    mermaid_blocks: list[tuple[str, str]] = []
    base = source_file.replace("/", "_").replace(".md", "")

    def _replace(m):
        counter[0] += 1
        mmd_name = f"{base}_mermaid_{counter[0]}.mmd"
        svg_name = f"{base}_mermaid_{counter[0]}.svg"
        mermaid_blocks.append((mmd_name, m.group(1)))
        svg_path = os.path.join(mermaid_dir, svg_name)
        return f"![Diagram]({svg_path})"

    modified = re.sub(
        r"```mermaid\n(.*?)```",
        _replace,
        text,
        flags=re.DOTALL,
    )
    return modified, mermaid_blocks


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

def preprocess_file(
    source_file: str,
    docs_dir: str,
    heading_shift: int,
    mermaid_dir: str,
    strip_h1: bool = False,
) -> tuple[str, list[tuple[str, str]]]:
    """Pre-process a single markdown file. Returns (text, mermaid_blocks)."""
    filepath = os.path.join(docs_dir, source_file)
    if not os.path.exists(filepath):
        print(f"  WARNING: {filepath} not found, skipping", file=sys.stderr)
        return "", []

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    text = strip_html_comments(text)
    text = convert_admonitions(text)
    text = replace_material_icons(text)
    text, mermaid_blocks = extract_and_replace_mermaid(
        text, source_file, mermaid_dir
    )
    text = fix_image_paths(text, source_file, docs_dir)
    text = simplify_internal_links(text)

    if strip_h1:
        text = strip_first_heading(text)

    text = shift_headings(text, heading_shift)

    return text.strip(), mermaid_blocks


def build_combined_document(docs_dir: str, mermaid_dir: str) -> tuple[str, list[tuple[str, str]]]:
    """Assemble all files into a single Pandoc-ready markdown document."""
    parts: list[str] = []
    all_mermaid: list[tuple[str, str]] = []

    # YAML front matter
    parts.append("""---
title: "Community Network Handbook"
subtitle: "A field guide to build community networks from scratch"
author: "AUCOOP"
date: "2025"
lang: "en"
---
""")

    # Preface (from home index.md)
    preface_file = os.path.join(docs_dir, "index.md")
    if os.path.exists(preface_file):
        text, mblocks = preprocess_file(
            "index.md", docs_dir, 0, mermaid_dir, strip_h1=True
        )
        if text.strip():
            parts.append("\\frontmatter\n")
            parts.append("# Preface {.unnumbered}\n")
            parts.append(text)
            parts.append("\n\\mainmatter\n")
        all_mermaid.extend(mblocks)

    # Main content
    for source_file, shift in NAV_ORDER:
        text, mblocks = preprocess_file(
            source_file, docs_dir, shift, mermaid_dir
        )
        if text.strip():
            parts.append(text)
            parts.append("")  # blank line separator
        all_mermaid.extend(mblocks)

    # Appendix (contributing.md)
    contrib_file = os.path.join(docs_dir, "contributing.md")
    if os.path.exists(contrib_file):
        text, mblocks = preprocess_file(
            "contributing.md", docs_dir, 0, mermaid_dir, strip_h1=True
        )
        if text.strip():
            parts.append("\n\\appendix\n")
            parts.append("# Contributing {.unnumbered}\n")
            parts.append(text)
        all_mermaid.extend(mblocks)

    return "\n\n".join(parts), all_mermaid


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Pre-process handbook for Pandoc")
    parser.add_argument(
        "--docs-dir",
        default="docs",
        help="Path to the docs/ directory (default: docs)",
    )
    parser.add_argument(
        "--output",
        default="build/book/combined.md",
        help="Output combined markdown file (default: build/book/combined.md)",
    )
    parser.add_argument(
        "--mermaid-dir",
        default="build/book/mermaid",
        help="Directory for extracted Mermaid files (default: build/book/mermaid)",
    )
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    os.makedirs(args.mermaid_dir, exist_ok=True)

    print(f"Pre-processing handbook from {args.docs_dir}...")
    combined, mermaid_blocks = build_combined_document(
        args.docs_dir, args.mermaid_dir
    )

    # Write combined markdown
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(combined)
    print(f"  -> {args.output} ({len(combined)} bytes)")

    # Write extracted Mermaid blocks
    for mmd_name, mmd_source in mermaid_blocks:
        mmd_path = os.path.join(args.mermaid_dir, mmd_name)
        with open(mmd_path, "w", encoding="utf-8") as f:
            f.write(mmd_source)
        print(f"  -> {mmd_path}")

    print(f"Done. {len(mermaid_blocks)} Mermaid diagrams extracted.")


if __name__ == "__main__":
    main()
