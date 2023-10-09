import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# Must have 40 data points in each array
# Data set 1
x1_data = np.array([2018, 2019, 2020, 2021, 2022])
y1_data = np.array([3378, 3367, 3011, 2630, 2692])

# Data set 2
x2_data = np.array([2018, 2019, 2020, 2021, 2022])
y2_data = np.array([1, 2, 3, 4, 5])

# Define the model function
def model_f(x, a, b, c):
    return a * (x - b) ** 2 + c

# Create a custom range of x-values with no interval
x1_custom = np.arange(min(x1_data), max(x1_data) + 1)
x2_custom = np.arange(min(x2_data), max(x2_data) + 1)

# Fit the model to data set 1 with initial guesses and a different optimization method
initial_guess = (1.0, 2019.0, 3000.0)  # Adjust these initial values as needed
popt1, pcov1 = curve_fit(model_f, x1_data, y1_data, p0=initial_guess, method='lm')
a_opt1, b_opt1, c_opt1 = popt1
x1_model = np.linspace(min(x1_custom), max(x1_custom), 100)
y1_model = model_f(x1_model, a_opt1, b_opt1, c_opt1)

# Similarly, fit the model to data set 2
initial_guess = (1.0, 2019.0, 3.0)  # Adjust these initial values as needed
popt2, pcov2 = curve_fit(model_f, x2_data, y2_data, p0=initial_guess, method='lm')
a_opt2, b_opt2, c_opt2 = popt2
x2_model = np.linspace(min(x2_custom), max(x2_custom), 100)
y2_model = model_f(x2_model, a_opt2, b_opt2, c_opt2)

# Create a 1x2 grid of subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# Plot data set 1 on the first subplot
axs[0].scatter(x1_data, y1_data, label='Data Set 1')
axs[0].plot(x1_model, y1_model, label='Model 1', color='r')
axs[0].set_title('Data Set 1')
axs[0].set_xlabel('Time')  # Add x-axis label

# Set custom x-axis ticks and labels for the first subplot
axs[0].set_xticks(x1_custom)
axs[0].set_xticklabels(x1_custom)

# Plot data set 2 on the second subplot
axs[1].scatter(x2_data, y2_data, label='Data Set 2')
axs[1].plot(x2_model, y2_model, label='Model 2', color='r')
axs[1].set_title('Data Set 2')
axs[1].set_xlabel('Time')  # Add x-axis label

# Set custom x-axis ticks and labels for the second subplot
axs[1].set_xticks(x2_custom)
axs[1].set_xticklabels(x2_custom)

# Add legends
axs[0].legend()
axs[1].legend()

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()
