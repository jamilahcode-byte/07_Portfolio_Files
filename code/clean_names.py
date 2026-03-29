# Ask the user to enter names separated by commas
names = input("Enter all names separated by commas: ").split(",")

# Create an empty list to store cleaned names
clean = []

# Loop through each name in the input list
for name in names:
    # Remove extra spaces from the beginning and end
    clean.append(name.strip())

# Print the cleaned list of names
print(clean)