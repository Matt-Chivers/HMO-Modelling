import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define a dictionary to hold the initial parameter values
params = {
    'elas': 0.67,
    'x1': 3,
}

# Define the student population dictionary
student_population = {
    '2018/19': 8984,
    '2019/20': 9224,
    '2020/21': 10119,
    '2021/22': 10425,
    '2022/23': 8619,  # Updated population for 2022/23
}

# Define the student population dictionary
HMO_provision = {
    '2018/19': 13036,
    '2019/20': 12953,
    '2020/21': 10415,
    '2021/22': 8619,
    '2022/23': 6802,  # !!!used to calibrate x1
}

# Create an empty list to store the price values
price_values = []

# Iterate over the keys (academic years) in the dictionary and calculate price
for academic_year, population in student_population.items():
    # Get the quant value from the HMO_provision dictionary based on the academic year
    quant = HMO_provision.get(academic_year, 0)  # Use 0 as a default value if the academic year is not found
    if population == 0:
        # Handle the case where population is 0 (or None) by skipping the calculation
        continue
    price = (quant / (params['x1'] * population)) ** (-1 / params['elas'])
    price_values.append(price)  # Append the calculated price to the list
    print(f"{academic_year}: {price}")
    print(f"{quant}")

print(price_values)

# Must have 5 data points in each array
# Data set 1
x1_data = np.array([2018, 2019, 2020, 2021, 2022])
y1_data = np.array(price_values[:len(x1_data)])  # Use the first 5 elements of price_values for y1_data

# Define the model function
def model_f(x, a, b, c):
    return a * (x - b) ** 2 + c

# Create a custom range of x-values with no interval
x1_custom = np.arange(min(x1_data), max(x1_data) + 1)

# Fit the model to data set 1 with initial guesses and a different optimization method
initial_guess = (1.0, 2019.0, 3000.0)  # Adjust these initial values as needed
popt1, pcov1 = curve_fit(model_f, x1_data, y1_data, p0=initial_guess)
a_opt1, b_opt1, c_opt1 = popt1
x1_model = np.linspace(min(x1_custom), max(x1_custom), 100)
y1_model = model_f(x1_model, a_opt1, b_opt1, c_opt1)

# Create a subplot with 1 row and 1 column
fig, axs = plt.subplots(1, 1, figsize=(8, 4))

# Plot data set 1 on the subplot
axs.scatter(x1_data, y1_data, label='Data Set 1')
axs.plot(x1_model, y1_model, label='Model 1', color='r')
axs.set_title('Time-Series 1')
axs.set_xlabel('Time')
axs.set_ylabel('Point of Equilibrium')

# Set custom x-axis ticks and labels for the subplot
axs.set_xticks(x1_custom)
axs.set_xticklabels(x1_custom)

# Add a legend
axs.legend()

# Show the plot
plt.show()
