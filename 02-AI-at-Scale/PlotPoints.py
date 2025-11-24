# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 15:37:59 2025

@author: ganq1
"""

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data

x_data = np.array([1, 2, 4])  # Temperature data
y_data = np.array([122.31, 119.54, 109.95])  # Pressure data

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, alpha=0.6, color='blue', s=50)

# Add labels with names and units
plt.xlabel('Number of Tensor', fontsize=12)
plt.ylabel('Running Time (s)', fontsize=12)
plt.title('Run vs TP Number at 8 Layers', fontsize=14, fontweight='bold')

# Add grid for better readability
plt.grid(True, alpha=0.3)




plt.tight_layout()

#Save the plot
plt.savefig('./Assets/TpvsRunTime.svg') 
# Show the plot
plt.show()

