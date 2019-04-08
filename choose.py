from data import food_storage
import random

item = random.choice(list(food_storage.keys()))
recipe = food_storage.get(item, 'methi thepla')
print(item,recipe)