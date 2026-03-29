

def clean_text(content: str) -> list[str]:
    """
    Clean and tokenize text content.
    
    Steps:
    - Strip leading/trailing whitespace from each line
    - Remove empty lines
    - Split into words
    - Return a list of cleaned words
    """
    # Normalize lines
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    print(lines)
    # Flatten into words
    words = [word for line in lines for word in line.split()]
    print(words)
    
    return " ".join(words).capitalize()


#print(clean_text(content ))

if __name__ == "__main__":
    pass