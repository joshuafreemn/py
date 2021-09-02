def build_profile(first, last, **extra_info):
	#Build a dictionary of user info

	profile = {} #create empty dictionary
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in extra_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein',
							 location='princeton',
							 feild='physics')

print(user_profile)
