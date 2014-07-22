class Wheel(object):
	def __init__(self, weight, cost, name):
		self.weight = weight
		self.cost = cost
		self.model_name = name

class Frame(object):
	def __init__(self, material, weight, cost, name):
		self.material = material # Should only accept "carbon", "aluminum", and "steel".
		self.weight = weight
		self.cost = cost
		self.name = name

class Model(object):
	def __init__(self, wheel, frame, name):
		self.wheel1 = wheel
		self.wheel2 = wheel
		self.frame = frame
		self.name = name
		self.weight = self.wheel1.weight + self.wheel2.weight + self.frame.weight
	def cost(self, shop):
		base_cost = self.wheel1.cost + self.wheel2.cost + self.frame.cost
		return base_cost * (1 + shop.markup) # add (1 + manufacturer.markup) * !!!

class Manufacturer(object):
	def __init__(self, name, markup, models):
		self.name = name
		self.markup = markup
		self.models = models

class Shop(object):
	def __init__(self, name, markup):
		self.name = name
		self.markup = markup
		self.inventory = []
		self.profit = 0

	def buy_bikes(self, *models):
		for model in models:
			self.inventory.append(model)

	def sell_bike(self, model, Customer):
		pass

class Customer(object):
	def __init__(self, name, fund):
		self.name = name
		self.fund = fund
		self.owned_bikes = []
		
