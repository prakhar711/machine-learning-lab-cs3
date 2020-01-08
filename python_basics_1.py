# -*- coding: utf-8 -*-
"""Python_Basics_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cceeeNJKkNW923HO_mk0BVmyVVk9dnyy

### print() function
"""

print("nikhar")

"""### Comments"""

# First Program
print("Acropolis")

"""### Variables"""

# In Python there is no need to mention the data type

var1 = 20      # An integer assignment
var2 = 4.123   # A floating point
var3 = "India" # A string

print(var1,' ',var2,' ',var3)

pi=3.14
print(pi*66)



"""### Assignment"""

# general syntax
#variable-name=value

# Assigning same value to multiple variables

var1 = var2 = var3 = 1
print(var1,' ',var2,' ',var3)

# Assigning Different values to variable in a single expression

var1, var2, var3 = 1, 2.5, "nikhar"
print(var1,' ',var2,' ',var3)

# Note: commas can be used for multi-assignments

"""### Taking input"""

firstname = input("Enter your first name: ")
lastname = input("Enter your second name: ")
semester = input("Enter your semester: ")

# run below code
age = input("Enter your age: ")
age = int(age)+5
print(age)

"""### Write a program in Python for data type conversion from: 
- int to string
- int to float
- string to int
- string to float
- float to int
- float to string
"""

a=10
print(str(a))
print(float(a))

b='20'
print(int(b))
print(float(b))

c=23.56
print(int(c))
print(str(c))

"""### Task1: 
#### WAP to display your infomation like (full name, branch, university name, age, 12th %, hobbies). Store each value into some meaningful variable.  the ouptput of the program should look like
"""

fullname = input("Enter your full name: ")
branch = input("Enter your branch: ")
university = input("Enter your university: ")
age = input("Enter your age: ")
twelthper = input("Enter your 12%: ")
hobbies = input("Enter your hobbies: ")
print(fullname)
print(branch)
print(university)
print(age)
print(twelthper)
print(hobbies)

"""### Commmonly used functions 
- round(n)
- format(n, '0.2f')
- format(n,',') # put a comma on thousand place
- format(n,'b') # print binary of the number, 'o', 'x'

- eval(expression)
- chr(n)
- ord(character)
- bin(n), oct(n), hex(n)

- #### function on string/character data
- isdigit()
- isalpha()
- isspace()
- numeric()
- ljust(width)
- rjust(width)
- cjust(width)
"""

# Python3 program to demonstarte 
# the str.format() method 
  
# using format option in a simple string 
print ("{}, A computer science portal for acropolis."
                        .format("acropolis")) 
  
# using format option for a 
# value stored in a variable 
str = "This article is written in {}"
print (str.format("Python")) 
  
# formatting a string using a numeric constant 
print ("Hello, I am {} years old !".format(20))

# Characters and their ASCII value

x=68
# print character corresponding to x 
print(chr(x))
char='D'
# print number corresponding to char
print(ord(char))

# write code to print your name 10 times
print('ACROPOLIS'*10)

for i in range(5):
    print("*"*i)

# new pattern program
print("\n")
for i in range(4,0,-1):
  print("*"*i)

for i in range(1,6):
  print(" "*(6-i),"*"*i)

# use seperator and end with specific symbol
a, b, c = 10, 20, 30
print(a,b,c,sep=':',end=',')

for i in range(1,5):
    print(" "*(5-i),"*"*i)

# unpack characters
word = 'PYTHON'
a,b,c,d,e,f = word
print(a,b,c,d,e,f)

"""### Format output"""

x = 5 
y = 10
print('The value of x is {} and y is {}'.format(x,y))

print('I like {0} and {1}'.format('ice cream','chocolate'))

print('I like {1} and {0}'.format('ice cream','chocolate'))

print('Hello {name}, {greeting}'.format(greeting = 'Good morning', name = 'Sachin !'))

"""### Task2
#### Raman likes tea but he has coffee. Riya likes coffee but has tea. Write a program in python so that both can enjoy what they like.
"""

# write your code after this line
raman='coffee'
riya='tea'
temp=raman
raman=riya
riya=temp
print("raman :{}".format(raman))
print("riya :{}".format(riya))

"""### Task3
Write a program for following
- Input: 'Python'
- Output: 642
"""

e,f,g,h,i,j='Python'
s=ord(e)+ord(f)+ord(g)+ord(h)+ord(i)+ord(j)
print(s)

"""# Working with math, calendar, random, datetime"""

import math
print(math.sqrt(9))
print(math.floor(10.8))
print (math.ceil(10.5))
math.pi

import random
x = random.random() # generate any random number between 0 and 1
print("x = ", x)

y = random.randint(5,20)# generate any random number between 5 and 20
print("y = ", y)

import datetime

date = datetime.datetime.now().date() # YYYY-MM-DD format
year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day

print(date)
print(year)
print(month)
print(day)

import calendar

year = int(input("Enter Year : "))
month = int(input("Enter the Month : "))

print(calendar.month(year, month))

"""### Task 4
#### WAP to justify the value of a number (right, left, center) in 20 chars with one digit accuracy. Use format() to print value of variable z (float) right justify in 30 chars with 3 digit accuracy.
"""

x=15246.59
y=14.156
print(format(x,'>20.1f'))
print(format(y,'>20.1f'))
print("\n")

print(format(x,'<20.1f'))
print(format(y,'<20.1f'))
print("\n")

print(format(x,'^20.1f'))
print(format(y,'^20.1f'))
print("\n")

z=20.745124
print(format(z, '>30.3f'))

