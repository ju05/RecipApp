from django import forms
from .models import Recipe, UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'