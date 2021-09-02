def get_formatted_name(forname, surname, middle_name=''):
	"""Return a full name, neatly fomatted."""
	if middle_name:
		full_name = forname + ' ' + middle_name + ' ' + surname
	
	full_name = forname + ' ' + surname
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)