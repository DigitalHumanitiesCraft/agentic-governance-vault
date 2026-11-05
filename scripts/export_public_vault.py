# /// script
# requires-python = ">=3.11"
# ///
"""Copy the committed vault into a public repository folder, without originals.

Data flow: the list of files comes from `git ls-files` of this vault, so only
committed material leaves the machine and gitignored files (eingang/, output/,
generated data.js, Obsidian workspace state) never do. From that list the
stored originals in sources/ are dropped, because they belong to their
publishers; their own summaries in sources/summaries/ stay, and quellen.md
links every original at its publisher. The target folder is replaced except
for its .git directory and the files named in KEEP, which the public
repository maintains itself.

Usage: uv run scripts/export_public_vault.py <target folder>
"""

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEEP = {".git", "README.md", "LICENSE.md"}


def _published(rel: str) -> bool:
    parts = rel.split("/")
    if parts[0] == "sources" and len(parts) == 2:
        return False  # originals; sources/summaries/ is a subfolder and stays
    return parts[0] != "eingang" or rel == "eingang/README.md"


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit("Usage: export_public_vault.py <target folder>")
    target = Path(sys.argv[1]).resolve()
    if ROOT in target.parents or target == ROOT:
        sys.exit("The target must lie outside the vault.")
    listing = subprocess.run(
        ["git", "-c", "core.quotepath=off", "ls-files", "-z", "."],
        cwd=ROOT,
        capture_output=True,
        check=True,
    ).stdout.decode("utf-8")
    files = sorted(f for f in listing.split("\0") if f and _published(f))
    missing = [f for f in files if not (ROOT / f).is_file()]
    if missing:
        sys.exit(f"Committed files missing in the working tree: {missing[:5]}")
    target.mkdir(parents=True, exist_ok=True)
    for entry in target.iterdir():
        if entry.name in KEEP:
            continue
        shutil.rmtree(entry) if entry.is_dir() else entry.unlink()
    for rel in files:
        if rel in KEEP:
            continue
        dest = target / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / rel, dest)
    print(f"{len(files)} files exported to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
