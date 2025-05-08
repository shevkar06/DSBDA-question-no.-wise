import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load datasets
applicants_df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\applicants.csv')
scores_df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\exam_scores.csv')
print("Datasets loaded successfully.\n")

# a. Clean inconsistent name formatting & missing test scores
applicants_df['Name'] = applicants_df['Name'].str.strip().str.title()
print("Applicant names formatted:\n", applicants_df['Name'].head())

scores_df = scores_df.dropna(subset=['SAT', 'ACT'])  # Drop rows with missing scores
print("\nScores after dropping missing SAT/ACT values:\n", scores_df.head())

# b. Join on ApplicationID
combined_df = pd.merge(applicants_df, scores_df, on='ApplicationID', how='inner')
print("\nCombined dataset after merge:\n", combined_df.head())

# c. Normalize test scores (0–1 scale)
scaler = MinMaxScaler()
score_cols = ['SAT', 'ACT']
combined_df[score_cols] = scaler.fit_transform(combined_df[score_cols])
print("\nNormalized SAT and ACT scores:\n", combined_df[score_cols].head())

# d. Convert Admission_Status to binary (1 = admitted, 0 = not admitted)
combined_df['Admission_Status'] = combined_df['Admission_Status'].str.lower().map({'admitted': 1, 'not admitted': 0})
print("\nConverted Admission_Status to binary:\n", combined_df['Admission_Status'].head())

# e. Remove duplicate applications and fix invalid test score entries
combined_df = combined_df.drop_duplicates(subset='ApplicationID')
for col in score_cols:
    combined_df = combined_df[(combined_df[col] >= 0) & (combined_df[col] <= 1)]
print("\nDataset after removing duplicates and filtering invalid scores:\n", combined_df.head())

# Final output
print("\nCleaned and processed dataset (final view):")
print(combined_df.head())