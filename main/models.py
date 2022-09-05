from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save

# -------------------------------------RECIPES MODELS-----------------------------------
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField(null = True, blank = True)
    unit = models.CharField(max_length=50, null = True, blank = True)


class Recipe(models.Model):
    title = models.CharField(max_length=200)    
    image = models.CharField(max_length=400)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    instructions = models.TextField()
    servings = models.CharField(max_length=5)
    prep_time = models.CharField(max_length=5)
    calories = models.IntegerField( blank=True)
    carbs = models.FloatField(blank=True)
    fat = models.FloatField(blank=True)
    protein = models.FloatField(blank=True)
    gluten_free = models.BooleanField(null = True)
    vegan = models.BooleanField(null = True)
    vegetarian = models.BooleanField(null = True)
    very_healthy = vegetarian = models.BooleanField(null = True)    
    type = ArrayField(ArrayField(models.CharField(max_length=50, blank=True)))
    cusine = type = ArrayField(ArrayField(models.CharField(max_length=50, blank=True)))
    occasion = type = ArrayField(ArrayField(models.CharField(max_length=50, blank=True)))

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("detail", kwargs={
            "id":self.id,
        })

# ------------------------------------------------PROFILE MODELS--------------------
class UserProfile(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    profile_picture = models.URLField(null = True)
    cover_picture = models.URLField(null = True)
    about = models.CharField(max_length=200, null=True)
    level = models.CharField(max_length=200, null=True)
    interested_type = models.CharField(max_length=200, null=True)
    interested_cuisine = models.CharField(max_length=200, null=True)       
    city = models.CharField(max_length=100, null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    def full_name(self)->str:
        return self.first_name + ' ' + self.last_name
        
def post_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.is_staff:
            UserProfile.objects.create(user_id = instance.id)     

post_save.connect(receiver=post_profile_create, sender=User)


