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
