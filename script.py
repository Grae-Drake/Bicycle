from models import *

# Wheels
bouncy = Wheel(10, 18, "bouncy")
flat = Wheel(10, 1, "flat")
fat = Wheel(12, 25, "fat")

# Frames
tripod = Frame("steel", 21, 100, "tripod")
dented = Frame("aluminum", 8, 80, "dented")
space_age = Frame("carbon", 5, 350, "space age")

# Manufacturers (need to add models)
schwinn = Manufacturer("Schwinn", .15, [])
acme = Manufacturer("Acme", .10, [])

# Models.  Note: need to associate manufacturers with models!!!
bruiser = Model(flat, tripod, "Bruiser", schwinn)
speedy = Model(bouncy, dented, "Speedy", schwinn)
fatty = Model(fat, tripod, "Fatty", acme)
turbo = Model(bouncy, space_age, "Turbo", acme)

# Shops
globo_shop = Shop("Globo Shop", .20)
globo_shop.buy_bikes(bruiser, speedy, fatty, turbo)

# Customers
grae = Customer("Grae", 1000)
alice = Customer("Alice", 500)
bob = Customer("Bob", 150)
customers = [grae, alice, bob]

# Print shop inventory:
globo_shop.display_inventory()

# Print customer options:
for customer in customers:
	customer.display_affordable_bikes(globo_shop)

globo_shop.sell_bike(bruiser, bob)
globo_shop.sell_bike(fatty, alice)
globo_shop.sell_bike(turbo, grae)
globo_shop.sell_bike(speedy, grae)

globo_shop.display_inventory()
print "{}'s profit is ${}".format(globo_shop.name, globo_shop.profit)

