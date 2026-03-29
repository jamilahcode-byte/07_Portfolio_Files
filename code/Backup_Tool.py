Prohect_Versioned Backup Tool
#Step1 import modules 
from pathlib import Path
from datetime import datetime
import shutil

#Step2 Backup function 
def backup(files):
    back_up = Path("Backups")
    backup_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%m%s")
    new_name = f"{file.stem}_{timestamp}{file.suffix}"
    shutil.copy2(file, backup_dir / new_name)
