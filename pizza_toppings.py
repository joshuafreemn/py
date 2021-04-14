prompt = "What do you want on your pizza?"
prompt += "\ntype 'bake' to make your pizza. "


adding = True
while adding:
	topping = input(prompt)

	if topping == 'bake':
		adding = False
		print("\nslidin' your pizza into the oven!\n")

	else:
		print("\nAdding " + topping + " to your pizza.\n")