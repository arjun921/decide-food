from data import food_storage
import random
import json

item = random.choice(list(food_storage.keys()))
ingredients = food_storage.get(item)
response = {
    'Dish': item,
    'Ingredients': ingredients
}
print(json.dumps(response, indent=4))
