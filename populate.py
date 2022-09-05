import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RecipApp.settings')
import django
django.setup()
import requests
from main.models import Ingredient, Recipe

url = 'https://api.spoonacular.com/recipes/716429/information?includeNutrition=false'

querystring = {"query":"Pasta Salad"}

headers = {
	"X-RapidAPI-Key": "0aa8b2c149564b51ad1750abc23a1b9a",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

response = requests.get('https://api.spoonacular.com/recipes/716429/information?apiKey=0aa8b2c149564b51ad1750abc23a1b9a&includeNutrition=true')
data = response.json()

# ------------------------------RECIPE MODELS-------------------------------------------
# I want to add a model called "shopping_list" as one to one relationship to Recipe and populate with
# GET https://api.spoonacular.com/mealplanner/dsky/shopping-list" and use just  "aisles" which is a list

def get_ingredients()->object:
	ingredients = data['extendedIngredients']
	for ingredient in ingredients:
		name = ingredient['name']
		unit = ingredient['unit']
		amount = ingredient['amount']
		ingredient = Ingredient.objects.get_or_create(name = name, unit = unit, amount = amount)
	return print(ingredient)

# -------------------------------RECIPE FIELDS------------------------------------------
# THOSE ARE WORKING:
# recipe_title = data['title']
# recipe_image = data['image']
# recipe_description = data['summary']
# recipe_servings = data['servings']
# recipe_prep_time = data['readyInMinutes']
# gluten_free = data['glutenFree'] 
# vegan = data['vegan'] 
# veggie = data['vegetarian'] 
# very_healthy = data['veryHealthy']     
# recipe_type = data['dishTypes'] 
# recipe_cusine = data['cuisines']  
# recipe_occasion = data['occasions'] 

# GET https://api.spoonacular.com/recipes/324694/analyzedInstructions
# I need 'number' and 'step' inside "recipe_instructions"
# recipe_instructions = data['instructions']

# GET https://api.spoonacular.com/recipes/{id}/nutritionWidget.json
	# where the {id} will be i
# recipe_calories = data['calories'] 
# recipe_carbs = data['carbs']
# recipe_fat = data['fat']
# recipe_protein = data['protein']



# print(recipe_calories, recipe_carbs, recipe_fat, recipe_protein)

# ----------------------------------------------POPULATE FUNCTION --------------------------------------------
# I am not sure how to use the get random recipes:
# you might want to consider using the complex recipe search endpoint and set the sort request parameter to random.

# GET https://api.spoonacular.com/recipes/random

# def populate_database():
# 	for i in range(1, 500):
		
