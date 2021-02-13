alien_color = 'orange'

if 'green' in alien_color:
	points = 5
elif 'yellow' in alien_color:
	points = 10
elif 'red' in alien_color:
	points = 15
else:
	points = 0

if points == 0:
	print("WTF! That ain't no alien!")
else:
	print(alien_color.title() + " alien killed, +" + str(points) + ".")