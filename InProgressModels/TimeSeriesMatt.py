import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define a dictionary to hold the initial parameter values
params = {
    'elas': 0.67,
    'x1': 54.77,
}

# Define the student population dictionary
student_population = {
    '2018/19': 8984,
    '2019/20': 9224,
    '2020/21': 10119,
    '2021/22': 10425,
    '2022/23': 10425,  # Updated population for 2022/23
}

# Define the student population dictionary
HMO_provision = {
    '2018/19': 13036,
    '2019/20': 12953,
    '2020/21': 10415,
    '2021/22': 8619,
    '2022/23': 6802, 
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
    price = round((quant / (params['x1'] * population)) ** (-1 / params['elas']), 2)
    price_values.append(price)  # Append the calculated price to the list
    print("Montly rental price for " + f"{academic_year}: £{price}")

# Must have 5 data points in each array
x_data = np.array([2018, 2019, 2020, 2021, 2022])
y_data = np.array(price_values[:len(x_data)])  # Use the first 5 elements of price_values for y_data

# Define the model function
def model_f(x, a, b, c):
    return a * (x - b) ** 2 + c

# Create a custom range of x-values with no interval
x_custom = np.arange(min(x_data), max(x_data) + 1)

# Fit the model to data set 1 with adjusted initial guesses and a different optimization method (lm)
initial_guess = (1.0, 2020.0, 4000.0)  # Adjust these initial values as needed
popt1, pcov1 = curve_fit(model_f, x_data, y_data, p0=initial_guess, method='lm')
a_opt1, b_opt1, c_opt1 = popt1
x_model = np.linspace(min(x_custom), max(x_custom), 100)
y_model = model_f(x_model, a_opt1, b_opt1, c_opt1)

# Create a subplot with 1 row and 1 column
fig, axs = plt.subplots(1, 1, figsize=(8, 4))

# Plot data set 1 on the subplot
axs.scatter(x_data, y_data, label='Data Set')
axs.plot(x_model, y_model, label='Trend', color='r')
axs.set_title('Time-Series Equilibrium Price')
axs.set_xlabel('Time')
axs.set_ylabel('Point of Equilibrium')

# Set custom x-axis ticks and labels for the subplot
axs.set_xticks(x_custom)
axs.set_xticklabels(x_custom)
axs.legend()

# Display the plot
plt.show()
