#Step 1: import module 
import pandas as pd

#Step 2: get from user file csv
file_csv = input("Enter file csv need clean: ").strip()

#Step 3: load & read messy csv
df = pd.read_csv(file_csv, encoding="utf-8")

#Step 4: see & display messy csv
print(df.columns)
print(df.head())

#Step 5: clean columns names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", "_",  regex=True)
        )

#Step 6: clean text values
df["full_name"] = df["full_name"].str.replace(r"\s+", " ", regex=True).str.title()
df["email_address"] = df["email_address"].str.strip().str.lower()
df["phone_number"] = df["phone_number"].astype(str).str.strip()

#Step 7: checks validation 
print(df.nunique())

#Step 8:  save clean csv
df.to_csv("clean_leads.csv", index=False)