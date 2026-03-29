Project Master Smart File Organizer

from pathlib import Path
from datetime import datetime
import shutil, hashlib, argparse

# Logging setup
LOG_FILE = Path("Logs/smart.log")
LOG_FILE.parent.mkdir(exist_ok=True)  # Ensure Logs folder exists

# Backup folder
BACKUP_DIR = Path("Backups")
BACKUP_DIR.mkdir(exist_ok=True)

def scan_folder(folder: Path):
    if not folder.exists():
        log(f"ERROR: Folder {folder} does not exist")
        return []
    files = [f for f in folder.iterdir() if f.is_file()]
    log(f"Scanned {len(files)} files in {folder}")
    return files
def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {message}\n")
def read_file(file: Path):
    try:
        content = file.read_text(encoding="utf-8")
        log(f"Read: {file.name}")
        return content
    except Exception as e:
        log(f"ERROR reading {file.name}: {e}")
        return ""
        
def append_file(file: Path, text: str):
    try:
        with file.open("a", encoding="utf-8") as f:
            f.write(text + "\n")
        log(f"Appended to: {file.name}")
    except Exception as e:
        log(f"ERROR appending {file.name}: {e}")
def rename_file(file: Path):
    try:
        new_name = f"{file.stem}_{int(file.stat().st_mtime)}{file.suffix}"
        file.rename(file.parent / new_name)
        log(f"Renamed: {file.name} → {new_name}")
        return file.parent / new_name
    except Exception as e:
        log(f"ERROR renaming {file.name}: {e}")
        return file

def move_file(file: Path, base_folder: Path):
    try:
        ext = file.suffix.lower()[1:]
        target = base_folder / ext
        target.mkdir(exist_ok=True)
        shutil.move(str(file), str(target / file.name))
        log(f"Moved: {file.name} → {target}")
    except Exception as e:
        log(f"ERROR moving {file.name}: {e}")
def file_hash(file: Path):
    h = hashlib.md5()
    try:
        h.update(file.read_bytes())
        return h.hexdigest()
    except Exception as e:
        log(f"ERROR hashing {file.name}: {e}")
        return None

def detect_duplicates(files):
    seen = {}
    duplicates = []
    for f in files:
        h = file_hash(f)
        if h:
            if h in seen:
                duplicates.append((f, seen[h]))
            else:
                seen[h] = f
    log(f"Detected {len(duplicates)} duplicates")
    return duplicates
def backup_file(file: Path):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_name = f"{file.stem}_{timestamp}{file.suffix}"
    shutil.copy2(file, BACKUP_DIR / new_name)
    log(f"Backed up: {file.name} → {new_name}")
    
def batch_report(folder: Path, output_file: Path):
    with output_file.open("w", encoding="utf-8") as out:
        for f in folder.glob("*.*"):
            out.write(f"\n--- {f.name} ---\n")
            out.write(f"Size: {f.stat().st_size} bytes\n")
            out.write(f"Modified: {datetime.fromtimestamp(f.stat().st_mtime)}\n")
    log(f"Batch report created: {output_file.name}")    
def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer Suite")
    parser.add_argument("folder", type=str, help="Folder path to organize / مسار المجلد")
    parser.add_argument("--report", type=str, default="final_report.txt", help="Batch report output / تقرير الملخص")
    parser.add_argument("--dry-run", action="store_true", help="Preview actions without changes / عرض تجريبي")
    args = parser.parse_args()

    folder = Path(args.folder)
    files = scan_folder(folder)

    if not args.dry_run:
        for f in files:
            backup_file(f)
            new_file = rename_file(f)
            move_file(new_file, folder)
    duplicates = detect_duplicates(files)
    batch_report(folder, Path(args.report))
    print(f"Completed organizing {folder}, {len(duplicates)} duplicates found")    