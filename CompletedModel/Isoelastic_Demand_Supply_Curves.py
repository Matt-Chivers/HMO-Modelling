import numpy as np
import matplotlib.pyplot as plt
import math

# Define a function to represent isoelastic demand, which depends on price (p), a constant (a), and elasticity (elas)
def isoelastic_demand(p, a, elas):
    return a * p ** (-elas)

# Define a function for vertical supply, which is independent of price and constant at a given quantity (quant)
def vertical_supply(p, quant):
    return quant

# Function to calculate and return the 'x1' parameter, derived from quantity, price, and elasticity in the given params dictionary
def calculate_x1(params):
    params['x1'] = params['quant'] / (params['price'] ** -params['elas'])
    return params['x1']

# Set initial parameters representing some economic scenario
original_params = {
    'quant': 6894,     # 2022 quantity 
    'price': 992.67,     # 2022 price according to Ayton House
    'elas': 0.67,      # Assumed elasticity
    'x1': None         # Scalar value
}

# Update the original parameters with the calculated 'x1' value
original_params['x1'] = calculate_x1(original_params)

# Dictionary to hold student number data for different years
students_not_in_halls_number = {
    '2018': 8983 - 3912,
    '2019': 9227 - 4052,
    '2020': 10120 - 3739,
    '2021': 10426 - 4184,
    '2022': 10468 - 4167,
}

# Function to simulate the effect of a demand shock, adjusting the parameters accordingly
def counterfactual_demand_shock(params, students_not_in_halls_number):
    demand_shock = students_not_in_halls_number['2022'] / students_not_in_halls_number['2018']
    a = params['x1']
    a *= demand_shock
    new_equilibrium_price = (params['quant'] / a) ** (-1 / params['elas'])
    return new_equilibrium_price, a

# Calculate new equilibrium price and adjusted constant 'a' after demand shock
new_equilibrium_price, new_a = counterfactual_demand_shock(original_params, students_not_in_halls_number)

# Update parameters with new equilibrium price
params = original_params.copy()
params['price'] = new_equilibrium_price
params['x1'] = params['quant'] / (params['price'] ** -params['elas'])

# Modify quantity to reflect a counterfactual scenario
params['quant'] = 6924 # According to Fife Council we have lost 122 HMO licenses since 2018
params['price'] = (params['quant'] / params['x1']) ** (-1 / params['elas'])

# Check that the calculated price matches an expected value
assert round(params['price']) == 806, f"Expected price to be approximately £920, but got £{params['price']}"

# Calculate 'a' for original and updated parameters
original_a = original_params['quant'] / (original_params['price'] ** -original_params['elas'])
updated_a = params['quant'] / (params['price'] ** -params['elas'])

# Generate a range of price values for plotting
p_values = np.linspace(0, 2000, 100)

# Compute the demand quantities for original and updated scenarios across different prices
q_demand_values_original = [isoelastic_demand(p, original_a, original_params['elas']) for p in p_values]
q_demand_values_updated = [isoelastic_demand(p, updated_a, params['elas']) for p in p_values]

# Begin plotting the demand and supply curves
plt.figure(figsize=(10, 6))

# Plot the 2022 demand curve and mark the equilibrium point
plt.plot(q_demand_values_original, p_values, label='2022 Demand Curve', color='blue')
plt.axvline(x=original_params['quant'], color='blue', linestyle='--', label='2022 Supply Curve')
plt.scatter(original_params['quant'], original_params['price'], color='blue', label=f'2022 Equilibrium: (q={round(original_params["quant"])}, p={round(original_params["price"])})')

# Plot the 2018 demand curve and mark the new equilibrium point
plt.plot(q_demand_values_updated, p_values, label='2018 Demand Curve', color='red')
plt.axvline(x=params['quant'], color='red', linestyle='--', label='2018 Supply Curve')
plt.scatter(params['quant'], params['price'], color='red', label=f'2018 Equilibrium: (q={round(params["quant"])}, p={round(params["price"])})')

# Setting labels, title, and grid for the plot
plt.xlabel('Quantity (q)')
plt.ylabel('Price £ (p)')
plt.title('Isoelastic Demand and Supply Curves: Original vs Counterfactual')
plt.legend()
plt.grid(True)
plt.xlim(0, 10000)

# Finalize and display the plot
plt.tight_layout()
plt.show()
