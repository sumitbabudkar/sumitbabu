This project analyzes global AI, Machine Learning, and Data Science salaries using real-world data.
It combines SQL, Python, Machine Learning, and Tableau to uncover salary trends by experience level, job role, remote work ratio, and country, and also builds a salary prediction model.

# Objectives

Analyze salary trends across AI/ML roles globally

Understand the impact of experience level and remote work on salary

Identify top-paying job roles

Compare salaries across countries

Build a machine learning model to predict salary

Present insights using an interactive Tableau dashboard

#Tech Stack

Database: MySQL

Programming: Python

Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn

Visualization: Tableau

ML Model: Linear RegressionData Source

Salary data stored in MySQL (salary_project database)

Table: salary_data

Key columns:

experience_level

job_title

salary_in_usd

remote_ratio

company_location

company_size

# Data Cleaning & Preparation

Removed missing and duplicate values

Standardized categorical fields

Removed invalid salary values

Selected relevant features for analysis and modeling

# Exploratory Data Analysis (EDA)
1. Salary vs Experience Level

Salaries increase significantly from Entry (EN) to Executive (EX) level

2. Remote Ratio vs Salary

Fully remote, hybrid, and onsite roles show comparable average salaries

Indicates remote work does not reduce compensation

3. Top Paying Roles

Head of Data

AI Engineer

Research Scientist

ML Engineer

4. Salary by Country

Higher average salaries observed in:

USA

Canada

Australia

Western Europe

# Machine Learning Model

Model Used: Linear Regression

Features:

Experience Level

Job Title

Remote Ratio

Company Size

Target: Salary in USD

# Model Evaluation

R² Score used to measure performance

MAE used to measure prediction error

The model provides a baseline salary prediction and highlights which features most influence compensation.

# Tableau Dashboard

The interactive dashboard includes:

Salary vs Experience Level

Remote Ratio vs Salary

Top Paying Job Roles
