# have i been pwned?

# For Loop

'''A for loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects. 
It executes a block of code repeatedly for each element in the sequence.
Here's a simple example:'''

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "pie")

print(fruits)

# Coding Excercise

student_scores = [85, 92, 78, 88, 95, 67, 74, 81, 90, 76]

total_exam_score = sum(student_scores)

sum = 0
for score in student_scores:
    sum =+ score
    
print(sum)

#max 

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
        
print(max_score)

# Create a loop with For and Range to go from 1 to 100.
for number in range(1, 101):
  # First check if the number is divisible by both 3 and 5.
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
 
  # Then check if the number is only divisible by 3
  elif number % 3 == 0:
    print("Fizz")
 
  # Finally check if the number is only divisible by 5
  elif number % 5 == 0:
    print("Buzz")
 
  # If it's not divisible by either of those numbers, just print the number
  else:
    print(number)