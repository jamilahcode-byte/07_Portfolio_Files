Project: Folder Scanner Tool

#Step1 import class 
from pathlib import Path 

#Step2 get folder path 
folder = Path(input("Enter folder path: "))

#step3 category files 
category = {}

#Step3 checks if folder path exists 
if folder.exists() and folder.is_dir():
    for item in folder.iterdir():
        if item.is_file():
            print("File:",item.name)
            category[item.suffix] = category.get(item.suffix, 0) + 1
        elif item.is_dir():
            print("Folder:",item.name)        
        else:
            print("unknown things:", item) 
    print(category)
else:
    print("Folder not found")   