import csv  # Import the CSV module to work with CSV files

# Open the CSV file in read mode
with open("data.csv", "r") as file:
    reader = csv.reader(file)  # Create a CSV reader object
    for row in reader:         # Loop through each row in the CSV
        print(row)             # Print the current row as a list