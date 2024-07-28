# Functions
# What are Functions
# Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save our time.
# Also functions are a key way to define interfaces so programmes can share their code

# How do you write functions in Python?
# As we have seen ion previous tutorials, Python makes us of blocks.
# A block is an area of code written in the format of:

## This is not executable code btw
# block_head:
#     1st block line
#     2nd block line
#     ...

#  Where a block line is more Python code (even another block), and the block head is of the following format: block_keyword block_name(argument1, argument2,...)
#  Block keywords you already know are "if", "for", and "while".

# Functions in python are defined using the block keyword "def", followed with the function's name as the block's name. For example:

# def my_function(): #function definition
#     print("hello from my function!")

# my_function()

# Functions may also recieve arguments (variables passed from the caller to the function). For example:

# def my_function_with_args(username, greeting):
#     print("Hello %s, from My_Function! I wish you %s" % (username, greeting))

# my_function_with_args("Danyal", "A happy sunday morning!")


