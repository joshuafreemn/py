
cities = {
	
	'amsterdam': {
		'country': 'netherlands',
		'population': 1558755,
		'climate': 'wet',
		'attraction': 'canals',
		'transport': 'cycle',
		'activity': 'smoking',
		'caution': 'bike theft',
	},

	'bristol': {
		'country': 'england',
		'population': 670000,
		'climate': 'mild',
		'attraction': 'clifton suspension bridge',
		'transport': 'take a ferry',
		'activity': 'hot air balooning',
		'caution': 'gangs',
	},

	'sydney': {
		'country': 'australia',
		'population': 5367206,
		'climate': 'hot',
		'attraction': 'sydney opera house',
		'transport': 'walk',
		'activity': 'singing',
		'caution': 'majour drug gangs',
	},

	'edinburugh': {
		'country': 'scotland',
		'population': 488050,
		'climate': 'wet',
		'attraction': 'castle',
		'transport': 'hike',
		'activity': 'drink ale',
		'caution': 'murder',
	},

	'stockholm': {
		'country': 'sweden',
		'population': 975551,
		'climate': 'cold',
		'attraction': 'ikea',
		'transport': 'set sail',
		'activity': 'get lost',
		'caution': 'fraud',
	},

	'vienna': {
		'country': 'austria',
		'population': 1911191,
		'climate': 'cold',
		'attraction': 'weiner rathaus',
		'transport': 'tram hop',
		'activity': '',
		'caution': 'bribery',
	},

	'dublin': {
		'country': 'ireland',
		'population': 1173179,
		'climate': 'mild',
		'attraction': 'guiness factory',
		'transport': 'jump on the back of a leprechaun'
		'activity': 'drinking',
		'caution': 'drunk and disordly behaviour',
	},

}

for city, info in cities.items():
	intro = city.title() + " is a city in " + info['country'].title() + ", it has a population of " + str(info['population']) + "."
	if info['climate'] == 'hot':
		weather = " It can get sunny in " + city.title() + ", you should pack some sunscreen."
	elif info['climate'] == 'mild': 
		weather = " It can get brisk in " + city.title() + ", you should pack a scarf."
	elif info['climate'] == 'wet':
		weather = " It can rain cats and dogs in " + city.title() + ", you should pack your coat and wellies."
	elif info['climate'] == 'cold':
		weather = " It can get rather chilly in " + city.title() + ", you should pack your hat and gloves."
	else:
		weather = " To be safe, you should pack your sunscreen, scarf and your coat and gloves for a trip to " + city.title() + "."
	activity = " You should head to " + city.title() + "'s " + info['attraction'].title() + 

	print("\n" + intro +  weather)












