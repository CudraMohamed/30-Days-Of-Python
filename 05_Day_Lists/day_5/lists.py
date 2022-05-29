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