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


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
sns.boxplot(x='experience_level', y='salary_in_usd', data=df)
plt.title("Salary vs Experience Level")
plt.show()
plt.figure(figsize=(8,5))
sns.barplot(x='remote_ratio', y='salary_in_usd', data=df)
plt.title("Salary vs Remote Ratio")
plt.show()
role_salary = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)

plt.figure(figsize=(10,6))
role_salary.plot(kind='bar')
plt.title("Average Salary by Job Role")
plt.show()
role_salary = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)

plt.figure(figsize=(10,6))
role_salary.plot(kind='bar')
plt.title("Average Salary by Job Role")
plt.ylabel("Salary (USD)")
plt.show()
