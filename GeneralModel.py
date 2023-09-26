# This method takes all the parameters and outputs the ones wich are not equal to zero.
x1 = 1
x2 = 2
x3 = 0
x4 = 0
x5 = 6

def check_for_non_zero_parameters(x1, x2, x3, x4, x5):
    parameters = [x1, x2, x3, x4, x5]
    parameters_in_use = []

    for param in parameters:
        if param != 0:
            parameters_in_use.append(param)

    return parameters_in_use

non_zero_parameters = check_for_non_zero_parameters(x1, x2, x3, x4, x5)

# Install package


    

