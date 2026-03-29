#Step 1: import module & read excel
import pandas as pd 
 
df = pd.read_excel("raw.xlsx")

#Step 2: clean columns & rows
df.columns = (
    df.columns
    .str.strip()
    .str.title()   
    )

for column in df.columns:
    if df[column].dtype == "object":
        df[column] = df[column].str.strip().str.title()


#Step 3: Remove empty values for fill & Remove duplicates 
df = df.dropna(how="all")
df = df.drop_duplicates()

#Step 4: fill missing values 
df["Age"] = df["Age"].fillna(0)
df["Email"] = df['Email'].fillna("no_email@example.com")

#Step 5: save cleaned Excel
df.to_excel("cleaned_raw.xlsx", index=False)

#Step 6: display cleaned rwas
print("cleaned rows:\n", df)