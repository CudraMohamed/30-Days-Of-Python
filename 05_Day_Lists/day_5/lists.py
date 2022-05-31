#Creating lists
empty_list=list()       #using inbuilt function
print(len(empty_list))

empty_list=[]
print(len(empty_list))       #using squre brackets

fruits= ['Mango','Banana','Apple','Guava','Watermelon']
print(fruits)
print(len(fruits))      #Length of a list

different_data_types=['Cudra',30,True,30.55,'nice123',{'name':'Cudra','language':'Python'}] #a list can have different data types
print(different_data_types)

#Accessing items in a list using indexing
print(fruits[0])
print(fruits[-1])

#Unpacking list items
fruits= ['Mango','Banana','Apple','Guava','Watermelon']
item1,item2,item3,*rest=fruits
print(item1)
print(item2)
print(item3)
print(rest)

#slicing items from a list
all_fruits=fruits[0:]
print(all_fruits)

every_2nd=fruits[::2]     #takes every second item
print(every_2nd)

reverse_items=fruits[::-1]      #reverse the list
print(reverse_items)

#Modifying lists
fruits[0]='Avocado'     #changes the 1st index to avocado
print(fruits)

last_index=len(fruits)-1        #accessing the last index using len
fruits[last_index]='lime'
print(fruits)

#Checking items in a list
existing='Banana' in fruits
print(existing)

#adding items at the end of the list
fruits.append('Grapes')
print(fruits)

#Inserting items into a list
fruits.insert(2,'lemon')
print(fruits)

#Removing items from a list
fruits.remove('lemon')
print(fruits)

fruits.pop(0)
print(fruits)

del fruits[1]
print(fruits)

fruits.clear()      #emptying a list
print(fruits)

#copying a list
fruit= ['Mango','Banana','Apple','Guava','Watermelon']
fruit_copy=fruit.copy()
print(fruit_copy)

#joining lists
vegetables=['Tomatoe','Cabbage','Carrots','onion']
print(fruit+vegetables)

fruit.extend(vegetables)
print(fruit)

print(fruit.count('Banana'))  #Counting items

#finding index of an item
print(fruit.index('Apple'))

#Reversing a list
fruit.reverse()
print(fruit)

#Sorting list items
fruit.sort()                    #sorting in ascending order
print(fruit)
fruit.sort(reverse=True)        #sorting in descending order
print(fruit)

print(sorted(fruit))            #sorts the list without modifying the original list
fruitss=sorted(fruit,reverse=True)
print(fruitss)

#Lists Exercise
# Exercises: Level 1
# Declare an empty list
empty_list = []
print(empty_list)
empty_list2 = list()
print(empty_list2)
# Declare a list with more than 5 items
cars = ["Jeep","Porsche","Audi","Nissan","Toyota","Mercedes Benz"]
print(cars)
# Find the length of your list
print(len(cars))
# Get the first item, the middle item and the last item of the list
print(cars[0],cars[3],cars[-1])
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Cudra',30,54,'single','Ke 60-001']
print(mixed_data_types)
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print(it_companies[0],it_companies[3],it_companies[-1])
# Print the list after modifying one of the companies
it_companies[0] = 'HCL Technologies'
print(it_companies)
# Add an IT company to it_companies
it_companies.append('Oracle')
print(it_companies)
# Insert an IT company in the middle of the companies list
it_companies.insert(3,"Tech Mahindra")
print(it_companies)
# Change one of the it_companies names to uppercase (IBM excluded!)
companies_upper=[company.upper() for company in it_companies]
print(companies_upper)
# Join the it_companies with a string '#;  '
joined_list='#'.join(it_companies)
print(joined_list)
# Check if a certain company exists in the it_companies list.
in_list="iHub" in it_companies
print(in_list)
# Sort the list using sort() method
companies=['HCL Technologies', 'Google', 'Microsoft', 'Tech Mahindra', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Oracle']
companies.sort()
print(companies)
# Reverse the list in descending order using reverse() method
companies.reverse()
print(companies)
# Slice out the last 3 companies from the list
del companies[0:2]
print(companies)
# Slice out the middle IT company or companies from the list
print(companies.pop(4))
# Remove the first IT company from the list
print(companies.pop(0))
# Remove the middle IT company or companies from the list
print(companies.pop(2))
# Remove the last IT company from the list
print(companies.pop())
# Remove all IT companies from the list
print(companies.clear())
print(companies)
# Destroy the IT companies list
del companies
# print(companies)
# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
fullstack = front_end+(back_end)
print(fullstack)
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack=fullstack
print(full_stack)
# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
print(ages)
print(min(ages))
# Add the min age and the max age again to the list
# print(ages.append(min(ages) and max(ages)))
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method
# Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
# Slice out the first 3 companies from the list
