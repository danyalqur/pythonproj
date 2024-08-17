# Serialization 
                                                                                                                 
# Python provides built-in JSON libraries to encode and decode JSON
# in Python 2.5, the simplejson module is used, whereas in Python 2.7, the json module is used. We are gonna try the json module with this Python 3.11 dist

# import json

# There are two basic formats for JSON data:
#   1. a string 
#   2. the object datastructure

# In Python, the object datastructure consists of lists and dictionaries nested inside each other. The object datastructure allows one to use Python methods
#  (for lists, and dictionaries) to add, list, search and, remove elements from the datastructure. The String format is mainly used to pass the data into 
#  another program or load into a datastructure.

# To load JSON back to a data structure, use the "loads" method. This method takes a string and turns it back into the json object datastructure.

# print(json.loads(json_string))
# # -> json_string dont exist my g

# To encode a datastructure to JSON, use the "dumps" method. This method takes an object and returns a String:

# import json
# json_string = json.dumps([1, 2, 3, "a", "b", "c"])
# print(json_string)
# # -> [1, 2, 3, "a", "b", "c"]

# Note:
#       (json) ---> [LOADS METHOD] ---> (datastructure)
#       HERE YOU WILL APPLY THE DICTIONARY OR LIST METHODS TO ADD IN NEW 
#       (datastructure / object) ---> [DUMPS METHOD] ---> (string / JSON)

# Python supports a Python proprietary data serialization method called pickle (also a faster alternative exists called cPickle). They can be used the same way

# import pickle
# pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
# print(pickle.loads(pickled_string))
# # -> [1, 2, 3, "a", "b", "c"]

# Exercise

import json

# fix this function, so it adds the given name and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here
    salaries_json = json.loads(salaries_json) # Turning the json to a datastructure
    salaries_json[name] = salary # Applying a dictionary method
    salaries_json = json.dumps(salaries_json) # Turning the datastructure back to a JSON
    return salaries_json

salaries = '{"Alfred" : 300, "Jane" : 400}'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
