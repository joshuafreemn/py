available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra pineapple', 'jalapeno']

requested_toppings = ['mushrooms', 'anchiovies', 'pineapple', 'extra pineapple']

if requested_toppings:
	for topping in requested_toppings:
		if topping in available_toppings:
			print("Adding " + topping.title() + ".")
		else:
			print("Sorry Bud, all out of " + topping + ".")
	print("\nYou're pizza is finito!")
else:
	print("Don't be a plain jane, add some toppings to ya pizza!")

