import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Define your data as a dictionary
data = {
    'Year': [2016, 2017, 2018, 2020, 2021, 2022],
    'Monthly_Rent': [991.6667, 957.6667, 922.6667, 1037, 1037, 1144.6667]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Initialize the Linear Regression model
model = LinearRegression()

# Fit the model with the data from the DataFrame
model.fit(df[['Year']], df['Monthly_Rent'])

# Create a range of years including the year to predict
years_range = np.array(range(2016, 2028)).reshape(-1, 1)

# Predict the rent for the range of years
rent_predictions = model.predict(years_range)

# Plot the actual data
plt.scatter(df['Year'], df['Monthly_Rent'], color='blue', label='Actual Data')

# Plot the line of best fit
plt.plot(years_range, rent_predictions, color='red', label='Line of Best Fit')

# Calculate the predicted value for 2027
year_to_predict = 2027
predicted_rent_2027 = model.predict([[year_to_predict]])[0]

# Print out the predicted rent for 2027
print(f"The predicted monthly rent for the year {year_to_predict} is £{predicted_rent_2027:.2f}")

# Highlight the predicted value for 2027
plt.scatter([year_to_predict], [predicted_rent_2027], color='green', label='2027 Prediction')

# Annotations and labels
plt.title('Monthly Rent Prediction')
plt.xlabel('Year')
plt.ylabel('Monthly Rent (£)')
plt.legend()

# Show the plot
plt.show()
