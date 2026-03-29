import pandas as pd 

def clean_csv(file_input, file_output, report_file):
    df = pd.read_csv(file_input, encoding="utf-8")
    report = {
      "original_rows": len(df),
      "missing_value": df.isna().sum().sum(),
      "duplicate_removed": df.duplicated(),
      "cleaned_rows": len(df) - df.duplicated(),
    }
    
    df = df.drop_duplicates()
    df.to_csv(file_output)
    
    with open(report_file, "w",encoding="utf-8") as file:
        for key, value in report.items():
            file.write(f"{key}: {value}")

            
clean_csv("data_dirty.csv", "cleaned.csv", "report.txt")                                    