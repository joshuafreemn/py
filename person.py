def build_person(forname, surname, age=''):
	#return a dicitonary of information anbout a person.
	person = {'first': forname, 'last': surname}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix')
print(musician)