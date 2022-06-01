#Tuples-ordered and unchangable(immutable)
#Methods related to tuple() include - 
# tuple()-creating an empty list 
# count() - count the numbers of a specified item in a tuple 
# index() - find the index of a specified item in a tuple
# > operator to join two or more tuples and to create a new tuple

empty_tuple = ()        #creating an empty tuple
print(empty_tuple)
empty_tuple2 = tuple()
print(empty_tuple2)

fruits = ('Banana','Mango','Apple','Guava','Pineapple')     #tuple with initial values
print(fruits)

print(len(fruits))      #a method to get the length of a tuple

first_item = fruits[0]      #Accessing items using Indexing
print(first_item)
print(fruits[-1])           #accessing using negative indexing

two_items = fruits[0:2]     #slicing tuples using positive index range
print(two_items)

three_items = fruits[-4:-1]       #negative range indexes
print(three_items)

to_list = list(fruits)      #changing a tuple to list
print(to_list)

print(tuple(fruits))        #back to tuple

print('Orange' in fruits)       #Checking an item in tuple
print('Banana' in fruits)

vegies = ('Cabbage','Kales','Tomato')
fruits_and_vegies = fruits + vegies     #Joining Tuples
print(fruits_and_vegies)

del vegies              #deleting a tuple
# print(vegies)           #to check if vegies is there, outputs an error that name is not defined

#Tuple Exercise
#Exercises: Level 1
# Create an empty tuple
empty = ()
print(empty)
empty2 = tuple()
print(empty2)
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
my_brothers=('Ash','Lash','Nur','Din')
print(my_brothers)
my_sisters = ('Tina','Nana','Dasha','Masha')
print(my_sisters)
# Join brothers and sisters tuples and assign it to siblings
my_siblings = my_brothers + my_sisters
print(my_siblings)
# How many siblings do you have?
print(len(my_siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
tuple_to_list = list(my_siblings)
print(tuple_to_list)
my_parents = ['Mama','Baba']
print(tuple(my_parents))
my_family = tuple_to_list + my_parents
print(tuple(my_family))
# Exercises: Level 2
# Unpack siblings and parents from family_members
siblings=my_family[0:8]
print(siblings)
parents = my_family[-2:]
print(parents)
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Banana','Mango','Apple','Guava','Pineapple') 
vegies = ('Cabbage','Kales','Tomato')
animals = ('Cow','Lion','Giraffe','Elephant')
food_stuff_tp = fruits + vegies + animals
print(food_stuff_tp)
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt_list = list(food_stuff_tp)
print(food_stuff_lt_list)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
slicing_middle_items = food_stuff_lt_list[5:7]
print(slicing_middle_items)
# Slice out the first three items and the last three items from food_staff_lt list
slicing_the_first_three = food_stuff_lt_list[0:3]
print(slicing_the_first_three)
# Delete the food_staff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)