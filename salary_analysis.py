import pandas as pd
import mysql.connector

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sumit@2026",
    database="salary_project"
)

# Load data
query = "SELECT * FROM salary_data"
df = pd.read_sql(query, conn)

# Basic checks
print(df.head())
print("\nTotal Rows:", df.shape[0])
print("\nColumns:", df.columns)

