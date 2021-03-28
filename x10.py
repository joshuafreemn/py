number = input("Pick a number: ")
number = int(number)

if number % 10 == 0:
	print("The number " + str(number) + " is divisiable by 10")
else:
	print("The number " + str(number) + " not divisible by 10")