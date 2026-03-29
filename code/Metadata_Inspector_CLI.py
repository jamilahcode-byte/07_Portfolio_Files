Project: Metadata Inspector CLI

#steps1 import module/class from library 
from pathlib import Path 
from datetime import datetime 

#step2 get files path 
file_path = Path(input("Enter file path: "))

def readable_size(size):
    if size  < 1024:
        return f"{size}B"
    elif size < 1024:
        return f"{size}KB"
    elif size/1024 < 1024:
        return f"{size}MB"
    elif size/1024/1024 < 1024:
        return f"{size}GB"  
    elif size/1024/1024/1024 < 1024:
        return f"{size}TB" 
    else:
        return f"unknowing" 
     
        


if file_path.exists():
    info = file_path.stat()
    size = readable_size(info.st_size)
    
    print("Size:", size)
    print("Create:", datetime.fromtimestamp(info.st_ctime))
    print("Modified:", datetime.fromtimestamp(info.st_mtime))
    