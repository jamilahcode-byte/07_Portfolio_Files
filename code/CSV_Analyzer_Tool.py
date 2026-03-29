import csv  # Import CSV module for reading CSV files

def analyze_csv(file_path):
    """
    Analyze a CSV file and calculate basic statistics on the 'age' column.
    Assumes 'age' is the second column (index 1).
    """
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)  # Read header row
        
        total_rows = 0
        ages = []  # List to store valid ages
        
        for row in reader:
            total_rows += 1
            # Check if the age column is not empty
            if row[1]:
                try:
                    ages.append(int(row[1]))
                except ValueError:
                    print(f"Invalid age value skipped: {row[1]}")
        
        # Print basic stats
        print(f"Total rows: {total_rows}")
        if ages:  # Avoid error if ages list is empty
            print(f"Max age: {max(ages)}")
            print(f"Min age: {min(ages)}")
            print(f"Average age: {sum(ages)/len(ages):.2f}")
        else:
            print("No valid age data found.")

# Run the tool
file_name = input("Enter CSV filename: ")
analyze_csv(file_name)