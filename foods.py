my_foods = ['pizza', 'falafel', 'sushi','spaghetti', 'pie', 'soup', 'hot dogs',]
friends_foods = my_foods[:]

my_foods.append('baked beans')
friends_foods.append('ice cream')

print("My favourite foods are:")
for food in my_foods:
	print(food.title())

print("\nMy friend's favourite foods are:")
for food in friend_foods:
	print(food.title())

print("\nMy top 3 foods are:")
print(my_foods[:3])

print("\nMy friends top 3 are:")
print(friends_foods[3:6])

print(f"\nMy compfoty food is {my_foods[-1:]} but my friedns is {friends_foods[-1:]}")