import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv')

# Optional cleanup: remove missing or duplicate values for better plotting
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Scatter Plot – Car Price by Age
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Age', y='Price')
plt.title("Scatter Plot: Car Price by Age")
plt.xlabel("Age (Years)")
plt.ylabel("Price")
plt.grid(True)
plt.show()

# Histogram – KM
plt.figure(figsize=(8,5))
sns.histplot(df['KM'], bins=30, kde=True)
plt.title("Histogram: Kilometers Driven")
plt.xlabel("KM")
plt.ylabel("Frequency")
plt.show()

# Bar Plot – FuelType Count
plt.figure(figsize=(6,4))
sns.countplot(x='FuelType', data=df)
plt.title("Fuel Type Distribution")
plt.xlabel("Fuel Type")
plt.ylabel("Count")
plt.show()
