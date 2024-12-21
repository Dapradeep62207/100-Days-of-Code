# Nested if / else
'''if condition:
      if another condition:
        do this
      else:
         do this
   else:
       do this'''

# if/elif/else

'''if condition1:
    do A
elif Condition2:
    do B
else:
    do this'''
    
# BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"
     
weight = 85
height = 1.85
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")