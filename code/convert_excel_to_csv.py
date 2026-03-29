import pandas as pd  # Import pandas for Excel/CSV operations

# Path to your Excel file
xlsx_path = "/storage/emulated/0/file_m.csv.xlsx"

# Path where CSV will be saved
csv_path = "/storage/emulated/0/file_m.csv"

# Read the Excel file into a DataFrame
df = pd.read_excel(xlsx_path)

# Convert the DataFrame to CSV (without the index column)
df.to_csv(csv_path, index=False)

print("CSV created successfully")