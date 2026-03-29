# Project: Text Line Counter
"""
A tiny script with real output. Freelancer-useful. No extras.
Counts the number of lines in a text file.
"""

# Open the file in read mode with UTF-8 encoding
with open("data.txt", "r", encoding="utf-8") as file:
    # Read all lines and store them in a list
    lines = file.readlines()

# Display the total number of lines in the file
print(f"The number of lines in this file: {len(lines)}")