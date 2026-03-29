import pandas as pd
#Step 1: INSPECT DATA
df = pd.read_csv("data.csv")
print(df.head())
print(df.info())

#step 2: HANDLE ENCODING ERRORS
df = pd.read_csv("data.csv", encoding="utf-8", errors="ignore")

#Step 3: REMOVE DUPLICATES (SMART)
df = df.drop_duplicates()

#Step 3.5: Remove duplicates by column:
df = df.drop_duplicates(subset=["email"])

#STEP 4 — MISSING VALUES STRATEGY
df = df.dropna()        # remove rows
df = df.fillna("N/A")  # or fill

#Step 5: TEXT NORMALIZATION
df["name"] = df["name"].str.strip().str.lower()
df["email"] = df["email"].str.replace(" ", "")

#Step 6: — COLUMN STANDARDIZATION
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

#STEP 7: — VALIDATE DATA
print(df.isna().sum())
print(df.duplicated().sum())

#STEP 8: — EXPORT CLEAN FILE
df.to_csv("clean_data.csv", index=False)