#import module 
import pandas as pd

#ask user file csv
file_csv = input("Enter file need read & copy: ").strip()

#Read & display csv
df = pd.read_csv(file_csv, encoding="utf-8")
print(df)

#Inspect 
missing_count = df.isna().sum().sum()
duplicate_count = df.duplicated().sum()

#remove duplicates (clean)
clean_df = df.drop_duplicates()

#save cleaned
clean_df.to_csv(f"cleaned_{file_csv}", index=False)


print("Value missing:", missing_count)
print("Values duplicate:", duplicate_count)



# 5. Save report
with open("report.txt", "w", encoding="utf-8") as f:
    f.write("CSV Health Report\n")
    f.write("-----------------\n")
    f.write(f"Total rows (original): {len(df)}\n")
    f.write(f"Total rows (cleaned): {len(clean_df)}\n")
    f.write(f"Missing values found: {missing_count}\n")
    f.write(f"Duplicate rows removed: {duplicate_count}\n")


print(f"Done. cleaned_{file_csv} and report.txt created.")