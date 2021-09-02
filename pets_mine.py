def describe_pet(animal_type='dog', pet_name):
	"""Display info about a pet."""
	print("\nYou hvae a " + animal_type.title() + ".")
	print("Your " + animal_type + "'s name is " + pet_name.title() + ".")

pet_talk = True

while pet_talk:
	species = input("\nWhat type animal do you have? ").lower()
	pet = input("What's your " + species + " called? ").lower()

	describe_pet(species, pet)

	repeat = input("\nHave you got any more pets? (yes/ no) " )
	if repeat == 'no':
		pet_talk = False
