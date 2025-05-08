import pandas as pd
from scipy.stats import zscore

# Load the dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv')

# a. Remove all missing values
df_cleaned = df.dropna()
print("a. Data after removing missing values:")
print(df_cleaned.head())

# b. Display datatypes and concise summary of all numeric variables
print("\nb. Data types of columns:")
print(df_cleaned.dtypes)

print("\nSummary of numeric variables:")
print(df_cleaned.describe())

# c. Remove all duplicate records
df_no_duplicates = df_cleaned.drop_duplicates()
print("\nc. Data after removing duplicate records:")
print(df_no_duplicates.head())

# d. Apply Z-score Normalization on Price Column
df_no_duplicates['Price_Zscore'] = zscore(df_no_duplicates['Price'])
print("\nd. Z-score Normalization on Price column:")
print(df_no_duplicates[['Price', 'Price_Zscore']].head())

# e. Shape and Reshape using pivot_table
# Example: average Price by FuelType and number of Doors
df['Doors'] = df['Doors'].replace({'two': 2, 'three': 3, 'four': 4, 'five': 5}).astype(int)
pivot_result = pd.pivot_table(df, values='Price', index='FuelType', columns='Doors', aggfunc='mean')
print("e. Pivot table - Average Price by FuelType and Doors:")
print(pivot_result)
