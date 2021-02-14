users = ['harry', 'eliott', 'roberto', 'katy', 'amiee', 'sarah',]

newbies = ['heather', 'KATY', 'josh', 'Sarah']

for newbie in newbies:
	for user in users:
		if newbie.lower() == user:
			print("Sorry " + user.title() + " already exsits. Get a new name.")
	else:
		print("Hi " + newbie.title() + ", welcome to the website.")
