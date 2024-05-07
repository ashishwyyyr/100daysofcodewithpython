# Write a program that adds the digits in a 2 digit number. eg. if the input 
#was 35, then the output should be 3+ 5 = 8\

#warning Do. not change the code on line 1.
#your program should work for different inputs.
#e.g.any two-digit number.
#the last line of your program should print the result

#example1 INput
# 39
#output 12
#example2 INPUT 43 OUTPUT 7


two_digit_number= input()
##################### DO not change the code above the line
# #write your code here

##MY RESPONSE
# a =input("enter the number at ones places")
# b =input("enter the number at tens places")
# c = int(a) + int(b)
# print(c)

#SOLUTION BY ANGELA BRO

#try hitting run code to see the data type

# print(type(two_digit_number))
# checking the data type told us that the given input 
# is in the form of string that means we can get ahold of the
# first digit by using [] through sub scripting

first_digit = int(two_digit_number[0])
#taking out the first digit from the string and then
#converting it to integer to later on to add the 
second_digit = int(two_digit_number[1])

digit_sum = first_digit + second_digit

print(digit_sum)

#just for fun i gave it an another try and made it more confising

print(int(two_digit_number[0]) + int(two_digit_number[1]))

