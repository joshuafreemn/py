	#define list
cars = ['bmw','audi', 'toyota', 'subaru']
	#sort in a-z order
cars.sort()
print(cars)
	#sprt
cars.sort(reverse=True)
print(cars)
print("\n")

	#redefing list
cars = ['bmw','audi', 'toyota', 'subaru']

print('Here is the orginal list:')
print(cars)

	#temporaily sort list
print("Here is the sorted list:")
print(sorted(cars))

print("Here is the orginal list again:")
print(cars)
print("\n")
	
	#reverse list
cars.reverse()		#note it just resece the orginsal order of the list and does not sort it z-a
print(cars)
	#revert list to orginal order
cars.reverse()

	#find the legth of a list
print(len(cars))
