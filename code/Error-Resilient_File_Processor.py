Project: Error-Resilient File Processor

#step1 import module 
from pathlib import Path 
from datetime import datetime 

#srep2 get folder path & create parent 
log_file = Path("Logs/error.log")
log_file.parent.mkdir(exist_ok=True)


#Step3 define log water function 
def log(msg):
    log_file.write_text(
    f"{datetime.now()} | {msg}\n",
    encoding = "utf-8",
    errors = "ignored"
    )

#Step4 safely rename Files
def safe_rename(file):
    try:
        new_name = file.wth_name(file.stem + "_safe" + file.suffix)
        file.rename(new_name)
        log(f"Renamed: {file.name}")
    except Exception as e:
        log(f"ERROR on {file.name}: {e}")