import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:\Users\Gaurav\Desktop\DataSet for Exam\Toyota.csv')

# Optional cleanup: remove missing or duplicate values for better plotting
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# a. Age vs Price – Scatter Plot (seaborn)
sns.scatterplot(data=df, x='Age', y='Price', hue='FuelType')
plt.title("Age vs Price by Fuel Type")
plt.show()

# b. Histogram – KM (seaborn)
sns.histplot(data=df, x='KM', bins=30, kde=True)
plt.title("Distribution of KM")
plt.show()

# c. Bar Plot – FuelType-wise Car Count
sns.countplot(data=df, x='FuelType', palette='Set2')
plt.title("Fuel Type Car Count")
plt.show()

