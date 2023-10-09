import math

# Define a dictionary to hold the initial parameter values
params = {
    'elas': .67,
    'x1': 3,
}

# Define the student population dictionary
student_population = {
    '2018/19': 8984,
    '2019/20': 9224,
    '2020/21': 10119,
    '2021/22': 10425,
    # '2022/23': None,  # You can fill in the population for 2022/23 when you have the data
}

# Define the student population dictionary
HMO_provision = {
    '2018/19': 13036,
    '2019/20': 12953,
    '2020/21': 10415,
    '2021/22': 8619,
    '2022/23': 6802,  # !!!used to calibrate x1
}

# Create an empty list to store the price values
price_values = []

# Iterate over the keys (academic years) in the dictionary and calculate price
for academic_year, population in student_population.items():
    population = student_population[academic_year]
    # Get the quant value from the HMO_provision dictionary based on the academic year
    quant = HMO_provision.get(academic_year, 0)  # Use 0 as a default value if the academic year is not found
    price = (quant / (params['x1']*population)) ** (-1 / params['elas'])
    price_values.append(price)  # Append the calculated price to the list
    print(f"{academic_year}: {price}")
    print(f"{quant}")
   # print(price_values)
    
print(price_values)
