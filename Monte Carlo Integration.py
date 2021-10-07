#####       The Monte Carlo method is used, in this case, to find the integral of a function, f(x), using randomly generated points between the integral limits     #####
#####                     Points are generated at random within the limits, and are tested to see if they lie within the function                                   #####
#####                            Counts are kept of the total number of tests, and the tests that fall under the function limits                                    #####
#####                                       The successful tests are those points that lie within the function                                                      #####
#####                       Unsuccessful tests fall outside the function, but within a larger, regular shape with a clearly defined area                            #####
#####            The ratio of successful / unsuccessful tests is found, and multiplied by the larger area to find the integral (area) of the function               #####

import numpy as np
from scipy import random

# Define the function to be integrated
def f(x):
    return np.sin(x)

# Set the limits of integration
a = 0
b = np.pi

# Set initial conditions for the number of total and successful tests
total_count = 0
area_count = 0

# Set the number of random points tested (the larger this value, the more accurate and less quick the test is)
n = 10000

# Main MC loop
# Loop iterated 'n' times, each time random x and y coordinated are set, and if they lie within the function, area_count is increased by 1
# Regardless of whether the test is successful or not, total_count increases by 1
# x_coord and y_coord use values based on the integration limits, and the known upper and lower values for the function within the limits 
while total_count < n:
    x_coord = random.uniform(a, b)
    y_coord = random.uniform(0, 1) 
    if y_coord < f(x_coord):
        area_count += 1
    total_count += 1

# The area of the function is the ratio of successful to unsuccessful tests, multiplied by the area of the larger shape (1 * pi)
result = (area_count / total_count) * np.pi
print(result)