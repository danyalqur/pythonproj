# Lambda Functions

# Normally we define a function using the def keyword somewhere in the code and call it whenever we need to use it. For example:

# def sum(a, b):
#     return a + b
# #
# a, b = 1, 2
# c = sum(a, b)
# print(c)

# Now instead of defining the function somewhere and calling it, we can use python's lambda functions, which are inline functions defined at the same place we
#  use it. So we need to declare a function somewhere and revisit the code just for a single time use

# # example of a lamdba function
# your_function_name = lambda inputs : output

# To use our sum example recreated as a lamdba function, we would do the following:

# a, b = 1, 2
# sum = lambda x, y : x + y
# c = sum(a,b)
# print(c)

# Here we are assigning the lambda function to the variable sum, and upon giving the arguments, i.e. a and b, it works like a normal function

# Exercise
# Write a program using lambda functions to check if a number in the given list is odd. Print "True" if the number is odd or "False" if not for each element

l = [2, 4, 7, 3, 14, 19]
for i in l:
    # your code here
    checker = lambda i : i % 2
    e = print(bool(checker(i)))