incredibles  = {
	
	'mr incredible': {
		'forname' : 'robert',
		'surname' : 'parr',
		'super power' : 'superhuman strength',
		'age' : '33',
		'city' : 'metroville',
		'status' : 'active',
		},
	'elasta girl': {
		'forname' : 'helen',
		'surname' : 'parr',
		'super power' : 'metamorphosis',
		'age' : '33',
		'city' : 'metroville',
		'status' : 'active',
		},
	'frozone': {
		'forname' : 'lucius',
		'surname' : 'best',
		'super power' : 'cryokinesis',
		'age' : '34',
		'city' : 'metroville',
		'status' : 'active',
	},
	'gazerbeam': {
		'forname' : 'simon',
		'surname' : 'paladino',
		'super power' : 'lazer beam eyes',
		'age' : '34',
		'city' : 'metroville',
		'status' : 'deceased',
	},
	'meta-man': {
		'forname' : 'mike',
		'surname' : 'matamus',
		'super power' : 'flight',
		'age' : '70',
		'city' : 'metroville',
		'status' : 'dead',
	}

}


for incredible, info in incredibles.items():
	print("Here's what i know about " + incredible.title() + ":")
	identity = info['forname'] + " " + info['surname']
	power = "They're main power is " + info['super power'] + ". "
	age = "(" + info['age'] + " y/o). " 
	if info['status'] == 'active':
		status = "They're still figiting crime from " + info['city'].title() + " and beyond."
	else:
		status = "They used to fight crime in " + info['city'].title() + "."

	cover_blower = identity.title() + " " + age + power + status

	print(cover_blower + "\n")
