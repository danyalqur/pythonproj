# Partial Functions

# You can create partial functions in Python by using the parital function from the functools library

# Partial functions allow one to derive a function with x parameters to a function with fewer parameters and fixed values set for the more limited function

# Like repurposing a function and tweaking its input needs and

# We need the functools module to make partial functions. The import looks like this:

# from functools import partial 

# The following example shows how we can create a partial function from a function:

# from functools import partial
# #
# def multiply(x, y):
#     return x * y
# #
# dbl = partial(multiply, 2) # creates a partial function and replaces the first parameter (x) of original function (multiply) with 2
# #
# print(dbl(4))
# # -> 8

# One important note: the default values will start replacing variables from the left. The 2 will replace x. In order to replace a given parameter we need to
#  do the following:

# import functools
# #
# from functools import partial
# #
# def multiply(x, y):
#     return x * y
# #
# dbl = partial(multiply, y=2) # in order to edit a parameter that is not the first, the format looks like this : partial_function = partial(my_function, b=2, c=3, d=4)
# #
# print(dbl(3))

# Exercise
# Edit the function provided by calling partial() and replacing the first three variables in func(). Then print with the new partial function using only 
#  one input variable so that the output equals 60.

#Following is the exercise, function provided:
from functools import partial
def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function
#
sixty = partial(func, u = 10, v = 2, w = 2) # filling from an order other than left to right can be problematic and cause issues down the line so dont do this
# When you use this format for fixing values, you must be explicit in the function call too
print(sixty(x = 10)) # Like this

# otherwise use the less explicit approach like this:
sixtyother = partial(func, 10, 2, 2)
print(sixtyother(10))
