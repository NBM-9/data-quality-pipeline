import requests
import pandas as pd
import sqlite3

# STEP 1: Get data from API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

# STEP 2: Convert to table
df = pd.json_normalize(data)

print("Original Data Preview:")
print(df.head())

# STEP 3: Data Quality Checks

print("\n--- DATA QUALITY REPORT ---")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicates:")
print(df.duplicated().sum())

# STEP 4: CLEAN DATA (basic cleanup)
df = df.drop_duplicates()

# STEP 5: CONNECT TO DATABASE
conn = sqlite3.connect("users.db")

# STEP 6: LOAD DATA INTO DATABASE
df.to_sql("users", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("\n✅ Data loaded successfully into SQLite database (users.db)")