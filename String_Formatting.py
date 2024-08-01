#String_Formatting.py

#Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), 
# together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d". Let's say you have a variable 
# called "name" with your user name in it, and you would then like to print(out a greeting to that user.): name = "John" print("Hello, %s!" % name)  -> Hello, John!

#To use two or more argument specifiers, use a tuple (parentheses): 
# name = "John"  
# age = 23  
# print("%s is %d years old." % (name, age))  
# -> John is 23 years old.

#Any object which is not a string can be formatted using the %s operator as well. The string which returns from the "repr" method of that object is formatted 
# as the string. For example: 
# mylist = [1,2,3]  
# print("A list: %s" % mylist)  
# -> A list is: [1,2,3]
# Think of this as turning the thing into a string

#Here are some basic argument specifiers you should know:
# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)

# Exercise 1
# You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

# Further notes
# tuples such as the data presented in the problem are fixed indexed from 0 and the individual item can be called as followed: data = ("John", "doe")  print(data[0])  -> "John"
#
# My first attempt looked like this 
# data = ("John", "Doe", 53.44)
# format_string = "Hello"
# print(format_string + " %s %s. Your current balance is $%s." % (data[0], data[1], data[3]))
# 
# This is incorrect because of the following note: The string which you make can have argument specifiers that can be specified in the print statement
# So the string can look like this 
# format_string = "Hello %s %s. Your current balance is $%s."
# and the print can look like this
# print(format_string % data)
# The python compiler just knows to use each tuple element in the place of the argument specifiers sequentially down the list

#Basic String Operations
# Strings are bits of text. They can be defined as anything between quotes: 
# astring = "Hello world!" 
# astring2 = 'Hello world!'

# As you can see, the first thing you learned was printing a simple sentence. This sentence was stored by Python as a string. 
# However, instead of immediately printing strings out, we will explore the various things you can do to them. 
# You can also use single quotes to assign a string. However, you will face problems if the value to be assigned itself contains single quotes. 
# For example to assign the string in these bracket(single quotes are ' ') you need to use double quotes only like this:

# astring = "Hello world!"
# print("single quotes are ' '")
# print(len(astring))
# -> single quotes are ' '
#    12

# That prints out 12, because "Hello world!" is 12 characters long, including punctuation and spaces.

# astring = "Hello world!"
# print(astring.index("o"))
# -> 4
# That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character. 
# Notice how there are actually two o's in the phrase - this method only recognizes the first.
# Python (and most other programming languages) start things at 0 instead of 1. So the index of "o" is 4.

# astring = "Hello world!"
# print(astring.count("l"))
# -> 3
# that is a lowercase L, not a number one. This counts the number of l's in the string. Therefore, it should print 3.

# astring = "Hello world!"
# print(astring[3:7])
# -> lo w
# This prints a slice of the string, starting at index 3, and ending at index 6. But why 6 and not 7? Again, most programming languages do this - 
# it makes doing math inside those brackets easier.
# If you just have one number in the brackets, it will give you the single character at that index. If you leave out the first number but keep the colon, 
#  it will give you a slice from the start to the number you left in. If you leave out the second number, it will give you a slice from the first number to the end.
# You can even put negative numbers inside the brackets. They are an easy way of starting at the end of the string instead of the beginning. 
#  This way, -3 means "3rd character from the end".

# astring = "Hello world!"
# print(astring[3:7:2])
# -> l   #(that is l then a whitespace, but the whitespace is ignored)
# This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step].

# astring = "Hello world!"
# print(astring[3:7])
# print(astring[3:7:1])
# Note that both of them produce same output

# There is no function like strrev in C to reverse a string. But with the above mentioned type of slice syntax you can easily reverse a string like this
# astring = "Hello world!"
# print(astring[::-1])
# -> !dlrow olleH

# These make a new string with all letters converted to uppercase and lowercase, respectively.
# astring = "Hello world!"
# print(astring.upper())
# print(astring.lower())
# -> HELLO WORLD!
#    hello world!

# The following is used to determine whether the string starts with something or ends with something, respectively. 
# The first one will print True, as the string starts with "Hello". 
# The second one will print False, as the string certainly does not end with "asdfasdfasdf".
# astring = "Hello world!"
# print(astring.startswith("Hello"))
# print(astring.endswith("asdfasdfasdf"))
# -> True
#    False

# The following splits the string into a bunch of strings grouped together in a list. Since this example splits at a space, the first item in the list will be "Hello", and the second will be "world!".
# astring = "Hello world!"
# afewwords = astring.split(" ")
# print(afewwords[0])
# print(afewwords[1])
# -> Hello
#    World!
# syntax of this is that whatever is in the double quotes is what is used to split the string


# Exercise 2

# Try to fix the code to print out the correct information by changing the string.

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

# Notes
# in python strings are immutable so you need to create a new string if you are trying to reconstruct it around any input parameter
# for example you can't remove a letter from an index, instead you must make a new string which skips that letter and add concatenate the new letter in