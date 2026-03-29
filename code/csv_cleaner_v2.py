
#Step1 import module 
import pandas as pd 

#Create function clean contact 
def clean_contacts(input_file,  output_file):
    
    try:
        df = pd.read_csv(input_file )
        if df.empty:
            print("Warning: empty CSV")
            return

        if "email" not in df.columns:
            print("Missing email column")
            return
            
        print("Processing clean.....")   
            
        df["name"] =  df["name"].str.strip()
        df = df.drop_duplicates()
        df["email"] = df["email"].fillna("no_email@example.com")
        
        
        df.to_csv(output_file, index=False)
        print("CSV cleaned successfully")
            
    except FileNotFoundError:
        print("File not found")
        return    
    except Exception as error:
        print("Error:", error)
 
    

clean_contacts("data.csv", "cleaned_data.csv")