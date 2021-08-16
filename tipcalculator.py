#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator.")
bill = float(input("What was the toal bill? "))
people = int(input("How many people were eating? "))
tip = int(input("How much would you like to tip? "))

split = (bill / people) * (1 + (tip / 100))
# amount = round(split, 2)
amount = "{:.2f}".format(split, 2)
print(f"Each person should pay: ${amount}")
