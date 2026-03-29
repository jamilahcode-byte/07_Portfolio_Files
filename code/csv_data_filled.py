import csv  # Import CSV module to read and write CSV files

# -----------------------------
# Step 1: Read CSV and collect ages
# -----------------------------
rows = []  # Store all rows
ages = []  # Store numeric ages (for calculating average)

with open("data_dirty.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # Read the header row separately
    for row in reader:
        rows.append(row)  # Keep all rows for later writing
        if row[1]:        # If age column is not empty
            ages.append(int(row[1]))  # Convert to int and store

# -----------------------------
# Step 2: Calculate average age
# -----------------------------
avg_age = int(sum(ages) / len(ages))  # Compute average age as integer

# -----------------------------
# Step 3: Fill missing values
# -----------------------------
for row in rows:
    if row[1] == "":              # Missing age
        row[1] = str(avg_age)     # Fill with average age (as string for CSV)
    if row[2] == "":              # Missing email
        row[2] = "unknown@example.com"  # Fill with placeholder email

# -----------------------------
# Step 4: Save cleaned CSV
# -----------------------------
with open("data_filled.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)  # Write header first
    writer.writerows(rows)   # Write all cleaned rows

print("Filled CSV saved as data_filled.csv")