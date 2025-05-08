import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv')

# Clean missing values
df = df.dropna()

# Standardize 'Doors' values
df['Doors'] = df['Doors'].replace({'two': 2, 'three': 3, 'four': 4, 'five': 5}).astype(int)

# One-hot encode 'FuelType'
df = pd.get_dummies(df, columns=['FuelType'], prefix='Fuel')

# 1. Sort observations on Price values in ascending order
sorted_df = df.sort_values(by='Price')
print("1. Sorted observations by Price (ascending):")
print(sorted_df[['Price']].head())

# 2. Create subset by selecting specific columns
subset_columns = df[['Price', 'Age', 'KM', 'Fuel_Petrol']]
print("\n2. Subset with selected columns:")
print(subset_columns.head())

# 3. Create subset by selecting specific rows and columns (first 5 rows)
subset_rows_cols = df.loc[0:4, ['Price', 'Age', 'Fuel_Diesel']]
print("\n3. Subset with selected rows and columns:")
print(subset_rows_cols)

# 4. Create subset where Price > 15000 and Age < 8
subset_price_age = df[(df['Price'] > 15000) & (df['Age'] < 8)]
print("\n4. Cars with Price > 15000 and Age < 8:")
print(subset_price_age[['Price', 'Age']])

# 5. Create subset of cars consuming Petrol
subset_petrol = df[df['Fuel_Petrol'] == 1]
print("\n5. Subset of cars consuming Petrol:")
print(subset_petrol[['Price', 'Fuel_Petrol']].head())

# 6. Apply decimal normalization on Price column
max_price = df['Price'].abs().max()
df['Price_Normalized'] = df['Price'] / (10 ** len(str(int(max_price))))
print("\n6. Price after decimal normalization:")
print(df[['Price', 'Price_Normalized']].head())
