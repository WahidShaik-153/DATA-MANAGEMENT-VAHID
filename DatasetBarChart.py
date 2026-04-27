import pandas as pd
import matplotlib.pyplot as plt

# ---- Load data from file path ----
file_path = "D:\REYAZUL_DMV_LAB\calories.csv.xlsx"  # change to your file path
data = pd.read_csv("D:\REYAZUL_DMV_LAB\calories.csv.xlsx")

# Example CSV structure:
# Category,Value1,Value2

# ---- Extract columns ----
categories = data['Category']
values1 = data['Value1']
values2 = data['Value2']

# ---- Create 2-grid bar charts ----
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# First bar chart
axes[0].bar(categories, values1, color='skyblue')
axes[0].set_title("Bar Chart 1")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Value1")
axes[0].tick_params(axis='x', rotation=45)

# Second bar chart
axes[1].bar(categories, values2, color='salmon')
axes[1].set_title("Bar Chart 2")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Value2")
axes[1].tick_params(axis='x', rotation=45)

# ---- Adjust layout ----
plt.tight_layout()

# ---- Show plot ----
plt.show()