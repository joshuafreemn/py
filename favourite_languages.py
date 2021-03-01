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

#loop through keys in dictionary
print("\nNames:")
for name in favorite_languages.keys():
	print(name.title())

#using keys() to find a particular person
if 'erin' not in favorite_languages.keys():
	print("\nErin, please take our poll!")

#looping through dictionay in order
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll!")

#Looping through values
print("\nThe follwoing languages have neem mentioned:")
for language in favorite_languages.values():
	print("\t" + language.title())