import pandas as pd

# Load dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv')


# a. Subset with selected columns
subset_a = df[['Price', 'Age', 'FuelType', 'Automatic']]
print("Subset A - Selected Columns:\n", subset_a.head(), "\n")

# b. Subset of all Petrol vehicles
subset_b = df[df['FuelType'] == 'Petrol']
print("Subset B - Petrol Vehicles:\n", subset_b.head(), "\n")

# c. Subset with Price > 15000 and Age < 8
subset_c = df[(df['Price'] > 15000) & (df['Age'] < 8)]
print("Subset C - Price > 15000 and Age < 8:\n", subset_c.head(), "\n")

# d. Merged subset of b and c (Petrol & Price > 15000 & Age < 8)
merged_subset = pd.merge(subset_b, subset_c, how='inner')
print("Merged Subset (B ∩ C):\n", merged_subset.head(), "\n")