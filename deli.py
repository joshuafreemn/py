sandwhich_orders = ['BLT', 'Pastami', 'Chuna', 'Pastami', 'Hummous and falafel', 'Beetball Marinia', 'Pastami']

finished_sandwiches = []
# while 'Pastami' in sandwhich_orders:
#	sandwhich_orders.remove('Pastami')
#	print("No Meant, Go Vegan!")

while sandwhich_orders:
	sandwhich_making = sandwhich_orders.pop()

	if 'Pastami' in sandwhich_making:
		print("No meat! eat pussy not animals, bitch!")
	else:
		print("Making your " + sandwhich_making + " .")
	
	finished_sandwiches.append(sandwhich_making)
	
	while 'Pastami' in finished_sandwiches:
		finished_sandwiches.remove('Pastami')

for sandwhich in finished_sandwiches:
	print("Order Up! " + sandwhich + "!")