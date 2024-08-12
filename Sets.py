# Sets

# Sets are lists with no duplicate entries. Let's say you want to collect a list of  words used in a paragraph:

# print(set("my name is Eric and Eric is my name".split()))
# # -> {'is', 'Eric', 'and', 'name', 'my'}

# Since some of the words are repeated twice, they are already in the set and so are not inserted twice

# Sets are a powerful tool in Python since they have the ability to calculate differences and intersections between other sets. For example, say you have a list
#  of participants in events A and B:

# a = set(["Jake", "John", "Eric"])
# print(a)
# b = set(["John", "Jill"])
# print(b)

# To find out which members attended both events, you may use the "intersection" method:

# a = set(["Jake", "John", "Eric"])
# b = set(["John", "Jill"])
# print(a.intersection(b))
# print(b.intersection(a))
# # -> {'John'}
# #    {'John'}

# To find out which members attended only one of the events, use the "symmetric_difference" method:

# a = set(["Jake", "John", "Eric"])
# b = set(["John", "Jill"])
# print(a.symmetric_difference(b))
# print(b.symmetric_difference(a))
# # -> {'Jake', 'Eric', 'Jill'}
# #    {'Eric', 'Jake', 'Jill'}

# To find out which members attended the given event and not the other, use the "difference" method (given.difference(other)):

# a = set(["Jake", "John", "Eric"])
# b = set(["John", "Jill"])
# print(a.difference(b))
# print(b.difference(a))
# # -> {'Eric', 'Jake'}
# #    {'Jill'}

# To receive a list of all participants use the "union" method

# a = set(["Jake", "John", "Eric"])
# b = set(["John", "Jill"])
# print(a.union(b)) 
# # -> {'Jake', 'John', 'Jill', 'Eric'}
# # Note that we are working with sets so 'John' does not appear twice

# Exercise
# Use the given lists to print out a set containing all the participants from event A which did not attend B.

a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

# Your code goes here
aset = set(a)
bset = set(b)
print(aset.difference(bset))

# Note: Don't forget that these methods work with sets, not lists, so  you have to turn these lists into sets with the set() class


