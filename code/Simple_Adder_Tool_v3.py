# Simple_Adder_Tool_v3.py
# A simple command-line tool that safely adds two numbers
# and saves the result to a text file.

# Function to safely get a number from the user
def get_number(prompt):
    """
    Repeatedly asks the user for input until a valid integer is entered.
    Returns the integer value.
    """
    while True:
        try:
            # Attempt to convert user input to an integer
            return int(input(prompt))
        except ValueError:
            # Handle invalid (non-numeric) input
            print("⚠️ Please enter a valid number!")

# Function to calculate, format, and display the result
def display_result(num1, num2):
    """
    Adds two numbers, prints the formatted result,
    and returns the calculated value.
    """
    result = num1 + num2
    print(f"💡 {num1} + {num2} = {result}")
    return result

# -------------------- Main Program Logic --------------------

# Get the first number from the user
num1 = get_number("Enter first number: ")

# Get the second number from the user
num2 = get_number("Enter second number: ")

# Calculate the sum and display it
total = display_result(num1, num2)

# Save the result automatically to a file (append mode)
with open("Simple_Adder_Results.txt", "a") as f:
    f.write(f"{num1} + {num2} = {total}\n")

# Confirm successful save
print("✅ Result saved automatically!")