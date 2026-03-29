Project: File Reader CLI
#v1_basic
#step1 import module 
from pathlib import Path 

#step2 ask user file or folder path 
file_path = Path(input("Enter file path:"))

def reader_file(file_path):
    #step3 try reading content & catch error 
    try:
        content = file_path.read_text(encoding="utf-8")
        return content
    except FileNotFoundError:
        print("File not found!")

print(reader_file(file_path ))