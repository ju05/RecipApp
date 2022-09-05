import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RecipApp.settings')
import django
django.setup()
import requests

from main.models import Ingredient, Recipe
# from main.recipes.ingredients_list import ingredients_list

# def populate_ingredient():
#     for category, ingredients in ingredients_list.items():
#         print(f'ADDING {category}')
#         for ingredient in ingredients:
#             print(f'ADDING {ingredient}')
#             Ingredient.objects.create(type = category, name = ingredient)




url = 'https://api.spoonacular.com/recipes/716429/information?includeNutrition=false'

querystring = {"query":"Pasta Salad"}

headers = {
	"X-RapidAPI-Key": "0aa8b2c149564b51ad1750abc23a1b9a",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

response = requests.get('https://api.spoonacular.com/recipes/716429/information?apiKey=0aa8b2c149564b51ad1750abc23a1b9a&includeNutrition=true')
data = response.json()

# ------------------------------RECIPE MODELS-------------------------------------------
ingredient = data['extendedIngredients']

# for ingredient in ingredient:
#     name = ingredient['name']
#     unit = ingredient['unit']
#     amount = ingredient['amount']
#     ingredient = Ingredient.objects.get_or_create(name = name, unit = unit, amount = amount)

# -------------------------------RECIPE FIELDS------------------------------------------
recipe_title = data['title']
recipe_image = data['image']
recipe_description = data['productMatches']
recipe_instructions = data['instructions']
recipe_servings = data['servings']
recipe_prep_time = data['readyInMinutes']



print(recipe_title)

#     title = models.CharField(max_length=200)    
#     image = models.CharField(max_length=400)
#     description = models.TextField()
#     ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
#     instructions = models.TextField()
#     servings = models.CharField(max_length=5)
#     prep_time = models.CharField(max_length=5)
#     calories = models.IntegerField( blank=True)
#     carbs = models.FloatField(blank=True)
#     fat = models.FloatField(blank=True)
#     protein = models.FloatField(blank=True)
#     type = models.ManyToManyField(Type, related_name='type')
#     level = models.ForeignKey(Level, on_delete=models.CASCADE)
#     meal = models.ManyToManyField(Meal,related_name='recipes', blank=True)
#     cusine = models.ManyToManyField(Cuisine, related_name='recipes',blank=True)
#     course = models.ManyToManyField(Course, related_name='recipes',blank=True)
#     holiday_seasonal = models.ManyToManyField(HolidaysSeasonal, related_name='recipes',blank=True)
#     occasion = models.ManyToManyField(Occasion, related_name='recipes',blank=True)



# for i in range(1, 500):
