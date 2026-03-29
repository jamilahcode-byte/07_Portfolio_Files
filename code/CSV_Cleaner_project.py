#Step 1: Import pandas module
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
    
#Step 4: normalice columns name
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", "_", regex=True)
    )

#Step 5: clean text values 
if "full_name" in df.columns:
    df["full_name"] = df["full_name"].astype(str).str.strip().str.title()

if "email_address" in df.columns:
    df["email_address"] = df["email_address"].astype(str).str.strip().str.lower()
if "phone_number" in df.columns:
   df["phone_number"] = df["phone_number"].astype(str).str.strip()  
   
#Step 6: Remove duplicates 
df = df.drop_duplicates(subset=["email_address"]) 

#Step 7: saved clean csv
df.to_csv(f"cleaned_{file_csv}")
print(f"\nCleaned CSV saved as 'cleaned_{file_csv}'")
