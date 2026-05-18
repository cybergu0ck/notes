import os
import re


def slugify(text):
    return re.sub(r"[^a-zA-Z0-9\- ]", "", text).strip().lower().replace(" ", "-")


def find_markdown_files(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md") and file != "contents.md":
                yield os.path.join(root, file)


def parse_headings(file_path):
    headings = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r"^(#{1,6})\s+(.*)", line)
            if match:
                level = len(match.group(1))
                title = match.group(2).strip()
                headings.append((level, title))
    return headings


def build_toc(root_dir):
    toc_lines = []
    for md_file in sorted(find_markdown_files(root_dir)):
        rel_path = os.path.relpath(md_file, root_dir)
        headings = parse_headings(md_file)
        if not headings:
            continue

        # Group by top-level heading (#)
        for i, (level, title) in enumerate(headings):
            if level == 1:
                link = f"{rel_path}#{slugify(title)}"
                toc_lines.append(f"- [{title}]({link})")
                # Collect all subheadings under this top-level heading
                subheadings = []
                for sub_level, sub_title in headings[i + 1 :]:
                    if sub_level == 1:
                        break
                    indent = "  " * (sub_level - 1)
                    sub_link = f"{rel_path}#{slugify(sub_title)}"
                    subheadings.append(f"{indent}- [{sub_title}]({sub_link})")
                if subheadings:
                    toc_lines.extend(subheadings)
                toc_lines.append("")  # Blank line
                toc_lines.append("")  # Another blank line
    return "\n".join(toc_lines)


def write_contents_md(root_dir):
    toc = build_toc(root_dir)
    with open(os.path.join(root_dir, "contents.md"), "w", encoding="utf-8") as f:
        f.write("# Table of Contents\n\n")
        f.write(toc)
        f.write("\n")


if __name__ == "__main__":
    write_contents_md(".")
    print("contents.md generated!")
