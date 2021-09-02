def car_info(make, model, **extra):

	car = {}
	car['make'] = make
	car['model'] = model
	for key, value in extra.items():
		car[key] = value
	return car

car_finder = car_info('Modle X','Tesla',
					  color='white',
					  insuranc=True)

print(car_finder)
