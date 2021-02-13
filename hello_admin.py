usernames = ['harry', 'eliott', 'roberto', 'katy', 'amiee', 'sarah', 'admin']

if usernames:
	for user in usernames:
		if 'admin' in user:
			print("Hello Admin, would you like to see a status report?")
		else:
			print("Welcome back "+ user.title() +", thankyou for logging in again.")
else:
	print("Great Scott, We need to find some users!")
