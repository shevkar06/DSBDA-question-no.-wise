import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv')

# a. Remove missing values
df.dropna(inplace=True)
print("a. After removing missing values:", df.shape)

# b. Data types and numeric summary
print("\nb. Data types:")
print(df.dtypes)
print("\nSummary of numeric variables:")
print(df.describe())

# c. Remove duplicates again just in case
df.drop_duplicates(inplace=True)
print("\nc. Shape after duplicate removal:", df.shape)

# d. Z-score normalization on Price
df['Price_Zscore'] = (df['Price'] - df['Price'].mean()) / df['Price'].std()
print("\nd. Z-score normalization of Price:")
print(df[['Price', 'Price_Zscore']].head())

# e. Pivot table: average price by FuelType and Automatic
pivot_table = df.pivot_table(values='Price', index='FuelType', columns='Automatic', aggfunc='mean')
print("\ne. Pivot table of average Price:")
print(pivot_table)
