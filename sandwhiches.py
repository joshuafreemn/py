def make_sandwhich(*fillings):
	print("Filling your sandwhich with:")
	for filling in fillings:
		print("- " + filling)

make_sandwhich('tuna','sweetcorn','mayo')