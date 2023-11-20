# Revised script to include printing the estimated student numbers for each year

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Student numbers data
studentNumber = {
    '2010': 7730 - 3649,
    '2011': 7775 - 3836,
    '2012': 7582 - 3518,
    '2013': 7860 - 3722,
    '2014': 8206 - 3574,
    '2015': 8420 - 3752,
    '2016': 8786 - 3783,
    '2017': 9140 - 3798, 
    '2018': 8983 - 3912,
    '2019': 9227 - 4052,
    '2020': 10120 - 3739,
    '2021': 10426 - 4184,
    '2022': 10468 - 4167
} 

# Extracting years and numbers for analysis
years = list(map(int, studentNumber.keys()))
numbers = list(studentNumber.values())

# Linear regression only on actual data
slope, intercept, r_value, p_value, std_err = linregress(years, numbers)

# Generating line of best fit values for existing data and predictions
extended_years = range(min(years), max(years) + 6)  # up to 2027
line_of_best_fit = [slope * year + intercept for year in extended_years]

# Plotting the data with individual years on the x-axis
plt.figure(figsize=(12, 6))
plt.plot(years, numbers, 'o', label='Actual Data')
plt.plot(extended_years, line_of_best_fit, 'g-', label='Line of Best Fit')

# Setting x-axis to display individual years
plt.xticks(extended_years)

plt.xlabel('Year')
plt.ylabel('Number of Students')
plt.title('Student Numbers Over Years with Linear Regression')
plt.legend()
plt.grid(True)
plt.show()

# Printing the estimated student numbers for each year
estimated_numbers = dict(zip(extended_years, line_of_best_fit))
print("Estimated Student Numbers by Year:")
for year, estimate in estimated_numbers.items():
    print(f"{year}: {round(estimate)}")

