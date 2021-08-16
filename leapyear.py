year = int(input("Which year do you want to check? "))

year4 = year % 4
year100 = year % 100
year400 = year % 400

if year4 == 0:
	if year100 == 0:
		if year400 == 0:
			print("This is a leap year")
		else:
			print("This is not a leap year")
	else:
		print("This is a leap year")
else:
	print("This is not a leap year")
