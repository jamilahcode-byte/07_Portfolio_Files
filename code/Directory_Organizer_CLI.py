Project: Directory Organizer CLI 

#step1 import modules 
from pathlib import Path 
import shutil 

#Step2 get folder path
folder = Path(".")

count = 1

#step3 loop through files 
for item in folder.iterdir():
    #step4 checks is file
    if item.is_file():
        #step5 get extensions 
        ext = item.suffix.lower()[1:] # without dot 
        #step6 taget/create folder path for files 
        new_name = f"{item.stem}_{count}{item.suffix}"
        target = folder / ext 
        target.mkdir(exist_ok=True)
        #step7 move file to new path 
        try:
            shutil.move(item, str(target / new_name))
            count += 1
        except Exception as error:
            print("Error:", error)