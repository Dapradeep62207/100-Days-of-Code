'''Day 1 Printing
String Manipulation
Input Function
Variables
Variable Naming rules
Debugging'''

#Print a string into the console.
print("Hello World")

#String Manipulation
print("Hello Pradeep" )

# String concatentaion
print("Hello" + " " + "Peter")

#Prints a string into the console, and asks the user for a string input.
print("Hello " + input("What is your name?") + "!")


#this is a comment.
print("This is a code")

'''Variables
A varible give a name to a piece of data. 
Link a box with a label, it tells you what's 
inside the box'''

#Assign a variable as string
my_name = "Peter"

#how to get the length of the string using length function

print(len(input("What is your name?")))

# One more len example
user_name = input("What is your name?")
length = len(user_name)
print(length)

#variable naming
user_name = "Peter"
my_age = 37

#The += Opreator
# This is convient way of saying "take the previous value and add to it"

my_age = 37

my_age += 4
#my_age is now 41

print(my_age)