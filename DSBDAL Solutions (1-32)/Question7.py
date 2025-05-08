import pandas as pd
import numpy as np

# Load datasets
info_df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\student_info.csv')
scores_df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\student_scores.csv')

# a. Basic cleaning – strip whitespace and drop fully empty rows
info_df.columns = info_df.columns.str.strip()
scores_df.columns = scores_df.columns.str.strip()
info_df = info_df.dropna(how='all').copy()
scores_df = scores_df.dropna(how='all').copy()

# b. Fill or drop missing values in Age, Email, and History
# Age: fill with median
info_df['Age'] = pd.to_numeric(info_df['Age'], errors='coerce')
info_df['Age'] = info_df['Age'].fillna(info_df['Age'].median())

# Email: drop rows with missing or unrecoverable emails
info_df['Email'] = info_df['Email'].astype(str).replace("nan", np.nan)
info_df = info_df.dropna(subset=['Email'])

# History: fill with average if numerical, else mode (depending on format)
if info_df['History'].dtype in [int, float]:
    info_df['History'] = info_df['History'].fillna(info_df['History'].mean())
else:
    info_df['History'] = info_df['History'].fillna(info_df['History'].mode()[0])

# c. Standardize email addresses
# Fix entries like "eva.email.com" to "eva@email.com"
def fix_email(email):
    if '@' not in email:
        parts = email.split('.')
        if len(parts) >= 2:
            return parts[0] + '@' + parts[1] + '.com'
    return email.strip().lower()

info_df['Email'] = info_df['Email'].apply(fix_email)

# d. Create average score across subjects
scores_df[['Math', 'Science', 'English']] = scores_df[['Math', 'Science', 'English']].apply(pd.to_numeric, errors='coerce')
scores_df['AverageScore'] = scores_df[['Math', 'Science', 'English']].mean(axis=1)

# e. Add HighPerformer column (1 if avg score > 85, else 0)
scores_df['HighPerformer'] = (scores_df['AverageScore'] > 85).astype(int)

# Final cleaned outputs
print("Cleaned student info:")
print(info_df.head())

print("\nScores with average and HighPerformer flag:")
print(scores_df[['StudentID', 'AverageScore', 'HighPerformer']].head())