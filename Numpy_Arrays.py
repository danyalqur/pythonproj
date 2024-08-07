# Numpy Arrays

# Getting Started
# Numpy arrays are a great alternative to Python Lists. Some of the key advantages of Numpy arrays are that:
#  1. they are fast
#  2. easy to work with
#  3. give users the opportunity to perform calculations across entire arrays

# In the following example, you will create two Python lists. Then, you will import the numpy package and create numpy arrays out of the newly created lists.

# # Create 2 new lists: height and weight
# height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
# weight = [81.65, 97.52, 95.25, 92.68, 86.18, 88.45]
# #
# # Import the numpy packacge as np
# import numpy as np
# #
# np_height = np.array(height)
# np_weight = np.array(weight)
# #
# print(np_height)
# print(np_weight)
# print(height)
# print(weight)
# # both print out the same thing
# print(type(np_height)) # Showing the change in type from list to numpy array 
# # -> <class 'numpy.ndarray'>
 
# Element-wise calculations
# Now we can perform element-wise calculations on height and weight. For example, you could take all 6 of the height and weight observations above and
#  use them to calculate BMI in a single equation. This operation will be fast and computationally efficient in comparison to the use of nested loops.
#  They are particularly helpful as your data set size increases and you have lets say 1000 calculations to make

# # Calcuate BMI
# bmi = np_weight / np_height ** 2
# # Print the result
# print(bmi)

# Subsetting
# Another great feature of Numpy arrays is the ability to subset. For instance, if you wanted to know which observations in our BMI array are above 23,
#  we could quickly subset it to find out

# # For a a boolean response
# print(bmi > 23)
# # Print only those observations above 23
# print(bmi[bmi > 24])

# Note: so subsetting basically means introducing conditionals to the data to remove certain data or find out about data in the dataset

# Exercise
# First, convert the list of weights from a list to a Numpy array. Then, convert all of the weights from kilograms to pounds. Use the scalar conversion
# of 2.2 lbs per kilogram to make your conversion. Lastly, print the resulting array of weights in pounds.

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg

np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg

np_weight_lbs = np_weight_kg * 2.2

# Print out np_weigh_lbs

print(np_weight_lbs)

