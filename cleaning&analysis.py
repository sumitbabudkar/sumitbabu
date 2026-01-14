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

#Data Overview & Structure
df.shape
df.head()
df.info()


2# Handling Missing Values
df.isnull().sum()

df.dropna(inplace=True)

#Removing Duplicate Records
df.drop_duplicates(inplace=True)


#Standardizing Categorical Values
df['experience_level'] = df['experience_level'].str.upper()
df['employment_type'] = df['employment_type'].str.upper()
df['company_size'] = df['company_size'].str.upper()


# Salary Validation & Outlier Check
df = df[df['salary_in_usd'] > 0]

df.describe()



# Feature Selection for Analysis
df_clean = df[[
    'work_year',
    'experience_level',
    'job_title',
    'salary_in_usd',
    'remote_ratio',
    'company_location',
    'company_size'
]]