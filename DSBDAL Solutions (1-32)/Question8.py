import pandas as pd
import numpy as np

# Load datasets
patients_df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\patients.csv')
visits_df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\visits.csv')

print("Initial patients data:")
print(patients_df.head())

print("\nInitial visits data:")
print(visits_df.head())

# a. Fill/drop missing diagnosis codes and ages
visits_df = visits_df.dropna(subset=['Diagnosis'])  # Drop rows with missing diagnosis
print("\nVisits data after dropping rows with missing Diagnosis:")
print(visits_df.head())

patients_df['Age'] = pd.to_numeric(patients_df['Age'], errors='coerce')
patients_df['Age'] = patients_df['Age'].fillna(patients_df['Age'].median())  # Fill missing age
print("\nPatients data after handling missing Age values:")
print(patients_df.head())

# b. Standardize gender values
def standardize_gender(val):
    val = str(val).strip().lower()
    if val in ['m', 'male']:
        return 'Male'
    elif val in ['f', 'female']:
        return 'Female'
    else:
        return 'Other'

patients_df['Gender'] = patients_df['Gender'].apply(standardize_gender)
print("\nPatients data after standardizing Gender values:")
print(patients_df.head())

# c. Merge patient info with visits (join on PatientID)
merged_df = pd.merge(visits_df, patients_df, left_on='PatientID', right_on='PatientID', how='inner')
print("\nMerged DataFrame:")
print(merged_df.head())

# d. Group to get total visits and unique diagnoses per patient
agg_df = merged_df.groupby('PatientID').agg(
    total_visits=('VisitID', 'count'),
    unique_diagnoses=('Diagnosis', pd.Series.nunique)
).reset_index()
print("\nAggregated visits data:")
print(agg_df.head())

# e. Correct out-of-range ages (e.g., age > 120 → set as NaN or drop)
patients_df.loc[patients_df['Age'] > 120, 'Age'] = np.nan
patients_df['Age'] = patients_df['Age'].fillna(patients_df['Age'].median())
print("\nPatients data after correcting out-of-range Age values:")
print(patients_df.head())

# Final output
print("\nFinal cleaned patient data:")
print(patients_df.head())

print("\nFinal aggregated visits data:")
print(agg_df.head())