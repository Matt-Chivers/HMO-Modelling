import numpy as np
import matplotlib.pyplot as plt
import math

# Define the isoelastic demand function
def isoelastic_demand(p, a, elas):
    return a * p ** (-elas)

# Define the vertical supply function (supply curve coming from the x-axis)
def vertical_supply(p, quant):
    return quant

# This method calculates the missing parameter 'x1'.
def calculate_x1(params):
    params['x1'] = params['quant'] / (params['price'] ** -params['elas'])
    return params['x1']

# Original parameters
original_params = {
    'quant': 6802,     # From FC
    'price': 1145,     # Ayton House
    'elas': 0.67,      # Assumption
    'x1': None
}

# Calculate 'x1' for original_params
original_params['x1'] = calculate_x1(original_params)

# Student number data
studentNumber = {
    '2018': 8983 - 3912,
    '2019': 9227 - 4052,
    '2020': 10120 - 3739,
    '2021': 10426 - 4184,
    '2022': 10468 - 4167,
}

# Apply counterfactual to the parameters based on demand shock
def counterfactual_demand_shock(params, studentNumber):
    demand_shock = studentNumber['2018'] / studentNumber['2022']
    a = params['x1']
    a *= demand_shock
    new_equilibrium_price = (params['quant'] / a) ** (-1 / params['elas'])
    return new_equilibrium_price, a

# Calculate new equilibrium price and a
new_equilibrium_price, new_a = counterfactual_demand_shock(original_params, studentNumber)

# Update parameters with the new equilibrium price
params = original_params.copy()
params['price'] = new_equilibrium_price
params['x1'] = params['quant'] / (params['price'] ** -params['elas'])

# Counterfactual increase in quantity
counterfactual_percent = 1.7935901206
params['quant'] = 6924  # Set the new quantity directly to 6924
params['price'] = (params['quant'] / params['x1']) ** (-1 / params['elas'])

# Ensure that the price is approximately £806 as required
assert round(params['price']) == 806, f"Expected price to be approximately £806, but got £{params['price']}"

# Calculate demand quantity for the given price with original and updated parameters
original_a = original_params['quant'] / (original_params['price'] ** -original_params['elas'])
updated_a = params['quant'] / (params['price'] ** -params['elas'])

p_values = np.linspace(0, 2000, 100)
q_demand_values_original = [isoelastic_demand(p, original_a, original_params['elas']) for p in p_values]
q_demand_values_updated = [isoelastic_demand(p, updated_a, params['elas']) for p in p_values]

# Plotting the combined isoelastic demand and vertical supply curves
plt.figure(figsize=(10, 6))

# Plot original demand curve and equilibrium
plt.plot(q_demand_values_original, p_values, label='2022 Demand Curve', color='blue')
plt.axvline(x=original_params['quant'], color='blue', linestyle='--', label='2022 Supply Curve')
plt.scatter(original_params['quant'], original_params['price'], color='blue', label=f'2022 Equilibrium: (q={round(original_params["quant"])}, p={round(original_params["price"])})')

# Plot updated demand curve and equilibrium
plt.plot(q_demand_values_updated, p_values, label='2018 Demand Curve', color='red')
plt.axvline(x=params['quant'], color='red', linestyle='--', label='2018 Supply Curve')
plt.scatter(params['quant'], params['price'], color='red', label=f'2018 Equilibrium: (q={round(params["quant"])}, p={round(params["price"])})')

plt.xlabel('Quantity (q)')
plt.ylabel('Price £ (p)')
plt.title('Isoelastic Demand and Supply Curves: Original vs Counterfactual')
plt.legend()
plt.grid(True)
plt.xlim(0, 10000)

plt.tight_layout()
plt.show()
