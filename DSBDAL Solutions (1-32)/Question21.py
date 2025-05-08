import pandas as pd
from scipy.stats import zscore

# Load the dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv')

# Remove missing values and duplicates for clean pivoting
df = df.dropna().drop_duplicates()

# a. Get unique values of categorical ‘Doors’
unique_doors = df['Doors'].unique()
print("\na. Unique values in 'Doors':", unique_doors)

# b. Transform all values in same format (ensure all are integers)
df['Doors'] = df['Doors'].replace({'two': 2, 'three': 3, 'four': 4, 'five': 5}).astype(int)
print("\nb. Transformed 'Doors' column:")
print(df['Doors'].value_counts())

# Ensure 'HP' column is numeric
df['HP'] = pd.to_numeric(df['HP'], errors='coerce')

# c. Apply Decimal Scaling Normalization on HP column
max_hp = df['HP'].abs().max()  # Get the maximum absolute value in the 'HP' column
scaling_factor = 10 ** len(str(int(max_hp)))  # Determine the scaling factor
df['HP_Normalized'] = df['HP'] / scaling_factor  # Normalize the 'HP' column
print("\nc. Decimal scaling normalization on HP column:")
print(df[['HP', 'HP_Normalized']].head())