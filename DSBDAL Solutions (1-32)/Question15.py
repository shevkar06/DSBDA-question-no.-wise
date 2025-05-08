import pandas as pd
import numpy as np

# Load main dataset
df = pd.read_csv(r"C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv")

### a. DATA CLEANING ###
print("Missing values before cleaning:\n", df.isnull().sum())

# Replace junk values with NaN
junk_values = ["", " ", "NA", "n/a", "--", "?", "null", "NaN"]
df.replace(junk_values, np.nan, inplace=True)

# Drop rows with too many missing values (optional)
df.dropna(thresh=df.shape[1] - 2, inplace=True)

# Fill missing values using forward fill
df.fillna(method='ffill', inplace=True)

print("\nMissing values after cleaning:\n", df.isnull().sum())


### b. DATA INTEGRATION ###
# Assume another dataset exists: Toyota_Extra.csv with additional data (e.g., mileage info)
try:
    df_extra = pd.read_csv("Toyota_Extra.csv")  # External dataset
    df = pd.merge(df, df_extra, on='Model', how='left')
    print("\nData merged successfully. Shape after integration:", df.shape)
except FileNotFoundError:
    print("\nToyota_Extra.csv not found. Skipping integration step.")


### c. DATA TRANSFORMATION ###
# Convert Age from months to years
df['Age_Years'] = (df['Age'] / 12).round(1)

# Normalize Price column
df['Price_Norm'] = (df['Price'] - df['Price'].min()) / (df['Price'].max() - df['Price'].min())

# Encode FuelType as numeric codes
df['FuelType_Code'] = df['FuelType'].astype('category').cat.codes

print("\nData after transformation:\n", df[['Age', 'Age_Years', 'Price', 'Price_Norm', 'FuelType', 'FuelType_Code']].head())


### d. ERROR CORRECTING ###
# Fix negative or zero prices/ages
df.loc[df['Price'] <= 0, 'Price'] = np.nan
df.loc[df['Age'] < 0, 'Age'] = np.nan

# Strip extra spaces from object columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

# Correct spelling errors in FuelType
df['FuelType'] = df['FuelType'].replace({'Petorl': 'Petrol', 'Diesel ': 'Diesel', 'CNG': 'CNG'})

print("\nData after error correction:\n", df.head())
