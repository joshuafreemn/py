pets = ['dog', 'cat','dog','fish','cat','rabbit','snake']
print(pets)

while 'dog' in pets:
	pets.remove('dog')
while 'cat' in pets:
	pets.remove('cat')

print(pets)