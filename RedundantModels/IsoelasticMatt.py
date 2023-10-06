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

# Generate a range of p values (price values)
p_values = np.linspace(500, 1000, 100)

# Calculate corresponding q values (quantity values) using the isoelastic demand function
q_demand_values = isoelastic_demand(p_values)

# Define the vertical supply function (supply curve coming from x-axis)
def vertical_supply(p):
    return quantity

# Calculate supply quantity for the given price
q_supply = vertical_supply(price)

# Generate a vertical supply curve (constant quantity)
q_supply_values = [vertical_supply(p) for p in p_values]

# Plot the isoelastic demand and vertical supply curves
plt.plot(q_demand_values, p_values, label='Isoelastic Demand Curve', color='r')
plt.axvline(x=quantity, color='g', linestyle='--', label=f'Supply Curve (q={quantity})')  # Vertical supply line
plt.scatter(quantity, price, color='b', label=f'Point of equilibrium: (q={quantity}, p={price})')
plt.xlabel('Quantity (q)')
plt.ylabel('Price £ (p)')
plt.title('Isoelastic Demand and Vertical Supply')
plt.legend()
plt.grid(True)
plt.show()
