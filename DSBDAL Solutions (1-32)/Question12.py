import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\StudentsPerformance.csv')
print("Dataset loaded successfully.\n")

# a. Check for and impute any missing test scores
missing_values = df[['math score', 'reading score', 'writing score']].isnull().sum()
print("Missing values in each test score column:\n", missing_values)

df['math score'] = df['math score'].fillna(df['math score'].median())
df['reading score'] = df['reading score'].fillna(df['reading score'].median())
df['writing score'] = df['writing score'].fillna(df['writing score'].median())
print("\nMissing values imputed with median.\n")

# b. Create an overall AverageScore column
df['AverageScore'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
print("Calculated 'AverageScore':\n", df[['math score', 'reading score', 'writing score', 'AverageScore']].head())

# c. Bucket students into performance bands
def performance_band(score):
    if score >= 85:
        return 'Excellent'
    elif score >= 60:
        return 'Average'
    else:
        return 'Poor'

df['PerformanceBand'] = df['AverageScore'].apply(performance_band)
print("\nAssigned performance bands:\n", df[['AverageScore', 'PerformanceBand']].head())

# d. Check for duplicate and inconsistent records
duplicates = df[df.duplicated()]
if not duplicates.empty:
    print("\nDuplicate student records found:\n", duplicates)
else:
    print("\nNo duplicate records found.")

inconsistent_data = df[(df['math score'] < 0) | (df['reading score'] < 0) | (df['writing score'] < 0)]
if not inconsistent_data.empty:
    print("\nInconsistent data (negative scores):\n", inconsistent_data)
else:
    print("\nNo inconsistent data found.")

# e. Encode gender, lunch, and test preparation course
label_encoder = LabelEncoder()

df['gender'] = label_encoder.fit_transform(df['gender'])
df['lunch'] = label_encoder.fit_transform(df['lunch'])
df['test preparation course'] = label_encoder.fit_transform(df['test preparation course'])

print("\nEncoded 'gender', 'lunch', and 'test preparation course':\n", df[['gender', 'lunch', 'test preparation course']].head())

# Final output
print("\nCleaned and processed student performance data:")
print(df.head())