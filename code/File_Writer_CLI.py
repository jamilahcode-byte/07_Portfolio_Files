Project: File Writer CLI

#step1 import class 
from pathlib import Path 

file_path = Path(input("Enter file path want write: "))
content = input("Enter content store: ")
def writer_file(file_path, content):
    try:
        file_path.write_text(content,  encoding="utf-8")
        print("File written successfully")
    except Exception as error:
        print(f"Error: {error}")

def append_file(file_path, content):
    try:
        file_path.open("a").write(content)
        print("File written successfully")
    except Exception as error:
        print(f"Error: {error}")
        
choice = input("""
     MENU
  1.File overwrite
  2.File append
  3.Exit
Enter choice number:""")

if choice == "1":
    writer_file(file_path, content )
elif choice == "2":
    append_file(file_path, content )
elif choice == "3":
    print("Exit..")
else:
    print("Invalid jumper choice")