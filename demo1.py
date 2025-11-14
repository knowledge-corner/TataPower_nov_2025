# pip install numpy pandas matplotlib seaborn

import numpy as np  # Numeric python library - used for numerical computations
import pandas as pd # Data analysis library - used for data manipulation and analysis
import matplotlib.pyplot as plt # Data visualisation library - used for creating static, animated, and interactive visualizations
#import seaborn as sns # Statistical data visualization library - built on top of matplotlib for making attractive and informative statistical graphics

# Ex. Read data from Employee.csv file
df = pd.read_csv(r"employees.csv")
print(df.head(10))  # Display the first few rows of the dataframe

# Dataframes - are tabular containers storing data in rows and columns. They are labeled container
print(df.shape)
df.columns = ["Name","Salary","Designation","Age","Gender","Car"]
print(df.columns)
print(df.head())

df.to_csv("new_employees.csv", index=False)  # Save dataframe to a new CSV file without the index

df.columns = df.columns.str.lower()  # Convert column names to lowercase