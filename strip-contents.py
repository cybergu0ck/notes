#!/usr/bin/env python3
"""
strip_contents.py

Removes redundant "Contents" navigation sections (the "[← Back to notes](...)"
link + "# Contents" heading + bullet list of links + trailing <br> lines)
that have been accidentally duplicated at the top of markdown notes.

Usage:
    python3 strip_contents.py [ROOT_DIR] [--dry-run] [--recursive] [--no-backup]

    ROOT_DIR       Directory to process (default: current directory)
    --dry-run      Show what would change without writing any files
    --recursive    Also process .md files in subdirectories (default: top-level only)
    --no-backup    Don't write .bak backup files before overwriting

By default, files literally named "contents.md" (case-insensitive) are
SKIPPED, since those are assumed to be the real table-of-contents file
that legitimately contains a "# Contents" list. Change SKIP_FILENAMES
below if that's not the case for you.
"""

import argparse
import os
import re
import sys

SKIP_FILENAMES = {"contents.md"}

# Matches a single stray "back to notes"-style navigation line, on its own
# line. Rather than trying to enumerate every possible arrow glyph/emoji
# (←, <-, <--, &larr;, ⬅, 🔙, etc.), this matches ANY line whose entire
# content is a single markdown link with "back" somewhere in its link text
# (case-insensitive). This covers "[← Back to notes](...)",
# "[<- Back to Notes](...)", "[⬅ back](...)", "[Go back](...)", etc.
BACK_LINK_RE = re.compile(
    r'^[ \t]*\[[^\]]*\bback\b[^\]]*\]\([^\n)]*\)[ \t]*\n?',
    re.MULTILINE | re.IGNORECASE,
)

# Matches one full "Contents" block:
#   '# Contents' heading
#   optional blank lines
#   one or more bullet-list lines (possibly indented, i.e. sub-items)
#   optional blank lines
#   zero or more '<br>' lines
#   optional trailing blank lines
CONTENTS_BLOCK_RE = re.compile(
    r'^#[ \t]+Contents[ \t]*\n'          # the "# Contents" heading line
    r'(?:[ \t]*\n)*'                      # blank line(s) after heading
    r'(?:^[ \t]*-\s+.*\n)+'               # one or more '- [...]' list lines
    r'(?:[ \t]*\n)*'                      # blank line(s) before <br>s
    r'(?:^<br>[ \t]*\n)*'                 # zero or more '<br>' lines
    r'(?:[ \t]*\n)*',                     # trailing blank line(s)
    re.MULTILINE,
)

# Collapse 3+ blank lines into a single blank line.
MULTI_BLANK_RE = re.compile(r'\n{3,}')


def clean_markdown(text: str) -> str:
    original = text

    # 1. Remove every stray "back to notes" link line.
    text = BACK_LINK_RE.sub('', text)

    # 2. Remove every "# Contents" block (heading + link list + <br>s).
    text = CONTENTS_BLOCK_RE.sub('', text)

    # 3. Strip any leading blank lines / stray <br> lines left at the
    #    very top of the file now that the Contents blocks are gone.
    text = re.sub(r'\A(?:[ \t]*\n|^<br>[ \t]*\n)+', '', text, flags=re.MULTILINE)

    # 4. Collapse runs of 3+ blank lines into a single blank line.
    text = MULTI_BLANK_RE.sub('\n\n', text)

    changed = text != original
    return text, changed


def find_md_files(root: str, recursive: bool):
    if recursive:
        for dirpath, _dirnames, filenames in os.walk(root):
            for name in filenames:
                if name.lower().endswith('.md'):
                    yield os.path.join(dirpath, name)
    else:
        for name in os.listdir(root):
            full = os.path.join(root, name)
            if os.path.isfile(full) and name.lower().endswith('.md'):
                yield full


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', default='.', help='Root directory (default: current dir)')
    parser.add_argument('--dry-run', action='store_true', help="Preview changes, don't write files")
    parser.add_argument('--recursive', action='store_true', help='Recurse into subdirectories')
    parser.add_argument('--no-backup', action='store_true', help="Don't write .bak files")
    args = parser.parse_args()

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f"Error: '{root}' is not a directory", file=sys.stderr)
        sys.exit(1)

    files = sorted(find_md_files(root, args.recursive))
    if not files:
        print("No .md files found.")
        return

    changed_count = 0
    for path in files:
        name = os.path.basename(path)
        if name.lower() in SKIP_FILENAMES:
            print(f"SKIP  (protected filename): {path}")
            continue

        with open(path, 'r', encoding='utf-8') as f:
            original = f.read()

        cleaned, changed = clean_markdown(original)

        if not changed:
            print(f"OK    (no Contents section found): {path}")
            continue

        changed_count += 1
        if args.dry_run:
            print(f"WOULD CHANGE: {path}")
            continue

        if not args.no_backup:
            with open(path + '.bak', 'w', encoding='utf-8') as f:
                f.write(original)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f"CLEANED: {path}")

    verb = "would be" if args.dry_run else "were"
    print(f"\n{changed_count} of {len(files)} file(s) {verb} changed.")


if __name__ == '__main__':
    main()