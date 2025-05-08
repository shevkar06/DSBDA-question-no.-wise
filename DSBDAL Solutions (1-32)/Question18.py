import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv')

# a. Remove missing values
df_cleaned = df.dropna()
print("a. Data after removing missing values:")
print(df_cleaned.head())

# b. Set Doors value to uniform format (e.g., 'three' -> 3)
df_cleaned['Doors'] = df_cleaned['Doors'].replace({'three': 3, 'four': 4, 'five': 5}).astype(int)
print("\nb. 'Doors' column after standardization:")
print(df_cleaned['Doors'].value_counts())

# c. Provide concise summary of all numeric variables
numeric_summary = df_cleaned.describe()
print("\nc. Summary of numeric variables:")
print(numeric_summary)

# d. Remove all duplicate records
df_no_duplicates = df_cleaned.drop_duplicates()
print("\nd. Data after removing duplicates:")
print(df_no_duplicates.head())

# e. Get dummies for categorical data FuelType (One-hot encoding)
df_encoded = pd.get_dummies(df_no_duplicates, columns=['FuelType'], prefix='Fuel')
print("\ne. One-hot encoded 'FuelType':")
print(df_encoded[['Fuel_CNG', 'Fuel_Diesel', 'Fuel_Petrol']].head())
