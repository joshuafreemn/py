available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra pineapple', 'jalapeno']

requested_toppings = ['mushrooms', 'pineapple', 'jalapeno', 'extra pineapple']

if requested_toppings:
	for topping in requested_toppings:
		print("Adding " + topping.title() + ".")
	print("\nYour pizza is finito.")
else:
	print("Don't be a plain jane, add some toppings to ya pizza!")