import pandas as pd

# Load dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv')

# a. Add 'Revised' column with 5% increase in Price
df['Revised'] = df['Price'] * 1.05
print("a. 'Revised' column added.")

# b. Subset: Price > 15000 and Age < 8
subset_24b = df[(df['Price'] > 15000) & (df['Age'] < 8)]
print("\nb. Subset with Price > 15000 and Age < 8:")
print(subset_24b[['Price', 'Age']].head())

# c. Sort by Revised Price in descending order
sorted_subset = subset_24b.sort_values(by='Revised', ascending=False)
print("\nc. Sorted by Revised Price:")
print(sorted_subset[['Price', 'Age', 'Revised']].head())

# Step 1: Inspect unique values in 'HP' column to check for non-numeric data
print("\nUnique values in 'HP' column before cleaning:")
print(df['HP'].unique())

# Step 2: Convert 'HP' column to numeric, coercing errors to NaN
df['HP'] = pd.to_numeric(df['HP'], errors='coerce')

# Step 3: Handle NaN values by replacing them with the mean of the 'HP' column
df['HP'] = df['HP'].fillna(df['HP'].mean())  # Replace NaN with mean of 'HP'

# d. Z-score normalization on HP
df['HP_Zscore'] = (df['HP'] - df['HP'].mean()) / df['HP'].std()
print("\nd. Z-score normalization on HP:")
print(df[['HP', 'HP_Zscore']].head())