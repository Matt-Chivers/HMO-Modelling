import numpy as np
from scipy.optimize import fsolve

# Define a dictionary to hold the initial parameter values
paramseq1 = {
    'quant': 6924,
    'price': 991.6667,
    'student': 5071
}

paramseq2 = {
    'quant': 6802,
    'price': 1144.67,
    'student': 6301
}

# Function to represent the system of equations
def equations(vars):
    x, elas = vars
    eq1 = paramseq1['quant'] - x * paramseq1['student'] * paramseq1['price']**elas
    eq2 = paramseq2['quant'] - x * paramseq2['student'] * paramseq2['price']**elas
    return [eq1, eq2]

# Initial guesses for x and elas
initial_guesses = [1, 1]

# Solve for x and elas
solution = fsolve(equations, initial_guesses)

# Unpack the results
x, elas = solution

# Print the results
print("Solution for x:", x)
print("Solution for elasticity (elas):", elas)
