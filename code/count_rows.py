import csv  # Import the CSV module to work with CSV files

# Open the CSV file in read mode with UTF-8 encoding
# 'newline=""' avoids extra blank lines on some systems
with open("data_clean.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)   # Create a CSV reader object
    header = next(reader)       # Read the first row as header (skip it)
    
    # Count the remaining rows in the CSV
    # Using generator expression (no extra list in memory)
    count = sum(1 for _ in reader)

# Print total number of data rows (excluding header)
print("Total rows:", count)