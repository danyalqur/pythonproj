# Map, Filter, Reduce
# Map, Filter, and Reduce are paradigms of functional programming. They allow the programmer to write 
#  simpler, shorter code without necessarily needing to bother about intricacies like loops and branching

# Essentially, the threee functions allow you to apply a function across a number of iterables, in a few
#  easy moves. map and filter come built-in with Python (in the __builtin__ module) and require no 
#  importing. reduce however needs to be imported as it reside in the functools module.

# Map
# The map() function in python has the followign syntax:
# 
# map(func, *iterables)
# 
# Where func is the function on which each element in iterables (as many as there are) would be applied on.
#  the asterisk * on iterables means there can be as many iterables as possible, in so far as func has
#  that exact number of required input arguments. The following key notes are important:
# 
# 1. The map() function in Python 3 returns a map object which is a generator object. To get the result as 
#  a list, the built-in list() function can be called on the map object. i.e. list(map(func, *iterables))
# 
# 2. The number of arguments to func must be the number of iterables listed

# Say I have a list (iterable) of my favourite pet names, all in lower case and I need them in uppercase
#  . Traditionally, in normal pythoning we would do something like this:

# my_pets = ['alfred', 'tabitha', 'william', 'arla']
# uppered_pets = []
# #
# for pet in my_pets:
#     pet_ = pet.upper()
#     uppered_pets.append(pet_)
# #
# print(uppered_pets)
# # -> ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']

# With map() functions, it's not only easier but it's also much more flexible. I simply do this:

# # Python 3
# my_pets = ['alfred', 'tabitha', 'william', 'arla']
# #
# uppered_pets = list(map(str.upper, my_pets))
# #
# print(uppered_pets)
# # -> ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']

# Both these give the same result. Note that using the defined map() syntax above, func in this case is
#  str.upper and iterables is the my_pets list. That list is categorised as a single iterable. Notice
#  that we didn't called the str.upper function (we didnt use str.upper()), as the map function does that
#  for us on each element in the my_pets list.

# What's more important to note is that the str.upper function requires only one argument by definition
#  and so we passed just one iterable to it. So, if the function you're passing requires two, or three,
#  or n arguments, then you need to pass in two, three, or n ITERABLES to it.

# Example: say I have a list of circle areas that i calculated somewhere, all in five decimal places.
#  If I need to round each element on the list to its position decimal places, meaning that i have to round
#  the first to one d.p , the second to 2 d.p etc; this is easily accomplishable with map().

# Python gives us the round() built-in function already which takes two arguments, the number to round up
# and the d.p to round to. so theoretically a homie could do it like this:

# circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
# #
# round_areas = list(map(round, circle_areas, range(1, 7))) # func, iterable1, iterable2 # [= *iterables]
# #
# print(round_areas)
# print(list(range(1, 7))) # list of 1 - 6
# # this is all self explanatory if you understood everything up to now

# One of the features of map() is that if there is a mismatch in the elements between your iterables it
#  will not throw out an exception, it will simply stop and give the result with the list length of the 
#  limiting iterable. We can see an example of this below:

# circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
# #
# result = list(map(round, circle_areas, range(1, 3))) # range(1, 3) is just [1, 2]
# #
# print(result) 
# # -> [3.6, 5.58]

# Obviously the same thing would happen if we shortened the circle areas list equally.

# Exercise 1:
#  To consolidate our knowledge of map(), we are going to make a lambda function zip(). zip takes a number 
#  of iterables and creates a tuple containing each of the elements in the iterables. like map() it 
#  returns a generator object, which can be converted to a list by using the list function on it.

my_strings = ['a','b' ,'c' ,'d' ,'e']
my_numbers = list(range(1, 6))

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)

# From this we can learn that it can be useful to combine map with lambda functions to give us a powerful
#  in line function application over multiple lists. This highlights how powerful python is as we did not
#  need to build a function in the standard way. 

# Filter
#  While map() passes each element in the iterable through a function and returns the result of all 
#  elements after having passed through the function, filter requires the function to return boolean
#  values, and then passes each element in the iterable through the function, "filtering" those that are
#  false. It has the following syntax:
# 
#  filter(func, iterable)

# The following points need to be noted regarding filter():
#  1. Unlike map(), only one iterable is required.
#  2. The func argument is required to return a boolean type. If it doesn't, filter simply returns the 
#     iterable passed to it. Also, as only one iterable is required, implicitly we should know that the 
#     func must take only one argument
#  3. filter passes each element in the iterable through func and returns only the ones that evaluate to
#     to true. It acts as a true "filter" as its name suggests :)

# Example 1: we have a list (iterable) of the scores of 10 students in a Chemistry exam. Let's filter out
#  those who got more than 75

# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# #
# passers = list(filter(lambda x: bool(x>75), scores))
# #
# print(passers)
# # -> [90, 76, 88, 81]

# Example 2: Palindrome detector. Let's filter all palindromes from a tuple of suspected palindromes

# dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
# #
# real_dromes = list(filter(lambda word: (word[::-1] == word) , dromes))
# #
# print(real_dromes)
# # -> ['madam', 'anutforajaroftuna']

# Reduce
# Reduce applies a function of two arguments cumulatively to the elements of an iterable