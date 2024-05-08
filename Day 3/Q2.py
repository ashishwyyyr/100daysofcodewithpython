# Instructions
# write a program that interperts the body mass index(BMI) based
# on a user's weight and height.

# it should tell them the interpretation of their BMI
# based on the BMI value.

# Under 18.5 they are underweight
# over 18.5 but below 25 they have a normal weight
# over 25 but below 30 they are slightly overweight
# over 30 but below 35 they are obese
# above 35 they are cliniclly obese

# refer to the screen shot shared in the folder.


# The Bmi is calculated by dividing a person's weight
# (in kg) by the square of their height(in m)

# IMportant you do not need to round the resilt to the nearest
# whole number.
# It's fine tp print out a float number for this exrcise. the interpretation message 
# needs to include the words in bold from the 
# interpretation 
# above e.g. underweight, normal weight, overweight,obese,clinically obese.
# example input
# 1.50
# 63
# example output 1

# your Bmi is 28.0 you are slightly over weight.

# since 63 / (1.50x1.50)=28

# the testing code will check for the print output
#     that is formatter like one of the 
# lines below:

# "Your BMI is 18.28678, you are underweight."
# "Your BMI is 22.0, you have a normal weight."
# "Your BMI is 28.50752, you are slightly overweight."
# "Your BMi is 32.56189, you are obese."
# "Your BMI is 37.50000, you are clinically obese."

#Enter your height in meters. e.g.,1.55
height = float(input())
#Enter your Weight in Kilograms e.g., 72
weight = int(input())
#Do not change the code above
bmi = weight/(height ** 2)

if bmi < 18.5:
    print(f"your BMI is {bmi}, you are underweight.")
elif bmi < 25: 
    print(f"Your Bmi is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
