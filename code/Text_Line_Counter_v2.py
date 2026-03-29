#Project: Text Line Counter
"""
A tiny script with real output. Freelancer-useful. No extras.
"""

#ask user file name
filename = input("Enter filename want count number lines: ").strip()

total_lines = 0

#read data from file
try:
    with open(filename, "r", encoding="utf-8") as file:
        #store lines in content 
        for line in file.readlines():
            total_lines += 1
except FileNotFoundError:
    print("File not found!")
except UnicodeDecodeError:
    print("Cannot decode file")
else:    
    #display on screen number lines
    print(f"The number line have this file: {total_lines}")