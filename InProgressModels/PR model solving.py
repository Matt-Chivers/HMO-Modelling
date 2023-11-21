import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

# Define a dictionary to hold the initial parameter values
paramseq1 = {
    'quant': 6802,
    'price': 991.67,
    'elas': ,
    'x1': ,
}
# Define a dictionary to hold the initial parameter values
paramseq2 = {
    'quant': 6924,
    'price': 1144,
    'elas': ,
    'x1': ,
}
# Student number data
studentNumber = {
    '2018': 8983 - 3912,
    '2022': 10468 - 4167,
}
# Function to represent the system of equations
def equations(vars, quant, price):
    x1, elas = vars
    return [
        quant - x1* price**-elas,
    ]
# Solve for x1 and elas for paramseq1
result1 = fsolve(equations, [1, 1], args=(paramseq1['quant'], paramseq1['price']))

# Solve for x1 and elas for paramseq2
result2 = fsolve(equations, [1, 1], args=(paramseq2['quant'], paramseq2['price']))

# Update the dictionaries with the results
paramseq1['x1'], paramseq1['elas'] = result1
paramseq2['x1'], paramseq2['elas'] = result2

# Print the results
print("Result for paramseq1:", paramseq1)
print("Result for paramseq2:", paramseq2)


# # Define the isoelastic demand function
# def isoelastic_demand(p, a, elas):
#     q = a * p ** (-elas)
#     return q

# # Define the vertical supply function (supply curve coming from the x-axis)
# def vertical_supply(p):
#     return params['quant']

# # This method takes all the parameters and calculates the missing one.
# def calculate_missing_parameter(params, target_parameter):
#     if params[target_parameter] != '?':
#         return params[target_parameter]
#     elif target_parameter == 'quant':
#         params[target_parameter] = params['x1'] * params['price'] ** -params['elas']
#     elif target_parameter == 'price':
#         params[target_parameter] = (params['quant'] / params['x1']) ** (-1 / params['elas'])
#     elif target_parameter == 'elas':
#         params[target_parameter] = -math.log(params['quant'] / params['x1']) / math.log(params['price'])
#     elif target_parameter == 'x1':
#         params[target_parameter] = params['quant'] / (params['price'] ** -params['elas'])
#     return params[target_parameter]

# target_parameter = 'quant'  # Replace with the parameter you want to calculate
# calculated_value = calculate_missing_parameter(params, target_parameter)
# print(f'{target_parameter}: {round(calculated_value, 2)}')

# # Apply counterfactual to the parameters based on demand shock from 2010 to 2011
# def counterfactual_demand_shock(params, studentNumber):
#     # Calculate the demand shock
#     demand_shock = studentNumber['2027'] / studentNumber['2016']

#     # Apply the demand shock to coefficient 'a'
#     a = params['quant'] / (params['price'] ** -params['elas'])
#     a *= demand_shock

#     # Recalculate 'price' to find the new equilibrium after the demand shock
#     new_equilibrium_price = (params['quant'] / a) ** (-1 / params['elas'])
    
#     return new_equilibrium_price, a

# # Calculate demand quantity for the given price
# a = params['quant'] / (params['price'] ** -params['elas'])
# p_values = np.linspace(0, 1000, 100)
# q_demand_values = [isoelastic_demand(p, a, params['elas']) for p in p_values]

# # Plot the isoelastic demand and vertical supply curves
# plt.figure(figsize=(12, 6))

# # Plot the first graph (original data)
# plt.subplot(1, 2, 1)
# plt.plot(q_demand_values, p_values, label='Isoelastic Demand Curve', color='r')
# plt.axvline(x=params['quant'], color='g', linestyle='--', label=f'Supply Curve')
# plt.scatter(params['quant'], params['price'], color='b', label=f'Point of equilibrium: (q={round(params["quant"])}, p={round(params["price"])})')
# plt.xlabel('Quantity (q)')
# plt.ylabel('Price £ (p)')
# plt.title('Isoelastic Demand and Supply Curves')
# plt.legend()
# plt.grid(True)
# plt.xlim(0, 10000)

# # Applying demand shock and plotting the updated curves
# new_equilibrium_price, new_a = counterfactual_demand_shock(params, studentNumber)

# # Plot the second graph (data after demand shock)
# plt.subplot(1, 2, 2)
# q_demand_values_post_shock = [isoelastic_demand(p, new_a, params['elas']) for p in p_values]
# plt.plot(q_demand_values_post_shock, p_values, label='Isoelastic Demand Curve (Post-Shock)', color='r')
# plt.axvline(x=params['quant'], color='g', linestyle='--', label=f'Supply Curve')
# plt.scatter(params['quant'], new_equilibrium_price, color='b', label=f'New Point of Equilibrium: (q={round(params["quant"])}, p={round(new_equilibrium_price)})')
# plt.xlabel('Quantity (q)')
# plt.ylabel('Price £ (p)')
# plt.title('Isoelastic Demand and Supply Curves After Demand Shock')
# plt.legend()
# plt.grid(True)
# plt.xlim(0, 10000)
# plt.tight_layout()
# plt.show()

# print('New equilibrium price after demand shock: £' + str(round(new_equilibrium_price, 2)))
