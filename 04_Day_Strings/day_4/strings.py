# A String could be a single character or bunch of texts
from base64 import b64decode


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
print(challenge.index(sub_string, 9)) # error
#
#rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
print(challenge.rindex(sub_string, 9)) # error
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