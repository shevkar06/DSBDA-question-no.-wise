import pandas as pd
import numpy as np

# Load datasets
info_df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\employee_info.csv')
perf_df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\performance.csv')


print("Datasets loaded successfully.\n")

# a. Clean invalid ages, join dates, and department names
info_df['Age'] = pd.to_numeric(info_df['Age'], errors='coerce')
info_df['Age'] = info_df['Age'].apply(lambda x: np.nan if x < 16 or x > 100 else x)
info_df['Age'] = info_df['Age'].fillna(info_df['Age'].median())
print("Cleaned ages:\n", info_df['Age'].head())

info_df['JoinDate'] = pd.to_datetime(info_df['JoinDate'], errors='coerce')
info_df = info_df.dropna(subset=['JoinDate'])
print("\nValid join dates:\n", info_df['JoinDate'].head())

info_df['Department'] = info_df['Department'].str.strip().str.title()
print("\nFormatted department names:\n", info_df['Department'].unique())

# b. Combine datasets using EmployeeID
combined_df = pd.merge(info_df, perf_df, on='EmployeeID', how='inner')
print("\nCombined dataset after merge:\n", combined_df.head())

# c. Create performance average score
score_cols = ['ReviewScore1', 'ReviewScore2']
combined_df[score_cols] = combined_df[score_cols].apply(pd.to_numeric, errors='coerce')
combined_df['PerformanceAvg'] = combined_df[score_cols].mean(axis=1)
print("\nPerformance average calculated:\n", combined_df[['ReviewScore1', 'ReviewScore2', 'PerformanceAvg']].head())

# d. Bucket performance into categories
def categorize_perf(score):
    if score < 60:
        return 'Low'
    elif score < 85:
        return 'Medium'
    else:
        return 'High'

combined_df['PerformanceCategory'] = combined_df['PerformanceAvg'].apply(categorize_perf)
print("\nPerformance categories assigned:\n", combined_df[['PerformanceAvg', 'PerformanceCategory']].head())

# e. Correct blank or mismatched department entries
dept_map = {
    '': np.nan, 'Hr': 'HR', 'Hr Dept': 'HR', 'Human Resources': 'HR',
    'It': 'IT', 'It Dept': 'IT', 'Tech': 'IT',
    'Finance Dept': 'Finance'
}
combined_df['Department'] = combined_df['Department'].replace(dept_map)
combined_df['Department'] = combined_df['Department'].fillna('Unknown')
print("\nCleaned department values:\n", combined_df['Department'].unique())

# Output
print("\nCleaned and processed employee data with performance:")
print(combined_df[['EmployeeID', 'Age', 'Department', 'PerformanceAvg', 'PerformanceCategory']].head())