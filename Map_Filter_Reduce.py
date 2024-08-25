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
#  If I 