# A String could be a single character or bunch of texts
from base64 import b64decode
from pickletools import string1


letter = 'p'
print(letter)
greetings = "Hello, World!"
print(greetings)
print(len(greetings)) # Prints the length of the characters in greetings variable inclusive of spaces

#Multiline string
sentence = '''I really love Python and the rest of
the programming languages'''
print(sentence) 
sentence2 = """I really love coding with Python and 
as well as the other programming languages"""
print(sentence2)

#String Concatenation /Merging/connecting strings together
first_name = 'Cudra'
second_name = 'Morehermade'
space = ' '
full_name = first_name + space + second_name 
print(full_name)
print(len(first_name)>len(second_name)) #False
print(len(full_name))

#Escape Sequence in Strings
#\n: new line
#\t: Tab means(8 spaces)
#\\: Back slash
#\': Single quote (')
#\": Double quote (")
print('I hope everyone is enjoying the Python Challenge.\nAre you?')
print('Days\tTopics\tExercices')
print('Day 1\t3 \t5')
print('In every programming language it starts with \"Hello World\"')

#String formatting
first_name ="Cudra"
second_name = "Morehermade"
language = "Python"
formated_String = 'I am {} {}.I teach {}'.format(first_name,second_name,language)
print(formated_String)

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

#String interpolation
a=5
b=6
print(f'{a}+{b}={a+b}')

#Python Strings as sequence of characters-
# unpacking strings
language = "Python"
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#String indexing
language = 'Python'
first_letter = language[0]
print(first_letter)
last_letter = language[-1]
print(last_letter)

#String slicing
language = 'Python'
first_three_letters = language[0:3]  #emits the last value
print(first_three_letters)
last_three=language[-3:]
print(last_three)   #prints all the value to the end of the sentence

#Reversing strings
greeting = "Hello, World!"
print(greeting[::-1])

#Skipping characters while slicing
language = 'Python'
pto= language[0:6:2]
print(pto)
name='Cudra'
cda=name[0:5:2]
print(cda)
stationery='pens'
pn=stationery[0:4:3]
print(pn)

#String Methods
challenge = 'thirty days of python'
print(challenge.capitalize())       #Capitalizes the first letter of a string
print(challenge.count('th'))        #returns occurences of 'sub-strings'
print(challenge.endswith('n'))      #checks if a string ends with a specified ending
challenges = 'thirty\tdays\tof\tpython'
print(challenges.expandtabs())
print(challenges.expandtabs(10))        #expands tabs size with spaces
print(challenges.find('y'))             #returns the index of the first occurrence substring if none then returns -1
print(challenges.rfind('y'))            #returns the index of the last occurrence substring if none then returns -1
radius = 10
pi=3.14
area=pi*radius**2
results= 'The area of a circle with radius {} is {}.'.format(str(radius),str(area))     #formats strings into a nicer output
print(results)
#index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
# print(challenge.index(sub_string, 9)) # error
#
#rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
# print(challenge.rindex(sub_string, 9)) # error
#isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False
#isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False
#isdecimal(): Checks if all characters in a string are decimal (0-9)
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed
#isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
#isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # 1/2
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
#isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
#islower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
#isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
#join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
#strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'
#replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
#split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
#title(): Returns a title cased string
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
#swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
#startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False

#Exercise
#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string1='Thirty'
string2='Days'
string3='Of'
string4='Python'
print(string1+' '+string2+' '+string3+' '+string4)
#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string5='Coding'
string6='For'
string7='All'
print(string5+' '+string6+' '+string7)
#Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
#Print the variable company using print().
print(company)
#Print the length of the company string using len() method and print().
print(len(company))
#Change all the characters to uppercase letters using upper() method.
print(company.upper())
#Change all the characters to lowercase letters using lower() method.
print(company.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
#Cut(slice) out the first word of Coding For All string.
print(company.strip('Coding'))
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))
print(company.rfind('Coding'))
print(company.rindex('Coding'))
print(company.index('Coding'))
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Python'))
# Change Python for Everyone to Python for All using the replace method or other methods.
python = 'Python for Everyone'
print(python)
print(python.replace('Everyone','All'))
# Split the string 'Coding For All' using space as the separator (split()) .
print('Coding For All'.split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" .split(','))
# What is the character at index 0 in the string Coding For All.
print(company[0])
# What is the last index of the string Coding For All.
print(company.rfind('l'))
# What character is at index 10 in "Coding For All" string.
print(company[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
print('Python For Everyone'[0],'Python For Everyone'[7],'Python For Everyone'[11])
# Create an acronym or an abbreviation for the name 'Coding For All'.
print(company[0],company[7],company[11])
# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.find('C'))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.find('F'))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.strip('because'))
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.replace('because',''))
# Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))
# Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      ' .strip())
# Which one of the following variables return True when we use the method isidentifier():
identifier='30DaysOfPython'
identifier_2='thirty_days_of_python'
print(identifier.isidentifier())
print(identifier_2.isidentifier())
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
py_libraries='Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'
print('#'.join(py_libraries))
# Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge.\nI just wonder what is next.')
# Use a tab escape sequence to write the following lines.

print('Name      Age     Country   City')
print('Asabeneh  250     Finland   Helsinki')
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius=10
area = 3.14 *radius **2
print('The area of a circle with radius {} is {} meters square.'.format(radius,area))
# Make the following using string formatting methods:
a=8
b=6
# 8 + 6 = 14
print('{}+{}={}'.format(a,b,a+b))
# 8 - 6 = 2
print('{}-{}={}'.format(a,b,a-b))
# 8 * 6 = 48
print('{}*{}={}'.format(a,b,a*b))
# 8 / 6 = 1.33
print('{}/{}={}'.format(a,b,a/b))
# 8 % 6 = 2
print('{}%{}={}'.format(a,b,a%b))
# 8 // 6 = 1
print('{}//{}={}'.format(a,b,a//b))
# 8 ** 6 = 262144
print('{}**{}={}'.format(a,b,a**b))