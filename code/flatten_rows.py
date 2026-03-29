import csv  # Import CSV module to read CSV files

# List to store all CSV values in a single flat list
flat = []

# Open the cleaned CSV file
with open("data_clean.csv", "r") as file:
    reader = csv.reader(file)  # Create a CSV reader object
    
    # Loop through each row in the CSV
    for row in reader:
        # Add all values of the row to the flat list
        flat.extend(row)  # extend() adds each element individually
    
# Print the flattened list
print(flat)