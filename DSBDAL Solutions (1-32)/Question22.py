import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv')

# a. Display shape, summary, and count of missing values
print("a. Shape of the dataset:", df.shape)
print("\nSummary of dataset:")
print(df.describe(include='all'))

print("\nCount of missing values in each column:")
print(df.isnull().sum())

# b. Remove duplicate records
df = df.drop_duplicates()
print("\nb. Shape after removing duplicates:", df.shape)

# c. Clean the dataset - Replace missing values with appropriate values
# For numeric columns, fill with mean
# For categorical columns, fill with mode
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        df[col].fillna(df[col].mean(), inplace=True)
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)

print("\nc. Missing values after imputation:")
print(df.isnull().sum())

# d. Convert 'MetColor' and 'Automatic' to object type
df['MetColor'] = df['MetColor'].astype('object')
df['Automatic'] = df['Automatic'].astype('object')

print("\nd. Data types after converting 'MetColor' and 'Automatic':")
print(df.dtypes[['MetColor', 'Automatic']])
