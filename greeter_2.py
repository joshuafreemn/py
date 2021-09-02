def get_formatted_name(forename, surname):
	#Return a full name, neatly fomatted.
	full_name = forename + ' ' + surname
	return full_name.title()

#this is an infinate loop!
while True:
	print("\nPlease tell me your name:")
	print("Enter 'q' to quit")


	f_name = input("Forename/s: ")
	if f_name == 'q':
		break
	
	l_name = input("Surname: ")
	if l_name == 'q':
		break

	formated_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formated_name + "!")