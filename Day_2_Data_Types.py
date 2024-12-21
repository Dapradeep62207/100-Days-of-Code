#Python Primitive Data Types
'''Strings
Integers
Floats
Booleans'''

#Subscriping
print("Hello"[0])

#negative subscrpting
print("Hello"[-1])

#integers : Integers are whole numbers.
my_number = 354

#large integers 
print(345_657_987_009)

#Floating point number
my_float = 3.14

#Strings : A string is just of characters. It should be surrounded by double quotes.
my_string = "Hello"

#Boolean
print(True)
print(False)

#String Concatenation: You can add string to string to create a new string. This is called concatenation,
print("Hello" + " " "Peter")

#Escaping a String: Because double quote is special.
speech = "she said: \"Hi\""
print(speech)

#Type Error
len(12345)

#Type checking
print(type("Hello"))

#Type casting
print(int("123"))

int()
float()
str()
bool()

name_of_the_user = input("Enter your name") 
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) #str
print(type(length_of_name))

print("Number of letters in your name: " + str(length_of_name))

#Mathematical Operations in Python
#Addition
print(123 +456)

#substraction
print(7-3)

#Multiplication
print(3 * 2)

#Division
print(6 / 3)
print(6 // 3) 

#Exponent
print(2 ** 3)

#PEMDAS 
# ()
# **
# * OR /
# + OR -

print(3 * 3 + 3 / 3 - 3)#result would be 7

#Challange
print(3 * (3 + 3) / 3 - 3) # result would be 6

#Number Manipulation
score = 0
# user scores a point
score += 1
# -=
# /=
# *=
print(score)

# F String
score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}, your winning is {is_winning}")

height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = 84 / (1.65 **2)

print(bmi)

# Round function
print(round(bmi))

print(round(bmi, 2))

#F-Strings: you can insert a variable into a string using f-strings.
#The Syntax is symple. just insert the variable in between a set of curly braces{}

days = 365

print(f"There are {days} in a year")

#converting a Data type
'''You can convert a variable from 1 data type to another.
converting to float: float()
converting to int: int()
converting to string: str()'''
n = 354
new_n = float(n)
print(new_n) #result 354.0

#Checking data types: You can check the type() fucntion to check what is the data type of a particular variable.

n = 3.14
print(type(n)) #result float