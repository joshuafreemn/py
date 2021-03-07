rivers = {
	'nottingham' : 'trent',
	'london' : 'thames',
	'hull' : 'humber',
	'manchester' : 'tame',
	'cambridge' : 'cam',
	'derby' : 'derwent',
	'lincoln' : 'witham',
}

for city, river in rivers.items():
	print("The river " + river.title() + " runs through the city of " + city.title())