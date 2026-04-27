import numpy as np 
import matplotlib.pyplot as plt

# Sample data
data = [12, 15, 14, 16, 18, 19, 20, 22, 24, 25, 18, 17, 16, 15, 14]

# Create histogram
plt.hist(data, bins=5, edgecolor='black')

# Labels and title
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram Example")

# Show grid (optional)
plt.grid(axis='y')

# Display the histogram
plt.show()