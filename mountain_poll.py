responses = {}brew install --cask caffeine

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
	# Prompt for the persson's name and response
	name = input("\nWhat is your name? ")
	response = input ("Which mountain would you like to climb someday? ")

	# Store response in the dictionary:
	responses[name] = response

	# Find out if anyone is going to take the poll
	repeat = input("Would you like to let another perosn respond (yes/no) ")
	if repeat == 'no':
		polling_active = False


# Polling is complete. Show results.
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name.title() + " would like to climb " + response + ".")