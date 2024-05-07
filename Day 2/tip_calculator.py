##MY RESPONSE

# print("Welcome to the tip calculator.")
# x = float(input("What was the total bill? $"))
# y = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
# z = float(input("How many people to split the bill?"))

# a = x + (((y/100) * x))
# b = round(a / z,2)

# print(f"each person should pay: ${b}")

## REPLY

#If the bill was $150.00, split between 5 people
# with 12 % tip
#Each person should pay(150.00 /5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15?"))
people = float(input("How many people to split the bill?"))
tip_as_present = tip /100
total_tip_amount = bill * tip_as_present
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")