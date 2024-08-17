# Code Introspection

# Code introspection is the ability to examine classes, functions and keywords to know
#  what they are, what they do and what they know

# Python provides several functions and utilities for code introspection

# help()
# # Launches the built-in help system in Python, providing an interactive interface for obtaining 
# # detailed information about modules, functions, classes, and objects. It's useful for quickly 
# # accessing documentation and understanding how to use different parts of Python's standard library.

# dir()
# # Returns a list of attributes and methods belonging to an object. This is useful for exploring 
# # the structure of an object, including its methods, properties, and inherited attributes, 
# # making it easier to understand what functionality is available.

# hasattr(object, name)
# # Checks if an object has an attribute with the specified name. It returns True if the attribute 
# # exists, and False otherwise. This is helpful when dynamically interacting with objects, 
# # ensuring that an attribute is present before attempting to use it.

# id(object)
# # Returns the unique identifier (memory address) of an object. This can be useful for comparing 
# # whether two variables reference the same object in memory, aiding in debugging and tracking 
# # object instances.

# type(object)
# # Returns the type of an object, indicating the class it belongs to. This is essential for 
# # understanding what kind of object you're working with, especially when dealing with generic or 
# # dynamically-typed code.

# repr(object)
# # Returns a string representation of an object that ideally can be used to recreate the object 
# # using eval(). This is useful for debugging, as it provides a more detailed and often unambiguous 
# # description of the object compared to str().

# callable(object)
# # Returns True if the object appears to be callable (i.e., it can be called like a function). 
# # This is helpful for verifying that an object can be invoked as a function before attempting to 
# # call it, avoiding potential runtime errors.

# issubclass(class, classinfo)
# # Returns True if the class is a subclass of the classinfo argument. It’s useful for verifying 
# # inheritance relationships, ensuring that one class is derived from another, which helps in 
# # enforcing or checking for expected behavior in class hierarchies.

# isinstance(object, classinfo)
# # Returns True if the object is an instance of the classinfo argument. This is commonly used to 
# # check an object's type before performing operations that require the object to be of a specific 
# # type, ensuring type safety in your code.

# __doc__
# # Contains the docstring of a function, class, or module, providing a brief description of its 
# # purpose and usage. Accessing this helps in quickly understanding what the object does without 
# # having to look at external documentation.

# __name__s
# # Contains the name of the object (typically a function, class, or module). This is useful in 
# # introspection to identify the name of an object programmatically, which can be helpful in 
# # debugging and logging.

# Exercise
# Print a list of all attributes of the given Vehicle object
# Use the help function to see what each function does.
# # Delete this when you are done.
# help(dir)
# help(hasattr)
# help(id)

# Define the Vehicle class.
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.
# Your code goes here
print(dir(Vehicle))
