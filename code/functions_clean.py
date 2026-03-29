# Function to clean text by removing extra spaces and converting to lowercase
def clean_text(text):
    return text.strip().lower()  # strip() removes spaces at start/end, lower() makes lowercase

# Try-except block to handle unexpected errors
try:
    # Test the function
    print(clean_text("  hello "))
except Exception as e:
    # Print error message if something goes wrong
    print("Error:", e)