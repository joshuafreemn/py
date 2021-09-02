import pizza

pizza.make_pizza(10, 'pepperoni')

from pizza import make_pizza

make_pizza(11, 'cheese')

from pizza import make_pizza as pizza_time

pizza_time(13, 'hawaian')

import pizza as hot_dog

hot_dog.make_pizza(14, 'sausage')

# from pizza import *
# would import all functions from pizza.py