Corrected version:
“Give Step 0 to Step 20 for Excel mastery.”


---

Below is a complete, professional Excel (XLS/XLSX) cleaning & handling system.
This is the best possible order, used in real paid Excel cleaning jobs.
CSV rules are integrated where needed.


---

STEP 0 — IMPORT EVERYTHING

import pandas as pd
import numpy as np
import re

Foundation. Never skip.


---

STEP 1 — IDENTIFY FILE & SHEETS

xls = pd.ExcelFile("data.xlsx")
print(xls.sheet_names)

Know what you are dealing with.


---

STEP 2 — READ EXCEL FILE

df = pd.read_excel("data.xlsx", sheet_name=0)

Supports multiple sheets.


---

STEP 3 — READ MULTIPLE SHEETS (IF NEEDED)

dfs = pd.read_excel("data.xlsx", sheet_name=None)

For reports, exports, CRM files.


---

STEP 4 — INSPECT DATA

df.head()
df.info()

Detect types, nulls, broken columns.


---

STEP 5 — STANDARDIZE COLUMN NAMES

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

Professional standard.


---

STEP 6 — REMOVE EMPTY ROWS & COLUMNS

df = df.dropna(how="all")
df = df.dropna(axis=1, how="all")

Excel often has junk space.


---

STEP 7 — TRIM ALL TEXT CELLS

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

Fix copy-paste issues.


---

STEP 8 — NORMALIZE TEXT CASE

df["email"] = df["email"].str.lower()
df["name"] = df["name"].str.title()

Consistency matters.


---

STEP 9 — REMOVE DUPLICATES

df = df.drop_duplicates()
# or
df = df.drop_duplicates(subset=["email"])

Critical for CRM, sales, contacts.


---

STEP 10 — HANDLE MISSING VALUES (SMART)

df = df.dropna(subset=["email"])
df["phone"] = df["phone"].fillna("N/A")

Rule:
Critical → drop
Optional → fill


---

STEP 11 — FIX DATA TYPES

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")

Excel lies about types.


---

STEP 12 — CLEAN NUMBERS & CURRENCY

df["price"] = (
    df["price"]
    .astype(str)
    .str.replace(r"[^\d.]", "", regex=True)
    .astype(float)
)

Common Excel issue.


---

STEP 13 — VALIDATE VALUES

df = df[df["age"] >= 0]
df = df[df["email"].str.contains("@", na=False)]

Clean ≠ valid.


---

STEP 14 — SPLIT / MERGE COLUMNS

df[["first_name", "last_name"]] = df["name"].str.split(" ", 1, expand=True)

Clients love structured data.


---

STEP 15 — HANDLE MULTI-VALUE CELLS

df["tags"] = df["tags"].str.split(",")
df = df.explode("tags")

Marketing & CRM files.


---

STEP 16 — REMOVE INVISIBLE CHARACTERS

df = df.replace(r"[\x00-\x1F\x7F]", "", regex=True)

Excel hidden junk.


---

STEP 17 — SORT & REORDER

df = df.sort_values(by="date")
df = df[["name", "email", "phone", "date"]]

Client-ready layout.


---

STEP 18 — FINAL VALIDATION

df.isna().sum()
df.duplicated().sum()

Never skip.


---

STEP 19 — WRITE CLEAN EXCEL

df.to_excel("clean.xlsx", index=False)

Delivery file.


---

STEP 20 — EXPORT CSV (BONUS)

df.to_csv("clean.csv", index=False)

Extra value for client.


---

Reality

Steps 5–12 = most paid Excel gigs

This works for finance, CRM, reports, scraped Excel

Same system = CSV + Excel mastery


If you want next:

One reusable Excel + CSV master script

Fiverr / Khamsat gig wording using these steps

Phone-only workflow


State which one.