#Sets- Unordered,un-indexed elements
#creating an empty list
from typing import OrderedDict
from unittest.util import unorderable_list_difference


my_set  =set()
print(my_set)
my_set2={}
print(my_set2)

her_set={'doll','cat','light','oil'}
print(len(her_set))     #length of the set

print('wig' in her_set)
print('cat' in her_set)     #checking items in the set

her_set.add('money')
print(her_set)      #adding items in the set

her_set.update(['pen','ruler','eraser','compass'])
print(her_set)      #adding items using update which takes in  a list of items

her_set.remove('light')
print(her_set)      #removing items using .remove() method

her_set.pop()
print(her_set)      #.pop() removes the first item in a set

her_set.clear()
print(her_set)      #removing all the items from the set

del her_set
# print(her_set)      #deleteing the who;e definition of set

#set does not accept duplicate input
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
print(set(fruits))      #converting list to set

vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
new_fruits = {'banana', 'orange', 'mango', 'lemon','orange', 'banana'}
print(vegetables.union(new_fruits))     #joining sets using .union()

vegetables.update(new_fruits)
print(vegetables)       #joining using update() method

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
intercept=whole_numbers.intersection(even_numbers) 
print(intercept)                #printing all the numbers that are present in both sets

superset=whole_numbers.issuperset(even_numbers)
print(superset)     #superset
subset=even_numbers.issubset(whole_numbers)
print(subset)       #subset

diff=whole_numbers.difference(even_numbers)
print(diff)     #checking the difference between th two sets

symmetric=whole_numbers.symmetric_difference(even_numbers)
print(symmetric)        #returns items that are not in both sets mathematically

disjoint= whole_numbers.isdisjoint(even_numbers)
print(disjoint)     #prints true if sets don't have any common number

# EXERCISE
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Level 1
# Find the length of the set it_companies
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Meta','Cellulant','Sendy'])
print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.remove('Meta')
print(it_companies)
# What is the difference between remove and discard
#The remove item will output an error if the specified item is not there while discard does not

# Exercises: Level 2
# Join A and B
print(A.union(B))
# Find A intersection B
print(A.intersection(B))
# Is A subset of B
print(A.issubset(B))
# Are A and B disjoint sets
print(A.isdisjoint(B))
# Join A with B and B with A
print(A.union(B))
print(B.union(A))
# What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# Delete the sets completely
del A
del B
# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_copy = set(age)
print(age_copy)
print(len(age),(len(age_copy)))
# Explain the difference between the following data types: string, list, tuple and set
#A string is an array that take either one or more unicode
# A list takes in different data types and it is ordered
# Tuple takes in different data types and it is unordered and allows duplicates
# Set takes in different data types but does not allow duplication of items
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
word = 'I am a teacher and I love to inspire and teach people.'
splitting = word.split()
print(splitting)
print(len(splitting))