import math

# Define a dictionary to hold the initial parameter values
params = {
    'elas': 1,
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
    '2018/19': 8984,
    '2019/20': 9224,
    '2020/21': 10119,
    '2021/22': 10425,
    # '2022/23': None,  # You can fill in the population for 2022/23 when you have the data
}

# Iterate over the keys (academic years) in the dictionary and calculate price
for academic_year, population in student_population.items():
    population = student_population[academic_year]
    # Get the quant value from the HMO_provision dictionary based on the academic year
    quant = HMO_provision.get(academic_year, 0)  # Use 0 as a default value if the academic year is not found
    price = (params['quant'] / (params['x1']*population)) ** (-1 / params['elas'])
    print(f"{academic_year}: {price}")
    Print(f"{quant}")
