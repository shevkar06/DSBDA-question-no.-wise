import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\heart.csv')
print("Dataset loaded successfully.\n")

# a. Fill missing values in cholesterol, restecg, and thal columns
df['chol'] = df['chol'].fillna(df['chol'].median())
df['restecg'] = df['restecg'].fillna(df['restecg'].mode()[0])
df['thal'] = df['thal'].fillna(df['thal'].mode()[0])
print("Missing values filled:\n", df[['chol', 'restecg', 'thal']].isnull().sum())

# b. Encode categorical columns like sex, cp, thal using One-Hot Encoding
df = pd.get_dummies(df, columns=['sex', 'cp', 'thal'], drop_first=True)
print("\nApplied One-Hot Encoding. Columns now include:\n", df.columns.tolist())

# c. Create an AgeGroup column
def age_group(age):
    if age < 35:
        return 'Young'
    elif age < 55:
        return 'Middle-aged'
    else:
        return 'Elderly'

df['AgeGroup'] = df['age'].apply(age_group)
print("\nAge groups assigned:\n", df[['age', 'AgeGroup']].head())

# Convert AgeGroup to categorical codes
df['AgeGroup'] = df['AgeGroup'].map({'Young': 0, 'Middle-aged': 1, 'Elderly': 2})
print("\nConverted 'AgeGroup' to numeric codes:\n", df['AgeGroup'].value_counts())

# d. Normalize features like chol, thalach, and oldpeak
scaler = StandardScaler()
df[['chol', 'thalach', 'oldpeak']] = scaler.fit_transform(df[['chol', 'thalach', 'oldpeak']])
print("\nNormalized 'chol', 'thalach', and 'oldpeak':\n", df[['chol', 'thalach', 'oldpeak']].head())

# e. Build a classification model
X = df.drop('target', axis=1)
y = df['target']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("\nTraining and test data split:")
print("Training samples:", X_train.shape[0])
print("Test samples:", X_test.shape[0])

# Random Forest pipeline
model = Pipeline([
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train the model
model.fit(X_train, y_train)
print("\nModel training completed.")

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))