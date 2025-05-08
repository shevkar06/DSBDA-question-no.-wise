import pandas as pd

# Load the airquality dataset (it comes built-in with pandas)
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\airquality.csv')

# a. Read dataset and display summary
print("Dataset Summary:")
print(df.describe())  # Summary statistics
print("\nDataset Info:")
print(df.info())  # Information about columns, types, and missing data
print("\nFirst few rows of the dataset:")
print(df.head())  # Show the first few rows

# b. Create data subsets having observations in the range 11 to 49 and another subset having temperature value less than 60
subset_range_11_to_49 = df[(df.index >= 11) & (df.index <= 49)]
subset_temp_less_60 = df[df['Temp'] < 60]

print("\nSubset 11 to 49:")
print(subset_range_11_to_49.head())

print("\nSubset Temp < 60:")
print(subset_temp_less_60.head())

# c. Merge observations of any two subsets
merged_subset = pd.concat([subset_range_11_to_49, subset_temp_less_60], ignore_index=True)

print("\nMerged Subset:")
print(merged_subset.head())

# d. Apply Sort Data on Temp values (assuming 'Temperature' is a column)
sorted_df = df.sort_values(by='Temp')

print("\nSorted Dataset based on Temp:")
print(sorted_df.head())
