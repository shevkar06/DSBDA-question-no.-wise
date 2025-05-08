import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv')

# Optional cleanup: remove missing or duplicate values for better plotting
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Age vs Price – Scatter Plot (matplotlib)
plt.figure(figsize=(8,5))
plt.scatter(df['Age'], df['Price'], color='blue', alpha=0.6)
plt.title("Age vs Price")
plt.xlabel("Age")
plt.ylabel("Price")
plt.grid(True)
plt.show()

# Histogram – KM (matplotlib)
plt.figure(figsize=(8,5))
plt.hist(df['KM'], bins=30, color='orange', edgecolor='black')
plt.title("Histogram of KM")
plt.xlabel("KM")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

#  Bar Plot – FuelType Count (matplotlib)
plt.figure(figsize=(6,4))
fuel_counts = df['FuelType'].value_counts()
plt.bar(fuel_counts.index, fuel_counts.values, color='green')
plt.title("FuelType Count")
plt.xlabel("FuelType")
plt.ylabel("Count")
plt.show()
