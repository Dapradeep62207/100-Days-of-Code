# Code Blocks, Functions, While Loop
# Karel the Robot

# Functions: 

def my_function(): # Define the function
    print("Hello") # Do this
    print("Bye") # Then do this

my_function() # Calling Functions

#Functions with outputs
'''In addition to outputs, a function can also have an output.
The output value is proceeded by the keyword "return".
This allows you to store the result from a function.'''

def add(n1, n2):
    return n1 + n2
result = add(2, 3)

print(result)

# #Variable Scope Variables created inside a functions are # destroyed once the function has executed. 
# The location (line of code) that you use # a variable will determine its value. 
# Here n is 2 but inside my_function() n is 3.
# # So, printing n inside and outside the function will determine # it's value'''

n = 2
def my_function():
    n = 3
    print(n)
#print(n) prints 2
#my_function() print 3