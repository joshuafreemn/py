def make_pizza(size, *toppings):
	#print the ist of topings that have been requested
	print("\nMaking a " + str(size) +
		  "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
