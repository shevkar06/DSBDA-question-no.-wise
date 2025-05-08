import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Load the airquality dataset (assuming it’s loaded as df)
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\airquality.csv')

# a. Create data subsets selecting specified columns (Ozone, Solar.R, Wind, Temp) and index range (let’s assume we use rows 1 to 50)
subset_columns = df[['Ozone', 'Solar.R', 'Wind', 'Temp']].iloc[1:51]  # Select rows 1 to 50 and specific columns
print("\nSubset with specified columns and index range:")
print(subset_columns.head())

# b. Rationally Replace NaN values
# For numerical columns like Ozone, Solar.R, Wind, Temp, replace NaN with the median value of each column
df['Ozone'] = df['Ozone'].fillna(df['Ozone'].median())
df['Solar.R'] = df['Solar.R'].fillna(df['Solar.R'].median())
df['Wind'] = df['Wind'].fillna(df['Wind'].median())
df['Temp'] = df['Temp'].fillna(df['Temp'].median())

# Verify if any NaN values are left
print("\nMissing values after replacement:")
print(df.isnull().sum())

# c. Data transformation - Apply Min-max Normalization on Solar.R
scaler = MinMaxScaler()
df['Solar.R'] = scaler.fit_transform(df[['Solar.R']])

print("\nData after Min-Max Normalization on Solar.R:")
print(df[['Solar.R']].head())

# d. Plot Month wise Temperature using Matplotlib/Seaborn
# First, ensure the dataset has a 'Month' column. If not, create one based on the row index.
# Assuming that 'Month' column is present or create one for this task.
df['Month'] = df['Month'].fillna(method='ffill')  # Forward fill to handle any missing values for 'Month'

# Plot temperature month-wise using seaborn (Boxplot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Month', y='Temp', data=df)
plt.title('Month-wise Temperature Distribution')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.show()