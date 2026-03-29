
#Step1 import module 
import pandas as pd 

#Create function clean contact 
def clean_contacts(input_file,  output_file):
    df = pd.read_csv(input_file )
    df = df.drop_duplicates()
    df["email"] = df["email"].fillna("no_email@example.com")
    df.to_csv(output_file, index=False)
    print("Clean done.")
    print(df)

clean_contacts("dirty_contacts.csv", "cleaned_dirty_contacts.csv")