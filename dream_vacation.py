vacations = {}

polling = True

while polling:
	name = input("\nWhat's your name? ").lower()
	destination = input("Where you off first, post pandemic? ").lower()

	vacations[name] = destination

	repeat = input("Would you like to let another person fly away? (yes/ no) " )
	if repeat == 'no':
		polling = False

print("\n--- Vacation Destinations ---")
for name, destination in vacations.items():
	print(name.title() + " is off to " + destination.title() + "." )

	
