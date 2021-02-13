motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

# dynamically built lists can start empty

motorbikes = []

motorbikes.append('honda')
motorbikes.append('suzuki')
motorbikes.append('yamaha')
motorbikes.append('ducati')

print(motorbikes)

motorbikes.insert(1, 'harley davidson')
print(motorbikes)

del motorbikes[2]
print(motorbikes)

popped_motorbikes = motorbikes.pop(1)
print(popped_motorbikes)

motorbikes.remove('yamaha')
print(motorbikes)