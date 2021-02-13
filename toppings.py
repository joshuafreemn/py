requested_toppings = ['mushrooms', 'pineapple', 'green peppers', 'extra pineapple']

for topping in requested_toppings:
	if topping == 'green peppers':
		print("Sorry, We're all out of green peppers right now.")
	else:
		print("Adding " + topping.title() + ".")

print("\nYour pizza is finito.")