# filter_numbers.py
# Micro-Project — Day 2: Filter Numbers Tool
# Purpose: Filter numbers greater than a user-defined threshold
# Skills used: lists, loops, conditionals, input validation, file writing, functions

# List of numbers to work with
numbers = [1, 2, 3, 4, 12, 14, 42, 32, 45, 56, 76, 78, 89, 98, 102]

# Ask the user for a threshold value
# Loop ensures the program does not crash on invalid input
while True:
    try:
        # Convert user input to integer
        threshold = int(input("Enter a threshold number (1-100): "))
        break  # Exit loop if input is valid
    except ValueError:
        # Runs if input cannot be converted to int
        print("Please enter a valid number!")

# Display numbers greater than the threshold
print(f"\nNumbers greater than {threshold}:")
for num in numbers:
    if num > threshold:
        print(num)

# Save filtered results to a text file
with open("filter_numbers_results.txt", "w") as f:
    for num in numbers:
        if num > threshold:
            f.write(f"{num}\n")

print("\nResults saved to filter_numbers_results.txt")

# Function version (reusable and clean)
def filter_numbers(numbers, threshold):
    """
    Returns a list of numbers greater than the given threshold
    """
    return [n for n in numbers if n > threshold]

# Call the function and store the result
result = filter_numbers(numbers, threshold)

# Print the final filtered list
print(result)