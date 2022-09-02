from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from main.models import Type, Level, Meal, Cusine,Course,HolidaysSeasonal,Occasion, Recipe, UserProfile
from .forms import ProfileForm
from django.db.models import Q
from django.db.models import OuterRef, Subquery
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    total_recipes = Recipe.objects.all().count()
    types = Type.objects.all()
    levels = Level.objects.all()
    meals = Meal.objects.all()
    cuisines = Cusine.objects.all()
    courses = Course.objects.all()
    holidays = HolidaysSeasonal.objects.all()
    occasions = Occasion.objects.all()
    context = {
        'title':'Homepage',
        'total_recipes': total_recipes,
        'types': types,
        'levels': levels,
        'meals': meals,
        'cuisines':cuisines,
        'courses':courses,
        'holidays': holidays,
        'occasions': occasions
    }    
    return render(request, 'home.html', context)

# ------------------------------------PROFILE FUNCTIONS--------------------------------
def update_profile(request):
    
    profile = request.user.userprofile
    form = ProfileForm(request.POST or None, instance=profile)
    context = {'form': form} 

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'update_profile.html', context)


def profile(request):

    user = request.user
    profile = user.userprofile     
    context = {'profile': profile}

    return render(request, 'profile.html', context)

# ---------------------------------- SEARCH BAR ----------------------------------------

def search(request):    
    recipes = Recipe.objects.all()    
    if request.method == 'GET':
        query = request.GET.get('search') 
        queryset = recipes.filter(Q(title__icontains=query))       
        results = recipes.filter(Q(title__icontains=query))
        results = recipes.filter(Q(description__icontains=query))
        results = recipes.filter(Q(ingredients__icontains=query))
        results = recipes.filter(Q(instructions__icontains=query))
        total = results.count() 
    if request.GET.get("Meal"):
        results = queryset.filter(Q(meal__title__icontains="breakfast"))
        topic = "breakfast" 
        print(request.POST)    
  
    # if request.GET.get("meal"):
    #     results = queryset.filter(Q(meal__title__icontains="breakfast"))
    #     topic = "meal"

    # if request.method == 'GET':
    #     query = request.GET.get('search')
    #     meal = Meal.objects.filter(title = query)        
    #     results = Recipe.objects.filter(Q(meal__in = Subquery(meal.values('title'))))
    context = {'query': query, 'results': results, 'total':total}
    return render(request, 'search.html', context)

def detail(request, id):    
    recipe = Recipe.objects.filter(id = id)[0]   
    
    context = {'recipe':recipe}
    return render(request, 'detail.html', context)


