def greet_users(names):
	#print simple greeting
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['iris', 'martha', 'julia', 'margot']
greet_users(usernames)