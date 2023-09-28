import unittest
import math

# Define a dictionary to hold the initial parameter values
params = {
    'quant': 3,
    'price': 10,
    'e': 0,
    'a': 3,
}

target_parameter = ""

# Your code for calculating the missing parameter
def calculate_missing_parameter(params, target_parameter):
     for key in params:
        if params[key] == 0:
            target_parameter = key  
            if target_parameter == 'quant':
                params[target_parameter] = params['a'] * params['price'] ** -params['e']
            elif target_parameter == 'price':
                params[target_parameter] = (params['quant'] / params['a']) ** (-1 / params['e'])
            elif target_parameter == 'e':
                params[target_parameter] = -math.log(params['quant'], params['price'])
            elif target_parameter == 'a':
                params[target_parameter] = params['quant'] / (params['price'] ** -params['e'] )    
            return params[target_parameter]
            
print(calculate_missing_parameter(params, target_parameter)) 
# Calculate the missing parameter based on the specified relationship quant = a * price^(-e)

    
    



# class TestCalculateMissingParameter(unittest.TestCase):

#     def test_calculate_missing_a(self):
#         result = calculate_missing_parameter({'quant': 6802, 'price': 700, 'e': .8, 'a': None}, 'a')
#         self.assertAlmostEqual(result, 4.0, places=2)  # 'a' is calculated based on the relationship

# if __name__ == '__main__':
#     unittest.main()
