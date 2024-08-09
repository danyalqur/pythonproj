# Pandas Basics

# Pandas DataFrames
# Pandas is a high-level data manipulation tool developed by Wes McKinney. It is built on the Numpy package and its key data structure is called the DateFrame.
#  Dataframes allow you to store and manipulate tabular data in rows of observations and columns of variables.

# There are several ways to create a DataFrane. One way is to use a dictionary. For example:

import pandas as pd

# dict = {
#     "country" : ["Brazil", "Russia", "India", "China", "South Africa"], 
#     "capital" : ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
#     "area"    : [8.516, 17.10, 3.286, 9.597, 1.221],
#     "population" : [200.4, 143.5, 1252, 1357, 52.98]
#         }
# brics = pd.DataFrame(dict)
# print(brics)
# # ->
# #               country    capital    area  population
# #       0        Brazil   Brasilia   8.516      200.40
# #       1        Russia     Moscow  17.100      143.50
# #       2         India  New Delhi   3.286     1252.00
# #       3         China    Beijing   9.597     1357.00
# #       4  South Africa   Pretoria   1.221       52.98
# #
# print("data type of dict is %s" % (type(dict)))
# # -> <class 'dict'>
# print("data type of brics is %s" % (type(brics)))
# # -> <class 'pandas.core.frame.DataFrame'>

# In the new brics DataFrame, Pandas has assigned a key for each country as the numerical values 0 through to 4. If you would like to have different index
#  values, say the two letter country code, you can easily change the index as so:

# # Set the index for brics
# brics.index = ["BR", "RU", "IN", "CH", "SA"]
# #
# # Print out brics with new index values
# print(brics)

# Another way to create a DataFrame is by importing a csv file using Pandas. Now the csv cars.csv can be imported using the pandas method pd.read_csv():

# Read and print cars
# cars = pd.read_csv('cars.csv')
# print(cars)

# Indexing DataFrames (generating pandas series and pandas DataFrames from DataFrames)
# There are several ways to index a Pandas DataFrame. One of the easiest ways to do this is by using square bracket notation.

# In the example below, you can use square brackets to select one of the columns of the cars DataFrame. You can either use:
#   1. A single bracket
#       -> The single bracket will output a Pandas Series
#   2. A double bracket
#       -> The double bracket will output a Pandas DataFrame

# import cars.csv as a DataFrame
cars = pd.read_csv('cars.csv', index_col = 0) # Setting as index means that we have got rid of the default index (0, 1, 2, ...) and used one of our columns 
#  as the index
#
# Print out cars_per_cap column as Pandas series
print(cars['cars_per_cap'])
print("datatype is %s \n \n" % (type(cars['cars_per_cap'])))
#
# Print our cars_per_cap column as Pandas DataFrame
print(cars[['cars_per_cap']])
print("datatype is %s \n \n" % (type(cars[['cars_per_cap']])))
#
# Print our DataFrame with cars_per_cap and country columns
print(cars[['cars_per_cap', 'country']]) 

# Note: The last command is only possible by creating a Pandas DataFrame, you can not make a Pandas Series that is multiple columns. Therefore only double
#  brackets can be used here

# Square brackets can also be used to access observations (rows) from a DataFrame. For example:

# Print out first four observations
print(cars[0:4])
#
# Print out fifth and sixth observations
print(cars[4:6])

# Using loc and iloc
# You can use loc and iloc to perform just about any data selection operation. loc is local-based, which means that you have to specify rows and columns 
#  based on their row and column labels. iloc is integer index based, so you have to specify rows and columns by their integer index like in the previous 
#  exercise

# Print out observation for Japan
print(cars.iloc[2]) # One square bracket for Pandas Series
# -> prints the row 2 of cars (indexed from 0, so really the third row in the chart)
#
# Print out observations for Russia and Morroco
print(cars.loc[['RU', 'MOR']]) # Two square brackets for Pandas DataFrame