# Task: Represent common multi-variable mathematical functions in Python.


# 1. Define a function called average_value that takes in two numerical inputs and outputs their average.
def average_value(x, y):
    average = (x + y) / 2
    return average


# 2. Define a function called max_of_three that takes in three numerical inputs and outputs the maximum value.
def max_of_three(x, y, z):
    lst = [x, y, z]
    max_value = max(lst)
    return max_value


# 3. Define a function called min_of_three that takes in three numerical inputs and outputs the minimum value.
def min_of_three(x, y, z):
    lst = [x, y, z]
    min_value = min(lst)
    return min_value


# 4. Define a function called midrange that takes in three numerical inputs and outputs the average of the maximum
# and minimum values. This function should call the functions created in tasks 1 - 3.
def midrange(x, y, z):
    avg_max_and_min = average_value(max_of_three(x, y, z), min_of_three(x, y, z))
    return avg_max_and_min
