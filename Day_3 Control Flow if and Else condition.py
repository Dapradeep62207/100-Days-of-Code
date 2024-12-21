# # if condition:
#      do this
# else:
#     do this

'''water_level = 50 cm
if water_level > 80 cm:
   print("Drain water")
else:
   print("Coninue")'''
   
print("Welcome to the rollercoster!")
height = int(input("What is your height in cm ? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age ?"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <=18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <=55:
        print("Everthing is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickts are $12.")
    
    wants_photo = input("Do you want to have a photo take? Type Y for Yes and N for No.")
    if wants_photo == "Y":
        # Add $3 to their bill
        bill += 3
    
    print(f"Your final bill is {bill}")
    
else:
    print("Sorry you have to grew taler before you can ride")

#Comparison Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# != Not equal to
# == to check the eligibilty

# Modulo Operator %

