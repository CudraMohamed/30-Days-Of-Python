#Conditional execution - a block of one or more statements will be executed if a certain expression is true
#Repetitive execution- a block or more statement will be repetitively executed as long as a certain expression is true
#If condition - checks if condition is true


a=3
if a >0:
    print('A is a positive number')
#if else
a=3
if a<0:
    print('A is a negative number')
else:
    print('A is a positive number')
#if elif else
a=0
if a >0:
    print('A is a positive number')
elif a<0:
    print("A is a negative number")
else:
    print('A is zero')

#Short Hand
a=3
print('A is positive') if a>0 else print('A is negative')

#Nested Conditions
a=0
if a>0:
    if a % 2 ==0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a==0:
    print('A is zero')
else:
    print('A is a negative number')

#If condition and logical Operators
a=0
if a > 0 and a % 2 == 0:
    print('A is an even and positive number')
elif a > 0 and a % 2 != 0:
    print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

#If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >=4:
    print('Access granted')
else:
    print('Access denied')

#Exercise
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback:
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

age = int(input("Enter your age: "))
if age >= 18:
    print('You are old enough to learn to drive')
elif age <18:
    remaining_yrs=18-age
    print(f'You need {remaining_yrs} to learn to drive')

    # Compare the values of my_age and your_age using if … else.
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age,
#  'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.

my_age=int(input("Enter your age: "))
your_age=int(input("Enter your age: "))
if my_age>your_age:
    yr=my_age-your_age
    if yr==1:
        print(f"I am {yr} year older than you")
    else:
        print(f"You are {yr} years older than me")
elif your_age>my_age:
    yr2=your_age-my_age
    if yr2==1:
        print(f"You are {yr2} year older than me")
    else:
        print(f"You are {yr2} years older than me")
else:
    print("We are agemates")

# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

a=int(input("Enter a number: "))
b=(int(input("Enter b number: ")))
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a is equal to b")

# ### Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# 90-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
marks=int(input("Enter student's grade: "))
if marks in range(90,100):
    print("grade A")
elif marks in range(70,89+1):
    print("grade B")
elif marks in range(60,69+1):
    print("grade C")
elif marks in range(50,59+1):
    print("grade D")
elif marks in range(0,49+1):
    print("grade F")
# Check if the season is Autumn, Winter, Spring or Summer.
#  If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter.
#  March, April or May, the season is Spring 
# June, July or August, the season is Summer

def months():
    month=(input('Enter a month: '))
    
    if month in ('September','October','November'):
        print("The season is Autumn")
    elif month in ('December','January','February'): 
         print('The season is Winter')
    elif month in ('March','April','May'):
        print('The season is Spring')
    elif month in ('June','July','August'):
        print('The season is Summer')
months()

# The following list contains some fruits:
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
if 'eggplant' in fruits:
    print('That food already exist in the list')
elif 'eggplant' not in fruits:
    fruits.append('eggplant')
    print(fruits)

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!

    person={
    'first_name': 'Nash',
    'last_name': 'Ash',
    'age': 290,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Html/Css', 'Kotlin', 'Python','MongoDB','Node'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#  Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    middle=len(person.keys())/2
    print(middle)

#  Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
x='Python'
if 'skills' in person and x in person['skills']:
    print('Python present')
else:
    print('Python absent')

#  If a person skills has only JavaScript and React, print('He is a front end developer'),
if person['skills']=='JavaScript' and 'React' :
    print('He is a Frontend Developer')
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
if person['skills']=='Node' and 'Python' and 'MongoDB':
    print('He is a Backend Developer')
#  Priif the person skills has React, Node and MongoDB,print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
elif person['skills']=='React' and 'Node' and 'MongoDB':
    print('She is a fullstack Developer')
else:
    print('unknown title')
#  If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
if  person['is_married']== True and person['country'] =='Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']} . She is married")