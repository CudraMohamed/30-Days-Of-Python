language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) 

#pass is used to override the expected when condition after the semicolon

#Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
for num in range(0,10+1):
    print(num)

numb=0
while numb <10+1:
    print(numb)
    numb+=1

# Iterate 10 to 0 using for loop, do the same using while loop.

for number in range(10,0,-1):
    print(number)           #can not print 0 because arguments in range must not be zero

numbers=10
while numbers<0:
    print(numbers)
    numbers-=1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:


#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
# humans="Helloyouall"
# for x in humans:
#            print(humans)

# Use nested loops to create the following:
# y=["you","lol"]
# for x in y:
#     for t in x:
#         print(t)

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for number in range(10+1):
        results=number**2
        if number ==0:
            print(f" 0 x 0 = {results}",end="")
        elif number ==1:
            print(f"1 x 1 = {results}",end="")
        elif number ==2:
            print(f"2 x 2 = {results}",end="")
        elif number ==3:
            print(f"3 x 3 = {results}",end="")
        elif number ==4:
            print(f"4 x 4 = {results}",end="")
        elif number ==5:
            print(f"5 x 5 = {results}",end="")
        elif number ==6:
            print(f"6 x 6 = {results}",end="")
        elif number ==7:
            print(f"7 x 7 = {results}",end="")
        elif number ==8:
            print(f"8 x 8 = {results}",end="")
        elif number ==9:
            print(f"9 x 9 = {results}",end="")
        else:
            number ==10
            print(f"10 x 10 = {results}",end="")
        print("\n")

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
skills=['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in skills:
    print(skill)
# Use for loop to iterate from 0 to 100 and print only even numbers
for a_number in range(0,100+1):
    if a_number %2==0:
        print(a_number)
# Use for loop to iterate from 0 to 100 and print only odd numbers
for b_number in range(0,100+1):
    if b_number %2 !=0:
        print(b_number)
# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.

    
    

# The sum of all numbers is 5050.
# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

# The sum of all evens is 2550. And the sum of all odds is 2500.
# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world