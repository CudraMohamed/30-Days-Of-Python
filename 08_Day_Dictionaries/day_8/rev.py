var = "james bond"
print(var[2::-1])

sampleSet = {'Jodi','Eric','Garry'}
sampleSet.add('Vicky')
print(sampleSet)

var = "james"*2*3
print(var)

for i in range(10,15,1):
    print(i,end=',')

def calculate(num1,num2=4):
    res=num1*num2
    print(res)

for i in range(1,5):
    print(i)
else:
    print("this is else block statement")

    p,q,r =10,20,30
    print(p,q,r)

    x=36/4*(3+2)*4+2
    print(x)

    listOne=[20,30,40]
    listTwo=[20,30,40]

    print(listOne == listTwo)
    print(listOne is listTwo)

    # for x in range(0.5,5.5,0.5):
    #  print(x)       #float object can not be interpreted to integer

#Write a function for checking the speed of drivers. This function should have one parameter: speed.
#If speed is less than 70, it should print “Ok”.
#Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
#If the driver gets more than 12 points, the function should print: “License suspended”/

def speed_check(speed):
    speedlimit=70
    demeritpoint=(speed-speedlimit*1)//5
    if speed<70:
        print('okay')
    elif demeritpoint>12 & speed >70:
        print('lisense suspend')
    elif speed >70:
        print(f'points:{demeritpoint}')
    else:
        print('none')
speed_check(85)

# What about we do this as the challenge for today?
# Write a Python program to count the number of characters (character frequency) in a string.
# Example: Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}#
def count_char(word):
    results={}
    for x in word:
        keys=results
        if x in keys:
            results[x]+=1
        else:
            results[x]=1
    print(results)
count_char('Cudra')


#Given an interger 165 ,write a program that prints the sum of the digits . The expected output is 12
def num():
    y=0
    for x in str(165):
        y+=int(x)
        print(y)
num()

greetings = ['Merhaba','Hello','Bonjour','Hola']
index=0
while index<len(greetings):
    x=greetings[index]
    print(len(x))
    index+=1
    
tuple1=(1,2,3,4,5,6)
print(tuple1[2:4])

numbers = (10,15,24,10,29,34,45,10)
x=numbers.count(10)
print(x)

x=len(numbers)
print(x)

#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask the user for their salary and year of service and print the net bonus amount. Write a python code to implement this scenario.
