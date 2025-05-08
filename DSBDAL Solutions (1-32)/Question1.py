import pandas as pd

# Load the dataset

df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Iris.csv')

# a. Subset rows where petal length > 1.5 and species is "setosa"
subset = df[(df['PetalLengthCm'] > 1.5) & (df['Species'] == 'Iris-setosa')]
print("a. Subset where PetalLengthCm > 1.5 and Species == 'Iris-setosa':")
print(subset)

# b. Merge with custom species info table (e.g., color or habitat)
species_info = pd.DataFrame({
    'Species': ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],
    'Color': ['White', 'Purple', 'Blue'],
    'Habitat': ['Meadow', 'Swamp', 'Forest']
})

merged = pd.merge(df, species_info, on='Species')
print("\nb. Merged dataset with species info:")
print(merged.head())

# c. Sort by sepal_width and then by sepal_length
sorted_df = df.sort_values(by=['SepalWidthCm', 'SepalLengthCm'])
print("\nc. Sorted by SepalWidthCm and SepalLengthCm:")
print(sorted_df.head())

# d. Transpose first 5 rows
transposed = df.head().transpose()
print("\nd. Transposed first 5 rows:")
print(transposed)

# e. Reshape with melt() and pivot()
# Melt into long format
melted = pd.melt(df, id_vars=['Id', 'Species'], 
                 value_vars=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'],
                 var_name='Feature', value_name='Value')
print("\ne.1 Melted format:")
print(melted.head())

# Pivot back into wide format
pivoted = melted.pivot_table(index=['Id', 'Species'], columns='Feature', values='Value').reset_index()
print("\ne.2 Pivoted back to wide format:")
print(pivoted.head())
