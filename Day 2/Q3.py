# Instructions

# i was reading this article by tim urban - your life in weeks and realised
# just how little time we actually have.

# create a program using maths and fstring that tells us how many 
# weeks we have left, if we live unitl 90 years old.

# It will take yourt current age as the input and output a message with our
# time left in format:

# you have x week left.

# where x is replaced with actual calculated number of weeks the input
# age has left until age 90.

# Warning: your output should match the example output format exactly,
# even the postions of the commas and full stops.


# input 56 output you have 1768 weeks left

##code here 

current_age = int(input())
#age = years

weeks_lived = current_age * 52

print(weeks_lived)

# x = weeks left

x = 4680 - weeks_lived

print(f'you have {x} weeks left')