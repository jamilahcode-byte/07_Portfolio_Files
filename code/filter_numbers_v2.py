# List of numbers to check against a threshold
numbers = [1, 2, 3, 4, 12, 14, 42, 32, 45, 56, 76, 78, 89, 98, 102]

# Ask the user to enter a threshold number
threshold = int(input("Enter a number to use as a threshold (1–100): "))

# Loop through each number in the list
for num in numbers:
    # Check if the number is greater than the threshold
    if num > threshold:
        # Print numbers that exceed the threshold
        print(num)