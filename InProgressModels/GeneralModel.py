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

# This method takes all the parameters and outputs the ones which are not equal to zero.
def calculate_missing_parameter(params, target_parameter):
    for key in params:
        if params[key] == '?':
            target_parameter = key
            if target_parameter == 'quant':
                params[target_parameter] = params['x1'] * params['price'] ** -params['elas']
            elif target_parameter == 'price':
                params[target_parameter] = (params['quant'] / params['x1']) ** (-1 / params['elas'])
            elif target_parameter == 'elas':
                params[target_parameter] = -math.log(params['quant'] / params['x1']) / math.log(params['price'])
            elif target_parameter == 'x1':
                params[target_parameter] = params['quant'] / (params['price'] ** -params['elas'])
            return params[target_parameter]

target_parameter = 'elas'  # Replace with the parameter you want to calculate
calculate_missing_parameter(params, target_parameter)
print(f'{target_parameter}: {round(params[target_parameter], 2)}')

# Solve equation for demand
a = params['quant'] / (params['price'] ** -params['elas'])

# Define the isoelastic demand function
def isoelastic_demand(p, a, elas):
    return a * p ** (-elas)

# Calculate demand quantity for the given price
q_demand = isoelastic_demand(params['price'], a, params['elas'])

# Generate a range of p values (price values)
p_values = np.linspace(500, 1000, 100)

# Calculate corresponding q values (quantity values) using the isoelastic demand function
q_demand_values = isoelastic_demand(p_values, a, params['elas'])

# Define the vertical supply function (supply curve coming from x-axis)
def vertical_supply(p):
    return params['quant']

# Calculate supply quantity for the given price
q_supply = vertical_supply(params['price'])

# Generate a vertical supply curve (constant quantity)
q_supply_values = [vertical_supply(p) for p in p_values]

# Plot the isoelastic demand and vertical supply curves
plt.plot(q_demand_values, p_values, label='Isoelastic Demand Curve', color='r')
plt.axvline(x=params['quant'], color='g', linestyle='--', label=f'Supply Curve')
plt.scatter(params['quant'], params['price'], color='b', label=f'Point of equilibrium: (q={round(params["quant"])}, p={round(params["price"])})')
plt.xlabel('Quantity (q)')
plt.ylabel('Price £ (p)')
plt.title('Isoelastic Demand and Supply Curves')
plt.legend()
plt.grid(True)
plt.show()
