# Classes and Objects

# Objects are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes.
# Classes are essentially a template to create your object

# A very basic class would look something like this

# class MyClass:
#     variable = "blah"
#
#     def function(self): # The reason for this self being included as a parameter will be explained later
#         print("This is a message inside the class")

# First, to assign the above class (template) to an object you would do the following:

# class MyClass:
#     variable = "blah"
#
#     def function(self):
#         print("This is a message inside the class.")
#
# myobjectx = MyClass()

# Now the varible "myobjectx" holds an object of the class "MyClass" that contains the variable and the function defined within the class called "MyClass"

# Accessing Object Variables
# To access the variable inside of the newly created object "myobjectx" you would do the following:

# class MyClass:
#     variable = "blah"
#
#     def function(self):
#         print("This is a message inside the class.")
#
# myobjectx = MyClass()

# myobjectx.variable #This does not do anythingbesides put a "blah here"

# The below would output the string blah

# class MyClass:
#     variable = "blah"
#
#     def function(self):
#         print("This is a message inside the class.")
#
# myobjectx = MyClass()
#
# print (myobjectx.variable)

# You can create multiple different objects that are the same class (have the same variables and functions defined). However, each object contains independent
#  copies of the variables defined in the class. For instance, if we were to define another object with the "MyClass" class and then change the string in the 
#  variable above:

# class MyClass:
#     variable = "blah"
#
#     def function(self):
#         print("This is a message inside the class.")
#
# myobjectx = MyClass()
# myobjecty = MyClass()
#
# myobjecty.variable = "yackity"
#
# print(myobjectx.variable)
# print(myobjecty.variable)
# #  -> one prints blah the other prints yackity

# Accessing Object Functions
# To access a function inside of an object you use a notation similar to accessing a variable:

# class MyClass:
#     variable = "blah"
#
#     def function(self):
#         print("This is a message inside the class.")
#
# myobjectx = MyClass()
#
# myobjectx.function() 
# # -> This will print out the message "This is a message inside the class."

# init()
# The __init__() function is a special function that is called when the class is being initiated. It's used for assigning values in a class.

# class NumberHolder:
#
#     def __init__(self, number):
#         self.number = number # Here the init is arranging things to assign a value to self.number which is number which is passed when the object is made
#
#     def returnNumber(self):
#         return self.number
#
# var = NumberHolder(7)
# print(var.returnNumber())
# #  -> prints 7

# Exercise
# We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60000.00 with a name of Fer
#  and car2 to be a blue van named Jump worth $10000.00

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    
car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())
