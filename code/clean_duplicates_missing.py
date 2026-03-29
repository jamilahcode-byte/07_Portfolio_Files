#Step 1: import module 
import pandas as pd

#Step 2: get from user file csv
file_csv = input("Enter file csv need clean: ").strip()

#Step 3: Read & store for clean dataframe
df = pd.read_csv(file_csv, encoding="utf-8")

#Step 4: Removes duplicates 
df = df.drop_duplicates()

#step 5: fill missing email
df["email"] = df["email"].fillna("no_email@example.com ")


#Step 6: save cleaned file csv
df.to_csv(f"cleaned_{file_csv}", index=False)
print(f"File saved as cleaned_{file_csv}")


#Step 7: compare rows before & after
dirty_count = pd.read_csv(file_csv, encoding="utf-8").shape[0]

cleaned_count = pd.read_csv(f"cleaned_{file_csv}", encoding="utf-8").shape[0]

#Step 8: display result 
print(f"Rows before:  {dirty_count}, after: {cleaned_count}")
