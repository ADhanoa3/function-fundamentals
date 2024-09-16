# Task: Represent common single-variable mathematical functions in Python.


# 1. Define a function called linear_function that represents the linear function f(x) = 2x+3.
def linear_function(x, slope=2):
    output = (slope * x) + 3
    return output


# 2. Define a function called constant_function that represents the constant function g(x) = 4.
def constant_function(x, slope=0):
    output = (x * slope) + 4
    return output


# 3. Define a function called exponential_function that represents the exponential function h(x) = 2^x.
def exponential_function(x, base=2):
    output = base**x
    return output


# 4. Use a built-in command to define a function called absolute_value that represents the absolute value function k(x)=|x|.
def absolute_value(x):
    abs_value = abs(x)
    return abs_value
