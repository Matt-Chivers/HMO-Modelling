# Install package
import numpy as np
import matplotlib.pyplot as plt
import math

# Define a dictionary to hold the initial parameter values
params = {
    'quant': 1,
    'price': 0,
    'e': 1,
    'a': 3,
}

# This method takes all the parameters and outputs the ones wich are not equal to zero.
def calculate_missing_parameter(params, target_parameter):
     for key in params:
        if params[key] == 0:
            target_parameter = key  
            if target_parameter == 'quant':
                params[target_parameter] = params['a'] * params['price'] ** -params['elas']
            elif target_parameter == 'price':
                params[target_parameter] = (params['quant'] / params['a']) ** (-1 / params['elas'])
            elif target_parameter == 'e':
                params[target_parameter] = -math.log(params['quant']/ params['a'], params['price'])
            elif target_parameter == 'a':
                params[target_parameter] = params['quant'] / (params['price'] ** -params['elas'] )    
            return params[target_parameter]
            
print(calculate_missing_parameter(params, target_parameter))


# Solve equation for demand
a = 'quant' / ('price'**(-'elas'))

# Define the isoelastic demand function
def isoelastic_demand(p):
    return a * p**(-'elas')

# Calculate demand quantity for the given price
q_demand = isoelastic_demand('price')

# Generate a range of p values (price values)
p_values = np.linspace(500, 1000, 100)

# Calculate corresponding q values (quantity values) using the isoelastic demand function
q_demand_values = isoelastic_demand(p_values)

# Define the vertical supply function (supply curve coming from x-axis)
def vertical_supply(p):
    return 'quant'

# Calculate supply quantity for the given price
q_supply = vertical_supply('price')

# Generate a vertical supply curve (constant quantity)
q_supply_values = [vertical_supply(p) for p in p_values]

# Plot the isoelastic demand and vertical supply curves
plt.plot(q_demand_values, p_values, label='Isoelastic Demand Curve', color='r')
plt.axvline(x='quant', color='g', linestyle='--', label=f'Supply Curve')  
plt.scatter(params['quant'], params['price'], color='b', label=f'Point of equilibrium: (q={params['quant']}, p={params['price']})')
plt.xlabel('Quantity (q)')
plt.ylabel('Price £ (p)')
plt.title('Isoelastic Demand and Supply Curves')
plt.legend()
plt.grid(True)
plt.show()
