# -*- coding: utf-8 -*-
"""
Created on Thu May  8 00:24:09 2025

@author: Gaurav
"""
import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\Gaurav\Desktop\DataSet for Exam\Salaries.csv")

# -------------------------------
# 29. Conditional data queries
# -------------------------------

# a. Get the rank and salary of all staff that does not belong to discipline A
query_29a = df[df['discipline'] != 'A'][['rank', 'salary']]
print("29a. Staff not in discipline A (rank and salary):")
print(query_29a.head(), "\n")

# b. Get rank, salary, and years of service of all male staff and only female professors
query_29b = df[((df['sex'] == 'Male') | ((df['sex'] == 'Female') & (df['rank'] == 'Prof')))][['rank', 'salary', 'service']]
print("29b. Male staff and only female professors (rank, salary, service):")
print(query_29b.head(), "\n")

# c. Get all Female staff who are either professor or earning more than 75000
query_29c = df[(df['sex'] == 'Female') & ((df['rank'] == 'Prof') | (df['salary'] > 75000))]
print("29c. Female professors or salary > 75000:")
print(query_29c.head(), "\n")

# d. Get the rank and salary of all staff other than professors and who are serving from at least 10 years
query_29d = df[(df['rank'] != 'Prof') & (df['service'] >= 10)][['rank', 'salary']]
print("29d. Non-professors with at least 10 years of service (rank and salary):")
print(query_29d.head(), "\n")
