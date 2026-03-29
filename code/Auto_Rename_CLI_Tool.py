Project: Auto-Rename CLI Tool

#steps1 import module/class from library 
from pathlib import Path 
from datetime import datetime 

#step2 get files path 
folder_path = Path(input("Enter folder path: "))

for item in folder_path.iterdir():
    if item.is_file():
        new_name = f"{item.stem}_{datetime.fromtimestamp(item.stat().st_mtime)}{item.suffix}"
        try:
            item.rename(folder/new_name)
            print(f"Renamed {item.name} -> {new_name}")
        except Exception as error:
            print("Error:", error)

