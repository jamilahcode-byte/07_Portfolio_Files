import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv("leads_advanced.csv")

# Step A: Replace empty strings with NaN
df = df.replace(r"^\s*$", np.nan, regex=True)
# inplace = تطبيق التغيير مباشرة

# Step B: Fill missing emails
df["email_address"] = df["email_address"].fillna("no_email@example.com")

# Fill missing name
df["full_name"] = df["full_name"].fillna("no_name")

# Step C: Forward fill phone numbers if missing
#df["phone_number"] = df.groupby("full_name")["phone_number"].ffill()
df["phone_number"] = df["phone_number"].ffill()
# method="ffill" = ملء للأمام

# Step D: Remove duplicates (full_name + phone_number)
df = df.drop_duplicates(subset=["full_name","phone_number"])

# Step E: Save cleaned CSV
df.to_csv("cleaned_advanced_leads.csv", index=False)