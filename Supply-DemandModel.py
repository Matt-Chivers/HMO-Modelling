# Enter "pip install matplotlib" into command line to produce graph
import matplotlib.pyplot as plt
import numpy as np
import sys

# This code takes the users input and assigns them to a variable
average_rent = float(input("What is the average rent? "))
house_supply = float(input("What is the supply of houses? "))
elasticity = float(input("What is the elasticity of demand? "))

def plot_graph():

    # This code calculates the slope
    slope = (house_supply * elasticity) / average_rent
    rounded_slope = round(slope, 2)
    print(rounded_slope)

    # This code calculates the intercept
    max_demand = -rounded_slope * house_supply + average_rent 
    absolute_demand = abs(max_demand)
    rounded_demand = round(absolute_demand, 2)
    print(rounded_demand)

    # This code calculates the demand curve
    string_demand = str(rounded_demand)
    string_intercept = str(rounded_slope)
    demand_curve = "y = " + string_demand + string_intercept + "x"
    print("The demand curve: " + demand_curve)

    # This code calculates the supply curve
    string_house_supply = str(house_supply)
    supply_curve = "x = " + string_house_supply
    print("The supply curve: " + supply_curve)

    # Create an array of x values
    x = np.linspace(0, 10000, 100)  # Adjust the range and number of points as needed

    # Calculate the corresponding y values for the demand curve using the equation
    y_demand = rounded_demand + rounded_slope * x

    # Create a vertical line at the specified point
    vertical_line_x = [house_supply, house_supply]
    vertical_line_y = [min(y_demand), max(y_demand)]

    # Plot the supply curve, demand curve, and the vertical line
    plt.figure(figsize=(8, 6))
    plt.plot(x, y_demand, label='Demand Curve')
    plt.axvline(x=house_supply, color='green', linestyle='--', label='Supply Curve')

    # Annotate the equilibrium point with text
    plt.annotate(
        f'Equilibrium: ({house_supply}, {average_rent})',
        xy=(house_supply, average_rent),
        xytext=(house_supply + 1000, average_rent + 100),
        arrowprops=dict(arrowstyle='->', color='black'),
    )

    plt.title('Supply and Demand Model')
    plt.xlabel('Quantity of Houses')
    plt.ylabel('Price of Rent')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Print the equilibrium point
    print(f'Equilibrium Price: £{average_rent}')
    print(f'Equilibrium Quantity: {house_supply}')

    # Call the method to run the code
plot_graph()

counterfactual = float(input("Counterfactual: If you want to see what happens when we increase or decrease supply by a certain percentage, type a number. If not, type 0 to exit. "))
if counterfactual > 0:
    house_supply = house_supply * (counterfactual / 100 + 1)
    plot_graph()
elif counterfactual < 0:
    house_supply = house_supply * (counterfactual / 100 + 1)
    plot_graph()
else: sys.exit()


