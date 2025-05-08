import pandas as pd

# Load dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\WineQT.csv')

# a. Subset wines with quality ≥ 7 and alcohol > 10%
subset = df[(df['quality'] >= 7) & (df['alcohol'] > 10)]
print("a. Wines with quality ≥ 7 and alcohol > 10%:")
print(subset.head())

# b. Merge red and white wine datasets with a new 'type' column
# Assuming two separate CSVs: red_wine.csv and white_wine.csv (if not, skip this step)
red = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\winequality-red.csv')
red['type'] = 'red'
white = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\winequality-white.csv')
white['type'] = 'white'
combined = pd.concat([red, white], ignore_index=True)
print("\nb. Combined red and white wine datasets:")
print(combined.head())

# c. Sort by citric acid and residual sugar
sorted_df = df.sort_values(by=['citric acid', 'residual sugar'], ascending=[False, False])
print("\nc. Sorted by citric acid and residual sugar:")
print(sorted_df.head())

# d. Transpose summary stats of chemical properties for each quality level
summary_stats = df.groupby('quality').agg({
    'fixed acidity': 'mean',
    'volatile acidity': 'mean',
    'citric acid': 'mean',
    'residual sugar': 'mean',
    'chlorides': 'mean',
    'alcohol': 'mean'
})
transposed = summary_stats.transpose()
print("\nd. Transposed summary statistics by wine quality:")
print(transposed)

# e. Pivot table showing average values of key features by wine quality
pivot = df.pivot_table(values=['alcohol', 'pH', 'density', 'residual sugar'],
                       index='quality',
                       aggfunc='mean')
print("\ne. Pivot table of key features by wine quality:")
print(pivot)
