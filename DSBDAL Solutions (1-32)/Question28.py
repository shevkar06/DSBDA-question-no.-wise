# -*- coding: utf-8 -*-
"""
Created on Thu May  8 00:21:17 2025

@author: Gaurav
"""
import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\Gaurav\Desktop\DataSet for Exam\Salaries.csv")

# -------------------------------
# 28. Perform the following operations
# -------------------------------

# a. Create data subsets
subset1 = df[['rank', 'salary']]
subset2 = df[df['discipline'] == 'A']
print("28a. Subset1 (rank and salary):")
print(subset1.head(), "\n")

# b. Merge Data
merged_df = pd.merge(subset1, subset2, on='rank', suffixes=('_sub1', '_sub2'))
print("28b. Merged Data:")
print(merged_df.head(), "\n")

# c. Sort Data by salary in descending order
sorted_df = df.sort_values(by='salary', ascending=False)
print("28c. Sorted Data by salary:")
print(sorted_df.head(), "\n")

# d. Transpose first 5 rows
transposed_df = df.head().T
print("28d. Transposed Data (first 5 rows):")
print(transposed_df, "\n")

# e. Shape and reshape Data
original_shape = df.shape
reshaped_salary = df['salary'].values.reshape(-1, 1)  # reshape to 2D array
print("28e. Original shape:", original_shape)
print("28e. Reshaped salary column shape:", reshaped_salary.shape, "\n")
