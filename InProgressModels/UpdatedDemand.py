import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import math

# Define a dictionary to hold the initial parameter values
params = {
    'quant': 6802,
    'price': 744,
    'elas': 0.67,
    'x1': '?',
}

studentNumber = {
    '2010': 7730 - 3649 ,
    '2011': 7775 - 3836,
    '2012': 7582 - 3518,
    '2013': 7860 - 3722,
    '2014': 8206 - 3574,
    '2015': 8420 - 3752,
    '2016': 8786 - 3783,
    '2017': 9140 - 3798, 
    '2018': 8983 - 3912,
    '2019': 9227 - 4052,
    '2020': 10120 - 3739,
    '2021': 10426 - 4184,
    '2022': 10468 - 4167,
    '2023': 10234,
} 

# Extracting years and numbers for analysis
years = list(map(int, studentNumber.keys()))
numbers = list(studentNumber.values())

# Remove the 2023 data for fitting
years_for_fitting = years[:-1]
numbers_for_fitting = numbers[:-1]

# Linear regression
slope, intercept, r_value, p_value, std_err = linregress(years_for_fitting, numbers_for_fitting)

# Predicted value for 2023
predicted_2023 = slope * 2023 + intercept

# Plotting the data and the line of best fit
plt.figure(figsize=(10, 6))
plt.plot(years_for_fitting, numbers_for_fitting, 'o', label='Actual Data')
plt.plot(years, [slope * x + intercept for x in years], 'r', label='Line of Best Fit')

# Highlighting the predicted 2023 value
plt.plot(2023, predicted_2023, 'go', label='Predicted 2023 Value')

plt.xlabel('Year')
plt.ylabel('Number of Students')
plt.title('Student Numbers Over Years with Linear Regression')
plt.legend()
plt.grid(True)
plt.show()

print('Predicted 2023 student number: ' + str(predicted_2023))

# Determining the coefficient 'a' using the 2010 value from studentNumber
# We assume that the 2010 student number is the demand at the original price level
demand_2010 = studentNumber['2010']
price = params['price']  # Original price
elas = params['elas']   # Elasticity

# Calculating 'a'
a = demand_2010 / (price ** -elas)

print('Value of a: ' + str(a))

# This method takes all the parameters and calculates the missing one.
def calculate_missing_parameter(params, target_parameter):
    if params[target_parameter] != '?':
        return params[target_parameter]
    elif target_parameter == 'quant':
        params[target_parameter] = params['x1'] * params['price'] ** -params['elas']
    elif target_parameter == 'price':
        params[target_parameter] = (params['quant'] / params['x1']) ** (-1 / params['elas'])
    elif target_parameter == 'elas':
        params[target_parameter] = -math.log(params['quant'] / params['x1']) / math.log(params['price'])
    elif target_parameter == 'x1':
        params[target_parameter] = params['quant'] / (params['price'] ** -params['elas'])
    return params[target_parameter]

target_parameter = 'x1'  # Replace with the parameter you want to calculate
calculated_value = calculate_missing_parameter(params, target_parameter)
print(f'{target_parameter}: {round(calculated_value, 2)}')

# Define the isoelastic demand function
def isoelastic_demand(p, a, elas):
    q = a * p ** (-elas)
    return q

# Calculate demand quantity for the given price
a = params['quant'] / (params['price'] ** -params['elas'])
p_values = np.linspace(0, 1000, 100)
q_demand_values = [isoelastic_demand(p, a, params['elas']) for p in p_values]

# Define the vertical supply function (supply curve coming from the x-axis)
def vertical_supply(p):
    return params['quant']

# Calculate supply quantity for the given price
q_supply = vertical_supply(params['price'])
q_supply_values = [vertical_supply(p) for p in p_values]

# Plot the isoelastic demand and vertical supply curves
plt.figure(figsize=(12, 6))

# Plot the first graph (original data)
plt.subplot(1, 2, 1)
plt.plot(q_demand_values, p_values, label='Isoelastic Demand Curve', color='r')
plt.axvline(x=params['quant'], color='g', linestyle='--', label=f'Supply Curve')
plt.scatter(params['quant'], params['price'], color='b', label=f'Point of equilibrium: (q={round(params["quant"])}, p={round(params["price"])})')
plt.xlabel('Quantity (q)')
plt.ylabel('Price £ (p)')
plt.title('Isoelastic Demand and Supply Curves')
plt.legend()
plt.grid(True)
plt.xlim(0, 10000)

# Define Counterfactual method
def counterfactual(params):
    counterfactual_parameter = input("Counterfactual: What parameter would you like to change? (quant, price, elas, x1): ")
    counterfactual_percent = float(input("By what percentage would you like to change it? If you do not want to add a change, type 0: "))

    if counterfactual_parameter == 'quant':
        params['quant'] *= (1 + (counterfactual_percent / 100))
        # Recalculate 'price' while keeping elasticity constant
        params['price'] = (params['quant'] / params['x1']) ** (-1 / params['elas'])
    elif counterfactual_parameter == 'price':
        params['price'] *= (1 + (counterfactual_percent / 100))
    elif counterfactual_parameter == 'elas':
        params['elas'] *= (1 + (counterfactual_percent / 100))
    elif counterfactual_parameter == 'x1':
        params['x1'] *= (1 + (counterfactual_percent / 100))
        # Recalculate 'price' to maintain consistency
        params['price'] = (params['quant'] / params['x1']) ** (-1 / params['elas'])
    return params

# Apply counterfactual to the parameters
params = counterfactual(params)
print("Updated Parameters:", params)

# Calculate demand quantity for the given price with updated parameters
a = params['quant'] / (params['price'] ** -params['elas'])
p_values = np.linspace(0, 1000, 100)  # Updated range for p_values
q_demand_values = [isoelastic_demand(p, a, params['elas']) for p in p_values]

# Plot the second graph (data after counterfactual changes)
plt.subplot(1, 2, 2)
plt.plot(q_demand_values, p_values, label='Isoelastic Demand Curve', color='r')
plt.axvline(x=params['quant'], color='g', linestyle='--', label=f'Supply Curve')
plt.scatter(params['quant'], params['price'], color='b', label=f'Point of equilibrium: (q={round(params["quant"])}, p={round(params["price"])})')
plt.xlabel('Quantity (q)')
plt.ylabel('Price £ (p)')
plt.title('Counterfactual Isoelastic Demand and Supply Curves')
plt.legend()
plt.grid(True)
plt.xlim(0, 10000)
plt.tight_layout()
plt.show()
