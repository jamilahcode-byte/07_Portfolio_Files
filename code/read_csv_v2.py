import csv  # Import CSV module

# Function to read a CSV file safely and print each row
def reader_csv(filename):
    try:
        # Open file in read mode with universal newline support
        with open(filename, "r", newline="", encoding="utf-8") as file:
            # Loop through each row using CSV reader
            for row in csv.reader(file):
                print(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as error:
        # Catch any other errors (permissions, encoding, etc.)
        print(f"Error: {error}")

# Ask user for the CSV file name
filename = input("Enter the CSV filename you want to read: ").strip()

# Call the function with user input
reader_csv(filename)