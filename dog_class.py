class Dog():
	#Simple model of a dog

	def __init__(self, name, age):
		#initalise name and age attributes
		self.name = name
		self.age = age

	def sit(self):
		#simulate a dog sitting in response to cmd
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		#simulate rolling over in responde to cmd 
		print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
ur_dog = Dog('lucy', 2)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

print("\nYour dog's name is " + ur_dog.name.title() + ".")
print("Your dog is " + str(ur_dog.age) + " years old.")
ur_dog.sit()
ur_dog.roll_over()