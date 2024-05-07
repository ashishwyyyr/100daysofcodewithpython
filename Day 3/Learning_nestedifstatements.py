# nested if/ else statement

# if condition:
#     if another condition:
#         do this
#     else:
#         do this:
# else:
#     do this

# if/elif/else
    
# if condition1:
#     do A 
# elif condition2:
#     do B 
# else:
#     do this 
       
print("welcome to the rollercoaster !")
height = int(input("what is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12")
 

else:
    print("Sorry,you have to grow taller before you can ride.")