# Import required modules
import pandas as pd
import sqlite3

# (1) Read CSV into DataFrame 
df = pd.read_csv('DATA/cyber_incidents.csv')

# (2) Check Data
# View first 5 rows
print(df.head()) 
# Check data types and missing values
print(df.info()) 
# Check for missing data
print(df.isnull().sum())

# (3) Connect to database
conn = sqlite3.connect('DATA/intelligence_platform.db')
# Bulk insert all rows 
df.to_sql( 'cyber_incidents', conn, if_exists='append', index=False ) 
print("✓ Data loaded successfully")

# (4) Verify data loading
# Count rows in database 
cursor = conn.cursor() 
cursor.execute("SELECT COUNT(*) FROM cyber_incidents")
count = cursor.fetchone()[0] 
print(f"Loaded {count} incidents") # View sample data 
cursor.execute("SELECT * FROM cyber_incidents LIMIT 3") 
for row in cursor.fetchall():
    print(row)
