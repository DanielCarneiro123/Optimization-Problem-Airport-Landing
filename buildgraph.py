import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the logarithmic function
def logarithmic_function(x, a, b):
    return a * np.log(x) + b

# Read time data from file
with open("src/execution_time.txt", "r") as time_file:
    time_data = [float(line.strip()) for line in time_file]

# Read fitness data from file and reverse the order
with open("src/genetic_output.txt", "r") as fitness_file:
    fitness_data = [float(line.strip()) for line in fitness_file]


# Perform curve fit
params, covariance = curve_fit(logarithmic_function, time_data, fitness_data)

# Generate fitted data
fitted_data = logarithmic_function(time_data, *params)

# Plot original data and fitted curve
plt.plot(time_data, fitness_data, 'b.', label='Original Data')
plt.plot(time_data, fitted_data, 'r-', label='Fitted Curve')
plt.xlabel('Time (seconds)')
plt.ylabel('Fitness Value')
plt.title('Fitness vs Time')
plt.legend()
plt.show()
