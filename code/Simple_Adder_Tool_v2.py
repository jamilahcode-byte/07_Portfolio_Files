# Function that gets a number from the user
# It takes one parameter: prompt (the message shown to the user)
def get_number(prompt):
    return int(input(prompt))  # Convert user input to integer and return it


# Get first number from the user
num1 = get_number("Enter first number: ")

# Get second number from the user
num2 = get_number("Enter second number: ")

# Print the sum directly
print("Result:", num1 + num2)


# Function that adds two numbers
# It takes two parameters and returns their sum
def add(num1, num2):
    return num1 + num2


# Call the add function using previously entered numbers
result = add(num1, num2)

# Print the result returned by the function
print("Result:", result)