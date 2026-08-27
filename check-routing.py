#!/usr/bin/env python3
"""
check-routing.py - find drift between your routing table and your actual notes.

The Context Router's one real weakness: the routing table is maintained by hand,
so it goes stale. Projects get created mid-conversation and never indexed; projects
end and their rows linger. This finds both.

Usage:
    python3 check-routing.py [path-to-notes-folder]

Defaults to the folder the script sits in. Exits 0 if clean, 1 if drift was found.
No dependencies.
"""

import os
import re
import sys

SKIP_DIRS = {".git", ".obsidian", ".trash", "node_modules", "__pycache__"}
SKIP_CONTEXT = {"_TEMPLATE_CONTEXT.md"}


def find_context_files(root):
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith("_CONTEXT.md") and fn not in SKIP_CONTEXT:
                full = os.path.join(dirpath, fn)
                found.append(os.path.relpath(full, root))
    return sorted(found)


def has_routing_rows(text):
    """A real routing table has table rows containing _CONTEXT.md paths."""
    for line in text.splitlines():
        if line.strip().startswith("|") and "_CONTEXT.md" in line:
            return True
    return False


def find_rules_file(root):
    """The routing table usually sits in CLAUDE.md at the root, but plenty of
    vaults keep a thin pointer there and the real table one folder down
    (e.g. _AI/CLAUDE.md). Look for the file that actually has the table."""
    candidates = []
    for name in ("CLAUDE.md", "AGENTS.md"):
        candidates.append(os.path.join(root, name))
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        depth = os.path.relpath(dirpath, root).count(os.sep) + 1
        if os.path.relpath(dirpath, root) == ".":
            continue
        if depth > 2:
            dirnames[:] = []
            continue
        for name in ("CLAUDE.md", "AGENTS.md", "MEMORY.md"):
            if name in filenames:
                candidates.append(os.path.join(dirpath, name))

    fallback = None
    for path in candidates:
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
        rel = os.path.relpath(path, root)
        if has_routing_rows(text):
            return rel, text
        if fallback is None and "_CONTEXT.md" in text:
            fallback = (rel, text)
    return fallback if fallback else (None, None)


PLACEHOLDER = re.compile(r"(projectfolder|\[|\bproject name\b|<)", re.I)


def routing_section(text):
    """Rules files often contain more than one table (a 'where things go' guide,
    a pruning table). Only the routing map lists real project paths, so use just
    that section when a heading names it."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith("#") and re.search(r"rout", line, re.I):
            start = i
            break
    if start is None:
        return text
    end = len(lines)
    level = len(lines[start]) - len(lines[start].lstrip("#"))
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("#"):
            lvl = len(lines[j]) - len(lines[j].lstrip("#"))
            if lvl <= level:
                end = j
                break
    return "\n".join(lines[start:end])


def routed_paths(text):
    """Pull every _CONTEXT.md path out of the routing table's rows."""
    paths = set()
    for line in routing_section(text).splitlines():
        if not line.strip().startswith("|"):
            continue
        for m in re.finditer(r"`?([^`|\s][^`|]*?_CONTEXT\.md)`?", line):
            candidate = m.group(1).strip().strip("`").lstrip("./")
            if PLACEHOLDER.search(candidate):
                continue
            paths.add(candidate)
    return paths


def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(__file__) or ".")
    rules_name, rules_text = find_rules_file(root)

    if rules_text and not has_routing_rows(rules_text):
        print(f"Found {rules_name}, but it has no routing table rows.")
        print("Nothing to check against yet. Run the setup interview first, or")
        print("point the script at the folder holding your real routing table.\n")
        return 1

    if not rules_text:
        print("No CLAUDE.md or AGENTS.md with a routing table found in:")
        print(f"  {root}")
        print("\nPoint the script at your notes folder:  python3 check-routing.py /path/to/notes")
        return 1

    on_disk = find_context_files(root)
    routed = routed_paths(rules_text)

    def norm(p):
        return p.replace("\\", "/").lstrip("./")

    on_disk_n = {norm(p) for p in on_disk}
    routed_n = {norm(p) for p in routed}

    orphans = sorted(on_disk_n - routed_n)
    dead = sorted(routed_n - on_disk_n)

    print(f"Notes folder : {root}")
    print(f"Rules file   : {rules_name}")
    print(f"Context files: {len(on_disk_n)}   Routing rows: {len(routed_n)}\n")

    if not orphans and not dead:
        print("No drift. Every project file has a routing row and every row points at a real file.")
        return 0

    if orphans:
        print(f"NOT ROUTED ({len(orphans)}) - these exist but nothing points at them.")
        print("Your AI will never find these on its own. Add a row, or delete the file.\n")
        for p in orphans:
            print(f"  {p}")
        print()

    if dead:
        print(f"DEAD ROWS ({len(dead)}) - the routing table points at files that aren't there.")
        print("Either the project moved, or it ended and the row should go.\n")
        for p in dead:
            print(f"  {p}")
        print()

    return 1


if __name__ == "__main__":
    sys.exit(main())
