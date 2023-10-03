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

def 