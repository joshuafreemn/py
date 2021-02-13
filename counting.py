print("Counting up to Twenty")
twenty = list(range(1, 21))
print(twenty)
print("\n")

print("Messing with a Million:")
millie = list(range(1, 1000001))
#for num in millie:
	#print(num)
print(f"The sum of {min(millie)} to {max(millie)} is {sum(millie)}")
print("\n")

print("Odd Numbers:")
odds = list(range(1, 21, 2))
print(odds)
print("\n")

print("Cubes:")
cubes = []
for value in range(1, 11): 
	cubes.append(value**3)
print(cubes)
print("\n")

print("Cube Compresion:")
cubes = [value**3 for value in range(1, 11)]
print(cubes)