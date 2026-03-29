import pandas as pd

# Load CSV with encoding fix and skip bad lines
df = pd.read_csv('data.csv', encoding='utf-8', on_bad_lines='skip')

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