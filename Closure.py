# Closures

# A closure is a function object that remembers values in enclosing scopes even if they are not present 
#  in memory. We'll work through this idea step by step

# Firstly, a NESTED FUNCTION is a function inside another function. It's very important to note that the
#  nested functions can access the variables of the enclosing scope. However, at least in Python, they
#  are only readonly. However, one can use the "nonlocal" keyword explicitly with these variables in 
#  order to modify them

# For example:
# def transmit_to_space(message):
#     "This is the enclosing function"
#     def data_transmitter():
#         "The nested function"
#         print(message)
# #
#     data_transmitter() # function call of nested function inside enlcosing function
# #
# print(transmit_to_space("Test message")) # Call of enclosing function

# This works well as the 'data_transmitter' function can access the 'message' because it is "local"
# To demonstrate the use of "nonlocal" keyword, consider this:

# def print_msg(number):
#     def printer():
#         "Here we are using the nonlocal keyword"
#         nonlocal number
#         number=3
#         print(number)
#     printer()
#     print(number)
# #
# print_msg(9) 
# # -> 3
# #    3

# Without the nonlocal keyword, the output would be "3 9", however with its usage we get "3 3"
#  this means the value of the "number" variable gets modified.

# Now we are going to return the function object rather than calling the nested function within.
#  Remember that even functions are objects in Python

# def transmit_to_space(message):
#     "This is the enlcosing function"
#     def data_transmitter():
#         "The nested function"
#         print(message) # remember that from Python's closure mechanism, the function has access to the 
#                        #  message variable from the enclosing function.
#     return data_transmitter # This return is what creates the closure. Remember that the closure is a
#                             #  function that remembers parameters passed in its enclosing scopes [even
#                             #  if they are not present in memory].
# #
# fun2 = transmit_to_space("my message is this") # This creates a new function which fixes the message
#
# # The transmit_to_space function runs, and the data_transmitter function is created.
# # However, instead of executing data_transmitter, the function itself (not its result) is returned 
# # and assigned to fun2.
# # The returned data_transmitter function now "remembers" the message that was passed to transmit_to_space.
# 
# fun2() # This calls the above created function
# # -> my message is this


# MOST IMPORTANT NoTE: Notice how we didnt have to give the message again, and the message does not 
#  exist elsewhere in memory. This is the key defining feature of what we have done here in creating the
#  closure

# The data_transmitter function is executed.
# Because of the closure, data_transmitter still has access to the message ("my message is this") 
# even though transmit_to_space has finished executing.
# It prints the message.

# Why is return data_transmitter needed?
# Creating a Closure: It allows data_transmitter to form a closure around the message variable. 
# Without returning the data_transmitter function, you would not be able to call it later and have it 
# "remember" the message.

# Deferred Execution: It enables you to defer the execution of data_transmitter until later. 
# This is useful when you want to fix certain parameters (like message) at one time but actually use them 
# at a different time.

# In summary, return data_transmitter is essential because it allows you to create and return a closure, 
# enabling the function to retain access to the message variable long after the enclosing 
# transmit_to_space function has finished executing.

# Even though the execution of the "transmit_to_space()" was completed, the message was rather preserved
#  This technique by which the data is attached to some code even after the end of those other functions
#  is called, is known as "closures" in Python

# ADVANTAGES: Closures can avoid use of global variables and provides some form of data hiding (e.g
#  when there are few methods in a class, use closures instead)

# Also, Decorators in Python make extensive use of closures.

# Exercise
# Make a nested loop and a python closure to make functions to get multiple multiplication functions 
#  using closures. That is using closures, one could make functions to create multiply_with_5(), or 
#  multiply_with_4() functions.

# your code goes here
def multiplier_of(number1):
    "This is the enclosing function"
    def multiplier(number2):
        print(number1 * number2)
    return multiplier

multiplywith5 = multiplier_of(5) # think of it like this, we're essentially asking to be given back the 
                                 #  nested function but with a parameter fixed that is used inside it
                                 #  that parameter being the one that is in the enclosing function's 
                                 #  scope 

multiplywith6 = multiplier_of(6)

multiplywith5(10)
multiplywith6(10)