import pandas as pd

# Load datasets
info_df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\student_info.csv')
scores_df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\student_scores.csv')

# a. Clean datasets (handle missing values, strip whitespace, fix types)
info_df = info_df.dropna().copy()
scores_df = scores_df.dropna().copy()

# Trim spaces in column names and string fields
info_df.columns = info_df.columns.str.strip()
scores_df.columns = scores_df.columns.str.strip()
info_df['Name'] = info_df['Name'].str.strip()
scores_df['Name'] = scores_df['Name'].str.strip()

# b. Remove invalid scores (e.g., Science = -1)
scores_df = scores_df[scores_df['Science'] >= 0]
print("b. Cleaned scores dataset without invalid Science scores:")
print(scores_df.head())

# c. Convert Grade to string format like "Grade 10"
info_df['Grade'] = info_df['Grade'].apply(lambda x: f"Grade {int(x)}")
print("\nc. Updated Grade format:")
print(info_df[['StudentID', 'Grade']].head())

# d. Perform inner join on StudentID to find common students
merged = pd.merge(info_df, scores_df, on='StudentID', how='inner')
print("\nd. Students present in both datasets:")
print(merged[['StudentID', 'Name_x', 'Grade', 'Math', 'Science', 'English']])

# e. Identify mismatches: students in scores_df not in info_df
unmatched = scores_df[~scores_df['StudentID'].isin(info_df['StudentID'])]
print("\ne. Students in scores but missing in info:")
print(unmatched)
