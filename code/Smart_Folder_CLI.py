#Project: Smart Folder CLI 

#Step1 import module
from pathlib import Path 
from datetime import datetime 
import shutil 

file_log = Path("log/activity.log")

#Step2fuction logging 
def log(message):
    with open(file_log, "a", encoding="utf-8") as file:
        file.write(f"{datetime.now()} | {message}")
        
#Step3 scan Folder 
def scan_folder(folder):
    return [f for f in folder.iterdir() if f.is_file()]


#step4 rename Files 
def rename_file(file):
    new_name = f"{file.stem}_{int(file.stat().st_mtime)}{file.suffix}"
    file.rename(file.parent / new_name)
    log(f"Renamed {file.name} → {new_name}")
    return Path(new_name) 

#step5 move file
def move_file(file, base_folder):
    ext = file.suffix.lower()[1:]
    target = base_folder / ext
    target.mkdir(exist_ok=True)
    try:
        shutil.move(str(file), str(target/file.name))
        log(f"Moved {file.name} -> {target}")
    except Exception as error:
        log(f"Error: {error}")


folder = Path(".")
files = scan_folder(folder)
for f in files:
    f = rename_file(f)
    move_file(f, folder)