# List of numbers
numbers = [1, 2, 3, 4]

# Variable to store the total sum
total = 0 

# Loop through each number and add it to total
for num in numbers:
    total += num

# Print the final sum
print(total)

# Conditions & loops:
# Loop through the list again
for num in numbers:
    # Check if the number is greater than 2
    if num > 2:
        # Print numbers that satisfy the condition
        print(num)