import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load dataset
df = pd.read_csv(r"C:\Users\Gaurav\Desktop\DataSet for Exam\Iris.csv")

# a. Insert intentional duplicates and missing values
df.loc[0] = df.loc[1]  # Intentional duplicate
df.loc[2, 'PetalLengthCm'] = None  # Insert missing value
df.loc[3, 'SepalWidthCm'] = None

# Check for duplicates
print("a. Duplicated rows:")
print(df[df.duplicated()])

# Remove duplicates
df = df.drop_duplicates()

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Handle missing values by filling with column mean
df['PetalLengthCm'].fillna(df['PetalLengthCm'].mean(), inplace=True)
df['SepalWidthCm'].fillna(df['SepalWidthCm'].mean(), inplace=True)

# b. Combine with external species characteristics table
species_info = pd.DataFrame({
    'Species': ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],
    'Color': ['Blue', 'Yellow', 'Purple'],
    'BloomingTime': ['Spring', 'Summer', 'Autumn']
})
df = pd.merge(df, species_info, on='Species', how='left')

print("\nb. Combined with species characteristics:")
print(df[['Species', 'Color', 'BloomingTime']].drop_duplicates())

# c. Normalize petal/sepal measurements using MinMaxScaler
scaler = MinMaxScaler()
columns_to_normalize = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

print("\nc. Normalized measurements:")
print(df[columns_to_normalize].head())

# d. Add size_ratio = petal_length / sepal_length
df['size_ratio'] = df['PetalLengthCm'] / df['SepalLengthCm']
print("\nd. Added size_ratio column:")
print(df[['PetalLengthCm', 'SepalLengthCm', 'size_ratio']].head())