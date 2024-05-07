# Instructions
# This program takes two inputs. The first input is stored in a variable called a. 
#The second input is stored in a variable called b.
# Write a program that switches the values stored in the variables a and b.
# Warning. You don't need to print anything. The print statement is already in the template code. However, your program should work for different inputs. e.g. any value of a and b.
# Example Input 1
# 29
# 41
# Example Output 1
# 8: 42
# b: 25
# Example Input 2
# Hello
# World
# Example Output 2
# a: World
# b: Hello


#there are two variables, a and b from input
a = input()
b = input()

#don't change the above
########################################
#write your code below this line
c = a
a = b
b = c

#write your code above this line
print("a: " + a)
print("b: " + b)

