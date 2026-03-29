#Step 1: import module
import pandas as pd 

#Step 2: read excel
df = pd.read_excel("raw.xlsx")

#Step 3: Remove empty values for fill
df = df.dropna(how="all")

print(df.columns)
#Step 4: fill missing values 
df["Age"] = df["Age"].fillna(0)

#Step 5: save cleaned Excel
df.to_excel("cleaned_raw.xlsx", index=False)

#Step 6: display cleaned rwas
print("cleaned rows:\n", df)