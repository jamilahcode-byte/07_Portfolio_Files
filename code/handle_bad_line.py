import pandas as pd

# Function to handle bad lines
def handle_bad_line(bad_line: list):
    # Example: just print it for review
    print("Bad line found:", bad_line)
    
    # Optionally, try to fix it
    # For example, fill missing columns with empty strings if shorter
    expected_columns = 5  # change to your actual number of columns
    if len(bad_line) < expected_columns:
        bad_line += [''] * (expected_columns - len(bad_line))
    elif len(bad_line) > expected_columns:
        # truncate extra columns
        bad_line = bad_line[:expected_columns]
    
    return bad_line

# Load CSV and process bad lines
df = pd.read_csv('data.csv', encoding='utf-8', on_bad_lines=handle_bad_line)

# Preview data
print(df.head())

# Remove duplicate rows
df = df.drop_duplicates()

# Fix column names
df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

# Fill empty cells
df['email'] = df['email'].fillna('no_email@example.com')

# Remove rows with all empty cells
df = df.dropna(how='all')

# Normalize text
df['name'] = df['name'].str.strip().str.title()

# Save cleaned CSV
df.to_csv('samples/cleaned_sample.csv', index=False)

# Save Excel version
df.to_excel('samples/cleaned_sample.xlsx', index=False)