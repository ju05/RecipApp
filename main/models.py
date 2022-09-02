from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save

# -------------------------------------RECIPES MODELS-----------------------------------
class Type(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Level(models.Model):
    title = models.CharField(max_length=200)    

    def __str__(self):
        return self.title

class Meal(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Cusine(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class HolidaysSeasonal(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

class Occasion(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=200)    
    image = models.CharField(max_length=400)
    description = models.TextField()
    ingredients = ArrayField(models.CharField(max_length=50))
    instructions = models.TextField()
    servings = models.CharField(max_length=5)
    prep_time = models.CharField(max_length=5)
    calories = models.IntegerField( blank=True)
    carbs = models.FloatField(blank=True)
    fat = models.FloatField(blank=True)
    protein = models.FloatField(blank=True)
    type = models.ManyToManyField(Type, related_name='type')
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    meal = models.ManyToManyField(Meal,related_name='recipes', blank=True)
    cusine = models.ManyToManyField(Cusine, related_name='recipes',blank=True)
    course = models.ManyToManyField(Course, related_name='recipes',blank=True)
    holiday_seasonal = models.ManyToManyField(HolidaysSeasonal, related_name='recipes',blank=True)
    occasion = models.ManyToManyField(Occasion, related_name='recipes',blank=True)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("detail", kwargs={
            "id":self.id,
        })

# ------------------------------------------------PROFILE MODELS--------------------
class UserProfile(models.Model):
    hobbies = models.CharField(max_length=200, null=True)
    image = models.URLField(null = True)
    address = models.CharField(max_length=100, null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
        
def post_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.is_staff:
            UserProfile.objects.create(user_id = instance.id)
      

post_save.connect(receiver=post_profile_create, sender=User)