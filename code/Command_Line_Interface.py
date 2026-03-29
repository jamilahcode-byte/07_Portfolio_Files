Project Command Line Interface

import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Smart File Organizer CLI")
parser.add_argument("folder", type=str, help="Path to folder to organize")
parser.add_argument("--dry-run", action="store_true", help="Show actions without changing files")
args = parser.parse_args()

folder = Path(args.folder)
if not folder.exists():
    print("Folder does not exist")
    exit()

print(f"Organizing folder: {folder}")
# Call previously defined smart organizer functions here