
STEP 1 — LOAD & INSPECT (ALWAYS FIRST)

import pandas as pd
df = pd.read_csv("data.csv")
df.head()
df.info()

Why: Identify types, nulls, encoding issues, column names.


---

STEP 2 — HANDLE ENCODING SAFELY

df = pd.read_csv("data.csv", encoding="utf-8", errors="ignore")

Why: Client files are often broken or mixed-encoded.


---

STEP 3 — STANDARDIZE COLUMN NAMES

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

Why: Everything else depends on clean column names.


---

STEP 4 — REMOVE EMPTY ROWS & COLUMNS

df = df.dropna(how="all")
df = df.dropna(axis=1, how="all")

Why: Garbage rows/columns inflate file size and errors.


---

STEP 5 — TRIM & NORMALIZE TEXT

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

Why: Fix spaces, hidden characters, copy-paste issues.


---

STEP 6 — FIX TEXT CASE (WHERE NEEDED)

df["name"] = df["name"].str.title()
df["email"] = df["email"].str.lower()

Why: Consistency = professional output.


---

STEP 7 — REMOVE DUPLICATES (SMART)

df = df.drop_duplicates()
# or
df = df.drop_duplicates(subset=["email"])

Why: Duplicate data breaks analysis and CRMs.


---

STEP 8 — HANDLE MISSING VALUES (STRATEGY)

df = df.dropna(subset=["email"])   # critical
df["phone"] = df["phone"].fillna("N/A")  # optional

Rule:
Critical → drop
Optional → fill


---

STEP 9 — FIX DATA TYPES

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")

Why: Numbers and dates must be real, not text.


---

STEP 10 — REMOVE INVALID VALUES

df = df[df["age"] >= 0]
df = df[df["email"].str.contains("@", na=False)]

Why: Clean ≠ just non-empty.


---

STEP 11 — NORMALIZE FORMATS

df["phone"] = df["phone"].str.replace(r"\D", "", regex=True)

Why: One format per column. No exceptions.


---

STEP 12 — HANDLE OUTLIERS (BASIC)

df = df[df["salary"] < df["salary"].quantile(0.99)]

Why: Extreme values destroy averages and charts.


---

STEP 13 — VALIDATE FINAL DATA

df.isna().sum()
df.duplicated().sum()

Why: Never deliver unchecked files.


---

STEP 14 — SORT & REORDER COLUMNS

df = df.sort_values(by="date")
df = df[["name", "email", "phone", "date"]]

Why: Client-friendly layout.


---

STEP 15 — EXPORT CLEAN FILE

df.to_csv("clean_data.csv", index=False)

Why: Final, delivery-ready asset.


---

Reality Check

Steps 3–10 = 80–90% of paid gigs
Corrected version:
“Other steps, including importing everything.”


STEP 0 — IMPORT EVERYTHING (ALWAYS FIRST)

import pandas as pd
import numpy as np
import re

Optional (only when needed):

from pathlib import Path

Why: No missing tools mid-cleaning.


---

STEP 16 — REMOVE INVISIBLE / BROKEN CHARACTERS

df = df.replace(r"[\x00-\x1F\x7F]", "", regex=True)

Why: Fix copy-paste, WhatsApp, Excel junk characters.


---

STEP 17 — FIX MIXED SEPARATORS (CSV DAMAGE)

df = pd.read_csv("data.csv", sep=None, engine="python")

Why: Some files mix , ; | \t.


---

STEP 18 — SPLIT / MERGE COLUMNS

df[["first_name", "last_name"]] = df["name"].str.split(" ", 1, expand=True)

Why: Clients want structured data.


---

STEP 19 — REMOVE TEST / FAKE DATA

df = df[~df["email"].str.contains("test|fake|example", na=False)]

Why: Common in scraped or demo datasets.


---

STEP 20 — DEDUPE FUZZY TEXT (ADVANCED)

df["name"] = df["name"].str.lower().str.replace(r"[^a-z ]", "", regex=True)
df = df.drop_duplicates(subset=["name"])

Why: Same value, different formatting.


---

STEP 21 — HANDLE MULTI-VALUE CELLS

df["tags"] = df["tags"].str.split(",")
df = df.explode("tags")

Why: CRM & marketing files often bundle values.


---

STEP 22 — REPLACE BAD PLACEHOLDERS

df = df.replace(["-", "--", "?", "none", "null"], np.nan)

Why: Fake nulls break analysis.


---

STEP 23 — FINAL SANITY CHECK

assert df.shape[0] > 0
assert df.shape[1] > 0

Why: Prevent empty deliveries.


---

STEP 24 — SAVE MULTIPLE FORMATS (PRO)

df.to_csv("clean_data.csv", index=False)
df.to_excel("clean_data.xlsx", index=False)

Why: Clients love options.


---

STEP 25 — LOG WHAT YOU DID (CLIENT TRUST)

with open("cleaning_log.txt", "w") as f:
    f.write("Duplicates removed, nulls handled, text normalized.")

Why: Increases reviews + repeat clients.


---

Bottom line

Step 0 + 1–15 → standard gigs

Steps 16–25 → advanced, higher-paying jobs

This is a full professional CSV-cleaning system


If you want next:

One reusable master script

Fiverr gig checklist mapped to these steps

Phone-only workflow


State which one.