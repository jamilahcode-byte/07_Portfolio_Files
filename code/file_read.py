# Read data from a file
with open("data.txt", "r", encoding="utf-8") as file:
    # Store the entire content of the file in a variable
    content = file.read()
    
    # Display the content on the screen
    print(content)