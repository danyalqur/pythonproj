# Modules and packages
# In programming, a module is a piece of software that has a specific functionality.
#  For example, when building a ping pong gmae, one module may be responsible for the game logic, and another module draws the game on the screen.
#  Each module consists of a different file, which may be edited separately

# Writing modules
# Modules in Python are just Python files with .py extension. The name of the module is the same as the file name. A Python module can have a set of functions,
#  classes, or variables defined and implemented. The following example includes two files
#  1. mygame/game.py
#  2. mygame/draw.py
#  The Python script game.py implements the game. It uses the function draw_game from the file draw.py, or in other words. the draw module that implements the 
#  logic for drawing the game on the screen

#  Modules are imported from other modules using the import command. In the following example, the game.py script may look something like this:

# # game.py
# # import the draw module
# import draw
#
# def play_game():
#     ...
#
# def main():
#     result = play_game()
#     draw.draw_game(result)
#
# if __name__ == '__main__' # this means that if this script is executed, then main() will be executed
#     main()
# # This script does not run

# The draw module may look something like this:

# # draw.py
# def draw_game():
#     ...
#
# def clear_screen(screen):
#     ...
# # This script does not run either

# In this example, the game module imports the draw module, which enables it to use functions implemented in that module.

# Notes, in the form of a diagram: 
#  game.py [module]
#   |
#   v
#  draw.py [module] (holds functions that game.py wants to use)

#  The main function uses the local function play_game to run the game, and then draws the result of the game using a function implemented in the draw module 
#  called draw_game. To use the function draw_game from the draw module, we need to specify in which module the function is implemented, using the dot operator
#  to reference the draw_game function from the game and then call draw.draw_game() because draw.py is the module

# When the import draw directive runs, the Python interpreter looks for a file in the directory in which the script (here game.py) was executed with the 
#  module name and a .py suffix (here draw.py). If it is found, it will be imported. If it is not found, it will continue looking for built-in modules.

# When importing a module, a .pyc file is created. This is a compiled Python file. Python compiles files into Python bytecode so that it won't have to parse
#  files each time modules are loaded. If a .pyc file exists, it gets loaded instead of the .py file. This process is transparent to the user.

# Importing module objects to the current namespace
# A namespace is a system where every object is named and can be access in Python. We import the function draw_game into the main script's namespace by using
#  the from command.

# # game.py
# # import the draw module
# from draw import draw_game
#
# def main():
#     result = play_game()
#     draw_game(result)
# # This script does not run either

# In this example, the name of the module does not precede draw_game, nor is the dot operator present. This is because we specified the module name using the
#  import command

# The advantages of this notaties is that you don't have to reference the module over and over. However, a namespave cannot have two objects with the same
#  name, so the import command may replace an existing object in the namespace

# Importing all objects from a module
# You can use the import * command to import all the objects in module. For example:

# # game.py
# # import the draw module
# from draw import *
#
# def main():
#     result = play_game()
#     draw_game(result)

# This might be a bit risky as changes in the module may affect the module which imports it, but it is shorter and doesnt require you to specify every object
#  you want to import form the module

# Custom import name
# Modules may be loaded under any name you want. This is useful when importing a module conditionally to use the same name in the rest of the code.

# For example, if you have two draw odules with slightly different names, you may do the following:

# # game.py
# # import the draw module
# if visual_mode
#     # in visual mode, we draw using graphics
#     import draw_visual as draw
# else:
#     # in textual mode, we print out text
#     import draw_textual as draw
#
# def main():
#     result = play_game()
#     draw.draw_game(result) # This can either be visual or textual depending on the visual_mode

# Module initialization
# The first time a module is loaded into a Python script, it is initialized be executing the code in the module once. If another module in your code imports
#  the same module again, it will not be loaded again, so local variables inside the module act as a 'singleton'
#  this means they are initialized only once
    
# You can use this to initialize objects, for example:

# # draw.py
# def draw_game():
#     # when clearing the screen we can us the main screen object intialized in this module
#     clear_screen(main_screen)
#     ...
#
# def clear_screen(screen):
#     ...
#
# class Screen():
#     ...

# # initialize main_screen as a singleton
# main_screen = Screen() # we have initialized this, meaning we created an object from a class but we have not yet set any variables or called any functions

# Extending module load path
# There are a couple of ways to tell the Python interpreter where to look for modules, aside from the defualt local directory and built-in modules.
#  You can use the environment variable PYTHONPATH to specify additional directories to look for modules like this:

# PYTHONPATH =/foo python game.py

# This executes game.py, and enables the script to load modules from the foo directory, as well as the local directory.

# You may also use the sys.path.append function. Execute it before running the import command:

# sys.path.append("/foo") # Now the foo directory bas been added to the list of paths where modules are looked for. 

# Exploring built in modules
# Two very important funcitons come in handy when exploring modules in Python - the dir and help functions.

# Example: To import the module, urllib which enables us to create read data from URLs, we import the module:

# # import the library
# import urllib
#
# # use it
# urllib.urlopen(...}

# We can look for which functions are implemented in each module using the dir function: (try this in the python terminal)
# >>> import urllib
# >>> dir(urllib)


