# Dictionaries.py
# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. 
#  Each value stored in a dictionary can be retrieved with its key, which is any type of object (a string, a number, a list, etc.) instead of using its
#  index to address it

# For example, a database of phone numbers could be stored using a dictionary like this:

# phonebook = {}
# phonebook["John"] = 938477566
# phonebook["Jack"] = 938377264
# phonebook["Jill"] = 947662781
# print(phonebook)
# # -> {'John': 938477566, 'Jack': 938377264, 'Jill': 947662781}
# #  it prints in the format- keyx : valuex, keyy : value y, ...

# Alternatively, a dictionary can be initialised with the same values in the following notation:

# phonebook = {
#     "John" : 938477566,
#     "Jack" : 938377264,
#     "Jill" : 947662781
# }
# print(phonebook)
# # -> {'John': 938477566, 'Jack': 938377264, 'Jill': 947662781}

# Iterating over dictionaries
# Dictionaries can be iterated over just like a list. However, a dictionary, unlike a list, does not keep the order of the values stored in it.
#  To iterate over key value pairs, use the following syntax:

# phonebook = { "John" : 938477566, "Jack" : 938377264, "Jill" : 947662781}
# for name, number in phonebook.items():
#     print("Phone number of %s is %d" % (name, number))
# # -> Phone number of John is 938477566
# #    Phone number of Jack is 938377264
# #    Phone number of Jill is 947662781
# # Note: can see that name, number which are representing key and value are used in the for loop with the comma between. dictionary.items() is where the 
# #  retrieving occurs

# Removing items from a dictionary
# To removed a specified key value pair / "specified index" (as referred to in the notes), use one of the following two notations

# phonebook = {
#    "John" : 938477566,
#    "Jack" : 938377264,
#    "Jill" : 947662781
# }
# del phonebook["John"]
# print(phonebook)
#
####   OR
#
# phonebook = {
#    "John" : 938477566,
#    "Jack" : 938377264,
#    "Jill" : 947662781
# }
# phonebook.pop("John")
# print(phonebook)
    
# Exercise
# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# your code goes here
phonebook["Jake"] = 938273443
phonebook.pop("Jill")
# Or
# del phonebook["Jill"]

phonebook["Jake"] = 938273443
phonebook.pop("Jill")
# Or
# del phonebook["Jill"]