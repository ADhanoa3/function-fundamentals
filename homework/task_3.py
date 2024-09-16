# Task: Represent functions with non-numerical parameters.


# 1. Define a function called first_element that takes in a list and outputs its first element.
def first_element(a, b, c, d):
    lst = [a, b, c, d]
    first = lst[0]
    return first


# 2. Define a function called last_element that takes in a list and outputs its last element.
def last_element(a, b, c, d):
    lst = [a, b, c, d]
    last = lst[-1]
    return last


# 3. Define a function called first_last_sum that takes in a list and outputs the sum of
# the first and last element. The function should call the functions in tasks 1-2.
def first_last_sum(a, b, c, d):
    firstlastsum = first_element(a, b, c, d) + last_element(a, b, c, d)
    return firstlastsum


# 4. Define a function called distance_from_origin that takes in a tuple representing a point
# in the xy-coordinate plane and outputs its distance from the origin.
# Hint: Learn how to "unpack" a tuple input.
def distance_from_origin(x, y):
    a, b = (x, y)
    import math

    square_distance = (a**2) + (b**2)
    distance = math.sqrt(square_distance)
    return distance


# 5. Define a function called distance_between that takes in two tuples representing points
# in the xy-coordinate plane and outputs their distance from each other.
# Hint: "Unpack" each input tuple.
def distance_between(x, y, w, z):
    a, b = (x, y)
    c, d = (w, z)
    import math

    square_distance = ((a - c) ** 2) + ((b - d) ** 2)
    distance = math.sqrt(square_distance)
    return distance
