from data import food_storage
import random

item = random.choice(list(food_storage.keys()))
recipe = food_storage.get(item, 'methi thepla')
variant = random.choice(recipe.get('variants',['']))
ingredients = recipe.get('ingredients','Nothing')+[variant]
print(item,variant,'Ingredients:',ingredients)