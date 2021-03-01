ranks = {
	'pcso' : 'police comunity support officers',
	'pc' : 'police counstable',
	'dc' : 'detective counstable',
	'ds' : 'dective sergant',
	'di' : 'dective inspecter',
	'dmi' : 'digital media invesigator',
}

for rank, meaning in ranks.items():
	print("A " + rank.upper() + " is a " + meaning.title())