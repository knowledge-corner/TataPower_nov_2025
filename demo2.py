import numpy as np
import pandas as pd

df = pd.read_csv(r"employees.csv")

# Ex. Display names of all employees
print(df["Name"])

# Ex. Display names and salaries of all employees
print(df[["Name", "Salary"]])

# Ex. Display average age of employees
print(df["Age"].mean())

# Sort the dataframe by Salary in descending order
df.sort_values(by="Salary", ascending=False, inplace=True)
print(df.head())

# Extract all managers from the df
print(df[df["Designation"] == "Manager"])

# Extract all female employees from the dataframe
print(df[df["Gender"] == "Female"])

# Extract all employees above 35 yrs of age
result = df[df["Age"] >= 35]
print(result)
print(result.shape)

# Extract employees in the age group of 35-45 years
print(df[df["Age"].between(35, 45)])

# Extract employees who are Manager, Team Lead and Senior Manager
print(df[df["Designation"].isin(["Manager", "Team Lead", "Senior Manager"])])

# Save above data of Manager, Team Lead and Senior Manager in a csv file
result = df[df["Designation"].isin(["Manager", "Team Lead", "Senior Manager"])]
result.to_csv("managers.csv", index=False)

# Extract all employees who name start with J
result_df = df[df["Name"].str.startswith("J")]
print(result_df) 

# What is average salary of Managers?
result_df = df[df["Designation"] == "Manager"]
print(result_df["Salary"].mean())

# Find all the designation
print(df["Designation"].unique())

# Replcae all the occurences of Team Head with Team Lead

# Are there any Team Leads who own a car