import numpy as np
import matplotlib.pyplot as plt
import math

# Define a dictionary to hold the initial parameter values
params = {
    'quant': 6802,
    'price': 700,
    'elas': '?',
    'x1': 1284443.7,
}

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

target_parameter = 'elas'  # Replace with the parameter you want to calculate
calculated_value = calculate_missing_parameter(params, target_parameter)
print(f'{target_parameter}: {round(calculated_value, 2)}')

# Define the isoelastic demand function
def isoelastic_demand(p, a, elas):
    q = a * p ** (-elas)
    return q

# Calculate demand quantity for the given price
a = params['quant'] / (params['price'] ** -params['elas'])
p_values = np.linspace(500, 1000, 100)
q_demand_values = [isoelastic_demand(p, a, params['elas']) for p in p_values]

# Define the vertical supply function (supply curve coming from x-axis)
def vertical_supply(p):
    return params['quant']

# Calculate supply quantity for the given price
q_supply = vertical_supply(params['price'])
q_supply_values = [vertical_supply(p) for p in p_values]

# Plot the isoelastic demand and vertical supply curves
plt.figure(figsize=(8, 6))
plt.plot(q_demand_values, p_values, label='Isoelastic Demand Curve', color='r')
plt.axvline(x=params['quant'], color='g', linestyle='--', label=f'Supply Curve')
plt.scatter(params['quant'], params['price'], color='b', label=f'Point of equilibrium: (q={round(params["quant"])}, p={round(params["price"])})')
plt.xlabel('Quantity (q)')
plt.ylabel('Price £ (p)')
plt.title('Isoelastic Demand and Supply Curves')
plt.legend()
plt.grid(True)
plt.show()

# Define Counterfactual method
def counterfactual(params):
    counterfactual_parameter = input("Counterfactual: What parameter would you like to increase / decrease? (quant, price, elas, x1): ")
    counterfactual_percent = float(input("By what percentage would you like to change it? If you do not want to add a change, type 0: "))

    if counterfactual_parameter == 'quant':
        params['quant'] *= (1 + (counterfactual_percent / 100))
    elif counterfactual_parameter == 'price':
        params['price'] *= (1 + (counterfactual_percent / 100))
    elif counterfactual_parameter == 'elas':
        params['elas'] *= (1 + (counterfactual_percent / 100))
    elif counterfactual_parameter == 'x1':
        params['x1'] *= (1 + (counterfactual_percent / 100))
    return params

# Apply counterfactual to the parameters
params = counterfactual(params)
print("Updated Parameters:", params)
