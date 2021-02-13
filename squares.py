	#long
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)

print(squares)

	#short
squares = []
for value in range(1, 11): 
	squares.append(value**2)
print(squares)

	#shortest (using list compesion)
squares = [value**2 for value in range(1, 11)]
print(squares)