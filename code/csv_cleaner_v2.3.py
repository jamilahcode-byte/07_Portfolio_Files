import pandas as pd

def clean_contacts(input_file, output_file):
    try:
        df = pd.read_csv(input_file)

        # Basic validation
        if df.empty:
            print("Warning: empty CSV")
            return
        if "email" not in df.columns:
            print("Missing email column")
            return

        print("Processing clean...")

        # Cleaning steps
        df["name"] = df["name"].str.strip()
        df = df.drop_duplicates()
        df["email"] = df["email"].fillna("no_email@example.com")

        # Save cleaned CSV
        df.to_csv(output_file, index=False)
        print(f"CSV cleaned successfully: {output_file}")
        print(f"Rows: {len(df)}")
        
    except FileNotFoundError:
        print("File not found:", input_file)
    except Exception as error:
        print("Error:", error)

# Run the function
clean_contacts("data.csv", "cleaned_data.csv")