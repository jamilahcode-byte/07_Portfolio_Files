import pandas as pd


def clean_csv(file_path, output_csv, output_excel=None):
    try:
        # Load CSV with encoding fix and skip bad lines
        df = pd.read_csv('data.csv', encoding='utf-8', on_bad_lines='skip')

        # Preview data
        print(df.head())
        # Fix column names
        df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

        # Fill empty cells
        df['email'] = df['email'].fillna('no_email@example.com')

        # Remove rows with all empty cells
        df = df.dropna(how='all')

        # Normalize text
        df['name'] = df['name'].str.strip().str.title()

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Save cleaned CSV
        df.to_csv('cleaned_sample.csv', index=False)

        # Save Excel version
        df.to_excel('cleaned_sample.xlsx', index=False)
    except Exception as error:
        print(f"Error: {error}")
if __name__ == "__main__":
    input_file = 'data.csv'
    clean_csv(input_file, 'cleaned_sample.csv', 'cleaned_sample.xlsx')   