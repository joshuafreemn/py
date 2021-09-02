pizzas = ['pepperoni', 'chilli freak', 'garden party', 'the works', 'the stinger']
for pizza in pizzas:
	print(f"I like {pizza.title()}, it might be my favourite.\n")
print("Acttually pizza is my favourite pizza!")

my_pizza = pizzas[:]
ur_pizza = pizzas[:]

my_pizza.append('hawian')
ur_pizza.append('meat feast')

print("\nMy favourite pizzas are:")
print(my_pizza)
print("\nYour favourite pizzas are:")
print(ur_pizza)