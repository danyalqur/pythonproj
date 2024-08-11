# Multiple Function Arguments

# Every function in Python receives a predefined number of arguments, if declared normally, like this:

# def myfunction(first, second, third):
#     # do something with the 3 variabels
#     ...

# It is possible to declare functions which receive a variable number of arguments, using the following syntax:

# def foo(first, second, third, *therest):
#     print("First: %s" % first)
#     print("Second: %s" % second)
#     print("Third: %s" % third)
#     print("And all the rest... %s" % list(therest))

# The "therest" variable is a list of variables, which receives all arguments which were given to the "foo" function after the first 3 arguments. So calling
#  foo(1, 2, 3, 4, 5) will print out:

# foo(1, 2, 3, 4, 5)
# # -> First: 1
# #    Second: 2
# #    Third: 3
# #    Amd all the rest... [4, 5]

# It is also possible to send functions arguments by keyword, so that the order of the argument does not matter, using the following syntax. The following
#  code yields the following output: The sum is: 6 Result: 1

# def bar(first, second, third, **options): # keyNOTE notice the double star here
#     if options.get("action") == "sum": # get is a method for a dictionary that gives back a value related to the key given to it
#         print("the sum is: %d" % (first + second + third))
#
#     if options.get("number") == "first":
#         return first
#
# result = bar(1, 2, 3, action = "sum", number = "first") # Think of this as the 4th and 5th entries here are forming a dictionary with these two key value pairs
# print("Result: %d" % result)

# The "bar" function receives 3 arguments. If an additional "action" argument is received, and it instructs on summing up the first 3 numbers, then the sum is
#  printed out. If the value of the "number" parameter passed in the function is equal to "first", then the function also knows to return the first argument
#  most noteable of all this is that here the key in this dictionary-esque format is the "keyword" being referred to in the above notes. Also the use of the
#  double star when we want to use keywords

# Exercise
# Fill in the foo and bar functions so they can recieve a variable amount of arguments (3 or more). The foo function must return the amount of extra arguments
#  received. The bar must return True if the argument with the keyword magicnumber is worth 7, and False otherwise

# edit the funcitons prototype and implementation
def foo(a, b, c, *foorest):
    return(len(list(foorest)))

def bar(a, b, c, **barrest):
    if barrest.get("magicnumber") == 7:
        return True
    else:
        return False

# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber = 6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")