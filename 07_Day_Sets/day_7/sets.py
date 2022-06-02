#Sets- Unordered,un-indexed elements
#creating an empty list
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