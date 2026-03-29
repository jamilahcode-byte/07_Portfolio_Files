Project Smart File Organizer CLI – MVP
from pathlib import Path
from datetime import datetime
import shutil, hashlib

LOG_FILE = Path("Logs/smart.log")
LOG_FILE.parent.mkdir(exist_ok=True)

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {msg}\n")

def scan_folder(folder):
    return [f for f in folder.iterdir() if f.is_file()]

def rename_file(file):
    new_name = f"{file.stem}_{int(file.stat().st_mtime)}{file.suffix}"
    file.rename(file.parent / new_name)
    log(f"Renamed: {file.name} → {new_name}")

def move_file(file, base_folder):
    ext = file.suffix.lower()[1:]
    target = base_folder / ext
    target.mkdir(exist_ok=True)
    shutil.move(str(file), str(target / file.name))
    log(f"Moved: {file.name} → {target}")

def backup(file):
    backup_dir = Path("Backups")
    backup_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copy2(file, backup_dir / f"{file.stem}_{timestamp}{file.suffix}")
    log(f"Backed up: {file.name}")