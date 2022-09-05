import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

querystring = {"query":"Pasta Salad"}

headers = {
	"X-RapidAPI-Key": "6167f5d90cmsh0c56ee811602330p16fda4jsn0734c17630c0",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())
