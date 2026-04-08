import os
import re
import sys
from pathlib import Path

def extract_headings(content):
    """Extract all headings from markdown content with their levels and text."""
    headings = []
    lines = content.split("\n")
    in_code_block = False

    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue

        if not in_code_block and line.startswith("#"):
            match = re.match(r"^(#{1,6})\s+(.+)", line)
            if match:
                level = len(match.group(1))
                text = match.group(2).strip()
                headings.append((level, text))

    return headings


def heading_to_anchor(text):
    """Convert heading text to a markdown anchor link."""
    anchor = text.lower()
    anchor = re.sub(r"[^\w\s-]", "", anchor)
    anchor = re.sub(r"\s+", "-", anchor)
    anchor = re.sub(r"-+", "-", anchor)
    anchor = anchor.strip("-")
    return anchor


def build_contents_section(headings):
    """Build a table of contents section from headings."""
    if not headings:
        return None

    lines = ["# Contents\n"]
    min_level = min(h[0] for h in headings)

    for level, text in headings:
        if text.lower() in ("contents", "table of contents", "toc"):
            continue

        indent = "  " * (level - min_level)
        anchor = heading_to_anchor(text)
        lines.append(f"{indent}- [{text}](#{anchor})")

    lines.append("\n<br>\n<br>\n<br>")

    return "\n".join(lines) + "\n"


def find_contents_block_end(lines):
    """Find the line index where the existing contents section ends."""
    in_contents = False
    for i, line in enumerate(lines):
        if re.match(r"^##\s+(Contents|Table of Contents|TOC)\s*$", line, re.IGNORECASE):
            in_contents = True
            continue
        if in_contents:
            # Contents section ends at the next heading (## or higher)
            if re.match(r"^#{1,6}\s+", line):
                return i
    return None


CONTENTS_PATTERN = re.compile(r"^#{1,2}\s+(Contents|Table of Contents|TOC)\s*$", re.IGNORECASE)


def has_contents_section(lines):
    return any(CONTENTS_PATTERN.match(l) for l in lines)


def remove_existing_contents(lines):
    start = None
    end = None

    for i, line in enumerate(lines):
        if CONTENTS_PATTERN.match(line):
            start = i
            continue
        if start is not None and end is None:
            if re.match(r"^#{1,6}\s+", line):
                end = i
                break

    if start is not None:
        end = end or len(lines)
        return lines[:start] + lines[end:]

    return lines


def inject_contents(file_path):
    """Inject a contents section into a markdown file."""
    path = Path(file_path)
    original_content = path.read_text(encoding="utf-8")
    lines = original_content.split("\n")

    # Remove existing contents section if present, preserving all other lines
    if has_contents_section(lines):
        lines = remove_existing_contents(lines)

    content_for_headings = "\n".join(lines)
    headings = extract_headings(content_for_headings)

    if len(headings) < 2:
        print(f"  Skipping (too few headings): {path.name}")
        return

    contents_section = build_contents_section(headings)
    if not contents_section:
        return

    # Always insert contents at the very top, before everything else
    contents_lines = contents_section.split("\n")
    lines = contents_lines + ["", "", ""] + lines

    new_content = "\n".join(lines)

    if new_content != original_content:
        path.write_text(new_content, encoding="utf-8")
        print(f"  Updated: {path}")
    else:
        print(f"  No changes: {path}")

def process_directory(root_dir):
    """Walk through all directories and process markdown files."""
    root_path = Path(root_dir).resolve()
    print(f"Scanning: {root_path}\n")

    md_files = sorted(root_path.rglob("*.md"))

    if not md_files:
        print("No markdown files found.")
        return

    print(f"Found {len(md_files)} markdown file(s):\n")
    for md_file in md_files:
        inject_contents(md_file)

    print(f"\nDone! Processed {len(md_files)} file(s).")

#-----------------------------------------------------------------------------------------------------------
EXCLUDE_DIRECTORY = ("_assets", "_resources", ".git")

def get_heading(level):
    return "#" * level


def build_index_for_directory(current_path, root_path, level=2):
    """Build markdown content for a single directory's index file."""
    lines = []

    try:
        subdirs = sorted([p for p in current_path.iterdir() if p.is_dir()])
        md_files = sorted(current_path.glob("*.md"))
    except PermissionError:
        return ""

    # Backlink to parent (if not root)
    if current_path != root_path:
        parent = current_path.parent
        if parent == root_path:
            parent_index = f"../{root_path.name}.md"
        else:
            parent_index = f"../{parent.name}.md"
        lines.append(f"[← Back to {parent.name}]({parent_index})\n")

    lines.append(f"# {current_path.name}\n")

    # List .md files directly in this directory (excluding the index file itself)
    index_filename = f"{current_path.name}.md"
    direct_md_files = [f for f in md_files if f.name != index_filename]
    if direct_md_files:
        lines.append("## Files\n")
        for md_file in direct_md_files:
            lines.append(f"- [{md_file.name}]({md_file.name})\n")

    # List subdirectories with links to their index files
    visible_subdirs = [d for d in subdirs if d.name not in EXCLUDE_DIRECTORY]
    if visible_subdirs:
        lines.append("## Subdirectories\n")
        for subdir in visible_subdirs:
            subdir_index = f"{subdir.name}/{subdir.name}.md"
            lines.append(f"- [{subdir.name}]({subdir_index})\n")

    return "\n".join(lines)


def create_index_files(root_dir):
    """Create an index .md file for the root and every subdirectory."""
    root_path = Path(root_dir).resolve()

    def walk(current_path):
        try:
            subdirs = sorted([p for p in current_path.iterdir() if p.is_dir()])
        except PermissionError:
            return

        # Write index file for current directory
        index_filename = f"{current_path.name}.md"
        output_file = current_path / index_filename
        content = build_index_for_directory(current_path, root_path)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Created: {output_file}")

        # Recurse into subdirectories
        for subdir in subdirs:
            if subdir.name in EXCLUDE_DIRECTORY:
                continue
            walk(subdir)

    walk(root_path)

if __name__ == "__main__":
    import sys
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    process_directory(root) #creates contents section in each markdown file
    create_index_files(root) #creates a content.md file in the root directory