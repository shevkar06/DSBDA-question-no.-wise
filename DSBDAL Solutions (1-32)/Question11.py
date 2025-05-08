import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Titanic-Dataset.csv')
print("Dataset loaded successfully.\n")

# a. Handle missing Age and Cabin values
df['Age'] = df['Age'].fillna(df['Age'].median())
print("Missing 'Age' values filled with median:\n", df['Age'].head())

df['Cabin'] = df['Cabin'].fillna('Unknown')
print("\nMissing 'Cabin' values filled with 'Unknown':\n", df['Cabin'].head())

# b. Convert Sex and Embarked columns into numeric form using encoding
label_encoder = LabelEncoder()

df['Sex'] = label_encoder.fit_transform(df['Sex'])
print("\nEncoded 'Sex' column (Male=0, Female=1):\n", df['Sex'].head())

df['Embarked'] = df['Embarked'].fillna('S')  # Fill missing with most common
df['Embarked'] = label_encoder.fit_transform(df['Embarked'])
print("\nEncoded 'Embarked' column (C=0, Q=1, S=2):\n", df['Embarked'].head())

# c. Create a new feature FamilySize = SibSp + Parch
df['FamilySize'] = df['SibSp'] + df['Parch']
print("\nCreated 'FamilySize' feature:\n", df[['SibSp', 'Parch', 'FamilySize']].head())

# d. Bin Fare into price categories
bins = [0, 10, 50, 100, np.inf]
labels = ['Low', 'Medium', 'High', 'Very High']
df['FareCategory'] = pd.cut(df['Fare'], bins=bins, labels=labels, right=False)
print("\nBinned 'Fare' into categories:\n", df[['Fare', 'FareCategory']].head())

# Final output
print("\nCleaned and processed Titanic dataset:")
print(df[['Age', 'Cabin', 'Sex', 'Embarked', 'FamilySize', 'FareCategory']].head())