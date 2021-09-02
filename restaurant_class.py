class Restaurant():

	def __init__(self, name, cuisine):
		self.name = name
		self.cuisine = cuisine

	def describe_restaurant(self):
		print("Welcome to the wonderful " + self.name.title() + "!")
		print("We hope you enjoy our " + self.cuisine + " cuisine.")

	def open_restaurant(self):
		print(self.name.title() + " is ready to take your order.")

my_restaurant = Restaurant('chish and fips', 'fish friendly fish and chips.')
print("\nMy restaurant is called " + my_restaurant.name.title())
print("My restaurant serves the best " + my_restaurant.cuisine)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print("\n")

ur_restaurant = Restaurant('flaming sombero', 'exxxtra hot mexican munchies')
ur_restaurant.describe_restaurant()
ur_restaurant.open_restaurant()
print("\n")

their_restaurant = Restaurant('the coconut curry', 'the mild mild east')
their_restaurant.describe_restaurant()
their_restaurant.open_restaurant()