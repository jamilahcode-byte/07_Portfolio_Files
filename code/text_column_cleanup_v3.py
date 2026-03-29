# Step 1: Import pandas module
import pandas as pd

# Step 2: Ask user for CSV file path
file_csv = input("Enter the CSV file path to clean: ").strip()

# Step 3: Load the CSV
# Use 'encoding="utf-8"' by default; can add error handling if needed
try:
    df = pd.read_csv(file_csv, encoding="utf-8")
except FileNotFoundError:
    print(f"Error: File '{file_csv}' not found.")
    exit()
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

# Step 4: Preview messy CSV
print("Original CSV preview:")
print("Columns:", df.columns.tolist())
print(df.head())

# Step 5: Clean column names
# Remove extra spaces, lowercase all letters, replace spaces with underscores
df.columns = (
    df.columns
    .str.strip()             # Remove leading/trailing spaces
    .str.lower()             # Convert to lowercase
    .str.replace(r"\s+", "_", regex=True)  # Replace one or more spaces with underscore
)

# Step 6: Clean text values
# Only clean if columns exist to prevent errors
if "full_name" in df.columns:
    df["full_name"] = df["full_name"].astype(str).str.strip().str.title()

if "email_address" in df.columns:
    df["email_address"] = df["email_address"].astype(str).str.strip().str.lower()
if "phone_number" in df.columns:
   df["phone_number"] = df["phone_number"].astype(str).str.strip()  
   

# Step 7: Validation checks
print("\nUnique value counts per column (after cleaning):")
print(df.nunique())

# Optional: Quick check for missing values
print("\nMissing values per column:")
print(df.isna().sum())

# Step 8: Save cleaned CSV
output_file = "clean_leads.csv"
df.to_csv(output_file, index=False)
print(f"\nCleaned CSV saved as '{output_file}'")