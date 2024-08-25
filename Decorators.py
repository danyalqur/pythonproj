# Decorators
# Decorators allow you to make simple modifications to callable objects like functions, methods or
#  classes. In this tutorial we'll look at functions.

# # The following syntax...
# @decorator
# def functions(arg):
#     return "value"
# #
# # ... is equivalent to 
# def function(arg):
#     return "value"
# function = decorator(function) # this passes the function to the decorator, and reassigns it to the 
#                                #  functions

# As you may have seen, a decorator is just another function which takes a function and returns one.
#  for example you could do this:

# def repeater(old_function):
#     def new_function(*args, **kwds): # learnpython.org/en/Multiple%20Function%20Arguments tells you how 
#                                      #  this works
#         old_function(*args, **kwds) # run the old function
#         old_function(*args, **kwds) # func so nice we ran it twice
#     return new_function # now we have to return the new_function or it wont reassign the value
# #
# # This would make a function repeat twice
# #
# @repeater
# def multiply(num1, num2):
#     print(num1*num2)
# #
# multiply(2,3)

# # You can also make it:
# # 1. change the output
# def double_out(old_function):
#     def new_function(*args, **kwds):
#         return 2 * old_function(*args, **kwds) # modify the return value
#     return new_function
# #
# # 2. change the input
# def double_Ii(old_function):
#     def new_function(arg): # only works if the olds function has one argument
#         return old_function(arg * 2) # modify the argument passed
#     return new_function
# #
# # 3. do checking
# def check(old_function):
#     def new_function(arg):
#         if arg < 0: raise (ValueError, "Negative Argument") # This causes an error, which is better than
#                                                             #  it doing the wrong thing
#         old_function(arg)
#     return new_function

# Let's say you want to multiply the output by a variable amound. You could define a decorator and use it
#  as follows:

# def multiply(multiplier): # passing the number we want to multiply
#     def multiply_generator(old_function): # multiply generator which we give the old function
#         def new_function(*args, **kwds): # new function here
#             return multiplier * old_function(*args, **kwds) # multiplier * output of old function call 
#                                                             #  using any passed args and kywds
#         return new_function
#     return multiply_generator # returns the new generator
# #
# # Usage
# @multiply(3) # multiply is not a decorator, but multiply(3) is
# def return_num(num): # return num is the old_function that is being passed in the multiply generator func
#     return num
# #
# # Now return_num is decorated and reassigned into itself
# print(return_num(5)) # should return 15

# You can do anything you want with the old function, even completely ignore it! Advanced decorators can
#  can also manipulate the doc string and argument number. 
#  Some good examples exist here: http://wiki.python.org/moin/PythonDecoratorLibrary

# Exercise
# Make a decorator factory which returns decorators that decorates functions with one argument. The 
#  factory should take one argument, a type, and then returns a decorator  with a function that 
#  checks if the input is the correct type. If it is wrong, it should print ("Bad Type"), really this
#  would be implemented IRL with raising an error but we dont want to do that in this exercise.  

def type_check(correct_type):
    #put code here
    def checked_func_factory(old_func):
        def new_func(*args, **kwds):
            if(isinstance(args[0], correct_type)):
                return old_func(*args, **kwds)
            else:
                print("Bad Type")
        return new_func
    return checked_func_factory

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])
