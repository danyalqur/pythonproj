# List Comprehensions

# List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single readable line.

# For example, let's saw we need to create a list of integeres which specify the length of each word in a certain sentence but only if the word is not the
# word "the"

# # The long way
# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_lengths = []
# for word in words:
#     if word != "the":
#         word_lengths.append(len(word))
# print(words)
# print(word_lengths)

# Using a list comprehension, we could simplify this process to this notation:
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split() # This makes a list for us
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

# Exercise
# Using a list comprehension, create a new list called "newlist" out of the list "numbers", which contains only the positive numbers from the list, as integers
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [round(number) for number in numbers if number > 0]
print(newlist)