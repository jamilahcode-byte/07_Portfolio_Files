#import module 
import pandas as pd

#ask user file csv
file_csv = input("Enter file need read & copy: ").strip()

#Read & display csv
df = pd.read_csv(file_csv, encoding="utf-8")
print(df)

# Save as new file 

df.to_csv(f"copy_{file_csv}", index=False)
print(f"File saved as copy_{file_csv}")