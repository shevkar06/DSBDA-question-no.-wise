import pandas as pd

# Load dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv')

# a. Remove duplicate records and display summary
df = df.drop_duplicates()
print("a. Shape after removing duplicates:", df.shape)
print("\nConcise summary:")
print(df.info())

# b. Subset with selected columns (first 10 records)
subset_b = df[['Price', 'Age', 'FuelType']].head(10)
print("\nb. Subset of Price, Age, FuelType (first 10 rows):")
print(subset_b)

# c. Transpose of the subset
print("\nc. Transpose of subset:")
print(subset_b.T)

print(df['HP'].dtype)
print(df['HP'].head())
df['HP'] = pd.to_numeric(df['HP'], errors='coerce')  # This will turn invalid entries into NaN


# d. Mean-max normalization on HP column
df['HP_Normalized'] = (df['HP'] - df['HP'].min()) / (df['HP'].max() - df['HP'].min())
print("\nd. Mean-max normalization of HP (first 5):")
print(df[['HP', 'HP_Normalized']].head())