import numpy as np
import pandas as pd

df = pd.read_csv(r"employees.csv")

# Replcae all the occurences of Team Head with Team Lead
df.loc[df["Designation"] == "Team Head", "Designation"] = "Team Lead"
print(df["Designation"].unique())

# Are there any Team Leads who own a car
result_df = df[(df["Designation"] == "Team Lead") & (df["Owns Car"] == "Yes")]
print(result_df)