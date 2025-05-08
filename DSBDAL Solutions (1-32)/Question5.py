import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv')

# a. Create data subsets
subset_1 = df[['Price', 'Age']]  # Removed 'Model'
subset_2 = df[df['Price'] > 10000]        # subset based on condition
print("Subset 1 (selected columns):\n", subset_1.head())
print("\nSubset 2 (Price > 10000):\n", subset_2.head())

# b. Merge Data (simulate merge using 'FuelType')
df_copy = df[['FuelType', 'HP']].drop_duplicates()
merged_df = pd.merge(subset_1, df_copy, left_index=True, right_index=True, how='inner')
print("\nMerged Data:\n", merged_df.head())

# c. Sort Data on specified column (e.g., 'Price')
sorted_df = df.sort_values(by='Price', ascending=False)
print("\nData sorted by Price (descending):\n", sorted_df[['Price']].head())

# d. Transposing Data
transposed = df.head().T  # Transpose first 5 rows
print("\nTransposed Data:\n", transposed)

# e. Shape and Reshape Data
print("\nOriginal shape:", df.shape)
reshaped = df[['Price', 'Age']].values.reshape(-1, 2)  # Convert to 2-column array
print("Reshaped array (2 columns):\n", reshaped[:5])
