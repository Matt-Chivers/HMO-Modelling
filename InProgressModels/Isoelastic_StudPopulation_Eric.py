# Student Population data: 
# 2016/17:  
# 2017/18:  
# 2018/19: 8,984   
# 2019/20: 9,224 
# 2020/21: 10,119 
# 2021/22: 10,425 
# 2022/23: 
# Student Population data for each academic year
student_population = {
    '2018/19': 8984,
    '2019/20': 9224,
    '2020/21': 10119,
    '2021/22': 10425,
#    '2022/23': None,  # You can fill in the population for 2022/23 when you have the data
}
# HMO Supply data for each academic year
HMO_provision = {
    '2018/19': 13036,
    '2019/20': 12953,
    '2020/21': 10415,
    '2021/22': 8169,
}

import numpy as np
print(np.__version__)

# Define a dictionary to hold the initial parameter values
params = {
    'quant': 6802,
    'price': 700,
    'elas': '?',
    'x1': 1284443.7,
}

import numpy as np
print(np.__version__)


# Student Population data for each academic year
student_population = {
    '2018/19': 8984,
    '2019/20': 9224,
    '2020/21': 10119,
    '2021/22': 10425,
    #'2022/23': None,  # You can fill in the population for 2022/23 when you have the data
}

# Define a function to calculate demand for a given year
def calc_isodemand(year, params):
    a = params['quant'] / (params['price'] ** -params['elas'])
    return [isoelastic_demand(p, a, params['elas'], year) for p in p_values]

# Define the isoelastic demand function
def isoelastic_demand(p, a, elas, year):
    return a * p ** (-elas) * student_population[year]

# Define the parameter values
params = {
    'quant': 6802,
    'price': 700,
    'elas': 0.67,
}

# Generate a range of price values
p_values = np.linspace(400, 900, 100)

# Calculate and store demand for each academic year
demand_data = {}
for year in student_population.keys():
    demand_data[year] = calc_isodemand(year, params)

# Print demand for each year
for year, demand in demand_data.items():
    print(f'Demand for {year}:')
    for p, q in zip(p_values, demand):
        print(f'Price: {p}, Demand: {q}')


