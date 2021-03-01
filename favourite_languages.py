favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
}
#print Sarah's fav language
print("Sarah's fave language is " + favorite_languages['sarah'].title() + ".\n")

#loop through dictionary
for name, language in favorite_languages.items():
	print(name.title() + "'s favourite language is " + language.title() + ".")