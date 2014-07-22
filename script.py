from models import *

# Wheels
bouncy = Wheel(10, 20, "bouncy")
flat = Wheel(10, 1, "flat")
fat = Wheel(12, 25, "fat")

# Frames
tripod = Frame("steel", 21, 100, "tripod")
dented = Frame("aluminum", 8, 80, "dented")
space_age = Frame("carbon", 5, 350, "space age")

# Models.  Note: need to associate manufacturers with models!!!
bruiser = Model(flat, tripod, "bruiser")
speedy = Model(bouncy, dented, "speedy")
fatty = Model(fat, tripod, "fatty")
turbo = Model(bouncy, space_age, "turbo")

# Manufacturers
schwinn = Manufacturer("Schwinn", .15, [bruiser, speedy, fatty])
acme = Manufacturer("acme", .10, [bruiser, speedy, turbo])

# Shops
globo_shop = Shop("globo shop", .20)
globo_shop.buy_bikes(bruiser, speedy, fatty, turbo)

# Customers
grae = Customer("grae", 1000)
alice = Customer("alice", 500)
bob = Customer("bob", 200)
customers = [grae, alice, bob]

# Print shop inventory:
print "{}'s inventory is:".format(globo_shop.name)
for model in globo_shop.inventory:
	print model.name + " for sale:"
	print "  Price: {}".format(model.cost(globo_shop))
	print "  Weight: {} pounds".format(model.weight)

# Print customer options:
for customer in customers:
	print "Showing models {} can afford".format(customer.name)
	for model in globo_shop.inventory:
		if model.cost(globo_shop) < customer.fund:
			print model.name

### Todo:
#   Print initial inventory
#   Each customer purchases a bike
#   After each purchase, print remaining inventory and total profit
###