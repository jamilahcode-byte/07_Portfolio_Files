# Day 4 — Handling user input with error checking

while True:
    try:
        # Ask the user to enter a number
        num = int(input("Enter a number: "))
        
        # Print the number entered by the user
        print("You entered:", num)
        
        # Exit the loop if input is valid
        break
    except ValueError:
        # If input is not a valid integer, show an error and repeat
        print("Invalid number, try again.")