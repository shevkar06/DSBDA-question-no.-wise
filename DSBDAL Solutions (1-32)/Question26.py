import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv')

# a. Sort by Price
sorted_price = df.sort_values(by='Price')
print("a. Sorted by Price (ascending):")
print(sorted_price[['Price']].head())

# b. Subset by selecting specific rows and columns
subset_26b = df.loc[0:10, ['Price', 'Age', 'FuelType']]
print("\nb. Selected rows and columns:")
print(subset_26b)

# c. Subset: Price > 15000 and Age < 8
subset_26c = df[(df['Price'] > 15000) & (df['Age'] < 8)]
print("\nc. Subset Price > 15000 and Age < 8:")
print(subset_26c[['Price', 'Age']].head())

# d. Subset: Cars with FuelType Petrol
subset_26d = df[df['FuelType'] == 'Petrol']
print("\nd. Subset with FuelType as Petrol:")
print(subset_26d[['FuelType']].head())

# e. Decimal normalization on Price
df['Price_DecimalNorm'] = df['Price'] / 10000
print("\ne. Decimal normalization of Price:")
print(df[['Price', 'Price_DecimalNorm']].head())
