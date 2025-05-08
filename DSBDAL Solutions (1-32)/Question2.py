import pandas as pd

# Load dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\StudentsPerformance.csv')

# a. Subset where math score > 80 and completed test preparation course
subset = df[(df['math score'] > 80) & (df['test preparation course'] == 'completed')]
print("a. Students with math score > 80 and completed test prep:")
print(subset.head())

# b. Merge with a demographic table (e.g., socioeconomic status)
demographics = pd.DataFrame({
    'parental level of education': [
        'bachelor\'s degree', 'some college', 'master\'s degree',
        'associate\'s degree', 'high school', 'some high school'
    ],
    'socioeconomic status': [
        'high', 'medium', 'high', 'medium', 'low', 'low'
    ]
})

merged = pd.merge(df, demographics, on='parental level of education', how='left')
print("\nb. Merged with socioeconomic status:")
print(merged.head())

# c. Sort by reading score and writing score in descending order
sorted_df = df.sort_values(by=['reading score', 'writing score'], ascending=False)
print("\nc. Sorted by reading and writing score (descending):")
print(sorted_df.head())

# d. Transpose average scores by gender across all subjects
avg_scores = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
transposed_avg = avg_scores.transpose()
print("\nd. Transposed average scores by gender:")
print(transposed_avg)

# e. Pivot table: average scores across lunch type and test preparation course
pivot = df.pivot_table(values=['math score', 'reading score', 'writing score'],
                       index='lunch',
                       columns='test preparation course',
                       aggfunc='mean')
print("\ne. Pivot table comparing lunch vs test prep status:")
print(pivot)
