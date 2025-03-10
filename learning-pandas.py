import pandas as pd
import numpy as np

# Creating a dummy DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 45],
    "Salary": [50000, 60000, 70000, 80000, 90000],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Joining Date": pd.date_range("2020-01-01", periods=5, freq="YE"),
}

df = pd.DataFrame(data)

# Display basic info
print("DataFrame Overview:")
print(df.info())  # Shows structure and data types

print("\n  First 3 Rows:")
print(df.head(3))  # Shows first 3 rows

print("\n  Summary Statistics:")
print(df.describe())  # Shows summary stats for numeric columns

print("\n  Column Names:")
print(df.columns)  # Shows column names

print("\n  Checking for Missing Values:")
print(df.isnull().sum())  # Checks for missing values

# Selecting columns
print("\n  Selecting a Single Column:")
print(df["Name"])

print("\n  Selecting Multiple Columns:")
print(df[["Name", "Salary"]])

# Filtering Data
print("\n  Employees in IT Department:")
print(df[df["Department"] == "IT"])

# Sorting Data
print("\n  Sorting by Salary (Descending Order):")
print(df.sort_values("Salary", ascending=False))

# Grouping Data
print("\n  Average Salary by Department:")
print(df.groupby("Department")["Salary"].mean())

# Adding a new column
df["Experience (Years)"] = [1, 5, 10, 15, 20]
print("\n  DataFrame after Adding Experience Column:")
print(df)

# Applying a function
df["Salary Increment"] = df["Salary"].apply(lambda x: x * 1.10)  # 10% increment
print("\n  Salary Increment Applied:")
print(df)

# Dropping a column
df.drop("Salary Increment", axis=1, inplace=True)
print("\n  After Dropping Salary Increment Column:")
print(df)

# Resetting the index
df.reset_index(drop=True, inplace=True)
print("\n  Reset Index:")
print(df)

# Converting a column to Categorical
df["Department"] = pd.Categorical(df["Department"])
print("\n  Data Types After Categorical Conversion:")
print(df.dtypes)

# Exporting Data
df.to_csv("dummy_data.csv", index=False)
print("\n✅ Data exported to 'dummy_data.csv'")

