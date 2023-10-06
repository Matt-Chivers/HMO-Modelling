import unittest
import math

# Define a dictionary to hold the initial parameter values
params = {
    'quant': 1,
    'price': 1111,
    'e': 1,
    'a': 3,
}

target_parameter = ""

# Code for calculating the missing parameter
def calculate_missing_parameter(params, target_parameter):
     for key in params:
        if params[key] == 0:
            target_parameter = key  
            if target_parameter == 'quant':
                params[target_parameter] = params['a'] * params['price'] ** -params['e']
            elif target_parameter == 'price':
                params[target_parameter] = (params['quant'] / params['a']) ** (-1 / params['e'])
            elif target_parameter == 'e':
                params[target_parameter] = -math.log(params['quant']/ params['a'], params['price'])
            elif target_parameter == 'a':
                params[target_parameter] = params['quant'] / (params['price'] ** -params['e'] )    
            return params[target_parameter]
            
print(calculate_missing_parameter(params, target_parameter))
