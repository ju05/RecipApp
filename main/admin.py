from django.contrib import admin
from .models import Type, Level, Meal, Cusine, Course, HolidaysSeasonal, Occasion, Recipe, UserProfile

# Register your models here.
admin.site.register(Type)
admin.site.register(Level)
admin.site.register(Meal)
admin.site.register(Cusine)
admin.site.register(Course)
admin.site.register(HolidaysSeasonal)
admin.site.register(Occasion)
admin.site.register(Recipe)
admin.site.register(UserProfile)

