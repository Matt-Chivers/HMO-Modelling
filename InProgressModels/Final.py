import numpy as np
import matplotlib.pyplot as plt
import math

# Define a dictionary to hold the initial parameter values for the first part
params = {
    'quant': 6802,
    'price': 1145,
    'elas': 0.67,
    'x1': None
}

# Student number data
studentNumber = {
    '2018': 8983 - 3912,
    '2019': 9227 - 4052,
    '2020': 10120 - 3739,
    '2021': 10426 - 4184,
    '2022': 10468 - 4167,
}

# Define the isoelastic demand function
def isoelastic_demand(p, a, elas):
    return a * p ** (-elas)

# Define the vertical supply function (supply curve coming from the x-axis)
def vertical_supply(p):
    return params['quant']

# This method calculates the missing parameter 'x1'.
def calculate_x1(params):
    params['x1'] = params['quant'] / (params['price'] ** -params['elas'])
    return params['x1']

# Calculate 'x1'
params['x1'] = calculate_x1(params)

# Apply counterfactual to the parameters based on demand shock
def counterfactual_demand_shock(params, studentNumber):
    demand_shock = studentNumber['2018'] / studentNumber['2022']
    a = params['x1']
    a *= demand_shock
    new_equilibrium_price = (params['quant'] / a) ** (-1 / params['elas'])
    return new_equilibrium_price, a

# Calculate new equilibrium price and a
new_equilibrium_price, new_a = counterfactual_demand_shock(params, studentNumber)

# Update parameters for the second part
params['price'] = new_equilibrium_price  # Update price with the new equilibrium price
params['x1'] = params['quant'] / (params['price'] ** -params['elas'])  # Recalculate x1 with the new price

# Define Counterfactual method
def counterfactual(params):
    # Dummy implementation for the counterfactual, replace with your logic
    # Normally, you would take user input here, but for simplicity, let's just apply a 10% increase in quantity
    counterfactual_parameter = 'quant'
    counterfactual_percent = 1.7935901206

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

# Calculate demand quantity for the given price with updated parameters
a = params['quant'] / (params['price'] ** -params['elas'])
p_values = np.linspace(0, 2000, 100)  # Updated range for p_values
q_demand_values = [isoelastic_demand(p, a, params['elas']) for p in p_values]

# Define the supply curve
q_supply_values = [vertical_supply(p) for p in p_values]

# Plotting the isoelastic demand and vertical supply curves
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

# Plot the second graph (data after counterfactual changes)
plt.subplot(1, 2, 2)
plt.plot(q_demand_values, p_values, label='Isoelastic Demand Curve (Post Counterfactual)', color='r')
plt.axvline(x=params['quant'], color='g', linestyle='--', label=f'Supply Curve (Post Counterfactual)')
plt.scatter(params['quant'], params['price'], color='b', label=f'Point of equilibrium: (q={round(params["quant"])}, p={round(params["price"])})')
plt.xlabel('Quantity (q)')
plt.ylabel('Price £ (p)')
plt.title('Counterfactual Isoelastic Demand and Supply Curves')
plt.legend()
plt.grid(True)
plt.xlim(0, 10000)

plt.tight_layout()
plt.show()
