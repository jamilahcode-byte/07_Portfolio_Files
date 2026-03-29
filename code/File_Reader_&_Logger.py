Project: File Reader + Logger

#step1 import module/class from library 
from pathlib import Path 
from datetime import datetime 

def log(message):
    with open("file.log", "w", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {message}\n")


file_path = Path(input("Enter file path:"))

def reader_file(file_path):
    #step3 try reading content & catch error 
    try:
        content = file_path.read_text(encoding="utf-8")
        log(f"read_file: {file_path}")
        return content
    except Exception as error:
        print("File not found!")
        log(f"Failed to read: {file_path} , Error: {errror}")

print(reader_file(file_path ))