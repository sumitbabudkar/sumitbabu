import pandas as pd
import mysql.connector
from sklearn.preprocessing import LabelEncoder

# -------------------------------
# MySQL connection
# -------------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sumit@2026", 
    database="salary_project"
)

# -------------------------------
# Load data
# -------------------------------
query = "SELECT * FROM salary_data"
df = pd.read_sql(query, conn)

# -------------------------------
# Basic checks
# -------------------------------
print(df.head())
print("\nTotal Rows:", df.shape[0])
print("\nColumns:", df.columns)

# -------------------------------
# Data cleaning (create df_clean)
# -------------------------------
df_clean = df.copy()

df_clean.drop_duplicates(inplace=True)
df_clean = df_clean[df_clean['salary_in_usd'] > 0]

# -------------------------------
# Encoding categorical variables
# -------------------------------
le = LabelEncoder()

df_clean['experience_level'] = le.fit_transform(df_clean['experience_level'])
df_clean['job_title'] = le.fit_transform(df_clean['job_title'])
df_clean['company_location'] = le.fit_transform(df_clean['company_location'])
df_clean['company_size'] = le.fit_transform(df_clean['company_size'])

#Define X (Features) and y (Target)
# -------------------------------
# Prepare ML dataframe
# -------------------------------
ml_df = df_clean.copy()

X = ml_df[['experience_level', 'job_title', 'remote_ratio', 'company_size']]
y = ml_df['salary_in_usd']
#Train–Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#Train the Model (Linear Regression)
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
#Make Predictions
y_pred = model.predict(X_test)


#Model Evaluation
from sklearn.metrics import r2_score, mean_absolute_error

print("R2 Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))


importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
}).sort_values(by='Coefficient', ascending=False)

print(importance)

print("\nData ready for ML")
