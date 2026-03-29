
#Step1 import modules (hashlib)
import hashlib
from pathlib import Path 

#Step2 define function 
def file_hash(path):
    hash = hashlib.md5()
    with open(path, "rb") as f:
        hash.update(file.read())
        return hash.hexdigest()

#Step3 get folder path 
folder = Path("Txt")   

seen = {}

for file in folder.iterdir():
    if file.is_file():
        hash = file_hash()
        if hash in seen:
            print("DUPLICATE:", file.name, "==", seen[hash])
        else:
            seen[hash] = file.name