import matplotlib.pyplot as plt
import numpy as np
import pandas as pd   

file_path = r"D:\REYAZUL_DMV_LAB\reyazuldataset.xlsx"


data = pd.read_excel(file_path)

labels = data['Category']
sizes = data['Values']

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title("Pie Chart")
plt.axis('equal')

plt.show()