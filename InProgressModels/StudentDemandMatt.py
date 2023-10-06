import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# Must have 40 data points in each array
# Data set 1
x1_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                   18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                   33, 34, 35, 36, 37, 38, 39, 40])
y1_data = np.array([3378, 3367, 3011, 2630, 2692, 3355, 3717, 3767, 3817, 3853, 3863, 3743, 
                   3783, 3788, 3256, 3010, 3104, 3039, 3318, 3201, 3294, 3223, 3235, 3207, 
                   3240, 3271, 3180, 2577, 2501, 2157, 2259, 2015, 2124, 2221, 2380, 2344, 
                   2270, 2056, 1897, 1366])

# Data set 2
x2_data = np.array([1, 2, 3, 4, 4, 4, 4, 5, 6, 8, 9, 10])
y2_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11])

# Define the model function
def model_f(x, a, b, c):
    return a * (x - b) ** 2 + c

# Fit the model to the data set 1
popt1, pcov1 = curve_fit(model_f, x1_data, y1_data)
a_opt1, b_opt1, c_opt1 = popt1
x1_model = np.linspace(min(x1_data), max(x1_data), 100)
y1_model = model_f(x1_model, a_opt1, b_opt1, c_opt1)

# Fit the model to the data set 2
popt2, pcov2 = curve_fit(model_f, x2_data, y2_data)
a_opt2, b_opt2, c_opt2 = popt2
x2_model = np.linspace(min(x2_data), max(x2_data), 100)
y2_model = model_f(x2_model, a_opt2, b_opt2, c_opt2)

# Create a 1x2 grid of subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# Plot data set 1 on the first subplot
axs[0].scatter(x1_data, y1_data)
axs[0].plot(x1_model, y1_model, label='', color='r')
axs[0].set_title('Data Set 1')

# Plot data set 2 on the second subplot
axs[1].scatter(x2_data, y2_data)
axs[1].plot(x2_model, y2_model, label='', color='r')
axs[1].set_title('Data Set 2')

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()