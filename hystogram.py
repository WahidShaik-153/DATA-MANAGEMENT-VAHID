import numpy as np 
import matplotlib.pyplot as plt

data = [12, 15, 14, 16, 18, 19, 20, 22, 24, 25, 18, 17, 16, 15, 14]

plt.hist(data, bins=5, edgecolor='black')

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram Example")

plt.grid(axis='y')

plt.show()
