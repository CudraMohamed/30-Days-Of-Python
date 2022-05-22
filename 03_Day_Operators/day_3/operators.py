#Boolean


print(True)
print(False)

#OPERATORS
#Assignment Operators
x=1
print(x)
x+=1
print(x)
x-=1
print(x)
x*=1
print(x)
x/=1
print(x)
x%=1
print(x)
x//=1
print(x)

#BITWISE OPERATORS
# x &=1
# print(x)
# x|=1
# print(x)
# x^=1
# print(x)
# x>>=1
# print(x)
# x<<=1
# print(x)

#Arithmetic operators
#In Integers
print('Addition : ',2+3)
print('Subtraction : ',2-3)
print('Multiplication : ',2*3)
print('Division : ',2/3)
print('Modulus : ',2%3)
print('Floor Division : ',2//3)
print('Exponation : ',2**3)

#In Floats
print('Floating point number P1 : ',3.14)
print('Floating point number gravity : ',9.81)

#In Complex numbers
print('Complex number ; ',1+1j)
print('Multiplication of complex numbers ; ',(1+1j)*(1-1j))

#Calculating area of a circle
radius = 10
area_of_circle=3.14*radius**2
print("Area of circle =",area_of_circle)

#Calculating area of a rectangle
length=10
width=20
area_of_rectangle=length*width
print("Area of rectangle = ",area_of_rectangle)

#Calculating the weight of an object
mass=75
gravity=9.81
weight=mass*gravity
print(weight,'N')

#Calculating the density of a liquid
mass=75
volume=0.075
density=mass/volume
print(density,'Kg/m^3')

#Comparison operators - #the output will be a boolean
#If one condition is true then the output will be True
print(3>2) #True - 3 is greater than 2
print(3>=2) #True - 3 is greater than 2
print(3<2)  #False - 3 is not less than 2
print(3==2)  #False  operator equals to
print(3!=2)  #True    Operator not eaqual to

#comparisons using the length of strings
print(len("Cudra")==len("Mohamed")) #False
print(len("Ready")<=len("learn"))

#Logical operators
#and ,or ,not
x=3
print(x<5 and x<10) #and returns True if both of the statements are true
print(x<5 or x<10)#or returns true if one of the statements is true
print(not(x<10 and x<5))#not reverse the results returns true if the reverse is true
print(not 3>2)
print(not True)
#Excercise
age = 21
height = 0.54
complex=(1-1j)
#Write a script that prompts the user to enter base and height of the triangle and 
# calculate an area of this triangle (area = 0.5 x b x h).
 #   Enter base: 20
  #  Enter height: 10
   # The area of the triangle is 100
base = int(input('Enter base : '))
height = float(input('Enter height :'))
area_of_triangle = 0.5*base*height
print('Area of triangle = ',area_of_triangle)

#Write a script that prompts the user to 
# enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).
#Enter side a: 5
#Enter side b: 4
#Enter side c: 3
#The perimeter of the triangle is 12
a = int(input('Enter side a : '))
b = int(input('Enter side b : '))
c = int(input('ENter side c : '))
perimeter_of_triangle = a+b+c
print(perimeter_of_triangle)

#Get length and width of a rectangle using prompt.
#Calculate its area (area = length x width) and 
#perimeter (perimeter = 2 x (length + width))
length = int(input('Enter Length : '))
width = int(input('Enter width : '))
area_of_rectangle_b = length * width
perimeter_of_rectangle = 2*(length * width)
print('Area of rectangle b = ',area_of_rectangle_b)
print('Perimeter of the rectangle = ',perimeter_of_rectangle)

#Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r)
# and circumference (c = 2 x pi x r) where pi = 3.14.
r = int(input('Radius : '))
pi = 3.14
area_of_circle_b = pi*r*r
print(area_of_circle_b)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
x=3
y = (2*x)-2
print(y)

#Calculate the value of y (y = p^2 + 6p + 9). 
# Try to use different x values and figure out
#  at what p value y is going to be 0.
p=int(input('Enter p : '))
y = p^2 + 6*p + 9
print(y)

#Find the length of 'python' and 'dragon' and
#  make a falsy comparison statement.
print(len('python')!=len('dragon'))
print('on' in ('python' and 'dragon'))
print('jargon' in 'I hope this course is not full of jargon')
print('on' not in ('python' and 'dragon'))

#Find the length of the text python and convert the value to float 
# and convert it to string
py_length = len('python')
py_float = float(py_length)
py_string = str(py_float)

#Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?
print(3%2==0) #use modulus(to check if the value is 0)

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == 2.7)

#Check if type of '10' is equal to type of 10
print(type('10')==type(10))

#Check if int('9.8') is equal to 10
print(int('9.8') == 10)

#Write a script that prompts the user 
# to enter hours and rate per hour. Calculate pay of the person?
#Enter hours: 40
#Enter rate per hour: 28
#Your weekly earning is 1120
hours = int(input('Enter hours : '))
rate_per_hour = int(input('Enter rate per hour : '))
weekly_earning = hours * rate_per_hour
print('Weekly earning = ',weekly_earning)

#Write a script that prompts the user to enter number of years. 
#Calculate the number of seconds a person can live. 
#Assume a person can live hundred years
#Enter number of years you have lived: 100
#You have lived for 3153600000 seconds.
years=input('Enter number of years ; ')
days=7
months=12
hours_per_day=24
minutes_an_hour=60
seconds_per_minute=60
seconds_you_can_live=years*days*months*hours_per_day*minutes_an_hour*seconds_per_minute
print('Number of seconds a person can live = ')
