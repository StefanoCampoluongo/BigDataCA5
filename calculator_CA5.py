# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 15:35:35 2018

@author: campo
"""
# import the math module
# import reduce
import math 
from functools import reduce

# An add function which takes a list and sums the elements
def add(values):
    types = (int, float, complex)#control of datatype
    if all(isinstance(x, types) for x in values):
        return reduce(lambda x, y: x+y, values)
    return "Elements in the input list can only be int, float or complex"

# A cosine function which takes a list of numbers (in degrees) and returns a list with the cosine of each element of the input list
def cosine(values):
    types = (int, float)#control of datatype
    if all(isinstance(x, types) for x in values):
        return list(map(lambda x: round(math.cos(math.radians(x)),15),values)) #15 decimal places to receive zero when expected (eg cos(90))
    return "Elements in the input list can only be int or float"

# A cube function which takes a list of numbers and returns a list with the cube of each element of the input list
# List Comprehension has been used
def cube(values):
    types = (int, float, complex)#control of datatype
    if all(isinstance(x, types) for x in values):
        return [i*i*i for i in values]
    return "Elements in the input list can only be int, float or complex"

# A division function which takes a list and divides the first element of the list by the other elements
def division(values):
     types = (int, float, complex)#control of datatype
     if all(isinstance(x, types) for x in values):
        if all(x != 0 for x in values[1:]): #only the first element of the input list can be zero
            return reduce(lambda x, y: x/y, values)
        return "Division by zero not allowed"#dividing a number by zero is not allowed
     return "Elements in the input list can only be int, float or complex"
   
# An exponent function which takes a list as argument, reduce has been used
def exponent(values):
    types = (int, float, complex)#control of datatype
    if all(isinstance(x, types) for x in values):
        if values[0]==0:
            if all(x >= 0 for x in values[1:]):
                return 0
            else:
                return "0 cannot be raised to a negative power"#zero by the power of a negative number is not allowed
        return reduce(lambda x, y: x**y, values)
    return "Elements in the input list can only be int, float or complex"

# A multiply function which takes a list and multiplies the elements
def multiply(values):
    types = (int, float, complex)#control of datatype
    if all(isinstance(x, types) for x in values):
        return reduce(lambda x, y: x*y, values)
    return "Elements in the input list can only be int, float or complex"

# A sine function which takes a list of numbers (in degrees) and returns a list with the sine of each element of the input list
def sine(values):
    types = (int, float)#control of datatype
    if all(isinstance(x, types) for x in values):
        return list(map(lambda x: round(math.sin(math.radians(x)),15),values)) #15 decimal places to receive zero when expected (eg cos(90))
    return "Elements in the input list can only be int or float"

# A square function which takes a list of numbers and returns a list with the square of each element of the input list
def square(values):
    types = (int, float, complex)#control of datatype
    if all(isinstance(x, types) for x in values):
        return [i*i for i in values] #List Comprehension
    return "Elements in the input list can only be int, float or complex"   

# A square root function which takes a list of numbers and returns a list with the square root of each element of the input list
def squareRoot(values):
    types = (int, float)#control of datatype
    if all(isinstance(x, types) for x in values) and all(x >= 0 for x in values):
        return list(map(lambda x: math.sqrt(x), values))
    return "Each element in the input list must be a positive number"

# A subtraction function which takes a list and subtracts to the first element of the list the other elements
def subtraction(values):
    types = (int, float, complex)#control of datatype
    if all(isinstance(x, types) for x in values):
        return reduce(lambda x, y: x-y, values)
    return "Elements in the input list can only be int, float or complex"


