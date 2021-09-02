def show_magicians(magician):
	for magician in magicians:
		print(magician)

def make_great(show_magicians):
	for magician in magicians:
		print("Welcome, the great " + magician)

magicians = [
		'Uri The Outstanding',
		'Scott Osterhouse',
		'Jewel The Masterly',
		'Mac Laub'
		'Luke Poffenberger'
			]

make_great(magicians[:])
show_magicians(magicians[:])