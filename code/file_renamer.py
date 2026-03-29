import shutil
from pathlib import Path

base = Path()
count = 1
dry_run = True

for item in base.iterdir():
    if not item.is_file():
        continue

    if item.name.startswith("file_"):
        continue

    new_name = f"file_{count}{item.suffix}"
    new_path = base / new_name

    print(f"{item.name} -> {new_name}")

    if new_path.exists():
        print("Skip (exists):", new_name)
    elif not dry_run:
        shutil.move(item, new_path)

    count += 1

print("Done.")