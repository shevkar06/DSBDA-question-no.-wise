import pandas as pd

# Load dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\housing.csv')

# a. Subset where median income > 5 and average rooms < 6
subset = df[(df['median_income'] > 5) & (df['total_rooms'] / df['households'] < 6)]
print("a. Houses with median income > 5 and average rooms < 6:")
print(subset.head())

# b. Merge with a regional lookup table (latitude/longitude → region)
region_lookup = pd.DataFrame({
    'region': ['North', 'South', 'East', 'West'],
    'lat_range': [(35, 40), (32, 35), (33, 36), (34, 38)],
    'lon_range': [(-122, -119), (-121, -118), (-120, -117), (-124, -121)]
})

# Function to assign region
def assign_region(row):
    for _, r in region_lookup.iterrows():
        if r['lat_range'][0] <= row['latitude'] <= r['lat_range'][1] and \
           r['lon_range'][0] <= row['longitude'] <= r['lon_range'][1]:
            return r['region']
    return 'Other'

df['region'] = df.apply(assign_region, axis=1)
print("\nb. Dataset with region assigned:")
print(df[['latitude', 'longitude', 'region']].head())

# c. Sort by median_house_value and population
sorted_df = df.sort_values(by=['median_house_value', 'population'], ascending=[False, False])
print("\nc. Sorted by median_house_value and population (descending):")
print(sorted_df.head())

# d. Transpose statistics summary to compare features
summary = df.describe().transpose()
print("\nd. Transposed summary statistics:")
print(summary)

# e. Reshape: Average house value across income and housing age bins
df['income_bin'] = pd.cut(df['median_income'], bins=[0, 2, 4, 6, 8, 10], labels=['0-2', '2-4', '4-6', '6-8', '8-10'])
df['age_bin'] = pd.cut(df['housing_median_age'], bins=[0, 10, 20, 30, 40, 50, 60], labels=['0-10','10-20','20-30','30-40','40-50','50-60'])

pivot = df.pivot_table(values='median_house_value', index='income_bin', columns='age_bin', aggfunc='mean')
print("\ne. Pivot: Average house value by income and age bins:")
print(pivot)
