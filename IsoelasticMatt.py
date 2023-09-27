import numpy as np
import matplotlib.pyplot as plt

# Hardcoded parameters for demand
price = 700
quantity = 6802
elasticity = 0.8

# Solve equation for demand
a = quantity / (price**(-elasticity))

# Define the isoelastic demand function
def isoelastic_demand(p):
    return a * p**(-elasticity)

# Calculate demand quantity for the given price
q_demand = isoelastic_demand(price)

# Define the vertical supply function
def vertical_supply(p):
    return quantity

# Calculate supply quantity for the given price
q_supply = vertical_supply(price)

# Generate a range of p values
p_values = np.linspace(500, 1000, 100)

# Calculate corresponding q values using the isoelastic demand and vertical supply functions
q_demand_values = isoelastic_demand(p_values)
q_supply_values = [vertical_supply(p) for p in p_values]

# Plot the isoelastic demand and vertical supply curves
plt.plot(p_values, q_demand_values, label='Isoelastic Demand Curve', color='r')
plt.axvline(x=price, color='g', linestyle='--', label='Supply Curve')  # Vertical supply line
plt.scatter(price, q_demand, color='b', label=f'Point of equilibrium: (p={price}, q={q_demand})')
plt.xlabel('Price £ (p)')
plt.ylabel('Quantity (q)')
plt.title('Supply and Isoelastic Demand')
plt.legend()
plt.grid(True)
plt.show()
